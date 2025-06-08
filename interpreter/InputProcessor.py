from antlr4 import FileStream, CommonTokenStream
from parse.HireXLexer import HireXLexer
from parse.HireXParser import HireXParser
from parse.HireXProcessor import HireXProcessor
from pprint import pprint


class InputProcessor:
    def __init__(self, input_file_path):
        self.input_file_path = input_file_path
        input_stream = FileStream(self.input_file_path)
        lexer = HireXLexer(input_stream)
        tokens = CommonTokenStream(lexer)
        parser = HireXParser(tokens)
        tree = parser.program()
        processor = HireXProcessor()
        self.input_tree = processor.visit(tree)

    def getParsedInput(self):
        return self.input_tree

    def printParsedInput(self):
        pprint(self.input_tree, indent=2, width=100, sort_dicts=False)
