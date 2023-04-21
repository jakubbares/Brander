from common.text_file import TextFileOpener
from parser import SUBTITLES_FILENAME, DATA_DIRECTORY
import os
from collections import defaultdict, Counter
from typing import List, Tuple, Dict, Set
import json
import random
from common.helper import intersection
from parser.hard_scorer import HardScorer
from parser.grammar_index import GrammarSentenceIndex
from parser.vocabulary_loader import VOC_1000_INDICES_FILEPATH

SENTENCE_INDEX_FILENAME = "sentence_index.json"
PROFANITY_FILENAME = "profanity.txt"

class SentenceIndex:
    def __init__(self, spacy, subtitles_file: TextFileOpener, vocabulary_match_mode=False):
        self.vocabulary_match_mode = vocabulary_match_mode
        self.index_filepath = os.path.join(DATA_DIRECTORY, SENTENCE_INDEX_FILENAME)
        self.subtitles_file = subtitles_file
        self.profanity_list = TextFileOpener(os.path.join(DATA_DIRECTORY, PROFANITY_FILENAME), min_length=0, max_length=100).read_in_list(1300)
        self.spacy = spacy
        self.hard_scorer = HardScorer(spacy, subtitles_file)
        self.grammar_index = GrammarSentenceIndex(spacy, subtitles_file)
        self.grammar_index.load_index()

    def load_voc_1000_indices(self):
        self.voc_indices = [int(row) for row in TextFileOpener(VOC_1000_INDICES_FILEPATH).read_in_list(10**8)]

    def get_matching_word_indices(self, words: List[str]) -> List[int]:
        if self.vocabulary_match_mode:
            return self.voc_indices
        matching_indices = []
        for word in words:
            try:
                word_indices = self.index[word.lower()]
                matching_indices.extend(word_indices)
            except:
                print(f"Did not find indices for: {word}")
        return matching_indices

    def search_simple(self, queries: List[str], count=100) -> List[Tuple[str, int]]:
        matching_indices = self.get_matching_word_indices(queries)
        counts = Counter(matching_indices)
        line_indices = [line_index for line_index, count in counts.most_common(count*20)]
        print(f"Found {len(line_indices)} indices")
        lines = self.subtitles_file.get_lines_by_indices(line_indices)
        print(f"Received {len(lines)} lines")
        return self.filter_lines_by_relevance(lines, queries, count)

    def search(self, grammar_types: List[str], queries: List[str], count: int) -> List[Tuple[str, int]]:
        print("Searching for:", queries)
        matching_indices = []
        line_indices_for_grammar_type = [num+1 for num in self.grammar_index.search_indices(grammar_types)] if grammar_types else range(1, 10**8)
        print(f"Loaded {len(line_indices_for_grammar_type)} for grammar types: {grammar_types}")
        #random_examples = random.sample(line_indices_for_grammar_type, k=5)
        #print("For example:")
        #self.subtitles_file.get_lines_by_indices(random_examples)
        for index, word in enumerate(queries):
            line_indices_for_word = self.find_word_in_index(index, word, len(queries))
            print(f"Found indices for: {word}")
            matching_indices.extend(line_indices_for_word)
        if len(grammar_types):
            matching_indices = intersection(matching_indices, line_indices_for_grammar_type)
        random.shuffle(matching_indices)
        counts = Counter(matching_indices)
        line_indices = [line_index for line_index, count in counts.most_common(count)]
        print(f"Found {len(line_indices)} indices")
        lines = self.subtitles_file.get_lines_by_indices(line_indices)
        print(f"Received {len(lines)} lines")
        return self.filter_lines_by_relevance(lines, queries, count)

    def filter_lines_by_relevance(self, lines: List[str], queries: List[str], count: int) -> List[Tuple[str, int]]:
        scored_sentences = []
        result = []
        for sentence, lemmas in self.yield_sentence_properties(lines):
            word_match_score = self.score_words_in_sentence(lemmas, queries)
            sentence_score = self.complete_sentence_score(sentence, word_match_score)
            if sentence not in result:
                scored_sentences.append((sentence, sentence_score))
                result.append(sentence)
        top_sentences = sorted(scored_sentences, key=lambda item: item[1], reverse=True)
        print("Sentence score: ", top_sentences[:count])
        return [(sentence, score) for sentence, score in top_sentences[:count]]

    def yield_sentence_properties(self, lines):
        for line in lines:
            for tokens, sentence in self.spacy.parse_line(text=line):
                lemmas = [token.lemma_ for token in tokens]
                yield sentence, lemmas

    def complete_sentence_score(self, sentence, word_match_score) -> int:
        try:
            tokens = self.spacy.parse(sentence)
            prop_noun_score = len([t for t in tokens if t.pos_ == "PROPN"])
            number_score = len([t for t in tokens if t.pos_ == "NUM"]) ** 2
            comma_score = len([t for t in tokens if t.lemma_ == ","]) * 2
            counts = Counter([t.lemma_ for t in tokens])
            repeats_score = max(counts.values())
            length_score = abs(7 - len(tokens)) + 3
            hard_score, target_voc_score = self.hard_scorer.score_sentence(sentence)
            profanity_score = 1 + (100 * len([t for t in tokens if t.lemma_ in self.profanity_list]))
            voc_match_multiplier = 30 if self.vocabulary_match_mode else 3
            total_score = word_match_score * 10**6 / ((target_voc_score + 3) * voc_match_multiplier) / (repeats_score * 3) / \
                          length_score * 3 / (prop_noun_score + 3) / (number_score + 6) / (comma_score + 5) / profanity_score
            self.report_sentence_score(sentence, total_score=total_score, prop_noun_score=(prop_noun_score + 3), number_score=number_score, comma_score=(comma_score + 5),
                                       word_match_score=(float(word_match_score)),  hard_score=(hard_score + 10),
                                       target_voc_score=((target_voc_score + 3) * voc_match_multiplier),
                                       repeats_score=(repeats_score * 3), length_score=length_score * 3, profanity_score=profanity_score)
            return total_score
        except:
            return 10**99

    def score_words_in_sentence(self, lemmas: List[str], queries: List[str]) -> float:
        if not lemmas:
            return 0
        score = 0
        unique_lemmas = set(lemmas)
        for index, query in enumerate(queries):
            if query in unique_lemmas:
                score += self.score_query_by_index(len(queries), index)
        return float(score) / len(lemmas)

    def score_query_by_index(self, query_count, word_index):
        return (query_count - word_index) * 3

    def find_word_in_index(self, word_index: int, word_lemma: str, query_count: int) -> List[int]:
        try:
            return list(set(self.index[word_lemma.lower()])) * self.score_query_by_index(query_count, word_index)
        except:
            print("Did not find query:", word_lemma)
            return []

    def index_lines(self, num_lines: int) -> None:
        self.index: Dict = defaultdict(lambda: [])
        for line_index, count, line in self.subtitles_file.read(num_lines):
            self.parse_line(line, line_index)
            if count % 50000 == 0:
                print("Saving", line_index)
                self.save_index(line_index)
        self.save_index()

    def parse_line(self, line: str, line_index: int) -> None:
        for tokens, sentence in self.spacy.parse_line(line):
            written_tokens = []
            for token in tokens:
                word_lemma = token.lemma_.lower()
                if token and line_index and word_lemma not in written_tokens:
                    self.index[word_lemma].append(line_index)
                    written_tokens.append(word_lemma)

    def save_index(self, line_index=None):
        self.index_file = open(f"{self.index_filepath}_{line_index}", "w")
        json.dump(self.index, self.index_file)

    def load_index(self):
        index_file = open(self.index_filepath, "r")
        self.index = json.load(index_file)

    def report_sentence_score(self, sentence, **kwargs):
        print({
            "sent": sentence,
            **kwargs
        })
