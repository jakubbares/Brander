from parser import DATA_DIRECTORY
import os
import re
from common.text_file import TextFileOpener

class JSONEditor:
    def __init__(self, file_name):
        self.file_path = os.path.join(DATA_DIRECTORY, file_name)
        self.new_file_path = os.path.join(DATA_DIRECTORY, file_name+"_new")
        self.file = TextFileOpener(self.file_path, min_length=0, max_length=10**999)
        self.write_file = open(self.new_file_path, "w")
        self.append_file = open(self.new_file_path, "a")

    def correct_file(self):
        last_line = None
        for index, count, line in self.file.read():
            if not line:
                break
            line = self.remove_nulls(line)
            self.write_file.write(line)
            last_line = line
        self.correct_line_ending(last_line)


    def remove_nulls(self, line):
        return re.sub("NUL", "", line)

    def correct_line_ending(self, line):
        endings = ["}", "]"]
        tokens_to_append = [0 for i in range(10)]
        for index, token in enumerate(endings):
            if not self.line_ends_with(line, token, -index):
                tokens_to_append[index] = token
        tokens_to_append = ''.join([f"{t}" for t in tokens_to_append if t])
        self.append_file.write(tokens_to_append)

    def line_ends_with(self, line, token, index):
        return line[index] == token


