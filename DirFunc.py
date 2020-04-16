from antlr4 import *
from enum import Enum
from antlr.CovidListener import CovidListener
from antlr.CovidParser import CovidParser

class Type(Enum):
    INT = 0
    FLOAT = 1
    CHAR = 2
    STRING = 3
    DATAFRAME = 4
    VOID = 5

class Variable:
    def __init__(self, name = "", data_type = None, value = None):
        self.name = name
        self.data_type = data_type
        self.value = value

    def __repr__(self):
        return f'\t Type: {self.data_type.name} \t Value: {self.value} \n'

class Function:
    def __init__(self, name = "", return_type = None, var_table = {}):
        self.name = name
        self.return_type = return_type
        self.var_table = var_table
    
    def __repr__(self):
        return f'\n Type: {self.return_type.name} \n Vars: \n {self.var_table} \n'

class DirFunc(CovidListener):
    func_table = {}
    curr_scope = ""
    curr_type = None

    def enterStart(self, ctx):
        self.func_table["global"] = Function("global", Type.VOID, {})
        self.curr_scope = "global"

    def enterMain(self, ctx):
        self.func_table["main"] = Function("main", Type.VOID, {})
        self.curr_scope = "main"

    def exitTipo(self, ctx):
        self.curr_type = Type[ctx.getText().upper()]

    def exitTipo_atom(self, ctx):
        self.curr_type = Type[ctx.getText().upper()]

    def enterFunc(self, ctx):
        func_name = ctx.ID().getText()
        func_type = Type[ctx.getChild(1).getText().upper()]
        
        self.curr_scope = func_name

        if not func_name in self.func_table:
            self.func_table[func_name] = Function(func_name, func_type, {})

    def addVariable(self, ctx, index):
        var_name = ctx.ID().getText()
        var_table = self.func_table[self.curr_scope].var_table

        if index >= 0:
            self.curr_type = Type[ctx.getChild(index).getText().upper()]

        if not var_name in var_table:
            var_table[var_name] = Variable(var_name, self.curr_type)

    def exitIdent(self, ctx):
        if isinstance(ctx.parentCtx.parentCtx, CovidParser.Var_blockContext):
            self.addVariable(ctx, -1)

    def enterParams(self, ctx):
        self.addVariable(ctx, 0)

    def enterParam(self, ctx):
        if ctx.getChildCount() != 0:
            self.addVariable(ctx, 1)
    
    def __repr__(self):
        return f'{self.func_table}'
