from antlr4 import *
from antlr.CovidListener import CovidListener
from antlr.CovidParser import CovidParser
from Utilities import Type, cleanString
from Memory import *

class Variable:
    """
    Internal definition for variable, used to fill var_table
    """
    def __init__(self, name = "", data_type = None, address = None, dims = 0, d1 = None, d2 = None, address_pointer = 0):
        self.name = name
        self.data_type = data_type
        self.address = address
        self.address_pointer = address_pointer
        self.dims = dims
        self.d1 = d1
        self.d2 = d2

    def __repr__(self):
        return f'\tName: {self.name}\t Type: {self.data_type.name} \t Address: {self.address}  \t Dims: {self.dims} \t d1 = {self.d1} \t d2 = {self.d2} \n'

class Function:
    """
    Internal definition for function, used to fill func_table
    """
    def __init__(self, name = "", return_type = None, var_table = {}):
        self.name = name
        self.return_type = return_type
        self.var_table = var_table
        self.address_dir = FuncAddressDir()
        self.first_quad = 0
        self.params = []

    def __repr__(self):
        return f'\n Type: {self.return_type.name} \n Vars: \n {self.var_table} \n Chunk: \n {self.address_dir} \n Param Types: \n\t {self.params}\n'

class DirFunc(CovidListener):
    """
    Used to create the function directory, and variable table, instantiate constant memory
    """
    func_table = {}
    curr_scope = ""
    curr_type = None

    constants = []

    global_address_dir = GlobalAddressDir()
    cte_address_dir = CteMemory()

    dataframe_mem = None
    dataframe_exists = False

    def enterStart(self, ctx):
        # Change context to global and instantiate global func table
        self.func_table["global"] = Function("global", Type.VOID, {})
        self.curr_scope = "global"

    def enterMain(self, ctx):
        # Change context to main and instantiate main table
        self.func_table["main"] = Function("main", Type.VOID, {})
        self.curr_scope = "main"

    def exitTipo(self, ctx):
        self.curr_type = Type[ctx.getText().upper()]

    def exitTipo_atom(self, ctx):
        self.curr_type = Type[ctx.getText().upper()]

    def enterFunc(self, ctx):
        # Get function name and type, update scope
        func_name = ctx.ID().getText()
        func_type = Type[ctx.getChild(1).getText().upper()]

        self.curr_scope = func_name

        # Add function to func_table
        if not func_name in self.func_table:
            self.func_table[func_name] = Function(func_name, func_type, {})

            # Insert function into global table, to store return value
            if func_type != Type.VOID:
                func_address = self.global_address_dir.getAddress(func_type)
                self.func_table["global"].var_table[func_name] = Variable(func_name, func_type, func_address)
        else:
            # Throw error if function is redefined
            print(f"[Error: {ctx.start.line}] Redefinition of function {func_name}")
            sys.exit()

    def addVariable(self, ctx, index):
        var_name = ctx.ID().getText()
        var_table = self.func_table[self.curr_scope].var_table

        d1 = 1
        d2 = 1
        dim = 0
        address_pointer = None

        # Determine if var has dimensions
        if isinstance(ctx, CovidParser.Ident_declContext):
            if ctx.getChildCount() == 4:
                d1 = int(ctx.getChild(2).getText())
                dim = 1
            elif ctx.getChildCount() == 7:
                d1 = int(ctx.getChild(2).getText())
                d2 = int(ctx.getChild(5).getText())
                dim = 2

        d1_str = str(d1)
        d2_str = str(d2)

        # Is a parameter
        if index >= 0:
            self.curr_type = Type[ctx.getChild(index).getText().upper()]

        # Add variable to var_table
        if not var_name in var_table:
            # Choose scope to insert table
            if self.curr_scope == "global":
                address = self.global_address_dir.getAddress(self.curr_type, d1 * d2)
            else:
                address = self.func_table[self.curr_scope].address_dir.addLocal(self.curr_type, d1 * d2)

            # Is a parameter, fill details on func_table for param list
            if index >= 0:
                self.func_table[self.curr_scope].params.append((address, self.curr_type))
            
            # If it has dimensions, gets starting address, appends dimensions to constant memory
            if dim > 0:
                if str(address) not in self.constants:
                    address_pointer = self.cte_address_dir.addConstant(Type.INT, str(address))
                    self.constants.append(str(address))
                else:
                    address_pointer = self.cte_address_dir.address_table[str(address)]

            # Solve address for first dimension
            if d1_str not in self.constants:
                address_d1 = self.cte_address_dir.addConstant(Type.INT, d1_str)
                self.constants.append(d1_str)
            else:
                address_d1 = self.cte_address_dir.address_table[str(d1)]

            # Solve address for second dimension
            if d2_str not in self.constants:
                address_d2 = self.cte_address_dir.addConstant(Type.INT, d2_str)
                self.constants.append(d2_str)
            else:
                address_d2 = self.cte_address_dir.address_table[d2_str]

            var_table[var_name] = Variable(var_name, self.curr_type, address, dim, address_d1, address_d2, address_pointer)
        
        else:
            print(f"[Error: {ctx.start.line}] Redefinition of variable {var_name}")
            sys.exit()

    def exitIdent_decl(self, ctx):
        if self.curr_type == Type.DATAFRAME:
            # Check if a dataframe already exists
            if self.dataframe_exists:
                print(f"[Error: {ctx.start.line}] Only one dataframe allowed per program")
                sys.exit()
            
            # If this is first dataframe, insert it into global table
            df_name = ctx.getText()
            self.func_table["global"].var_table[df_name] = Variable(df_name, Type.DATAFRAME, 900)
            self.dataframe_exists = True
        else:
            # Otherwise add variable to var_table
            self.addVariable(ctx, -1)

    def enterParams(self, ctx):
        # Add param as local variable
        self.addVariable(ctx, 0)

    def enterParam(self, ctx):
        # Add param as local variable
        if ctx.getChildCount() != 0:
            self.addVariable(ctx, 1)

    def exitCte(self, ctx):
        ctx_text = ctx.getText()

        # Do not add constant if it already exists
        if ctx_text in self.constants:
            return

        # Add constant to cte_memory
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
        return f'Func table: \n{self.func_table} \n Global: \n{self.global_address_dir}'
