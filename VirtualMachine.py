import sys
from DirFunc import DirFunc
from Quadruples import Quadruple
from Memory import Memory
from Utilities import Operator, getDataType, Type
from SemanticCube import semantic_cube

import operator

class Cache:
    def __init__(self, quad_pos, ctx, local_mem, temp_mem):
        self.quad_pos = quad_pos
        self.ctx = ctx
        self.local_mem = local_mem
        self.temp_mem = temp_mem

class VirtualMachine:
    
    def __init__(self, func_table, quad_list, cte_mem, global_addr_dir):
        self.func_table = func_table
        self.quad_list = quad_list
        self.cte_mem = cte_mem
        self.context = "main"
        self.quad_pos = 0
        self.memory_stack = []

        #Prepare for context change
        self.next_context = None
        self.next_local_men = None
        self.next_temp_mem = None

        # Init global memory
        self.global_mem = Memory(global_addr_dir)

        # Init main memory and context
        self.context = "main"
        self.local_mem = Memory(self.func_table["main"].address_dir.local)
        self.temp_mem = Memory(self.func_table["main"].address_dir.temp)

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

    def performLogical(self, quad, oper):
        result = 1 if oper(self.resolveMem(quad.op1), self.resolveMem(quad.op2)) else 0
        self.temp_mem.writeAddress(quad.res, result)

    def performAND(self, quad):
        l_operator = True if self.resolveMem(quad.op1) != 0 else False
        r_operator = True if self.resolveMem(quad.op2) != 0 else False
        result = 1 if l_operator and r_operator else 0
        self.temp_mem.writeAddress(quad.res, result)
        
    def performOR(self, quad):
        l_operator = True if self.resolveMem(quad.op1) != 0 else False
        r_operator = True if self.resolveMem(quad.op2) != 0 else False
        result = 1 if l_operator or r_operator else 0
        self.temp_mem.writeAddress(quad.res, result)

    def performNOT(self, quad):
        result = 0 if self.resolveMem(quad.op1) != 0 else 1
        self.temp_mem.writeAddress(quad.res, result)

    def performRead(self, quad):
        addr = quad.op1
        data_type = (addr % 1000) // 100
        val = input()

        if data_type == 0:
            val = int(val)
        elif data_type == 1:
            val = float(val)

        if addr >= 1000:
            self.local_mem.writeAddress(addr, val)
        else:
            self.global_mem.writeAddress(addr, val)

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

    def performGOTO(self, quad, cond = None):        
        if cond == None:
            self.quad_pos = quad.res

        else:
            op = True if self.resolveMem(quad.op1) != 0 else False
            if cond == op:
                self.quad_pos = quad.res
            else:
                self.quad_pos += 1

    def performINCR(self, quad):
        addr = quad.op1
        val = self.resolveMem(addr) + 1
        
        if addr >= 1000:
            self.local_mem.writeAddress(addr, val)
        else:
            self.global_mem.writeAddress(addr, val)
    
    def cleanNextContext(self):
        self.next_local_mem = None
        self.next_temp_mem = None
        self.next_context = None

    def performERA(self, quad):
        self.next_context = quad.op1
        self.next_local_mem = Memory(self.func_table[quad.op1].address_dir.local)
        self.next_temp_mem = Memory(self.func_table[quad.op1].address_dir.temp)

    def performPARAM(self, quad):
        from_address = quad.op1
        from_type = getDataType(from_address)

        param_num = int(quad.res[3:])
        dest_addr, dest_type = self.func_table[self.next_context].params[param_num]

        if from_address >= 2000:
            val = self.temp_mem.getValue(from_address)
        elif from_address >= 1000:
            val = self.local_mem.getValue(from_address)
        else:
            val = self.global_mem.getValue(from_address)

        result_type = semantic_cube[dest_type][from_type][Operator.ASGN]

        if result_type != None:
            if result_type == Type.INT:
                val = int(val)
            elif result_type == Type.FLOAT:
                val = float(val)

            self.next_local_mem.writeAddress(dest_addr, val)
        else:
            print("Error: Argument type does not match parameter type")
            sys.exit()

    def performGOSUB(self, quad):
        self.memory_stack.append(Cache(self.quad_pos + 1, self.context, self.local_mem, self.temp_mem))

        self.context = self.next_context
        self.local_mem = self.next_local_mem
        self.temp_mem = self.next_temp_mem

        self.quad_pos = quad.op2
        self.cleanNextContext()

    def performRETURN(self, quad):
        asgn_quad = Quadruple(Operator.ASGN, self.func_table["global"].var_table[self.context].address, quad.res)
        self.performASGN(asgn_quad)

    def performENDPROC(self):
        cache = self.memory_stack.pop()
        
        self.quad_pos = cache.quad_pos
        self.context = cache.ctx
        self.local_mem = cache.local_mem
        self.temp_mem = cache.temp_mem

    def run(self):
        while self.quad_pos < len(self.quad_list):
            quad = self.quad_list[self.quad_pos]
            # print(f"current quad {self.quad_pos}")
            # input("Press enter to continue")

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
                # Solves new lines and tabs to simulate escaped sequences
                print(str(self.resolveMem(quad.op1)).replace('\\n','\n').replace('\\t', '\t'), end="")
            elif quad.oper == Operator.INPUT:
                self.performRead(quad)
            elif quad.oper == Operator.GT:
                self.performArithmetic(quad, operator.gt)
            elif quad.oper == Operator.GTE:
                self.performArithmetic(quad, operator.ge)
            elif quad.oper == Operator.LT:
                self.performArithmetic(quad, operator.lt)
            elif quad.oper == Operator.LTE:
                self.performArithmetic(quad, operator.le)
            elif quad.oper == Operator.NE:
                self.performArithmetic(quad, operator.ne)
            elif quad.oper == Operator.EQ:
                self.performArithmetic(quad, operator.eq)
            elif quad.oper == Operator.AND:
                self.performAND(quad)
            elif quad.oper == Operator.OR:
                self.performOR(quad)
            elif quad.oper == Operator.NOT:
                self.performNOT(quad)

            # NonLinear Quads
            elif quad.oper == Operator.INCR:
                self.performINCR(quad)
            elif quad.oper == Operator.GOTO:
                self.performGOTO(quad)
                continue
            elif quad.oper == Operator.GOTOF:
                self.performGOTO(quad, False)
                continue
            elif quad.oper == Operator.GOTOV:
                self.performGOTO(quad, True)
                continue
            elif quad.oper == Operator.ERA:
                self.performERA(quad)
                pass
            elif quad.oper == Operator.PARAM:
                self.performPARAM(quad)
                pass
            elif quad.oper == Operator.GOSUB:
                self.performGOSUB(quad)
                continue
            elif quad.oper == Operator.ENDPROC:
                self.performENDPROC()
                continue
            elif quad.oper == Operator.RETURN:
                self.performRETURN(quad)
            elif quad.oper == Operator.END:
                sys.exit()

            # Undefined
            else:
                print(f"Quad not caught: {quad.oper}")

            self.quad_pos += 1