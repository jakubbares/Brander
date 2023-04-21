from spacy import displacy
import spacy
from common.helper import flatten
from spacy.matcher import Matcher
import pandas as pd
from typing import List, Dict, Tuple
import re
pattern_keys = ["TEXT", "LOWER", "LEMMA", "POS", "OP", "IS_DIGIT", "IS_PUNCT"]

class Token:
    def __init__(self, token, label=None, text=None):
        self.lemma_ = text if text else token.lemma_.replace(":", "").strip("-")
        self.text = text if text else token.text.replace(":", "").strip("-")
        self.tag_ = token.tag_
        self.pos_ = token.pos_
        self.dep_ = token.dep_
        self.children = token.children
        self.sent = token.sent
        self.i = token.i
        self.label_ = label

    def __repr__(self):
        return f"{self.dep_}-{self.text}-{self.pos_}-{self.tag_}"

class Spacy:
    def __init__(self, allowed_pos_types: List[str] = []):
        self.allowed_pos_types = allowed_pos_types
        self.model = spacy.load("en_core_web_lg")
        """
        source_nlp = spacy.load("en_core_web_lg")
        self.model = spacy.blank('en')
        self.model.add_pipe('senter', source=source_nlp)
        self.model.add_pipe('parser', source=source_nlp)
        self.model.add_pipe('ner', source=source_nlp)
        self.model.add_pipe('tagger', source=source_nlp)
        self.model.add_pipe('lemmatizer', source=source_nlp, config={'mode':'rule'})
        """

    def parse_line(self, text: str) -> List[Tuple[List[Token], str]]:
        sentences = self.model(text).sents
        return [(self.parse(s.node), self.clean_text(s.text)) for s in sentences]

    def parse_line_with_ents(self, text: str) -> List[Tuple[List[Token], str]]:
        sentences = self.model(text).sents
        return [(self.parse_with_ents(s.node), self.clean_text(s.text)) for s in sentences]

    def parse(self, sentence: str):
        sentence = self.clean_text(sentence)
        self.doc = self.model(sentence)
        return self.doc

    def parse_with_ents(self, sentence) -> List[Token]:
        sentence = self.clean_text(sentence)
        self.doc = self.model(sentence)
        parsed_tokens = []
        found_entities = []
        for token in self.doc:
            parsed_token = Token(token)
            if token.i in self.entity_indices():
                found_entity, entity_label = self.find_entity_by_index(token.i)
                if found_entity in found_entities:
                    continue
                found_entities.append(found_entity)
                parsed_token = Token(token, entity_label, text=found_entity)
            parsed_tokens.append(parsed_token)
        return parsed_tokens

    def entity_indices(self) -> List[int]:
        return flatten([range(entity.start, entity.end) for entity in self.doc.ents])

    def find_entity_by_index(self, token_index) -> Tuple[str, str]:
        for entity in self.doc.ents:
            if token_index in range(entity.start, entity.end):
                return ' '.join([t.lemma_ for t in self.doc[entity.start:entity.end]]), entity.label_

    def parse_for_dataset(self, sentence: str, min_words=6, max_words=12) -> Tuple:
        self.doc = self.model(sentence)
        if self.sentence_passes_filter():
            print(self.doc)
            tokens = self.get_tokens_by_pos_type(min_words=min_words, max_words=max_words)
            print(tokens)
            verb_tense = self.get_verb_tag()
            return tokens, verb_tense
        return [], None

    def parse_for_cooccurrence(self, sentence: str) -> List[List[str]]:
        self.doc = self.model(sentence)
        if self.sentence_passes_filter():
            combinations = self.get_tokens_by_dep()
            return [self.extract_from_tokens(comb) for comb in combinations]
        return [[]]
        #tokens = self.get_tokens_by_pos_type(min_words=2, max_words=100)
        #return [f"{t['lemma']},{t['pos']}" for t in tokens]

    def sentence_passes_filter(self):
        return not any([t for t in self.doc if t.tag_ == ","])

    def extract_from_tokens(self, tokens):
        return [f"{t['lemma']},{t['pos']}" for t in tokens]

    def clean_text(self, text):
        text = re.sub(f"[^\sA-Za-z0-9,.:;?!-_$%&@']+", "", text)
        return text.strip('"').strip("-").strip("\n").strip(" ")

    def get_sentence_type(self):
        #https://towardsdatascience.com/mood-modality-and-dialogue-sentiment-b06cd36eca88
        """imperative
                interrogative
                exclamatory"""

    def get_verb_tag(self) -> str:
        verbs = [token for token in self.doc if token.pos_ == "VERB"]
        if len(verbs):
            analyzed = verbs[0]
            return analyzed.tag_
        return "None"

    def get_verb_tense(self) -> str:
        verbs = [token for token in self.doc if token.pos_ == "VERB"]
        if len(verbs):
            analyzed = verbs[0]
            tense = analyzed.morph.get("Tense")
            return tense[0] if tense else "Any"
        return "Any"

    def get_tokens_by_dep(self) -> List[List[Dict]]:
        objects = [token for token in self.doc if "obj" in token.pos_]
        head_predicates = [token.head for token in objects]
        return [[objects[index], head_predicates[index]] for index in range(len(objects))]

    def get_tokens_by_pos_type(self, min_words=6, max_words=12) -> List[Dict]:
        return [{"lemma": token.lemma_, "pos": token.pos_} for token in self.doc
                if token.pos_ in self.allowed_pos_types] \
            if len(self.doc) >= min_words and len(self.doc) <= max_words \
            else []

    def match(self, pattern_name, pattern, text):
        matcher = Matcher(self.model.vocab)
        matcher.add(pattern_name, None, pattern)
        doc = self.model(text)
        matches = matcher(doc)
        for match_id, start, end in matches:
            matched_span = doc[start:end]
            print(matched_span.text)


    def vectorize(self, query):
        query_vector = self.model(query)[0].vector_norm
        return query_vector

    def create_dataframe(self, words):
        tokens = self.model(" ".join(words))
        dictionary = [{"candidate": token.lemma_, "vector": token.vector_norm} for token in tokens if token.has_vector]
        return pd.DataFrame(dictionary)

    def morphology(self):
        for token in self.doc:
            print(token)
            print(token.morph.to_dict())

    def dependency(self):
        for token in self.doc:
            print(token)
            print(f"Head is {token.head}")
            print(token.dep_)

    def tree(self):
        displacy.serve(self.doc, style='dep')
