import sys
from Utilities import Type

class AddressDir:
    def __init__(self, context):
        """
        Class stores the space needed for variables per type
        Provides functions to get address for a variable and get the size of a function
        """
        self.context = context

        self.addresses = {
            Type.INT: 0,
            Type.FLOAT: 0,
            Type.CHAR: 0,
            Type.STRING: 0,
            Type.DATAFRAME: 0
        }

    def getAddress(self, data_type, size = 1):
        # Return next address
        pointer_val = self.addresses[data_type]
        self.addresses[data_type] += size

        # Check if stack has been exceeded
        if self.addresses[data_type] > 100:
            print("[Error] Memory stack exceeded for type and context")
            sys.exit()

        context_val = self.context * 1000

        if data_type == Type.INT:
            data_type_val = 0
        elif data_type == Type.FLOAT:
            data_type_val = 100
        elif data_type == Type.CHAR:
            data_type_val = 200
        elif data_type == Type.STRING:
            data_type_val = 300

        return context_val + data_type_val + pointer_val

    def getSize(self):
        return sum(self.addresses.values())
    
    def __repr__(self):
        result = f"Context {self.context}\n Addresses: {self.addresses}\n"
        return result


class GlobalAddressDir(AddressDir):
    def __init__(self):
        super().__init__(0)

class LocalAddressDir(AddressDir):
    def __init__(self):
        super().__init__(1)

class TempAddressDir(AddressDir):
    def __init__(self):
        super().__init__(2)

        # List with freed addresses
        self.freed_addresses = {
            Type.INT: [],
            Type.FLOAT: [],
            Type.CHAR: [],
            Type.STRING: []
        }

    # If temp address will no longer be used, store it as available
    def releaseAddress(self, data_type, address):
        self.freed_addresses[data_type].append(address)

    def getAddress(self, data_type):
        # If a freed space is available, return this address
        if len(self.freed_addresses[data_type]) > 0:
            return self.freed_addresses[data_type].pop(0)
        
        # Else return a newly generated one
        return super().getAddress(data_type)

class FuncAddressDir:
    def __init__(self):
        """
        Instanciate local address dir and temp dir for a function
        Provide functionality to get size of the memories as well as addresses of each kind
        """
        self.local = LocalAddressDir()
        self.temp = TempAddressDir()

    def getLocalSize(self):
        return sum(self.local.addresses.values())

    def getTempSize(self):
        return sum(self.temp.addresses.values())
    
    def addLocal(self, data_type, size = 1):
        return self.local.getAddress(data_type, size)

    def addTemp(self, data_type):
        return self.temp.getAddress(data_type)
    
    def __repr__(self):
        return f"Local: {self.local}\n Temp: {self.temp}\n"

class CteMemory:
    def __init__(self):
        """
        Stores all constant operands and their virtual address
        """
        self.context = 3

        self.addresses = {
            Type.INT: [],
            Type.FLOAT: [],
            Type.CHAR: [],
            Type.STRING: []
        }

        self.address_table = {}

    def getAddress(self, data_type, value):
        # Return next address
        pointer_val = len(self.addresses[data_type])
        self.addresses[data_type].append(value)

        # Check if stack has been exceeded
        if pointer_val > 100:
            print("[Error] Memory stack exceeded for type and context")
            sys.exit()

        context_val = self.context * 1000

        if data_type == Type.INT:
            data_type_val = 0
        elif data_type == Type.FLOAT:
            data_type_val = 100
        elif data_type == Type.CHAR:
            data_type_val = 200
        elif data_type == Type.STRING:
            data_type_val = 300

        return context_val + data_type_val + pointer_val

    def addConstant(self, data_type, value):
        # get an address for the constant and store it
        address = self.getAddress(data_type, value)
        if address:
            self.address_table[value] = address

        return address

    def getConstant(self, address):
        # Obtain value for constant, using an address
        reduced_addr = (address - 3000) 

        if reduced_addr < 100:
            return int(self.addresses[Type.INT][reduced_addr])
        elif reduced_addr < 200:
            return float(self.addresses[Type.FLOAT][reduced_addr - 100])
        elif reduced_addr < 300:
            return self.addresses[Type.CHAR][reduced_addr - 200]
        else:
            return self.addresses[Type.STRING][reduced_addr - 300]
    
    def __repr__(self):
        return f'Constants \nINT: {self.addresses[Type.INT]}\nFLOAT: {self.addresses[Type.FLOAT]}\nCHAR: {self.addresses[Type.CHAR]}\nSTRING:{self.addresses[Type.STRING]}'

class PointerMemory:
    """
    Stores pointers in a dictionary to solve for addresses
    """
    pointer_count = 4000
    pointers = {}

    def getPointer(self):
        # Ask for a new pointer address and update count
        ptr = self.pointer_count
        self.pointer_count += 1
        return ptr

    def writePointer(self, ptr, address):
        # Write a value for the pointer
        self.pointers[ptr] = address

    def getAddress(self, ptr):
        # Obtain original address
        return self.pointers[ptr]

    def resetPointers(self):
        # Reset pointer address when switching contexts
        self.pointer_count = 4000
        self.pointers.clear()
    
    def __repr__(self):
        return f"Pointer memory: {self.pointers}"

class Memory:
    def __init__(self, directory):
        """
        Generates a array of the size needed to represent the function memory
        Creates pointers to access the space of each memory
        Provides functionality to get values given an address and write in addresses given address and value
        """
        self.int_pointer = 0
        self.float_pointer = self.int_pointer + directory.addresses[Type.INT]
        self.char_pointer = self.float_pointer + directory.addresses[Type.FLOAT]
        self.string_pointer = self.char_pointer + directory.addresses[Type.CHAR]
        self.df_pointer = self.string_pointer + directory.addresses[Type.STRING]

        self.size = self.df_pointer + directory.addresses[Type.DATAFRAME]
        self.space = [None for x in range(self.size)]

    def getValue(self, address):
        # Obtain the value for a var, given an address
        data_type_val = (address % 1000) // 100
        pointer_val = address % 100

        try:
            # bloque a intentar
            if data_type_val == 0:
                return int(self.space[self.int_pointer + pointer_val])
            elif data_type_val == 1:
                return float(self.space[self.float_pointer + pointer_val])
            elif data_type_val == 2:
                return self.space[self.char_pointer + pointer_val]
            elif data_type_val == 3:
                return self.space[self.string_pointer + pointer_val]
        except:
            print("[Error] uninitialized variable")
            sys.exit()
        
    def writeAddress(self, address, value):
        # Write a value for a var, given an address and the value
        data_type_val = (address % 1000) // 100
        pointer_val = address % 100
        
        if data_type_val == 0:
            self.space[self.int_pointer + pointer_val] = value
        elif data_type_val == 1:
            self.space[self.float_pointer + pointer_val] = value
        elif data_type_val == 2:
            self.space[self.char_pointer + pointer_val] = value
        elif data_type_val == 3:
            self.space[self.string_pointer + pointer_val] = value
