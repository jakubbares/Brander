class TextFileWriter:
    def __init__(self, file_path: str):
        self.file = open(file_path, "w")

    def write_line(self, line):
        self.file.write(line+"\n")

    def write_lines(self, lines):
        for line in lines:
            self.file.write(f"{line}\n")
