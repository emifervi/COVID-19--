from Utilities import Type

class AddressDir:
    def __init__(self, context):
        self.context = context

        self.addresses = {
            Type.INT: 0,
            Type.FLOAT: 0,
            Type.CHAR: 0,
            Type.STRING: 0
        }

    def getAddress(self, data_type):
        # Return next address
        pointer_val = self.addresses[data_type]
        self.addresses[data_type] += 1

        # Check if stack has been exceeded
        if pointer_val > 100:
            print("Error: Memory stack exceeded for type and context")
            return

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

class GlobalAddressDir(AddressDir):
    def __init__(self):
        super().__init__(0)

class LocalAddressDir(AddressDir):
    def __init__(self):
        super().__init__(1)

class TempAddressDir(AddressDir):
    def __init__(self):
        super().__init__(2)

        self.freed_addresses = {
            Type.INT: [],
            Type.FLOAT: [],
            Type.CHAR: [],
            Type.STRING: []
        }

    def releaseAddress(self, data_type, address):
        self.freed_addresses[data_type].append(address)

    def getAddress(self, data_type):
        # If a freed space is available, return this address
        if len(self.freed_addresses[data_type]) > 0:
            return self.freed_addresses[data_type].pop(0)
        
        return super().getAddress(data_type)

class FuncAddressDir:
    def __init__(self):
        self.local = LocalAddressDir()
        self.temp = TempAddressDir()

    def getLocalSize(self):
        return sum(self.local.addresses.values())

    def getTempSize(self):
        return sum(self.temp.addresses.values())
    
    #TODO: Modify ERA to use two operands, local and temp size
    def getSize(self):
        return self.getLocalSize() + self.getTempSize()
    
    def addLocal(self, data_type):
        return self.local.getAddress(data_type)

    def addTemp(self, data_type):
        return self.temp.getAddress(data_type)

class CteMemory():
    def __init__(self):
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
            print("Error: Memory stack exceeded for type and context")
            return

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
        address = self.getAddress(data_type, value)
        if address:
            self.address_table[str(value)] = address

class Memory:
    def __init__(self, directory):
        self.int_pointer = 0
        self.float_pointer = self.int_pointer + len(directory.addresses[Type.INT])
        self.char_pointer = self.float_pointer + len(directory.addresses[Type.FLOAT])
        self.string_pointer = self.char_pointer + len(directory.addresses[Type.CHAR])

        self.size = self.string_pointer + len(directory.addresses[Type.STRING])

        self.space = [None for x in range(self.size)]

    def writeAddress(self, address, value):
        data_type_val = (address % 1000) // 100
        pointer_val = data_type_val % 100

        if data_type_val == 0:
            self.space[self.int_pointer + pointer_val] = value
        elif data_type_val == 1:
            self.space[self.float_pointer + pointer_val] = value
        elif data_type_val == 2:
            self.space[self.char_pointer + pointer_val] = value
        elif data_type_val == 3:
            self.space[self.string_pointer + pointer_val] = value

