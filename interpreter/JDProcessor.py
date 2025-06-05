from antlr4 import FileStream, CommonTokenStream
from parse.HireXLexer import HireXLexer
from parse.HireXParser import HireXParser
from parse.HireXProcessor import HireXProcessor
from pprint import pprint


class JDProcessor:
    def __init__(self, jd_file_path):
        self.jd_file_path = jd_file_path
        self.jd = {}
        

    def getParsedJD(self):
        input_stream = FileStream(self.jd_file_path)
        lexer = HireXLexer(input_stream)
        tokens = CommonTokenStream(lexer)
        parser = HireXParser(tokens)
        tree = parser.program()

        validator = HireXProcessor()
        self.jd = validator.visit(tree)

        return self.jd

    def printParsedJD(self):
        pprint(self.jd, indent=2, width=100, sort_dicts=False)


 