from antlr4 import FileStream, CommonTokenStream
from parse.HireLexer import HireLexer
from parse.HireParser import HireParser
from parse.HireProcessor import HireProcessor
from pprint import pprint

input_stream = FileStream("./tests/JD.txt")

lexer = HireLexer(input_stream)
tokens = CommonTokenStream(lexer)
parser = HireParser(tokens)
tree = parser.program()

visitor = HireProcessor()
result = visitor.visit(tree)


print("Processor result:")
pprint(result, indent=2, width=100, sort_dicts=False)