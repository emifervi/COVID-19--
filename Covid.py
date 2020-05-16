import sys
from antlr4 import *
from antlr.CovidLexer import CovidLexer
from antlr.CovidParser import CovidParser
from antlr.CovidListener import CovidListener
from DirFunc import DirFunc
from Quadruples import QuadrupleList
from VirtualMachine import VirtualMachine
from antlr4.tree.Trees import Trees

debug = True

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = CovidLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CovidParser(stream)
    tree = parser.start()

    dir_func = DirFunc()
    walker = ParseTreeWalker()
    walker.walk(dir_func, tree)

    quad_list = QuadrupleList(dir_func)
    walker = ParseTreeWalker()
    walker.walk(quad_list, tree)

    virtual_machine = VirtualMachine(
        dir_func.func_table, 
        quad_list.quad_list, 
        quad_list.cte_address_dir,
        dir_func.global_address_dir
    )

    if debug:
        #print(Trees.toStringTree(tree, None, parser))
        #print(dir_func)
        #print(quad_list)
        pass

    if parser.getNumberOfSyntaxErrors() == 0:
        print("Successful compilation!")
        virtual_machine.run()
 
if __name__ == '__main__':
    main(sys.argv)