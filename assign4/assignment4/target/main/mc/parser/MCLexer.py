# Generated from main/mc/parser/MC.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2.")
        buf.write("\u018e\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\3\3\3\3\3\3\3\5\3{\n\3\3\4\6\4~\n\4\r\4\16")
        buf.write("\4\177\3\5\3\5\5\5\u0084\n\5\3\5\6\5\u0087\n\5\r\5\16")
        buf.write("\5\u0088\3\5\3\5\5\5\u008d\n\5\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\5\6\u0098\n\6\3\7\3\7\3\7\3\7\7\7\u009e\n")
        buf.write("\7\f\7\16\7\u00a1\13\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b")
        buf.write("\3\b\7\b\u00ac\n\b\f\b\16\b\u00af\13\b\3\b\3\b\3\t\3\t")
        buf.write("\3\n\3\n\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3\r\3\16\3\16\3")
        buf.write("\17\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23")
        buf.write("\3\24\3\24\3\24\3\25\3\25\3\25\3\26\3\26\3\27\3\27\3\27")
        buf.write("\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3 ")
        buf.write("\3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3")
        buf.write("(\3)\6)\u0115\n)\r)\16)\u0116\3)\3)\7)\u011b\n)\f)\16")
        buf.write(")\u011e\13)\3)\7)\u0121\n)\f)\16)\u0124\13)\3)\3)\6)\u0128")
        buf.write("\n)\r)\16)\u0129\5)\u012c\n)\3*\3*\5*\u0130\n*\3*\6*\u0133")
        buf.write("\n*\r*\16*\u0134\3+\3+\3,\3,\5,\u013b\n,\3-\3-\3-\3.\3")
        buf.write(".\3.\5.\u0143\n.\3/\3/\3/\3/\3/\3/\3/\3/\3\60\3\60\3\60")
        buf.write("\3\60\3\60\3\60\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\62")
        buf.write("\3\62\3\62\3\62\3\63\3\63\7\63\u0160\n\63\f\63\16\63\u0163")
        buf.write("\13\63\3\64\6\64\u0166\n\64\r\64\16\64\u0167\3\64\3\64")
        buf.write("\3\65\3\65\7\65\u016e\n\65\f\65\16\65\u0171\13\65\3\65")
        buf.write("\3\65\3\65\3\66\3\66\7\66\u0178\n\66\f\66\16\66\u017b")
        buf.write("\13\66\3\66\5\66\u017e\n\66\3\66\3\66\3\67\3\67\7\67\u0184")
        buf.write("\n\67\f\67\16\67\u0187\13\67\3\67\3\67\3\67\38\38\38\3")
        buf.write("\u009f\29\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25")
        buf.write("\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+")
        buf.write("\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E")
        buf.write("$G%I&K\'M(O\2Q\2S\2U\2W\2Y\2[\2]\2_\2a\2c\2e)g*i+k,m-")
        buf.write("o.\3\2\r\4\2\f\f\17\17\3\2\62;\4\2GGgg\3\2//\7\2\n\f\16")
        buf.write("\17$$))^^\n\2$$))^^ddhhppttvv\3\2^^\5\2C\\aac|\6\2\62")
        buf.write(";C\\aac|\5\2\13\f\17\17\"\"\5\3\n\f\16\17^^\2\u019a\2")
        buf.write("\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3")
        buf.write("\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2")
        buf.write("\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2")
        buf.write("\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%")
        buf.write("\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2")
        buf.write("\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\3q\3\2\2\2\5z\3\2")
        buf.write("\2\2\7}\3\2\2\2\t\u008c\3\2\2\2\13\u0097\3\2\2\2\r\u0099")
        buf.write("\3\2\2\2\17\u00a7\3\2\2\2\21\u00b2\3\2\2\2\23\u00b4\3")
        buf.write("\2\2\2\25\u00b6\3\2\2\2\27\u00b8\3\2\2\2\31\u00bb\3\2")
        buf.write("\2\2\33\u00be\3\2\2\2\35\u00c0\3\2\2\2\37\u00c3\3\2\2")
        buf.write("\2!\u00c5\3\2\2\2#\u00c7\3\2\2\2%\u00c9\3\2\2\2\'\u00cb")
        buf.write("\3\2\2\2)\u00ce\3\2\2\2+\u00d1\3\2\2\2-\u00d3\3\2\2\2")
        buf.write("/\u00d6\3\2\2\2\61\u00d9\3\2\2\2\63\u00de\3\2\2\2\65\u00e1")
        buf.write("\3\2\2\2\67\u00e7\3\2\2\29\u00eb\3\2\2\2;\u00f1\3\2\2")
        buf.write("\2=\u00fa\3\2\2\2?\u0101\3\2\2\2A\u0103\3\2\2\2C\u0105")
        buf.write("\3\2\2\2E\u0107\3\2\2\2G\u0109\3\2\2\2I\u010b\3\2\2\2")
        buf.write("K\u010d\3\2\2\2M\u010f\3\2\2\2O\u0111\3\2\2\2Q\u012b\3")
        buf.write("\2\2\2S\u012d\3\2\2\2U\u0136\3\2\2\2W\u013a\3\2\2\2Y\u013c")
        buf.write("\3\2\2\2[\u0142\3\2\2\2]\u0144\3\2\2\2_\u014c\3\2\2\2")
        buf.write("a\u0152\3\2\2\2c\u0159\3\2\2\2e\u015d\3\2\2\2g\u0165\3")
        buf.write("\2\2\2i\u016b\3\2\2\2k\u0175\3\2\2\2m\u0181\3\2\2\2o\u018b")
        buf.write("\3\2\2\2qr\7x\2\2rs\7q\2\2st\7k\2\2tu\7f\2\2u\4\3\2\2")
        buf.write("\2v{\5c\62\2w{\5]/\2x{\5_\60\2y{\5a\61\2zv\3\2\2\2zw\3")
        buf.write("\2\2\2zx\3\2\2\2zy\3\2\2\2{\6\3\2\2\2|~\5O(\2}|\3\2\2")
        buf.write("\2~\177\3\2\2\2\177}\3\2\2\2\177\u0080\3\2\2\2\u0080\b")
        buf.write("\3\2\2\2\u0081\u0083\5Q)\2\u0082\u0084\5S*\2\u0083\u0082")
        buf.write("\3\2\2\2\u0083\u0084\3\2\2\2\u0084\u008d\3\2\2\2\u0085")
        buf.write("\u0087\5O(\2\u0086\u0085\3\2\2\2\u0087\u0088\3\2\2\2\u0088")
        buf.write("\u0086\3\2\2\2\u0088\u0089\3\2\2\2\u0089\u008a\3\2\2\2")
        buf.write("\u008a\u008b\5S*\2\u008b\u008d\3\2\2\2\u008c\u0081\3\2")
        buf.write("\2\2\u008c\u0086\3\2\2\2\u008d\n\3\2\2\2\u008e\u008f\7")
        buf.write("v\2\2\u008f\u0090\7t\2\2\u0090\u0091\7w\2\2\u0091\u0098")
        buf.write("\7g\2\2\u0092\u0093\7h\2\2\u0093\u0094\7c\2\2\u0094\u0095")
        buf.write("\7n\2\2\u0095\u0096\7u\2\2\u0096\u0098\7g\2\2\u0097\u008e")
        buf.write("\3\2\2\2\u0097\u0092\3\2\2\2\u0098\f\3\2\2\2\u0099\u009a")
        buf.write("\7\61\2\2\u009a\u009b\7,\2\2\u009b\u009f\3\2\2\2\u009c")
        buf.write("\u009e\13\2\2\2\u009d\u009c\3\2\2\2\u009e\u00a1\3\2\2")
        buf.write("\2\u009f\u00a0\3\2\2\2\u009f\u009d\3\2\2\2\u00a0\u00a2")
        buf.write("\3\2\2\2\u00a1\u009f\3\2\2\2\u00a2\u00a3\7,\2\2\u00a3")
        buf.write("\u00a4\7\61\2\2\u00a4\u00a5\3\2\2\2\u00a5\u00a6\b\7\2")
        buf.write("\2\u00a6\16\3\2\2\2\u00a7\u00a8\7\61\2\2\u00a8\u00a9\7")
        buf.write("\61\2\2\u00a9\u00ad\3\2\2\2\u00aa\u00ac\n\2\2\2\u00ab")
        buf.write("\u00aa\3\2\2\2\u00ac\u00af\3\2\2\2\u00ad\u00ab\3\2\2\2")
        buf.write("\u00ad\u00ae\3\2\2\2\u00ae\u00b0\3\2\2\2\u00af\u00ad\3")
        buf.write("\2\2\2\u00b0\u00b1\b\b\2\2\u00b1\20\3\2\2\2\u00b2\u00b3")
        buf.write("\7-\2\2\u00b3\22\3\2\2\2\u00b4\u00b5\7,\2\2\u00b5\24\3")
        buf.write("\2\2\2\u00b6\u00b7\7#\2\2\u00b7\26\3\2\2\2\u00b8\u00b9")
        buf.write("\7~\2\2\u00b9\u00ba\7~\2\2\u00ba\30\3\2\2\2\u00bb\u00bc")
        buf.write("\7#\2\2\u00bc\u00bd\7?\2\2\u00bd\32\3\2\2\2\u00be\u00bf")
        buf.write("\7>\2\2\u00bf\34\3\2\2\2\u00c0\u00c1\7>\2\2\u00c1\u00c2")
        buf.write("\7?\2\2\u00c2\36\3\2\2\2\u00c3\u00c4\7?\2\2\u00c4 \3\2")
        buf.write("\2\2\u00c5\u00c6\7/\2\2\u00c6\"\3\2\2\2\u00c7\u00c8\7")
        buf.write("\61\2\2\u00c8$\3\2\2\2\u00c9\u00ca\7\'\2\2\u00ca&\3\2")
        buf.write("\2\2\u00cb\u00cc\7(\2\2\u00cc\u00cd\7(\2\2\u00cd(\3\2")
        buf.write("\2\2\u00ce\u00cf\7?\2\2\u00cf\u00d0\7?\2\2\u00d0*\3\2")
        buf.write("\2\2\u00d1\u00d2\7@\2\2\u00d2,\3\2\2\2\u00d3\u00d4\7@")
        buf.write("\2\2\u00d4\u00d5\7?\2\2\u00d5.\3\2\2\2\u00d6\u00d7\7k")
        buf.write("\2\2\u00d7\u00d8\7h\2\2\u00d8\60\3\2\2\2\u00d9\u00da\7")
        buf.write("g\2\2\u00da\u00db\7n\2\2\u00db\u00dc\7u\2\2\u00dc\u00dd")
        buf.write("\7g\2\2\u00dd\62\3\2\2\2\u00de\u00df\7f\2\2\u00df\u00e0")
        buf.write("\7q\2\2\u00e0\64\3\2\2\2\u00e1\u00e2\7y\2\2\u00e2\u00e3")
        buf.write("\7j\2\2\u00e3\u00e4\7k\2\2\u00e4\u00e5\7n\2\2\u00e5\u00e6")
        buf.write("\7g\2\2\u00e6\66\3\2\2\2\u00e7\u00e8\7h\2\2\u00e8\u00e9")
        buf.write("\7q\2\2\u00e9\u00ea\7t\2\2\u00ea8\3\2\2\2\u00eb\u00ec")
        buf.write("\7d\2\2\u00ec\u00ed\7t\2\2\u00ed\u00ee\7g\2\2\u00ee\u00ef")
        buf.write("\7c\2\2\u00ef\u00f0\7m\2\2\u00f0:\3\2\2\2\u00f1\u00f2")
        buf.write("\7e\2\2\u00f2\u00f3\7q\2\2\u00f3\u00f4\7p\2\2\u00f4\u00f5")
        buf.write("\7v\2\2\u00f5\u00f6\7k\2\2\u00f6\u00f7\7p\2\2\u00f7\u00f8")
        buf.write("\7w\2\2\u00f8\u00f9\7g\2\2\u00f9<\3\2\2\2\u00fa\u00fb")
        buf.write("\7t\2\2\u00fb\u00fc\7g\2\2\u00fc\u00fd\7v\2\2\u00fd\u00fe")
        buf.write("\7w\2\2\u00fe\u00ff\7t\2\2\u00ff\u0100\7p\2\2\u0100>\3")
        buf.write("\2\2\2\u0101\u0102\7*\2\2\u0102@\3\2\2\2\u0103\u0104\7")
        buf.write("+\2\2\u0104B\3\2\2\2\u0105\u0106\7}\2\2\u0106D\3\2\2\2")
        buf.write("\u0107\u0108\7\177\2\2\u0108F\3\2\2\2\u0109\u010a\7]\2")
        buf.write("\2\u010aH\3\2\2\2\u010b\u010c\7_\2\2\u010cJ\3\2\2\2\u010d")
        buf.write("\u010e\7=\2\2\u010eL\3\2\2\2\u010f\u0110\7.\2\2\u0110")
        buf.write("N\3\2\2\2\u0111\u0112\t\3\2\2\u0112P\3\2\2\2\u0113\u0115")
        buf.write("\5O(\2\u0114\u0113\3\2\2\2\u0115\u0116\3\2\2\2\u0116\u0114")
        buf.write("\3\2\2\2\u0116\u0117\3\2\2\2\u0117\u0118\3\2\2\2\u0118")
        buf.write("\u011c\7\60\2\2\u0119\u011b\5O(\2\u011a\u0119\3\2\2\2")
        buf.write("\u011b\u011e\3\2\2\2\u011c\u011a\3\2\2\2\u011c\u011d\3")
        buf.write("\2\2\2\u011d\u012c\3\2\2\2\u011e\u011c\3\2\2\2\u011f\u0121")
        buf.write("\5O(\2\u0120\u011f\3\2\2\2\u0121\u0124\3\2\2\2\u0122\u0120")
        buf.write("\3\2\2\2\u0122\u0123\3\2\2\2\u0123\u0125\3\2\2\2\u0124")
        buf.write("\u0122\3\2\2\2\u0125\u0127\7\60\2\2\u0126\u0128\5O(\2")
        buf.write("\u0127\u0126\3\2\2\2\u0128\u0129\3\2\2\2\u0129\u0127\3")
        buf.write("\2\2\2\u0129\u012a\3\2\2\2\u012a\u012c\3\2\2\2\u012b\u0114")
        buf.write("\3\2\2\2\u012b\u0122\3\2\2\2\u012cR\3\2\2\2\u012d\u012f")
        buf.write("\t\4\2\2\u012e\u0130\t\5\2\2\u012f\u012e\3\2\2\2\u012f")
        buf.write("\u0130\3\2\2\2\u0130\u0132\3\2\2\2\u0131\u0133\5O(\2\u0132")
        buf.write("\u0131\3\2\2\2\u0133\u0134\3\2\2\2\u0134\u0132\3\2\2\2")
        buf.write("\u0134\u0135\3\2\2\2\u0135T\3\2\2\2\u0136\u0137\7$\2\2")
        buf.write("\u0137V\3\2\2\2\u0138\u013b\n\6\2\2\u0139\u013b\5Y-\2")
        buf.write("\u013a\u0138\3\2\2\2\u013a\u0139\3\2\2\2\u013bX\3\2\2")
        buf.write("\2\u013c\u013d\7^\2\2\u013d\u013e\t\7\2\2\u013eZ\3\2\2")
        buf.write("\2\u013f\u0140\7^\2\2\u0140\u0143\n\7\2\2\u0141\u0143")
        buf.write("\n\b\2\2\u0142\u013f\3\2\2\2\u0142\u0141\3\2\2\2\u0143")
        buf.write("\\\3\2\2\2\u0144\u0145\7d\2\2\u0145\u0146\7q\2\2\u0146")
        buf.write("\u0147\7q\2\2\u0147\u0148\7n\2\2\u0148\u0149\7g\2\2\u0149")
        buf.write("\u014a\7c\2\2\u014a\u014b\7p\2\2\u014b^\3\2\2\2\u014c")
        buf.write("\u014d\7h\2\2\u014d\u014e\7n\2\2\u014e\u014f\7q\2\2\u014f")
        buf.write("\u0150\7c\2\2\u0150\u0151\7v\2\2\u0151`\3\2\2\2\u0152")
        buf.write("\u0153\7u\2\2\u0153\u0154\7v\2\2\u0154\u0155\7t\2\2\u0155")
        buf.write("\u0156\7k\2\2\u0156\u0157\7p\2\2\u0157\u0158\7i\2\2\u0158")
        buf.write("b\3\2\2\2\u0159\u015a\7k\2\2\u015a\u015b\7p\2\2\u015b")
        buf.write("\u015c\7v\2\2\u015cd\3\2\2\2\u015d\u0161\t\t\2\2\u015e")
        buf.write("\u0160\t\n\2\2\u015f\u015e\3\2\2\2\u0160\u0163\3\2\2\2")
        buf.write("\u0161\u015f\3\2\2\2\u0161\u0162\3\2\2\2\u0162f\3\2\2")
        buf.write("\2\u0163\u0161\3\2\2\2\u0164\u0166\t\13\2\2\u0165\u0164")
        buf.write("\3\2\2\2\u0166\u0167\3\2\2\2\u0167\u0165\3\2\2\2\u0167")
        buf.write("\u0168\3\2\2\2\u0168\u0169\3\2\2\2\u0169\u016a\b\64\2")
        buf.write("\2\u016ah\3\2\2\2\u016b\u016f\7$\2\2\u016c\u016e\5W,\2")
        buf.write("\u016d\u016c\3\2\2\2\u016e\u0171\3\2\2\2\u016f\u016d\3")
        buf.write("\2\2\2\u016f\u0170\3\2\2\2\u0170\u0172\3\2\2\2\u0171\u016f")
        buf.write("\3\2\2\2\u0172\u0173\7$\2\2\u0173\u0174\b\65\3\2\u0174")
        buf.write("j\3\2\2\2\u0175\u0179\7$\2\2\u0176\u0178\5W,\2\u0177\u0176")
        buf.write("\3\2\2\2\u0178\u017b\3\2\2\2\u0179\u0177\3\2\2\2\u0179")
        buf.write("\u017a\3\2\2\2\u017a\u017d\3\2\2\2\u017b\u0179\3\2\2\2")
        buf.write("\u017c\u017e\t\f\2\2\u017d\u017c\3\2\2\2\u017e\u017f\3")
        buf.write("\2\2\2\u017f\u0180\b\66\4\2\u0180l\3\2\2\2\u0181\u0185")
        buf.write("\7$\2\2\u0182\u0184\5W,\2\u0183\u0182\3\2\2\2\u0184\u0187")
        buf.write("\3\2\2\2\u0185\u0183\3\2\2\2\u0185\u0186\3\2\2\2\u0186")
        buf.write("\u0188\3\2\2\2\u0187\u0185\3\2\2\2\u0188\u0189\5[.\2\u0189")
        buf.write("\u018a\b\67\5\2\u018an\3\2\2\2\u018b\u018c\13\2\2\2\u018c")
        buf.write("\u018d\b8\6\2\u018dp\3\2\2\2\33\2z\177\u0083\u0088\u008c")
        buf.write("\u0097\u009f\u00ad\u0116\u011c\u0122\u0129\u012b\u012f")
        buf.write("\u0134\u013a\u0142\u015f\u0161\u0167\u016f\u0179\u017d")
        buf.write("\u0185\7\b\2\2\3\65\2\3\66\3\3\67\4\38\5")
        return buf.getvalue()


class MCLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    VOIDTYPE = 1
    PRIMI = 2
    INTLIT = 3
    REAL = 4
    BOOLLIT = 5
    BlockComment = 6
    LineComment = 7
    ADD = 8
    MULTI = 9
    LOGICALNOT = 10
    LOGICALOR = 11
    NOTEQUAL = 12
    LESSTHAN = 13
    LTOREQUAL = 14
    ASS = 15
    SUBTR = 16
    DIVISION = 17
    MODUL = 18
    LOGICALAND = 19
    LOGICALEQ = 20
    GREATER = 21
    GREATEREQ = 22
    If = 23
    Else = 24
    Do = 25
    While = 26
    For = 27
    Break = 28
    Continue = 29
    Return = 30
    LB = 31
    RB = 32
    LP = 33
    RP = 34
    LS = 35
    RS = 36
    SEMI = 37
    COMMA = 38
    IDEN = 39
    WS = 40
    STRINGLIT = 41
    UNCLOSE_STRING = 42
    ILLEGAL_ESCAPE = 43
    ERROR_CHAR = 44

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'void'", "'+'", "'*'", "'!'", "'||'", "'!='", "'<'", "'<='", 
            "'='", "'-'", "'/'", "'%'", "'&&'", "'=='", "'>'", "'>='", "'if'", 
            "'else'", "'do'", "'while'", "'for'", "'break'", "'continue'", 
            "'return'", "'('", "')'", "'{'", "'}'", "'['", "']'", "';'", 
            "','" ]

    symbolicNames = [ "<INVALID>",
            "VOIDTYPE", "PRIMI", "INTLIT", "REAL", "BOOLLIT", "BlockComment", 
            "LineComment", "ADD", "MULTI", "LOGICALNOT", "LOGICALOR", "NOTEQUAL", 
            "LESSTHAN", "LTOREQUAL", "ASS", "SUBTR", "DIVISION", "MODUL", 
            "LOGICALAND", "LOGICALEQ", "GREATER", "GREATEREQ", "If", "Else", 
            "Do", "While", "For", "Break", "Continue", "Return", "LB", "RB", 
            "LP", "RP", "LS", "RS", "SEMI", "COMMA", "IDEN", "WS", "STRINGLIT", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "VOIDTYPE", "PRIMI", "INTLIT", "REAL", "BOOLLIT", "BlockComment", 
                  "LineComment", "ADD", "MULTI", "LOGICALNOT", "LOGICALOR", 
                  "NOTEQUAL", "LESSTHAN", "LTOREQUAL", "ASS", "SUBTR", "DIVISION", 
                  "MODUL", "LOGICALAND", "LOGICALEQ", "GREATER", "GREATEREQ", 
                  "If", "Else", "Do", "While", "For", "Break", "Continue", 
                  "Return", "LB", "RB", "LP", "RP", "LS", "RS", "SEMI", 
                  "COMMA", "DIGIT", "REAL_DEC", "REAL_EXP", "DOUQUOTES", 
                  "STR_CHAR", "ESC_SEQ", "ESC_ILLEGAL", "BOOLEAN", "FLOAT", 
                  "STRING", "INT", "IDEN", "WS", "STRINGLIT", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    grammarFileName = "MC.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[51] = self.STRINGLIT_action 
            actions[52] = self.UNCLOSE_STRING_action 
            actions[53] = self.ILLEGAL_ESCAPE_action 
            actions[54] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            temp = self.text;
            self.text = temp[1:-1]

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

            y = str(self.text)
            p = ['\b', '\t', '\n', '\f', '\r', "'", '\\']
            if y[-1] in p:
                raise UncloseString(y[1:-1])
            else:
                raise UncloseString(y[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            y = str(self.text)
            raise IllegalEscape(y[1:])

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            raise ErrorToken(self.text);

     


