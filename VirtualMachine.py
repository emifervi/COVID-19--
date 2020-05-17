from DirFunc import DirFunc
from Quadruples import QuadrupleList
from Memory import Memory
from Utilities import Operator

import operator

class VirtualMachine:
    
    def __init__(self, func_table, quad_list, cte_mem, global_addr_dir):
        self.func_table = func_table
        self.quad_list = quad_list
        self.cte_mem = cte_mem
        self.global_mem = Memory(global_addr_dir)
        self.context = "main"

        self.setContext(self.context)

    def setContext(self, func_name):
        self.local_mem = Memory(self.func_table[func_name].address_dir.local)
        self.temp_mem = Memory(self.func_table[func_name].address_dir.temp)

    def resolveMem(self, address):
        if address >= 3000:
            return self.cte_mem.getConstant(address)
        if address >= 2000:
            return self.temp_mem.getValue(address)
        if address >= 1000:
            return self.local_mem.getValue(address)
        else:
            return self.global_mem.getValue(address)
            
    def performArithmetic(self, quad, oper):
        result = oper(self.resolveMem(quad.op1), self.resolveMem(quad.op2))
        self.temp_mem.writeAddress(quad.res, result)

    def performASGN(self, quad):
        value = self.resolveMem(quad.op1)
        target_addr = quad.res

        data_type_val = (target_addr % 1000) // 100

        if data_type_val == 0:
            value = int(value)
        elif data_type_val == 1:
            value = float(value)

        if target_addr >= 2000:
            self.temp_mem.writeAddress(target_addr, value)
        elif target_addr >= 1000:
            self.local_mem.writeAddress(target_addr, value)
        else:
            self.global_mem.writeAddress(target_addr, value)

    def run(self):
        for quad in self.quad_list:
            #Linear Quads
            if quad.oper == Operator.SUM:
                self.performArithmetic(quad, operator.add)
            elif quad.oper == Operator.SUB:
                self.performArithmetic(quad, operator.sub)
            elif quad.oper == Operator.MULT:
                self.performArithmetic(quad, operator.mul)
            elif quad.oper == Operator.DIV:
                self.performArithmetic(quad, operator.truediv)
            elif quad.oper == Operator.ASGN:
                self.performASGN(quad)
            elif quad.oper == Operator.PRINT:
                # Solves new lines to simulate scaped sequences
                print(str(self.resolveMem(quad.op1)).replace('\\n','\n').replace('\\t', '\t'), end="")
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