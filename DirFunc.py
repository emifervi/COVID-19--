from antlr4 import *
from antlr.CovidListener import CovidListener
from antlr.CovidParser import CovidParser
from Utilities import Type, cleanString
from Memory import *

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
        self.address_dir = FuncAddressDir()
        self.first_quad = 0
        self.param_types = []

    def __repr__(self):
        return f'\n Type: {self.return_type.name} \n Vars: \n {self.var_table} \n Chunk: \n {self.address_dir} \n Param Types: \n\t {self.param_types}\n'

class DirFunc(CovidListener):
    func_table = {}
    curr_scope = ""
    curr_type = None

    constants = []

    global_address_dir = GlobalAddressDir()
    cte_address_dir = CteMemory()

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

            if func_type != Type.VOID:
                func_address = self.global_address_dir.getAddress(func_type)
                self.func_table["global"].var_table[func_name] = Variable(func_name, func_type, func_address)

    def addVariable(self, ctx, index):
        var_name = ctx.ID().getText()
        var_table = self.func_table[self.curr_scope].var_table

        # Is a parameter
        if index >= 0:
            self.curr_type = Type[ctx.getChild(index).getText().upper()]
            self.func_table[self.curr_scope].param_types.append(self.curr_type)

        if not var_name in var_table:
            if self.curr_scope == "global":
                address = self.global_address_dir.getAddress(self.curr_type)
            else:
                address = self.func_table[self.curr_scope].address_dir.addLocal(self.curr_type)
            
            var_table[var_name] = Variable(var_name, self.curr_type, address)

    def exitIdent(self, ctx):
        if isinstance(ctx.parentCtx.parentCtx, CovidParser.Var_blockContext):
            self.addVariable(ctx, -1)

    def enterParams(self, ctx):
        self.addVariable(ctx, 0)

    def enterParam(self, ctx):
        if ctx.getChildCount() != 0:
            self.addVariable(ctx, 1)

    def exitCte(self, ctx):
        ctx_text = ctx.getText()

        if ctx_text in self.constants:
            return

        if ctx.INT_CTE() != None:
            self.cte_address_dir.addConstant(Type.INT, ctx_text)
            self.constants.append(ctx_text)
        elif ctx.FLOAT_CTE() != None:
            self.cte_address_dir.addConstant(Type.FLOAT, ctx_text)
            self.constants.append(ctx_text)
        elif ctx.CHAR_CTE() != None:
            self.cte_address_dir.addConstant(Type.CHAR, cleanString(ctx_text))
            self.constants.append(ctx_text)
        elif ctx.STRING_CTE() != None:
            self.cte_address_dir.addConstant(Type.STRING, cleanString(ctx_text))
            self.constants.append(ctx_text)

    def __repr__(self):
        return f'{self.func_table}'
