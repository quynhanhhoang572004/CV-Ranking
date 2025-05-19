from antlr4 import FileStream, CommonTokenStream
from parse.JDMatcherLexer import JDMatcherLexer
from parse.JDMatcherParser import JDMatcherParser
from parse.JDMatcherValidator import JDMatcherValidator
from pprint import pprint

input_stream = FileStream("./tests/JD.txt")

lexer = JDMatcherLexer(input_stream)
tokens = CommonTokenStream(lexer)
parser = JDMatcherParser(tokens)
tree = parser.program()

visitor = JDMatcherValidator()
result = visitor.visit(tree)


print("Validator result:")
pprint(result, indent=2, width=100, sort_dicts=False)