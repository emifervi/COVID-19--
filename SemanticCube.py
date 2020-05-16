from enum import IntEnum
from Utilities import Operator, Type

semantic_cube = [[[None for x in range(len(Operator))] for x in range(len(Type))] for x in range(len(Type))]

semantic_cube[Type.INT][Type.INT][Operator.MULT] = Type.INT
semantic_cube[Type.INT][Type.INT][Operator.DIV] = Type.INT
semantic_cube[Type.INT][Type.INT][Operator.SUM] = Type.INT
semantic_cube[Type.INT][Type.INT][Operator.SUB] = Type.INT
semantic_cube[Type.INT][Type.INT][Operator.GT] = Type.INT
semantic_cube[Type.INT][Type.INT][Operator.LT] = Type.INT
semantic_cube[Type.INT][Type.INT][Operator.GTE] = Type.INT
semantic_cube[Type.INT][Type.INT][Operator.LTE] = Type.INT
semantic_cube[Type.INT][Type.INT][Operator.NE] = Type.INT
semantic_cube[Type.INT][Type.INT][Operator.EQ] = Type.INT
semantic_cube[Type.INT][Type.INT][Operator.AND] = Type.INT
semantic_cube[Type.INT][Type.INT][Operator.OR] = Type.INT
semantic_cube[Type.INT][Type.INT][Operator.NOT] = Type.INT
semantic_cube[Type.INT][Type.INT][Operator.NOT] = Type.INT
semantic_cube[Type.INT][Type.INT][Operator.ASGN] = Type.INT

semantic_cube[Type.INT][Type.FLOAT][Operator.MULT] = Type.FLOAT
semantic_cube[Type.INT][Type.FLOAT][Operator.DIV] = Type.FLOAT
semantic_cube[Type.INT][Type.FLOAT][Operator.SUM] = Type.FLOAT
semantic_cube[Type.INT][Type.FLOAT][Operator.SUB] = Type.FLOAT
semantic_cube[Type.INT][Type.FLOAT][Operator.GT] = Type.INT
semantic_cube[Type.INT][Type.FLOAT][Operator.LT] = Type.INT
semantic_cube[Type.INT][Type.FLOAT][Operator.GTE] = Type.INT
semantic_cube[Type.INT][Type.FLOAT][Operator.LTE] = Type.INT
semantic_cube[Type.INT][Type.FLOAT][Operator.NE] = Type.INT
semantic_cube[Type.INT][Type.FLOAT][Operator.EQ] = Type.INT
semantic_cube[Type.INT][Type.FLOAT][Operator.ASGN] = Type.INT

semantic_cube[Type.FLOAT][Type.INT][Operator.MULT] = Type.FLOAT
semantic_cube[Type.FLOAT][Type.INT][Operator.DIV] = Type.FLOAT
semantic_cube[Type.FLOAT][Type.INT][Operator.SUM] = Type.FLOAT
semantic_cube[Type.FLOAT][Type.INT][Operator.SUB] = Type.FLOAT
semantic_cube[Type.FLOAT][Type.INT][Operator.GT] = Type.INT
semantic_cube[Type.FLOAT][Type.INT][Operator.LT] = Type.INT
semantic_cube[Type.FLOAT][Type.INT][Operator.GTE] = Type.INT
semantic_cube[Type.FLOAT][Type.INT][Operator.LTE] = Type.INT
semantic_cube[Type.FLOAT][Type.INT][Operator.NE] = Type.INT
semantic_cube[Type.FLOAT][Type.INT][Operator.EQ] = Type.INT
semantic_cube[Type.FLOAT][Type.INT][Operator.ASGN] = Type.FLOAT

semantic_cube[Type.FLOAT][Type.FLOAT][Operator.MULT] = Type.FLOAT
semantic_cube[Type.FLOAT][Type.FLOAT][Operator.DIV] = Type.FLOAT
semantic_cube[Type.FLOAT][Type.FLOAT][Operator.SUM] = Type.FLOAT
semantic_cube[Type.FLOAT][Type.FLOAT][Operator.SUB] = Type.FLOAT
semantic_cube[Type.FLOAT][Type.FLOAT][Operator.GT] = Type.INT
semantic_cube[Type.FLOAT][Type.FLOAT][Operator.LT] = Type.INT
semantic_cube[Type.FLOAT][Type.FLOAT][Operator.GTE] = Type.INT
semantic_cube[Type.FLOAT][Type.FLOAT][Operator.LTE] = Type.INT
semantic_cube[Type.FLOAT][Type.FLOAT][Operator.NE] = Type.INT
semantic_cube[Type.FLOAT][Type.FLOAT][Operator.EQ] = Type.INT
semantic_cube[Type.FLOAT][Type.FLOAT][Operator.ASGN] = Type.FLOAT

semantic_cube[Type.CHAR][Type.CHAR][Operator.GT] = Type.INT
semantic_cube[Type.CHAR][Type.CHAR][Operator.LT] = Type.INT
semantic_cube[Type.CHAR][Type.CHAR][Operator.GTE] = Type.INT
semantic_cube[Type.CHAR][Type.CHAR][Operator.LTE] = Type.INT
semantic_cube[Type.CHAR][Type.CHAR][Operator.NE] = Type.INT
semantic_cube[Type.CHAR][Type.CHAR][Operator.EQ] = Type.INT
semantic_cube[Type.CHAR][Type.CHAR][Operator.ASGN] = Type.CHAR

semantic_cube[Type.STRING][Type.CHAR][Operator.ASGN] = Type.STRING

semantic_cube[Type.STRING][Type.STRING][Operator.GT] = Type.INT
semantic_cube[Type.STRING][Type.STRING][Operator.LT] = Type.INT
semantic_cube[Type.STRING][Type.STRING][Operator.GTE] = Type.INT
semantic_cube[Type.STRING][Type.STRING][Operator.LTE] = Type.INT
semantic_cube[Type.STRING][Type.STRING][Operator.NE] = Type.INT
semantic_cube[Type.STRING][Type.STRING][Operator.EQ] = Type.INT
semantic_cube[Type.STRING][Type.STRING][Operator.ASGN] = Type.STRING