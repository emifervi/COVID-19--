# Generated from Covid.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3@")
        buf.write("\u0206\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\3\2\3")
        buf.write("\2\3\2\3\2\5\2y\n\2\3\2\7\2|\n\2\f\2\16\2\177\13\2\3\2")
        buf.write("\3\2\3\3\3\3\3\3\3\3\3\3\6\3\u0088\n\3\r\3\16\3\u0089")
        buf.write("\3\4\3\4\3\4\3\4\3\4\6\4\u0091\n\4\r\4\16\4\u0092\3\5")
        buf.write("\3\5\3\5\7\5\u0098\n\5\f\5\16\5\u009b\13\5\3\6\3\6\3\6")
        buf.write("\3\6\5\6\u00a1\n\6\3\6\3\6\3\6\5\6\u00a6\n\6\3\7\3\7\3")
        buf.write("\7\7\7\u00ab\n\7\f\7\16\7\u00ae\13\7\3\b\3\b\5\b\u00b2")
        buf.write("\n\b\3\b\5\b\u00b5\n\b\3\t\3\t\3\t\3\t\3\n\3\n\5\n\u00bd")
        buf.write("\n\n\3\13\3\13\3\f\3\f\3\f\3\f\3\f\5\f\u00c6\n\f\3\f\3")
        buf.write("\f\3\f\5\f\u00cb\n\f\3\f\3\f\3\r\3\r\5\r\u00d1\n\r\3\16")
        buf.write("\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\5\17\u00dd")
        buf.write("\n\17\3\20\3\20\7\20\u00e1\n\20\f\20\16\20\u00e4\13\20")
        buf.write("\3\20\3\20\3\21\3\21\3\21\3\21\3\21\5\21\u00ed\n\21\3")
        buf.write("\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\5\22\u00fe\n\22\3\23\3\23\3\23\3")
        buf.write("\23\3\23\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\7\25")
        buf.write("\u010d\n\25\f\25\16\25\u0110\13\25\3\25\5\25\u0113\n\25")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\32")
        buf.write("\3\32\3\32\3\32\3\32\5\32\u012f\n\32\3\33\3\33\3\33\3")
        buf.write("\33\3\33\3\33\5\33\u0137\n\33\3\34\3\34\3\34\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\37")
        buf.write("\3\37\3\37\3\37\3 \3 \3 \3!\3!\3!\3!\3!\5!\u0154\n!\3")
        buf.write("\"\3\"\3\"\3#\3#\3#\3#\3#\5#\u015e\n#\3$\3$\3$\3$\3$\5")
        buf.write("$\u0165\n$\3%\3%\3&\3&\3&\3&\3&\5&\u016e\n&\3\'\3\'\3")
        buf.write("(\3(\3(\3)\3)\3)\3)\3)\5)\u017a\n)\3*\3*\3*\3+\3+\3+\3")
        buf.write("+\3+\5+\u0184\n+\3,\5,\u0187\n,\3,\3,\3,\3,\3,\5,\u018e")
        buf.write("\n,\3,\3,\5,\u0192\n,\3,\3,\5,\u0196\n,\3,\3,\5,\u019a")
        buf.write("\n,\3-\3-\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\5.\u01aa")
        buf.write("\n.\3/\3/\3/\3/\3/\3\60\3\60\3\60\3\60\3\60\3\60\3\60")
        buf.write("\3\60\3\60\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\62\3\62")
        buf.write("\3\62\3\62\3\62\3\62\3\62\3\63\3\63\3\63\3\63\3\63\3\63")
        buf.write("\3\63\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\65\3\65\3\65")
        buf.write("\3\65\3\65\3\65\3\65\3\66\3\66\3\66\3\66\3\66\3\66\3\66")
        buf.write("\3\67\3\67\3\67\3\67\3\67\3\67\3\67\38\38\38\38\38\38")
        buf.write("\38\38\38\39\39\39\39\39\39\39\39\39\3:\3:\3:\3:\3:\3")
        buf.write(":\3:\3:\3:\3:\2\2;\2\4\6\b\n\f\16\20\22\24\26\30\32\34")
        buf.write("\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjln")
        buf.write("pr\2\b\3\2!$\3\2\20\21\3\2\23\26\3\2\3\4\3\2\5\6\3\2:")
        buf.write("=\2\u0202\2t\3\2\2\2\4\u0082\3\2\2\2\6\u008b\3\2\2\2\b")
        buf.write("\u0094\3\2\2\2\n\u009c\3\2\2\2\f\u00a7\3\2\2\2\16\u00af")
        buf.write("\3\2\2\2\20\u00b6\3\2\2\2\22\u00bc\3\2\2\2\24\u00be\3")
        buf.write("\2\2\2\26\u00c0\3\2\2\2\30\u00d0\3\2\2\2\32\u00d2\3\2")
        buf.write("\2\2\34\u00dc\3\2\2\2\36\u00de\3\2\2\2 \u00e7\3\2\2\2")
        buf.write("\"\u00fd\3\2\2\2$\u00ff\3\2\2\2&\u0104\3\2\2\2(\u0112")
        buf.write("\3\2\2\2*\u0114\3\2\2\2,\u011a\3\2\2\2.\u0120\3\2\2\2")
        buf.write("\60\u0126\3\2\2\2\62\u012e\3\2\2\2\64\u0130\3\2\2\2\66")
        buf.write("\u0138\3\2\2\28\u013b\3\2\2\2:\u0141\3\2\2\2<\u0147\3")
        buf.write("\2\2\2>\u014b\3\2\2\2@\u0153\3\2\2\2B\u0155\3\2\2\2D\u015d")
        buf.write("\3\2\2\2F\u0164\3\2\2\2H\u0166\3\2\2\2J\u016d\3\2\2\2")
        buf.write("L\u016f\3\2\2\2N\u0171\3\2\2\2P\u0179\3\2\2\2R\u017b\3")
        buf.write("\2\2\2T\u0183\3\2\2\2V\u0199\3\2\2\2X\u019b\3\2\2\2Z\u01a9")
        buf.write("\3\2\2\2\\\u01ab\3\2\2\2^\u01b0\3\2\2\2`\u01b9\3\2\2\2")
        buf.write("b\u01c0\3\2\2\2d\u01c7\3\2\2\2f\u01ce\3\2\2\2h\u01d5\3")
        buf.write("\2\2\2j\u01dc\3\2\2\2l\u01e3\3\2\2\2n\u01ea\3\2\2\2p\u01f3")
        buf.write("\3\2\2\2r\u01fc\3\2\2\2tu\7\32\2\2uv\7>\2\2vx\7\7\2\2")
        buf.write("wy\5\4\3\2xw\3\2\2\2xy\3\2\2\2y}\3\2\2\2z|\5\26\f\2{z")
        buf.write("\3\2\2\2|\177\3\2\2\2}{\3\2\2\2}~\3\2\2\2~\u0080\3\2\2")
        buf.write("\2\177}\3\2\2\2\u0080\u0081\5 \21\2\u0081\3\3\2\2\2\u0082")
        buf.write("\u0087\7\33\2\2\u0083\u0084\5\22\n\2\u0084\u0085\5\b\5")
        buf.write("\2\u0085\u0086\7\7\2\2\u0086\u0088\3\2\2\2\u0087\u0083")
        buf.write("\3\2\2\2\u0088\u0089\3\2\2\2\u0089\u0087\3\2\2\2\u0089")
        buf.write("\u008a\3\2\2\2\u008a\5\3\2\2\2\u008b\u0090\7\33\2\2\u008c")
        buf.write("\u008d\5\24\13\2\u008d\u008e\5\b\5\2\u008e\u008f\7\7\2")
        buf.write("\2\u008f\u0091\3\2\2\2\u0090\u008c\3\2\2\2\u0091\u0092")
        buf.write("\3\2\2\2\u0092\u0090\3\2\2\2\u0092\u0093\3\2\2\2\u0093")
        buf.write("\7\3\2\2\2\u0094\u0099\5\n\6\2\u0095\u0096\7\t\2\2\u0096")
        buf.write("\u0098\5\n\6\2\u0097\u0095\3\2\2\2\u0098\u009b\3\2\2\2")
        buf.write("\u0099\u0097\3\2\2\2\u0099\u009a\3\2\2\2\u009a\t\3\2\2")
        buf.write("\2\u009b\u0099\3\2\2\2\u009c\u00a0\7>\2\2\u009d\u009e")
        buf.write("\7\16\2\2\u009e\u009f\7:\2\2\u009f\u00a1\7\17\2\2\u00a0")
        buf.write("\u009d\3\2\2\2\u00a0\u00a1\3\2\2\2\u00a1\u00a5\3\2\2\2")
        buf.write("\u00a2\u00a3\7\16\2\2\u00a3\u00a4\7:\2\2\u00a4\u00a6\7")
        buf.write("\17\2\2\u00a5\u00a2\3\2\2\2\u00a5\u00a6\3\2\2\2\u00a6")
        buf.write("\13\3\2\2\2\u00a7\u00ac\5\16\b\2\u00a8\u00a9\7\t\2\2\u00a9")
        buf.write("\u00ab\5\16\b\2\u00aa\u00a8\3\2\2\2\u00ab\u00ae\3\2\2")
        buf.write("\2\u00ac\u00aa\3\2\2\2\u00ac\u00ad\3\2\2\2\u00ad\r\3\2")
        buf.write("\2\2\u00ae\u00ac\3\2\2\2\u00af\u00b1\7>\2\2\u00b0\u00b2")
        buf.write("\5\20\t\2\u00b1\u00b0\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2")
        buf.write("\u00b4\3\2\2\2\u00b3\u00b5\5\20\t\2\u00b4\u00b3\3\2\2")
        buf.write("\2\u00b4\u00b5\3\2\2\2\u00b5\17\3\2\2\2\u00b6\u00b7\7")
        buf.write("\16\2\2\u00b7\u00b8\5> \2\u00b8\u00b9\7\17\2\2\u00b9\21")
        buf.write("\3\2\2\2\u00ba\u00bd\5\24\13\2\u00bb\u00bd\7%\2\2\u00bc")
        buf.write("\u00ba\3\2\2\2\u00bc\u00bb\3\2\2\2\u00bd\23\3\2\2\2\u00be")
        buf.write("\u00bf\t\2\2\2\u00bf\25\3\2\2\2\u00c0\u00c1\7\'\2\2\u00c1")
        buf.write("\u00c2\5\30\r\2\u00c2\u00c3\7>\2\2\u00c3\u00c5\7\f\2\2")
        buf.write("\u00c4\u00c6\5\32\16\2\u00c5\u00c4\3\2\2\2\u00c5\u00c6")
        buf.write("\3\2\2\2\u00c6\u00c7\3\2\2\2\u00c7\u00c8\7\r\2\2\u00c8")
        buf.write("\u00ca\7\7\2\2\u00c9\u00cb\5\6\4\2\u00ca\u00c9\3\2\2\2")
        buf.write("\u00ca\u00cb\3\2\2\2\u00cb\u00cc\3\2\2\2\u00cc\u00cd\5")
        buf.write("\36\20\2\u00cd\27\3\2\2\2\u00ce\u00d1\5\24\13\2\u00cf")
        buf.write("\u00d1\7&\2\2\u00d0\u00ce\3\2\2\2\u00d0\u00cf\3\2\2\2")
        buf.write("\u00d1\31\3\2\2\2\u00d2\u00d3\5\24\13\2\u00d3\u00d4\7")
        buf.write(">\2\2\u00d4\u00d5\5\34\17\2\u00d5\33\3\2\2\2\u00d6\u00d7")
        buf.write("\7\t\2\2\u00d7\u00d8\5\24\13\2\u00d8\u00d9\7>\2\2\u00d9")
        buf.write("\u00da\5\34\17\2\u00da\u00dd\3\2\2\2\u00db\u00dd\3\2\2")
        buf.write("\2\u00dc\u00d6\3\2\2\2\u00dc\u00db\3\2\2\2\u00dd\35\3")
        buf.write("\2\2\2\u00de\u00e2\7\n\2\2\u00df\u00e1\5\"\22\2\u00e0")
        buf.write("\u00df\3\2\2\2\u00e1\u00e4\3\2\2\2\u00e2\u00e0\3\2\2\2")
        buf.write("\u00e2\u00e3\3\2\2\2\u00e3\u00e5\3\2\2\2\u00e4\u00e2\3")
        buf.write("\2\2\2\u00e5\u00e6\7\13\2\2\u00e6\37\3\2\2\2\u00e7\u00e8")
        buf.write("\7)\2\2\u00e8\u00e9\7\f\2\2\u00e9\u00ea\7\r\2\2\u00ea")
        buf.write("\u00ec\7\7\2\2\u00eb\u00ed\5\6\4\2\u00ec\u00eb\3\2\2\2")
        buf.write("\u00ec\u00ed\3\2\2\2\u00ed\u00ee\3\2\2\2\u00ee\u00ef\5")
        buf.write("\36\20\2\u00ef!\3\2\2\2\u00f0\u00fe\5$\23\2\u00f1\u00f2")
        buf.write("\5&\24\2\u00f2\u00f3\7\7\2\2\u00f3\u00fe\3\2\2\2\u00f4")
        buf.write("\u00fe\5*\26\2\u00f5\u00fe\5,\27\2\u00f6\u00fe\5.\30\2")
        buf.write("\u00f7\u00fe\5\64\33\2\u00f8\u00fe\58\35\2\u00f9\u00fe")
        buf.write("\5:\36\2\u00fa\u00fb\5Z.\2\u00fb\u00fc\7\7\2\2\u00fc\u00fe")
        buf.write("\3\2\2\2\u00fd\u00f0\3\2\2\2\u00fd\u00f1\3\2\2\2\u00fd")
        buf.write("\u00f4\3\2\2\2\u00fd\u00f5\3\2\2\2\u00fd\u00f6\3\2\2\2")
        buf.write("\u00fd\u00f7\3\2\2\2\u00fd\u00f8\3\2\2\2\u00fd\u00f9\3")
        buf.write("\2\2\2\u00fd\u00fa\3\2\2\2\u00fe#\3\2\2\2\u00ff\u0100")
        buf.write("\5\16\b\2\u0100\u0101\7\31\2\2\u0101\u0102\5> \2\u0102")
        buf.write("\u0103\7\7\2\2\u0103%\3\2\2\2\u0104\u0105\7>\2\2\u0105")
        buf.write("\u0106\7\f\2\2\u0106\u0107\5(\25\2\u0107\u0108\7\r\2\2")
        buf.write("\u0108\'\3\2\2\2\u0109\u010e\5> \2\u010a\u010b\7\t\2\2")
        buf.write("\u010b\u010d\5> \2\u010c\u010a\3\2\2\2\u010d\u0110\3\2")
        buf.write("\2\2\u010e\u010c\3\2\2\2\u010e\u010f\3\2\2\2\u010f\u0113")
        buf.write("\3\2\2\2\u0110\u010e\3\2\2\2\u0111\u0113\3\2\2\2\u0112")
        buf.write("\u0109\3\2\2\2\u0112\u0111\3\2\2\2\u0113)\3\2\2\2\u0114")
        buf.write("\u0115\7*\2\2\u0115\u0116\7\f\2\2\u0116\u0117\5> \2\u0117")
        buf.write("\u0118\7\r\2\2\u0118\u0119\7\7\2\2\u0119+\3\2\2\2\u011a")
        buf.write("\u011b\7+\2\2\u011b\u011c\7\f\2\2\u011c\u011d\5\f\7\2")
        buf.write("\u011d\u011e\7\r\2\2\u011e\u011f\7\7\2\2\u011f-\3\2\2")
        buf.write("\2\u0120\u0121\7(\2\2\u0121\u0122\7\f\2\2\u0122\u0123")
        buf.write("\5\60\31\2\u0123\u0124\7\r\2\2\u0124\u0125\7\7\2\2\u0125")
        buf.write("/\3\2\2\2\u0126\u0127\5> \2\u0127\u0128\5\62\32\2\u0128")
        buf.write("\61\3\2\2\2\u0129\u012a\7\t\2\2\u012a\u012b\5> \2\u012b")
        buf.write("\u012c\5\62\32\2\u012c\u012f\3\2\2\2\u012d\u012f\3\2\2")
        buf.write("\2\u012e\u0129\3\2\2\2\u012e\u012d\3\2\2\2\u012f\63\3")
        buf.write("\2\2\2\u0130\u0131\7\34\2\2\u0131\u0132\7\f\2\2\u0132")
        buf.write("\u0133\5> \2\u0133\u0134\7\r\2\2\u0134\u0136\5\36\20\2")
        buf.write("\u0135\u0137\5\66\34\2\u0136\u0135\3\2\2\2\u0136\u0137")
        buf.write("\3\2\2\2\u0137\65\3\2\2\2\u0138\u0139\7 \2\2\u0139\u013a")
        buf.write("\5\36\20\2\u013a\67\3\2\2\2\u013b\u013c\7\35\2\2\u013c")
        buf.write("\u013d\7\f\2\2\u013d\u013e\5> \2\u013e\u013f\7\r\2\2\u013f")
        buf.write("\u0140\5\36\20\2\u01409\3\2\2\2\u0141\u0142\7\36\2\2\u0142")
        buf.write("\u0143\5<\37\2\u0143\u0144\7\37\2\2\u0144\u0145\5> \2")
        buf.write("\u0145\u0146\5\36\20\2\u0146;\3\2\2\2\u0147\u0148\7>\2")
        buf.write("\2\u0148\u0149\7\31\2\2\u0149\u014a\5> \2\u014a=\3\2\2")
        buf.write("\2\u014b\u014c\5B\"\2\u014c\u014d\5@!\2\u014d?\3\2\2\2")
        buf.write("\u014e\u014f\7\27\2\2\u014f\u0150\5B\"\2\u0150\u0151\5")
        buf.write("@!\2\u0151\u0154\3\2\2\2\u0152\u0154\3\2\2\2\u0153\u014e")
        buf.write("\3\2\2\2\u0153\u0152\3\2\2\2\u0154A\3\2\2\2\u0155\u0156")
        buf.write("\5F$\2\u0156\u0157\5D#\2\u0157C\3\2\2\2\u0158\u0159\7")
        buf.write("\30\2\2\u0159\u015a\5F$\2\u015a\u015b\5D#\2\u015b\u015e")
        buf.write("\3\2\2\2\u015c\u015e\3\2\2\2\u015d\u0158\3\2\2\2\u015d")
        buf.write("\u015c\3\2\2\2\u015eE\3\2\2\2\u015f\u0160\5J&\2\u0160")
        buf.write("\u0161\5H%\2\u0161\u0162\5J&\2\u0162\u0165\3\2\2\2\u0163")
        buf.write("\u0165\5J&\2\u0164\u015f\3\2\2\2\u0164\u0163\3\2\2\2\u0165")
        buf.write("G\3\2\2\2\u0166\u0167\t\3\2\2\u0167I\3\2\2\2\u0168\u0169")
        buf.write("\5N(\2\u0169\u016a\5L\'\2\u016a\u016b\5N(\2\u016b\u016e")
        buf.write("\3\2\2\2\u016c\u016e\5N(\2\u016d\u0168\3\2\2\2\u016d\u016c")
        buf.write("\3\2\2\2\u016eK\3\2\2\2\u016f\u0170\t\4\2\2\u0170M\3\2")
        buf.write("\2\2\u0171\u0172\5R*\2\u0172\u0173\5P)\2\u0173O\3\2\2")
        buf.write("\2\u0174\u0175\t\5\2\2\u0175\u0176\5R*\2\u0176\u0177\5")
        buf.write("P)\2\u0177\u017a\3\2\2\2\u0178\u017a\3\2\2\2\u0179\u0174")
        buf.write("\3\2\2\2\u0179\u0178\3\2\2\2\u017aQ\3\2\2\2\u017b\u017c")
        buf.write("\5V,\2\u017c\u017d\5T+\2\u017dS\3\2\2\2\u017e\u017f\t")
        buf.write("\6\2\2\u017f\u0180\5V,\2\u0180\u0181\5T+\2\u0181\u0184")
        buf.write("\3\2\2\2\u0182\u0184\3\2\2\2\u0183\u017e\3\2\2\2\u0183")
        buf.write("\u0182\3\2\2\2\u0184U\3\2\2\2\u0185\u0187\7\22\2\2\u0186")
        buf.write("\u0185\3\2\2\2\u0186\u0187\3\2\2\2\u0187\u0188\3\2\2\2")
        buf.write("\u0188\u0189\7\f\2\2\u0189\u018a\5> \2\u018a\u018b\7\r")
        buf.write("\2\2\u018b\u019a\3\2\2\2\u018c\u018e\7\22\2\2\u018d\u018c")
        buf.write("\3\2\2\2\u018d\u018e\3\2\2\2\u018e\u018f\3\2\2\2\u018f")
        buf.write("\u019a\5X-\2\u0190\u0192\7\22\2\2\u0191\u0190\3\2\2\2")
        buf.write("\u0191\u0192\3\2\2\2\u0192\u0193\3\2\2\2\u0193\u019a\5")
        buf.write("\16\b\2\u0194\u0196\7\22\2\2\u0195\u0194\3\2\2\2\u0195")
        buf.write("\u0196\3\2\2\2\u0196\u0197\3\2\2\2\u0197\u019a\5&\24\2")
        buf.write("\u0198\u019a\5Z.\2\u0199\u0186\3\2\2\2\u0199\u018d\3\2")
        buf.write("\2\2\u0199\u0191\3\2\2\2\u0199\u0195\3\2\2\2\u0199\u0198")
        buf.write("\3\2\2\2\u019aW\3\2\2\2\u019b\u019c\t\7\2\2\u019cY\3\2")
        buf.write("\2\2\u019d\u01aa\5\\/\2\u019e\u01aa\5^\60\2\u019f\u01aa")
        buf.write("\5`\61\2\u01a0\u01aa\5b\62\2\u01a1\u01aa\5d\63\2\u01a2")
        buf.write("\u01aa\5f\64\2\u01a3\u01aa\5h\65\2\u01a4\u01aa\5j\66\2")
        buf.write("\u01a5\u01aa\5l\67\2\u01a6\u01aa\5n8\2\u01a7\u01aa\5p")
        buf.write("9\2\u01a8\u01aa\5r:\2\u01a9\u019d\3\2\2\2\u01a9\u019e")
        buf.write("\3\2\2\2\u01a9\u019f\3\2\2\2\u01a9\u01a0\3\2\2\2\u01a9")
        buf.write("\u01a1\3\2\2\2\u01a9\u01a2\3\2\2\2\u01a9\u01a3\3\2\2\2")
        buf.write("\u01a9\u01a4\3\2\2\2\u01a9\u01a5\3\2\2\2\u01a9\u01a6\3")
        buf.write("\2\2\2\u01a9\u01a7\3\2\2\2\u01a9\u01a8\3\2\2\2\u01aa[")
        buf.write("\3\2\2\2\u01ab\u01ac\7,\2\2\u01ac\u01ad\7\f\2\2\u01ad")
        buf.write("\u01ae\5V,\2\u01ae\u01af\7\r\2\2\u01af]\3\2\2\2\u01b0")
        buf.write("\u01b1\7-\2\2\u01b1\u01b2\7\f\2\2\u01b2\u01b3\5\16\b\2")
        buf.write("\u01b3\u01b4\7\t\2\2\u01b4\u01b5\5\16\b\2\u01b5\u01b6")
        buf.write("\7\t\2\2\u01b6\u01b7\5\16\b\2\u01b7\u01b8\7\r\2\2\u01b8")
        buf.write("_\3\2\2\2\u01b9\u01ba\7.\2\2\u01ba\u01bb\7\f\2\2\u01bb")
        buf.write("\u01bc\5\16\b\2\u01bc\u01bd\7\t\2\2\u01bd\u01be\5V,\2")
        buf.write("\u01be\u01bf\7\r\2\2\u01bfa\3\2\2\2\u01c0\u01c1\7/\2\2")
        buf.write("\u01c1\u01c2\7\f\2\2\u01c2\u01c3\5\16\b\2\u01c3\u01c4")
        buf.write("\7\t\2\2\u01c4\u01c5\5V,\2\u01c5\u01c6\7\r\2\2\u01c6c")
        buf.write("\3\2\2\2\u01c7\u01c8\7\60\2\2\u01c8\u01c9\7\f\2\2\u01c9")
        buf.write("\u01ca\5\16\b\2\u01ca\u01cb\7\t\2\2\u01cb\u01cc\5V,\2")
        buf.write("\u01cc\u01cd\7\r\2\2\u01cde\3\2\2\2\u01ce\u01cf\7\61\2")
        buf.write("\2\u01cf\u01d0\7\f\2\2\u01d0\u01d1\5\16\b\2\u01d1\u01d2")
        buf.write("\7\t\2\2\u01d2\u01d3\5V,\2\u01d3\u01d4\7\r\2\2\u01d4g")
        buf.write("\3\2\2\2\u01d5\u01d6\7\62\2\2\u01d6\u01d7\7\f\2\2\u01d7")
        buf.write("\u01d8\5\16\b\2\u01d8\u01d9\7\t\2\2\u01d9\u01da\5V,\2")
        buf.write("\u01da\u01db\7\r\2\2\u01dbi\3\2\2\2\u01dc\u01dd\7\63\2")
        buf.write("\2\u01dd\u01de\7\f\2\2\u01de\u01df\5\16\b\2\u01df\u01e0")
        buf.write("\7\t\2\2\u01e0\u01e1\5V,\2\u01e1\u01e2\7\r\2\2\u01e2k")
        buf.write("\3\2\2\2\u01e3\u01e4\7\64\2\2\u01e4\u01e5\7\f\2\2\u01e5")
        buf.write("\u01e6\5\16\b\2\u01e6\u01e7\7\t\2\2\u01e7\u01e8\5V,\2")
        buf.write("\u01e8\u01e9\7\r\2\2\u01e9m\3\2\2\2\u01ea\u01eb\7\66\2")
        buf.write("\2\u01eb\u01ec\7\f\2\2\u01ec\u01ed\5\16\b\2\u01ed\u01ee")
        buf.write("\7\t\2\2\u01ee\u01ef\5V,\2\u01ef\u01f0\7\t\2\2\u01f0\u01f1")
        buf.write("\5V,\2\u01f1\u01f2\7\r\2\2\u01f2o\3\2\2\2\u01f3\u01f4")
        buf.write("\7\67\2\2\u01f4\u01f5\7\f\2\2\u01f5\u01f6\5\16\b\2\u01f6")
        buf.write("\u01f7\7\t\2\2\u01f7\u01f8\5V,\2\u01f8\u01f9\7\t\2\2\u01f9")
        buf.write("\u01fa\5> \2\u01fa\u01fb\7\r\2\2\u01fbq\3\2\2\2\u01fc")
        buf.write("\u01fd\78\2\2\u01fd\u01fe\7\f\2\2\u01fe\u01ff\5\16\b\2")
        buf.write("\u01ff\u0200\7\t\2\2\u0200\u0201\5V,\2\u0201\u0202\7\t")
        buf.write("\2\2\u0202\u0203\5V,\2\u0203\u0204\7\r\2\2\u0204s\3\2")
        buf.write("\2\2$x}\u0089\u0092\u0099\u00a0\u00a5\u00ac\u00b1\u00b4")
        buf.write("\u00bc\u00c5\u00ca\u00d0\u00dc\u00e2\u00ec\u00fd\u010e")
        buf.write("\u0112\u012e\u0136\u0153\u015d\u0164\u016d\u0179\u0183")
        buf.write("\u0186\u018d\u0191\u0195\u0199\u01a9")
        return buf.getvalue()


