from nltk.corpus.reader import wordnet

def process_synset(synset):
    return {
        "name": synset.name(),
        "definition": synset.definition(),
        "lemmas": [lemma.name() for lemma in synset.lemmas()],
    }

def process_synsets(synsets):
    return [process_synset(synset) for synset in synsets]

def path_distance(a, b):
    return wordnet.path_similarity(a, b)

def to_wordnet_pos(spacy_pos):
    wn_pos = spacy_pos[0].lower()
    if wn_pos == "a":
        return ["a", "s"]
    return [wn_pos]

def vector_average(vectors):
    return [float(sum(l))/len(l) for l in zip(*vectors)]
