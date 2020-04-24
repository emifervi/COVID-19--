from antlr4 import *
from enum import IntEnum
from DirFunc import DirFunc, Memory, Type
from SemanticCube import semantic_cube, Operator
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
    curr_scope = ""
    quad_counter = 0

    def __init__(self, dir_func):
        self.func_table = dir_func.func_table
        self.memory = dir_func.memory

    def enterFunc(self, ctx):
        func_name = ctx.ID().getText()
        self.curr_scope = func_name

    def enterMain(self, ctx):
        self.curr_scope = "main"

    def addOperandToStack(self, var_id):
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

    def exitCte(self, ctx):
        if ctx.INT_CTE() != None:
            self.operand_stack.append((self.memory.getAddress("const"), Type.INT))
        elif ctx.FLOAT_CTE() != None:
            self.operand_stack.append((self.memory.getAddress("const"), Type.FLOAT))
        elif ctx.CHAR_CTE() != None:
            self.operand_stack.append((self.memory.getAddress("const"), Type.CHAR))
        elif ctx.STRING_CTE() != None:
            self.operand_stack.append((self.memory.getAddress("const"), Type.STRING))

    def enterArtm_term(self, ctx):
        if ctx.PLUS() != None:
            self.operator_stack.append(Operator.SUM)
        elif ctx.MINUS() != None:
            self.operator_stack.append(Operator.SUB)

    def enterFact_term(self, ctx):
        if ctx.MULT() != None:
            self.operator_stack.append(Operator.MULT)
        elif ctx.DIVIDE() != None:
            self.operator_stack.append(Operator.DIV)

    def enterComp_term(self, ctx):
        if ctx.EQ() != None:
            self.operator_stack.append(Operator.EQ)
        elif ctx.NE() != None:
            self.operator_stack.append(Operator.NE)

    def parseAsgnQuad(self):
        if len(self.operator_stack) == 0:
            return

        if self.operator_stack[-1] == Operator.ASGN:
            r_operand, r_type = self.operand_stack.pop()
            l_operand, l_type = self.operand_stack.pop()
            operator = self.operator_stack.pop()

            result_type = semantic_cube[l_type][r_type][operator]

            if result_type != None:
                quad = Quadruple(operator, l_operand, r_operand)
                self.createQuadruple(quad)

                if self.memory.getAddressType(r_operand) == "temp":
                    self.memory.releaseAddress(r_operand)

            else:
                print('Error: Type mismatch')        


    def parseFourTupleQuad(self, operands):
        if len(self.operator_stack) == 0:
            return

        if self.operator_stack[-1] in operands:
            r_operand, r_type = self.operand_stack.pop()
            l_operand, l_type = self.operand_stack.pop()
            operator = self.operator_stack.pop()

            result_type = semantic_cube[l_type][r_type][operator]

            if result_type != None:
                result_addr = self.memory.getAddress('temp')
                quad = Quadruple(operator, result_addr, l_operand, r_operand)
                self.createQuadruple(quad)
                self.operand_stack.append((result_addr, result_type))

                if self.memory.getAddressType(r_operand) == "temp":
                    self.memory.releaseAddress(r_operand)

                if self.memory.getAddressType(l_operand) == "temp":
                    self.memory.releaseAddress(l_operand)

            else:
                print('Error: Type mismatch')

    def exitFact_terms(self, ctx):
        self.parseFourTupleQuad([Operator.SUM, Operator.SUB])

    def exitOperand(self, ctx):
        self.parseFourTupleQuad([Operator.MULT, Operator.DIV])

    def exitComp_term(self, ctx):
        self.parseFourTupleQuad([Operator.NE, Operator.EQ])
    
    def createQuadruple(self, quad):
        self.quad_list.append(quad)
        self.quad_counter += 1

    def __repr__(self):
        representation = f'Operator Stack:\n{self.operator_stack}\n\nOperand Stack:\n{self.operand_stack}\n\nQuad List:\n{self.quad_list}\n'

        return representation