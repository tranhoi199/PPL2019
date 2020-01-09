import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """
            int main(){
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,300))

    def test_more_complex_program(self):
        """More complex program"""
        input = """int main () {
            putIntLn(4);
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("putIntLn"),[IntLiteral(4)])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,301))
    
    def test_call_without_parameter(self):
        """More complex program"""
        input = """int main () {
            getIntLn();
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("getIntLn"),[])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,302))

    def test_declare_outside_function(self):
        """Variable Decalre"""
        input = """
            int i;
            float t;
            string s;
        """
        expect = str(Program([VarDecl("i",IntType()),VarDecl("t",FloatType()),VarDecl("s",StringType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,303))

    def test_program_with_only_variable_declare(self):
        """Only variable declare inside main"""
        input = """
            void main(){
                int i;
                string s;
                float t;
                boolean b;                
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("i",IntType()),VarDecl("s",StringType()),VarDecl("t",FloatType()),VarDecl("b",BoolType())]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,304))

    def test_program_with_simple_assign(self):
        """Simple assign"""
        input = """
                void main(){
                    int i;
                    i=1;
                    float f;
                    f=0.2e-3;                                
                }
            """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("i",IntType()),BinaryOp("=",Id("i"),IntLiteral(1)),VarDecl("f",FloatType()),BinaryOp("=",Id("f"),FloatLiteral(0.0002))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,305))

    def test_program_with_complex_assign(self):
        """Complex assign"""
        input = """
                    void main(){
                        i=a*3+1-2/4;
                        b=true&&false||(false&&!true);
                        b=false;
                        s="ABCXYZ";                          
                    }
                """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("=",Id("i"),BinaryOp("-",BinaryOp("+",BinaryOp("*",Id("a"),IntLiteral(3)),IntLiteral(1)),BinaryOp("/",IntLiteral(2),IntLiteral(4)))),BinaryOp("=",Id("b"),BinaryOp("||",BinaryOp("&&",BooleanLiteral("true"),BooleanLiteral("false")),BinaryOp("&&",BooleanLiteral("false"),UnaryOp("!",BooleanLiteral("true"))))),BinaryOp("=",Id("b"),BooleanLiteral("false")),BinaryOp("=",Id("s"),StringLiteral("ABCXYZ"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,306))

    def test_program_with_more_complex_assign(self):
        """More Complex assign"""
        input = """
                    void main(){
                        i=2.0e-1+5e6;
                        i=20315+15456=ab;
                        s="ABC"+"xyz";
                        t=true||false&&true||false;                                                  
                    }
                """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("=",Id("i"),BinaryOp("+",FloatLiteral(0.2),FloatLiteral(5000000.0))),BinaryOp("=",BinaryOp("=",Id("i"),BinaryOp("+",IntLiteral(20315),IntLiteral(15456))),Id("ab")),BinaryOp("=",Id("s"),BinaryOp("+",StringLiteral("ABC"),StringLiteral("xyz"))),BinaryOp("=",Id("t"),BinaryOp("||",BinaryOp("||",BooleanLiteral("true"),BinaryOp("&&",BooleanLiteral("false"),BooleanLiteral("true"))),BooleanLiteral("false")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,307))

    def test_complex_assign_with_funcall(self):
        """Complex assign with funcall"""
        input = """
                    void main(){
                        i=0+funcall(i+1);                                              
                    }
                """
        expect=str(Program([FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("=",Id("i"),BinaryOp("+",IntLiteral(0),CallExpr(Id("funcall"),[BinaryOp("+",Id("i"),IntLiteral(1))])))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,308))

    def test_more_complex_assign_with_funcall(self):
        """Complex assign with funcall"""
        input = """
                    void main(){
                        i="ABC"-1/82.365e-1%t*2+funcall(funcall1(i*o+funcall2(2+3)));                                              
                    }
                """
        expect=str(Program([FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("=",Id("i"),BinaryOp("+",BinaryOp("-",StringLiteral("ABC"),BinaryOp("*",BinaryOp("%",BinaryOp("/",IntLiteral(1),FloatLiteral(8.2365)),Id("t")),IntLiteral(2))),CallExpr(Id("funcall"),[CallExpr(Id("funcall1"),[BinaryOp("+",BinaryOp("*",Id("i"),Id("o")),CallExpr(Id("funcall2"),[BinaryOp("+",IntLiteral(2),IntLiteral(3))]))])])))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,309))

    def test_mixed_assign_funcall_variable_declare(self):
        """Mixed assign, funcall, variable declare"""
        input = """
                    void main(){
                        int i;
                        i="ABC"-1/82.365e-1%t*2+funcall(funcall1(i*o+funcall2(2+3)));
                        string s;
                        s="ABCXYZ";
                        s=test(s+"xuy");                                              
                    }
                """
        expect=str(Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("i",IntType()),BinaryOp("=",Id("i"),BinaryOp("+",BinaryOp("-",StringLiteral("ABC"),BinaryOp("*",BinaryOp("%",BinaryOp("/",IntLiteral(1),FloatLiteral(8.2365)),Id("t")),IntLiteral(2))),CallExpr(Id("funcall"),[CallExpr(Id("funcall1"),[BinaryOp("+",BinaryOp("*",Id("i"),Id("o")),CallExpr(Id("funcall2"),[BinaryOp("+",IntLiteral(2),IntLiteral(3))]))])]))),VarDecl("s",StringType()),BinaryOp("=",Id("s"),StringLiteral("ABCXYZ")),BinaryOp("=",Id("s"),CallExpr(Id("test"),[BinaryOp("+",Id("s"),StringLiteral("xuy"))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,310))

    def test_long_nested_funcall(self):
        """Nested funcall"""
        input = """
                        int main(){
                            funcall1(funcall2(funcall3(funcall4(funcall5(funcall6(funcall7(funcall8(funcall9(funcall10())))))))));                  
                        }
                    """
        expect=str(Program([FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("funcall1"),[CallExpr(Id("funcall2"),[CallExpr(Id("funcall3"),[CallExpr(Id("funcall4"),[CallExpr(Id("funcall5"),[CallExpr(Id("funcall6"),[CallExpr(Id("funcall7"),[CallExpr(Id("funcall8"),[CallExpr(Id("funcall9"),[CallExpr(Id("funcall10"),[])])])])])])])])])])]))]))

        self.assertTrue(TestAST.checkASTGen(input,expect,311))

    def test_function_declare(self):
        """Function declare not main declare"""
        input = """
                    float test(int a,float b, string c,boolean d,int e[]){}
                    """
        expect=str(Program([FuncDecl(Id("test"),[VarDecl("a",IntType()),VarDecl("b",FloatType()),VarDecl("c",StringType()),VarDecl("d",BoolType()),VarDecl("e",ArrayPointerType(IntType()))],FloatType(),Block([]))]))

        self.assertTrue(TestAST.checkASTGen(input,expect,312))

    def test_function_declare_1(self):
        """Return type is array"""
        input = """
                    float[] test(int a,float b, string c,boolean d,int e[]){}
                    """
        expect=str(Program([FuncDecl(Id("test"),[VarDecl("a",IntType()),VarDecl("b",FloatType()),VarDecl("c",StringType()),VarDecl("d",BoolType()),VarDecl("e",ArrayPointerType(IntType()))],ArrayPointerType(FloatType()),Block([]))]))

        self.assertTrue(TestAST.checkASTGen(input,expect,313))

    def test_function_declare_main_declare(self):
        """Function declare and main declare"""
        input = """
                   int main(){}
                   string test(){}
                    """
        expect=str(Program([FuncDecl(Id("main"),[],IntType(),Block([])),FuncDecl(Id("test"),[],StringType(),Block([]))]))

        self.assertTrue(TestAST.checkASTGen(input,expect,314))

    def test_function_main_variable_declare(self):
        """Mixed function, main, variable declare"""
        input = """
                    int a;
                    int main(){}
                    float test(int b,float a[]){}
                    string b;                    
                    """
        expect=str(Program([VarDecl("a",IntType()),FuncDecl(Id("main"),[],IntType(),Block([])),FuncDecl(Id("test"),[VarDecl("b",IntType()),VarDecl("a",ArrayPointerType(FloatType()))],FloatType(),Block([])),VarDecl("b",StringType())]))


        self.assertTrue(TestAST.checkASTGen(input,expect,315))

    def test_relation_expression(self):
        """Relational Expression"""
        input = """
                    int main(){
                        boolean b;
                        b= true||(a>b);
                    }                  
                        """
        expect=str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("b",BoolType()),BinaryOp("=",Id("b"),BinaryOp("||",BooleanLiteral("true"),BinaryOp(">",Id("a"),Id("b"))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,316))

    def test_return_simple_statement(self):
        """Return simple statement"""
        input = """
                    int main(){
                        return true;
                        return 1;
                        return "ABC";
                        return a;
                    }                  
                        """
        expect=str(Program([FuncDecl(Id("main"),[],IntType(),Block([Return(BooleanLiteral("true")),Return(IntLiteral(1)),Return(StringLiteral("ABC")),Return(Id("a"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,317))

    def test_return_complex_statement(self):
        """Return complex statement"""
        input = """
            int main(){
                return a+b-c;
                return a*b/2+1%2-5;
                return true||true&&false(true||(a>b)&&a==c);
                return "ABC"+"xyzabc";
                return 2.0e-9+30e5;
            }                  
        """
        expect=str(Program([FuncDecl(Id("main"),[],IntType(),Block([Return(BinaryOp("-",BinaryOp("+",Id("a"),Id("b")),Id("c"))),Return(BinaryOp("-",BinaryOp("+",BinaryOp("/",BinaryOp("*",Id("a"),Id("b")),IntLiteral(2)),BinaryOp("%",IntLiteral(1),IntLiteral(2))),IntLiteral(5))),Return(BinaryOp("||",BooleanLiteral("true"),BinaryOp("&&",BooleanLiteral("true"),BooleanLiteral("false")))),BinaryOp("||",BooleanLiteral("true"),BinaryOp("&&",BinaryOp(">",Id("a"),Id("b")),BinaryOp("==",Id("a"),Id("c")))),Return(BinaryOp("+",StringLiteral("ABC"),StringLiteral("xyzabc"))),Return(BinaryOp("+",FloatLiteral(2e-09),FloatLiteral(3000000.0)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,318))

    def test_equal_statement(self):
        """Equal statement"""
        input = """
            int main(){
                a=a==b==c==e==f==g==h!=d!=y!=h==c;
            }                  
        """
        expect=str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",Id("a"),BinaryOp("==",BinaryOp("!=",BinaryOp("!=",BinaryOp("!=",BinaryOp("==",BinaryOp("==",BinaryOp("==",BinaryOp("==",BinaryOp("==",BinaryOp("==",Id("a"),Id("b")),Id("c")),Id("e")),Id("f")),Id("g")),Id("h")),Id("d")),Id("y")),Id("h")),Id("c")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,319))

    def test_add_statementt(self):
        """Add statement"""
        input = """
            int main(){
                int a;
                a=a+b=i-9=c;
                string s;
                s="ABC"+"AGH"*"IOK"/"JKL";
                float f;
                f=1.0+2.0e-6+3.5+6.5;
            }                  
        """
        expect=str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",IntType()),BinaryOp("=",BinaryOp("=",BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),Id("b"))),BinaryOp("-",Id("i"),IntLiteral(9))),Id("c")),VarDecl("s",StringType()),BinaryOp("=",Id("s"),BinaryOp("+",StringLiteral("ABC"),BinaryOp("/",BinaryOp("*",StringLiteral("AGH"),StringLiteral("IOK")),StringLiteral("JKL")))),VarDecl("f",FloatType()),BinaryOp("=",Id("f"),BinaryOp("+",BinaryOp("+",BinaryOp("+",FloatLiteral(1.0),FloatLiteral(2e-06)),FloatLiteral(3.5)),FloatLiteral(6.5)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,320))

    def test_complex_add_statementt(self):
        """Add statement"""
        input = """
            int main(){
                a=a+b+c*6/8%5+3+645-98+test(56)*96/(96+(-96)*(-63));
            }                  
        """
        expect=str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",Id("a"),BinaryOp("+",BinaryOp("-",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",Id("a"),Id("b")),BinaryOp("%",BinaryOp("/",BinaryOp("*",Id("c"),IntLiteral(6)),IntLiteral(8)),IntLiteral(5))),IntLiteral(3)),IntLiteral(645)),IntLiteral(98)),BinaryOp("/",BinaryOp("*",CallExpr(Id("test"),[IntLiteral(56)]),IntLiteral(96)),BinaryOp("+",IntLiteral(96),BinaryOp("*",UnaryOp("-",IntLiteral(96)),UnaryOp("-",IntLiteral(63)))))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,321))

    def test_nested_bracket(self):
        """Nested Bracket"""
        input = """
            int main(){
                a=((((((((((((((((((((((((a+2))))))))))))))))))))))));
            }                  
        """
        expect=str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(2)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,322))

    def test_simple_unary_statement(self):
        """Simple unary statement"""
        input = """
            int main(){
                a=!b;
                a=-b;
                a=--b;
            }                  
        """
        expect=str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",Id("a"),UnaryOp("!",Id("b"))),BinaryOp("=",Id("a"),UnaryOp("-",Id("b"))),BinaryOp("=",Id("a"),UnaryOp("-",UnaryOp("-",Id("b"))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,323))

    def test_complex_unary_statement(self):
        """Complex uanry statement"""
        input = """
            int main(){
                a= -!-!!!-!!!-!!!-!!!b;
            }                  
        """
        expect=str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",Id("a"),UnaryOp("-",UnaryOp("!",UnaryOp("-",UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("-",UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("-",UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("-",UnaryOp("!",UnaryOp("!",UnaryOp("!",Id("b"))))))))))))))))))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,324))

    def test_simple_array_cell(self):
        """Simple array cell"""
        input = """
            int main(){
                int a[7];
                a[5]=0;
                a[5]=a[7];
                n=a[3];
            }         
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",ArrayType(7,IntType())),BinaryOp("=",ArrayCell(Id("a"),IntLiteral(5)),IntLiteral(0)),BinaryOp("=",ArrayCell(Id("a"),IntLiteral(5)),ArrayCell(Id("a"),IntLiteral(7))),BinaryOp("=",Id("n"),ArrayCell(Id("a"),IntLiteral(3)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,325))

    def test_complex_array_cell(self):
        """Simple array cell"""
        input = """
            int main(){
                a[7*5+1-3/2%5]=1;
                g=bt[42%9*6+3-8/2+funcall(6)];
            }         
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",ArrayCell(Id("a"),BinaryOp("-",BinaryOp("+",BinaryOp("*",IntLiteral(7),IntLiteral(5)),IntLiteral(1)),BinaryOp("%",BinaryOp("/",IntLiteral(3),IntLiteral(2)),IntLiteral(5)))),IntLiteral(1)),BinaryOp("=",Id("g"),ArrayCell(Id("bt"),BinaryOp("+",BinaryOp("-",BinaryOp("+",BinaryOp("*",BinaryOp("%",IntLiteral(42),IntLiteral(9)),IntLiteral(6)),IntLiteral(3)),BinaryOp("/",IntLiteral(8),IntLiteral(2))),CallExpr(Id("funcall"),[IntLiteral(6)]))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,326))

    def test_simple_funcall(self):
        """Simple funcall"""
        input = """
            int main(){
                int a;
                a=funcall(56+9-8);
            }         
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",IntType()),BinaryOp("=",Id("a"),CallExpr(Id("funcall"),[BinaryOp("-",BinaryOp("+",IntLiteral(56),IntLiteral(9)),IntLiteral(8))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,327))

    def test_complex_funcall(self):
        """Complex funcall"""
        input = """
            int main(){
                int a;
                a=funcall(i*5+3-8/6);
                funcall(true&&false||false>=(true||false&&(true||true)));
            }         
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",IntType()),BinaryOp("=",Id("a"),CallExpr(Id("funcall"),[BinaryOp("-",BinaryOp("+",BinaryOp("*",Id("i"),IntLiteral(5)),IntLiteral(3)),BinaryOp("/",IntLiteral(8),IntLiteral(6)))])),CallExpr(Id("funcall"),[BinaryOp("||",BinaryOp("&&",BooleanLiteral("true"),BooleanLiteral("false")),BinaryOp(">=",BooleanLiteral("false"),BinaryOp("||",BooleanLiteral("true"),BinaryOp("&&",BooleanLiteral("false"),BinaryOp("||",BooleanLiteral("true"),BooleanLiteral("true"))))))])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,328))

    def test_multi_para_funcall(self):
        """Multi para funcall"""
        input = """
            int main(){
                funcall(a,b,c,e,f,g,true&&false||true,a+6*(5-6+9%5+6)*8-9/3);
            }         
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("funcall"),[Id("a"),Id("b"),Id("c"),Id("e"),Id("f"),Id("g"),BinaryOp("||",BinaryOp("&&",BooleanLiteral("true"),BooleanLiteral("false")),BooleanLiteral("true")),BinaryOp("-",BinaryOp("+",Id("a"),BinaryOp("*",BinaryOp("*",IntLiteral(6),BinaryOp("+",BinaryOp("+",BinaryOp("-",IntLiteral(5),IntLiteral(6)),BinaryOp("%",IntLiteral(9),IntLiteral(5))),IntLiteral(6))),IntLiteral(8))),BinaryOp("/",IntLiteral(9),IntLiteral(3)))])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,329))

    def test_multi_complex_para_funcall(self):
        """Multi para funcall"""
        input = """
            int main(){
                funcall(funcall1(a,b,c,r,g),a,f,qw,q,a,x,56+98-96+3,-89-89-63,"ABC"+"abc");
            }         
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("funcall"),[CallExpr(Id("funcall1"),[Id("a"),Id("b"),Id("c"),Id("r"),Id("g")]),Id("a"),Id("f"),Id("qw"),Id("q"),Id("a"),Id("x"),BinaryOp("+",BinaryOp("-",BinaryOp("+",IntLiteral(56),IntLiteral(98)),IntLiteral(96)),IntLiteral(3)),BinaryOp("-",BinaryOp("-",UnaryOp("-",IntLiteral(89)),IntLiteral(89)),IntLiteral(63)),BinaryOp("+",StringLiteral("ABC"),StringLiteral("abc"))])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,330))

    def test_simple_if_statement(self):
        """If statement"""
        input = """
            int main(){
                if(3>4) i=i+1;
            }         
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp(">",IntLiteral(3),IntLiteral(4)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,331))

    def test_simple_if_else_statement(self):
        """If else statement"""
        input = """
            int main(){
                if(3>4) i=i+1;
                else i=i+2;
            }         
        """
        expect =str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp(">",IntLiteral(3),IntLiteral(4)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(2))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,332))

    def test_complex_if_statement(self):
        """Complex if statement"""
        input = """
            int main(){
                if(i>4)
                {
                    int i;
                    float b;
                    string s;
                    s="ABC";
                    int p[5];
                    i = 1+5;
                    b = true||false;
                }
            }         
        """
        expect =str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp(">",Id("i"),IntLiteral(4)),Block([VarDecl("i",IntType()),VarDecl("b",FloatType()),VarDecl("s",StringType()),BinaryOp("=",Id("s"),StringLiteral("ABC")),VarDecl("p",ArrayType(5,IntType())),BinaryOp("=",Id("i"),BinaryOp("+",IntLiteral(1),IntLiteral(5))),BinaryOp("=",Id("b"),BinaryOp("||",BooleanLiteral("true"),BooleanLiteral("false")))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,333))

    def test_complex_if_else_statement(self):
        """Complex if else statement"""
        input = """
            int main(){
                if(i>4)
                {
                    i= 3*2+1-2;
                    s="ABC"+"abc";
                }else
                    i=i+2-6*8/3;
            }         
        """
        expect =str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp(">",Id("i"),IntLiteral(4)),Block([BinaryOp("=",Id("i"),BinaryOp("-",BinaryOp("+",BinaryOp("*",IntLiteral(3),IntLiteral(2)),IntLiteral(1)),IntLiteral(2))),BinaryOp("=",Id("s"),BinaryOp("+",StringLiteral("ABC"),StringLiteral("abc")))]),BinaryOp("=",Id("i"),BinaryOp("-",BinaryOp("+",Id("i"),IntLiteral(2)),BinaryOp("/",BinaryOp("*",IntLiteral(6),IntLiteral(8)),IntLiteral(3)))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,334))

    def test_complex_if_else_with_block_statement(self):
        """Complex if else statement (else has block)"""
        input = """
            int main(){
                if(i>4)
                {
                    i= 3*2+1-2;
                    s="ABC"+"abc";
                }else
                    {
                        int i;
                        i=i+3*8/6;
                        b=true||false&&true||(true||false);
                    }
            }         
        """
        expect =str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp(">",Id("i"),IntLiteral(4)),Block([BinaryOp("=",Id("i"),BinaryOp("-",BinaryOp("+",BinaryOp("*",IntLiteral(3),IntLiteral(2)),IntLiteral(1)),IntLiteral(2))),BinaryOp("=",Id("s"),BinaryOp("+",StringLiteral("ABC"),StringLiteral("abc")))]),Block([VarDecl("i",IntType()),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),BinaryOp("/",BinaryOp("*",IntLiteral(3),IntLiteral(8)),IntLiteral(6)))),BinaryOp("=",Id("b"),BinaryOp("||",BinaryOp("||",BooleanLiteral("true"),BinaryOp("&&",BooleanLiteral("false"),BooleanLiteral("true"))),BinaryOp("||",BooleanLiteral("true"),BooleanLiteral("false"))))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,335))

    def test_simple_nested_if(self):
        """Simple nested if statement"""
        input = """
            int main(){
                if (i>4)
                    if(i<3)
                        i=i+1;
            }         
        """
        expect =str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp(">",Id("i"),IntLiteral(4)),If(BinaryOp("<",Id("i"),IntLiteral(3)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,336))

    def test_complex_nested_if(self):
        """Complex nested if statement"""
        input = """
            int main(){
                if (i>4)
                    if(i<3)
                        {
                            int i;
                            i=3;
                            s="ABC"+"xyz";
                            if(i<2) 
                                print(i);
                            m=3;
                        }
            }         
        """
        expect =str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp(">",Id("i"),IntLiteral(4)),If(BinaryOp("<",Id("i"),IntLiteral(3)),Block([VarDecl("i",IntType()),BinaryOp("=",Id("i"),IntLiteral(3)),BinaryOp("=",Id("s"),BinaryOp("+",StringLiteral("ABC"),StringLiteral("xyz"))),If(BinaryOp("<",Id("i"),IntLiteral(2)),CallExpr(Id("print"),[Id("i")])),BinaryOp("=",Id("m"),IntLiteral(3))])))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,337))

    def test_moe_complex_nested_if(self):
        """More complex nested if statement"""
        input = """
            int main(){
                if (i>4)
                {
                    string s;
                    int a[6];
                    if(i<3)
                        {
                            int i;
                            i=3;
                            s="ABC"+"xyz";
                            if(i<2) 
                                print(i);
                            m=3;
                 
                        }
                    int h;
                    h=4+5+8+9;
                    if(true)
                        int i;
                }
            }         
        """
        expect =str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp(">",Id("i"),IntLiteral(4)),Block([VarDecl("s",StringType()),VarDecl("a",ArrayType(IntLiteral(6),IntType())),If(BinaryOp("<",Id("i"),IntLiteral(3)),Block([VarDecl("i",IntType()),BinaryOp("=",Id("i"),IntLiteral(3)),BinaryOp("=",Id("s"),BinaryOp("+",StringLiteral("ABC"),StringLiteral("xyz"))),If(BinaryOp("<",Id("i"),IntLiteral(2)),CallExpr(Id("print"),[Id("i")])),BinaryOp("=",Id("m"),IntLiteral(3))])),VarDecl("h",IntType()),BinaryOp("=",Id("h"),BinaryOp("+",BinaryOp("+",BinaryOp("+",IntLiteral(4),IntLiteral(5)),IntLiteral(8)),IntLiteral(9))),If(BooleanLiteral("true"),VarDecl("i",IntType()))]))]))]))

        self.assertTrue(TestAST.checkASTGen(input,expect,338))

    def test_moe_complex_nested_if(self):
        """Declare empty funtion"""
        input = """int testFunction(){}"""
        expect = str(Program([FuncDecl(Id("testFunction"),[],IntType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,339))

    def test_declare_empty_function_with_para(self):
        """Declare empty funtion that have parameter"""
        input = """int testFuction(int a,float b,string n){}"""
        expect = str(Program([FuncDecl(Id("testFuction"),[VarDecl("a",IntType()),VarDecl("b",FloatType()),VarDecl("n",StringType())],IntType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,340))

    def test_declare_empty_function_with_array_para(self):
        """Declare empty funtion that have array parameter"""
        input = """int testFuction(int a,float b,string n,string a[]){}"""
        expect = str(Program([FuncDecl(Id("testFuction"),[VarDecl("a",IntType()),VarDecl("b",FloatType()),VarDecl("n",StringType()),VarDecl("a",ArrayPointerType(StringType()))],IntType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,341))

    def test_function_with_variable(self):
        """Function with variable inside"""
        input = """int testFuction(int a,float b,string n,string a[]){
            int a;
            float b;
            string s;
            int a[6];
        }"""
        expect = str(Program([FuncDecl(Id("testFuction"),[VarDecl("a",IntType()),VarDecl("b",FloatType()),VarDecl("n",StringType()),VarDecl("a",ArrayPointerType(StringType()))],IntType(),Block([VarDecl("a",IntType()),VarDecl("b",FloatType()),VarDecl("s",StringType()),VarDecl("a",ArrayType(6,IntType()))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,342))

    def test_function_with_funcall_and_complex_para(self):
        """Function with funcall inside"""
        input = """int testFuction(int a,float b,string n,string a[]){
            testFunction(3*2+1-2,i*3>1);
        }"""
        expect = str(Program([FuncDecl(Id("testFuction"),[VarDecl("a",IntType()),VarDecl("b",FloatType()),VarDecl("n",StringType()),VarDecl("a",ArrayPointerType(StringType()))],IntType(),Block([CallExpr(Id("testFunction"),[BinaryOp("-",BinaryOp("+",BinaryOp("*",IntLiteral(3),IntLiteral(2)),IntLiteral(1)),IntLiteral(2)),BinaryOp(">",BinaryOp("*",Id("i"),IntLiteral(3)),IntLiteral(1))])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,343))

    def test_function_with_funcall_and_complex_para_mixed_variable(self):
        """Function with funcall inside and have variable mixed in"""
        input = """int testFuction(int a,float b,string n,string a[]){
            int i;
            float b;
            string a;
            testFunction(3*2+1-2,i*3>1);
        }"""
        expect = str(Program([FuncDecl(Id("testFuction"),[VarDecl("a",IntType()),VarDecl("b",FloatType()),VarDecl("n",StringType()),VarDecl("a",ArrayPointerType(StringType()))],IntType(),Block([VarDecl("i",IntType()),VarDecl("b",FloatType()),VarDecl("a",StringType()),CallExpr(Id("testFunction"),[BinaryOp("-",BinaryOp("+",BinaryOp("*",IntLiteral(3),IntLiteral(2)),IntLiteral(1)),IntLiteral(2)),BinaryOp(">",BinaryOp("*",Id("i"),IntLiteral(3)),IntLiteral(1))])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,344))

    def test_program_with_multi_function(self):
        "Program have multiple functon"
        input = """int test_Function(){
            int a;
            float b;
            }
            void main(){
                string str[5];
                int a;
            }
        """
        expect = str(Program([FuncDecl(Id("test_Function"),[],IntType(),Block([VarDecl("a",IntType()),VarDecl("b",FloatType())])),FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("str",ArrayType(5,StringType())),VarDecl("a",IntType())]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,345))

    def test_function_with_output_array(self):
        "Function with output is array"
        input = """int[] testFunction(){}
        """
        expect = str(Program([FuncDecl(Id("testFunction"),[],ArrayPointerType(IntType()),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,346))

    def test_boolean_expression(self):
        "Simple expression"
        input = """int testFunction(){
            int a;
            boolean b;
            b=b>(a*i)+1-2;
        }
        """
        expect = str(Program([FuncDecl(Id("testFunction"),[],IntType(),Block([VarDecl("a",IntType()),VarDecl("b",BoolType()),BinaryOp("=",Id("b"),BinaryOp(">",Id("b"),BinaryOp("-",BinaryOp("+",BinaryOp("*",Id("a"),Id("i")),IntLiteral(1)),IntLiteral(2))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,347))

    def test_multi_assignment_expression(self):
        "Expression that have many assignment"
        input = """int testFunction(){
            i=3=4=5=6=7;
        }
        """
        expect = str(Program([FuncDecl(Id("testFunction"),[],IntType(),Block([BinaryOp("=",BinaryOp("=",BinaryOp("=",BinaryOp("=",BinaryOp("=",Id("i"),IntLiteral(3)),IntLiteral(4)),IntLiteral(5)),IntLiteral(6)),IntLiteral(7))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,348))

    def test_wrong_expression(self):
        "Not, minus, plus sign wrong position"
        input = """int testFunction(){
            i=i+!5-+p;
        }
        """
        expect = str(Program([FuncDecl(Id("testFunction"),[],IntType(),Block([BinaryOp("=",Id("i"),BinaryOp("-",BinaryOp("+",Id("i"),UnaryOp("!",IntLiteral(5))),Id("p")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,349))

    def test_expression_with_float(self):
        "Expression with float number"
        input = """
        int testFunction(){
            float i;
            i=5.0+0.2e-5;
        }
        """
        expect = str(Program([FuncDecl(Id("testFunction"),[],IntType(),Block([VarDecl("i",FloatType()),BinaryOp("=",Id("i"),BinaryOp("+",FloatLiteral(5.0),FloatLiteral(2e-06)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,350))

    def test_expression_with_string(self):
        "Expression with string"
        input = """
        int testFunction(){
            string str;
            str="This is a"+"string";
        }
        """
        expect = str(Program([FuncDecl(Id("testFunction"),[],IntType(),Block([VarDecl("str",StringType()),BinaryOp("=",Id("str"),BinaryOp("+",StringLiteral("This is a"),StringLiteral("string")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,351))

    def test_if_statement_with_string(self):
        "String in if statement"
        input = """
        int testFunction(){
            if(i>3)
                {
                    string i;
                    i="This is a string";
                }
                
        }
        """
        expect = str(Program([FuncDecl(Id("testFunction"),[],IntType(),Block([If(BinaryOp(">",Id("i"),IntLiteral(3)),Block([VarDecl("i",StringType()),BinaryOp("=",Id("i"),StringLiteral("This is a string"))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,352))

    def test_more_complex_nested_if_statement(self):
        "More complex nested if statement"
        input = """     
        int main(){   
            if(3>4) {
                if(2>3) {
                    if(8>1) o=i+o;
                    else if(u>0) i-1;
                }
                else if(m>n){
                    if(2>3)
                        I+9;
                }
                    
            }else{
                if(m>n) {
                    if(2>3) i+21;
                }
                else i-1;
            }
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp(">",IntLiteral(3),IntLiteral(4)),Block([If(BinaryOp(">",IntLiteral(2),IntLiteral(3)),Block([If(BinaryOp(">",IntLiteral(8),IntLiteral(1)),BinaryOp("=",Id("o"),BinaryOp("+",Id("i"),Id("o"))),If(BinaryOp(">",Id("u"),IntLiteral(0)),BinaryOp("-",Id("i"),IntLiteral(1))))]),If(BinaryOp(">",Id("m"),Id("n")),Block([If(BinaryOp(">",IntLiteral(2),IntLiteral(3)),BinaryOp("+",Id("I"),IntLiteral(9)))])))]),Block([If(BinaryOp(">",Id("m"),Id("n")),Block([If(BinaryOp(">",IntLiteral(2),IntLiteral(3)),BinaryOp("+",Id("i"),IntLiteral(21)))]),BinaryOp("-",Id("i"),IntLiteral(1)))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,353))

    def test_complex_nested_if_statement_without_block(self):
        "Complex nested if statement without block"
        input = """     
        int main(){   
            if(i>2)
                if(m>n)
                    if(2==2)
                        if(25/3>1)
                            if(i>2) 
                                if(i<2)
                                    if(i>3)
                                        if(9>1)
                                            i=i+1;
                                        else 1+3;
                                    else 1+4;
                                else i=1;
                            else 5+6;
                        else 1+2;
                    else 1+3;
                else i;            
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp(">",Id("i"),IntLiteral(2)),If(BinaryOp(">",Id("m"),Id("n")),If(BinaryOp("==",IntLiteral(2),IntLiteral(2)),If(BinaryOp(">",BinaryOp("/",IntLiteral(25),IntLiteral(3)),IntLiteral(1)),If(BinaryOp(">",Id("i"),IntLiteral(2)),If(BinaryOp("<",Id("i"),IntLiteral(2)),If(BinaryOp(">",Id("i"),IntLiteral(3)),If(BinaryOp(">",IntLiteral(9),IntLiteral(1)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),BinaryOp("+",IntLiteral(1),IntLiteral(3))),BinaryOp("+",IntLiteral(1),IntLiteral(4))),BinaryOp("=",Id("i"),IntLiteral(1))),BinaryOp("+",IntLiteral(5),IntLiteral(6))),BinaryOp("+",IntLiteral(1),IntLiteral(2))),BinaryOp("+",IntLiteral(1),IntLiteral(3))),Id("i")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,354))

    def test_simple_for_statement(self):
        "Simple for statement"
        input = """     
        int main(){   
            for(i=1;i<1;i=i+1){
                i-1;
            } 
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(1)),BinaryOp("<",Id("i"),IntLiteral(1)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([BinaryOp("-",Id("i"),IntLiteral(1))]))]))])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,355))

    def test_complex_for_statement(self):
        "Simple for statement"
        input = """     
        int main(){   
            for(i=1;i<(a*b+3-1/2);i=i||1+2){
                int a;
                a=3;
                5+6;
            } 
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(1)),BinaryOp("<",Id("i"),BinaryOp("-",BinaryOp("+",BinaryOp("*",Id("a"),Id("b")),IntLiteral(3)),BinaryOp("/",IntLiteral(1),IntLiteral(2)))),BinaryOp("=",Id("i"),BinaryOp("||",Id("i"),BinaryOp("+",IntLiteral(1),IntLiteral(2)))),Block([VarDecl("a",IntType()),BinaryOp("=",Id("a"),IntLiteral(3)),BinaryOp("+",IntLiteral(5),IntLiteral(6))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,356))

    def test_block_for_statement(self):
        "Block statement in for statement"
        input = """     
        int main(){   
            for(i=1;i<(a*b+3-1/2);i=i||1+2){
                int a;
                a=3;
                5+6;
            } 
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(1)),BinaryOp("<",Id("i"),BinaryOp("-",BinaryOp("+",BinaryOp("*",Id("a"),Id("b")),IntLiteral(3)),BinaryOp("/",IntLiteral(1),IntLiteral(2)))),BinaryOp("=",Id("i"),BinaryOp("||",Id("i"),BinaryOp("+",IntLiteral(1),IntLiteral(2)))),Block([VarDecl("a",IntType()),BinaryOp("=",Id("a"),IntLiteral(3)),BinaryOp("+",IntLiteral(5),IntLiteral(6))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,357))

    def test_if_statement_inside_for_statement(self):
        "If statement inside for statment"
        input = """     
        int main(){   
            for(i=1;i<(a*b+3-1/2);i=i||1+2)
                if(1>3) i=i+1;
                else i=i-1;
        }
        """
        expect =str(Program([FuncDecl(Id("main"),[],IntType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(1)),BinaryOp("<",Id("i"),BinaryOp("-",BinaryOp("+",BinaryOp("*",Id("a"),Id("b")),IntLiteral(3)),BinaryOp("/",IntLiteral(1),IntLiteral(2)))),BinaryOp("=",Id("i"),BinaryOp("||",Id("i"),BinaryOp("+",IntLiteral(1),IntLiteral(2)))),If(BinaryOp(">",IntLiteral(1),IntLiteral(3)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),BinaryOp("=",Id("i"),BinaryOp("-",Id("i"),IntLiteral(1)))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,358))

    def test_complex_if_statement_inside_for_statement(self):
        "Complex if statement inside for statment"
        input = """     
        int main(){   
            for(i=1;i<(a*b+3-1/2);i=i||1+2)
                if(9>10) {
                    i=i+1;
                    int b;
                    string s;
                }else
                {
                    int h;
                    a=a+1;
                }
        }
        """
        expect=str(Program([FuncDecl(Id("main"),[],IntType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(1)),BinaryOp("<",Id("i"),BinaryOp("-",BinaryOp("+",BinaryOp("*",Id("a"),Id("b")),IntLiteral(3)),BinaryOp("/",IntLiteral(1),IntLiteral(2)))),BinaryOp("=",Id("i"),BinaryOp("||",Id("i"),BinaryOp("+",IntLiteral(1),IntLiteral(2)))),If(BinaryOp(">",IntLiteral(9),IntLiteral(10)),Block([BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),VarDecl("b",IntType()),VarDecl("s",StringType())]),Block([VarDecl("h",IntType()),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1)))])))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,359))

    def test_nested_for_function(self):
        "Nested for function"
        input = """
            int main(){
                for(i=1;i<2;i=i+1){
                    for(j=1;j<i;j=j+1)
                        int j;
                }
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(1)),BinaryOp("<",Id("i"),IntLiteral(2)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([For(BinaryOp("=",Id("j"),IntLiteral(1)),BinaryOp("<",Id("j"),Id("i")),BinaryOp("=",Id("j"),BinaryOp("+",Id("j"),IntLiteral(1))),VarDecl("j",IntType()))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,360))

    def test_complex_nested_for_function(self):
        "Complex nested for function"
        input = """     
            int main(){
                for(i=1;i<2;i=i+1)
                    for(j=1;j<i;j=j+1)
                        for(k=1;k>1;k=k-1){
                            for(h=1;h>3-4;h=h*2)
                                int j;
                            k=k-1;
                        }                
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(1)),BinaryOp("<",Id("i"),IntLiteral(2)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),For(BinaryOp("=",Id("j"),IntLiteral(1)),BinaryOp("<",Id("j"),Id("i")),BinaryOp("=",Id("j"),BinaryOp("+",Id("j"),IntLiteral(1))),For(BinaryOp("=",Id("k"),IntLiteral(1)),BinaryOp(">",Id("k"),IntLiteral(1)),BinaryOp("=",Id("k"),BinaryOp("-",Id("k"),IntLiteral(1))),Block([For(BinaryOp("=",Id("h"),IntLiteral(1)),BinaryOp(">",Id("h"),BinaryOp("-",IntLiteral(3),IntLiteral(4))),BinaryOp("=",Id("h"),BinaryOp("*",Id("h"),IntLiteral(2))),VarDecl("j",IntType())),BinaryOp("=",Id("k"),BinaryOp("-",Id("k"),IntLiteral(1)))]))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,361))

    def test_for_statement_inside_if_statement(self):
        "For statement inside of if statement"
        input = """     
            int main(){
                if(k>1)
                    for(i=2;i<2;i=i+1){
                        int k;
                        k<1;
                        k=k+1;
                    }           
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp(">",Id("k"),IntLiteral(1)),For(BinaryOp("=",Id("i"),IntLiteral(2)),BinaryOp("<",Id("i"),IntLiteral(2)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([VarDecl("k",IntType()),BinaryOp("<",Id("k"),IntLiteral(1)),BinaryOp("=",Id("k"),BinaryOp("+",Id("k"),IntLiteral(1)))])))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,362))

    def test_for_statement_with_float(self):
        "Float number inside for condition"
        input = """     
            int main(){
                    for(f=2.0e-53;i<8.0e3;i=i+.1){
                        int k;
                        k<1;
                        k=k+1;
                    }                 
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([For(BinaryOp("=",Id("f"),FloatLiteral(2e-53)),BinaryOp("<",Id("i"),FloatLiteral(8000.0)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),FloatLiteral(0.1))),Block([VarDecl("k",IntType()),BinaryOp("<",Id("k"),IntLiteral(1)),BinaryOp("=",Id("k"),BinaryOp("+",Id("k"),IntLiteral(1)))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,363))

    def test_for_statement_with_string(self):
        "String inside for statement"
        input = """     
            int main(){
                    for(i=1;i<1;i=i+1){
                        string s;
                        s="This is a string";
                    }                 
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(1)),BinaryOp("<",Id("i"),IntLiteral(1)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([VarDecl("s",StringType()),BinaryOp("=",Id("s"),StringLiteral("This is a string"))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,364))

    def test_multi_variable_declaration(self):
        "Declare multi variable"
        input = """     
            int main(){
                int a,b,c,d,e,f;
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",IntType()),VarDecl("e",IntType()),VarDecl("f",IntType())]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,365))

    def test_multi_variable_declaration_mixed_with_array(self):
        "Declare multi variable mixed with array"
        input = """
            int main(){
                int a,b,c,d,e,f,a[5],s[10];
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",IntType()),VarDecl("e",IntType()),VarDecl("f",IntType()),VarDecl("a",ArrayType(5,IntType())),VarDecl("s",ArrayType(10,IntType()))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,366))

    def test_multi_variable_declaration_mixed_with_array_outside_function(self):
        "Declare multi variable outside of function"
        input = """     
                int a,b,c,d,e,f,a[5],s[10];
        """
        expect = str(Program([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",IntType()),VarDecl("e",IntType()),VarDecl("f",IntType()),VarDecl("a",ArrayType(5,IntType())),VarDecl("s",ArrayType(10,IntType()))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,367))

    def test_funcall_multi_assignment(self):
        "Multi assignment inside funcall"
        input = """     
                int main(){
                    func(i=1=a+3=1);
                }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("func"),[BinaryOp("=",BinaryOp("=",BinaryOp("=",Id("i"),IntLiteral(1)),BinaryOp("+",Id("a"),IntLiteral(3))),IntLiteral(1))])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,368))

    def test_expression_inside_funcall(self):
        "Expression in side funcall"
        input = """     
                int main(){
                    func(i<3>1-1=2+3*2%1);
                }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("func"),[BinaryOp("=",BinaryOp(">",BinaryOp("<",Id("i"),IntLiteral(3)),BinaryOp("-",IntLiteral(1),IntLiteral(1))),BinaryOp("+",IntLiteral(2),BinaryOp("%",BinaryOp("*",IntLiteral(3),IntLiteral(2)),IntLiteral(1))))])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,369))

    def test_complex_array(self):
        "Complex array"
        input = """     
                int main(){
                    a[0]=a[2*b[3+1]=2];
                }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",ArrayCell(Id("a"),IntLiteral(0)),ArrayCell(Id("a"),BinaryOp("=",BinaryOp("*",IntLiteral(2),ArrayCell(Id("b"),BinaryOp("+",IntLiteral(3),IntLiteral(1)))),IntLiteral(2))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,370))

    def test_return_break_inside_do_statement(self):
        "Complex array"
        input = """     
                int main(){
                    do
                        int i;
                        break;
                        return;
                    while i=1;
                }

        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Dowhile([VarDecl("i",IntType()),Break(),Return()],BinaryOp("=",Id("i"),IntLiteral(1)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,371))

    def test_simple_do_while_statement(self):
        "Test simple do while statement"
        input = """                 
            int testFunc(int a,float a[],string s){
                do{
                    int a;
                    func(1);
                    func(a);
                }while(i<0);
            }
        """
        expect = str(Program([FuncDecl(Id("testFunc"),[VarDecl("a",IntType()),VarDecl("a",ArrayPointerType(FloatType())),VarDecl("s",StringType())],IntType(),Block([Dowhile([Block([VarDecl("a",IntType()),CallExpr(Id("func"),[IntLiteral(1)]),CallExpr(Id("func"),[Id("a")])])],BinaryOp("<",Id("i"),IntLiteral(0)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,372))

    def test_complex_do_while_statement(self):
        "Test complex do while statement"
        input = """                 
            int testFunc(int a,float a[],string s){
                do{
                    int a;
                    func(1);
                    func(a);
                    if(a>3)
                        a=a+1;
                    else a=a-1;
                }while(i<0*1+3/2);
            }
        """
        expect = str(Program([FuncDecl(Id("testFunc"),[VarDecl("a",IntType()),VarDecl("a",ArrayPointerType(FloatType())),VarDecl("s",StringType())],IntType(),Block([Dowhile([Block([VarDecl("a",IntType()),CallExpr(Id("func"),[IntLiteral(1)]),CallExpr(Id("func"),[Id("a")]),If(BinaryOp(">",Id("a"),IntLiteral(3)),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),BinaryOp("=",Id("a"),BinaryOp("-",Id("a"),IntLiteral(1))))])],BinaryOp("<",Id("i"),BinaryOp("+",BinaryOp("*",IntLiteral(0),IntLiteral(1)),BinaryOp("/",IntLiteral(3),IntLiteral(2)))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,373))

    def test_more_complex_do_while_statement(self):
        "Test more complex do while statement"
        input = """                 
            int testFunc(int a,float a[],string s){
                do{
                    int a;
                    func(1);
                    func(a);
                    if(a>3)
                        {
                            for(i=1;i<2;i=i+1)
                                {
                                    int i;
                                }
                        }
                    else a=a-1;
                }while(i<0*1+3/2);
            }
        """
        expect = str(Program([FuncDecl(Id("testFunc"),[VarDecl("a",IntType()),VarDecl("a",ArrayPointerType(FloatType())),VarDecl("s",StringType())],IntType(),Block([Dowhile([Block([VarDecl("a",IntType()),CallExpr(Id("func"),[IntLiteral(1)]),CallExpr(Id("func"),[Id("a")]),If(BinaryOp(">",Id("a"),IntLiteral(3)),Block([For(BinaryOp("=",Id("i"),IntLiteral(1)),BinaryOp("<",Id("i"),IntLiteral(2)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([VarDecl("i",IntType())]))]),BinaryOp("=",Id("a"),BinaryOp("-",Id("a"),IntLiteral(1))))])],BinaryOp("<",Id("i"),BinaryOp("+",BinaryOp("*",IntLiteral(0),IntLiteral(1)),BinaryOp("/",IntLiteral(3),IntLiteral(2)))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,374))

    def test_nested_do_while_statement(self):
        "Test nested do while statement"
        input = """                 
            int testFunc(int a,float a[],string s){
                do{
                    do{
                        do i=i+1;
                        while(i<1);
                    }while(i<1);
                }while(i<0*1+3/2);
            }
        """
        expect=str(Program([FuncDecl(Id("testFunc"),[VarDecl("a",IntType()),VarDecl("a",ArrayPointerType(FloatType())),VarDecl("s",StringType())],IntType(),Block([Dowhile([Block([Dowhile([Block([Dowhile([BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))],BinaryOp("<",Id("i"),IntLiteral(1)))])],BinaryOp("<",Id("i"),IntLiteral(1)))])],BinaryOp("<",Id("i"),BinaryOp("+",BinaryOp("*",IntLiteral(0),IntLiteral(1)),BinaryOp("/",IntLiteral(3),IntLiteral(2)))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,375))

    def test_block_comment_do_while_statement(self):
        "Test block comment in do while program"
        input = """                 
            int testFunc(int a,float a[],string s){
                do{
                    /*
                        This is a block comment
                    */
                }while(i<0*1+3/2);
            }
        """
        expect = str(Program([FuncDecl(Id("testFunc"),[VarDecl("a",IntType()),VarDecl("a",ArrayPointerType(FloatType())),VarDecl("s",StringType())],IntType(),Block([Dowhile([Block([])],BinaryOp("<",Id("i"),BinaryOp("+",BinaryOp("*",IntLiteral(0),IntLiteral(1)),BinaryOp("/",IntLiteral(3),IntLiteral(2)))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,376))

    def test_line_comment_do_while_statement(self):
        "Test line comment in do while program"
        input = """                 
            int testFunc(int a,float a[],string s){
                do{
                    //This is a line comment
                }while(i<0*1+3/2);
            }
        """
        expect = str(Program([FuncDecl(Id("testFunc"),[VarDecl("a",IntType()),VarDecl("a",ArrayPointerType(FloatType())),VarDecl("s",StringType())],IntType(),Block([Dowhile([Block([])],BinaryOp("<",Id("i"),BinaryOp("+",BinaryOp("*",IntLiteral(0),IntLiteral(1)),BinaryOp("/",IntLiteral(3),IntLiteral(2)))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,377))

    def test_complex_nested_do_while(self):
        "Complex nested do while"
        input = """                 
            int main(){
                do 
                    int i;
                    do
                        a=1+5-3;
                        p[1]=2;
                        int a[7];
                        do 
                            i=1;
                        while (i<1);
                    while (i>3);
                while(i<3);
            
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Dowhile([VarDecl("i",IntType()),Dowhile([BinaryOp("=",Id("a"),BinaryOp("-",BinaryOp("+",IntLiteral(1),IntLiteral(5)),IntLiteral(3))),BinaryOp("=",ArrayCell(Id("p"),IntLiteral(1)),IntLiteral(2)),VarDecl("a",ArrayType(7,IntType())),Dowhile([BinaryOp("=",Id("i"),IntLiteral(1))],BinaryOp("<",Id("i"),IntLiteral(1)))],BinaryOp(">",Id("i"),IntLiteral(3)))],BinaryOp("<",Id("i"),IntLiteral(3)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,378))

    def test_complex_do_while_1(self):
        "Complex nested do while"
        input = """                 
            int main(){
                do
                    int i;
                    funcall(1);
                    string a[89];
                    if (i<3) 
                        do
                            int i;
                        while (a<3);
                while (a==1);
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Dowhile([VarDecl("i",IntType()),CallExpr(Id("funcall"),[IntLiteral(1)]),VarDecl("a",ArrayType(89,StringType())),If(BinaryOp("<",Id("i"),IntLiteral(3)),Dowhile([VarDecl("i",IntType())],BinaryOp("<",Id("a"),IntLiteral(3))))],BinaryOp("==",Id("a"),IntLiteral(1)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,379))

    def test_complex_do_while_2(self):
        "Complex nested do while"
        input = """                 
            int main(){
                do
                    int i;
                    funcall(1);
                    string a[89];
                    for (i=2;i==3;i=i+8-9/3){
                        if(1<3)
                            return 1;
                    }
                while (a==1);
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Dowhile([VarDecl("i",IntType()),CallExpr(Id("funcall"),[IntLiteral(1)]),VarDecl("a",ArrayType(89,StringType())),For(BinaryOp("=",Id("i"),IntLiteral(2)),BinaryOp("==",Id("i"),IntLiteral(3)),BinaryOp("=",Id("i"),BinaryOp("-",BinaryOp("+",Id("i"),IntLiteral(8)),BinaryOp("/",IntLiteral(9),IntLiteral(3)))),Block([If(BinaryOp("<",IntLiteral(1),IntLiteral(3)),Return(IntLiteral(1)))]))],BinaryOp("==",Id("a"),IntLiteral(1)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,380))

    def test_complex_do_while_3(self):
        "Complex nested do while"
        input = """                 
            int main(){
                do
                    int a[3];
                    a=(true||false)&&false||true==dalse;
                while (true||false&&(true||true));
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Dowhile([VarDecl("a",ArrayType(3,IntType())),BinaryOp("=",Id("a"),BinaryOp("||",BinaryOp("&&",BinaryOp("||",BooleanLiteral("true"),BooleanLiteral("false")),BooleanLiteral("false")),BinaryOp("==",BooleanLiteral("true"),Id("dalse"))))],BinaryOp("||",BooleanLiteral("true"),BinaryOp("&&",BooleanLiteral("false"),BinaryOp("||",BooleanLiteral("true"),BooleanLiteral("true")))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,381))

    def test_complex_do_while_4(self):
        "Complex nested do while"
        input = """                 
            int main(){
                print(1);
                punIntLn("UIAL");
                callFunc();
                do
                    string s,a[3],l[2];
                    int i;
                    i=1;
                    s="ABC"+"a45994";
                while (s!="abc");
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("print"),[IntLiteral(1)]),CallExpr(Id("punIntLn"),[StringLiteral("UIAL")]),CallExpr(Id("callFunc"),[]),Dowhile([VarDecl("s",StringType()),VarDecl("a",ArrayType(3,StringType())),VarDecl("l",ArrayType(2,StringType())),VarDecl("i",IntType()),BinaryOp("=",Id("i"),IntLiteral(1)),BinaryOp("=",Id("s"),BinaryOp("+",StringLiteral("ABC"),StringLiteral("a45994")))],BinaryOp("!=",Id("s"),StringLiteral("abc")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,382))

    def test_complex_do_while_5(self):
        "Complex nested do while"
        input = """                 
            int main(){
                print(1);
                punIntLn("UIAL");
                callFunc();
                do
                    string s,a[3],l[2];
                    int i;
                    i=1;
                    for(i="ABC";i==1;i=a+1)
                        do
                            int i;
                            string s;
                            s="ABC";
                        while (i<1);
                    s="ABC"+"a45994";
                while (s!="abc");
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("print"),[IntLiteral(1)]),CallExpr(Id("punIntLn"),[StringLiteral("UIAL")]),CallExpr(Id("callFunc"),[]),Dowhile([VarDecl("s",StringType()),VarDecl("a",ArrayType(3,StringType())),VarDecl("l",ArrayType(2,StringType())),VarDecl("i",IntType()),BinaryOp("=",Id("i"),IntLiteral(1)),For(BinaryOp("=",Id("i"),StringLiteral("ABC")),BinaryOp("==",Id("i"),IntLiteral(1)),BinaryOp("=",Id("i"),BinaryOp("+",Id("a"),IntLiteral(1))),Dowhile([VarDecl("i",IntType()),VarDecl("s",StringType()),BinaryOp("=",Id("s"),StringLiteral("ABC"))],BinaryOp("<",Id("i"),IntLiteral(1)))),BinaryOp("=",Id("s"),BinaryOp("+",StringLiteral("ABC"),StringLiteral("a45994")))],BinaryOp("!=",Id("s"),StringLiteral("abc")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,383))

    def test_complex_if_else_statement_1(self):
        "Complex if else statement"
        input = """                 
            int main(){
                if(1>2==3<4)
                {
                    for(i=2;i>4;i=i+69854){
                        int i;
                        int a;
                        float b;
                        string b;
                        boolean b;
                        b=true||false&&true||(true||false);
                    }
                }
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp("==",BinaryOp(">",IntLiteral(1),IntLiteral(2)),BinaryOp("<",IntLiteral(3),IntLiteral(4))),Block([For(BinaryOp("=",Id("i"),IntLiteral(2)),BinaryOp(">",Id("i"),IntLiteral(4)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(69854))),Block([VarDecl("i",IntType()),VarDecl("a",IntType()),VarDecl("b",FloatType()),VarDecl("b",StringType()),VarDecl("b",BoolType()),BinaryOp("=",Id("b"),BinaryOp("||",BinaryOp("||",BooleanLiteral("true"),BinaryOp("&&",BooleanLiteral("false"),BooleanLiteral("true"))),BinaryOp("||",BooleanLiteral("true"),BooleanLiteral("false"))))]))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,384))

    def test_complex_if_else_statement_2(self):
        "Complex if else statement"
        input = """                 
                int main(){
                    if(1>2==3<4)
                    {
                        putLin(i==2||true&&false<3>4);
                        int i;
                        float g;
                        g=2.0e-96;
                    } else break;
                }
                """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp("==",BinaryOp(">",IntLiteral(1),IntLiteral(2)),BinaryOp("<",IntLiteral(3),IntLiteral(4))),Block([CallExpr(Id("putLin"),[BinaryOp("||",BinaryOp("==",Id("i"),IntLiteral(2)),BinaryOp("&&",BooleanLiteral("true"),BinaryOp(">",BinaryOp("<",BooleanLiteral("false"),IntLiteral(3)),IntLiteral(4))))]),VarDecl("i",IntType()),VarDecl("g",FloatType()),BinaryOp("=",Id("g"),FloatLiteral(2e-96))]),Break())]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,385))

    def test_complex_if_else_statement_3(self):
        "Complex if else statement"
        input = """                 
                int main(){
                    if(1>2==3<4)
                    {
                        int k;
                        int a[6];
                        do
                            int i;
                            float b;
                            boolean rf;
                            put(i);
                            put(abc);
                        while (i==3);
                    } else break;
                }
                """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp("==",BinaryOp(">",IntLiteral(1),IntLiteral(2)),BinaryOp("<",IntLiteral(3),IntLiteral(4))),Block([VarDecl("k",IntType()),VarDecl("a",ArrayType(6,IntType())),Dowhile([VarDecl("i",IntType()),VarDecl("b",FloatType()),VarDecl("rf",BoolType()),CallExpr(Id("put"),[Id("i")]),CallExpr(Id("put"),[Id("abc")])],BinaryOp("==",Id("i"),IntLiteral(3)))]),Break())]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,386))

    def test_complex_if_else_statement_4(self):
        "Complex if else statement"
        input = """                 
                void main(){
                    if(put(i))
                        int i;
                    else{
                        put(i+3);
                        int g;
                        float h;
                        return 3;
                    }
                }
                """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([If(CallExpr(Id("put"),[Id("i")]),VarDecl("i",IntType()),Block([CallExpr(Id("put"),[BinaryOp("+",Id("i"),IntLiteral(3))]),VarDecl("g",IntType()),VarDecl("h",FloatType()),Return(IntLiteral(3))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,387))

    def test_complex_if_else_statement_5(self):
        "Complex if else statement"
        input = """                 
                void main(){
                    if(put(i))
                        int i;
                    else{
                        if(putLin(89==3)){
                            int i;
                        }else{
                            do int k;
                            float f;
                            f=f+1;
                            while(true);
                        }
                    }
                }
                """

        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([If(CallExpr(Id("put"),[Id("i")]),VarDecl("i",IntType()),Block([If(CallExpr(Id("putLin"),[BinaryOp("==",IntLiteral(89),IntLiteral(3))]),Block([VarDecl("i",IntType())]),Block([Dowhile([VarDecl("k",IntType()),VarDecl("f",FloatType()),BinaryOp("=",Id("f"),BinaryOp("+",Id("f"),IntLiteral(1)))],BooleanLiteral("true"))]))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,388))

    def test_complex_for_statement_1(self):
        "Complex for statement"
        input = """                 
                void main(){
                    for(j=1;j!=2==3;putlin(1))
                        int i;
                }
                """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([For(BinaryOp("=",Id("j"),IntLiteral(1)),BinaryOp("==",BinaryOp("!=",Id("j"),IntLiteral(2)),IntLiteral(3)),CallExpr(Id("putlin"),[IntLiteral(1)]),VarDecl("i",IntType()))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,389))

    def test_complex_for_statement_2(self):
        "Complex for statement"
        input = """                 
                    void main(){
                        for(i=2;i==3<4>5;i=u+3-1/2%4){
                            int i;
                            float f;
                            a[4]=5;
                            do
                                int i;
                                float f;
                                g==true;
                            while(g!=false);
                        }
                    }
                    """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(2)),BinaryOp("==",Id("i"),BinaryOp(">",BinaryOp("<",IntLiteral(3),IntLiteral(4)),IntLiteral(5))),BinaryOp("=",Id("i"),BinaryOp("-",BinaryOp("+",Id("u"),IntLiteral(3)),BinaryOp("%",BinaryOp("/",IntLiteral(1),IntLiteral(2)),IntLiteral(4)))),Block([VarDecl("i",IntType()),VarDecl("f",FloatType()),BinaryOp("=",ArrayCell(Id("a"),IntLiteral(4)),IntLiteral(5)),Dowhile([VarDecl("i",IntType()),VarDecl("f",FloatType()),BinaryOp("==",Id("g"),BooleanLiteral("true"))],BinaryOp("!=",Id("g"),BooleanLiteral("false")))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,390))

    def test_complex_for_statement_3(self):
        "Complex for statement"
        input = """                 
                    void main(){
                        for(i=2;i==3<4>5;i=u+3-1/2%4){
                            for (k=3;punt(i);i+i+1)
                                for(j=8-9*6+3/1;putLine(1);i=i+2312341)
                                    if(true)
                                        return false;
                                    else continue;
                        }
                    }
                    """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(2)),BinaryOp("==",Id("i"),BinaryOp(">",BinaryOp("<",IntLiteral(3),IntLiteral(4)),IntLiteral(5))),BinaryOp("=",Id("i"),BinaryOp("-",BinaryOp("+",Id("u"),IntLiteral(3)),BinaryOp("%",BinaryOp("/",IntLiteral(1),IntLiteral(2)),IntLiteral(4)))),Block([For(BinaryOp("=",Id("k"),IntLiteral(3)),CallExpr(Id("punt"),[Id("i")]),BinaryOp("+",BinaryOp("+",Id("i"),Id("i")),IntLiteral(1)),For(BinaryOp("=",Id("j"),BinaryOp("+",BinaryOp("-",IntLiteral(8),BinaryOp("*",IntLiteral(9),IntLiteral(6))),BinaryOp("/",IntLiteral(3),IntLiteral(1)))),CallExpr(Id("putLine"),[IntLiteral(1)]),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(2312341))),If(BooleanLiteral("true"),Return(BooleanLiteral("false")),Continue())))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,391))

    def test_complex_for_statement_4(self):
        "Complex for statement"
        input = """                 
                    void main(){
                        for(putLine(i*3+1-2);put(i);i+put(ioop))
                            putline(1);
                        for(i=3;put(i);i+put(ioop))
                            continue;                        
                    }
                    """
        expect =str(Program([FuncDecl(Id("main"),[],VoidType(),Block([For(CallExpr(Id("putLine"),[BinaryOp("-",BinaryOp("+",BinaryOp("*",Id("i"),IntLiteral(3)),IntLiteral(1)),IntLiteral(2))]),CallExpr(Id("put"),[Id("i")]),BinaryOp("+",Id("i"),CallExpr(Id("put"),[Id("ioop")])),CallExpr(Id("putline"),[IntLiteral(1)])),For(BinaryOp("=",Id("i"),IntLiteral(3)),CallExpr(Id("put"),[Id("i")]),BinaryOp("+",Id("i"),CallExpr(Id("put"),[Id("ioop")])),Continue())]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,392))

    def test_complex_for_statement_5(self):
        "Complex for statement"
        input = """                 
                    void main(){
                        for(putLine(i*3+1-2);put(i);i+put(ioop))
                            putline(1);
                        for(i=3;put(i);i+put(ioop))
                            continue;                        
                    }
                    """
        expect =str(Program([FuncDecl(Id("main"),[],VoidType(),Block([For(CallExpr(Id("putLine"),[BinaryOp("-",BinaryOp("+",BinaryOp("*",Id("i"),IntLiteral(3)),IntLiteral(1)),IntLiteral(2))]),CallExpr(Id("put"),[Id("i")]),BinaryOp("+",Id("i"),CallExpr(Id("put"),[Id("ioop")])),CallExpr(Id("putline"),[IntLiteral(1)])),For(BinaryOp("=",Id("i"),IntLiteral(3)),CallExpr(Id("put"),[Id("i")]),BinaryOp("+",Id("i"),CallExpr(Id("put"),[Id("ioop")])),Continue())]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,392))

    def test_complex_for_statement_6(self):
        "Complex if else statement"
        input = """                 
                    void main(){
                        for(putLine(i*3+1-2);put(i);i+put(ioop))
                        {
                            for(i=2;i<3;i=i+1){
                                do
                                    if(i<3)
                                        return 3;
                                while(putLine(1));
                            }
                        }
                 
                    }
                    """
        expect =str(Program([FuncDecl(Id("main"),[],VoidType(),Block([For(CallExpr(Id("putLine"),[BinaryOp("-",BinaryOp("+",BinaryOp("*",Id("i"),IntLiteral(3)),IntLiteral(1)),IntLiteral(2))]),CallExpr(Id("put"),[Id("i")]),BinaryOp("+",Id("i"),CallExpr(Id("put"),[Id("ioop")])),Block([For(BinaryOp("=",Id("i"),IntLiteral(2)),BinaryOp("<",Id("i"),IntLiteral(3)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([Dowhile([If(BinaryOp("<",Id("i"),IntLiteral(3)),Return(IntLiteral(3)))],CallExpr(Id("putLine"),[IntLiteral(1)]))]))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,393))

    def test_complete_program_1(self):
        "Complete program"
        input = """
            int main(){
                do {
                for(i =0; i < 22; i = i + 1)
                    c = c + c*i;
                }
                while( c < 1000000);
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Dowhile([Block([For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),IntLiteral(22)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),BinaryOp("=",Id("c"),BinaryOp("+",Id("c"),BinaryOp("*",Id("c"),Id("i")))))])],BinaryOp("<",Id("c"),IntLiteral(1000000)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,394))

    def test_complete_program_2(self):
        "Complete Program"
        input = """
            float foo(int a) {
                a = 0;
                int i ;
            do {
                for (i = 0; i <=99999999 ; i = i + 1)
                    a = a + a*i;
            }
            while (a < 99999);
            return 2;
            }
            int main(){
                string x;
                x = foo(x);
            }
        """
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl("a",IntType())],FloatType(),Block([BinaryOp("=",Id("a"),IntLiteral(0)),VarDecl("i",IntType()),Dowhile([Block([For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<=",Id("i"),IntLiteral(99999999)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),BinaryOp("*",Id("a"),Id("i")))))])],BinaryOp("<",Id("a"),IntLiteral(99999))),Return(IntLiteral(2))])),FuncDecl(Id("main"),[],IntType(),Block([VarDecl("x",StringType()),BinaryOp("=",Id("x"),CallExpr(Id("foo"),[Id("x")]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,395))

    def test_comple_program_3(self):
        "Complete program"
        input = """
            int x;
            int y;
            int z;
            void tbp(int a, int b, int c){
                c = a*b*c*x*y*z;
                return c;
            }
            void main(){
                tbp(x,y,z);
                //almost done
            }
        """
        expect = str(Program([VarDecl("x",IntType()),VarDecl("y",IntType()),VarDecl("z",IntType()),FuncDecl(Id("tbp"),[VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType())],VoidType(),Block([BinaryOp("=",Id("c"),BinaryOp("*",BinaryOp("*",BinaryOp("*",BinaryOp("*",BinaryOp("*",Id("a"),Id("b")),Id("c")),Id("x")),Id("y")),Id("z"))),Return(Id("c"))])),FuncDecl(Id("main"),[],VoidType(),Block([CallExpr(Id("tbp"),[Id("x"),Id("y"),Id("z")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,396))

    def test_complete_program_4(self):
        input = """
            void foo(){}
            float foo2(){
                foo();
                foo2();
            }

        """
        expect = str(Program([FuncDecl(Id("foo"),[],VoidType(),Block([])),FuncDecl(Id("foo2"),[],FloatType(),Block([CallExpr(Id("foo"),[]),CallExpr(Id("foo2"),[])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,397))

    def test_complete_program_5(self):
        input = """
            int main(){}
            int test(float b,int a[],string s){}
            int[] test1(int j,string s){
                string s;
                s="OPIUH9";
                ///line comment
                /*
                    block comment
                */
                for (i=1;i<2;i=i+1)
                    return i*2+1;
            }

        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([])),FuncDecl(Id("test"),[VarDecl("b",FloatType()),VarDecl("a",ArrayPointerType(IntType())),VarDecl("s",StringType())],IntType(),Block([])),FuncDecl(Id("test1"),[VarDecl("j",IntType()),VarDecl("s",StringType())],ArrayPointerType(IntType()),Block([VarDecl("s",StringType()),BinaryOp("=",Id("s"),StringLiteral("OPIUH9")),For(BinaryOp("=",Id("i"),IntLiteral(1)),BinaryOp("<",Id("i"),IntLiteral(2)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Return(BinaryOp("+",BinaryOp("*",Id("i"),IntLiteral(2)),IntLiteral(1))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,398))

    def test_complete_program_6(self):
        input = """
            int main(){
                int i;
                i=input();
                print(giaiThua(i));
            }
            
            int giaiThua(int i){
                if(i==1) return 1;
                return giaithua(i-1)*i;
            }
            

        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("i",IntType()),BinaryOp("=",Id("i"),CallExpr(Id("input"),[])),CallExpr(Id("print"),[CallExpr(Id("giaiThua"),[Id("i")])])])),FuncDecl(Id("giaiThua"),[VarDecl("i",IntType())],IntType(),Block([If(BinaryOp("==",Id("i"),IntLiteral(1)),Return(IntLiteral(1))),Return(BinaryOp("*",CallExpr(Id("giaithua"),[BinaryOp("-",Id("i"),IntLiteral(1))]),Id("i")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,399))
















