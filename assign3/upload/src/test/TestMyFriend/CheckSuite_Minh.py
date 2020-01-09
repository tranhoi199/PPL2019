import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):
    # def test_undeclared_function(self):
    #     """Simple program: int main() {} """
    #     input = """int main() {foo();}"""
    #     expect = "Undeclared Function: foo"
    #     self.assertTrue(TestChecker.test(input,expect,400))

    # def test_diff_numofparam_stmt(self):
    #     """More complex program"""
    #     input = """int main () {
    #         putIntLn();
    #     }"""
    #     expect = "Type Mismatch In Statement: CallExpr(Id(putIntLn),[])"
    #     self.assertTrue(TestChecker.test(input,expect,401))
    
    # def test_diff_numofparam_expr(self):
    #     """More complex program"""
    #     input = """int main () {
    #         putIntLn(getInt(4));
    #     }"""
    #     expect = "Type Mismatch In Expression: CallExpr(Id(getInt),[IntLiteral(4)])" 
    #     self.assertTrue(TestChecker.test(input,expect,402))
    # def test_undeclared_function_use_ast(self):
    #     """Simple program: int main() {} """
    #     # input = Program([FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("foo"),[])]))])
    # 
    #     expect = "Undeclared Function: foo"
    #     self.assertTrue(TestChecker.test(input,expect,403))
    # def test_diff_numofparam_expr_use_ast(self):
    #     """More complex program"""
    #     input = Program([
    #             FuncDecl(Id("main"),[],IntType(),Block([
    #                 CallExpr(Id("putIntLn"),[
    #                     CallExpr(Id("getInt"),[IntLiteral(4)])
    #                     ])]))])
    #     expect = "Type Mismatch In Expression: CallExpr(Id(getInt),[IntLiteral(4)])"
    #     self.assertTrue(TestChecker.test(input,expect,404))
    # def test_diff_numofparam_stmt_use_ast(self):
    #     """More complex program"""
    #     input = Program([
    #             FuncDecl(Id("main"),[],IntType(),Block([
    #                 CallExpr(Id("putIntLn"),[])]))])
    #     expect = "Type Mismatch In Statement: CallExpr(Id(putIntLn),[])"
    #     self.assertTrue(TestChecker.test(input,expect,405))
    
    def test_valid_function_use_ast(self):
        """Simple program: int main() {} """
        input = Program([
            VarDecl("minh",FloatType()),
            FuncDecl(Id("main"),[],VoidType(),Block([]))
            ])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,500))
    def test_redeclared_variable_use_ast(self):
        input = Program([
            VarDecl("a",IntType()),
            VarDecl("a",IntType()),
            FuncDecl(Id("main"),[],VoidType(),Block([]))
            ])
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,501))
    def test_no_entry_point_use_ast(self):
        input = Program([VarDecl("a",IntType()),
        FuncDecl(Id("hello"),[],IntType(),Block([]))])
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,502))
    def test_redeclare_param_use_ast(self):
        input = Program([
            FuncDecl(
                Id("hello"),
                [VarDecl("a",IntType()),VarDecl("a",FloatType())],
                IntType(),
                Block([])),
            FuncDecl(Id("main"),[],VoidType(),Block([]))])
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input,expect,503))

    def test_redeclare_function_use_ast(self):
        input = Program([
            FuncDecl(Id("hello"),
                [VarDecl("a",IntType())],IntType(),Block([])),
            FuncDecl(Id("hello"),[VarDecl("a",IntType())],IntType(),Block([])),
            FuncDecl(Id("main"),[],VoidType(),Block([]))])
        expect = "Redeclared Function: hello"
        self.assertTrue(TestChecker.test(input,expect,504))

    def test_redeclare_in_function_use_ast(self):
        input = Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("minh",IntType()),VarDecl("minh",IntType())]))])
        expect = "Redeclared Variable: minh"
        self.assertTrue(TestChecker.test(input,expect,505))

    def test_redeclare_in_function_use_ast_1(self):
        input = Program([
            FuncDecl(Id("hello"),
            [VarDecl("x",IntType())],
            IntType(),
            Block([VarDecl("x",IntType()),VarDecl("z",IntType())])),
            FuncDecl(Id("main"),
            [],
            VoidType(),
            Block([VarDecl("x",IntType()),VarDecl("y",IntType())]))
            ])
        expect = "Redeclared Variable: x"
        self.assertTrue(TestChecker.test(input,expect,506))

    def test_redeclare_in_function_use_ast_2(self):
        input = Program([
            FuncDecl(Id("main"),
            [],
            VoidType(),
            Block([
                VarDecl("x",IntType()),
                VarDecl("y",IntType()),
                Block([
                    VarDecl("x",IntType()),
                    VarDecl("x",IntType())
                    ])
            ]))
        ])
        expect = "Redeclared Variable: x"
        self.assertTrue(TestChecker.test(input,expect,507))
    def test_redeclare_in_block_multilevel_use_ast(self):
        input = Program([
                FuncDecl(Id("main"),
                [],
                VoidType(),
                Block([
                    VarDecl("a",IntType()),
                    VarDecl("b",IntType()),
                    Block([
                        VarDecl("c",IntType()),
                        VarDecl("d",IntType()),
                        Block([
                            VarDecl("z",IntType()),
                            VarDecl("t",IntType()),
                            Block([
                                VarDecl("x",IntType()),
                                VarDecl("y",IntType()),
                                VarDecl("x",IntType())
                            ])
                        ])
                    ])
                ]))
            ])
        expect = "Redeclared Variable: x"
        self.assertTrue(TestChecker.test(input,expect,508))

    def test_expression_use_ast(self):
        input = Program([
            FuncDecl(Id("main"),
            [],
            VoidType(),
            Block([
                VarDecl("x",IntType()),
                VarDecl("y",IntType()),
                BinaryOp("=",Id("x"),BinaryOp("+",IntLiteral(7),FloatLiteral(12)))]))
            ])
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(x),BinaryOp(+,IntLiteral(7),FloatLiteral(12)))"
        self.assertTrue(TestChecker.test(input,expect,509))

    def test_undeclare_use_ast(self):
        input = Program([
                FuncDecl(Id("main"),
                [],
                VoidType(),
                Block([
                    VarDecl("a",IntType()),
                    VarDecl("b",IntType()),
                    Block([
                        VarDecl("c",IntType()),
                        VarDecl("d",IntType()),
                        Block([
                            VarDecl("z",IntType()),
                            VarDecl("t",IntType()),
                            Block([
                                VarDecl("x",IntType()),
                                VarDecl("y",IntType()),
                                BinaryOp("=",Id("w"),UnaryOp("-",Id("y")))
                            ])
                        ])
                    ])
                ]))
            ])
        expect = "Undeclared Identifier: w"
        self.assertTrue(TestChecker.test(input,expect,510))

    def test_type_mis_match_expr_with_Id_use_ast(self):
        input = Program([
                FuncDecl(Id("main"),
                [],
                VoidType(),
                Block([
                    VarDecl("a",IntType()),
                    VarDecl("b",IntType()),
                    Block([
                        VarDecl("c",IntType()),
                        VarDecl("d",IntType()),
                        Block([
                            VarDecl("z",FloatType()),
                            VarDecl("t",IntType()),
                            BinaryOp("=",Id("b"),BinaryOp("*",Id("z"),Id("t"))),
                            Block([
                                VarDecl("x",IntType()),
                                VarDecl("y",IntType()),
                                BinaryOp("=",Id("a"),UnaryOp("-",Id("y")))
                            ])
                        ])
                    ])
                ]))
            ])
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(b),BinaryOp(*,Id(z),Id(t)))"
        self.assertTrue(TestChecker.test(input,expect,511))

    def test_type_mis_match_expr_many_func_use_ast(self):
        input = Program([
                VarDecl("z",IntType()),
                FuncDecl(Id("main"),
                [],
                VoidType(),
                Block([
                    VarDecl("a",IntType()),
                    VarDecl("b",IntType()),
                    Block([
                        VarDecl("c",IntType()),
                        VarDecl("d",IntType()),
                        BinaryOp("=",Id("b"),BinaryOp("*",Id("z"),Id("z"))),
                        Block([
                            VarDecl("z",IntType()),
                            VarDecl("t",IntType())
                        ])
                    ])
                ])),
                FuncDecl(Id("temp"),
                [VarDecl("w",FloatType())],
                FloatType(),
                Block([
                    VarDecl("a",IntType()),
                    VarDecl("b",IntType()),
                    Block([
                        VarDecl("c",IntType()),
                        VarDecl("d",IntType()),
                        BinaryOp("=",Id("z"),BinaryOp("*",Id("z"),FloatLiteral(3.2))),
                        Block([
                            VarDecl("z",IntType()),
                            VarDecl("t",IntType())
                        ])
                    ])
                ]))
            ])
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(z),BinaryOp(*,Id(z),FloatLiteral(3.2)))"
        self.assertTrue(TestChecker.test(input,expect,512))

    def test_type_mis_match_expr_with_ArrayCell_use_ast(self):
        input = Program([
                FuncDecl(Id("main"),
                [],
                VoidType(),
                Block([
                    VarDecl("a",IntType()),
                    VarDecl("b",FloatType()),
                    VarDecl("arr",ArrayType(IntLiteral(5),IntType())),
                    Block([
                        VarDecl("c",IntType()),
                        VarDecl("d",IntType()),
                        Block([
                            VarDecl("z",IntType()),
                            VarDecl("t",IntType()),
                            BinaryOp("=",BinaryOp("*",Id("z"),Id("t")),ArrayCell(Id("a"),Id("t"))),
                            Block([
                                VarDecl("x",IntType()),
                                VarDecl("y",IntType()),
                                BinaryOp("=",Id("a"),UnaryOp("-",Id("y")))
                            ])
                        ])
                    ])
                ]))
            ])
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),Id(t))"
        self.assertTrue(TestChecker.test(input,expect,513))

    def test_call_expression_use_ast(self):
        input = Program([
                FuncDecl(Id("foo"),
                [VarDecl("arr",ArrayPointerType(IntType()))],
                VoidType(),
                Block([
                    
                ])),
                FuncDecl(Id("main"),
                [],
                VoidType(),
                Block([
                    VarDecl("a",IntType()),
                    VarDecl("b",FloatType()),
                    VarDecl("arr",ArrayType(IntLiteral(5),FloatType())),
                    Block([
                        VarDecl("c",IntType()),
                        VarDecl("d",IntType()),
                        Block([
                            VarDecl("z",IntType()),
                            VarDecl("t",IntType()),
                            CallExpr(Id("foo"),[Id("arr")]),
                            Block([
                                VarDecl("x",IntType()),
                                VarDecl("y",IntType()),
                                BinaryOp("=",Id("a"),UnaryOp("-",Id("y")))
                            ])
                        ])
                    ])
                ]))
            ])
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[Id(arr)])"
        self.assertTrue(TestChecker.test(input,expect,514))

    def test_if_statement_invalid_expr_use_ast(self):
        input = Program([
                FuncDecl(Id("main"),
                [],
                VoidType(),
                Block([
                    VarDecl("a",IntType()),
                    VarDecl("b",FloatType()),
                    VarDecl("arr",ArrayType(IntLiteral(5),IntType())),
                    Block([
                        VarDecl("c",IntType()),
                        VarDecl("d",IntType()),
                        Block([
                            VarDecl("z",IntType()),
                            VarDecl("t",IntType()),
                            If(BinaryOp("=",Id("c"),Id("d")),Block([
                                BinaryOp("=",Id("z"),BinaryOp("+",Id("z"),IntLiteral(1)))
                            ])),
                            Block([
                                VarDecl("x",IntType()),
                                VarDecl("y",IntType()),
                                BinaryOp("=",Id("a"),UnaryOp("-",Id("y")))
                            ])
                        ])
                    ])
                ]))
            ])
        expect = "Type Mismatch In Statement: If(BinaryOp(=,Id(c),Id(d)),Block([BinaryOp(=,Id(z),BinaryOp(+,Id(z),IntLiteral(1)))]))"
        self.assertTrue(TestChecker.test(input,expect,515))

    def test_if_statement_valid_expr_have_else_use_ast(self):
        input = Program([
                FuncDecl(Id("main"),
                [],
                VoidType(),
                Block([
                    VarDecl("a",IntType()),
                    VarDecl("b",FloatType()),
                    VarDecl("arr",ArrayType(IntLiteral(5),IntType())),
                    Block([
                        VarDecl("c",IntType()),
                        VarDecl("d",IntType()),
                        Block([
                            VarDecl("z",IntType()),
                            VarDecl("t",IntType()),
                            If(BinaryOp("==",Id("c"),Id("d")),Block([
                                BinaryOp("=",Id("z"),BinaryOp("+",Id("z"),IntLiteral(1)))
                            ]),BinaryOp("=",ArrayCell(Id("arr"),Id("c")),BinaryOp("+",Id("z"),Id("t")))),
                            Block([
                                VarDecl("x",IntType()),
                                VarDecl("y",IntType()),
                                BinaryOp("=",Id("a"),UnaryOp("-",Id("y"))),
                                Block([
                                    VarDecl("x",IntType()),
                                    VarDecl("y",IntType()),
                                    Block([
                                        VarDecl("x",IntType()),
                                        VarDecl("y",IntType())
                                    ])
                                ])
                            ]),
                            Block([
                                VarDecl("x",IntType()),
                                VarDecl("y",IntType()),
                                BinaryOp("=",Id("a"),UnaryOp("-",Id("y")))
                            ])
                        ]),
                        Block([
                            VarDecl("x",IntType()),
                            VarDecl("y",IntType())
                        ])
                    ])
                ]))
            ])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,516))

    def test_undeclare_identifier_use_ast(self):
        input = Program([
                FuncDecl(Id("main"),
                [],
                VoidType(),
                Block([
                    BinaryOp("=",Id("a"),IntLiteral(5))
                ]))
            ])
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,517))

    def test_break_in_for_use_ast(self):
        input = Program([
                FuncDecl(Id("main"),
                [],
                VoidType(),
                Block([
                    VarDecl("a",IntType()),
                    For(
                        BinaryOp("=",Id("a"),IntLiteral(1)),
                        BinaryOp("<",Id("a"),IntLiteral(10)),
                        BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),
                        Block([
                            Break()
                        ])
                    )
                ]))
            ])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,518))

    def test_break_not_in_for_use_ast(self):
        input = Program([
                FuncDecl(Id("main"),
                [],
                VoidType(),
                Block([
                    VarDecl("a",IntType()),
                    For(
                        BinaryOp("=",Id("a"),IntLiteral(1)),
                        BinaryOp("<",Id("a"),IntLiteral(10)),
                        BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),
                        Block([
                            Break()
                        ])
                    ),
                    Break()
                ]))
            ])
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,519))

    def test_continue_in_for_use_ast(self):
        input = Program([
                FuncDecl(Id("main"),
                [],
                VoidType(),
                Block([
                    VarDecl("a",IntType()),
                    For(
                        BinaryOp("=",Id("a"),IntLiteral(1)),
                        BinaryOp("<",Id("a"),IntLiteral(10)),
                        BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),
                        Block([
                            If(BooleanLiteral(True),Continue())
                        ])
                    ),
                ]))
            ])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,520))

    def test_continue_not_in_for_use_ast(self):
        input = Program([
                FuncDecl(Id("main"),
                [],
                VoidType(),
                Block([
                    VarDecl("a",IntType()),
                    For(
                        BinaryOp("=",Id("a"),IntLiteral(1)),
                        BinaryOp("<",Id("a"),IntLiteral(10)),
                        BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),
                        Block([
                            If(BooleanLiteral(True),Continue())
                        ])
                    ),
                    Continue()
                ]))
            ])
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,521))

    def test_continue_in_for_nested_use_ast(self):
        input = Program([
                FuncDecl(Id("main"),
                [],
                VoidType(),
                Block([
                    VarDecl("a",IntType()),
                    For(
                        BinaryOp("=",Id("a"),IntLiteral(1)),
                        BinaryOp("<",Id("a"),IntLiteral(10)),
                        BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),
                        Block([
                            If(BooleanLiteral(True),Continue()),
                            For(
                                BinaryOp("=",Id("a"),IntLiteral(1)),
                                BinaryOp("<",Id("a"),IntLiteral(10)),
                                BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),
                                Block([
                                    If(BooleanLiteral(True),Continue())
                                ])
                            ),
                            Break()
                        ])
                    ),
                ]))
            ])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,522))

    def test_continue_invalid_in_for_nested_use_ast(self):
        input = Program([
                FuncDecl(Id("main"),
                [],
                VoidType(),
                Block([
                    VarDecl("a",IntType()),
                    For(
                        BinaryOp("=",Id("a"),IntLiteral(1)),
                        BinaryOp("<",Id("a"),IntLiteral(10)),
                        BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),
                        Block([
                            If(BooleanLiteral(True),Continue()),
                            For(
                                BinaryOp("=",Id("a"),IntLiteral(1)),
                                BinaryOp("<",Id("a"),IntLiteral(10)),
                                BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),
                                Block([
                                    If(BooleanLiteral(True),Continue()),
                                    Break()
                                ])
                            ),
                            Break()
                        ])
                    ),
                    Continue()
                ]))
            ])
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,523))

    def test_continue_invalid_in_dowhile_use_ast(self):
        input = Program([
                FuncDecl(Id("main"),
                [],
                VoidType(),
                Block([
                    VarDecl("a",IntType()),
                    Dowhile([
                        BinaryOp("=",Id("a"),IntLiteral(1)),
                        BinaryOp("<",Id("a"),IntLiteral(10)),
                        BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),
                        Block([
                            If(BooleanLiteral(True),Continue()),
                            For(
                                BinaryOp("=",Id("a"),IntLiteral(1)),
                                BinaryOp("<",Id("a"),IntLiteral(10)),
                                BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),
                                Block([
                                    If(BooleanLiteral(True),Continue()),
                                    Break()
                                ])
                            ),
                            Break()
                        ])
                    ],
                    BinaryOp("<",Id("a"),IntLiteral(10))),
                    Continue()
                ]))
            ])
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,524))

    def test_invalid_expression_in_dowhile_use_ast(self):
        input = Program([
                FuncDecl(Id("main"),
                [],
                VoidType(),
                Block([
                    VarDecl("a",IntType()),
                    Dowhile([
                        BinaryOp("=",Id("a"),IntLiteral(1)),
                        BinaryOp("<",Id("a"),IntLiteral(10)),
                        BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),
                        Block([
                            If(BooleanLiteral(True),Continue()),
                            For(
                                BinaryOp("=",Id("a"),IntLiteral(1)),
                                BinaryOp("<",Id("a"),IntLiteral(10)),
                                BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),
                                Block([
                                    If(BooleanLiteral(True),Continue()),
                                    Break(),
                                    Block([Continue()])
                                ])
                            ),
                            Break()
                        ])
                    ],
                    BinaryOp("=",Id("a"),IntLiteral(10))),
                ]))
            ])
        expect = "Type Mismatch In Statement: Dowhile([BinaryOp(=,Id(a),IntLiteral(1)),BinaryOp(<,Id(a),IntLiteral(10)),BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1))),Block([If(BooleanLiteral(true),Continue()),For(BinaryOp(=,Id(a),IntLiteral(1));BinaryOp(<,Id(a),IntLiteral(10));BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)));Block([If(BooleanLiteral(true),Continue()),Break(),Block([Continue()])])),Break()])],BinaryOp(=,Id(a),IntLiteral(10)))"
        self.assertTrue(TestChecker.test(input,expect,525))

    def test_function_void_have_return_use_ast(self):
        input = Program([
                FuncDecl(Id("main"),
                [],
                VoidType(),
                Block([
                    VarDecl("a",IntType()),
                    CallExpr(Id("foo"),[])
                ])),
                FuncDecl(Id("foo"),
                [],
                VoidType(),
                Block([
                    VarDecl("b",IntType()),
                    Return()
                ]))
            ])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,526))

    def test_function_void_return_have_expr_use_ast(self):
        input = Program([
                FuncDecl(Id("main"),
                [],
                VoidType(),
                Block([
                    VarDecl("a",IntType()),
                ])),
                FuncDecl(Id("foo"),
                [],
                VoidType(),
                Block([
                    VarDecl("b",IntType()),
                    Return(Id("b"))
                ]))
            ])
        expect = "Type Mismatch In Statement: Return(Id(b))"
        self.assertTrue(TestChecker.test(input,expect,527))

    def test_function_not_void_return_no_have_expr_use_ast(self):
        input = Program([
                FuncDecl(Id("main"),
                [],
                VoidType(),
                Block([
                    VarDecl("a",IntType()),
                ])),
                FuncDecl(Id("foo"),
                [],
                FloatType(),
                Block([
                    VarDecl("b",IntType()),
                    Return()
                ]))
            ])
        expect = "Type Mismatch In Statement: Return()"
        self.assertTrue(TestChecker.test(input,expect,528))

    def test_function_not_void_return_have_expr_compatible_use_ast(self):
        input = Program([
                FuncDecl(Id("main"),
                [],
                VoidType(),
                Block([
                    VarDecl("a",IntType()),
                    CallExpr(Id("foo"),[])
                ])),
                FuncDecl(Id("foo"),
                [],
                FloatType(),
                Block([
                    VarDecl("b",IntType()),
                    VarDecl("c",FloatType()),
                    Return(Id("b"))
                ]))
            ])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,529))

    def test_function_not_void_return_have_expr_not_compatible_use_ast(self):
        input = Program([
                FuncDecl(Id("main"),
                [],
                VoidType(),
                Block([
                    VarDecl("a",IntType()),
                ])),
                FuncDecl(Id("foo"),
                [],
                IntType(),
                Block([
                    VarDecl("b",IntType()),
                    VarDecl("c",FloatType()),
                    Return(Id("c"))
                ]))
            ])
        expect = "Type Mismatch In Statement: Return(Id(c))"
        self.assertTrue(TestChecker.test(input,expect,530))

    def test_function_not_void_return_have_expr_type_arrpointer_compatible_use_ast(self):
        input = Program([
                FuncDecl(Id("main"),
                [],
                VoidType(),
                Block([
                    VarDecl("a",IntType()),
                    CallExpr(Id("foo"),[])
                ])),
                FuncDecl(Id("foo"),
                [],
                ArrayPointerType(IntType()),
                Block([
                    VarDecl("b",IntType()),
                    VarDecl("c",FloatType()),
                    VarDecl("arr",ArrayType(IntLiteral(5),IntType())),
                    Return(Id("arr"))
                ]))
            ])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,531))

    def test_function_not_void_return_have_expr_type_arrpointer_compatible_use_ast_1(self):
        input = Program([
                FuncDecl(Id("main"),
                [],
                VoidType(),
                Block([
                    VarDecl("a",IntType()),
                    VarDecl("arr",ArrayType(IntLiteral(5),FloatType())),
                    CallExpr(Id("foofoo"),[Id("arr")]),
                    Return()
                ])),
                FuncDecl(Id("foofoo"),
                [VarDecl("temp",ArrayPointerType(FloatType()))],
                ArrayPointerType(FloatType()),
                Block([
                    VarDecl("b",IntType()),
                    Return(Id("temp")),
                    VarDecl("c",FloatType()),
                    VarDecl("arr",ArrayType(IntLiteral(5),IntType())),
                ]))
            ])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,532))

    def test_function_not_void_return_have_expr_type_arrpointer_not_compatible_use_ast(self):
        input = Program([
                FuncDecl(Id("main"),
                [],
                VoidType(),
                Block([
                    VarDecl("a",IntType()),
                    Return()
                ])),
                FuncDecl(Id("foofoo"),
                [VarDecl("temp",ArrayPointerType(IntType()))],
                ArrayPointerType(FloatType()),
                Block([
                    VarDecl("b",IntType()),
                    VarDecl("c",FloatType()),
                    VarDecl("arr",ArrayType(IntLiteral(5),IntType())),
                    Return(Id("temp"))
                ]))
            ])
        expect = "Type Mismatch In Statement: Return(Id(temp))"
        self.assertTrue(TestChecker.test(input,expect,533))

    def test_function_not_return_use_ast(self):
        input = Program([
                FuncDecl(Id("main"),
                [],
                VoidType(),
                Block([
                    VarDecl("a",IntType()),
                    Return()
                ])),
                FuncDecl(Id("foofoo"),
                [VarDecl("temp",ArrayPointerType(FloatType()))],
                ArrayPointerType(FloatType()),
                Block([
                    VarDecl("b",IntType()),
                    VarDecl("c",FloatType()),
                    VarDecl("arr",ArrayType(IntLiteral(5),IntType())),
                ]))
            ])
        expect = "Function foofoo Not Return "
        self.assertTrue(TestChecker.test(input,expect,534))

    def test_function_not_return_with_many_func_use_ast(self):
        input = Program([
                FuncDecl(Id("main"),
                [],
                VoidType(),
                Block([
                    VarDecl("a",IntType()),
                    Return()
                ])),
                FuncDecl(Id("foofoo"),
                [VarDecl("temp",ArrayPointerType(FloatType()))],
                ArrayPointerType(FloatType()),
                Block([
                    VarDecl("b",IntType()),
                    VarDecl("c",FloatType()),
                    VarDecl("arr",ArrayType(IntLiteral(5),IntType())),
                    Return(Id("temp"))
                ])),
                FuncDecl(Id("foopol"),
                [VarDecl("temp",ArrayPointerType(IntType()))],
                FloatType(),
                Block([
                    VarDecl("b",IntType()),
                    VarDecl("c",FloatType()),
                    VarDecl("arr",ArrayType(IntLiteral(5),IntType())),
                    
                ])),
            ])
        expect = "Function foopol Not Return "
        self.assertTrue(TestChecker.test(input,expect,535))

    def test_function_not_return_with_nested_block_use_ast(self):
        input = Program([
                FuncDecl(Id("main"),
                [],
                VoidType(),
                Block([
                    VarDecl("a",IntType()),
                    VarDecl("arr",ArrayType(IntLiteral(10),FloatType())),
                    VarDecl("arrpol",ArrayType(IntLiteral(10),IntType())),
                    CallExpr(Id("foofoo"),[Id("arr")]),
                    CallExpr(Id("foopol"),[Id("arrpol")]),
                    Return()
                ])),
                FuncDecl(Id("foofoo"),
                [VarDecl("temp",ArrayPointerType(FloatType()))],
                VoidType(),
                Block([
                    VarDecl("b",IntType()),
                    VarDecl("c",FloatType()),
                    VarDecl("arr",ArrayType(IntLiteral(5),IntType())),
                    Return()
                ])),
                FuncDecl(Id("foopol"),
                [VarDecl("temp",ArrayPointerType(IntType()))],
                FloatType(),
                Block([
                    VarDecl("b",IntType()),
                    VarDecl("c",FloatType()),
                    VarDecl("arr",ArrayType(IntLiteral(5),IntType())),
                    Block([
                        Block([
                            Return(Id("c"))
                        ]),
                        Block([
                            VarDecl("b",IntType()),
                            VarDecl("c",FloatType()),
                            Return(Id("c"))
                        ]),
                        Block([
                            Return(Id("c"))
                        ]),
                    ])
                ])),
            ])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,536))

    def test_function_not_return_with_if_use_ast(self):
        input = Program([
                FuncDecl(Id("main"),
                [],
                VoidType(),
                Block([
                    VarDecl("a",IntType()),
                    VarDecl("arr",ArrayType(IntLiteral(10),FloatType())),
                    VarDecl("arrpol",ArrayType(IntLiteral(10),IntType())),
                    CallExpr(Id("foofoo"),[Id("arr")]),
                    CallExpr(Id("foopol"),[Id("arrpol")]),
                    Return()
                ])),
                FuncDecl(Id("foofoo"),
                [VarDecl("temp",ArrayPointerType(FloatType()))],
                VoidType(),
                Block([
                    VarDecl("b",IntType()),
                    VarDecl("c",FloatType()),
                    VarDecl("arr",ArrayType(IntLiteral(5),IntType())),
                    Return()
                ])),
                FuncDecl(Id("foopol"),
                [VarDecl("temp",ArrayPointerType(IntType()))],
                FloatType(),
                Block([
                    VarDecl("b",IntType()),
                    VarDecl("c",FloatType()),
                    VarDecl("arr",ArrayType(IntLiteral(5),IntType())),
                    Block([
                        VarDecl("check",BoolType()),
                        If(Id("check"),Block([
                            BinaryOp("=",Id("c"),Id("b")),
                            Return(Id("c"))
                        ]),Return(Id("c"))),
                        # Return(Id("c"))
                    ])
                ])),
            ])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,537))

    def test_function_recursive_use_ast(self):
        input = Program([
                FuncDecl(Id("main"),
                [],
                VoidType(),
                Block([
                    VarDecl("a",IntType()),
                    VarDecl("arr",ArrayType(IntLiteral(10),FloatType())),
                    VarDecl("arrpol",ArrayType(IntLiteral(10),IntType())),
                    CallExpr(Id("foofoo"),[Id("arr")]),
                    CallExpr(Id("foopol"),[Id("arrpol")]),
                    Return()
                ])),
                FuncDecl(Id("foofoo"),
                [VarDecl("temp",ArrayPointerType(FloatType()))],
                VoidType(),
                Block([
                    VarDecl("b",IntType()),
                    VarDecl("c",FloatType()),
                    VarDecl("arr",ArrayType(IntLiteral(5),IntType())),
                    Return()
                ])),
                FuncDecl(Id("foopol"),
                [VarDecl("temp",ArrayPointerType(IntType()))],
                FloatType(),
                Block([
                    VarDecl("b",IntType()),
                    VarDecl("c",FloatType()),
                    VarDecl("arr",ArrayType(IntLiteral(5),IntType())),
                    CallExpr(Id("foopol"),[Id("arr")]),
                    Block([
                        VarDecl("check",BoolType()),
                        If(Id("check"),Block([
                            BinaryOp("=",Id("c"),Id("b")),
                            Return(Id("c"))
                        ]),Return(Id("c"))),
                        # Return(Id("c"))
                    ])
                ])),
            ])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,538))

    def test_func_not_return_in_for_use_ast(self):
        input = Program([
                FuncDecl(Id("main"),
                [],
                VoidType(),
                Block([
                    VarDecl("a",IntType()),
                    Return()
                ])),
                FuncDecl(Id("foofoo"),
                [VarDecl("temp",ArrayPointerType(FloatType()))],
                IntType(),
                Block([
                    VarDecl("a",IntType()),
                    VarDecl("c",FloatType()),
                    VarDecl("arr",ArrayType(IntLiteral(5),IntType())),
                    For(
                        BinaryOp("=",Id("a"),IntLiteral(1)),
                        BinaryOp("<",Id("a"),IntLiteral(10)),
                        BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),
                        Block([
                            If(BooleanLiteral(True),Return(Id("a"))),
                            Break(),
                            Block([Continue()]),
                            Return(Id("a"))
                        ])
                    ),
                ])),
            ])
        expect = "Function foofoo Not Return "
        self.assertTrue(TestChecker.test(input,expect,539))

    def test_func_name_same_variable_use_ast(self):
        input = Program([
                FuncDecl(Id("main"),
                [],
                VoidType(),
                Block([
                    VarDecl("a",IntType()),
                    CallExpr(Id("test"),[Id("a")]),
                    Return()
                ])),
                FuncDecl(Id("ab"),
                [],
                IntType(),
                Block([
                    Return(IntLiteral(1))
                ])),
                FuncDecl(Id("test"),
                [VarDecl("abc",IntType())],
                IntType(),
                Block([
                    CallExpr(Id("ab"),[]),
                    BinaryOp("=",Id("abc"),IntLiteral(10)),
                ])),
            ])
        expect = "Function test Not Return "
        self.assertTrue(TestChecker.test(input,expect,540))

    def test_func_name_same_variable_use_ast_1(self):
        input = Program([
                FuncDecl(Id("main"),
                [],
                VoidType(),
                Block([
                    VarDecl("a",IntType()),
                    CallExpr(Id("test"),[Id("a")]),
                    Return()
                ])),
                FuncDecl(Id("ab"),
                [],
                ArrayPointerType(IntType()),
                Block([
                    VarDecl("a",ArrayType(IntLiteral(10),IntType())),
                    Return(Id("a")),
                    VarDecl("b",FloatType()),
                    Block([
                        BinaryOp("=",Id("b"),IntLiteral(10))
                    ]),
                ])),
                FuncDecl(Id("test"),
                [VarDecl("abc",IntType())],
                IntType(),
                Block([
                    BinaryOp("=",Id("abc"),IntLiteral(10)),
                    CallExpr(Id("ab"),[]),
                    CallExpr(Id("test"),[Id("abc")]),
                    Block([
                        If(BooleanLiteral(True),Return(Id("abc")),Return(Id("abc"))),
                        If(BooleanLiteral(True),Return(Id("abc"))),
                        Return(Id("abc"))
                    ])
                ])),
            ])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,541))

    def test_unreachable_func_use_ast(self):
        input = Program([
                FuncDecl(Id("main"),
                [],
                VoidType(),
                Block([
                    VarDecl("a",IntType()),
                    Return()
                ])),
                FuncDecl(Id("test"),
                [VarDecl("abc",IntType())],
                IntType(),
                Block([
                    Block([
                        If(BooleanLiteral(True),Return(Id("abc")),Return(Id("abc"))),
                        If(BooleanLiteral(True),Return(Id("abc")))
                    ]),
                    Return(Id("abc"))
                ])),
            ])
        expect = "Unreachable Function: test"
        self.assertTrue(TestChecker.test(input,expect,542))

    def test_not_left_value_use_ast(self):
        input = Program([
                FuncDecl(Id("main"),
                [],
                VoidType(),
                Block([
                    VarDecl("a",IntType()),
                    VarDecl("arr",ArrayType(IntLiteral(10),IntType())),
                    BinaryOp("=",BinaryOp("+",Id("a"),IntLiteral(3)),Id("a")),
                    # BinaryOp("=",Id("arr"),BinaryOp("+",Id("a"),IntLiteral(3))),
                    Return()
                ])),
            ])
        expect = "Not Left Value: BinaryOp(=,BinaryOp(+,Id(a),IntLiteral(3)),Id(a))"
        self.assertTrue(TestChecker.test(input,expect,543))

    def test_not_left_value_valid_with_many_assignment_use_ast(self):
        input = Program([
                FuncDecl(Id("main"),
                [],
                VoidType(),
                Block([
                    VarDecl("a",IntType()),
                    VarDecl("b",IntType()),
                    VarDecl("c",IntType()),
                    VarDecl("arr",ArrayType(IntLiteral(10),IntType())),
                    BinaryOp("=",Id("a"),BinaryOp("=",Id("b"),BinaryOp("=",Id("c"),IntLiteral(100)))),
                    Return()
                ])),
            ])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,544))

    def test_not_left_value_valid_with_callexpr_use_ast(self):
        input = Program([
                FuncDecl(Id("main"),
                [],
                VoidType(),
                Block([
                    VarDecl("a",IntType()),
                    VarDecl("b",IntType()),
                    VarDecl("c",IntType()),
                    VarDecl("arr",ArrayType(IntLiteral(10),IntType())),
                    BinaryOp("=",Id("a"),CallExpr(Id("foo"),[])),
                    Return()
                ])),
                FuncDecl(Id("foo"),
                [],
                IntType(),
                Block([
                    Return(IntLiteral(10))
                ])
                )
            ])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,545))

    def test_not_left_value_invalid_with_callexpr_use_ast(self):
        input = Program([
                FuncDecl(Id("main"),
                [],
                VoidType(),
                Block([
                    VarDecl("a",IntType()),
                    VarDecl("b",IntType()),
                    VarDecl("c",IntType()),
                    VarDecl("arr",ArrayType(IntLiteral(10),IntType())),
                    BinaryOp("=",CallExpr(Id("foo"),[]),Id("a")),
                    Return()
                ])),
                FuncDecl(Id("foo"),
                [],
                IntType(),
                Block([
                    Return(IntLiteral(10))
                ])
                )
            ])
        expect = "Not Left Value: BinaryOp(=,CallExpr(Id(foo),[]),Id(a))"
        self.assertTrue(TestChecker.test(input,expect,546))

    def test_not_left_value_valid_with_arraycell_use_ast(self):
        input = Program([
                FuncDecl(Id("main"),
                [],
                VoidType(),
                Block([
                    VarDecl("a",IntType()),
                    VarDecl("b",IntType()),
                    VarDecl("c",IntType()),
                    VarDecl("arr",ArrayType(IntLiteral(10),IntType())),
                    BinaryOp("=",ArrayCell(Id("arr"),Id("b")),CallExpr(Id("foo"),[])),
                    Return()
                ])),
                FuncDecl(Id("foo"),
                [],
                IntType(),
                Block([
                    Return(IntLiteral(10))
                ])
                )
            ])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,547))

    def test_not_left_value_invalid_with_arraycell_use_ast(self):
        input = Program([
                FuncDecl(Id("main"),
                [],
                VoidType(),
                Block([
                    VarDecl("a",IntType()),
                    VarDecl("b",IntType()),
                    VarDecl("c",IntType()),
                    VarDecl("arr",ArrayType(IntLiteral(10),IntType())),
                    BinaryOp("=",BinaryOp("+",ArrayCell(Id("arr"),Id("b")),IntLiteral(1)),CallExpr(Id("foo"),[])),
                    Return()
                ])),
                FuncDecl(Id("foo"),
                [],
                IntType(),
                Block([
                    Return(IntLiteral(10))
                ])
                )
            ])
        expect = "Not Left Value: BinaryOp(=,BinaryOp(+,ArrayCell(Id(arr),Id(b)),IntLiteral(1)),CallExpr(Id(foo),[]))"
        self.assertTrue(TestChecker.test(input,expect,548))

    def test_expression_with_unary_use_ast(self):
        input = Program([
                FuncDecl(Id("main"),
                [],
                VoidType(),
                Block([
                    VarDecl("a",StringType()),
                    VarDecl("b",StringType()),
                    BinaryOp("=",Id("b"),UnaryOp("-",Id("a"))),
                    Return()
                ])),
            ])
        expect = "Type Mismatch In Expression: UnaryOp(-,Id(a))"
        self.assertTrue(TestChecker.test(input,expect,549))

    def test_callexrp_with_void_use_ast(self):
        input = Program([
                FuncDecl(Id("main"),
                [],
                VoidType(),
                Block([
                    VarDecl("m",ArrayType(IntLiteral(5),IntType())),
                    CallExpr(Id("foo"),[Id("m"),IntLiteral(2)]),
                    Return()
                ])),
                FuncDecl(Id("foo"),
                [VarDecl("a",ArrayPointerType(IntType())),VarDecl("b",IntType())],
                VoidType(),
                Block([]))
            ])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,550))

    def test_function_same_name_with_variable_use_ast(self):
        input = Program([
                FuncDecl(Id("main"),
                [],
                VoidType(),
                Block([
                    VarDecl("ab",IntType()),
                    CallExpr(Id("ab"),[]),
                    Return()
                ])),
                FuncDecl(Id("ab"),
                [],
                IntType(),
                Block([
                    Return(IntLiteral(1))
                ]))
            ])
        expect = "Undeclared Function: ab"
        self.assertTrue(TestChecker.test(input,expect,551))

    def test_function_same_name_with_variable_complicate_use_ast(self):
        input = Program([
                VarDecl("i",IntType()),
                FuncDecl(Id("main"),
                [],
                VoidType(),
                Block([
                    VarDecl("main",IntType()),
                    BinaryOp("=",Id("main"),CallExpr(Id("f"),[])),
                    CallExpr(Id("putIntLn"),[Id("main")]),
                    Block([
                        VarDecl("i",IntType()),
                        VarDecl("main",IntType()),
                        VarDecl("f",IntType()),
                        BinaryOp("=",Id("main"),BinaryOp("=",Id("f"),BinaryOp("=",Id("i"),IntLiteral(100)))),
                        CallExpr(Id("putIntLn"),[Id("i")]),
                        CallExpr(Id("putIntLn"),[Id("main")]),
                        CallExpr(Id("putIntLn"),[Id("f")]),
                    ]),
                    CallExpr(Id("putIntLn"),[Id("main")]),
                    Return()
                ])),
                FuncDecl(Id("f"),
                [],
                IntType(),
                Block([
                    Return(IntLiteral(200))
                ]))
            ])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,552))

    def test_some_expression_complicated_with_variable_hide_func_use_ast(self):
        input = Program([
                VarDecl("i",IntType()),
                FuncDecl(Id("main"),
                [],
                VoidType(),
                Block([
                    VarDecl("main",IntType()),
                    BinaryOp("=",Id("main"),CallExpr(Id("f"),[])),
                    CallExpr(Id("putIntLn"),[Id("main")]),
                    Block([
                        VarDecl("i",IntType()),
                        VarDecl("main",IntType()),
                        VarDecl("f",IntType()),
                        BinaryOp("=",Id("main"),BinaryOp("+",CallExpr(Id("f"),[]),BinaryOp("*",Id("i"),CallExpr(Id("f"),[])))),
                    ]),
                    CallExpr(Id("putIntLn"),[Id("main")]),
                    Return()
                ])),
                FuncDecl(Id("f"),
                [],
                IntType(),
                Block([
                    Return(IntLiteral(200))
                ]))
            ])
        expect = "Undeclared Function: f"
        self.assertTrue(TestChecker.test(input,expect,553))

    #test complex program with for and return
    def test_complex_program_with_for_and_return_invalid_use_ast(self):
        input = Program([
                VarDecl("i",IntType()),
                FuncDecl(Id("main"),
                [],
                VoidType(),
                Block([
                    CallExpr(Id("f"),[])
                ])),
                FuncDecl(Id("f"),
                [],
                IntType(),
                Block([
                    VarDecl("i",IntType()),
                    For(
                        BinaryOp("=",Id("i"),IntLiteral(0)),
                        BinaryOp("<",Id("i"),IntLiteral(10)),
                        BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),
                        Block([
                            If(BooleanLiteral(True),Block([Return(IntLiteral(0))]),Block([Return(IntLiteral(1))])),
                            If(BooleanLiteral(True),Block([Return(IntLiteral(2))]))
                        ])
                    )
                ]))
            ])
        expect = "Function f Not Return "
        self.assertTrue(TestChecker.test(input,expect,554))

    def test_complex_program_with_for_and_return_valid_use_ast(self):
        input = Program([
                VarDecl("i",IntType()),
                FuncDecl(Id("main"),
                [],
                VoidType(),
                Block([
                    CallExpr(Id("f"),[])
                ])),
                FuncDecl(Id("f"),
                [],
                IntType(),
                Block([
                    VarDecl("i",IntType()),
                    For(
                        BinaryOp("=",Id("i"),IntLiteral(0)),
                        BinaryOp("<",Id("i"),IntLiteral(10)),
                        BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),
                        Block([
                            If(BooleanLiteral(True),Block([Return(IntLiteral(0))]),Block([Return(IntLiteral(1))])),
                            If(BooleanLiteral(True),Block([Return(IntLiteral(2))]))
                        ]),
                    ),
                    Return(Id("i"))
                ]))
            ])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,555))

    #test complex program with dowhile and return
    def test_complex_program_with_dowhile_and_return_invalid_use_ast(self):
        input = Program([
                VarDecl("i",IntType()),
                FuncDecl(Id("main"),
                [],
                VoidType(),
                Block([
                    CallExpr(Id("f"),[])
                ])),
                FuncDecl(Id("f"),
                [],
                IntType(),
                Block([
                    VarDecl("i",IntType()),
                    Dowhile([
                        BinaryOp("=",Id("i"),IntLiteral(0)),
                        BinaryOp("<",Id("i"),IntLiteral(10)),
                        BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),
                        Block([
                            If(BooleanLiteral(True),Block([Return(IntLiteral(2))]))
                        ])
                    ],UnaryOp("!",BooleanLiteral(False)))
                ]))
            ])
        expect = "Function f Not Return "
        self.assertTrue(TestChecker.test(input,expect,556))

    def test_complex_program_with_dowhile_and_return_valid_use_ast(self):
        input = Program([
                VarDecl("i",IntType()),
                FuncDecl(Id("main"),
                [],
                VoidType(),
                Block([
                    CallExpr(Id("f"),[])
                ])),
                FuncDecl(Id("f"),
                [],
                IntType(),
                Block([
                    VarDecl("i",IntType()),
                    Dowhile([
                        BinaryOp("=",Id("i"),IntLiteral(0)),
                        BinaryOp("<",Id("i"),IntLiteral(10)),
                        BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),
                        Block([
                            If(BooleanLiteral(True),Block([Return(IntLiteral(0))]),Block([Return(IntLiteral(1))])),
                            If(BooleanLiteral(True),Block([Return(IntLiteral(2))]))
                        ])
                    ],UnaryOp("!",BooleanLiteral(False)))
                ]))
            ])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,557))

    def test_redeclare_name_func_with_name_builtin_use_ast(self):
        input = Program([
                VarDecl("i",IntType()),
                FuncDecl(Id("main"),
                [],
                VoidType(),
                Block([
                    CallExpr(Id("f"),[])
                ])),
                FuncDecl(Id("getInt"),
                [],
                IntType(),
                Block([
                    VarDecl("i",IntType()),
                        BinaryOp("=",Id("i"),IntLiteral(0)),
                        BinaryOp("<",Id("i"),IntLiteral(10)),
                        BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),
                        Block([
                            If(BooleanLiteral(True),Block([Return(IntLiteral(0))]),Block([Return(IntLiteral(1))])),
                            If(BooleanLiteral(True),Block([Return(IntLiteral(2))]))
                        ])
                ]))
            ])
        expect = "Redeclared Function: getInt"
        self.assertTrue(TestChecker.test(input,expect,558))

    def test_func_call_with_many_func_use_ast(self):
        input = Program([
                VarDecl("i",IntType()),
                FuncDecl(Id("main"),
                [],
                IntType(),
                Block([
                    CallExpr(Id("foo"),[]),
                    Return(IntLiteral(1))
                ])),
                FuncDecl(Id("foo"),
                [],
                IntType(),
                Block([
                    CallExpr(Id("test"),[]),
                    Return(IntLiteral(1))
                ])),
                FuncDecl(Id("test"),
                [],
                IntType(),
                Block([
                    Return(IntLiteral(1))
                ])),
            ])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,559))

    def test_some_expr_complicated_use_ast(self):
        input = """int main(){
                int a,b;
                int arr[10];
                arr[a]=a+b/(4+5)*7-a*b;
                b=gt(10);
                return 0;
            }
            int gt(int n){
                if(n==0 || n==1)
                    return 1;
                return gt(n-1)*n;
            }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,560))

    def test_redeclaration_func_with_complicated_use_ast(self):
        input = """void main(){
                int a,b;
                float arr[10];
                arr[a]=foo(arr)[b];
                return;
            }
            float[] foo(float n[]){
                float arr[100];
                int a;
                if(a==0 || a==1)
                    return arr;
                return n;
            }
            void getFloat(){
                return;
            }
        """
        expect = "Redeclared Function: getFloat"
        self.assertTrue(TestChecker.test(input,expect,561))

    def test_variable_hide_func_with_many_block_nested_use_ast(self):
        input = """void main(){
                int a,b;
                float arr[10];
                arr[a]=foo(arr)[b];
                return;
            }
            float[] foo(float n[]){
                float arr[100];
                int a;
                for(a=0;a<100;a=a+1){
                    {
                        int c,d;
                        int gt;
                    }
                }
                if(true){
                    gt();
                    float gt;
                    gt();
                    gt=9.786;
                }
                return arr;
            }
            float gt(){
                return 2;
            }
        """
        expect = "Undeclared Function: gt"
        self.assertTrue(TestChecker.test(input,expect,562))

    def test_variable_hide_func_with_many_block_nested_use_ast_1(self):
        input = """void main(){
                int a,b;
                float arr[10];
                arr[a]=foo(arr)[b];
                gt();
                return;
            }
            float[] foo(float n[]){
                float arr[100];
                int a;
                for(a=0;a<100;a=a+1){
                    {
                        int c,d;
                        int gt;
                        if(true){
                            foo(n);
                            float gt;
                            c=gt*d;  // error here
                            gt=9.786;
                        }
                        {
                            c=gt*d;
                        }
                    }
                }
                gt();
                return arr;
            }
            float gt(){
                return 2;
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(c),BinaryOp(*,Id(gt),Id(d)))"
        self.assertTrue(TestChecker.test(input,expect,563))

    def test_redeclare_param_with_many_block_nested(self):
        input = """void main(){
                int a,b;
                float arr[10];
                gt(a,9.5);
                return;
            }
            float gt(int a, float a){    //error here
                {
                    {
                        {
                            float a;
                        }
                    }
                }
                return 2;
            }
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input,expect,564))

    def test_undeclare_identifier_with_many_block_nested(self):
        input = """void main(){
                float a,b;
                float arr[10];
                b=gt(4,9.5)+a/b-a*b;
                {
                    int f;
                    float g;
                    {
                        {
                            int g;
                            g=f;  
                        }
                    }
                    {
                        if(true){
                            j=g*f;      //error here
                        }
                    }
                }
                return;
            }
            float gt(int a, float b){    
                {
                    {
                        {
                            float a;
                            a=a*b/2+7;
                        }
                    }
                }
                return 2;
            }
        """
        expect = "Undeclared Identifier: j"
        self.assertTrue(TestChecker.test(input,expect,565))

    def test_undeclare_func_with_many_block_because_is_hiden_nested(self):
        input = """
            void a(){
                return;
            }
            int main(int a){
                {
                    int a;
                    {
                        int a;
                        {
                            int a;
                            a();    //error here
                        }
                    }
                }
                return 1;
            }
        """
        expect = "Undeclared Function: a"
        self.assertTrue(TestChecker.test(input,expect,566))

    def test_undeclare_func_with_many_block_real_nested(self):
        input = """
            void a(){
                return;
            }
            int main(){
                {
                    b();
                    c();
                    d();
                    a();
                    getInt();
                    getFloat();
                    putBool(true);
                    f();    //error here
                }
                return 1;
            }
            int b(){
                return 1;
            }
            string c(){
                return "hello";
            }
            boolean d(){
                return false;
            }
        """
        expect = "Undeclared Function: f"
        self.assertTrue(TestChecker.test(input,expect,567))

    #type mismatch in statement with many block
    def test_type_mismatch_in_if_statement_valid_with_many_block(self):
        input = """
            int main(int a){
                {
                   {
                       boolean a,b,c;                    
                       if(a && b && c){
                           a=false;
                           c=false;
                       }
                       else{
                           b=false;
                       }
                   }
                }
                return 1;
            }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,568))

    def test_type_mismatch_in_if_statement_invalid_with_many_block(self):
        input = """
            int main(int a){
                {
                   {
                       int a,b,c;                    
                       if(a = b+c){ //error here: wrong condition
                           a=10;
                           c=10;
                           a=b+c;
                       }
                       else{
                           b=10;
                       }
                   }
                }
                return 1;
            }
        """
        expect = "Type Mismatch In Statement: If(BinaryOp(=,Id(a),BinaryOp(+,Id(b),Id(c))),Block([BinaryOp(=,Id(a),IntLiteral(10)),BinaryOp(=,Id(c),IntLiteral(10)),BinaryOp(=,Id(a),BinaryOp(+,Id(b),Id(c)))]),Block([BinaryOp(=,Id(b),IntLiteral(10))]))"
        self.assertTrue(TestChecker.test(input,expect,569))

    def test_type_mismatch_in_if_statement_nested_valid_with_many_block(self):
        input = """
            int main(int a){
                {
                   {
                       int a,b,c;                    
                       if(a >= b+c){ 
                           if(a<b){
                               if(a==c){
                                   float c;
                                   c=9.5;
                               }
                           }
                           a=b+c;
                       }
                       else{
                           if(c==10){
                               float c;
                               c=b+a*9.5;
                           }
                           b=10;
                       }
                   }
                }
                return 1;
            }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,570))

    def test_type_mismatch_in_if_statement_nested_invalid_with_many_block(self):
        input = """
            int main(int a){
                {
                   {
                       int a,b,c;                    
                       if(a >= b+c){ 
                           if(a<b){
                               if(a==c){
                                   float c;
                                   c=9.5;
                               }
                           }
                           a=b+c;
                       }
                       else{
                           if(c){   //Error here: wrong condition
                               float c;
                               c=b+a*9.5;
                           }
                           b=10;
                       }
                   }
                }
                return 1;
            }
        """
        expect = "Type Mismatch In Statement: If(Id(c),Block([VarDecl(c,FloatType),BinaryOp(=,Id(c),BinaryOp(+,Id(b),BinaryOp(*,Id(a),FloatLiteral(9.5))))]))"
        self.assertTrue(TestChecker.test(input,expect,571))

    #test for statement
    def test_type_mismatch_in_for_statement_valid_with_many_block(self):
        input = """
            int main(int a){
                for(a=0;a<10;a=a+1){
                    int i;
                    for(i=0;i!=10;i=i-1){
                        putString("I love PPL and I need to pass it");
                    }
                }
                return 1;
            }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,572))

    def test_type_mismatch_in_for_statement_invalid_expr1_with_many_block(self):
        input = """
            int main(int a){
                for(a==0;a<10;a=a+1){   //error here: invalid expression 1
                    int i;
                    for(i=0;i!=10;i=i-1){
                        putString("I love PPL and I need to pass it");
                    }
                }
                return 1;
            }
        """
        expect = "Type Mismatch In Statement: For(BinaryOp(==,Id(a),IntLiteral(0));BinaryOp(<,Id(a),IntLiteral(10));BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)));Block([VarDecl(i,IntType),For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(!=,Id(i),IntLiteral(10));BinaryOp(=,Id(i),BinaryOp(-,Id(i),IntLiteral(1)));Block([CallExpr(Id(putString),[StringLiteral(I love PPL and I need to pass it)])]))]))"
        self.assertTrue(TestChecker.test(input,expect,573))

    def test_type_mismatch_in_for_statement_invalid_expr2_with_many_block(self):
        input = """
            int main(int a){
                for(a=0;a=a+10;a=a+1){   //error here: invalid expression 2
                    int i;
                    for(i=0;i!=10;i=i-1){
                        putString("I love PPL and I need to pass it");
                    }
                }
                return 1;
            }
        """
        expect = "Type Mismatch In Statement: For(BinaryOp(=,Id(a),IntLiteral(0));BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(10)));BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)));Block([VarDecl(i,IntType),For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(!=,Id(i),IntLiteral(10));BinaryOp(=,Id(i),BinaryOp(-,Id(i),IntLiteral(1)));Block([CallExpr(Id(putString),[StringLiteral(I love PPL and I need to pass it)])]))]))"
        self.assertTrue(TestChecker.test(input,expect,574))

    def test_type_mismatch_in_for_statement_invalid_expr3_with_many_block(self):
        input = """
            int main(int a){
                for(a=0;a<10;a=a+1){  
                    int i;
                    for(i=0;i!=10;i<=i-1){    //error here: invalid expression 3
                        putString("I love PPL and I need to pass it");
                    }
                }
                return 1;
            }
        """
        expect = "Type Mismatch In Statement: For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(!=,Id(i),IntLiteral(10));BinaryOp(<=,Id(i),BinaryOp(-,Id(i),IntLiteral(1)));Block([CallExpr(Id(putString),[StringLiteral(I love PPL and I need to pass it)])]))"
        self.assertTrue(TestChecker.test(input,expect,575))

    #test dowhile statement
    def test_type_mismatch_in_dowhile_statement_valid_with_many_block(self):
        input = """
            int main(int a){
                do{
                    int b,c,d;
                    float arr[10];
                    if(b>c)
                        break;
                    else{
                        do
                        b=b+c;
                        {
                            d=d*b*c;
                        }
                        while(d<=c);
                    }
                }while(true);
                return 1;
            }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,576))

    def test_type_mismatch_in_dowhile_statement_invalid_with_many_block(self):
        input = """
            int main(int a){
                do{
                    int b,c,d;
                    float arr[10];
                    if(b>c)
                        break;
                    else{
                        do
                        b=b+c;
                        {
                            d=d*b*c;
                        }
                        while(d=c); //Error here: wrong condition
                    }
                }while(a==0);    
                return 1;
            }
        """
        expect = "Type Mismatch In Statement: Dowhile([BinaryOp(=,Id(b),BinaryOp(+,Id(b),Id(c))),Block([BinaryOp(=,Id(d),BinaryOp(*,BinaryOp(*,Id(d),Id(b)),Id(c)))])],BinaryOp(=,Id(d),Id(c)))"
        self.assertTrue(TestChecker.test(input,expect,577))

    #test return with return type and function type
    def test_type_mismatch_in_return_statement_invalid_between_return_type_and_func_type_with_many_block(self):
        input = """
            int main(int a){
                foo();
                return 1;
            }
            float foo(){
                {
                    {
                        {
                            {
                                return false;      //error here: not match type
                            }
                        }
                    }
                }
            }
        """
        expect = "Type Mismatch In Statement: Return(BooleanLiteral(false))"
        self.assertTrue(TestChecker.test(input,expect,578))

    def test_type_mismatch_in_return_statement_invalid_between_return_type_and_func_void_type_with_many_block(self):
        input = """
            int main(int a){
                return 1;
            }
            void foo(){
                {
                    {
                        {
                            {
                                return false;      //error here: void but return
                            }
                        }
                    }
                }
            }
        """
        expect = "Type Mismatch In Statement: Return(BooleanLiteral(false))"
        self.assertTrue(TestChecker.test(input,expect,579))

    #test expression
    def test_type_mismatch_in_expression_invalid_between_func_and_variable_with_many_block(self):
        input = """
            void main(){
                foo[3];     //error here
            }
            int foo(){
                return 3;
            }
        """
        expect = "Undeclared Identifier: foo"
        self.assertTrue(TestChecker.test(input,expect,580))

    def test_type_mismatch_in_expression_invalid_array_type_with_many_block(self):
        input = """
            void main(){
                float arr[10];
                {
                    {
                        int arr[10];
                        arr[true]=2;    //error here
                    }
                }
                foo();
            }
            int foo(){
                return 3;
            }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(arr),BooleanLiteral(true))"
        self.assertTrue(TestChecker.test(input,expect,581))

    def test_type_mismatch_in_expression_invalid_array_type_with_many_block_1(self):
        input = """
            void main(){
                string arr[10];
                {
                    {
                        int arr[10];
                        arr[2]=false;    //error here
                    }
                }
                foo();
                putString("I want to pass PPL");
            }
            int foo(){
                return 3;
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,ArrayCell(Id(arr),IntLiteral(2)),BooleanLiteral(false))"
        self.assertTrue(TestChecker.test(input,expect,582))
    
    #test binary expression
    def test_type_mismatch_in_expression_binary_valid_with_many_block(self):
        input = """
            void main(){
                string arr[10];
                {
                    {
                        int a,b;
                        float c,d;
                        float arr[10];
                        c=a+b*c/d-2*5;
                        arr[8]=c+1;
                    }
                }
                foo();
                putString("I want to pass PPL");
            }
            int foo(){
                return 3;
            }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,583))

    def test_type_mismatch_in_expression_binary_invalid_with_many_block(self):
        input = """
            void main(){
                string arr[10];
                {
                    {
                        int a,b;
                        boolean c,d;
                        float arr[10];
                        c=a+b*c/d-2*5;      //error here  
                        arr[8]=a+1;
                    }
                }
                foo();
                putString("I want to pass PPL");
            }
            int foo(){
                return 3;
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(*,Id(b),Id(c))"
        self.assertTrue(TestChecker.test(input,expect,584))

    #test unary expression
    def test_type_mismatch_in_expression_unary_valid_with_many_block(self):
        input = """
            void main(){
                boolean arr[10];
                {
                    {
                        int a,b;
                        float c,d;
                        float arr[10];
                        c=-a+b*c/d-2*5;   
                        arr[8]=a+1;
                        arr[7]=-a;
                        boolean hello;
                        hello=!hello;
                    }
                    if(arr[0]==true){
                        return;
                    }
                }
                foo();
                putString("I want to pass PPL");
            }
            int foo(){
                return 3;
            }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,585))

    def test_type_mismatch_in_expression_unary_invalid_with_many_block(self):
        input = """
            void main(){
                boolean arr[10];
                {
                    {
                        int a,b;
                        float c,d;
                        float arr[10];
                        c=-a+b*c/d-2*5;   
                        arr[8]=a+1;
                        arr[7]=-a;
                        boolean hello;
                        hello=!d;       //error here
                    }
                    if(arr[0]==true){
                        return;
                    }
                }
                foo();
                putString("I want to pass PPL");
            }
            int foo(){
                return 3;
            }
        """
        expect = "Type Mismatch In Expression: UnaryOp(!,Id(d))"
        self.assertTrue(TestChecker.test(input,expect,586))

    #test assignment expression
    def test_type_mismatch_in_expression_assignment_expr_invalid_with_many_block(self):
        input = """
            void main(){
                boolean arr[10];
                {
                    {
                        if(arr[9]==false){
                            int arr[10];
                            arr[9]=20;  
                            arr[8]=false;       //error here
                        }
                        else{
                            return;
                        }
                    }
                    if(arr[0]==true){
                        return;
                    }
                }
                foo();
                putString("I want to pass PPL");
            }
            int foo(){
                return 3;
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,ArrayCell(Id(arr),IntLiteral(8)),BooleanLiteral(false))"
        self.assertTrue(TestChecker.test(input,expect,587))

    def test_type_mismatch_in_expression_assignment_expr_valid_with_many_block(self):
        input = """
            void main(){
                boolean arr[10];
                {
                    {
                        if(arr[9]==false){
                            int arr[10];
                            arr[9]=20;  
                            arr[8]=99;       
                        }
                        else{
                            return;
                        }
                        arr[9]=false;
                    }
                    if(arr[0]==true){
                        return;
                    }
                }
                foo();
                putString("I want to pass PPL");
            }
            int foo(){
                return 3;
            }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,588))

    #test funcall expression
    def test_type_mismatch_in_expression_funcall_expr_valid_with_many_block(self):
        input = """
            void main(){
                boolean arr[10];
                foo();
                putString("I want to pass PPL");
                string a;
                getStr(a);
                {
                    {
                        {
                            string b;
                            getStr(b);
                        }
                    }
                }
            }
            int foo(){
                return 3;
            }
            string[] getStr(string a){
                int size;
                string arr[10];
                arr[10]=a;
                return arr;
            }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,589))

    def test_type_mismatch_in_expression_funcall_expr_invalid_with_many_block(self):
        input = """
            void main(){
                boolean arr[10];
                foo();
                putString("I want to pass PPL");
                string a;
                getStr(a);
                {
                    {
                        {
                            boolean b;
                            getStr(b);      //error here: invalid parameter
                        }
                    }
                }
            }
            int foo(){
                return 3;
            }
            string[] getStr(string a){
                int size;
                string arr[10];
                arr[10]=a;
                return arr;
            }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(getStr),[Id(b)])"
        self.assertTrue(TestChecker.test(input,expect,590))

    #break in not loop
    def test_break_in_not_loop_invalid_with_many_block(self):
        input = """
            void main(){
                boolean arr[10];
                foo();
                putString("I want to pass PPL");
                string a;
                getStr(a);
                {
                    {
                        {
                            string b;
                            getStr(b);      
                        }
                    }
                    {
                        {
                            if(true){
                                break;      //error here: break in not loop
                            }
                        }
                    }
                }
            }
            int foo(){
                return 3;
            }
            string[] getStr(string a){
                int size;
                string arr[10];
                arr[10]=a;
                return arr;
            }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,591))

    def test_break_in_not_loop_valid_with_many_block(self):
        input = """
            void main(){
                boolean arr[10];
                foo();
                putString("I want to pass PPL");
                string a;
                getStr(a);
                {
                    {
                        {
                            string b;
                            getStr(b);      
                        }
                    }
                    {
                        {
                            do
                            if(true){
                                {
                                    {
                                        {
                                            break;
                                        }
                                    }
                                }
                            }
                            else{
                                return;
                            }
                            while(true);
                        }
                    }
                }
            }
            int foo(){
                return 3;
            }
            string[] getStr(string a){
                int size;
                string arr[10];
                arr[10]=a;
                return arr;
            }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,592))

    #test continue in not loop
    def test_continue_in_not_loop_valid_with_many_block(self):
        input = """
            void main(){
                boolean arr[10];
                foo();
                putString("I want to pass PPL");
                string a;
                getStr(a);
                {
                    {
                        {
                            string b;
                            getStr(b);      
                        }
                    }
                    {
                        {
                            do
                            if(true){
                                {
                                    {
                                        {
                                            continue;
                                        }
                                        continue;
                                    }
                                }
                            }
                            else{
                                return;
                            }
                            continue;
                            while(true);
                        }
                    }
                }
            }
            int foo(){
                return 3;
            }
            string[] getStr(string a){
                int size;
                string arr[10];
                arr[10]=a;
                return arr;
            }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,593))

    def test_continue_in_not_loop_invalid_with_many_block(self):
        input = """
            void main(){
                boolean arr[10];
                foo();
                putString("I want to pass PPL");
                string a;
                getStr(a);
                {
                    {
                        {
                            string b;
                            getStr(b);      
                        }
                    }
                    {
                        {
                            if(true){
                                {
                                    {
                                        {
                                            continue;       //error here
                                        }
                                        continue;
                                    }
                                }
                            }
                            else{
                                return;
                            }
                            continue;
                        }
                    }
                }
            }
            int foo(){
                return 3;
            }
            string[] getStr(string a){
                int size;
                string arr[10];
                arr[10]=a;
                return arr;
            }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,594))

    #test no entry point
    def test_no_entry_point_invalid_with_many_block(self):
        input = """
            void man(){
                boolean arr[10];
                foo();
                putString("I want to pass PPL");
                string a;
                getStr(a);
            }
            int foo(){
                return 3;
            }
            string[] getStr(string a){
                int size;
                string arr[10];
                arr[10]=a;
                return arr;
            }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,595))

    #test unreachable function
    def test_unreachable_func_invalid_with_many_block(self):
        input = """
            int main(){
                boolean arr[10];
                foo();
                putString("I want to pass PPL");
                string a;
                getStr(a);
                return 0;
            }
            int foo(){
                return 3;
            }
            string[] getStr(string a){
                string arr[10];
                return arr;
            }
            void print(string a){   //error here: not call print
                putString(a);
            }
        """
        expect = "Unreachable Function: print"
        self.assertTrue(TestChecker.test(input,expect,596))

    def test_unreachable_func_valid_with_many_block(self):
        input = """
            int main(){
                boolean arr[10];
                foo();
                putString("I want to pass PPL");
                string a;
                getStr(a);
                return 0;   
                print(a);
            }
            int foo(){
                return 3;
            }
            string[] getStr(string a){
                string arr[10];
                return arr;
            }
            void print(string a){ 
                putString(a);
            }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,597))

    #test not left value
    def test_not_left_value_invalid_with_many_block(self):
        input = """
            int main(){
                boolean arr[10];
                foo();
                putString("I want to pass PPL");
                string a;
                a="hello";
                int b;
                b+2=5;      //error here
                return 0;
                print(a);
            }
            int foo(){
                return 3;
            }
            void print(string a){ 
                putString(a);
            }
        """
        expect = "Not Left Value: BinaryOp(=,BinaryOp(+,Id(b),IntLiteral(2)),IntLiteral(5))"
        self.assertTrue(TestChecker.test(input,expect,598))

    def test_not_left_value_valid_with_many_block(self):
        input = """
            int main(){
                boolean arr[10];
                foo();
                putString("I want to pass PPL");
                string a;
                a="hello";
                int b;
                b=5*2+10;
                return 0;
                print(a)[3]="print";
            }
            int foo(){
                return 3;
            }
            string[] print(string a){ 
                putString(a);
                string arr[10];
                return arr;
            }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,599))

    