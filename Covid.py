import sys
from antlr4 import *
from antlr.CovidLexer import CovidLexer
from antlr.CovidParser import CovidParser
from DirFunc import DirFunc
 
def main(argv):
    input_stream = FileStream(argv[1])
    lexer = CovidLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CovidParser(stream)
    tree = parser.start()

    dir_func = DirFunc()
    walker = ParseTreeWalker()
    walker.walk(dir_func, tree)

    # print(dir_func)

    if parser.getNumberOfSyntaxErrors() == 0:
        print("Successful compilation!")
 
if __name__ == '__main__':
    main(sys.argv)