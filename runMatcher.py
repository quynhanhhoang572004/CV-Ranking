import sys, os
import subprocess
import unittest
from antlr4 import *


# Define your variables
DIR = os.path.dirname(__file__)
ANTLR_JAR = 'D:/Software/antlr4-4.9.2-complete.jar'

CPL_Dest = 'parse'
SRC = 'Sample.g4'
TESTS = os.path.join(DIR, './tests')


def printUsage():
    print('python Hello.py gen')
    print('python Hello.py test')


def printBreak():
    print('-----------------------------------------------')


def generateAntlr2Python():
    print('Antlr4 is running...')
    subprocess.run(['java', '-jar', ANTLR_JAR, '-o', CPL_Dest, '-no-listener', '-Dlanguage=Python3', SRC])
    print('Generate successfully')

def runTest():
    print('Running testcases...')
    

    from CompiledFiles.JDMatcherLexer import JDMatcherLexer
    from CompiledFiles.JDMatcherParser import JDMatcherParser
    from antlr4.error.ErrorListener import ErrorListener

    class CustomErrorListener(ErrorListener):
        def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
            print(f"Input rejected: {msg}")
            exit(1)  # Exit the program with an error

    filename = 'ListCV.txt'
    inputFile = os.path.join(DIR, './tests', filename)    

    print('List of token: ')
    lexer = JDMatcherLexer(FileStream(inputFile))        
    tokens = []
    token = lexer.nextToken()
    while token.type != Token.EOF:
        tokens.append(token.text)
        token = lexer.nextToken()
    tokens.append('<EOF>')
    print(','.join(tokens))    

    # test
    input_stream = FileStream(inputFile)
    lexer = JDMatcherLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = JDMatcherParser(stream)
    tree = parser.program()  # Start parsing at the `program` rule

    # Print the parse tree (for debugging)
    print(tree.toStringTree(recog=parser))
    # end of test

    
    # Reset the input stream for parsing and catch the error
    lexer = JDMatcherLexer(FileStream(inputFile))
    token_stream = CommonTokenStream(lexer)

    parser = JDMatcherParser(token_stream)   
    parser.removeErrorListeners()
    parser.addErrorListener(CustomErrorListener())    
    try:
        parser.program()
        print("Input accepted")
    except SystemExit:        
        pass
    
    printBreak()
    print('Run tests completely')

def main(argv):
    print('Complete jar file ANTLR  :  ' + str(ANTLR_JAR))
    print('Length of arguments      :  ' + str(len(argv)))    
    printBreak()

    if len(argv) < 1:
        printUsage()
    elif argv[0] == 'gen':
        generateAntlr2Python()    
    elif argv[0] == 'test':       
        runTest()
    else:
        printUsage()


if __name__ == '__main__':
    main(sys.argv[1:])     
    
    