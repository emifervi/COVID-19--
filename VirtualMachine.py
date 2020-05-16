from DirFunc import DirFunc
from Quadruples import QuadrupleList
from Memory import Memory
from Utilities import Operator

class VirtualMachine:
    
    def __init__(self, func_table, quad_list, cte_mem, global_mem):
        self.func_table = func_table
        self.quad_list = quad_list
        self.cte_mem = cte_mem
        self.global_mem = global_mem

        self.local_mem = None
        self.temp_mem = None

    def resolveMem(self, address):
        if address >= 3000:
            return self.cte_mem.getConstant(address)

    def run(self):
        for quad in self.quad_list:
            #Linear Quads
            if quad.oper == Operator.SUM:
                pass
            elif quad.oper == Operator.SUB:
                pass
            elif quad.oper == Operator.MULT:
                pass
            elif quad.oper == Operator.DIV:
                pass
            elif quad.oper == Operator.ASGN:
                pass
            elif quad.oper == Operator.PRINT:
                # Solves new lines to simulate scaped sequences
                print(self.resolveMem(quad.op1).replace('\\n','\n').replace('\\t', '\t'), end="")
            elif quad.oper == Operator.INPUT:
                pass
            elif quad.oper == Operator.GT:
                pass
            elif quad.oper == Operator.GTE:
                pass
            elif quad.oper == Operator.LT:
                pass
            elif quad.oper == Operator.LTE:
                pass
            elif quad.oper == Operator.NE:
                pass
            elif quad.oper == Operator.EQ:
                pass
            elif quad.oper == Operator.NE:
                pass
            elif quad.oper == Operator.AND:
                pass
            elif quad.oper == Operator.OR:
                pass
            elif quad.oper == Operator.NOT:
                pass

            # NonLinear Quads
            elif quad.oper == Operator.INCR:
                pass
            elif quad.oper == Operator.GOTO:
                pass
            elif quad.oper == Operator.GOTOF:
                pass
            elif quad.oper == Operator.GOTOV:
                pass
            elif quad.oper == Operator.ERA:
                pass
            elif quad.oper == Operator.PARAM:
                pass
            elif quad.oper == Operator.GOSUB:
                pass
            elif quad.oper == Operator.ENDPROC:
                pass
            elif quad.oper == Operator.RETURN:
                pass
            elif quad.oper == Operator.END:
                pass

            # Undefined
            else:
                print(f"Quad not caught: {quad.oper}")