class CovidParser ( Parser ):

    grammarFileName = "Covid.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'", "'*'", "'/'", "';'", "':'", 
                     "','", "'{'", "'}'", "'('", "')'", "'['", "']'", "'=='", 
                     "'!='", "'!'", "'<='", "'>='", "'<'", "'>'", "'||'", 
                     "'&&'", "'='", "'program'", "'var'", "'if'", "'while'", 
                     "'for'", "'to'", "'else'", "'int'", "'float'", "'char'", 
                     "'string'", "'dataframe'", "'void'", "'func'", "'print'", 
                     "'main'", "'return'", "'input'", "'load_file'", "'load_data'", 
                     "'avg'", "'mode'", "'range'", "'variance'", "'std_dev'", 
                     "'max'", "'min'", "'moment'", "'plot'", "'histogram'", 
                     "'correl'" ]

    symbolicNames = [ "<INVALID>", "PLUS", "MINUS", "MULT", "DIVIDE", "SEMI", 
                      "COLON", "COMMA", "CURLY_L", "CURLY_R", "PARENS_L", 
                      "PARENS_R", "SQUARE_L", "SQUARE_R", "EQ", "NE", "NOT", 
                      "LTE", "GTE", "LT", "GT", "OR", "AND", "ASGN", "PROGRAM", 
                      "VAR", "IF", "WHILE", "FOR", "TO", "ELSE", "INT", 
                      "FLOAT", "CHAR", "STRING", "DATAFRAME", "VOID", "FUNC", 
                      "PRINT", "MAIN", "RETURN", "INPUT", "LOAD_FILE", "LOAD_DATA", 
                      "AVG", "MODE", "RANGE", "VARIANCE", "STD_DEV", "MAX", 
                      "MIN", "MOMENT", "PLOT", "HISTOGRAM", "CORREL", "WS", 
                      "INT_CTE", "FLOAT_CTE", "STRING_CTE", "CHAR_CTE", 
                      "ID", "LINE_CMT", "BLOCK_CMT" ]

    RULE_start = 0
    RULE_gb_var_block = 1
    RULE_var_block = 2
    RULE_ids_decl = 3
    RULE_ident_decl = 4
    RULE_ids = 5
    RULE_ident = 6
    RULE_ident_ind = 7
    RULE_tipo = 8
    RULE_tipo_atom = 9
    RULE_func = 10
    RULE_return_type = 11
    RULE_params = 12
    RULE_param = 13
    RULE_block = 14
    RULE_main = 15
    RULE_statement = 16
    RULE_assignment = 17
    RULE_call = 18
    RULE_args = 19
    RULE_regresa = 20
    RULE_read = 21
    RULE_write = 22
    RULE_impr = 23
    RULE_imprs = 24
    RULE_decision = 25
    RULE_else_block = 26
    RULE_while_loop = 27
    RULE_for_loop = 28
    RULE_for_asgn = 29
    RULE_expr = 30
    RULE_exprs = 31
    RULE_and_term = 32
    RULE_and_terms = 33
    RULE_comp_term = 34
    RULE_comp_op = 35
    RULE_rel_term = 36
    RULE_rel_op = 37
    RULE_artm_term = 38
    RULE_artm_terms = 39
    RULE_fact_term = 40
    RULE_fact_terms = 41
    RULE_operand = 42
    RULE_cte = 43
    RULE_covid = 44
    RULE_load_file = 45
    RULE_load_data = 46
    RULE_avg = 47
    RULE_moda = 48
    RULE_rango = 49
    RULE_variance = 50
    RULE_std_dev = 51
    RULE_maxi = 52
    RULE_mini = 53
    RULE_plot = 54
    RULE_histogram = 55
    RULE_correl = 56

    ruleNames =  [ "start", "gb_var_block", "var_block", "ids_decl", "ident_decl", 
                   "ids", "ident", "ident_ind", "tipo", "tipo_atom", "func", 
                   "return_type", "params", "param", "block", "main", "statement", 
                   "assignment", "call", "args", "regresa", "read", "write", 
                   "impr", "imprs", "decision", "else_block", "while_loop", 
                   "for_loop", "for_asgn", "expr", "exprs", "and_term", 
                   "and_terms", "comp_term", "comp_op", "rel_term", "rel_op", 
                   "artm_term", "artm_terms", "fact_term", "fact_terms", 
                   "operand", "cte", "covid", "load_file", "load_data", 
                   "avg", "moda", "rango", "variance", "std_dev", "maxi", 
                   "mini", "plot", "histogram", "correl" ]

    EOF = Token.EOF
    PLUS=1
    MINUS=2
    MULT=3
    DIVIDE=4
    SEMI=5
    COLON=6
    COMMA=7
    CURLY_L=8
    CURLY_R=9
    PARENS_L=10
    PARENS_R=11
    SQUARE_L=12
    SQUARE_R=13
    EQ=14
    NE=15
    NOT=16
    LTE=17
    GTE=18
    LT=19
    GT=20
    OR=21
    AND=22
    ASGN=23
    PROGRAM=24
    VAR=25
    IF=26
    WHILE=27
    FOR=28
    TO=29
    ELSE=30
    INT=31
    FLOAT=32
    CHAR=33
    STRING=34
    DATAFRAME=35
    VOID=36
    FUNC=37
    PRINT=38
    MAIN=39
    RETURN=40
    INPUT=41
    LOAD_FILE=42
    LOAD_DATA=43
    AVG=44
    MODE=45
    RANGE=46
    VARIANCE=47
    STD_DEV=48
    MAX=49
    MIN=50
    MOMENT=51
    PLOT=52
    HISTOGRAM=53
    CORREL=54
    WS=55
    INT_CTE=56
    FLOAT_CTE=57
    STRING_CTE=58
    CHAR_CTE=59
    ID=60
    LINE_CMT=61
    BLOCK_CMT=62

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROGRAM(self):
            return self.getToken(CovidParser.PROGRAM, 0)

        def ID(self):
            return self.getToken(CovidParser.ID, 0)

        def SEMI(self):
            return self.getToken(CovidParser.SEMI, 0)

        def main(self):
            return self.getTypedRuleContext(CovidParser.MainContext,0)


        def gb_var_block(self):
            return self.getTypedRuleContext(CovidParser.Gb_var_blockContext,0)


        def func(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CovidParser.FuncContext)
            else:
                return self.getTypedRuleContext(CovidParser.FuncContext,i)


        def getRuleIndex(self):
            return CovidParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)




    def start(self):

        localctx = CovidParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.match(CovidParser.PROGRAM)
            self.state = 115
            self.match(CovidParser.ID)
            self.state = 116
            self.match(CovidParser.SEMI)
            self.state = 118
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CovidParser.VAR:
                self.state = 117
                self.gb_var_block()


            self.state = 123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CovidParser.FUNC:
                self.state = 120
                self.func()
                self.state = 125
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 126
            self.main()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Gb_var_blockContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(CovidParser.VAR, 0)

        def tipo(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CovidParser.TipoContext)
            else:
                return self.getTypedRuleContext(CovidParser.TipoContext,i)


        def ids_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CovidParser.Ids_declContext)
            else:
                return self.getTypedRuleContext(CovidParser.Ids_declContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(CovidParser.SEMI)
            else:
                return self.getToken(CovidParser.SEMI, i)

        def getRuleIndex(self):
            return CovidParser.RULE_gb_var_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGb_var_block" ):
                listener.enterGb_var_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGb_var_block" ):
                listener.exitGb_var_block(self)




    def gb_var_block(self):

        localctx = CovidParser.Gb_var_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_gb_var_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.match(CovidParser.VAR)
            self.state = 133 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 129
                self.tipo()
                self.state = 130
                self.ids_decl()
                self.state = 131
                self.match(CovidParser.SEMI)
                self.state = 135 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CovidParser.INT) | (1 << CovidParser.FLOAT) | (1 << CovidParser.CHAR) | (1 << CovidParser.STRING) | (1 << CovidParser.DATAFRAME))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_blockContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(CovidParser.VAR, 0)

        def tipo_atom(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CovidParser.Tipo_atomContext)
            else:
                return self.getTypedRuleContext(CovidParser.Tipo_atomContext,i)


        def ids_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CovidParser.Ids_declContext)
            else:
                return self.getTypedRuleContext(CovidParser.Ids_declContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(CovidParser.SEMI)
            else:
                return self.getToken(CovidParser.SEMI, i)

        def getRuleIndex(self):
            return CovidParser.RULE_var_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_block" ):
                listener.enterVar_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_block" ):
                listener.exitVar_block(self)




    def var_block(self):

        localctx = CovidParser.Var_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_var_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.match(CovidParser.VAR)
            self.state = 142 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 138
                self.tipo_atom()
                self.state = 139
                self.ids_decl()
                self.state = 140
                self.match(CovidParser.SEMI)
                self.state = 144 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CovidParser.INT) | (1 << CovidParser.FLOAT) | (1 << CovidParser.CHAR) | (1 << CovidParser.STRING))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ids_declContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ident_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CovidParser.Ident_declContext)
            else:
                return self.getTypedRuleContext(CovidParser.Ident_declContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CovidParser.COMMA)
            else:
                return self.getToken(CovidParser.COMMA, i)

        def getRuleIndex(self):
            return CovidParser.RULE_ids_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIds_decl" ):
                listener.enterIds_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIds_decl" ):
                listener.exitIds_decl(self)




    def ids_decl(self):

        localctx = CovidParser.Ids_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_ids_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.ident_decl()
            self.state = 151
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CovidParser.COMMA:
                self.state = 147
                self.match(CovidParser.COMMA)
                self.state = 148
                self.ident_decl()
                self.state = 153
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ident_declContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CovidParser.ID, 0)

        def SQUARE_L(self, i:int=None):
            if i is None:
                return self.getTokens(CovidParser.SQUARE_L)
            else:
                return self.getToken(CovidParser.SQUARE_L, i)

        def INT_CTE(self, i:int=None):
            if i is None:
                return self.getTokens(CovidParser.INT_CTE)
            else:
                return self.getToken(CovidParser.INT_CTE, i)

        def SQUARE_R(self, i:int=None):
            if i is None:
                return self.getTokens(CovidParser.SQUARE_R)
            else:
                return self.getToken(CovidParser.SQUARE_R, i)

        def getRuleIndex(self):
            return CovidParser.RULE_ident_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdent_decl" ):
                listener.enterIdent_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdent_decl" ):
                listener.exitIdent_decl(self)




    def ident_decl(self):

        localctx = CovidParser.Ident_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_ident_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.match(CovidParser.ID)
            self.state = 158
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 155
                self.match(CovidParser.SQUARE_L)
                self.state = 156
                self.match(CovidParser.INT_CTE)
                self.state = 157
                self.match(CovidParser.SQUARE_R)


            self.state = 163
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CovidParser.SQUARE_L:
                self.state = 160
                self.match(CovidParser.SQUARE_L)
                self.state = 161
                self.match(CovidParser.INT_CTE)
                self.state = 162
                self.match(CovidParser.SQUARE_R)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ident(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CovidParser.IdentContext)
            else:
                return self.getTypedRuleContext(CovidParser.IdentContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CovidParser.COMMA)
            else:
                return self.getToken(CovidParser.COMMA, i)

        def getRuleIndex(self):
            return CovidParser.RULE_ids

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIds" ):
                listener.enterIds(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIds" ):
                listener.exitIds(self)




    def ids(self):

        localctx = CovidParser.IdsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_ids)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.ident()
            self.state = 170
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CovidParser.COMMA:
                self.state = 166
                self.match(CovidParser.COMMA)
                self.state = 167
                self.ident()
                self.state = 172
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CovidParser.ID, 0)

        def ident_ind(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CovidParser.Ident_indContext)
            else:
                return self.getTypedRuleContext(CovidParser.Ident_indContext,i)


        def getRuleIndex(self):
            return CovidParser.RULE_ident

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdent" ):
                listener.enterIdent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdent" ):
                listener.exitIdent(self)




    def ident(self):

        localctx = CovidParser.IdentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_ident)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.match(CovidParser.ID)
            self.state = 175
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 174
                self.ident_ind()


            self.state = 178
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CovidParser.SQUARE_L:
                self.state = 177
                self.ident_ind()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ident_indContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SQUARE_L(self):
            return self.getToken(CovidParser.SQUARE_L, 0)

        def expr(self):
            return self.getTypedRuleContext(CovidParser.ExprContext,0)


        def SQUARE_R(self):
            return self.getToken(CovidParser.SQUARE_R, 0)

        def getRuleIndex(self):
            return CovidParser.RULE_ident_ind

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdent_ind" ):
                listener.enterIdent_ind(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdent_ind" ):
                listener.exitIdent_ind(self)




    def ident_ind(self):

        localctx = CovidParser.Ident_indContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_ident_ind)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.match(CovidParser.SQUARE_L)
            self.state = 181
            self.expr()
            self.state = 182
            self.match(CovidParser.SQUARE_R)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TipoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo_atom(self):
            return self.getTypedRuleContext(CovidParser.Tipo_atomContext,0)


        def DATAFRAME(self):
            return self.getToken(CovidParser.DATAFRAME, 0)

        def getRuleIndex(self):
            return CovidParser.RULE_tipo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipo" ):
                listener.enterTipo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipo" ):
                listener.exitTipo(self)




    def tipo(self):

        localctx = CovidParser.TipoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_tipo)
        try:
            self.state = 186
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CovidParser.INT, CovidParser.FLOAT, CovidParser.CHAR, CovidParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 184
                self.tipo_atom()
                pass
            elif token in [CovidParser.DATAFRAME]:
                self.enterOuterAlt(localctx, 2)
                self.state = 185
                self.match(CovidParser.DATAFRAME)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Tipo_atomContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(CovidParser.INT, 0)

        def FLOAT(self):
            return self.getToken(CovidParser.FLOAT, 0)

        def CHAR(self):
            return self.getToken(CovidParser.CHAR, 0)

        def STRING(self):
            return self.getToken(CovidParser.STRING, 0)

        def getRuleIndex(self):
            return CovidParser.RULE_tipo_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipo_atom" ):
                listener.enterTipo_atom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipo_atom" ):
                listener.exitTipo_atom(self)




    def tipo_atom(self):

        localctx = CovidParser.Tipo_atomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_tipo_atom)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CovidParser.INT) | (1 << CovidParser.FLOAT) | (1 << CovidParser.CHAR) | (1 << CovidParser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(CovidParser.FUNC, 0)

        def return_type(self):
            return self.getTypedRuleContext(CovidParser.Return_typeContext,0)


        def ID(self):
            return self.getToken(CovidParser.ID, 0)

        def PARENS_L(self):
            return self.getToken(CovidParser.PARENS_L, 0)

        def PARENS_R(self):
            return self.getToken(CovidParser.PARENS_R, 0)

        def SEMI(self):
            return self.getToken(CovidParser.SEMI, 0)

        def block(self):
            return self.getTypedRuleContext(CovidParser.BlockContext,0)


        def params(self):
            return self.getTypedRuleContext(CovidParser.ParamsContext,0)


        def var_block(self):
            return self.getTypedRuleContext(CovidParser.Var_blockContext,0)


        def getRuleIndex(self):
            return CovidParser.RULE_func

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc" ):
                listener.enterFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc" ):
                listener.exitFunc(self)




    def func(self):

        localctx = CovidParser.FuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_func)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.match(CovidParser.FUNC)
            self.state = 191
            self.return_type()
            self.state = 192
            self.match(CovidParser.ID)
            self.state = 193
            self.match(CovidParser.PARENS_L)
            self.state = 195
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CovidParser.INT) | (1 << CovidParser.FLOAT) | (1 << CovidParser.CHAR) | (1 << CovidParser.STRING))) != 0):
                self.state = 194
                self.params()


            self.state = 197
            self.match(CovidParser.PARENS_R)
            self.state = 198
            self.match(CovidParser.SEMI)
            self.state = 200
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CovidParser.VAR:
                self.state = 199
                self.var_block()


            self.state = 202
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo_atom(self):
            return self.getTypedRuleContext(CovidParser.Tipo_atomContext,0)


        def VOID(self):
            return self.getToken(CovidParser.VOID, 0)

        def getRuleIndex(self):
            return CovidParser.RULE_return_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn_type" ):
                listener.enterReturn_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn_type" ):
                listener.exitReturn_type(self)




    def return_type(self):

        localctx = CovidParser.Return_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_return_type)
        try:
            self.state = 206
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CovidParser.INT, CovidParser.FLOAT, CovidParser.CHAR, CovidParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 204
                self.tipo_atom()
                pass
            elif token in [CovidParser.VOID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 205
                self.match(CovidParser.VOID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo_atom(self):
            return self.getTypedRuleContext(CovidParser.Tipo_atomContext,0)


        def ID(self):
            return self.getToken(CovidParser.ID, 0)

        def param(self):
            return self.getTypedRuleContext(CovidParser.ParamContext,0)


        def getRuleIndex(self):
            return CovidParser.RULE_params

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParams" ):
                listener.enterParams(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParams" ):
                listener.exitParams(self)




    def params(self):

        localctx = CovidParser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_params)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.tipo_atom()
            self.state = 209
            self.match(CovidParser.ID)
            self.state = 210
            self.param()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(CovidParser.COMMA, 0)

        def tipo_atom(self):
            return self.getTypedRuleContext(CovidParser.Tipo_atomContext,0)


        def ID(self):
            return self.getToken(CovidParser.ID, 0)

        def param(self):
            return self.getTypedRuleContext(CovidParser.ParamContext,0)


        def getRuleIndex(self):
            return CovidParser.RULE_param

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam" ):
                listener.enterParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam" ):
                listener.exitParam(self)




    def param(self):

        localctx = CovidParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_param)
        try:
            self.state = 218
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CovidParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 212
                self.match(CovidParser.COMMA)
                self.state = 213
                self.tipo_atom()
                self.state = 214
                self.match(CovidParser.ID)
                self.state = 215
                self.param()
                pass
            elif token in [CovidParser.PARENS_R]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CURLY_L(self):
            return self.getToken(CovidParser.CURLY_L, 0)

        def CURLY_R(self):
            return self.getToken(CovidParser.CURLY_R, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CovidParser.StatementContext)
            else:
                return self.getTypedRuleContext(CovidParser.StatementContext,i)


        def getRuleIndex(self):
            return CovidParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = CovidParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            self.match(CovidParser.CURLY_L)
            self.state = 224
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CovidParser.IF) | (1 << CovidParser.WHILE) | (1 << CovidParser.FOR) | (1 << CovidParser.PRINT) | (1 << CovidParser.RETURN) | (1 << CovidParser.INPUT) | (1 << CovidParser.LOAD_FILE) | (1 << CovidParser.LOAD_DATA) | (1 << CovidParser.AVG) | (1 << CovidParser.MODE) | (1 << CovidParser.RANGE) | (1 << CovidParser.VARIANCE) | (1 << CovidParser.STD_DEV) | (1 << CovidParser.MAX) | (1 << CovidParser.MIN) | (1 << CovidParser.PLOT) | (1 << CovidParser.HISTOGRAM) | (1 << CovidParser.CORREL) | (1 << CovidParser.ID))) != 0):
                self.state = 221
                self.statement()
                self.state = 226
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 227
            self.match(CovidParser.CURLY_R)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MainContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MAIN(self):
            return self.getToken(CovidParser.MAIN, 0)

        def PARENS_L(self):
            return self.getToken(CovidParser.PARENS_L, 0)

        def PARENS_R(self):
            return self.getToken(CovidParser.PARENS_R, 0)

        def SEMI(self):
            return self.getToken(CovidParser.SEMI, 0)

        def block(self):
            return self.getTypedRuleContext(CovidParser.BlockContext,0)


        def var_block(self):
            return self.getTypedRuleContext(CovidParser.Var_blockContext,0)


        def getRuleIndex(self):
            return CovidParser.RULE_main

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMain" ):
                listener.enterMain(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMain" ):
                listener.exitMain(self)




    def main(self):

        localctx = CovidParser.MainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_main)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.match(CovidParser.MAIN)
            self.state = 230
            self.match(CovidParser.PARENS_L)
            self.state = 231
            self.match(CovidParser.PARENS_R)
            self.state = 232
            self.match(CovidParser.SEMI)
            self.state = 234
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CovidParser.VAR:
                self.state = 233
                self.var_block()


            self.state = 236
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(CovidParser.AssignmentContext,0)


        def call(self):
            return self.getTypedRuleContext(CovidParser.CallContext,0)


        def SEMI(self):
            return self.getToken(CovidParser.SEMI, 0)

        def regresa(self):
            return self.getTypedRuleContext(CovidParser.RegresaContext,0)


        def read(self):
            return self.getTypedRuleContext(CovidParser.ReadContext,0)


        def write(self):
            return self.getTypedRuleContext(CovidParser.WriteContext,0)


        def decision(self):
            return self.getTypedRuleContext(CovidParser.DecisionContext,0)


        def while_loop(self):
            return self.getTypedRuleContext(CovidParser.While_loopContext,0)


        def for_loop(self):
            return self.getTypedRuleContext(CovidParser.For_loopContext,0)


        def covid(self):
            return self.getTypedRuleContext(CovidParser.CovidContext,0)


        def getRuleIndex(self):
            return CovidParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = CovidParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_statement)
        try:
            self.state = 251
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 238
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 239
                self.call()
                self.state = 240
                self.match(CovidParser.SEMI)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 242
                self.regresa()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 243
                self.read()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 244
                self.write()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 245
                self.decision()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 246
                self.while_loop()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 247
                self.for_loop()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 248
                self.covid()
                self.state = 249
                self.match(CovidParser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ident(self):
            return self.getTypedRuleContext(CovidParser.IdentContext,0)


        def ASGN(self):
            return self.getToken(CovidParser.ASGN, 0)

        def expr(self):
            return self.getTypedRuleContext(CovidParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(CovidParser.SEMI, 0)

        def getRuleIndex(self):
            return CovidParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = CovidParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.ident()
            self.state = 254
            self.match(CovidParser.ASGN)
            self.state = 255
            self.expr()
            self.state = 256
            self.match(CovidParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CovidParser.ID, 0)

        def PARENS_L(self):
            return self.getToken(CovidParser.PARENS_L, 0)

        def args(self):
            return self.getTypedRuleContext(CovidParser.ArgsContext,0)


        def PARENS_R(self):
            return self.getToken(CovidParser.PARENS_R, 0)

        def getRuleIndex(self):
            return CovidParser.RULE_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCall" ):
                listener.enterCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCall" ):
                listener.exitCall(self)




    def call(self):

        localctx = CovidParser.CallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            self.match(CovidParser.ID)
            self.state = 259
            self.match(CovidParser.PARENS_L)
            self.state = 260
            self.args()
            self.state = 261
            self.match(CovidParser.PARENS_R)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CovidParser.ExprContext)
            else:
                return self.getTypedRuleContext(CovidParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CovidParser.COMMA)
            else:
                return self.getToken(CovidParser.COMMA, i)

        def getRuleIndex(self):
            return CovidParser.RULE_args

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgs" ):
                listener.enterArgs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgs" ):
                listener.exitArgs(self)




    def args(self):

        localctx = CovidParser.ArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_args)
        self._la = 0 # Token type
        try:
            self.state = 272
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CovidParser.PARENS_L, CovidParser.NOT, CovidParser.LOAD_FILE, CovidParser.LOAD_DATA, CovidParser.AVG, CovidParser.MODE, CovidParser.RANGE, CovidParser.VARIANCE, CovidParser.STD_DEV, CovidParser.MAX, CovidParser.MIN, CovidParser.PLOT, CovidParser.HISTOGRAM, CovidParser.CORREL, CovidParser.INT_CTE, CovidParser.FLOAT_CTE, CovidParser.STRING_CTE, CovidParser.CHAR_CTE, CovidParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 263
                self.expr()
                self.state = 268
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==CovidParser.COMMA:
                    self.state = 264
                    self.match(CovidParser.COMMA)
                    self.state = 265
                    self.expr()
                    self.state = 270
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [CovidParser.PARENS_R]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RegresaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(CovidParser.RETURN, 0)

        def PARENS_L(self):
            return self.getToken(CovidParser.PARENS_L, 0)

        def expr(self):
            return self.getTypedRuleContext(CovidParser.ExprContext,0)


        def PARENS_R(self):
            return self.getToken(CovidParser.PARENS_R, 0)

        def SEMI(self):
            return self.getToken(CovidParser.SEMI, 0)

        def getRuleIndex(self):
            return CovidParser.RULE_regresa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRegresa" ):
                listener.enterRegresa(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRegresa" ):
                listener.exitRegresa(self)




    def regresa(self):

        localctx = CovidParser.RegresaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_regresa)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            self.match(CovidParser.RETURN)
            self.state = 275
            self.match(CovidParser.PARENS_L)
            self.state = 276
            self.expr()
            self.state = 277
            self.match(CovidParser.PARENS_R)
            self.state = 278
            self.match(CovidParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReadContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INPUT(self):
            return self.getToken(CovidParser.INPUT, 0)

        def PARENS_L(self):
            return self.getToken(CovidParser.PARENS_L, 0)

        def ids(self):
            return self.getTypedRuleContext(CovidParser.IdsContext,0)


        def PARENS_R(self):
            return self.getToken(CovidParser.PARENS_R, 0)

        def SEMI(self):
            return self.getToken(CovidParser.SEMI, 0)

        def getRuleIndex(self):
            return CovidParser.RULE_read

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRead" ):
                listener.enterRead(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRead" ):
                listener.exitRead(self)




    def read(self):

        localctx = CovidParser.ReadContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_read)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
            self.match(CovidParser.INPUT)
            self.state = 281
            self.match(CovidParser.PARENS_L)
            self.state = 282
            self.ids()
            self.state = 283
            self.match(CovidParser.PARENS_R)
            self.state = 284
            self.match(CovidParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WriteContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(CovidParser.PRINT, 0)

        def PARENS_L(self):
            return self.getToken(CovidParser.PARENS_L, 0)

        def impr(self):
            return self.getTypedRuleContext(CovidParser.ImprContext,0)


        def PARENS_R(self):
            return self.getToken(CovidParser.PARENS_R, 0)

        def SEMI(self):
            return self.getToken(CovidParser.SEMI, 0)

        def getRuleIndex(self):
            return CovidParser.RULE_write

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWrite" ):
                listener.enterWrite(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWrite" ):
                listener.exitWrite(self)




    def write(self):

        localctx = CovidParser.WriteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_write)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self.match(CovidParser.PRINT)
            self.state = 287
            self.match(CovidParser.PARENS_L)
            self.state = 288
            self.impr()
            self.state = 289
            self.match(CovidParser.PARENS_R)
            self.state = 290
            self.match(CovidParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(CovidParser.ExprContext,0)


        def imprs(self):
            return self.getTypedRuleContext(CovidParser.ImprsContext,0)


        def getRuleIndex(self):
            return CovidParser.RULE_impr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImpr" ):
                listener.enterImpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImpr" ):
                listener.exitImpr(self)




    def impr(self):

        localctx = CovidParser.ImprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_impr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 292
            self.expr()
            self.state = 293
            self.imprs()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImprsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(CovidParser.COMMA, 0)

        def expr(self):
            return self.getTypedRuleContext(CovidParser.ExprContext,0)


        def imprs(self):
            return self.getTypedRuleContext(CovidParser.ImprsContext,0)


        def getRuleIndex(self):
            return CovidParser.RULE_imprs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImprs" ):
                listener.enterImprs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImprs" ):
                listener.exitImprs(self)




    def imprs(self):

        localctx = CovidParser.ImprsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_imprs)
        try:
            self.state = 300
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CovidParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 295
                self.match(CovidParser.COMMA)
                self.state = 296
                self.expr()
                self.state = 297
                self.imprs()
                pass
            elif token in [CovidParser.PARENS_R]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DecisionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(CovidParser.IF, 0)

        def PARENS_L(self):
            return self.getToken(CovidParser.PARENS_L, 0)

        def expr(self):
            return self.getTypedRuleContext(CovidParser.ExprContext,0)


        def PARENS_R(self):
            return self.getToken(CovidParser.PARENS_R, 0)

        def block(self):
            return self.getTypedRuleContext(CovidParser.BlockContext,0)


        def else_block(self):
            return self.getTypedRuleContext(CovidParser.Else_blockContext,0)


        def getRuleIndex(self):
            return CovidParser.RULE_decision

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecision" ):
                listener.enterDecision(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecision" ):
                listener.exitDecision(self)




    def decision(self):

        localctx = CovidParser.DecisionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_decision)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302
            self.match(CovidParser.IF)
            self.state = 303
            self.match(CovidParser.PARENS_L)
            self.state = 304
            self.expr()
            self.state = 305
            self.match(CovidParser.PARENS_R)
            self.state = 306
            self.block()
            self.state = 308
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CovidParser.ELSE:
                self.state = 307
                self.else_block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_blockContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(CovidParser.ELSE, 0)

        def block(self):
            return self.getTypedRuleContext(CovidParser.BlockContext,0)


        def getRuleIndex(self):
            return CovidParser.RULE_else_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElse_block" ):
                listener.enterElse_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElse_block" ):
                listener.exitElse_block(self)




    def else_block(self):

        localctx = CovidParser.Else_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_else_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 310
            self.match(CovidParser.ELSE)
            self.state = 311
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_loopContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(CovidParser.WHILE, 0)

        def PARENS_L(self):
            return self.getToken(CovidParser.PARENS_L, 0)

        def expr(self):
            return self.getTypedRuleContext(CovidParser.ExprContext,0)


        def PARENS_R(self):
            return self.getToken(CovidParser.PARENS_R, 0)

        def block(self):
            return self.getTypedRuleContext(CovidParser.BlockContext,0)


        def getRuleIndex(self):
            return CovidParser.RULE_while_loop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_loop" ):
                listener.enterWhile_loop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_loop" ):
                listener.exitWhile_loop(self)




    def while_loop(self):

        localctx = CovidParser.While_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_while_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 313
            self.match(CovidParser.WHILE)
            self.state = 314
            self.match(CovidParser.PARENS_L)
            self.state = 315
            self.expr()
            self.state = 316
            self.match(CovidParser.PARENS_R)
            self.state = 317
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_loopContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(CovidParser.FOR, 0)

        def for_asgn(self):
            return self.getTypedRuleContext(CovidParser.For_asgnContext,0)


        def TO(self):
            return self.getToken(CovidParser.TO, 0)

        def expr(self):
            return self.getTypedRuleContext(CovidParser.ExprContext,0)


        def block(self):
            return self.getTypedRuleContext(CovidParser.BlockContext,0)


        def getRuleIndex(self):
            return CovidParser.RULE_for_loop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_loop" ):
                listener.enterFor_loop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_loop" ):
                listener.exitFor_loop(self)




    def for_loop(self):

        localctx = CovidParser.For_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_for_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 319
            self.match(CovidParser.FOR)
            self.state = 320
            self.for_asgn()
            self.state = 321
            self.match(CovidParser.TO)
            self.state = 322
            self.expr()
            self.state = 323
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_asgnContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CovidParser.ID, 0)

        def ASGN(self):
            return self.getToken(CovidParser.ASGN, 0)

        def expr(self):
            return self.getTypedRuleContext(CovidParser.ExprContext,0)


        def getRuleIndex(self):
            return CovidParser.RULE_for_asgn

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_asgn" ):
                listener.enterFor_asgn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_asgn" ):
                listener.exitFor_asgn(self)




    def for_asgn(self):

        localctx = CovidParser.For_asgnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_for_asgn)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 325
            self.match(CovidParser.ID)
            self.state = 326
            self.match(CovidParser.ASGN)
            self.state = 327
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def and_term(self):
            return self.getTypedRuleContext(CovidParser.And_termContext,0)


        def exprs(self):
            return self.getTypedRuleContext(CovidParser.ExprsContext,0)


        def getRuleIndex(self):
            return CovidParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = CovidParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 329
            self.and_term()
            self.state = 330
            self.exprs()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OR(self):
            return self.getToken(CovidParser.OR, 0)

        def and_term(self):
            return self.getTypedRuleContext(CovidParser.And_termContext,0)


        def exprs(self):
            return self.getTypedRuleContext(CovidParser.ExprsContext,0)


        def getRuleIndex(self):
            return CovidParser.RULE_exprs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprs" ):
                listener.enterExprs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprs" ):
                listener.exitExprs(self)




    def exprs(self):

        localctx = CovidParser.ExprsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_exprs)
        try:
            self.state = 337
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CovidParser.OR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 332
                self.match(CovidParser.OR)
                self.state = 333
                self.and_term()
                self.state = 334
                self.exprs()
                pass
            elif token in [CovidParser.SEMI, CovidParser.COMMA, CovidParser.CURLY_L, CovidParser.PARENS_R, CovidParser.SQUARE_R, CovidParser.TO]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class And_termContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comp_term(self):
            return self.getTypedRuleContext(CovidParser.Comp_termContext,0)


        def and_terms(self):
            return self.getTypedRuleContext(CovidParser.And_termsContext,0)


        def getRuleIndex(self):
            return CovidParser.RULE_and_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnd_term" ):
                listener.enterAnd_term(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnd_term" ):
                listener.exitAnd_term(self)




    def and_term(self):

        localctx = CovidParser.And_termContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_and_term)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 339
            self.comp_term()
            self.state = 340
            self.and_terms()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class And_termsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AND(self):
            return self.getToken(CovidParser.AND, 0)

        def comp_term(self):
            return self.getTypedRuleContext(CovidParser.Comp_termContext,0)


        def and_terms(self):
            return self.getTypedRuleContext(CovidParser.And_termsContext,0)


        def getRuleIndex(self):
            return CovidParser.RULE_and_terms

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnd_terms" ):
                listener.enterAnd_terms(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnd_terms" ):
                listener.exitAnd_terms(self)




    def and_terms(self):

        localctx = CovidParser.And_termsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_and_terms)
        try:
            self.state = 347
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CovidParser.AND]:
                self.enterOuterAlt(localctx, 1)
                self.state = 342
                self.match(CovidParser.AND)
                self.state = 343
                self.comp_term()
                self.state = 344
                self.and_terms()
                pass
            elif token in [CovidParser.SEMI, CovidParser.COMMA, CovidParser.CURLY_L, CovidParser.PARENS_R, CovidParser.SQUARE_R, CovidParser.OR, CovidParser.TO]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Comp_termContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def rel_term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CovidParser.Rel_termContext)
            else:
                return self.getTypedRuleContext(CovidParser.Rel_termContext,i)


        def comp_op(self):
            return self.getTypedRuleContext(CovidParser.Comp_opContext,0)


        def getRuleIndex(self):
            return CovidParser.RULE_comp_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComp_term" ):
                listener.enterComp_term(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComp_term" ):
                listener.exitComp_term(self)




    def comp_term(self):

        localctx = CovidParser.Comp_termContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_comp_term)
        try:
            self.state = 354
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 349
                self.rel_term()
                self.state = 350
                self.comp_op()
                self.state = 351
                self.rel_term()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 353
                self.rel_term()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Comp_opContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQ(self):
            return self.getToken(CovidParser.EQ, 0)

        def NE(self):
            return self.getToken(CovidParser.NE, 0)

        def getRuleIndex(self):
            return CovidParser.RULE_comp_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComp_op" ):
                listener.enterComp_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComp_op" ):
                listener.exitComp_op(self)




    def comp_op(self):

        localctx = CovidParser.Comp_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_comp_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 356
            _la = self._input.LA(1)
            if not(_la==CovidParser.EQ or _la==CovidParser.NE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Rel_termContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def artm_term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CovidParser.Artm_termContext)
            else:
                return self.getTypedRuleContext(CovidParser.Artm_termContext,i)


        def rel_op(self):
            return self.getTypedRuleContext(CovidParser.Rel_opContext,0)


        def getRuleIndex(self):
            return CovidParser.RULE_rel_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRel_term" ):
                listener.enterRel_term(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRel_term" ):
                listener.exitRel_term(self)




    def rel_term(self):

        localctx = CovidParser.Rel_termContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_rel_term)
        try:
            self.state = 363
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 358
                self.artm_term()
                self.state = 359
                self.rel_op()
                self.state = 360
                self.artm_term()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 362
                self.artm_term()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Rel_opContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LT(self):
            return self.getToken(CovidParser.LT, 0)

        def GT(self):
            return self.getToken(CovidParser.GT, 0)

        def LTE(self):
            return self.getToken(CovidParser.LTE, 0)

        def GTE(self):
            return self.getToken(CovidParser.GTE, 0)

        def getRuleIndex(self):
            return CovidParser.RULE_rel_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRel_op" ):
                listener.enterRel_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRel_op" ):
                listener.exitRel_op(self)




    def rel_op(self):

        localctx = CovidParser.Rel_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_rel_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 365
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CovidParser.LTE) | (1 << CovidParser.GTE) | (1 << CovidParser.LT) | (1 << CovidParser.GT))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Artm_termContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fact_term(self):
            return self.getTypedRuleContext(CovidParser.Fact_termContext,0)


        def artm_terms(self):
            return self.getTypedRuleContext(CovidParser.Artm_termsContext,0)


        def getRuleIndex(self):
            return CovidParser.RULE_artm_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArtm_term" ):
                listener.enterArtm_term(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArtm_term" ):
                listener.exitArtm_term(self)




    def artm_term(self):

        localctx = CovidParser.Artm_termContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_artm_term)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 367
            self.fact_term()
            self.state = 368
            self.artm_terms()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Artm_termsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fact_term(self):
            return self.getTypedRuleContext(CovidParser.Fact_termContext,0)


        def artm_terms(self):
            return self.getTypedRuleContext(CovidParser.Artm_termsContext,0)


        def PLUS(self):
            return self.getToken(CovidParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(CovidParser.MINUS, 0)

        def getRuleIndex(self):
            return CovidParser.RULE_artm_terms

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArtm_terms" ):
                listener.enterArtm_terms(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArtm_terms" ):
                listener.exitArtm_terms(self)




    def artm_terms(self):

        localctx = CovidParser.Artm_termsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_artm_terms)
        self._la = 0 # Token type
        try:
            self.state = 375
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CovidParser.PLUS, CovidParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 370
                _la = self._input.LA(1)
                if not(_la==CovidParser.PLUS or _la==CovidParser.MINUS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 371
                self.fact_term()
                self.state = 372
                self.artm_terms()
                pass
            elif token in [CovidParser.SEMI, CovidParser.COMMA, CovidParser.CURLY_L, CovidParser.PARENS_R, CovidParser.SQUARE_R, CovidParser.EQ, CovidParser.NE, CovidParser.LTE, CovidParser.GTE, CovidParser.LT, CovidParser.GT, CovidParser.OR, CovidParser.AND, CovidParser.TO]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Fact_termContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operand(self):
            return self.getTypedRuleContext(CovidParser.OperandContext,0)


        def fact_terms(self):
            return self.getTypedRuleContext(CovidParser.Fact_termsContext,0)


        def getRuleIndex(self):
            return CovidParser.RULE_fact_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFact_term" ):
                listener.enterFact_term(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFact_term" ):
                listener.exitFact_term(self)




    def fact_term(self):

        localctx = CovidParser.Fact_termContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_fact_term)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 377
            self.operand()
            self.state = 378
            self.fact_terms()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Fact_termsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operand(self):
            return self.getTypedRuleContext(CovidParser.OperandContext,0)


        def fact_terms(self):
            return self.getTypedRuleContext(CovidParser.Fact_termsContext,0)


        def MULT(self):
            return self.getToken(CovidParser.MULT, 0)

        def DIVIDE(self):
            return self.getToken(CovidParser.DIVIDE, 0)

        def getRuleIndex(self):
            return CovidParser.RULE_fact_terms

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFact_terms" ):
                listener.enterFact_terms(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFact_terms" ):
                listener.exitFact_terms(self)




    def fact_terms(self):

        localctx = CovidParser.Fact_termsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_fact_terms)
        self._la = 0 # Token type
        try:
            self.state = 385
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CovidParser.MULT, CovidParser.DIVIDE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 380
                _la = self._input.LA(1)
                if not(_la==CovidParser.MULT or _la==CovidParser.DIVIDE):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 381
                self.operand()
                self.state = 382
                self.fact_terms()
                pass
            elif token in [CovidParser.PLUS, CovidParser.MINUS, CovidParser.SEMI, CovidParser.COMMA, CovidParser.CURLY_L, CovidParser.PARENS_R, CovidParser.SQUARE_R, CovidParser.EQ, CovidParser.NE, CovidParser.LTE, CovidParser.GTE, CovidParser.LT, CovidParser.GT, CovidParser.OR, CovidParser.AND, CovidParser.TO]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PARENS_L(self):
            return self.getToken(CovidParser.PARENS_L, 0)

        def expr(self):
            return self.getTypedRuleContext(CovidParser.ExprContext,0)


        def PARENS_R(self):
            return self.getToken(CovidParser.PARENS_R, 0)

        def NOT(self):
            return self.getToken(CovidParser.NOT, 0)

        def cte(self):
            return self.getTypedRuleContext(CovidParser.CteContext,0)


        def ident(self):
            return self.getTypedRuleContext(CovidParser.IdentContext,0)


        def call(self):
            return self.getTypedRuleContext(CovidParser.CallContext,0)


        def covid(self):
            return self.getTypedRuleContext(CovidParser.CovidContext,0)


        def getRuleIndex(self):
            return CovidParser.RULE_operand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperand" ):
                listener.enterOperand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperand" ):
                listener.exitOperand(self)




    def operand(self):

        localctx = CovidParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_operand)
        self._la = 0 # Token type
        try:
            self.state = 407
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 388
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CovidParser.NOT:
                    self.state = 387
                    self.match(CovidParser.NOT)


                self.state = 390
                self.match(CovidParser.PARENS_L)
                self.state = 391
                self.expr()
                self.state = 392
                self.match(CovidParser.PARENS_R)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 395
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CovidParser.NOT:
                    self.state = 394
                    self.match(CovidParser.NOT)


                self.state = 397
                self.cte()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 399
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CovidParser.NOT:
                    self.state = 398
                    self.match(CovidParser.NOT)


                self.state = 401
                self.ident()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 403
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CovidParser.NOT:
                    self.state = 402
                    self.match(CovidParser.NOT)


                self.state = 405
                self.call()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 406
                self.covid()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CteContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_CTE(self):
            return self.getToken(CovidParser.INT_CTE, 0)

        def FLOAT_CTE(self):
            return self.getToken(CovidParser.FLOAT_CTE, 0)

        def CHAR_CTE(self):
            return self.getToken(CovidParser.CHAR_CTE, 0)

        def STRING_CTE(self):
            return self.getToken(CovidParser.STRING_CTE, 0)

        def getRuleIndex(self):
            return CovidParser.RULE_cte

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCte" ):
                listener.enterCte(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCte" ):
                listener.exitCte(self)




    def cte(self):

        localctx = CovidParser.CteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_cte)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 409
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CovidParser.INT_CTE) | (1 << CovidParser.FLOAT_CTE) | (1 << CovidParser.STRING_CTE) | (1 << CovidParser.CHAR_CTE))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CovidContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def load_file(self):
            return self.getTypedRuleContext(CovidParser.Load_fileContext,0)


        def load_data(self):
            return self.getTypedRuleContext(CovidParser.Load_dataContext,0)


        def avg(self):
            return self.getTypedRuleContext(CovidParser.AvgContext,0)


        def moda(self):
            return self.getTypedRuleContext(CovidParser.ModaContext,0)


        def rango(self):
            return self.getTypedRuleContext(CovidParser.RangoContext,0)


        def variance(self):
            return self.getTypedRuleContext(CovidParser.VarianceContext,0)


        def std_dev(self):
            return self.getTypedRuleContext(CovidParser.Std_devContext,0)


        def maxi(self):
            return self.getTypedRuleContext(CovidParser.MaxiContext,0)


        def mini(self):
            return self.getTypedRuleContext(CovidParser.MiniContext,0)


        def plot(self):
            return self.getTypedRuleContext(CovidParser.PlotContext,0)


        def histogram(self):
            return self.getTypedRuleContext(CovidParser.HistogramContext,0)


        def correl(self):
            return self.getTypedRuleContext(CovidParser.CorrelContext,0)


        def getRuleIndex(self):
            return CovidParser.RULE_covid

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCovid" ):
                listener.enterCovid(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCovid" ):
                listener.exitCovid(self)




    def covid(self):

        localctx = CovidParser.CovidContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_covid)
        try:
            self.state = 423
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CovidParser.LOAD_FILE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 411
                self.load_file()
                pass
            elif token in [CovidParser.LOAD_DATA]:
                self.enterOuterAlt(localctx, 2)
                self.state = 412
                self.load_data()
                pass
            elif token in [CovidParser.AVG]:
                self.enterOuterAlt(localctx, 3)
                self.state = 413
                self.avg()
                pass
            elif token in [CovidParser.MODE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 414
                self.moda()
                pass
            elif token in [CovidParser.RANGE]:
                self.enterOuterAlt(localctx, 5)
                self.state = 415
                self.rango()
                pass
            elif token in [CovidParser.VARIANCE]:
                self.enterOuterAlt(localctx, 6)
                self.state = 416
                self.variance()
                pass
            elif token in [CovidParser.STD_DEV]:
                self.enterOuterAlt(localctx, 7)
                self.state = 417
                self.std_dev()
                pass
            elif token in [CovidParser.MAX]:
                self.enterOuterAlt(localctx, 8)
                self.state = 418
                self.maxi()
                pass
            elif token in [CovidParser.MIN]:
                self.enterOuterAlt(localctx, 9)
                self.state = 419
                self.mini()
                pass
            elif token in [CovidParser.PLOT]:
                self.enterOuterAlt(localctx, 10)
                self.state = 420
                self.plot()
                pass
            elif token in [CovidParser.HISTOGRAM]:
                self.enterOuterAlt(localctx, 11)
                self.state = 421
                self.histogram()
                pass
            elif token in [CovidParser.CORREL]:
                self.enterOuterAlt(localctx, 12)
                self.state = 422
                self.correl()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Load_fileContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LOAD_FILE(self):
            return self.getToken(CovidParser.LOAD_FILE, 0)

        def PARENS_L(self):
            return self.getToken(CovidParser.PARENS_L, 0)

        def operand(self):
            return self.getTypedRuleContext(CovidParser.OperandContext,0)


        def PARENS_R(self):
            return self.getToken(CovidParser.PARENS_R, 0)

        def getRuleIndex(self):
            return CovidParser.RULE_load_file

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoad_file" ):
                listener.enterLoad_file(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoad_file" ):
                listener.exitLoad_file(self)




    def load_file(self):

        localctx = CovidParser.Load_fileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_load_file)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 425
            self.match(CovidParser.LOAD_FILE)
            self.state = 426
            self.match(CovidParser.PARENS_L)
            self.state = 427
            self.operand()
            self.state = 428
            self.match(CovidParser.PARENS_R)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Load_dataContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LOAD_DATA(self):
            return self.getToken(CovidParser.LOAD_DATA, 0)

        def PARENS_L(self):
            return self.getToken(CovidParser.PARENS_L, 0)

        def ident(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CovidParser.IdentContext)
            else:
                return self.getTypedRuleContext(CovidParser.IdentContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CovidParser.COMMA)
            else:
                return self.getToken(CovidParser.COMMA, i)

        def PARENS_R(self):
            return self.getToken(CovidParser.PARENS_R, 0)

        def getRuleIndex(self):
            return CovidParser.RULE_load_data

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoad_data" ):
                listener.enterLoad_data(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoad_data" ):
                listener.exitLoad_data(self)




    def load_data(self):

        localctx = CovidParser.Load_dataContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_load_data)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 430
            self.match(CovidParser.LOAD_DATA)
            self.state = 431
            self.match(CovidParser.PARENS_L)
            self.state = 432
            self.ident()
            self.state = 433
            self.match(CovidParser.COMMA)
            self.state = 434
            self.ident()
            self.state = 435
            self.match(CovidParser.COMMA)
            self.state = 436
            self.ident()
            self.state = 437
            self.match(CovidParser.PARENS_R)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AvgContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AVG(self):
            return self.getToken(CovidParser.AVG, 0)

        def PARENS_L(self):
            return self.getToken(CovidParser.PARENS_L, 0)

        def ident(self):
            return self.getTypedRuleContext(CovidParser.IdentContext,0)


        def COMMA(self):
            return self.getToken(CovidParser.COMMA, 0)

        def operand(self):
            return self.getTypedRuleContext(CovidParser.OperandContext,0)


        def PARENS_R(self):
            return self.getToken(CovidParser.PARENS_R, 0)

        def getRuleIndex(self):
            return CovidParser.RULE_avg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAvg" ):
                listener.enterAvg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAvg" ):
                listener.exitAvg(self)




    def avg(self):

        localctx = CovidParser.AvgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_avg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 439
            self.match(CovidParser.AVG)
            self.state = 440
            self.match(CovidParser.PARENS_L)
            self.state = 441
            self.ident()
            self.state = 442
            self.match(CovidParser.COMMA)
            self.state = 443
            self.operand()
            self.state = 444
            self.match(CovidParser.PARENS_R)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ModaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MODE(self):
            return self.getToken(CovidParser.MODE, 0)

        def PARENS_L(self):
            return self.getToken(CovidParser.PARENS_L, 0)

        def ident(self):
            return self.getTypedRuleContext(CovidParser.IdentContext,0)


        def COMMA(self):
            return self.getToken(CovidParser.COMMA, 0)

        def operand(self):
            return self.getTypedRuleContext(CovidParser.OperandContext,0)


        def PARENS_R(self):
            return self.getToken(CovidParser.PARENS_R, 0)

        def getRuleIndex(self):
            return CovidParser.RULE_moda

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModa" ):
                listener.enterModa(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModa" ):
                listener.exitModa(self)




    def moda(self):

        localctx = CovidParser.ModaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_moda)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 446
            self.match(CovidParser.MODE)
            self.state = 447
            self.match(CovidParser.PARENS_L)
            self.state = 448
            self.ident()
            self.state = 449
            self.match(CovidParser.COMMA)
            self.state = 450
            self.operand()
            self.state = 451
            self.match(CovidParser.PARENS_R)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RangoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RANGE(self):
            return self.getToken(CovidParser.RANGE, 0)

        def PARENS_L(self):
            return self.getToken(CovidParser.PARENS_L, 0)

        def ident(self):
            return self.getTypedRuleContext(CovidParser.IdentContext,0)


        def COMMA(self):
            return self.getToken(CovidParser.COMMA, 0)

        def operand(self):
            return self.getTypedRuleContext(CovidParser.OperandContext,0)


        def PARENS_R(self):
            return self.getToken(CovidParser.PARENS_R, 0)

        def getRuleIndex(self):
            return CovidParser.RULE_rango

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRango" ):
                listener.enterRango(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRango" ):
                listener.exitRango(self)




    def rango(self):

        localctx = CovidParser.RangoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_rango)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 453
            self.match(CovidParser.RANGE)
            self.state = 454
            self.match(CovidParser.PARENS_L)
            self.state = 455
            self.ident()
            self.state = 456
            self.match(CovidParser.COMMA)
            self.state = 457
            self.operand()
            self.state = 458
            self.match(CovidParser.PARENS_R)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarianceContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIANCE(self):
            return self.getToken(CovidParser.VARIANCE, 0)

        def PARENS_L(self):
            return self.getToken(CovidParser.PARENS_L, 0)

        def ident(self):
            return self.getTypedRuleContext(CovidParser.IdentContext,0)


        def COMMA(self):
            return self.getToken(CovidParser.COMMA, 0)

        def operand(self):
            return self.getTypedRuleContext(CovidParser.OperandContext,0)


        def PARENS_R(self):
            return self.getToken(CovidParser.PARENS_R, 0)

        def getRuleIndex(self):
            return CovidParser.RULE_variance

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariance" ):
                listener.enterVariance(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariance" ):
                listener.exitVariance(self)




    def variance(self):

        localctx = CovidParser.VarianceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_variance)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 460
            self.match(CovidParser.VARIANCE)
            self.state = 461
            self.match(CovidParser.PARENS_L)
            self.state = 462
            self.ident()
            self.state = 463
            self.match(CovidParser.COMMA)
            self.state = 464
            self.operand()
            self.state = 465
            self.match(CovidParser.PARENS_R)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Std_devContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STD_DEV(self):
            return self.getToken(CovidParser.STD_DEV, 0)

        def PARENS_L(self):
            return self.getToken(CovidParser.PARENS_L, 0)

        def ident(self):
            return self.getTypedRuleContext(CovidParser.IdentContext,0)


        def COMMA(self):
            return self.getToken(CovidParser.COMMA, 0)

        def operand(self):
            return self.getTypedRuleContext(CovidParser.OperandContext,0)


        def PARENS_R(self):
            return self.getToken(CovidParser.PARENS_R, 0)

        def getRuleIndex(self):
            return CovidParser.RULE_std_dev

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStd_dev" ):
                listener.enterStd_dev(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStd_dev" ):
                listener.exitStd_dev(self)




    def std_dev(self):

        localctx = CovidParser.Std_devContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_std_dev)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 467
            self.match(CovidParser.STD_DEV)
            self.state = 468
            self.match(CovidParser.PARENS_L)
            self.state = 469
            self.ident()
            self.state = 470
            self.match(CovidParser.COMMA)
            self.state = 471
            self.operand()
            self.state = 472
            self.match(CovidParser.PARENS_R)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MaxiContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MAX(self):
            return self.getToken(CovidParser.MAX, 0)

        def PARENS_L(self):
            return self.getToken(CovidParser.PARENS_L, 0)

        def ident(self):
            return self.getTypedRuleContext(CovidParser.IdentContext,0)


        def COMMA(self):
            return self.getToken(CovidParser.COMMA, 0)

        def operand(self):
            return self.getTypedRuleContext(CovidParser.OperandContext,0)


        def PARENS_R(self):
            return self.getToken(CovidParser.PARENS_R, 0)

        def getRuleIndex(self):
            return CovidParser.RULE_maxi

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMaxi" ):
                listener.enterMaxi(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMaxi" ):
                listener.exitMaxi(self)




    def maxi(self):

        localctx = CovidParser.MaxiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_maxi)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 474
            self.match(CovidParser.MAX)
            self.state = 475
            self.match(CovidParser.PARENS_L)
            self.state = 476
            self.ident()
            self.state = 477
            self.match(CovidParser.COMMA)
            self.state = 478
            self.operand()
            self.state = 479
            self.match(CovidParser.PARENS_R)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MiniContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MIN(self):
            return self.getToken(CovidParser.MIN, 0)

        def PARENS_L(self):
            return self.getToken(CovidParser.PARENS_L, 0)

        def ident(self):
            return self.getTypedRuleContext(CovidParser.IdentContext,0)


        def COMMA(self):
            return self.getToken(CovidParser.COMMA, 0)

        def operand(self):
            return self.getTypedRuleContext(CovidParser.OperandContext,0)


        def PARENS_R(self):
            return self.getToken(CovidParser.PARENS_R, 0)

        def getRuleIndex(self):
            return CovidParser.RULE_mini

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMini" ):
                listener.enterMini(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMini" ):
                listener.exitMini(self)




    def mini(self):

        localctx = CovidParser.MiniContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_mini)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 481
            self.match(CovidParser.MIN)
            self.state = 482
            self.match(CovidParser.PARENS_L)
            self.state = 483
            self.ident()
            self.state = 484
            self.match(CovidParser.COMMA)
            self.state = 485
            self.operand()
            self.state = 486
            self.match(CovidParser.PARENS_R)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PlotContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLOT(self):
            return self.getToken(CovidParser.PLOT, 0)

        def PARENS_L(self):
            return self.getToken(CovidParser.PARENS_L, 0)

        def ident(self):
            return self.getTypedRuleContext(CovidParser.IdentContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CovidParser.COMMA)
            else:
                return self.getToken(CovidParser.COMMA, i)

        def operand(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CovidParser.OperandContext)
            else:
                return self.getTypedRuleContext(CovidParser.OperandContext,i)


        def PARENS_R(self):
            return self.getToken(CovidParser.PARENS_R, 0)

        def getRuleIndex(self):
            return CovidParser.RULE_plot

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPlot" ):
                listener.enterPlot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPlot" ):
                listener.exitPlot(self)




    def plot(self):

        localctx = CovidParser.PlotContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_plot)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 488
            self.match(CovidParser.PLOT)
            self.state = 489
            self.match(CovidParser.PARENS_L)
            self.state = 490
            self.ident()
            self.state = 491
            self.match(CovidParser.COMMA)
            self.state = 492
            self.operand()
            self.state = 493
            self.match(CovidParser.COMMA)
            self.state = 494
            self.operand()
            self.state = 495
            self.match(CovidParser.PARENS_R)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HistogramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def HISTOGRAM(self):
            return self.getToken(CovidParser.HISTOGRAM, 0)

        def PARENS_L(self):
            return self.getToken(CovidParser.PARENS_L, 0)

        def ident(self):
            return self.getTypedRuleContext(CovidParser.IdentContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CovidParser.COMMA)
            else:
                return self.getToken(CovidParser.COMMA, i)

        def operand(self):
            return self.getTypedRuleContext(CovidParser.OperandContext,0)


        def expr(self):
            return self.getTypedRuleContext(CovidParser.ExprContext,0)


        def PARENS_R(self):
            return self.getToken(CovidParser.PARENS_R, 0)

        def getRuleIndex(self):
            return CovidParser.RULE_histogram

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHistogram" ):
                listener.enterHistogram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHistogram" ):
                listener.exitHistogram(self)




    def histogram(self):

        localctx = CovidParser.HistogramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_histogram)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 497
            self.match(CovidParser.HISTOGRAM)
            self.state = 498
            self.match(CovidParser.PARENS_L)
            self.state = 499
            self.ident()
            self.state = 500
            self.match(CovidParser.COMMA)
            self.state = 501
            self.operand()
            self.state = 502
            self.match(CovidParser.COMMA)
            self.state = 503
            self.expr()
            self.state = 504
            self.match(CovidParser.PARENS_R)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CorrelContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CORREL(self):
            return self.getToken(CovidParser.CORREL, 0)

        def PARENS_L(self):
            return self.getToken(CovidParser.PARENS_L, 0)

        def ident(self):
            return self.getTypedRuleContext(CovidParser.IdentContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CovidParser.COMMA)
            else:
                return self.getToken(CovidParser.COMMA, i)

        def operand(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CovidParser.OperandContext)
            else:
                return self.getTypedRuleContext(CovidParser.OperandContext,i)


        def PARENS_R(self):
            return self.getToken(CovidParser.PARENS_R, 0)

        def getRuleIndex(self):
            return CovidParser.RULE_correl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCorrel" ):
                listener.enterCorrel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCorrel" ):
                listener.exitCorrel(self)




    def correl(self):

        localctx = CovidParser.CorrelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_correl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 506
            self.match(CovidParser.CORREL)
            self.state = 507
            self.match(CovidParser.PARENS_L)
            self.state = 508
            self.ident()
            self.state = 509
            self.match(CovidParser.COMMA)
            self.state = 510
            self.operand()
            self.state = 511
            self.match(CovidParser.COMMA)
            self.state = 512
            self.operand()
            self.state = 513
            self.match(CovidParser.PARENS_R)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





