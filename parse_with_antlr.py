import os
import json
from antlr4 import *
from parse.cv_scanLexer import cv_scanLexer
from parse.cv_scanParser import cv_scanParser
from parse.visitors import MyVisitor


class CVParser:
    def __init__(self, input_folder="outputs", output_file="parsed_sections.json"):
        self.input_folder = input_folder
        self.output_file = output_file
        self.results = []

    def parse_file(self, filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            text = f.read()

        input_stream = InputStream(text)
        lexer = cv_scanLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = cv_scanParser(token_stream)
        tree = parser.document()

        visitor = MyVisitor()
        result = visitor.visit(tree)
        return result

    def run(self):
        for filename in os.listdir(self.input_folder):
            if filename.endswith(".txt"):
                filepath = os.path.join(self.input_folder, filename)
                print(f"▶ Parsing: {filename}")
                try:
                    parsed_data = self.parse_file(filepath)
                    self.results.append({
                        "file": filename,
                        "data": parsed_data
                    })
                except Exception as e:
                    print(f"❌ Lỗi khi parse {filename}: {e}")

        self.save_results()

    def save_results(self):
        with open(self.output_file, "w", encoding="utf-8") as f:
            json.dump(self.results, f, ensure_ascii=False, indent=2)
        print(f"✅ Đã lưu kết quả vào {self.output_file}")


if __name__ == "__main__":
    parser = CVParser()
    parser.run()
