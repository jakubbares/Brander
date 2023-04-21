import csv
import os
from parser import DATA_DIRECTORY

class CSVWriter:
    def __init__(self, file_name):
        self.write_file = open(os.path.join(DATA_DIRECTORY, file_name), 'w')
        self.writer = csv.writer(self.write_file)

    def from_line(self, line):
        self.write_file.write(line+"\n")

    def from_dict_list(self, dict_list):
        for item in dict_list:
            row = [value for value in item.values()]
            self.writer.writerow(row)

    def from_tuple_list(self, tuple_list):
        self.writer.writerows(tuple_list)

    def from_dict(self, item):
        row = [value for value in item.values()]
        self.writer.writerow(row)

    def from_tuple(self, tuple):
        row = tuple
        self.writer.writerow(row)
