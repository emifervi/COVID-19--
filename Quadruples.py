from antlr4 import *
from enum import IntEnum
from DirFunc import DirFunc
from Memory import *
from Utilities import Type, Operator, cleanString
from SemanticCube import semantic_cube
from antlr.CovidListener import CovidListener
from antlr.CovidParser import CovidParser

class Quadruple:
    def __init__(self, oper, res, op1, op2=None):
        self.oper = oper
        self.op1 = op1
        self.op2 = op2
        self.res = res

    def __repr__(self):
        return f'({self.oper.name}, {self.op1}, {self.op2}, {self.res})\n'

class QuadrupleList(CovidListener):
    quad_list = []
    operand_stack = []
    operator_stack = []
    jump_stack = []
    curr_scope = ""
    call_scope = ""
    quad_counter = 0
    k = 0

    def __init__(self, dir_func):
        self.func_table = dir_func.func_table
        self.cte_address_dir = dir_func.cte_address_dir

        self.createQuadruple(Quadruple(Operator.GOTO,None,None,None))

    def changeFuncContext(self, func_name):
        """
        Updates runtime scope
        """
        self.curr_scope = func_name

        self.func_table[func_name].first_quad = self.quad_counter

    def enterFunc(self, ctx):
        self.changeFuncContext(ctx.ID().getText())

    def enterMain(self, ctx):
        self.changeFuncContext("main")
        self.quad_list[0].res = self.quad_counter

    def exitFunc(self, ctx):
        self.createQuadruple(Quadruple(Operator.ENDPROC,None,None,None))

    def exitMain(self, ctx):
        self.createQuadruple(Quadruple(Operator.END,None,None,None))

    def enterArgs(self, ctx):
        self.k = 0

    def exitArgs(self, ctx):
        if len(self.func_table[self.call_scope].param_types) != self.k:
            print("Error: Number of arguments does not coincide with number of parameters")
    
    def addOperandToStack(self, var_id):
        """
        Checks if the variable exists and adds the operand to the stack
        base on the scope
        """
        local_table = self.func_table[self.curr_scope].var_table
        global_table = self.func_table["global"].var_table

        if var_id in local_table:
            self.operand_stack.append((local_table[var_id].address, local_table[var_id].data_type))
        elif var_id in global_table:
            self.operand_stack.append((global_table[var_id].address, global_table[var_id].data_type))
        else:
            print("undeclared variable") # error

    def enterAssignment(self, ctx):
        self.addOperandToStack(ctx.getChild(0).getText())
        self.operator_stack.append(Operator.ASGN)

    def exitAssignment(self, ctx):
        self.parseAsgnQuad()

    def exitIdent(self, ctx):
        if isinstance(ctx.parentCtx, CovidParser.OperandContext):
            self.addOperandToStack(ctx.ID().getText())

        if isinstance(ctx.parentCtx.parentCtx, CovidParser.ReadContext):
            self.operator_stack.append(Operator.INPUT)
            self.addOperandToStack(ctx.ID().getText())
            self.parseReadQuad()

    def exitCte(self, ctx):
        """
        Checks for the existence of constants and adds them
        to the operand stack as needed
        """
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

    def parseAsgnQuad(self):
        """
        Checks the operator stack the asssignment OP
        Creates the cuadruple for assignment
        """
        if not self.operator_stack:
            return

        if self.operator_stack[-1] == Operator.ASGN:

            r_operand, r_type = self.operand_stack.pop()
            l_operand, l_type = self.operand_stack.pop()
            operator = self.operator_stack.pop()

            result_type = semantic_cube[l_type][r_type][operator]

            if result_type != None:
                quad = Quadruple(operator, l_operand, r_operand)
                self.createQuadruple(quad)

                if (r_operand / 1000) == 2:
                    self.func_table[self.curr_scope].address_dir.temp.releaseAddress(r_type, r_operand)

            else:
                print('Error: Type mismatch')

    def parseNotQuad(self):
        if not self.operator_stack:
            return

        if self.operator_stack[-1] == Operator.NOT:
            self.operator_stack.pop()
            operand, data_type = self.operand_stack.pop()

            if data_type == Type.INT:
                result_addr = self.func_table[self.curr_scope].address_dir.addTemp(data_type)

                quad = Quadruple(Operator.NOT, result_addr, operand)
                self.createQuadruple(quad)
                self.operand_stack.append((result_addr, Type.INT))

                if (operand / 1000) == 2:
                    self.func_table[self.curr_scope].address_dir.temp.releaseAddress(data_type, operand)

            else:
                print('Error: Type mismatch')

    def parsePrintQuad(self):
        if not self.operator_stack:
            return

        if self.operator_stack[-1] == Operator.PRINT:
            self.operator_stack.pop()
            operand, data_type = self.operand_stack.pop()

            quad = Quadruple(Operator.PRINT, None, operand)
            self.createQuadruple(quad)

            if (operand / 1000) == 2:
                self.func_table[self.curr_scope].address_dir.temp.releaseAddress(data_type, operand)

    def parseReadQuad(self):
        if not self.operator_stack:
            return

        if self.operator_stack[-1] == Operator.INPUT:
            self.operator_stack.pop()
            operand, _ = self.operand_stack.pop()

            quad = Quadruple(Operator.INPUT, None, operand)
            self.createQuadruple(quad)

    def parseFourTupleQuad(self, operands):
        """
        Checks the operator stack
        Creates the cuadruples as needed
        """
        if not self.operator_stack:
            return

        if self.operator_stack[-1] in operands:

            r_operand, r_type = self.operand_stack.pop()
            l_operand, l_type = self.operand_stack.pop()
            operator = self.operator_stack.pop()

            result_type = semantic_cube[l_type][r_type][operator]

            if result_type != None:
                result_addr = self.func_table[self.curr_scope].address_dir.addTemp(result_type)
                quad = Quadruple(operator, result_addr, l_operand, r_operand)
                self.createQuadruple(quad)
                self.operand_stack.append((result_addr, result_type))

                if (r_operand / 1000) == 2:
                    self.func_table[self.curr_scope].address_dir.temp.releaseAddress(r_type, r_operand)

                if (l_operand / 1000) == 2:
                    self.func_table[self.curr_scope].address_dir.temp.releaseAddress(l_type, l_operand)

            else:
                print('Error: Type mismatch')

    def createGOTOFQuad(self, cond):
        quad = Quadruple(Operator.GOTOF, None, cond, None)
        self.createQuadruple(quad)
        self.jump_stack.append(self.quad_counter - 1)

    def enterExpr(self, ctx):
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
        if ctx.ID():
            self.enterCall(ctx)

        if ctx.NOT():
            self.operator_stack.append(Operator.NOT)

        if ctx.getChild(0).getText() == '(':
            self.operator_stack.append(Operator.FF)

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
        self.addOperandToStack(ctx.ID().getText()) # push iterator to stack for increment
        self.addOperandToStack(ctx.ID().getText()) # push iterator to stack for comparison
        self.addOperandToStack(ctx.ID().getText()) # push iterator to stack for assignment

    def enterCall(self, ctx):
        func_name = ctx.ID().getText()
        self.call_scope = func_name
        if func_name in self.func_table:
            quad = Quadruple(Operator.ERA, None, self.func_table[func_name].address_dir.getSize())
            self.createQuadruple(quad)
        else:
            print("Error: Function not defined")

    def exitRegresa(self, ctx):
        ret, ret_type = self.operand_stack.pop()
        func_type = self.func_table[self.curr_scope].return_type
        
        if semantic_cube[ret_type][func_type][Operator.ASGN]:
            quad = Quadruple(Operator.RETURN, ret, None)
            self.createQuadruple(quad)
        
        else:
            print('Return expression type does not match function type')
    
    def exitCall(self, ctx):
        func_name = ctx.ID().getText()
        address = self.func_table[func_name].first_quad
        quad = Quadruple(Operator.GOSUB, None, func_name, address)
        self.createQuadruple(quad)

    def exitFor_asgn(self, ctx):
        self.operator_stack.append(Operator.ASGN)
        self.parseAsgnQuad()

    def exitExpr(self, ctx):
        # generates quadruple for print operations
        if isinstance(ctx.parentCtx, CovidParser.ImprsContext) or isinstance(ctx.parentCtx, CovidParser.ImprContext):
            self.operator_stack.append(Operator.PRINT)
            self.parsePrintQuad()

        # generates jump on false quadruples for if and while
        if isinstance(ctx.parentCtx, CovidParser.DecisionContext) or isinstance(ctx.parentCtx, CovidParser.While_loopContext):
            cond, cond_type = self.operand_stack.pop()
            if cond_type != Type.INT:
                print("Error: Expected INT type for conditional expression")
            else:
                self.createGOTOFQuad(cond)

        # generates jump on false for 
        if isinstance(ctx.parentCtx, CovidParser.For_loopContext):
            self.operator_stack.append(Operator.LT)
            self.parseFourTupleQuad([Operator.LT])
            
            cond, _ = self.operand_stack.pop()
            self.createGOTOFQuad(cond)
        
        if isinstance(ctx.parentCtx, CovidParser.ArgsContext):
            arg, arg_type = self.operand_stack.pop()
            param_type = self.func_table[self.call_scope].param_types[self.k]

            result_type = semantic_cube[arg_type][param_type][Operator.ASGN]

            if result_type != None:
                quad = Quadruple(Operator.PARAM, f"par{self.k}", arg)
                self.createQuadruple(quad)
                self.k += 1
            else:
                print("Error: Parameter type mismatch")
            
    def exitDecision(self, ctx):
        # Solve either goto from else or gotof from false if
        go_to = self.jump_stack.pop()
        self.quad_list[go_to].res = self.quad_counter

    def exitWhile_loop(self, ctx):
        go_to_false = self.jump_stack.pop()
        loop_go_to = self.jump_stack.pop()

        quad = Quadruple(Operator.GOTO, loop_go_to, None, None)
        self.createQuadruple(quad)

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
        self.parseFourTupleQuad([Operator.OR])

    def exitComp_term(self, ctx):
        self.parseFourTupleQuad([Operator.AND])

    def exitRel_term(self, ctx):
        self.parseFourTupleQuad([Operator.NE, Operator.EQ])

    def exitArtm_term(self, ctx):
        self.parseFourTupleQuad([Operator.LT, Operator.GT, Operator.LTE, Operator.GTE])

    def exitFact_term(self, ctx):
        self.parseFourTupleQuad([Operator.SUM, Operator.SUB])

    def exitOperand(self, ctx):
        if not self.operator_stack:
            return

        if self.operator_stack[-1] == Operator.NOT:
            self.parseNotQuad()

        if not self.operator_stack:
            return

        if self.operator_stack[-1] == Operator.FF and ctx.getText()[-1] == ")":
            self.operator_stack.pop()

            if not self.operator_stack:
                return

            if self.operator_stack[-1] == Operator.NOT:
                self.parseNotQuad()

        self.parseFourTupleQuad([Operator.MULT, Operator.DIV])

        # store result from non-void func in temp
        if ctx.ID():
            func_name = ctx.ID().getText()
            func_type = self.func_table[func_name].return_type
            if func_type != Type.VOID:
                func_address = self.func_table["global"].var_table[func_name].address

                address = self.func_table[func_name].first_quad
                quad = Quadruple(Operator.GOSUB, None, func_name, address)
                self.createQuadruple(quad)

                result_addr = self.func_table[self.curr_scope].address_dir.addTemp(func_type)
                quad = Quadruple(Operator.ASGN, result_addr, func_address)
                self.operand_stack.append((result_addr, func_type))
                self.createQuadruple(quad)

    def createQuadruple(self, quad):
        self.quad_list.append(quad)
        self.quad_counter += 1

    def __repr__(self):
        result_list = ""
        for index, quad in enumerate(self.quad_list):
            result_list += f'{index}.\t{quad}'

        representation = f'Operator Stack:\n{self.operator_stack}\n\nOperand Stack:\n{self.operand_stack}\n\nQuad List:\n{result_list}\n'
        return representation
