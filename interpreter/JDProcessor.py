from antlr4 import InputStream, CommonTokenStream
from parse.HireLexer import HireLexer
from parse.HireParser import HireParser
from parse.HireProcessor import HireProcessor
from pprint import pprint


class JDProcessor:
    def __init__(self, inputString):
        self.inputString = inputString
        self.jd = {}
        

    def getParsedJD(self):
        input_stream = InputStream(self.inputString)
        lexer = HireLexer(input_stream)
        tokens = CommonTokenStream(lexer)
        parser = HireParser(tokens)
        tree = parser.program()

        validator = HireProcessor()
        self.jd = validator.visit(tree)

        return self.jd

    def printParsedJD(self):
        pprint(self.jd, indent=2, width=100, sort_dicts=False)


 