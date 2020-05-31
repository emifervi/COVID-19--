import sys
from DirFunc import DirFunc
from Quadruples import Quadruple
from Memory import Memory
from Utilities import Operator, getDataType, Type
from SemanticCube import semantic_cube
from os import path
import pandas as pd
import matplotlib.pyplot as plt
import operator

class Cache:
    """
    Stores a context for the ctx_stack (includes, current quad position, name and memory spaces)
    """
    def __init__(self, quad_pos, ctx, local_mem, temp_mem):
        self.quad_pos = quad_pos
        self.ctx = ctx
        self.local_mem = local_mem
        self.temp_mem = temp_mem
    
    def __repr__(self):
        return f'{self.quad_pos} - {self.ctx}'

class VirtualMachine:
    """
    Class simulate virtual machine, is in charge of runtime for the language
    """
    def __init__(self, func_table, quad_list, cte_mem, pointer_mem, global_addr_dir):
        self.func_table = func_table
        self.quad_list = quad_list
        self.cte_mem = cte_mem
        self.ctx_stack = []
        self.call_stack = []
        self.file_path = None
        self.dataframe = None

        # Init global memory
        self.global_mem = Memory(global_addr_dir)

        # Init pointer memory
        self.pointer_mem = pointer_mem

        # Init main memory and context
        local_mem = Memory(self.func_table["main"].address_dir.local)
        temp_mem = Memory(self.func_table["main"].address_dir.temp)
        self.ctx_stack.append(Cache(0, "main", local_mem, temp_mem))

    def performPRINT(self, quad):
        # Solves new lines and tabs to simulate escaped sequences
        print(str(self.resolveMem(quad.op1)).replace('\\n','\n').replace('\\t', '\t'), end="")

    def resolveMem(self, address):
        # Obtains the value by searching in different contexts
        if address >= 4000:
            real_address = self.pointer_mem.getAddress(address)
            return self.resolveMem(real_address)
        if address >= 3000:
            return self.cte_mem.getConstant(address)
        if address >= 2000:
            return self.ctx_stack[-1].temp_mem.getValue(address)
        if address >= 1000:            
            return self.ctx_stack[-1].local_mem.getValue(address)
        else:
            return self.global_mem.getValue(address)
    
    def writeResult(self, address, result):
        # Writes a value by searching in different contexts
        if address >= 4000:
            self.pointer_mem.writePointer(address, result)
        elif address >= 2000:
            self.ctx_stack[-1].temp_mem.writeAddress(address, result)
        elif address >= 1000:
            self.ctx_stack[-1].local_mem.writeAddress(address, result)
        else:
            self.global_mem.writeAddress(address, result)
            
    def performArithmetic(self, quad, oper):
        # Common function for all arithmetic operations
        try:
            result = oper(self.resolveMem(quad.op1), self.resolveMem(quad.op2))
            self.writeResult(quad.res, result)
        except ZeroDivisionError:
            # Throw error if there is a division by zero
            print("[Error] Division by zero")
            sys.exit()

    def performLogical(self, quad, oper):
        # Common function for all rel and eq operations
        result = 1 if oper(self.resolveMem(quad.op1), self.resolveMem(quad.op2)) else 0
        self.writeResult(quad.res, result)

    def performAND(self, quad):
        # If number is 0 -> false, otherwise true
        l_operator = True if self.resolveMem(quad.op1) != 0 else False
        r_operator = True if self.resolveMem(quad.op2) != 0 else False
        result = 1 if l_operator and r_operator else 0
        self.writeResult(quad.res, result)
        
    def performOR(self, quad):
        # If number is 0 -> false, otherwise ture
        l_operator = True if self.resolveMem(quad.op1) != 0 else False
        r_operator = True if self.resolveMem(quad.op2) != 0 else False
        result = 1 if l_operator or r_operator else 0
        self.writeResult(quad.res, result)

    def performNOT(self, quad):
        # Inverts a logical int (0 -> 1)
        result = 0 if self.resolveMem(quad.op1) != 0 else 1
        self.writeResult(quad.res, result)

    def performREAD(self, quad):
        # Reads std input and writes the value
        addr = quad.op1
        val = input()

        # Check if address is a pointer that needs solving, before writing to mem
        if addr >= 4000:
            quad = Quadruple(Operator.ASGN, self.pointer_mem.getAddress(addr), val)
            self.performASGN(quad, True)
            return
        
        # Gets datatype and casts accordingly
        data_type = (addr % 1000) // 100
        
        if data_type == 0:
            val = int(val)
        elif data_type == 1:
            val = float(val)

        # Writes memory
        if addr >= 2000:
            self.ctx_stack[-1].temp_mem.writeAddress(addr, val)
        elif addr >= 1000:
            self.ctx_stack[-1].local_mem.writeAddress(addr, val)
        else:
            self.global_mem.writeAddress(addr, val)

    def performASGN(self, quad, flag = False):
        # If pointer, use op1 as value, otherwise it's an address
        if flag:
            value = quad.op1
        else:
            value = self.resolveMem(quad.op1)
        
        # Solves data type and casts accordingly
        target_addr = quad.res
        data_type_val = (target_addr % 1000) // 100

        if data_type_val == 0:
            value = int(value)
        elif data_type_val == 1:
            value = float(value)

        # Writes to memory
        if target_addr >= 4000:
            quad = Quadruple(Operator.ASGN, self.pointer_mem.getAddress(target_addr), quad.op1)
            self.performASGN(quad)
        elif target_addr >= 2000:
            self.ctx_stack[-1].temp_mem.writeAddress(target_addr, value)
        elif target_addr >= 1000:
            self.ctx_stack[-1].local_mem.writeAddress(target_addr, value)
        else:
            self.global_mem.writeAddress(target_addr, value)

    def performGOTO(self, quad, cond = None):
        # Change quad position unconditionally (GOTO)    
        if cond == None:
            self.ctx_stack[-1].quad_pos = quad.res

        else:
            # Only change based on condition
            op = True if self.resolveMem(quad.op1) != 0 else False
            if cond == op:
                self.ctx_stack[-1].quad_pos = quad.res
            else:
                self.ctx_stack[-1].quad_pos += 1

    def performINCR(self, quad):
        # Solves address and updates the increment value, writes value to memory
        addr = quad.op1
        val = self.resolveMem(addr) + 1
        
        if addr >= 1000:
            self.ctx_stack[-1].local_mem.writeAddress(addr, val)
        else:
            self.global_mem.writeAddress(addr, val)

    def performERA(self, quad):
        # Instantiate memory of next context and appends it to the call stack
        next_local_mem = Memory(self.func_table[quad.op1].address_dir.local)
        next_temp_mem = Memory(self.func_table[quad.op1].address_dir.temp)
        next_context = quad.op1
        self.call_stack.append(Cache(None, next_context, next_local_mem, next_temp_mem))

    def performPARAM(self, quad):
        # Writes a value for a parameter, given an argument
        from_address = quad.op1

        # Out of bounds (deprecated, but won't touch)
        if from_address >= 5000:
            return
        
        # Get the type of the argument, param number and param data
        from_type = getDataType(from_address)

        param_num = int(quad.res[3:])
        dest_addr, dest_type = self.func_table[self.call_stack[-1].ctx].params[param_num]

        # Get value of parameter
        if from_address >= 4000:
            quad = Quadruple(Operator.PARAM, quad.res, self.pointer_mem.getAddress(from_address))
            self.performPARAM(quad)
            return
        elif from_address >= 3000:
            val = self.cte_mem.getConstant(from_address)
        elif from_address >= 2000:
            val = self.ctx_stack[-1].temp_mem.getValue(from_address)
        elif from_address >= 1000:
            val = self.ctx_stack[-1].local_mem.getValue(from_address)
        else:
            val = self.global_mem.getValue(from_address)

        # Check if it is valid
        result_type = semantic_cube[dest_type][from_type][Operator.ASGN]

        if result_type != None:
            if result_type == Type.INT:
                val = int(val)
            elif result_type == Type.FLOAT:
                val = float(val)

            self.call_stack[-1].local_mem.writeAddress(dest_addr, val)
        else:
            print("[Error]: Argument type does not match parameter type")
            sys.exit()

    def performGOSUB(self, quad):
        # When returning from func, return to next quad
        self.ctx_stack[-1].quad_pos += 1

        # Save where we're going and change context from current one to next call
        self.call_stack[-1].quad_pos = quad.op2
        self.ctx_stack.append(self.call_stack.pop())

    def performRETURN(self, quad):
        # Parche guadalupano
        asgn_quad = Quadruple(Operator.ASGN, self.func_table["global"].var_table[self.ctx_stack[-1].ctx].address, quad.res)
        self.performASGN(asgn_quad)
        self.performENDPROC()

    def performENDPROC(self):
        # Remove current context
        self.ctx_stack.pop()
    
    def performVER(self, quad):
        # Check if an expr inside array indexing fall within bounds of array
        if self.resolveMem(quad.op2) <= self.resolveMem(quad.op1) or self.resolveMem(quad.op1) < 0:
            print("[Error] Index out of range for array")
            sys.exit()
    
    def performFILE(self, quad):
        # get file path value, check for the file type and if it exists
        file_path = self.resolveMem(quad.op1)
        if file_path[-4:] != ".csv":
            print("[Error] File should be .csv format")
            sys.exit()
        if not path.exists(file_path):
            print("[Error] File could not be opened")
            sys.exit()
        else:
            self.file_path = file_path
    
    def performDATA(self,quad):
        # Create a dataframe, from file path previously defined
        self.dataframe = pd.read_csv(self.file_path)

        self.writeResult(quad.op1, len(self.dataframe.index))
        self.writeResult(quad.op2, len(self.dataframe.columns))
    
    def performAVG(self, quad):
        try:
            avg = self.dataframe[self.resolveMem(quad.op1)].mean()
            self.writeResult(quad.res, avg)
        except TypeError:
            print("[Error] Dataframe key not found in file.")
            sys.exit()

    def performMODE(self, quad):
        try:
            mode = self.dataframe[self.resolveMem(quad.op1)].mode()
            self.writeResult(quad.res, mode)
        except TypeError:
            print("[Error] Dataframe key not found in file.")
            sys.exit()
    
    def performRANGE(self, quad):
        try:
            rango = self.dataframe[self.resolveMem(quad.op1)].max() - self.dataframe[self.resolveMem(quad.op1)].min()
            self.writeResult(quad.res, rango)
        except TypeError:
            print("[Error] Dataframe key not found in file.")
            sys.exit()
    
    def performVAR(self, quad):
        try:
            variance = self.dataframe[self.resolveMem(quad.op1)].var()
            self.writeResult(quad.res, variance)
        except TypeError:
            print("[Error] Dataframe key not found in file.")
            sys.exit()
    
    def performSTD_DEV(self, quad):
        try:
            std_dev = self.dataframe[self.resolveMem(quad.op1)].std()
            self.writeResult(quad.res, std_dev)
        except TypeError:
            print("[Error] Dataframe key not found in file.")
            sys.exit()
    
    def performMAX(self, quad):
        try:
            maxi = self.dataframe[self.resolveMem(quad.op1)].max()
            self.writeResult(quad.res, maxi)
        except TypeError:
            print("[Error] Dataframe key not found in file.")
            sys.exit()
    
    def performMIN(self, quad):
        try:
            mini = self.dataframe[self.resolveMem(quad.op1)].min()
            self.writeResult(quad.res, mini)
        except TypeError:
            print("[Error] Dataframe key not found in file.")
            sys.exit()
    
    def performCORREL(self, quad):
        try:
            correl = self.dataframe[self.resolveMem(quad.op1)].corr(self.dataframe[self.resolveMem(quad.op2)])
            self.writeResult(quad.res, correl)
        except TypeError:
            print("[Error] Dataframe key not found in file.")
            sys.exit()
    
    def performPLOT(self, quad):
        try:
            self.dataframe.plot(x = self.resolveMem(quad.op1), y = self.resolveMem(quad.op2), kind='scatter')
            plt.show()
        except TypeError:
            print("[Error] Dataframe key not found in file.")
            sys.exit()
    
    def performHIST(self, quad):
        try:
            self.dataframe.hist(self.resolveMem(quad.op1), bins=self.resolveMem(quad.op2), grid=False)
            plt.show()
        except TypeError:
            print("[Error] Dataframe key not found in file.")
            sys.exit()
    
    def run(self):
        while self.ctx_stack[-1].quad_pos < len(self.quad_list):
            # Get quad
            quad = self.quad_list[self.ctx_stack[-1].quad_pos]

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
                self.performPRINT(quad)
            elif quad.oper == Operator.INPUT:
                self.performREAD(quad)
            elif quad.oper == Operator.GT:
                self.performLogical(quad, operator.gt)
            elif quad.oper == Operator.GTE:
                self.performLogical(quad, operator.ge)
            elif quad.oper == Operator.LT:
                self.performLogical(quad, operator.lt)
            elif quad.oper == Operator.LTE:
                self.performLogical(quad, operator.le)
            elif quad.oper == Operator.NE:
                self.performLogical(quad, operator.ne)
            elif quad.oper == Operator.EQ:
                self.performLogical(quad, operator.eq)
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
                continue
            elif quad.oper == Operator.END:
                sys.exit()

            # Array Quads
            elif quad.oper == Operator.VER:
                self.performVER(quad)

            # COVID Quads
            elif quad.oper == Operator.FILE:
                self.performFILE(quad)
            elif quad.oper == Operator.DATA:
                self.performDATA(quad)
            elif quad.oper == Operator.AVG:
                self.performAVG(quad)
            elif quad.oper == Operator.MODE:
                self.performMODE(quad)
            elif quad.oper == Operator.RANGE:
                self.performRANGE(quad)
            elif quad.oper == Operator.VAR:
                self.performVAR(quad)
            elif quad.oper == Operator.STD_DEV:
                self.performSTD_DEV(quad)
            elif quad.oper == Operator.MAX:
                self.performMAX(quad)
            elif quad.oper == Operator.MIN:
                self.performMIN(quad)
            elif quad.oper == Operator.CORREL:
                self.performCORREL(quad)
            elif quad.oper == Operator.PLOT:
                self.performPLOT(quad)
            elif quad.oper == Operator.HIST:
                self.performHIST(quad)
            
            # Undefined
            else:
                print(f"Quad not caught: {quad.oper}")

            # Go to next quad
            self.ctx_stack[-1].quad_pos += 1
