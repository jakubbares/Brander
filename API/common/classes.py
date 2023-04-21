import urllib
import html2text

def process_description(text):
    return html2text.html2text(text).replace("\n", " ").replace('*', '').replace("#", "").replace('_', "")

class BertDataset(object):
    def __init__(self, train, test):
        self.train = train
        self.test = test

class Dataset(object):
    def __init__(self, X_train, y_train, X_val, y_val):
        self.X_train = X_train
        self.y_train = y_train
        self.X_val = X_val
        self.y_val = y_val

