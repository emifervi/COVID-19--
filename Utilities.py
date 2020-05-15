from enum import IntEnum

class Type(IntEnum):
    INT = 0
    FLOAT = 1
    CHAR = 2
    STRING = 3
    DATAFRAME = 4
    VOID = 5

    def __repr__(self):
        return f'{self.name}'

class Operator(IntEnum):
    MULT = 0
    DIV = 1
    SUM = 2
    SUB = 3
    GT = 4
    LT = 5
    GTE = 6
    LTE = 7
    NE = 8
    EQ = 9
    ASGN = 10
    AND = 11
    OR = 12
    NOT = 13
    FF = 14
    PRINT = 15
    INPUT = 16
    GOTOF = 17
    GOTOV = 18
    GOTO = 19
    INCR = 20
    ERA = 21
    GOSUB = 22
    ENDPROC = 23
    END = 24
    PARAM = 25
    RETURN = 26

    def __repr__(self):
        return f'{self.name}'