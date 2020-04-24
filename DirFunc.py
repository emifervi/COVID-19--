from antlr4 import *
from enum import IntEnum
from antlr.CovidListener import CovidListener
from antlr.CovidParser import CovidParser

class Type(IntEnum):
    INT = 0
    FLOAT = 1
    CHAR = 2
    STRING = 3
    DATAFRAME = 4
    VOID = 5

    def __repr__(self):
        return f'{self.name}'

class Variable:
    def __init__(self, name = "", data_type = None, address = None):
        self.name = name
        self.data_type = data_type
        self.address = address

    def __repr__(self):
        return f'\t Type: {self.data_type.name} \t Address: {self.address} \n'

class Function:
    def __init__(self, name = "", return_type = None, var_table = {}):
        self.name = name
        self.return_type = return_type
        self.var_table = var_table
    
    def __repr__(self):
        return f'\n Type: {self.return_type.name} \n Vars: \n {self.var_table} \n'

class Memory:
    memory = {
        "global": 0,
        "local": 1000,
        "temp": 2000,
        "const": 3000
    }

    def resetLocal(self):
        self.memory["local"] = 1000

    def getAddressType(self, address):
        if address < 1000:
            return "global"
        elif address < 2000:
            return "local"
        elif address < 3000:
            return "temp"
        else:
            return "const"

    def releaseAddress(self, address):
        return

    def getAddress(self, context):
        if context not in self.memory:
            context = "local"
        
        pointer = self.memory[context]
        self.memory[context] += 1
        return pointer


class DirFunc(CovidListener):
    func_table = {}
    curr_scope = ""
    curr_type = None
    memory = Memory()

    def enterStart(self, ctx):
        self.func_table["global"] = Function("global", Type.VOID, {})
        self.curr_scope = "global"

    def enterMain(self, ctx):
        self.func_table["main"] = Function("main", Type.VOID, {})
        self.curr_scope = "main"
        self.memory.resetLocal()

    def exitTipo(self, ctx):
        self.curr_type = Type[ctx.getText().upper()]

    def exitTipo_atom(self, ctx):
        self.curr_type = Type[ctx.getText().upper()]

    def enterFunc(self, ctx):
        func_name = ctx.ID().getText()
        func_type = Type[ctx.getChild(1).getText().upper()]
        
        self.curr_scope = func_name
        self.memory.resetLocal()

        if not func_name in self.func_table:
            self.func_table[func_name] = Function(func_name, func_type, {})

    def addVariable(self, ctx, index):
        var_name = ctx.ID().getText()
        var_table = self.func_table[self.curr_scope].var_table

        if index >= 0:
            self.curr_type = Type[ctx.getChild(index).getText().upper()]

        if not var_name in var_table:
            var_table[var_name] = Variable(var_name, self.curr_type, self.memory.getAddress(self.curr_scope))

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
