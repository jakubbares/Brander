from sentence_transformers import SentenceTransformer

from data import WIKIPEDIA_EMBEDDINGS_PATH
from library.common.csv_writer import CSVWriter
from library.common.logger import Logger
import pandas as pd
from typing import List

class Embedder:
    def __init__(self, path, iter_k=5000):
        self.logger = Logger("embedder").logger
        self.path = path
        self.iter_k = iter_k
        self.df = pd.DataFrame()

    def encode(self, texts: List[str], index_items: List[str]=[]):
        index_items = index_items if len(index_items) else texts
        model = SentenceTransformer('distilbert-base-nli-stsb-mean-tokens')
        self.logger.info("Embedding texts")
        batch = []
        index_batch = []
        for i, (text, index_item) in enumerate(zip(texts, index_items)):
            index_batch.append(index_item)
            batch.append(text)
            if (i + 1) % self.iter_k == 0:
                vectors = model.encode(batch)
                print("Length of indices", len(index_batch))
                print("Length of vectors", len(vectors))
                self.save_to_file(vectors, index_batch)
                batch = []
                index_batch = []
                print("Did batch number", i)
        vectors = model.encode(batch)
        print("Final save")
        print("Length of indices", len(index_batch))
        print("Length of vectors", len(vectors))
        self.save_to_file(vectors, index_batch)

    def save_to_file(self, vectors, index_items):
        new = pd.DataFrame(vectors, index=index_items)
        if self.df.empty:
            print("Empty")
            self.df = new
        else:
            self.df = self.df.append(new)
        self.df.to_csv(self.path)

    def load_from_file(self):
        return pd.read_csv(self.path, index_col=0)


