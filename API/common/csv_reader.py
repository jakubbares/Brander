import csv
import os
from parser import DATA_DIRECTORY
import pandas as pd
class CSVReader:
    def __init__(self, file_name):
        self.read_file = open(os.path.join(DATA_DIRECTORY, file_name), 'r')

    def get_num_lines(self):
        nonempty_lines = [line.strip("\n") for line in self.read_file if line != "\n"]
        return len(nonempty_lines)

