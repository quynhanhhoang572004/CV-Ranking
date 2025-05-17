from antlr4 import FileStream, CommonTokenStream
from parse.JDLexer import JDLexer
from parse.JDParser import JDParser
from parse.JDValidator import JDValidator
from pprint import pprint

input_stream = FileStream("./tests/ExampleJD.txt")

lexer = JDLexer(input_stream)
tokens = CommonTokenStream(lexer)
parser = JDParser(tokens)
tree = parser.program()

visitor = JDValidator()
result = visitor.visit(tree)


print("Validator result:")
pprint(result, indent=2, width=100, sort_dicts=False)