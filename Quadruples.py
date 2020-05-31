import sys
from Memory import PointerMemory
from antlr4 import *
from enum import IntEnum
from DirFunc import DirFunc
from Utilities import Type, Operator, cleanString
from SemanticCube import semantic_cube
from antlr.CovidListener import CovidListener
from antlr.CovidParser import CovidParser

class Quadruple:
    """
    Class for quadruple. Contains operation, operands and result
    """
    def __init__(self, oper, res, op1, op2=None):
        self.oper = oper
        self.op1 = op1
        self.op2 = op2
        self.res = res

    def __repr__(self):
        return f'({self.oper.name}, {self.op1}, {self.op2}, {self.res})\n'

class QuadrupleList(CovidListener):
    """
    Generates a list of quads for intermediate code repr. and does semantic checks
    """

    quad_list = []
    operand_stack = []
    operator_stack = []
    jump_stack = []
    curr_scope = ""
    call_stack = []
    quad_counter = 0
    k = 0
    has_return = None
    pointer_mem = PointerMemory()

    def __init__(self, dir_func):
        self.func_table = dir_func.func_table
        self.cte_address_dir = dir_func.cte_address_dir

        self.createQuadruple(Quadruple(Operator.GOTO,None,None,None))

    def changeFuncContext(self, func_name):
        # Updates current scope and updates quad counter
        self.curr_scope = func_name

        self.func_table[func_name].first_quad = self.quad_counter

    def enterFunc(self, ctx):
        # Change context and get func type
        self.changeFuncContext(ctx.ID().getText())

        func_type = ctx.getChild(1).getText()

        # Starts flag to check if a function must have a return or not
        if func_type != "void":
            self.has_return = False
        else:
            self.has_return = True

    def enterMain(self, ctx):
        # Change context to main
        self.changeFuncContext("main")
        self.quad_list[0].res = self.quad_counter

    def exitFunc(self, ctx):
        if not self.has_return:
            # No return in non-void func
            print(f"[Error: {ctx.start.line}] Non void function does not have a return statement")
            sys.exit()
        
        self.createQuadruple(Quadruple(Operator.ENDPROC,None,None,None))

    def exitMain(self, ctx):
        # Insert final quad
        self.createQuadruple(Quadruple(Operator.END,None,None,None))

    def enterArgs(self, ctx):
        # Apend fake bottom to operator stack and star the param counter
        self.operator_stack.append(Operator.FF)
        self.k = 0

    def exitArgs(self, ctx):
        # Remove fake bottom when solving arguments
        if len(self.operator_stack) > 0:
            if self.operator_stack[-1] == Operator.FF:
                self.operator_stack.pop()
        
        # Check if number of parameters coincides with the parameter counter
        if len(self.func_table[self.call_stack[-1]].params) != self.k:
            print(f"[Error: {ctx.start.line}] Number of arguments does not coincide with number of parameters in {self.call_stack[-1]}")
            sys.exit()

    def exitAssignment(self, ctx):
        self.parseAsgnQuad(ctx.start.line)

    def addOperandToStack(self, var_name, line_num):
        local_table = self.func_table[self.curr_scope].var_table
        global_table = self.func_table["global"].var_table

        # Check where the variable belongs (global or local)
        if var_name in local_table:
            table = local_table 
        elif var_name in global_table:
            table = global_table
        else:
            print(f"[Error: {line_num}] use of undeclared variable: {var_name}")
            sys.exit()

        # Get relevant data for the var
        dims = table[var_name].dims
        start = table[var_name].address
        address_start = table[var_name].address_pointer
        data_type = table[var_name].data_type
        d1_addr = table[var_name].d1
        d2_addr = table[var_name].d2

        if dims == 1:
            # Get index and throw error if the type is not int
            s1, s1_type = self.operand_stack.pop()

            if s1_type != Type.INT:
                print(f"[Error: {line_num}] Array index is not an int")
                sys.exit()
            
            # Verify that index is within bounds
            ver_quad = Quadruple(Operator.VER, None, s1, d1_addr)
            self.createQuadruple(ver_quad)

            # Obtain pointer and push to operand stack
            pointer = self.pointer_mem.getPointer()

            sum_quad = Quadruple(Operator.SUM, pointer, address_start, s1)
            self.createQuadruple(sum_quad)
            self.operand_stack.append((pointer, data_type))

        elif dims == 2:
            # Get indices
            s2, s2_type = self.operand_stack.pop()
            s1, s1_type = self.operand_stack.pop()
            
            if s1_type != Type.INT or s2_type != Type.INT:
                print(f"[Error: {line_num}] Array index is not an int")
                sys.exit()

            # Verify first index is within bounds
            ver_quad = Quadruple(Operator.VER, None, s1, d1_addr)
            self.createQuadruple(ver_quad)

            # Shift to proper row
            mult_res = self.func_table[self.curr_scope].address_dir.addTemp(Type.INT)
            mult_quad = Quadruple(Operator.MULT, mult_res, s1, d2_addr)
            self.createQuadruple(mult_quad)

            # Verify second index is within bounds
            ver_quad = Quadruple(Operator.VER, None, s2, d2_addr)
            self.createQuadruple(ver_quad)

            # Apply row shift to start of array 
            sum_res = self.func_table[self.curr_scope].address_dir.addTemp(Type.INT)
            sum_quad = Quadruple(Operator.SUM, sum_res, address_start, mult_res)
            self.createQuadruple(sum_quad)

            # Obtain pointer and push to operand stack
            pointer = self.pointer_mem.getPointer()
            sum_quad = Quadruple(Operator.SUM, pointer, sum_res, s2)
            self.createQuadruple(sum_quad)
            self.operand_stack.append((pointer, data_type))

        else:
            self.operand_stack.append((start, data_type))

    def exitIdent(self, ctx):
        # Insert target address in an assignment
        if isinstance(ctx.parentCtx, CovidParser.AssignmentContext):
            self.addOperandToStack(ctx.ID().getText(), ctx.start.line)
            self.operator_stack.append(Operator.ASGN)

        # Append to operant stack if the parent is operand or if parent of parent is a compiler specific func
        if (isinstance(ctx.parentCtx, CovidParser.OperandContext) or
            isinstance(ctx.parentCtx.parentCtx, CovidParser.CovidContext)):
            self.addOperandToStack(ctx.ID().getText(), ctx.start.line)

        # Insert INPUT quad for argument inside input method
        if isinstance(ctx.parentCtx.parentCtx, CovidParser.ReadContext):
            self.operator_stack.append(Operator.INPUT)
            self.addOperandToStack(ctx.ID().getText(), ctx.start.line)
            self.parseReadQuad()

    def exitCte(self, ctx):
        # Checks for the existence of constants and adds them to operand stack

        if ctx.INT_CTE() != None:
            address = self.cte_address_dir.address_table[ctx.getText()]
            self.operand_stack.append((address, Type.INT))
        elif ctx.FLOAT_CTE() != None:
            address = self.cte_address_dir.address_table[ctx.getText()]
            self.operand_stack.append((address, Type.FLOAT))
        elif ctx.CHAR_CTE() != None:
            address = self.cte_address_dir.address_table[cleanString(ctx.getText())]
            self.operand_stack.append((address, Type.CHAR))
        elif ctx.STRING_CTE() != None:
            address = self.cte_address_dir.address_table[cleanString(ctx.getText())]
            self.operand_stack.append((address, Type.STRING))

    def parseAsgnQuad(self, line_num):
        # Checks the operator stack is empty
        if not self.operator_stack:
            return

        if self.operator_stack[-1] == Operator.ASGN:

            # Extract types
            r_operand, r_type = self.operand_stack.pop()
            l_operand, l_type = self.operand_stack.pop()
            operator = self.operator_stack.pop()

            result_type = semantic_cube[l_type][r_type][operator]

            # Check that assignment is compatible
            if result_type != None:
                quad = Quadruple(operator, l_operand, r_operand)
                self.createQuadruple(quad)

                # Check if address must be released (it is temp)
                if (r_operand / 1000) == 2:
                    self.func_table[self.curr_scope].address_dir.temp.releaseAddress(r_type, r_operand)

            else:
                print(f'[Error: {line_num}] Type mismatch')
                sys.exit()

    def parseNotQuad(self, line_num):
        # Check if operator stack is empty
        if not self.operator_stack:
            return

        # Check if operand had a NOT operator
        if self.operator_stack[-1] == Operator.NOT:
            self.operator_stack.pop()
            operand, data_type = self.operand_stack.pop()
            
            # Check operand data type (must be int)
            if data_type == Type.INT:
                result_addr = self.func_table[self.curr_scope].address_dir.addTemp(data_type)

                # Create NOT quad
                quad = Quadruple(Operator.NOT, result_addr, operand)
                self.createQuadruple(quad)
                self.operand_stack.append((result_addr, Type.INT))

                # Check if address must be released (it is temp)
                if (operand / 1000) == 2:
                    self.func_table[self.curr_scope].address_dir.temp.releaseAddress(data_type, operand)

            else:
                print(f'[Error: {line_num}] NOT operand must be an INT')
                sys.exit()

    def parsePrintQuad(self):
        if not self.operator_stack:
            # If empty, void func couldve been used as expr
            return

        # Check if a PRINT quad is pending
        if self.operator_stack[-1] == Operator.PRINT:
            self.operator_stack.pop()
            operand, data_type = self.operand_stack.pop()
            
            # Create PRINT quad
            quad = Quadruple(Operator.PRINT, None, operand)
            self.createQuadruple(quad)
            
            # Check if address must be released (it is temp)
            if (operand / 1000) == 2:
                self.func_table[self.curr_scope].address_dir.temp.releaseAddress(data_type, operand)

    def parseReadQuad(self):
        # Check if operator stack is empty
        if not self.operator_stack:
            return

        # Check if there is an INPUT quad pending
        if self.operator_stack[-1] == Operator.INPUT:
            self.operator_stack.pop()
            operand, _ = self.operand_stack.pop()

            quad = Quadruple(Operator.INPUT, None, operand)
            self.createQuadruple(quad)

    def parseFourTupleQuad(self, operands, line_num):
        # Parse most four tuple quads
        
        if not self.operator_stack:
            return

        if self.operator_stack[-1] in operands:

            r_operand, r_type = self.operand_stack.pop()
            l_operand, l_type = self.operand_stack.pop()
            operator = self.operator_stack.pop()
            
            # Verify semantics for both types of operands with a given operator
            result_type = semantic_cube[l_type][r_type][operator]

            if result_type != None:
                result_addr = self.func_table[self.curr_scope].address_dir.addTemp(result_type)
                # Create respective quad
                quad = Quadruple(operator, result_addr, l_operand, r_operand)
                self.createQuadruple(quad)
                self.operand_stack.append((result_addr, result_type))

                # Check if addresses must be released (if temp)
                if (r_operand / 1000) == 2:
                    self.func_table[self.curr_scope].address_dir.temp.releaseAddress(r_type, r_operand)
                if (l_operand / 1000) == 2:
                    self.func_table[self.curr_scope].address_dir.temp.releaseAddress(l_type, l_operand)

            else:
                print(f'[Error: {line_num}] Type mismatch')
                sys.exit()

    def createGOTOFQuad(self, cond):
        quad = Quadruple(Operator.GOTOF, None, cond, None)
        self.createQuadruple(quad)
        self.jump_stack.append(self.quad_counter - 1)

    def enterExpr(self, ctx):
        # Store jump to evaluate upper limit in a for loop
        if isinstance(ctx.parentCtx, CovidParser.For_loopContext):
            self.jump_stack.append(self.quad_counter) 

    def enterExprs(self, ctx):
        if ctx.OR() != None:
            self.operator_stack.append(Operator.OR)

    def enterAnd_terms(self, ctx):
        if ctx.AND() != None:
            self.operator_stack.append(Operator.AND)

    def enterComp_op(self, ctx):
        if ctx.EQ() != None:
            self.operator_stack.append(Operator.EQ)
        elif ctx.NE() != None:
            self.operator_stack.append(Operator.NE)

    def enterRel_op(self, ctx):
        if ctx.GT() != None:
            self.operator_stack.append(Operator.GT)
        elif ctx.LT() != None:
            self.operator_stack.append(Operator.LT)
        elif ctx.GTE() != None:
            self.operator_stack.append(Operator.GTE)
        elif ctx.LTE() != None:
            self.operator_stack.append(Operator.LTE)

    def enterArtm_terms(self, ctx):
        if ctx.PLUS() != None:
            self.operator_stack.append(Operator.SUM)
        elif ctx.MINUS() != None:
            self.operator_stack.append(Operator.SUB)

    def enterFact_terms(self, ctx):
        if ctx.MULT() != None:
            self.operator_stack.append(Operator.MULT)
        elif ctx.DIVIDE() != None:
            self.operator_stack.append(Operator.DIV)

    def enterOperand(self, ctx):
        if ctx.NOT():
            self.operator_stack.append(Operator.NOT)

        # Check if nested operation, adds fake bottom to operator stack
        if ctx.getChild(0).getText() == '(':
            self.operator_stack.append(Operator.FF)

        # Check if fake bottom must be added for a !(expr) operand
        if ctx.getChildCount() > 1:
            if ctx.getChild(1).getText() == '(' and ctx.getChild(0).getText() == '!':
                self.operator_stack.append(Operator.FF)

    def enterElse_block(self, ctx):
        # Generate goto operation for true if
        quad = Quadruple(Operator.GOTO, None, None, None)
        self.createQuadruple(quad)

        # Obtain position of jump that needs solving (false if) and complete
        go_to_false = self.jump_stack.pop()
        self.quad_list[go_to_false].res = self.quad_counter

        # Append the new goto to the jump stack for future solution
        self.jump_stack.append(self.quad_counter - 1)

    def enterWhile_loop(self, ctx):
        self.jump_stack.append(self.quad_counter) # push counter to stack to solve goto
    
    def enterFor_asgn(self, ctx):
        self.addOperandToStack(ctx.ID().getText(), ctx.start.line) # push iterator to stack for increment
        self.addOperandToStack(ctx.ID().getText(), ctx.start.line) # push iterator to stack for comparison
        self.addOperandToStack(ctx.ID().getText(), ctx.start.line) # push iterator to stack for assignment

    def enterCall(self, ctx):
        # Add call to the call stack
        func_name = ctx.ID().getText()
        self.call_stack.append(func_name)

        # Check if function from call exists
        if func_name in self.func_table:
            quad = Quadruple(Operator.ERA, None, func_name)
            self.createQuadruple(quad)
        else:
            print(f"[Error: {ctx.start.line}] Function {func_name} not defined")
            sys.exit()

    def enterIdent_ind(self, ctx):
        # Add fake bottom to solve array indexing
        self.operator_stack.append(Operator.FF)

    def exitIdent_ind(self, ctx):
        # Pop fake bottom in case of indexing
        if self.operator_stack[-1] == Operator.FF:
            self.operator_stack.pop()

    def exitRegresa(self, ctx):
        # Function does have a return statement
        self.has_return = True
        ret, ret_type = self.operand_stack.pop()
        func_type = self.func_table[self.curr_scope].return_type
        
        # Check semantic cube with a given return, func type and asignment operation
        if semantic_cube[ret_type][func_type][Operator.ASGN] != None:
            quad = Quadruple(Operator.RETURN, ret, None)
            self.createQuadruple(quad)
         
        else:
            # User wrote a return statement inside a void func
            if func_type == Type.VOID:
                print(f'[Error: {ctx.start.line}] Void type functions must not return.')
                sys.exit()
            # Return type does not match the function type
            else:
                print(f'[Error: {ctx.start.line}] Return expression type does not match function type. Must be {func_type.name.lower()}.')
                sys.exit()
    
    def exitCall(self, ctx):
        # Remove from call stack, get func name
        self.call_stack.pop()
        func_name = ctx.ID().getText()

        # Generate GOSUB quad
        address = self.func_table[func_name].first_quad
        quad = Quadruple(Operator.GOSUB, None, func_name, address)
        self.createQuadruple(quad)

        # Store result from non-void func in temp
        func_type = self.func_table[func_name].return_type

        if func_type != Type.VOID:
            # Get address of function and generate asgn quadruple for non void func
            func_address = self.func_table["global"].var_table[func_name].address

            result_addr = self.func_table[self.curr_scope].address_dir.addTemp(func_type)
            quad = Quadruple(Operator.ASGN, result_addr, func_address)
            self.operand_stack.append((result_addr, func_type))
            self.createQuadruple(quad)
        else:
            # Check if void function was used as part of an expression
            if isinstance(ctx.parentCtx, CovidParser.OperandContext):
                print(f"[Error: {ctx.start.line}] Void function does not return value for expression.")
                sys.exit()

    def exitFor_asgn(self, ctx):
        # Instantiate the iterator in a for loop
        self.operator_stack.append(Operator.ASGN)
        self.parseAsgnQuad(ctx.start.line)

    def exitExpr(self, ctx):
        # generates quadruple for print operations
        if isinstance(ctx.parentCtx, CovidParser.ImprsContext) or isinstance(ctx.parentCtx, CovidParser.ImprContext):
            self.operator_stack.append(Operator.PRINT)
            self.parsePrintQuad()

        # generates jump on false quadruples for if and while
        if isinstance(ctx.parentCtx, CovidParser.DecisionContext) or isinstance(ctx.parentCtx, CovidParser.While_loopContext):
            cond, cond_type = self.operand_stack.pop()
            if cond_type != Type.INT:
                print(f"[Error: {ctx.start.line}] Expected int type for conditional expression")
                sys.exit()
            else:
                self.createGOTOFQuad(cond)

        # generates jump on false for 
        if isinstance(ctx.parentCtx, CovidParser.For_loopContext):
            self.operator_stack.append(Operator.LT)
            self.parseFourTupleQuad([Operator.LT], ctx.start.line)
            
            cond, _ = self.operand_stack.pop()
            self.createGOTOFQuad(cond)
        
        if isinstance(ctx.parentCtx, CovidParser.ArgsContext):
            arg, arg_type = self.operand_stack.pop()
            try:
                # Extract param type from incoming call function
                _, param_type = self.func_table[self.call_stack[-1]].params[self.k]
            except:
                # Gave more args than function asked for
                print(f"[Error: {ctx.start.line}] Number of arguments does not coincide with number of parameters in {self.call_stack[-1]}")
                sys.exit()

            # Check for semantic considerations usign semantic cube
            result_type = semantic_cube[arg_type][param_type][Operator.ASGN]

            if result_type != None:
                # Generate cuadruple and update param counter
                quad = Quadruple(Operator.PARAM, f"par{self.k}", arg)
                self.createQuadruple(quad)
                self.k += 1
            else:
                # Argument type does not match param type
                print(f"[Error: {ctx.start.line}] Parameter type mismatch. Expected {param_type.name.lower()}, got {arg_type.name.lower()}.")
                sys.exit()
            
    def exitDecision(self, ctx):
        # Solve either goto from else or gotof from false if
        go_to = self.jump_stack.pop()
        self.quad_list[go_to].res = self.quad_counter

    def exitWhile_loop(self, ctx):
        # Extract jump values from jump stack
        go_to_false = self.jump_stack.pop()
        loop_go_to = self.jump_stack.pop()

        # Create looping behaviour for while loop
        quad = Quadruple(Operator.GOTO, loop_go_to, None, None)
        self.createQuadruple(quad)
        
        # Solve pending gotof from while loop 
        self.quad_list[go_to_false].res = self.quad_counter

    def exitFor_loop(self, ctx):
        # INCR var
        operand, _ = self.operand_stack.pop()
        quad = Quadruple(Operator.INCR, None, operand)
        self.createQuadruple(quad)

        # Create GOTO and solve GOTOF
        go_to_false = self.jump_stack.pop()
        loop_go_to = self.jump_stack.pop()
        quad = Quadruple(Operator.GOTO, loop_go_to, None, None)
        self.createQuadruple(quad)

        self.quad_list[go_to_false].res = self.quad_counter

    def exitAnd_term(self, ctx):
        self.parseFourTupleQuad([Operator.OR], ctx.start.line)

    def exitComp_term(self, ctx):
        self.parseFourTupleQuad([Operator.AND], ctx.start.line)

    def exitRel_term(self, ctx):
        self.parseFourTupleQuad([Operator.NE, Operator.EQ], ctx.start.line)

    def exitArtm_term(self, ctx):
        self.parseFourTupleQuad([Operator.LT, Operator.GT, Operator.LTE, Operator.GTE], ctx.start.line)

    def exitFact_term(self, ctx):
        self.parseFourTupleQuad([Operator.SUM, Operator.SUB], ctx.start.line)

    def exitOperand(self, ctx):
        # Check if operator stack is empty
        if not self.operator_stack:
            return

        # Check if there was a NOT operator
        if self.operator_stack[-1] == Operator.NOT:
            self.parseNotQuad(ctx.start.line)
        
        # if operator stack is empty again
        if not self.operator_stack:
            return

        # Needs to remove a previouly added fake bottom
        if self.operator_stack[-1] == Operator.FF and ctx.getText()[-1] == ")":
            self.operator_stack.pop()
            
            # Check if operator stack is emtpy one last time (no anxiety here)
            if not self.operator_stack:
                return

            if self.operator_stack[-1] == Operator.NOT:
                self.parseNotQuad(ctx.start.line)

        # Parse all remaining operators
        self.parseFourTupleQuad([Operator.MULT, Operator.DIV], ctx.start.line)

    def createQuadruple(self, quad):
        # Add quad to list and increment counter
        self.quad_list.append(quad)
        self.quad_counter += 1

    def exitLoad_file(self, ctx):
        operand, data_type = self.operand_stack.pop()
        
        # Check if file path is a string
        if data_type == Type.STRING:
            quad = Quadruple(Operator.FILE, None, operand)
            self.createQuadruple(quad)
        else:
            # Throw error if is not string
            print(f"[Error: {ctx.start.line}] Argument must be of type string, got {data_type.name.lower()}.")
            sys.exit()
    
    def exitLoad_data(self, ctx):
        # Extract cols, rows, and data frame
        cols, cols_type = self.operand_stack.pop()
        rows, rows_type = self.operand_stack.pop()
        _, df_type = self.operand_stack.pop()

        # Check argument types
        if df_type != Type.DATAFRAME:
            print(f"[Error {ctx.start.line}] load_data() first argument must be of type dataframe, got {df_type.name.lower()}.")
            sys.exit()
        
        if rows_type != Type.INT:
            print(f"[Error {ctx.start.line}] load_data() second argument must be of type int, got {rows_type.name.lower()}.")
            sys.exit()

        if cols_type != Type.INT:
            print(f"[Error {ctx.start.line}] load_data() third argument must be of type int, got {cols_type.name.lower()}.")
            sys.exit()

        quad = Quadruple(Operator.DATA, None, rows, cols)
        self.createQuadruple(quad)

    def parseCovidSimpleQuad(self, oper, name, line_num):
        col, col_type = self.operand_stack.pop()
        _, df_type = self.operand_stack.pop()

        # Check argument types
        if df_type != Type.DATAFRAME:
            print(f"[Error {line_num}] {name}() first argument must be of type dataframe, got {df_type.name.lower()}.")
            sys.exit()
        
        if col_type != Type.STRING:
            print(f"[Error {line_num}] {name}() second argument must be of type string, got {col_type.name.lower()}.")
            sys.exit()

        # Create Simple Quad and store result in temp 
        avg_res = self.func_table[self.curr_scope].address_dir.addTemp(Type.FLOAT)
        quad = Quadruple(oper, avg_res, col)
        self.createQuadruple(quad)
        self.operand_stack.append((avg_res, Type.FLOAT))

    def exitAvg(self, ctx):
        self.parseCovidSimpleQuad(Operator.AVG, "avg", ctx.start.line)

    def exitModa(self, ctx):
        self.parseCovidSimpleQuad(Operator.MODE, "mode", ctx.start.line)

    def exitRango(self, ctx):
        self.parseCovidSimpleQuad(Operator.RANGE, "range", ctx.start.line)

    def exitVariance(self, ctx):
        self.parseCovidSimpleQuad(Operator.VAR, "variance", ctx.start.line)

    def exitStd_dev(self, ctx):
        self.parseCovidSimpleQuad(Operator.STD_DEV, "std_dev", ctx.start.line)

    def exitMaxi(self, ctx):
        self.parseCovidSimpleQuad(Operator.MAX, "max", ctx.start.line)

    def exitMini(self, ctx):
        self.parseCovidSimpleQuad(Operator.MIN, "min", ctx.start.line)

    def parseCovidComplexQuad(self, oper, name, gives_result, line_num):
        # Extract variables to use for quad
        var2, var2_type = self.operand_stack.pop()
        var1, var1_type = self.operand_stack.pop()
        _, df_type = self.operand_stack.pop()

        # Check argument types
        if df_type != Type.DATAFRAME:
            print(f"[Error {line_num}] {name}() first argument must be of type dataframe, got {df_type.name.lower()}")
            sys.exit()
        
        if var1_type != Type.STRING:
            print(f"[Error {line_num}] {name}() second argument must be of type string, got {var1_type.name.lower()}.")
            sys.exit()
        
        if var2_type != Type.STRING:
            print(f"[Error {line_num}] {name}() third argument must be of type string, got {var2_type.name.lower()}.")
            sys.exit()

        # Create Complex Quad and store result in temp 
        if gives_result:
            corr_res = self.func_table[self.curr_scope].address_dir.addTemp(Type.FLOAT)
        else:
            corr_res = None

        quad = Quadruple(oper, corr_res, var1, var2)
        self.createQuadruple(quad)
        
        if gives_result:
            self.operand_stack.append((corr_res, Type.FLOAT))

    def exitCorrel(self, ctx):
        self.parseCovidComplexQuad(Operator.CORREL, "correl", True, ctx.start.line)
    
    def exitPlot(self, ctx):
        self.parseCovidComplexQuad(Operator.PLOT, "plot", False, ctx.start.line)

    def exitHistogram(self, ctx):
        # Extract variables to use for histogram
        bins, bins_type = self.operand_stack.pop()
        col, col_type = self.operand_stack.pop()
        _, df_type = self.operand_stack.pop()

        # Check argument types
        if df_type != Type.DATAFRAME:
            print(f"[Error {ctx.start.line}] histogram() first argument must be of type dataframe, got {df_type.name.lower()}")
            sys.exit()
        
        if col_type != Type.STRING:
            print(f"[Error: {ctx.start.line}] histogram() second argument must be of type string, got {col_type.name.lower()}")
            sys.exit()
        
        if bins_type != Type.INT:
            print(f"[Error {ctx.start.line}] histogram() third argument must be of type int, got {bins_type.name.lower()}")
            sys.exit()

        quad = Quadruple(Operator.HIST, None, col, bins)
        self.createQuadruple(quad)

    def __repr__(self):
        result_list = ""
        for index, quad in enumerate(self.quad_list):
            result_list += f'{index}.\t{quad}'

        representation = f'Operator Stack:\n{self.operator_stack}\n\nOperand Stack:\n{self.operand_stack}\n\nQuad List:\n{result_list}\n'
        return representation
