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
        buf.write("\u0210\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
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
        buf.write("\3\4\3\4\3\4\7\4\u008f\n\4\f\4\16\4\u0092\13\4\3\5\3\5")
        buf.write("\3\5\3\5\5\5\u0098\n\5\3\5\3\5\3\5\5\5\u009d\n\5\3\6\3")
        buf.write("\6\3\6\7\6\u00a2\n\6\f\6\16\6\u00a5\13\6\3\7\3\7\5\7\u00a9")
        buf.write("\n\7\3\7\5\7\u00ac\n\7\3\b\3\b\3\b\3\b\3\t\3\t\5\t\u00b4")
        buf.write("\n\t\3\n\3\n\3\13\3\13\3\13\3\13\3\13\5\13\u00bd\n\13")
        buf.write("\3\13\3\13\3\13\5\13\u00c2\n\13\3\13\3\13\3\f\3\f\5\f")
        buf.write("\u00c8\n\f\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\16\5\16\u00d4\n\16\3\17\3\17\7\17\u00d8\n\17\f\17\16")
        buf.write("\17\u00db\13\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\5\20")
        buf.write("\u00e4\n\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3")
        buf.write("\21\3\21\3\21\3\21\3\21\3\21\3\21\5\21\u00f5\n\21\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\24\3\24")
        buf.write("\3\24\7\24\u0104\n\24\f\24\16\24\u0107\13\24\3\24\5\24")
        buf.write("\u010a\n\24\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3")
        buf.write("\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\30")
        buf.write("\3\30\3\30\3\31\3\31\3\31\3\31\3\31\5\31\u0126\n\31\3")
        buf.write("\32\3\32\3\32\3\32\3\32\3\32\5\32\u012e\n\32\3\33\3\33")
        buf.write("\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3 \3 \3")
        buf.write(" \3 \3 \5 \u014b\n \3!\3!\3!\3\"\3\"\3\"\3\"\3\"\5\"\u0155")
        buf.write("\n\"\3#\3#\3#\3#\3#\5#\u015c\n#\3$\3$\3%\3%\3%\3%\3%\5")
        buf.write("%\u0165\n%\3&\3&\3\'\3\'\3\'\3(\3(\3(\3(\3(\5(\u0171\n")
        buf.write("(\3)\3)\3)\3*\3*\3*\3*\3*\5*\u017b\n*\3+\5+\u017e\n+\3")
        buf.write("+\3+\3+\3+\3+\5+\u0185\n+\3+\3+\5+\u0189\n+\3+\3+\5+\u018d")
        buf.write("\n+\3+\3+\5+\u0191\n+\3,\3,\3-\3-\3-\3-\3-\3-\3-\3-\3")
        buf.write("-\3-\3-\3-\3-\5-\u01a2\n-\3.\3.\3.\3.\3.\3.\5.\u01aa\n")
        buf.write(".\3.\3.\3.\3.\3.\3.\3/\3/\3/\3/\3/\3/\3/\3/\3/\3\60\3")
        buf.write("\60\3\60\3\60\3\60\3\60\3\60\3\61\3\61\3\61\3\61\3\61")
        buf.write("\3\61\3\61\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\63\3\63")
        buf.write("\3\63\3\63\3\63\3\63\3\63\3\64\3\64\3\64\3\64\3\64\3\64")
        buf.write("\3\64\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\66\3\66\3\66")
        buf.write("\3\66\3\66\3\66\3\66\3\67\3\67\3\67\3\67\3\67\3\67\3\67")
        buf.write("\3\67\3\67\38\38\38\38\38\38\38\38\38\39\39\39\39\39\3")
        buf.write("9\39\39\39\3:\3:\3:\3:\3:\3:\3:\3:\3:\3:\2\2;\2\4\6\b")
        buf.write("\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668")
        buf.write(":<>@BDFHJLNPRTVXZ\\^`bdfhjlnpr\2\b\3\2!$\3\2\20\21\3\2")
        buf.write("\23\26\3\2\3\4\3\2\5\6\3\2:=\2\u020d\2t\3\2\2\2\4\u0082")
        buf.write("\3\2\2\2\6\u008b\3\2\2\2\b\u0093\3\2\2\2\n\u009e\3\2\2")
        buf.write("\2\f\u00a6\3\2\2\2\16\u00ad\3\2\2\2\20\u00b3\3\2\2\2\22")
        buf.write("\u00b5\3\2\2\2\24\u00b7\3\2\2\2\26\u00c7\3\2\2\2\30\u00c9")
        buf.write("\3\2\2\2\32\u00d3\3\2\2\2\34\u00d5\3\2\2\2\36\u00de\3")
        buf.write("\2\2\2 \u00f4\3\2\2\2\"\u00f6\3\2\2\2$\u00fb\3\2\2\2&")
        buf.write("\u0109\3\2\2\2(\u010b\3\2\2\2*\u0111\3\2\2\2,\u0117\3")
        buf.write("\2\2\2.\u011d\3\2\2\2\60\u0125\3\2\2\2\62\u0127\3\2\2")
        buf.write("\2\64\u012f\3\2\2\2\66\u0132\3\2\2\28\u0138\3\2\2\2:\u013e")
        buf.write("\3\2\2\2<\u0142\3\2\2\2>\u014a\3\2\2\2@\u014c\3\2\2\2")
        buf.write("B\u0154\3\2\2\2D\u015b\3\2\2\2F\u015d\3\2\2\2H\u0164\3")
        buf.write("\2\2\2J\u0166\3\2\2\2L\u0168\3\2\2\2N\u0170\3\2\2\2P\u0172")
        buf.write("\3\2\2\2R\u017a\3\2\2\2T\u0190\3\2\2\2V\u0192\3\2\2\2")
        buf.write("X\u01a1\3\2\2\2Z\u01a3\3\2\2\2\\\u01b1\3\2\2\2^\u01ba")
        buf.write("\3\2\2\2`\u01c1\3\2\2\2b\u01c8\3\2\2\2d\u01cf\3\2\2\2")
        buf.write("f\u01d6\3\2\2\2h\u01dd\3\2\2\2j\u01e4\3\2\2\2l\u01eb\3")
        buf.write("\2\2\2n\u01f4\3\2\2\2p\u01fd\3\2\2\2r\u0206\3\2\2\2tu")
        buf.write("\7\32\2\2uv\7>\2\2vx\7\7\2\2wy\5\4\3\2xw\3\2\2\2xy\3\2")
        buf.write("\2\2y}\3\2\2\2z|\5\24\13\2{z\3\2\2\2|\177\3\2\2\2}{\3")
        buf.write("\2\2\2}~\3\2\2\2~\u0080\3\2\2\2\177}\3\2\2\2\u0080\u0081")
        buf.write("\5\36\20\2\u0081\3\3\2\2\2\u0082\u0087\7\33\2\2\u0083")
        buf.write("\u0084\5\20\t\2\u0084\u0085\5\6\4\2\u0085\u0086\7\7\2")
        buf.write("\2\u0086\u0088\3\2\2\2\u0087\u0083\3\2\2\2\u0088\u0089")
        buf.write("\3\2\2\2\u0089\u0087\3\2\2\2\u0089\u008a\3\2\2\2\u008a")
        buf.write("\5\3\2\2\2\u008b\u0090\5\b\5\2\u008c\u008d\7\t\2\2\u008d")
        buf.write("\u008f\5\b\5\2\u008e\u008c\3\2\2\2\u008f\u0092\3\2\2\2")
        buf.write("\u0090\u008e\3\2\2\2\u0090\u0091\3\2\2\2\u0091\7\3\2\2")
        buf.write("\2\u0092\u0090\3\2\2\2\u0093\u0097\7>\2\2\u0094\u0095")
        buf.write("\7\16\2\2\u0095\u0096\7:\2\2\u0096\u0098\7\17\2\2\u0097")
        buf.write("\u0094\3\2\2\2\u0097\u0098\3\2\2\2\u0098\u009c\3\2\2\2")
        buf.write("\u0099\u009a\7\16\2\2\u009a\u009b\7:\2\2\u009b\u009d\7")
        buf.write("\17\2\2\u009c\u0099\3\2\2\2\u009c\u009d\3\2\2\2\u009d")
        buf.write("\t\3\2\2\2\u009e\u00a3\5\f\7\2\u009f\u00a0\7\t\2\2\u00a0")
        buf.write("\u00a2\5\f\7\2\u00a1\u009f\3\2\2\2\u00a2\u00a5\3\2\2\2")
        buf.write("\u00a3\u00a1\3\2\2\2\u00a3\u00a4\3\2\2\2\u00a4\13\3\2")
        buf.write("\2\2\u00a5\u00a3\3\2\2\2\u00a6\u00a8\7>\2\2\u00a7\u00a9")
        buf.write("\5\16\b\2\u00a8\u00a7\3\2\2\2\u00a8\u00a9\3\2\2\2\u00a9")
        buf.write("\u00ab\3\2\2\2\u00aa\u00ac\5\16\b\2\u00ab\u00aa\3\2\2")
        buf.write("\2\u00ab\u00ac\3\2\2\2\u00ac\r\3\2\2\2\u00ad\u00ae\7\16")
        buf.write("\2\2\u00ae\u00af\5<\37\2\u00af\u00b0\7\17\2\2\u00b0\17")
        buf.write("\3\2\2\2\u00b1\u00b4\5\22\n\2\u00b2\u00b4\7%\2\2\u00b3")
        buf.write("\u00b1\3\2\2\2\u00b3\u00b2\3\2\2\2\u00b4\21\3\2\2\2\u00b5")
        buf.write("\u00b6\t\2\2\2\u00b6\23\3\2\2\2\u00b7\u00b8\7\'\2\2\u00b8")
        buf.write("\u00b9\5\26\f\2\u00b9\u00ba\7>\2\2\u00ba\u00bc\7\f\2\2")
        buf.write("\u00bb\u00bd\5\30\r\2\u00bc\u00bb\3\2\2\2\u00bc\u00bd")
        buf.write("\3\2\2\2\u00bd\u00be\3\2\2\2\u00be\u00bf\7\r\2\2\u00bf")
        buf.write("\u00c1\7\7\2\2\u00c0\u00c2\5\4\3\2\u00c1\u00c0\3\2\2\2")
        buf.write("\u00c1\u00c2\3\2\2\2\u00c2\u00c3\3\2\2\2\u00c3\u00c4\5")
        buf.write("\34\17\2\u00c4\25\3\2\2\2\u00c5\u00c8\5\22\n\2\u00c6\u00c8")
        buf.write("\7&\2\2\u00c7\u00c5\3\2\2\2\u00c7\u00c6\3\2\2\2\u00c8")
        buf.write("\27\3\2\2\2\u00c9\u00ca\5\22\n\2\u00ca\u00cb\7>\2\2\u00cb")
        buf.write("\u00cc\5\32\16\2\u00cc\31\3\2\2\2\u00cd\u00ce\7\t\2\2")
        buf.write("\u00ce\u00cf\5\22\n\2\u00cf\u00d0\7>\2\2\u00d0\u00d1\5")
        buf.write("\32\16\2\u00d1\u00d4\3\2\2\2\u00d2\u00d4\3\2\2\2\u00d3")
        buf.write("\u00cd\3\2\2\2\u00d3\u00d2\3\2\2\2\u00d4\33\3\2\2\2\u00d5")
        buf.write("\u00d9\7\n\2\2\u00d6\u00d8\5 \21\2\u00d7\u00d6\3\2\2\2")
        buf.write("\u00d8\u00db\3\2\2\2\u00d9\u00d7\3\2\2\2\u00d9\u00da\3")
        buf.write("\2\2\2\u00da\u00dc\3\2\2\2\u00db\u00d9\3\2\2\2\u00dc\u00dd")
        buf.write("\7\13\2\2\u00dd\35\3\2\2\2\u00de\u00df\7)\2\2\u00df\u00e0")
        buf.write("\7\f\2\2\u00e0\u00e1\7\r\2\2\u00e1\u00e3\7\7\2\2\u00e2")
        buf.write("\u00e4\5\4\3\2\u00e3\u00e2\3\2\2\2\u00e3\u00e4\3\2\2\2")
        buf.write("\u00e4\u00e5\3\2\2\2\u00e5\u00e6\5\34\17\2\u00e6\37\3")
        buf.write("\2\2\2\u00e7\u00f5\5\"\22\2\u00e8\u00e9\5$\23\2\u00e9")
        buf.write("\u00ea\7\7\2\2\u00ea\u00f5\3\2\2\2\u00eb\u00f5\5(\25\2")
        buf.write("\u00ec\u00f5\5*\26\2\u00ed\u00f5\5,\27\2\u00ee\u00f5\5")
        buf.write("\62\32\2\u00ef\u00f5\5\66\34\2\u00f0\u00f5\58\35\2\u00f1")
        buf.write("\u00f2\5X-\2\u00f2\u00f3\7\7\2\2\u00f3\u00f5\3\2\2\2\u00f4")
        buf.write("\u00e7\3\2\2\2\u00f4\u00e8\3\2\2\2\u00f4\u00eb\3\2\2\2")
        buf.write("\u00f4\u00ec\3\2\2\2\u00f4\u00ed\3\2\2\2\u00f4\u00ee\3")
        buf.write("\2\2\2\u00f4\u00ef\3\2\2\2\u00f4\u00f0\3\2\2\2\u00f4\u00f1")
        buf.write("\3\2\2\2\u00f5!\3\2\2\2\u00f6\u00f7\5\f\7\2\u00f7\u00f8")
        buf.write("\7\31\2\2\u00f8\u00f9\5<\37\2\u00f9\u00fa\7\7\2\2\u00fa")
        buf.write("#\3\2\2\2\u00fb\u00fc\7>\2\2\u00fc\u00fd\7\f\2\2\u00fd")
        buf.write("\u00fe\5&\24\2\u00fe\u00ff\7\r\2\2\u00ff%\3\2\2\2\u0100")
        buf.write("\u0105\5<\37\2\u0101\u0102\7\t\2\2\u0102\u0104\5<\37\2")
        buf.write("\u0103\u0101\3\2\2\2\u0104\u0107\3\2\2\2\u0105\u0103\3")
        buf.write("\2\2\2\u0105\u0106\3\2\2\2\u0106\u010a\3\2\2\2\u0107\u0105")
        buf.write("\3\2\2\2\u0108\u010a\3\2\2\2\u0109\u0100\3\2\2\2\u0109")
        buf.write("\u0108\3\2\2\2\u010a\'\3\2\2\2\u010b\u010c\7*\2\2\u010c")
        buf.write("\u010d\7\f\2\2\u010d\u010e\5<\37\2\u010e\u010f\7\r\2\2")
        buf.write("\u010f\u0110\7\7\2\2\u0110)\3\2\2\2\u0111\u0112\7+\2\2")
        buf.write("\u0112\u0113\7\f\2\2\u0113\u0114\5\n\6\2\u0114\u0115\7")
        buf.write("\r\2\2\u0115\u0116\7\7\2\2\u0116+\3\2\2\2\u0117\u0118")
        buf.write("\7(\2\2\u0118\u0119\7\f\2\2\u0119\u011a\5.\30\2\u011a")
        buf.write("\u011b\7\r\2\2\u011b\u011c\7\7\2\2\u011c-\3\2\2\2\u011d")
        buf.write("\u011e\5<\37\2\u011e\u011f\5\60\31\2\u011f/\3\2\2\2\u0120")
        buf.write("\u0121\7\t\2\2\u0121\u0122\5<\37\2\u0122\u0123\5\60\31")
        buf.write("\2\u0123\u0126\3\2\2\2\u0124\u0126\3\2\2\2\u0125\u0120")
        buf.write("\3\2\2\2\u0125\u0124\3\2\2\2\u0126\61\3\2\2\2\u0127\u0128")
        buf.write("\7\34\2\2\u0128\u0129\7\f\2\2\u0129\u012a\5<\37\2\u012a")
        buf.write("\u012b\7\r\2\2\u012b\u012d\5\34\17\2\u012c\u012e\5\64")
        buf.write("\33\2\u012d\u012c\3\2\2\2\u012d\u012e\3\2\2\2\u012e\63")
        buf.write("\3\2\2\2\u012f\u0130\7 \2\2\u0130\u0131\5\34\17\2\u0131")
        buf.write("\65\3\2\2\2\u0132\u0133\7\35\2\2\u0133\u0134\7\f\2\2\u0134")
        buf.write("\u0135\5<\37\2\u0135\u0136\7\r\2\2\u0136\u0137\5\34\17")
        buf.write("\2\u0137\67\3\2\2\2\u0138\u0139\7\36\2\2\u0139\u013a\5")
        buf.write(":\36\2\u013a\u013b\7\37\2\2\u013b\u013c\5<\37\2\u013c")
        buf.write("\u013d\5\34\17\2\u013d9\3\2\2\2\u013e\u013f\7>\2\2\u013f")
        buf.write("\u0140\7\31\2\2\u0140\u0141\5<\37\2\u0141;\3\2\2\2\u0142")
        buf.write("\u0143\5@!\2\u0143\u0144\5> \2\u0144=\3\2\2\2\u0145\u0146")
        buf.write("\7\27\2\2\u0146\u0147\5@!\2\u0147\u0148\5> \2\u0148\u014b")
        buf.write("\3\2\2\2\u0149\u014b\3\2\2\2\u014a\u0145\3\2\2\2\u014a")
        buf.write("\u0149\3\2\2\2\u014b?\3\2\2\2\u014c\u014d\5D#\2\u014d")
        buf.write("\u014e\5B\"\2\u014eA\3\2\2\2\u014f\u0150\7\30\2\2\u0150")
        buf.write("\u0151\5D#\2\u0151\u0152\5B\"\2\u0152\u0155\3\2\2\2\u0153")
        buf.write("\u0155\3\2\2\2\u0154\u014f\3\2\2\2\u0154\u0153\3\2\2\2")
        buf.write("\u0155C\3\2\2\2\u0156\u0157\5H%\2\u0157\u0158\5F$\2\u0158")
        buf.write("\u0159\5H%\2\u0159\u015c\3\2\2\2\u015a\u015c\5H%\2\u015b")
        buf.write("\u0156\3\2\2\2\u015b\u015a\3\2\2\2\u015cE\3\2\2\2\u015d")
        buf.write("\u015e\t\3\2\2\u015eG\3\2\2\2\u015f\u0160\5L\'\2\u0160")
        buf.write("\u0161\5J&\2\u0161\u0162\5L\'\2\u0162\u0165\3\2\2\2\u0163")
        buf.write("\u0165\5L\'\2\u0164\u015f\3\2\2\2\u0164\u0163\3\2\2\2")
        buf.write("\u0165I\3\2\2\2\u0166\u0167\t\4\2\2\u0167K\3\2\2\2\u0168")
        buf.write("\u0169\5P)\2\u0169\u016a\5N(\2\u016aM\3\2\2\2\u016b\u016c")
        buf.write("\t\5\2\2\u016c\u016d\5P)\2\u016d\u016e\5N(\2\u016e\u0171")
        buf.write("\3\2\2\2\u016f\u0171\3\2\2\2\u0170\u016b\3\2\2\2\u0170")
        buf.write("\u016f\3\2\2\2\u0171O\3\2\2\2\u0172\u0173\5T+\2\u0173")
        buf.write("\u0174\5R*\2\u0174Q\3\2\2\2\u0175\u0176\t\6\2\2\u0176")
        buf.write("\u0177\5T+\2\u0177\u0178\5R*\2\u0178\u017b\3\2\2\2\u0179")
        buf.write("\u017b\3\2\2\2\u017a\u0175\3\2\2\2\u017a\u0179\3\2\2\2")
        buf.write("\u017bS\3\2\2\2\u017c\u017e\7\22\2\2\u017d\u017c\3\2\2")
        buf.write("\2\u017d\u017e\3\2\2\2\u017e\u017f\3\2\2\2\u017f\u0180")
        buf.write("\7\f\2\2\u0180\u0181\5<\37\2\u0181\u0182\7\r\2\2\u0182")
        buf.write("\u0191\3\2\2\2\u0183\u0185\7\22\2\2\u0184\u0183\3\2\2")
        buf.write("\2\u0184\u0185\3\2\2\2\u0185\u0186\3\2\2\2\u0186\u0191")
        buf.write("\5V,\2\u0187\u0189\7\22\2\2\u0188\u0187\3\2\2\2\u0188")
        buf.write("\u0189\3\2\2\2\u0189\u018a\3\2\2\2\u018a\u0191\5\f\7\2")
        buf.write("\u018b\u018d\7\22\2\2\u018c\u018b\3\2\2\2\u018c\u018d")
        buf.write("\3\2\2\2\u018d\u018e\3\2\2\2\u018e\u0191\5$\23\2\u018f")
        buf.write("\u0191\5X-\2\u0190\u017d\3\2\2\2\u0190\u0184\3\2\2\2\u0190")
        buf.write("\u0188\3\2\2\2\u0190\u018c\3\2\2\2\u0190\u018f\3\2\2\2")
        buf.write("\u0191U\3\2\2\2\u0192\u0193\t\7\2\2\u0193W\3\2\2\2\u0194")
        buf.write("\u01a2\5Z.\2\u0195\u01a2\5\\/\2\u0196\u01a2\5^\60\2\u0197")
        buf.write("\u01a2\5`\61\2\u0198\u01a2\5b\62\2\u0199\u01a2\5d\63\2")
        buf.write("\u019a\u01a2\5f\64\2\u019b\u01a2\5h\65\2\u019c\u01a2\5")
        buf.write("j\66\2\u019d\u01a2\5l\67\2\u019e\u01a2\5n8\2\u019f\u01a2")
        buf.write("\5p9\2\u01a0\u01a2\5r:\2\u01a1\u0194\3\2\2\2\u01a1\u0195")
        buf.write("\3\2\2\2\u01a1\u0196\3\2\2\2\u01a1\u0197\3\2\2\2\u01a1")
        buf.write("\u0198\3\2\2\2\u01a1\u0199\3\2\2\2\u01a1\u019a\3\2\2\2")
        buf.write("\u01a1\u019b\3\2\2\2\u01a1\u019c\3\2\2\2\u01a1\u019d\3")
        buf.write("\2\2\2\u01a1\u019e\3\2\2\2\u01a1\u019f\3\2\2\2\u01a1\u01a0")
        buf.write("\3\2\2\2\u01a2Y\3\2\2\2\u01a3\u01a4\7,\2\2\u01a4\u01a5")
        buf.write("\7\f\2\2\u01a5\u01a6\5\f\7\2\u01a6\u01a9\7\t\2\2\u01a7")
        buf.write("\u01aa\5\f\7\2\u01a8\u01aa\7<\2\2\u01a9\u01a7\3\2\2\2")
        buf.write("\u01a9\u01a8\3\2\2\2\u01aa\u01ab\3\2\2\2\u01ab\u01ac\7")
        buf.write("\t\2\2\u01ac\u01ad\5\f\7\2\u01ad\u01ae\7\t\2\2\u01ae\u01af")
        buf.write("\5\f\7\2\u01af\u01b0\7\r\2\2\u01b0[\3\2\2\2\u01b1\u01b2")
        buf.write("\7-\2\2\u01b2\u01b3\7\f\2\2\u01b3\u01b4\5\f\7\2\u01b4")
        buf.write("\u01b5\7\t\2\2\u01b5\u01b6\5\f\7\2\u01b6\u01b7\7\t\2\2")
        buf.write("\u01b7\u01b8\5\f\7\2\u01b8\u01b9\7\r\2\2\u01b9]\3\2\2")
        buf.write("\2\u01ba\u01bb\7.\2\2\u01bb\u01bc\7\f\2\2\u01bc\u01bd")
        buf.write("\5\f\7\2\u01bd\u01be\7\t\2\2\u01be\u01bf\5\f\7\2\u01bf")
        buf.write("\u01c0\7\r\2\2\u01c0_\3\2\2\2\u01c1\u01c2\7/\2\2\u01c2")
        buf.write("\u01c3\7\f\2\2\u01c3\u01c4\5\f\7\2\u01c4\u01c5\7\t\2\2")
        buf.write("\u01c5\u01c6\5\f\7\2\u01c6\u01c7\7\r\2\2\u01c7a\3\2\2")
        buf.write("\2\u01c8\u01c9\7\60\2\2\u01c9\u01ca\7\f\2\2\u01ca\u01cb")
        buf.write("\5\f\7\2\u01cb\u01cc\7\t\2\2\u01cc\u01cd\5\f\7\2\u01cd")
        buf.write("\u01ce\7\r\2\2\u01cec\3\2\2\2\u01cf\u01d0\7\61\2\2\u01d0")
        buf.write("\u01d1\7\f\2\2\u01d1\u01d2\5\f\7\2\u01d2\u01d3\7\t\2\2")
        buf.write("\u01d3\u01d4\5\f\7\2\u01d4\u01d5\7\r\2\2\u01d5e\3\2\2")
        buf.write("\2\u01d6\u01d7\7\62\2\2\u01d7\u01d8\7\f\2\2\u01d8\u01d9")
        buf.write("\5\f\7\2\u01d9\u01da\7\t\2\2\u01da\u01db\5\f\7\2\u01db")
        buf.write("\u01dc\7\r\2\2\u01dcg\3\2\2\2\u01dd\u01de\7\63\2\2\u01de")
        buf.write("\u01df\7\f\2\2\u01df\u01e0\5\f\7\2\u01e0\u01e1\7\t\2\2")
        buf.write("\u01e1\u01e2\5\f\7\2\u01e2\u01e3\7\r\2\2\u01e3i\3\2\2")
        buf.write("\2\u01e4\u01e5\7\64\2\2\u01e5\u01e6\7\f\2\2\u01e6\u01e7")
        buf.write("\5\f\7\2\u01e7\u01e8\7\t\2\2\u01e8\u01e9\5\f\7\2\u01e9")
        buf.write("\u01ea\7\r\2\2\u01eak\3\2\2\2\u01eb\u01ec\7\65\2\2\u01ec")
        buf.write("\u01ed\7\f\2\2\u01ed\u01ee\5\f\7\2\u01ee\u01ef\7\t\2\2")
        buf.write("\u01ef\u01f0\5\f\7\2\u01f0\u01f1\7\t\2\2\u01f1\u01f2\7")
        buf.write(":\2\2\u01f2\u01f3\7\r\2\2\u01f3m\3\2\2\2\u01f4\u01f5\7")
        buf.write("\66\2\2\u01f5\u01f6\7\f\2\2\u01f6\u01f7\5\f\7\2\u01f7")
        buf.write("\u01f8\7\t\2\2\u01f8\u01f9\5\f\7\2\u01f9\u01fa\7\t\2\2")
        buf.write("\u01fa\u01fb\5\f\7\2\u01fb\u01fc\7\r\2\2\u01fco\3\2\2")
        buf.write("\2\u01fd\u01fe\7\67\2\2\u01fe\u01ff\7\f\2\2\u01ff\u0200")
        buf.write("\5\f\7\2\u0200\u0201\7\t\2\2\u0201\u0202\5\f\7\2\u0202")
        buf.write("\u0203\7\t\2\2\u0203\u0204\7:\2\2\u0204\u0205\7\r\2\2")
        buf.write("\u0205q\3\2\2\2\u0206\u0207\78\2\2\u0207\u0208\7\f\2\2")
        buf.write("\u0208\u0209\5\f\7\2\u0209\u020a\7\t\2\2\u020a\u020b\5")
        buf.write("\f\7\2\u020b\u020c\7\t\2\2\u020c\u020d\5\f\7\2\u020d\u020e")
        buf.write("\7\r\2\2\u020es\3\2\2\2$x}\u0089\u0090\u0097\u009c\u00a3")
        buf.write("\u00a8\u00ab\u00b3\u00bc\u00c1\u00c7\u00d3\u00d9\u00e3")
        buf.write("\u00f4\u0105\u0109\u0125\u012d\u014a\u0154\u015b\u0164")
        buf.write("\u0170\u017a\u017d\u0184\u0188\u018c\u0190\u01a1\u01a9")
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
    RULE_var_block = 1
    RULE_ids_decl = 2
    RULE_ident_decl = 3
    RULE_ids = 4
    RULE_ident = 5
    RULE_ident_ind = 6
    RULE_tipo = 7
    RULE_tipo_atom = 8
    RULE_func = 9
    RULE_return_type = 10
    RULE_params = 11
    RULE_param = 12
    RULE_block = 13
    RULE_main = 14
    RULE_statement = 15
    RULE_assignment = 16
    RULE_call = 17
    RULE_args = 18
    RULE_regresa = 19
    RULE_read = 20
    RULE_write = 21
    RULE_impr = 22
    RULE_imprs = 23
    RULE_decision = 24
    RULE_else_block = 25
    RULE_while_loop = 26
    RULE_for_loop = 27
    RULE_for_asgn = 28
    RULE_expr = 29
    RULE_exprs = 30
    RULE_and_term = 31
    RULE_and_terms = 32
    RULE_comp_term = 33
    RULE_comp_op = 34
    RULE_rel_term = 35
    RULE_rel_op = 36
    RULE_artm_term = 37
    RULE_artm_terms = 38
    RULE_fact_term = 39
    RULE_fact_terms = 40
    RULE_operand = 41
    RULE_cte = 42
    RULE_covid = 43
    RULE_load_file = 44
    RULE_load_data = 45
    RULE_avg = 46
    RULE_moda = 47
    RULE_rango = 48
    RULE_variance = 49
    RULE_std_dev = 50
    RULE_maxi = 51
    RULE_mini = 52
    RULE_moment = 53
    RULE_plot = 54
    RULE_histogram = 55
    RULE_correl = 56

    ruleNames =  [ "start", "var_block", "ids_decl", "ident_decl", "ids", 
                   "ident", "ident_ind", "tipo", "tipo_atom", "func", "return_type", 
                   "params", "param", "block", "main", "statement", "assignment", 
                   "call", "args", "regresa", "read", "write", "impr", "imprs", 
                   "decision", "else_block", "while_loop", "for_loop", "for_asgn", 
                   "expr", "exprs", "and_term", "and_terms", "comp_term", 
                   "comp_op", "rel_term", "rel_op", "artm_term", "artm_terms", 
                   "fact_term", "fact_terms", "operand", "cte", "covid", 
                   "load_file", "load_data", "avg", "moda", "rango", "variance", 
                   "std_dev", "maxi", "mini", "moment", "plot", "histogram", 
                   "correl" ]

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


        def var_block(self):
            return self.getTypedRuleContext(CovidParser.Var_blockContext,0)


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
                self.var_block()


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


    class Var_blockContext(ParserRuleContext):

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
            return CovidParser.RULE_var_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_block" ):
                listener.enterVar_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_block" ):
                listener.exitVar_block(self)




    def var_block(self):

        localctx = CovidParser.Var_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_var_block)
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
        self.enterRule(localctx, 4, self.RULE_ids_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.ident_decl()
            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CovidParser.COMMA:
                self.state = 138
                self.match(CovidParser.COMMA)
                self.state = 139
                self.ident_decl()
                self.state = 144
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
        self.enterRule(localctx, 6, self.RULE_ident_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.match(CovidParser.ID)
            self.state = 149
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 146
                self.match(CovidParser.SQUARE_L)
                self.state = 147
                self.match(CovidParser.INT_CTE)
                self.state = 148
                self.match(CovidParser.SQUARE_R)


            self.state = 154
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CovidParser.SQUARE_L:
                self.state = 151
                self.match(CovidParser.SQUARE_L)
                self.state = 152
                self.match(CovidParser.INT_CTE)
                self.state = 153
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
        self.enterRule(localctx, 8, self.RULE_ids)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self.ident()
            self.state = 161
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CovidParser.COMMA:
                self.state = 157
                self.match(CovidParser.COMMA)
                self.state = 158
                self.ident()
                self.state = 163
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
        self.enterRule(localctx, 10, self.RULE_ident)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.match(CovidParser.ID)
            self.state = 166
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 165
                self.ident_ind()


            self.state = 169
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CovidParser.SQUARE_L:
                self.state = 168
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
        self.enterRule(localctx, 12, self.RULE_ident_ind)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.match(CovidParser.SQUARE_L)
            self.state = 172
            self.expr()
            self.state = 173
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
        self.enterRule(localctx, 14, self.RULE_tipo)
        try:
            self.state = 177
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CovidParser.INT, CovidParser.FLOAT, CovidParser.CHAR, CovidParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 175
                self.tipo_atom()
                pass
            elif token in [CovidParser.DATAFRAME]:
                self.enterOuterAlt(localctx, 2)
                self.state = 176
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
        self.enterRule(localctx, 16, self.RULE_tipo_atom)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
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
        self.enterRule(localctx, 18, self.RULE_func)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.match(CovidParser.FUNC)
            self.state = 182
            self.return_type()
            self.state = 183
            self.match(CovidParser.ID)
            self.state = 184
            self.match(CovidParser.PARENS_L)
            self.state = 186
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CovidParser.INT) | (1 << CovidParser.FLOAT) | (1 << CovidParser.CHAR) | (1 << CovidParser.STRING))) != 0):
                self.state = 185
                self.params()


            self.state = 188
            self.match(CovidParser.PARENS_R)
            self.state = 189
            self.match(CovidParser.SEMI)
            self.state = 191
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CovidParser.VAR:
                self.state = 190
                self.var_block()


            self.state = 193
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
        self.enterRule(localctx, 20, self.RULE_return_type)
        try:
            self.state = 197
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CovidParser.INT, CovidParser.FLOAT, CovidParser.CHAR, CovidParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 195
                self.tipo_atom()
                pass
            elif token in [CovidParser.VOID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 196
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
        self.enterRule(localctx, 22, self.RULE_params)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.tipo_atom()
            self.state = 200
            self.match(CovidParser.ID)
            self.state = 201
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
        self.enterRule(localctx, 24, self.RULE_param)
        try:
            self.state = 209
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CovidParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 203
                self.match(CovidParser.COMMA)
                self.state = 204
                self.tipo_atom()
                self.state = 205
                self.match(CovidParser.ID)
                self.state = 206
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
        self.enterRule(localctx, 26, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            self.match(CovidParser.CURLY_L)
            self.state = 215
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CovidParser.IF) | (1 << CovidParser.WHILE) | (1 << CovidParser.FOR) | (1 << CovidParser.PRINT) | (1 << CovidParser.RETURN) | (1 << CovidParser.INPUT) | (1 << CovidParser.LOAD_FILE) | (1 << CovidParser.LOAD_DATA) | (1 << CovidParser.AVG) | (1 << CovidParser.MODE) | (1 << CovidParser.RANGE) | (1 << CovidParser.VARIANCE) | (1 << CovidParser.STD_DEV) | (1 << CovidParser.MAX) | (1 << CovidParser.MIN) | (1 << CovidParser.MOMENT) | (1 << CovidParser.PLOT) | (1 << CovidParser.HISTOGRAM) | (1 << CovidParser.CORREL) | (1 << CovidParser.ID))) != 0):
                self.state = 212
                self.statement()
                self.state = 217
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 218
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
        self.enterRule(localctx, 28, self.RULE_main)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            self.match(CovidParser.MAIN)
            self.state = 221
            self.match(CovidParser.PARENS_L)
            self.state = 222
            self.match(CovidParser.PARENS_R)
            self.state = 223
            self.match(CovidParser.SEMI)
            self.state = 225
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CovidParser.VAR:
                self.state = 224
                self.var_block()


            self.state = 227
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
        self.enterRule(localctx, 30, self.RULE_statement)
        try:
            self.state = 242
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 229
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 230
                self.call()
                self.state = 231
                self.match(CovidParser.SEMI)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 233
                self.regresa()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 234
                self.read()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 235
                self.write()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 236
                self.decision()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 237
                self.while_loop()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 238
                self.for_loop()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 239
                self.covid()
                self.state = 240
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
        self.enterRule(localctx, 32, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self.ident()
            self.state = 245
            self.match(CovidParser.ASGN)
            self.state = 246
            self.expr()
            self.state = 247
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
        self.enterRule(localctx, 34, self.RULE_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 249
            self.match(CovidParser.ID)
            self.state = 250
            self.match(CovidParser.PARENS_L)
            self.state = 251
            self.args()
            self.state = 252
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
        self.enterRule(localctx, 36, self.RULE_args)
        self._la = 0 # Token type
        try:
            self.state = 263
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CovidParser.PARENS_L, CovidParser.NOT, CovidParser.LOAD_FILE, CovidParser.LOAD_DATA, CovidParser.AVG, CovidParser.MODE, CovidParser.RANGE, CovidParser.VARIANCE, CovidParser.STD_DEV, CovidParser.MAX, CovidParser.MIN, CovidParser.MOMENT, CovidParser.PLOT, CovidParser.HISTOGRAM, CovidParser.CORREL, CovidParser.INT_CTE, CovidParser.FLOAT_CTE, CovidParser.STRING_CTE, CovidParser.CHAR_CTE, CovidParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 254
                self.expr()
                self.state = 259
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==CovidParser.COMMA:
                    self.state = 255
                    self.match(CovidParser.COMMA)
                    self.state = 256
                    self.expr()
                    self.state = 261
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
        self.enterRule(localctx, 38, self.RULE_regresa)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self.match(CovidParser.RETURN)
            self.state = 266
            self.match(CovidParser.PARENS_L)
            self.state = 267
            self.expr()
            self.state = 268
            self.match(CovidParser.PARENS_R)
            self.state = 269
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
        self.enterRule(localctx, 40, self.RULE_read)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 271
            self.match(CovidParser.INPUT)
            self.state = 272
            self.match(CovidParser.PARENS_L)
            self.state = 273
            self.ids()
            self.state = 274
            self.match(CovidParser.PARENS_R)
            self.state = 275
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
        self.enterRule(localctx, 42, self.RULE_write)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
            self.match(CovidParser.PRINT)
            self.state = 278
            self.match(CovidParser.PARENS_L)
            self.state = 279
            self.impr()
            self.state = 280
            self.match(CovidParser.PARENS_R)
            self.state = 281
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
        self.enterRule(localctx, 44, self.RULE_impr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 283
            self.expr()
            self.state = 284
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
        self.enterRule(localctx, 46, self.RULE_imprs)
        try:
            self.state = 291
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CovidParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 286
                self.match(CovidParser.COMMA)
                self.state = 287
                self.expr()
                self.state = 288
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
        self.enterRule(localctx, 48, self.RULE_decision)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 293
            self.match(CovidParser.IF)
            self.state = 294
            self.match(CovidParser.PARENS_L)
            self.state = 295
            self.expr()
            self.state = 296
            self.match(CovidParser.PARENS_R)
            self.state = 297
            self.block()
            self.state = 299
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CovidParser.ELSE:
                self.state = 298
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
        self.enterRule(localctx, 50, self.RULE_else_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 301
            self.match(CovidParser.ELSE)
            self.state = 302
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
        self.enterRule(localctx, 52, self.RULE_while_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 304
            self.match(CovidParser.WHILE)
            self.state = 305
            self.match(CovidParser.PARENS_L)
            self.state = 306
            self.expr()
            self.state = 307
            self.match(CovidParser.PARENS_R)
            self.state = 308
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
        self.enterRule(localctx, 54, self.RULE_for_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 310
            self.match(CovidParser.FOR)
            self.state = 311
            self.for_asgn()
            self.state = 312
            self.match(CovidParser.TO)
            self.state = 313
            self.expr()
            self.state = 314
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
        self.enterRule(localctx, 56, self.RULE_for_asgn)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 316
            self.match(CovidParser.ID)
            self.state = 317
            self.match(CovidParser.ASGN)
            self.state = 318
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
        self.enterRule(localctx, 58, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 320
            self.and_term()
            self.state = 321
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
        self.enterRule(localctx, 60, self.RULE_exprs)
        try:
            self.state = 328
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CovidParser.OR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 323
                self.match(CovidParser.OR)
                self.state = 324
                self.and_term()
                self.state = 325
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
        self.enterRule(localctx, 62, self.RULE_and_term)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 330
            self.comp_term()
            self.state = 331
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
        self.enterRule(localctx, 64, self.RULE_and_terms)
        try:
            self.state = 338
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CovidParser.AND]:
                self.enterOuterAlt(localctx, 1)
                self.state = 333
                self.match(CovidParser.AND)
                self.state = 334
                self.comp_term()
                self.state = 335
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
        self.enterRule(localctx, 66, self.RULE_comp_term)
        try:
            self.state = 345
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 340
                self.rel_term()
                self.state = 341
                self.comp_op()
                self.state = 342
                self.rel_term()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 344
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
        self.enterRule(localctx, 68, self.RULE_comp_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 347
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
        self.enterRule(localctx, 70, self.RULE_rel_term)
        try:
            self.state = 354
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 349
                self.artm_term()
                self.state = 350
                self.rel_op()
                self.state = 351
                self.artm_term()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 353
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
        self.enterRule(localctx, 72, self.RULE_rel_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 356
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
        self.enterRule(localctx, 74, self.RULE_artm_term)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 358
            self.fact_term()
            self.state = 359
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
        self.enterRule(localctx, 76, self.RULE_artm_terms)
        self._la = 0 # Token type
        try:
            self.state = 366
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CovidParser.PLUS, CovidParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 361
                _la = self._input.LA(1)
                if not(_la==CovidParser.PLUS or _la==CovidParser.MINUS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 362
                self.fact_term()
                self.state = 363
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
        self.enterRule(localctx, 78, self.RULE_fact_term)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 368
            self.operand()
            self.state = 369
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
        self.enterRule(localctx, 80, self.RULE_fact_terms)
        self._la = 0 # Token type
        try:
            self.state = 376
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CovidParser.MULT, CovidParser.DIVIDE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 371
                _la = self._input.LA(1)
                if not(_la==CovidParser.MULT or _la==CovidParser.DIVIDE):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 372
                self.operand()
                self.state = 373
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
        self.enterRule(localctx, 82, self.RULE_operand)
        self._la = 0 # Token type
        try:
            self.state = 398
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 379
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CovidParser.NOT:
                    self.state = 378
                    self.match(CovidParser.NOT)


                self.state = 381
                self.match(CovidParser.PARENS_L)
                self.state = 382
                self.expr()
                self.state = 383
                self.match(CovidParser.PARENS_R)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 386
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CovidParser.NOT:
                    self.state = 385
                    self.match(CovidParser.NOT)


                self.state = 388
                self.cte()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 390
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CovidParser.NOT:
                    self.state = 389
                    self.match(CovidParser.NOT)


                self.state = 392
                self.ident()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 394
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CovidParser.NOT:
                    self.state = 393
                    self.match(CovidParser.NOT)


                self.state = 396
                self.call()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 397
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
        self.enterRule(localctx, 84, self.RULE_cte)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 400
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


        def moment(self):
            return self.getTypedRuleContext(CovidParser.MomentContext,0)


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
        self.enterRule(localctx, 86, self.RULE_covid)
        try:
            self.state = 415
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CovidParser.LOAD_FILE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 402
                self.load_file()
                pass
            elif token in [CovidParser.LOAD_DATA]:
                self.enterOuterAlt(localctx, 2)
                self.state = 403
                self.load_data()
                pass
            elif token in [CovidParser.AVG]:
                self.enterOuterAlt(localctx, 3)
                self.state = 404
                self.avg()
                pass
            elif token in [CovidParser.MODE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 405
                self.moda()
                pass
            elif token in [CovidParser.RANGE]:
                self.enterOuterAlt(localctx, 5)
                self.state = 406
                self.rango()
                pass
            elif token in [CovidParser.VARIANCE]:
                self.enterOuterAlt(localctx, 6)
                self.state = 407
                self.variance()
                pass
            elif token in [CovidParser.STD_DEV]:
                self.enterOuterAlt(localctx, 7)
                self.state = 408
                self.std_dev()
                pass
            elif token in [CovidParser.MAX]:
                self.enterOuterAlt(localctx, 8)
                self.state = 409
                self.maxi()
                pass
            elif token in [CovidParser.MIN]:
                self.enterOuterAlt(localctx, 9)
                self.state = 410
                self.mini()
                pass
            elif token in [CovidParser.MOMENT]:
                self.enterOuterAlt(localctx, 10)
                self.state = 411
                self.moment()
                pass
            elif token in [CovidParser.PLOT]:
                self.enterOuterAlt(localctx, 11)
                self.state = 412
                self.plot()
                pass
            elif token in [CovidParser.HISTOGRAM]:
                self.enterOuterAlt(localctx, 12)
                self.state = 413
                self.histogram()
                pass
            elif token in [CovidParser.CORREL]:
                self.enterOuterAlt(localctx, 13)
                self.state = 414
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

        def STRING_CTE(self):
            return self.getToken(CovidParser.STRING_CTE, 0)

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
        self.enterRule(localctx, 88, self.RULE_load_file)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 417
            self.match(CovidParser.LOAD_FILE)
            self.state = 418
            self.match(CovidParser.PARENS_L)
            self.state = 419
            self.ident()
            self.state = 420
            self.match(CovidParser.COMMA)
            self.state = 423
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CovidParser.ID]:
                self.state = 421
                self.ident()
                pass
            elif token in [CovidParser.STRING_CTE]:
                self.state = 422
                self.match(CovidParser.STRING_CTE)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 425
            self.match(CovidParser.COMMA)
            self.state = 426
            self.ident()
            self.state = 427
            self.match(CovidParser.COMMA)
            self.state = 428
            self.ident()
            self.state = 429
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
        self.enterRule(localctx, 90, self.RULE_load_data)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 431
            self.match(CovidParser.LOAD_DATA)
            self.state = 432
            self.match(CovidParser.PARENS_L)
            self.state = 433
            self.ident()
            self.state = 434
            self.match(CovidParser.COMMA)
            self.state = 435
            self.ident()
            self.state = 436
            self.match(CovidParser.COMMA)
            self.state = 437
            self.ident()
            self.state = 438
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

        def ident(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CovidParser.IdentContext)
            else:
                return self.getTypedRuleContext(CovidParser.IdentContext,i)


        def COMMA(self):
            return self.getToken(CovidParser.COMMA, 0)

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
        self.enterRule(localctx, 92, self.RULE_avg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 440
            self.match(CovidParser.AVG)
            self.state = 441
            self.match(CovidParser.PARENS_L)
            self.state = 442
            self.ident()
            self.state = 443
            self.match(CovidParser.COMMA)
            self.state = 444
            self.ident()
            self.state = 445
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

        def ident(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CovidParser.IdentContext)
            else:
                return self.getTypedRuleContext(CovidParser.IdentContext,i)


        def COMMA(self):
            return self.getToken(CovidParser.COMMA, 0)

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
        self.enterRule(localctx, 94, self.RULE_moda)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 447
            self.match(CovidParser.MODE)
            self.state = 448
            self.match(CovidParser.PARENS_L)
            self.state = 449
            self.ident()
            self.state = 450
            self.match(CovidParser.COMMA)
            self.state = 451
            self.ident()
            self.state = 452
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

        def ident(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CovidParser.IdentContext)
            else:
                return self.getTypedRuleContext(CovidParser.IdentContext,i)


        def COMMA(self):
            return self.getToken(CovidParser.COMMA, 0)

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
        self.enterRule(localctx, 96, self.RULE_rango)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 454
            self.match(CovidParser.RANGE)
            self.state = 455
            self.match(CovidParser.PARENS_L)
            self.state = 456
            self.ident()
            self.state = 457
            self.match(CovidParser.COMMA)
            self.state = 458
            self.ident()
            self.state = 459
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

        def ident(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CovidParser.IdentContext)
            else:
                return self.getTypedRuleContext(CovidParser.IdentContext,i)


        def COMMA(self):
            return self.getToken(CovidParser.COMMA, 0)

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
        self.enterRule(localctx, 98, self.RULE_variance)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 461
            self.match(CovidParser.VARIANCE)
            self.state = 462
            self.match(CovidParser.PARENS_L)
            self.state = 463
            self.ident()
            self.state = 464
            self.match(CovidParser.COMMA)
            self.state = 465
            self.ident()
            self.state = 466
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

        def ident(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CovidParser.IdentContext)
            else:
                return self.getTypedRuleContext(CovidParser.IdentContext,i)


        def COMMA(self):
            return self.getToken(CovidParser.COMMA, 0)

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
        self.enterRule(localctx, 100, self.RULE_std_dev)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 468
            self.match(CovidParser.STD_DEV)
            self.state = 469
            self.match(CovidParser.PARENS_L)
            self.state = 470
            self.ident()
            self.state = 471
            self.match(CovidParser.COMMA)
            self.state = 472
            self.ident()
            self.state = 473
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

        def ident(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CovidParser.IdentContext)
            else:
                return self.getTypedRuleContext(CovidParser.IdentContext,i)


        def COMMA(self):
            return self.getToken(CovidParser.COMMA, 0)

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
        self.enterRule(localctx, 102, self.RULE_maxi)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 475
            self.match(CovidParser.MAX)
            self.state = 476
            self.match(CovidParser.PARENS_L)
            self.state = 477
            self.ident()
            self.state = 478
            self.match(CovidParser.COMMA)
            self.state = 479
            self.ident()
            self.state = 480
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

        def ident(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CovidParser.IdentContext)
            else:
                return self.getTypedRuleContext(CovidParser.IdentContext,i)


        def COMMA(self):
            return self.getToken(CovidParser.COMMA, 0)

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
        self.enterRule(localctx, 104, self.RULE_mini)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 482
            self.match(CovidParser.MIN)
            self.state = 483
            self.match(CovidParser.PARENS_L)
            self.state = 484
            self.ident()
            self.state = 485
            self.match(CovidParser.COMMA)
            self.state = 486
            self.ident()
            self.state = 487
            self.match(CovidParser.PARENS_R)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MomentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MOMENT(self):
            return self.getToken(CovidParser.MOMENT, 0)

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

        def INT_CTE(self):
            return self.getToken(CovidParser.INT_CTE, 0)

        def PARENS_R(self):
            return self.getToken(CovidParser.PARENS_R, 0)

        def getRuleIndex(self):
            return CovidParser.RULE_moment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMoment" ):
                listener.enterMoment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMoment" ):
                listener.exitMoment(self)




    def moment(self):

        localctx = CovidParser.MomentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_moment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 489
            self.match(CovidParser.MOMENT)
            self.state = 490
            self.match(CovidParser.PARENS_L)
            self.state = 491
            self.ident()
            self.state = 492
            self.match(CovidParser.COMMA)
            self.state = 493
            self.ident()
            self.state = 494
            self.match(CovidParser.COMMA)
            self.state = 495
            self.match(CovidParser.INT_CTE)
            self.state = 496
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
            self.state = 498
            self.match(CovidParser.PLOT)
            self.state = 499
            self.match(CovidParser.PARENS_L)
            self.state = 500
            self.ident()
            self.state = 501
            self.match(CovidParser.COMMA)
            self.state = 502
            self.ident()
            self.state = 503
            self.match(CovidParser.COMMA)
            self.state = 504
            self.ident()
            self.state = 505
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

        def INT_CTE(self):
            return self.getToken(CovidParser.INT_CTE, 0)

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
            self.state = 507
            self.match(CovidParser.HISTOGRAM)
            self.state = 508
            self.match(CovidParser.PARENS_L)
            self.state = 509
            self.ident()
            self.state = 510
            self.match(CovidParser.COMMA)
            self.state = 511
            self.ident()
            self.state = 512
            self.match(CovidParser.COMMA)
            self.state = 513
            self.match(CovidParser.INT_CTE)
            self.state = 514
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
            self.state = 516
            self.match(CovidParser.CORREL)
            self.state = 517
            self.match(CovidParser.PARENS_L)
            self.state = 518
            self.ident()
            self.state = 519
            self.match(CovidParser.COMMA)
            self.state = 520
            self.ident()
            self.state = 521
            self.match(CovidParser.COMMA)
            self.state = 522
            self.ident()
            self.state = 523
            self.match(CovidParser.PARENS_R)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





