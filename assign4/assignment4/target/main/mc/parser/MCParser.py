# Generated from main/mc/parser/MC.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3.")
        buf.write("\u0143\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\3\2\6\2J\n")
        buf.write("\2\r\2\16\2K\3\2\3\2\3\3\3\3\5\3R\n\3\3\4\3\4\3\4\3\4")
        buf.write("\7\4X\n\4\f\4\16\4[\13\4\3\4\3\4\3\5\3\5\3\6\3\6\3\6\3")
        buf.write("\6\5\6e\n\6\3\7\3\7\3\7\3\7\5\7k\n\7\3\7\3\7\3\7\3\b\3")
        buf.write("\b\3\b\7\bs\n\b\f\b\16\bv\13\b\3\t\3\t\3\t\3\t\3\t\5\t")
        buf.write("}\n\t\3\n\3\n\3\n\3\n\5\n\u0083\n\n\3\13\3\13\7\13\u0087")
        buf.write("\n\13\f\13\16\13\u008a\13\13\3\13\3\13\3\f\3\f\5\f\u0090")
        buf.write("\n\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u009a\n\r\3\16")
        buf.write("\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\5\17\u00a5\n")
        buf.write("\17\3\20\3\20\3\20\3\20\3\20\3\20\7\20\u00ad\n\20\f\20")
        buf.write("\16\20\u00b0\13\20\3\21\3\21\3\21\3\21\3\21\3\21\7\21")
        buf.write("\u00b8\n\21\f\21\16\21\u00bb\13\21\3\22\3\22\3\22\3\22")
        buf.write("\3\22\5\22\u00c2\n\22\3\23\3\23\3\24\3\24\3\24\3\24\3")
        buf.write("\24\5\24\u00cb\n\24\3\25\3\25\3\25\3\25\3\25\3\25\7\25")
        buf.write("\u00d3\n\25\f\25\16\25\u00d6\13\25\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\7\26\u00de\n\26\f\26\16\26\u00e1\13\26\3\27")
        buf.write("\3\27\3\27\5\27\u00e6\n\27\3\30\3\30\3\30\3\30\3\30\3")
        buf.write("\30\5\30\u00ee\n\30\3\31\3\31\3\31\3\31\3\31\5\31\u00f5")
        buf.write("\n\31\3\32\3\32\3\32\3\32\5\32\u00fb\n\32\3\32\3\32\7")
        buf.write("\32\u00ff\n\32\f\32\16\32\u0102\13\32\3\33\3\33\3\34\3")
        buf.write("\34\3\34\5\34\u0109\n\34\3\34\3\34\3\35\3\35\3\35\7\35")
        buf.write("\u0110\n\35\f\35\16\35\u0113\13\35\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\5\36\u011c\n\36\3\37\3\37\6\37\u0120\n")
        buf.write("\37\r\37\16\37\u0121\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3")
        buf.write(" \3 \3 \3 \3 \3 \3!\3!\3!\3\"\3\"\3\"\3#\3#\3#\3#\3#\3")
        buf.write("#\5#\u013e\n#\3$\3$\3$\3$\3Y\7\36 (*\62%\2\4\6\b\n\f\16")
        buf.write("\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDF")
        buf.write("\2\b\4\2\16\16\26\26\4\2\17\20\27\30\4\2\n\n\22\22\4\2")
        buf.write("\13\13\23\24\4\2\f\f\22\22\4\2\5\7++\2\u0143\2I\3\2\2")
        buf.write("\2\4Q\3\2\2\2\6S\3\2\2\2\b^\3\2\2\2\n`\3\2\2\2\ff\3\2")
        buf.write("\2\2\16o\3\2\2\2\20|\3\2\2\2\22~\3\2\2\2\24\u0084\3\2")
        buf.write("\2\2\26\u008f\3\2\2\2\30\u0099\3\2\2\2\32\u009b\3\2\2")
        buf.write("\2\34\u00a4\3\2\2\2\36\u00a6\3\2\2\2 \u00b1\3\2\2\2\"")
        buf.write("\u00c1\3\2\2\2$\u00c3\3\2\2\2&\u00ca\3\2\2\2(\u00cc\3")
        buf.write("\2\2\2*\u00d7\3\2\2\2,\u00e5\3\2\2\2.\u00ed\3\2\2\2\60")
        buf.write("\u00f4\3\2\2\2\62\u00fa\3\2\2\2\64\u0103\3\2\2\2\66\u0105")
        buf.write("\3\2\2\28\u010c\3\2\2\2:\u0114\3\2\2\2<\u011d\3\2\2\2")
        buf.write(">\u0127\3\2\2\2@\u0131\3\2\2\2B\u0134\3\2\2\2D\u013d\3")
        buf.write("\2\2\2F\u013f\3\2\2\2HJ\5\4\3\2IH\3\2\2\2JK\3\2\2\2KI")
        buf.write("\3\2\2\2KL\3\2\2\2LM\3\2\2\2MN\7\2\2\3N\3\3\2\2\2OR\5")
        buf.write("\6\4\2PR\5\f\7\2QO\3\2\2\2QP\3\2\2\2R\5\3\2\2\2ST\5\b")
        buf.write("\5\2TY\5\n\6\2UV\7(\2\2VX\5\n\6\2WU\3\2\2\2X[\3\2\2\2")
        buf.write("YZ\3\2\2\2YW\3\2\2\2Z\\\3\2\2\2[Y\3\2\2\2\\]\7\'\2\2]")
        buf.write("\7\3\2\2\2^_\7\4\2\2_\t\3\2\2\2`d\7)\2\2ab\7%\2\2bc\7")
        buf.write("\5\2\2ce\7&\2\2da\3\2\2\2de\3\2\2\2e\13\3\2\2\2fg\5\20")
        buf.write("\t\2gh\7)\2\2hj\7!\2\2ik\5\16\b\2ji\3\2\2\2jk\3\2\2\2")
        buf.write("kl\3\2\2\2lm\7\"\2\2mn\5\24\13\2n\r\3\2\2\2ot\5\22\n\2")
        buf.write("pq\7(\2\2qs\5\22\n\2rp\3\2\2\2sv\3\2\2\2tr\3\2\2\2tu\3")
        buf.write("\2\2\2u\17\3\2\2\2vt\3\2\2\2w}\7\4\2\2x}\7\3\2\2yz\7\4")
        buf.write("\2\2z{\7%\2\2{}\7&\2\2|w\3\2\2\2|x\3\2\2\2|y\3\2\2\2}")
        buf.write("\21\3\2\2\2~\177\7\4\2\2\177\u0082\7)\2\2\u0080\u0081")
        buf.write("\7%\2\2\u0081\u0083\7&\2\2\u0082\u0080\3\2\2\2\u0082\u0083")
        buf.write("\3\2\2\2\u0083\23\3\2\2\2\u0084\u0088\7#\2\2\u0085\u0087")
        buf.write("\5\26\f\2\u0086\u0085\3\2\2\2\u0087\u008a\3\2\2\2\u0088")
        buf.write("\u0086\3\2\2\2\u0088\u0089\3\2\2\2\u0089\u008b\3\2\2\2")
        buf.write("\u008a\u0088\3\2\2\2\u008b\u008c\7$\2\2\u008c\25\3\2\2")
        buf.write("\2\u008d\u0090\5\6\4\2\u008e\u0090\5\30\r\2\u008f\u008d")
        buf.write("\3\2\2\2\u008f\u008e\3\2\2\2\u0090\27\3\2\2\2\u0091\u009a")
        buf.write("\5:\36\2\u0092\u009a\5<\37\2\u0093\u009a\5> \2\u0094\u009a")
        buf.write("\5@!\2\u0095\u009a\5B\"\2\u0096\u009a\5D#\2\u0097\u009a")
        buf.write("\5F$\2\u0098\u009a\5\24\13\2\u0099\u0091\3\2\2\2\u0099")
        buf.write("\u0092\3\2\2\2\u0099\u0093\3\2\2\2\u0099\u0094\3\2\2\2")
        buf.write("\u0099\u0095\3\2\2\2\u0099\u0096\3\2\2\2\u0099\u0097\3")
        buf.write("\2\2\2\u0099\u0098\3\2\2\2\u009a\31\3\2\2\2\u009b\u009c")
        buf.write("\7%\2\2\u009c\u009d\5\34\17\2\u009d\u009e\7&\2\2\u009e")
        buf.write("\33\3\2\2\2\u009f\u00a0\5\36\20\2\u00a0\u00a1\7\21\2\2")
        buf.write("\u00a1\u00a2\5\34\17\2\u00a2\u00a5\3\2\2\2\u00a3\u00a5")
        buf.write("\5\36\20\2\u00a4\u009f\3\2\2\2\u00a4\u00a3\3\2\2\2\u00a5")
        buf.write("\35\3\2\2\2\u00a6\u00a7\b\20\1\2\u00a7\u00a8\5 \21\2\u00a8")
        buf.write("\u00ae\3\2\2\2\u00a9\u00aa\f\4\2\2\u00aa\u00ab\7\r\2\2")
        buf.write("\u00ab\u00ad\5 \21\2\u00ac\u00a9\3\2\2\2\u00ad\u00b0\3")
        buf.write("\2\2\2\u00ae\u00ac\3\2\2\2\u00ae\u00af\3\2\2\2\u00af\37")
        buf.write("\3\2\2\2\u00b0\u00ae\3\2\2\2\u00b1\u00b2\b\21\1\2\u00b2")
        buf.write("\u00b3\5\"\22\2\u00b3\u00b9\3\2\2\2\u00b4\u00b5\f\4\2")
        buf.write("\2\u00b5\u00b6\7\25\2\2\u00b6\u00b8\5\"\22\2\u00b7\u00b4")
        buf.write("\3\2\2\2\u00b8\u00bb\3\2\2\2\u00b9\u00b7\3\2\2\2\u00b9")
        buf.write("\u00ba\3\2\2\2\u00ba!\3\2\2\2\u00bb\u00b9\3\2\2\2\u00bc")
        buf.write("\u00bd\5&\24\2\u00bd\u00be\5$\23\2\u00be\u00bf\5&\24\2")
        buf.write("\u00bf\u00c2\3\2\2\2\u00c0\u00c2\5&\24\2\u00c1\u00bc\3")
        buf.write("\2\2\2\u00c1\u00c0\3\2\2\2\u00c2#\3\2\2\2\u00c3\u00c4")
        buf.write("\t\2\2\2\u00c4%\3\2\2\2\u00c5\u00c6\5(\25\2\u00c6\u00c7")
        buf.write("\t\3\2\2\u00c7\u00c8\5(\25\2\u00c8\u00cb\3\2\2\2\u00c9")
        buf.write("\u00cb\5(\25\2\u00ca\u00c5\3\2\2\2\u00ca\u00c9\3\2\2\2")
        buf.write("\u00cb\'\3\2\2\2\u00cc\u00cd\b\25\1\2\u00cd\u00ce\5*\26")
        buf.write("\2\u00ce\u00d4\3\2\2\2\u00cf\u00d0\f\4\2\2\u00d0\u00d1")
        buf.write("\t\4\2\2\u00d1\u00d3\5*\26\2\u00d2\u00cf\3\2\2\2\u00d3")
        buf.write("\u00d6\3\2\2\2\u00d4\u00d2\3\2\2\2\u00d4\u00d5\3\2\2\2")
        buf.write("\u00d5)\3\2\2\2\u00d6\u00d4\3\2\2\2\u00d7\u00d8\b\26\1")
        buf.write("\2\u00d8\u00d9\5,\27\2\u00d9\u00df\3\2\2\2\u00da\u00db")
        buf.write("\f\4\2\2\u00db\u00dc\t\5\2\2\u00dc\u00de\5,\27\2\u00dd")
        buf.write("\u00da\3\2\2\2\u00de\u00e1\3\2\2\2\u00df\u00dd\3\2\2\2")
        buf.write("\u00df\u00e0\3\2\2\2\u00e0+\3\2\2\2\u00e1\u00df\3\2\2")
        buf.write("\2\u00e2\u00e3\t\6\2\2\u00e3\u00e6\5,\27\2\u00e4\u00e6")
        buf.write("\5.\30\2\u00e5\u00e2\3\2\2\2\u00e5\u00e4\3\2\2\2\u00e6")
        buf.write("-\3\2\2\2\u00e7\u00e8\5\60\31\2\u00e8\u00e9\7%\2\2\u00e9")
        buf.write("\u00ea\5\60\31\2\u00ea\u00eb\7&\2\2\u00eb\u00ee\3\2\2")
        buf.write("\2\u00ec\u00ee\5\60\31\2\u00ed\u00e7\3\2\2\2\u00ed\u00ec")
        buf.write("\3\2\2\2\u00ee/\3\2\2\2\u00ef\u00f0\7!\2\2\u00f0\u00f1")
        buf.write("\5\34\17\2\u00f1\u00f2\7\"\2\2\u00f2\u00f5\3\2\2\2\u00f3")
        buf.write("\u00f5\5\62\32\2\u00f4\u00ef\3\2\2\2\u00f4\u00f3\3\2\2")
        buf.write("\2\u00f5\61\3\2\2\2\u00f6\u00f7\b\32\1\2\u00f7\u00fb\5")
        buf.write("\64\33\2\u00f8\u00fb\7)\2\2\u00f9\u00fb\5\66\34\2\u00fa")
        buf.write("\u00f6\3\2\2\2\u00fa\u00f8\3\2\2\2\u00fa\u00f9\3\2\2\2")
        buf.write("\u00fb\u0100\3\2\2\2\u00fc\u00fd\f\3\2\2\u00fd\u00ff\5")
        buf.write("\32\16\2\u00fe\u00fc\3\2\2\2\u00ff\u0102\3\2\2\2\u0100")
        buf.write("\u00fe\3\2\2\2\u0100\u0101\3\2\2\2\u0101\63\3\2\2\2\u0102")
        buf.write("\u0100\3\2\2\2\u0103\u0104\t\7\2\2\u0104\65\3\2\2\2\u0105")
        buf.write("\u0106\7)\2\2\u0106\u0108\7!\2\2\u0107\u0109\58\35\2\u0108")
        buf.write("\u0107\3\2\2\2\u0108\u0109\3\2\2\2\u0109\u010a\3\2\2\2")
        buf.write("\u010a\u010b\7\"\2\2\u010b\67\3\2\2\2\u010c\u0111\5\34")
        buf.write("\17\2\u010d\u010e\7(\2\2\u010e\u0110\5\34\17\2\u010f\u010d")
        buf.write("\3\2\2\2\u0110\u0113\3\2\2\2\u0111\u010f\3\2\2\2\u0111")
        buf.write("\u0112\3\2\2\2\u01129\3\2\2\2\u0113\u0111\3\2\2\2\u0114")
        buf.write("\u0115\7\31\2\2\u0115\u0116\7!\2\2\u0116\u0117\5\34\17")
        buf.write("\2\u0117\u0118\7\"\2\2\u0118\u011b\5\30\r\2\u0119\u011a")
        buf.write("\7\32\2\2\u011a\u011c\5\30\r\2\u011b\u0119\3\2\2\2\u011b")
        buf.write("\u011c\3\2\2\2\u011c;\3\2\2\2\u011d\u011f\7\33\2\2\u011e")
        buf.write("\u0120\5\30\r\2\u011f\u011e\3\2\2\2\u0120\u0121\3\2\2")
        buf.write("\2\u0121\u011f\3\2\2\2\u0121\u0122\3\2\2\2\u0122\u0123")
        buf.write("\3\2\2\2\u0123\u0124\7\34\2\2\u0124\u0125\5\34\17\2\u0125")
        buf.write("\u0126\7\'\2\2\u0126=\3\2\2\2\u0127\u0128\7\35\2\2\u0128")
        buf.write("\u0129\7!\2\2\u0129\u012a\5\34\17\2\u012a\u012b\7\'\2")
        buf.write("\2\u012b\u012c\5\34\17\2\u012c\u012d\7\'\2\2\u012d\u012e")
        buf.write("\5\34\17\2\u012e\u012f\7\"\2\2\u012f\u0130\5\30\r\2\u0130")
        buf.write("?\3\2\2\2\u0131\u0132\7\36\2\2\u0132\u0133\7\'\2\2\u0133")
        buf.write("A\3\2\2\2\u0134\u0135\7\37\2\2\u0135\u0136\7\'\2\2\u0136")
        buf.write("C\3\2\2\2\u0137\u0138\7 \2\2\u0138\u0139\5\34\17\2\u0139")
        buf.write("\u013a\7\'\2\2\u013a\u013e\3\2\2\2\u013b\u013c\7 \2\2")
        buf.write("\u013c\u013e\7\'\2\2\u013d\u0137\3\2\2\2\u013d\u013b\3")
        buf.write("\2\2\2\u013eE\3\2\2\2\u013f\u0140\5\34\17\2\u0140\u0141")
        buf.write("\7\'\2\2\u0141G\3\2\2\2\36KQYdjt|\u0082\u0088\u008f\u0099")
        buf.write("\u00a4\u00ae\u00b9\u00c1\u00ca\u00d4\u00df\u00e5\u00ed")
        buf.write("\u00f4\u00fa\u0100\u0108\u0111\u011b\u0121\u013d")
        return buf.getvalue()


