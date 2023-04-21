import random
from typing import List, Tuple
import linecache

class TextFileOpener:
    def __init__(self, file_path, min_length=1, max_length=200):
        self.min_length = min_length
        self.max_length = max_length
        self.file_path = file_path
        self.open_file()

    def read_and_shuffle(self, num_lines=100) -> Tuple[int, int, str]:
        count = 0
        index = 0
        while True:
            line = self.file.readline()
            index += 1
            line = line.strip("\n")
            line_length = len(line)
            if line_length >= self.min_length and line_length <= self.max_length and random.randint(0, 100) == 0:
                count += 1
                yield index, count, line
            if not line or count >= num_lines:
                break

    def read(self, num_lines=1000) -> Tuple[int, int, str]:
        count = 0
        for index, line in enumerate(self.file):
            line = line.strip("\n")
            if not line or count >= num_lines:
                break
            line_length = len(line)
            if line_length >= self.min_length and line_length <= self.max_length:
                count += 1
                yield index, count, line


    def search(self, query: str, num_lines: int) -> None:
        for index, count, line in self.read(num_lines):
            if query in line:
                print(line)

    def search_multiple(self, queries: List[str], num_lines: int) -> None:
        for index, count, line in self.read(num_lines):
            if all([query in line for query in queries]):
                print(line)

    def get_lines_by_indices(self, query_indices: List[int]) -> List[str]:
        result = []
        for query_index in query_indices:
            line = linecache.getline(self.file_path, query_index).strip()
            result.append(line)
            print(query_index, line)
        return result

    def read_in_list(self, num_lines: int) -> List[str]:
        result = []
        for index, count, line in self.read(num_lines):
            result.append(line)
        return result

    def open_file(self):
        print("Opening file at path:", self.file_path)
        self.file = open(self.file_path, "r")

    def num_lines(self) -> int:
        return len([i for i in enumerate(self.file)])