class MCParser ( Parser ):

    grammarFileName = "MC.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'void'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'+'", "'*'", 
                     "'!'", "'||'", "'!='", "'<'", "'<='", "'='", "'-'", 
                     "'/'", "'%'", "'&&'", "'=='", "'>'", "'>='", "'if'", 
                     "'else'", "'do'", "'while'", "'for'", "'break'", "'continue'", 
                     "'return'", "'('", "')'", "'{'", "'}'", "'['", "']'", 
                     "';'", "','" ]

    symbolicNames = [ "<INVALID>", "VOIDTYPE", "PRIMI", "INTLIT", "REAL", 
                      "BOOLLIT", "BlockComment", "LineComment", "ADD", "MULTI", 
                      "LOGICALNOT", "LOGICALOR", "NOTEQUAL", "LESSTHAN", 
                      "LTOREQUAL", "ASS", "SUBTR", "DIVISION", "MODUL", 
                      "LOGICALAND", "LOGICALEQ", "GREATER", "GREATEREQ", 
                      "If", "Else", "Do", "While", "For", "Break", "Continue", 
                      "Return", "LB", "RB", "LP", "RP", "LS", "RS", "SEMI", 
                      "COMMA", "IDEN", "WS", "STRINGLIT", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_declar = 1
    RULE_vardec = 2
    RULE_vartypes = 3
    RULE_varname = 4
    RULE_funcdec = 5
    RULE_paralist = 6
    RULE_functypes = 7
    RULE_funcpara = 8
    RULE_blockstate = 9
    RULE_manydeclar = 10
    RULE_statement = 11
    RULE_postfix_array = 12
    RULE_exp = 13
    RULE_exp1 = 14
    RULE_exp2 = 15
    RULE_exp3 = 16
    RULE_eq_and_not = 17
    RULE_exp4 = 18
    RULE_exp5 = 19
    RULE_exp6 = 20
    RULE_exp7 = 21
    RULE_exp8 = 22
    RULE_exp9 = 23
    RULE_operands = 24
    RULE_literal = 25
    RULE_call_func = 26
    RULE_para_list = 27
    RULE_if_statement = 28
    RULE_do_while_statement = 29
    RULE_for_statement = 30
    RULE_break_statement = 31
    RULE_continue_statement = 32
    RULE_return_statement = 33
    RULE_exp_statement = 34

    ruleNames =  [ "program", "declar", "vardec", "vartypes", "varname", 
                   "funcdec", "paralist", "functypes", "funcpara", "blockstate", 
                   "manydeclar", "statement", "postfix_array", "exp", "exp1", 
                   "exp2", "exp3", "eq_and_not", "exp4", "exp5", "exp6", 
                   "exp7", "exp8", "exp9", "operands", "literal", "call_func", 
                   "para_list", "if_statement", "do_while_statement", "for_statement", 
                   "break_statement", "continue_statement", "return_statement", 
                   "exp_statement" ]

    EOF = Token.EOF
    VOIDTYPE=1
    PRIMI=2
    INTLIT=3
    REAL=4
    BOOLLIT=5
    BlockComment=6
    LineComment=7
    ADD=8
    MULTI=9
    LOGICALNOT=10
    LOGICALOR=11
    NOTEQUAL=12
    LESSTHAN=13
    LTOREQUAL=14
    ASS=15
    SUBTR=16
    DIVISION=17
    MODUL=18
    LOGICALAND=19
    LOGICALEQ=20
    GREATER=21
    GREATEREQ=22
    If=23
    Else=24
    Do=25
    While=26
    For=27
    Break=28
    Continue=29
    Return=30
    LB=31
    RB=32
    LP=33
    RP=34
    LS=35
    RS=36
    SEMI=37
    COMMA=38
    IDEN=39
    WS=40
    STRINGLIT=41
    UNCLOSE_STRING=42
    ILLEGAL_ESCAPE=43
    ERROR_CHAR=44

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MCParser.EOF, 0)

        def declar(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.DeclarContext)
            else:
                return self.getTypedRuleContext(MCParser.DeclarContext,i)


        def getRuleIndex(self):
            return MCParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MCParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 70
                self.declar()
                self.state = 73 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MCParser.VOIDTYPE or _la==MCParser.PRIMI):
                    break

            self.state = 75
            self.match(MCParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardec(self):
            return self.getTypedRuleContext(MCParser.VardecContext,0)


        def funcdec(self):
            return self.getTypedRuleContext(MCParser.FuncdecContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_declar

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclar" ):
                return visitor.visitDeclar(self)
            else:
                return visitor.visitChildren(self)




    def declar(self):

        localctx = MCParser.DeclarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declar)
        try:
            self.state = 79
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 77
                self.vardec()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 78
                self.funcdec()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardecContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vartypes(self):
            return self.getTypedRuleContext(MCParser.VartypesContext,0)


        def varname(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.VarnameContext)
            else:
                return self.getTypedRuleContext(MCParser.VarnameContext,i)


        def SEMI(self):
            return self.getToken(MCParser.SEMI, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MCParser.COMMA)
            else:
                return self.getToken(MCParser.COMMA, i)

        def getRuleIndex(self):
            return MCParser.RULE_vardec

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardec" ):
                return visitor.visitVardec(self)
            else:
                return visitor.visitChildren(self)




    def vardec(self):

        localctx = MCParser.VardecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_vardec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.vartypes()
            self.state = 82
            self.varname()
            self.state = 87
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 83
                    self.match(MCParser.COMMA)
                    self.state = 84
                    self.varname() 
                self.state = 89
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

            self.state = 90
            self.match(MCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VartypesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRIMI(self):
            return self.getToken(MCParser.PRIMI, 0)

        def getRuleIndex(self):
            return MCParser.RULE_vartypes

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVartypes" ):
                return visitor.visitVartypes(self)
            else:
                return visitor.visitChildren(self)




    def vartypes(self):

        localctx = MCParser.VartypesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_vartypes)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.match(MCParser.PRIMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarnameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDEN(self):
            return self.getToken(MCParser.IDEN, 0)

        def LS(self):
            return self.getToken(MCParser.LS, 0)

        def INTLIT(self):
            return self.getToken(MCParser.INTLIT, 0)

        def RS(self):
            return self.getToken(MCParser.RS, 0)

        def getRuleIndex(self):
            return MCParser.RULE_varname

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarname" ):
                return visitor.visitVarname(self)
            else:
                return visitor.visitChildren(self)




    def varname(self):

        localctx = MCParser.VarnameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_varname)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(MCParser.IDEN)
            self.state = 98
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MCParser.LS:
                self.state = 95
                self.match(MCParser.LS)
                self.state = 96
                self.match(MCParser.INTLIT)
                self.state = 97
                self.match(MCParser.RS)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncdecContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functypes(self):
            return self.getTypedRuleContext(MCParser.FunctypesContext,0)


        def IDEN(self):
            return self.getToken(MCParser.IDEN, 0)

        def LB(self):
            return self.getToken(MCParser.LB, 0)

        def RB(self):
            return self.getToken(MCParser.RB, 0)

        def blockstate(self):
            return self.getTypedRuleContext(MCParser.BlockstateContext,0)


        def paralist(self):
            return self.getTypedRuleContext(MCParser.ParalistContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_funcdec

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncdec" ):
                return visitor.visitFuncdec(self)
            else:
                return visitor.visitChildren(self)




    def funcdec(self):

        localctx = MCParser.FuncdecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_funcdec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.functypes()
            self.state = 101
            self.match(MCParser.IDEN)
            self.state = 102
            self.match(MCParser.LB)
            self.state = 104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MCParser.PRIMI:
                self.state = 103
                self.paralist()


            self.state = 106
            self.match(MCParser.RB)
            self.state = 107
            self.blockstate()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParalistContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcpara(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.FuncparaContext)
            else:
                return self.getTypedRuleContext(MCParser.FuncparaContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MCParser.COMMA)
            else:
                return self.getToken(MCParser.COMMA, i)

        def getRuleIndex(self):
            return MCParser.RULE_paralist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParalist" ):
                return visitor.visitParalist(self)
            else:
                return visitor.visitChildren(self)




    def paralist(self):

        localctx = MCParser.ParalistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_paralist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.funcpara()
            self.state = 114
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MCParser.COMMA:
                self.state = 110
                self.match(MCParser.COMMA)
                self.state = 111
                self.funcpara()
                self.state = 116
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctypesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRIMI(self):
            return self.getToken(MCParser.PRIMI, 0)

        def VOIDTYPE(self):
            return self.getToken(MCParser.VOIDTYPE, 0)

        def LS(self):
            return self.getToken(MCParser.LS, 0)

        def RS(self):
            return self.getToken(MCParser.RS, 0)

        def getRuleIndex(self):
            return MCParser.RULE_functypes

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctypes" ):
                return visitor.visitFunctypes(self)
            else:
                return visitor.visitChildren(self)




    def functypes(self):

        localctx = MCParser.FunctypesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_functypes)
        try:
            self.state = 122
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 117
                self.match(MCParser.PRIMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 118
                self.match(MCParser.VOIDTYPE)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 119
                self.match(MCParser.PRIMI)
                self.state = 120
                self.match(MCParser.LS)
                self.state = 121
                self.match(MCParser.RS)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncparaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRIMI(self):
            return self.getToken(MCParser.PRIMI, 0)

        def IDEN(self):
            return self.getToken(MCParser.IDEN, 0)

        def LS(self):
            return self.getToken(MCParser.LS, 0)

        def RS(self):
            return self.getToken(MCParser.RS, 0)

        def getRuleIndex(self):
            return MCParser.RULE_funcpara

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncpara" ):
                return visitor.visitFuncpara(self)
            else:
                return visitor.visitChildren(self)




    def funcpara(self):

        localctx = MCParser.FuncparaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_funcpara)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.match(MCParser.PRIMI)
            self.state = 125
            self.match(MCParser.IDEN)
            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MCParser.LS:
                self.state = 126
                self.match(MCParser.LS)
                self.state = 127
                self.match(MCParser.RS)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockstateContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(MCParser.LP, 0)

        def RP(self):
            return self.getToken(MCParser.RP, 0)

        def manydeclar(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.ManydeclarContext)
            else:
                return self.getTypedRuleContext(MCParser.ManydeclarContext,i)


        def getRuleIndex(self):
            return MCParser.RULE_blockstate

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockstate" ):
                return visitor.visitBlockstate(self)
            else:
                return visitor.visitChildren(self)




    def blockstate(self):

        localctx = MCParser.BlockstateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_blockstate)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.match(MCParser.LP)
            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.PRIMI) | (1 << MCParser.INTLIT) | (1 << MCParser.REAL) | (1 << MCParser.BOOLLIT) | (1 << MCParser.LOGICALNOT) | (1 << MCParser.SUBTR) | (1 << MCParser.If) | (1 << MCParser.Do) | (1 << MCParser.For) | (1 << MCParser.Break) | (1 << MCParser.Continue) | (1 << MCParser.Return) | (1 << MCParser.LB) | (1 << MCParser.LP) | (1 << MCParser.IDEN) | (1 << MCParser.STRINGLIT))) != 0):
                self.state = 131
                self.manydeclar()
                self.state = 136
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 137
            self.match(MCParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ManydeclarContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardec(self):
            return self.getTypedRuleContext(MCParser.VardecContext,0)


        def statement(self):
            return self.getTypedRuleContext(MCParser.StatementContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_manydeclar

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitManydeclar" ):
                return visitor.visitManydeclar(self)
            else:
                return visitor.visitChildren(self)




    def manydeclar(self):

        localctx = MCParser.ManydeclarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_manydeclar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MCParser.PRIMI]:
                self.state = 139
                self.vardec()
                pass
            elif token in [MCParser.INTLIT, MCParser.REAL, MCParser.BOOLLIT, MCParser.LOGICALNOT, MCParser.SUBTR, MCParser.If, MCParser.Do, MCParser.For, MCParser.Break, MCParser.Continue, MCParser.Return, MCParser.LB, MCParser.LP, MCParser.IDEN, MCParser.STRINGLIT]:
                self.state = 140
                self.statement()
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


    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_statement(self):
            return self.getTypedRuleContext(MCParser.If_statementContext,0)


        def do_while_statement(self):
            return self.getTypedRuleContext(MCParser.Do_while_statementContext,0)


        def for_statement(self):
            return self.getTypedRuleContext(MCParser.For_statementContext,0)


        def break_statement(self):
            return self.getTypedRuleContext(MCParser.Break_statementContext,0)


        def continue_statement(self):
            return self.getTypedRuleContext(MCParser.Continue_statementContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(MCParser.Return_statementContext,0)


        def exp_statement(self):
            return self.getTypedRuleContext(MCParser.Exp_statementContext,0)


        def blockstate(self):
            return self.getTypedRuleContext(MCParser.BlockstateContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MCParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_statement)
        try:
            self.state = 151
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MCParser.If]:
                self.enterOuterAlt(localctx, 1)
                self.state = 143
                self.if_statement()
                pass
            elif token in [MCParser.Do]:
                self.enterOuterAlt(localctx, 2)
                self.state = 144
                self.do_while_statement()
                pass
            elif token in [MCParser.For]:
                self.enterOuterAlt(localctx, 3)
                self.state = 145
                self.for_statement()
                pass
            elif token in [MCParser.Break]:
                self.enterOuterAlt(localctx, 4)
                self.state = 146
                self.break_statement()
                pass
            elif token in [MCParser.Continue]:
                self.enterOuterAlt(localctx, 5)
                self.state = 147
                self.continue_statement()
                pass
            elif token in [MCParser.Return]:
                self.enterOuterAlt(localctx, 6)
                self.state = 148
                self.return_statement()
                pass
            elif token in [MCParser.INTLIT, MCParser.REAL, MCParser.BOOLLIT, MCParser.LOGICALNOT, MCParser.SUBTR, MCParser.LB, MCParser.IDEN, MCParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 7)
                self.state = 149
                self.exp_statement()
                pass
            elif token in [MCParser.LP]:
                self.enterOuterAlt(localctx, 8)
                self.state = 150
                self.blockstate()
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


    class Postfix_arrayContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LS(self):
            return self.getToken(MCParser.LS, 0)

        def exp(self):
            return self.getTypedRuleContext(MCParser.ExpContext,0)


        def RS(self):
            return self.getToken(MCParser.RS, 0)

        def getRuleIndex(self):
            return MCParser.RULE_postfix_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPostfix_array" ):
                return visitor.visitPostfix_array(self)
            else:
                return visitor.visitChildren(self)




    def postfix_array(self):

        localctx = MCParser.Postfix_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_postfix_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.match(MCParser.LS)
            self.state = 154
            self.exp()
            self.state = 155
            self.match(MCParser.RS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp1(self):
            return self.getTypedRuleContext(MCParser.Exp1Context,0)


        def ASS(self):
            return self.getToken(MCParser.ASS, 0)

        def exp(self):
            return self.getTypedRuleContext(MCParser.ExpContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = MCParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_exp)
        try:
            self.state = 162
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 157
                self.exp1(0)
                self.state = 158
                self.match(MCParser.ASS)
                self.state = 159
                self.exp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 161
                self.exp1(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp2(self):
            return self.getTypedRuleContext(MCParser.Exp2Context,0)


        def exp1(self):
            return self.getTypedRuleContext(MCParser.Exp1Context,0)


        def LOGICALOR(self):
            return self.getToken(MCParser.LOGICALOR, 0)

        def getRuleIndex(self):
            return MCParser.RULE_exp1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp1" ):
                return visitor.visitExp1(self)
            else:
                return visitor.visitChildren(self)



    def exp1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MCParser.Exp1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_exp1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.exp2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 172
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MCParser.Exp1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp1)
                    self.state = 167
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 168
                    self.match(MCParser.LOGICALOR)
                    self.state = 169
                    self.exp2(0) 
                self.state = 174
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp3(self):
            return self.getTypedRuleContext(MCParser.Exp3Context,0)


        def exp2(self):
            return self.getTypedRuleContext(MCParser.Exp2Context,0)


        def LOGICALAND(self):
            return self.getToken(MCParser.LOGICALAND, 0)

        def getRuleIndex(self):
            return MCParser.RULE_exp2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp2" ):
                return visitor.visitExp2(self)
            else:
                return visitor.visitChildren(self)



    def exp2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MCParser.Exp2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_exp2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self.exp3()
            self._ctx.stop = self._input.LT(-1)
            self.state = 183
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MCParser.Exp2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                    self.state = 178
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 179
                    self.match(MCParser.LOGICALAND)
                    self.state = 180
                    self.exp3() 
                self.state = 185
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp4(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.Exp4Context)
            else:
                return self.getTypedRuleContext(MCParser.Exp4Context,i)


        def eq_and_not(self):
            return self.getTypedRuleContext(MCParser.Eq_and_notContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_exp3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp3" ):
                return visitor.visitExp3(self)
            else:
                return visitor.visitChildren(self)




    def exp3(self):

        localctx = MCParser.Exp3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_exp3)
        try:
            self.state = 191
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 186
                self.exp4()
                self.state = 187
                self.eq_and_not()
                self.state = 188
                self.exp4()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 190
                self.exp4()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Eq_and_notContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LOGICALEQ(self):
            return self.getToken(MCParser.LOGICALEQ, 0)

        def NOTEQUAL(self):
            return self.getToken(MCParser.NOTEQUAL, 0)

        def getRuleIndex(self):
            return MCParser.RULE_eq_and_not

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEq_and_not" ):
                return visitor.visitEq_and_not(self)
            else:
                return visitor.visitChildren(self)




    def eq_and_not(self):

        localctx = MCParser.Eq_and_notContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_eq_and_not)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            _la = self._input.LA(1)
            if not(_la==MCParser.NOTEQUAL or _la==MCParser.LOGICALEQ):
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


    class Exp4Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp5(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.Exp5Context)
            else:
                return self.getTypedRuleContext(MCParser.Exp5Context,i)


        def LESSTHAN(self):
            return self.getToken(MCParser.LESSTHAN, 0)

        def LTOREQUAL(self):
            return self.getToken(MCParser.LTOREQUAL, 0)

        def GREATER(self):
            return self.getToken(MCParser.GREATER, 0)

        def GREATEREQ(self):
            return self.getToken(MCParser.GREATEREQ, 0)

        def getRuleIndex(self):
            return MCParser.RULE_exp4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp4" ):
                return visitor.visitExp4(self)
            else:
                return visitor.visitChildren(self)




    def exp4(self):

        localctx = MCParser.Exp4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_exp4)
        self._la = 0 # Token type
        try:
            self.state = 200
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 195
                self.exp5(0)
                self.state = 196
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.LESSTHAN) | (1 << MCParser.LTOREQUAL) | (1 << MCParser.GREATER) | (1 << MCParser.GREATEREQ))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 197
                self.exp5(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 199
                self.exp5(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp5Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp6(self):
            return self.getTypedRuleContext(MCParser.Exp6Context,0)


        def exp5(self):
            return self.getTypedRuleContext(MCParser.Exp5Context,0)


        def ADD(self):
            return self.getToken(MCParser.ADD, 0)

        def SUBTR(self):
            return self.getToken(MCParser.SUBTR, 0)

        def getRuleIndex(self):
            return MCParser.RULE_exp5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp5" ):
                return visitor.visitExp5(self)
            else:
                return visitor.visitChildren(self)



    def exp5(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MCParser.Exp5Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 38
        self.enterRecursionRule(localctx, 38, self.RULE_exp5, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.exp6(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 210
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MCParser.Exp5Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp5)
                    self.state = 205
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 206
                    _la = self._input.LA(1)
                    if not(_la==MCParser.ADD or _la==MCParser.SUBTR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 207
                    self.exp6(0) 
                self.state = 212
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp6Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp7(self):
            return self.getTypedRuleContext(MCParser.Exp7Context,0)


        def exp6(self):
            return self.getTypedRuleContext(MCParser.Exp6Context,0)


        def DIVISION(self):
            return self.getToken(MCParser.DIVISION, 0)

        def MODUL(self):
            return self.getToken(MCParser.MODUL, 0)

        def MULTI(self):
            return self.getToken(MCParser.MULTI, 0)

        def getRuleIndex(self):
            return MCParser.RULE_exp6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp6" ):
                return visitor.visitExp6(self)
            else:
                return visitor.visitChildren(self)



    def exp6(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MCParser.Exp6Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_exp6, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.exp7()
            self._ctx.stop = self._input.LT(-1)
            self.state = 221
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MCParser.Exp6Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp6)
                    self.state = 216
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 217
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.MULTI) | (1 << MCParser.DIVISION) | (1 << MCParser.MODUL))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 218
                    self.exp7() 
                self.state = 223
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp7Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp7(self):
            return self.getTypedRuleContext(MCParser.Exp7Context,0)


        def LOGICALNOT(self):
            return self.getToken(MCParser.LOGICALNOT, 0)

        def SUBTR(self):
            return self.getToken(MCParser.SUBTR, 0)

        def exp8(self):
            return self.getTypedRuleContext(MCParser.Exp8Context,0)


        def getRuleIndex(self):
            return MCParser.RULE_exp7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp7" ):
                return visitor.visitExp7(self)
            else:
                return visitor.visitChildren(self)




    def exp7(self):

        localctx = MCParser.Exp7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_exp7)
        self._la = 0 # Token type
        try:
            self.state = 227
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MCParser.LOGICALNOT, MCParser.SUBTR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 224
                _la = self._input.LA(1)
                if not(_la==MCParser.LOGICALNOT or _la==MCParser.SUBTR):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 225
                self.exp7()
                pass
            elif token in [MCParser.INTLIT, MCParser.REAL, MCParser.BOOLLIT, MCParser.LB, MCParser.IDEN, MCParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 226
                self.exp8()
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


    class Exp8Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp9(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.Exp9Context)
            else:
                return self.getTypedRuleContext(MCParser.Exp9Context,i)


        def LS(self):
            return self.getToken(MCParser.LS, 0)

        def RS(self):
            return self.getToken(MCParser.RS, 0)

        def getRuleIndex(self):
            return MCParser.RULE_exp8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp8" ):
                return visitor.visitExp8(self)
            else:
                return visitor.visitChildren(self)




    def exp8(self):

        localctx = MCParser.Exp8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_exp8)
        try:
            self.state = 235
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 229
                self.exp9()
                self.state = 230
                self.match(MCParser.LS)
                self.state = 231
                self.exp9()
                self.state = 232
                self.match(MCParser.RS)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 234
                self.exp9()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp9Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(MCParser.LB, 0)

        def exp(self):
            return self.getTypedRuleContext(MCParser.ExpContext,0)


        def RB(self):
            return self.getToken(MCParser.RB, 0)

        def operands(self):
            return self.getTypedRuleContext(MCParser.OperandsContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_exp9

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp9" ):
                return visitor.visitExp9(self)
            else:
                return visitor.visitChildren(self)




    def exp9(self):

        localctx = MCParser.Exp9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_exp9)
        try:
            self.state = 242
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MCParser.LB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 237
                self.match(MCParser.LB)
                self.state = 238
                self.exp()
                self.state = 239
                self.match(MCParser.RB)
                pass
            elif token in [MCParser.INTLIT, MCParser.REAL, MCParser.BOOLLIT, MCParser.IDEN, MCParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 241
                self.operands(0)
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


    class OperandsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(MCParser.LiteralContext,0)


        def IDEN(self):
            return self.getToken(MCParser.IDEN, 0)

        def call_func(self):
            return self.getTypedRuleContext(MCParser.Call_funcContext,0)


        def operands(self):
            return self.getTypedRuleContext(MCParser.OperandsContext,0)


        def postfix_array(self):
            return self.getTypedRuleContext(MCParser.Postfix_arrayContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_operands

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperands" ):
                return visitor.visitOperands(self)
            else:
                return visitor.visitChildren(self)



    def operands(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MCParser.OperandsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 48
        self.enterRecursionRule(localctx, 48, self.RULE_operands, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 245
                self.literal()
                pass

            elif la_ == 2:
                self.state = 246
                self.match(MCParser.IDEN)
                pass

            elif la_ == 3:
                self.state = 247
                self.call_func()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 254
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MCParser.OperandsContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_operands)
                    self.state = 250
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 251
                    self.postfix_array() 
                self.state = 256
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class LiteralContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(MCParser.INTLIT, 0)

        def REAL(self):
            return self.getToken(MCParser.REAL, 0)

        def BOOLLIT(self):
            return self.getToken(MCParser.BOOLLIT, 0)

        def STRINGLIT(self):
            return self.getToken(MCParser.STRINGLIT, 0)

        def getRuleIndex(self):
            return MCParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = MCParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.INTLIT) | (1 << MCParser.REAL) | (1 << MCParser.BOOLLIT) | (1 << MCParser.STRINGLIT))) != 0)):
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


    class Call_funcContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDEN(self):
            return self.getToken(MCParser.IDEN, 0)

        def LB(self):
            return self.getToken(MCParser.LB, 0)

        def RB(self):
            return self.getToken(MCParser.RB, 0)

        def para_list(self):
            return self.getTypedRuleContext(MCParser.Para_listContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_call_func

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_func" ):
                return visitor.visitCall_func(self)
            else:
                return visitor.visitChildren(self)




    def call_func(self):

        localctx = MCParser.Call_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_call_func)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self.match(MCParser.IDEN)
            self.state = 260
            self.match(MCParser.LB)
            self.state = 262
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.INTLIT) | (1 << MCParser.REAL) | (1 << MCParser.BOOLLIT) | (1 << MCParser.LOGICALNOT) | (1 << MCParser.SUBTR) | (1 << MCParser.LB) | (1 << MCParser.IDEN) | (1 << MCParser.STRINGLIT))) != 0):
                self.state = 261
                self.para_list()


            self.state = 264
            self.match(MCParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Para_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.ExpContext)
            else:
                return self.getTypedRuleContext(MCParser.ExpContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MCParser.COMMA)
            else:
                return self.getToken(MCParser.COMMA, i)

        def getRuleIndex(self):
            return MCParser.RULE_para_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPara_list" ):
                return visitor.visitPara_list(self)
            else:
                return visitor.visitChildren(self)




    def para_list(self):

        localctx = MCParser.Para_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_para_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
            self.exp()
            self.state = 271
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MCParser.COMMA:
                self.state = 267
                self.match(MCParser.COMMA)
                self.state = 268
                self.exp()
                self.state = 273
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def If(self):
            return self.getToken(MCParser.If, 0)

        def LB(self):
            return self.getToken(MCParser.LB, 0)

        def exp(self):
            return self.getTypedRuleContext(MCParser.ExpContext,0)


        def RB(self):
            return self.getToken(MCParser.RB, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.StatementContext)
            else:
                return self.getTypedRuleContext(MCParser.StatementContext,i)


        def Else(self):
            return self.getToken(MCParser.Else, 0)

        def getRuleIndex(self):
            return MCParser.RULE_if_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = MCParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            self.match(MCParser.If)
            self.state = 275
            self.match(MCParser.LB)
            self.state = 276
            self.exp()
            self.state = 277
            self.match(MCParser.RB)
            self.state = 278
            self.statement()
            self.state = 281
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 279
                self.match(MCParser.Else)
                self.state = 280
                self.statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Do_while_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Do(self):
            return self.getToken(MCParser.Do, 0)

        def While(self):
            return self.getToken(MCParser.While, 0)

        def exp(self):
            return self.getTypedRuleContext(MCParser.ExpContext,0)


        def SEMI(self):
            return self.getToken(MCParser.SEMI, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.StatementContext)
            else:
                return self.getTypedRuleContext(MCParser.StatementContext,i)


        def getRuleIndex(self):
            return MCParser.RULE_do_while_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDo_while_statement" ):
                return visitor.visitDo_while_statement(self)
            else:
                return visitor.visitChildren(self)




    def do_while_statement(self):

        localctx = MCParser.Do_while_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_do_while_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 283
            self.match(MCParser.Do)
            self.state = 285 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 284
                self.statement()
                self.state = 287 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.INTLIT) | (1 << MCParser.REAL) | (1 << MCParser.BOOLLIT) | (1 << MCParser.LOGICALNOT) | (1 << MCParser.SUBTR) | (1 << MCParser.If) | (1 << MCParser.Do) | (1 << MCParser.For) | (1 << MCParser.Break) | (1 << MCParser.Continue) | (1 << MCParser.Return) | (1 << MCParser.LB) | (1 << MCParser.LP) | (1 << MCParser.IDEN) | (1 << MCParser.STRINGLIT))) != 0)):
                    break

            self.state = 289
            self.match(MCParser.While)
            self.state = 290
            self.exp()
            self.state = 291
            self.match(MCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def For(self):
            return self.getToken(MCParser.For, 0)

        def LB(self):
            return self.getToken(MCParser.LB, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.ExpContext)
            else:
                return self.getTypedRuleContext(MCParser.ExpContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(MCParser.SEMI)
            else:
                return self.getToken(MCParser.SEMI, i)

        def RB(self):
            return self.getToken(MCParser.RB, 0)

        def statement(self):
            return self.getTypedRuleContext(MCParser.StatementContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_for_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_statement" ):
                return visitor.visitFor_statement(self)
            else:
                return visitor.visitChildren(self)




    def for_statement(self):

        localctx = MCParser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_for_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 293
            self.match(MCParser.For)
            self.state = 294
            self.match(MCParser.LB)
            self.state = 295
            self.exp()
            self.state = 296
            self.match(MCParser.SEMI)
            self.state = 297
            self.exp()
            self.state = 298
            self.match(MCParser.SEMI)
            self.state = 299
            self.exp()
            self.state = 300
            self.match(MCParser.RB)
            self.state = 301
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Break(self):
            return self.getToken(MCParser.Break, 0)

        def SEMI(self):
            return self.getToken(MCParser.SEMI, 0)

        def getRuleIndex(self):
            return MCParser.RULE_break_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_statement" ):
                return visitor.visitBreak_statement(self)
            else:
                return visitor.visitChildren(self)




    def break_statement(self):

        localctx = MCParser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            self.match(MCParser.Break)
            self.state = 304
            self.match(MCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Continue(self):
            return self.getToken(MCParser.Continue, 0)

        def SEMI(self):
            return self.getToken(MCParser.SEMI, 0)

        def getRuleIndex(self):
            return MCParser.RULE_continue_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_statement" ):
                return visitor.visitContinue_statement(self)
            else:
                return visitor.visitChildren(self)




    def continue_statement(self):

        localctx = MCParser.Continue_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
            self.match(MCParser.Continue)
            self.state = 307
            self.match(MCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Return(self):
            return self.getToken(MCParser.Return, 0)

        def exp(self):
            return self.getTypedRuleContext(MCParser.ExpContext,0)


        def SEMI(self):
            return self.getToken(MCParser.SEMI, 0)

        def getRuleIndex(self):
            return MCParser.RULE_return_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_statement" ):
                return visitor.visitReturn_statement(self)
            else:
                return visitor.visitChildren(self)




    def return_statement(self):

        localctx = MCParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_return_statement)
        try:
            self.state = 315
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 309
                self.match(MCParser.Return)
                self.state = 310
                self.exp()
                self.state = 311
                self.match(MCParser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 313
                self.match(MCParser.Return)
                self.state = 314
                self.match(MCParser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(MCParser.ExpContext,0)


        def SEMI(self):
            return self.getToken(MCParser.SEMI, 0)

        def getRuleIndex(self):
            return MCParser.RULE_exp_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp_statement" ):
                return visitor.visitExp_statement(self)
            else:
                return visitor.visitChildren(self)




    def exp_statement(self):

        localctx = MCParser.Exp_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_exp_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 317
            self.exp()
            self.state = 318
            self.match(MCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[14] = self.exp1_sempred
        self._predicates[15] = self.exp2_sempred
        self._predicates[19] = self.exp5_sempred
        self._predicates[20] = self.exp6_sempred
        self._predicates[24] = self.operands_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp1_sempred(self, localctx:Exp1Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def exp2_sempred(self, localctx:Exp2Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def exp5_sempred(self, localctx:Exp5Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def exp6_sempred(self, localctx:Exp6Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def operands_sempred(self, localctx:OperandsContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 1)
         




