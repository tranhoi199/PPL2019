import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):

    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """int main() {}"""
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
    def test_vardecl(self):
        """Simple program: int main() {} """
        input = """int a;"""
        expect = str(Program([VarDecl(Id("a"),IntType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,303))
    def test_vardecl1(self):
        """Simple program: int main() {} """
        input = """int a,b;
            """
        expect = str(Program([VarDecl(Id('a'),IntType()),VarDecl(Id('b'),IntType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,304))
    def test_vardecl2(self):
        """Simple program: int main() {} """
        input = """int c[10];
            """
        expect = str(Program([VarDecl(Id('c'),ArrayType(10,IntType()))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,305))
    def test_vardecl3(self):
        """Simple program: int main() {} """
        input = """int a,c[10];
            """
        expect = str(Program([VarDecl(Id('a'),IntType()),VarDecl(Id('c'),ArrayType(10,IntType()))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,306))
    def test_vardecl4(self):
        """Simple program: int main() {} """
        input = """float a,c[10];
            """
        expect = str(Program([VarDecl(Id('a'),FloatType()),VarDecl(Id('c'),ArrayType(10,FloatType()))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,307))
    def test_vardecl5(self):
        """Simple program: int main() {} """
        input = """string a,c[10];
            """
        expect = str(Program([VarDecl(Id('a'),StringType()),VarDecl(Id('c'),ArrayType(10,StringType()))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,308))
    def test_vardecl6(self):
        """Simple program: int main() {} """
        input = """boolean a,c[10];
            """
        expect = str(Program([VarDecl(Id('a'),BoolType()),VarDecl(Id('c'),ArrayType(10,BoolType()))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,309))
    def test_vardecl7(self):
        """Simple program: int main() {} """
        input = """boolean a,c[10]; int a,b;string c[10];
            """
        expect = str(Program([VarDecl(Id('a'),BoolType()),VarDecl(Id('c'),ArrayType(BoolType(),10)),VarDecl(Id('a'),IntType),VarDecl(Id('b'),IntType),VarDecl(Id('c'),ArrayType(StringType(),10))]))
    
    def test_funcdec(self):
        """Simple program: int main() {} """
        input = """int main() {int a;}"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl(Id('a'),IntType())]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,311))
    def test_funcdec1(self):
       """Simple program: int main() {} """
       input = """int[] main() {}"""
       expect = str(Program([FuncDecl(Id('main'),[],ArrayPointerType(IntType()),Block([]))]))
       self.assertTrue(TestAST.checkASTGen(input,expect,312))
    def test_funcdec2(self):
       """Simple program: int main() {} """
       input = """
           int abc[10];
           int[] main(int a, int b) {}"""
       expect = str(Program([VarDecl(Id('abc'),ArrayType(10,IntType())),FuncDecl(Id('main'),[VarDecl(Id('a'),IntType),VarDecl(Id('b'),IntType)],ArrayPointerType(IntType),Block([]))]))
    def test_funcdec3(self):
        """Simple program: int main() {} """
        input = """
           
           int main(int a, int b) {
               
           }"""
        expect = str(Program([FuncDecl(Id('main'),[VarDecl(Id('a'),IntType()),VarDecl(Id('b'),IntType())],IntType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,315))
    def test_funcdec4(self):
        """Simple program: int main() {} """
        input = """
           
           int main(int a, boolean b[]) {
               
           }"""
        expect = str(Program([FuncDecl(Id('main'),[VarDecl(Id('a'),IntType()),VarDecl(Id('b'),ArrayPointerType(BoolType()))],IntType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,316))
    def test_funcdec5(self):
        """Simple program: int main() {} """
        input = """
           
           int main() {
               
               a = 1;
               
               
           }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([BinaryOp('=',Id('a'),IntLiteral(1))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,317))
    def test_funcdec6(self):
        """Simple program: int main() {} """
        input = """
           
           int main() {
               
               a = 1;
               a < 1;
               
           }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([BinaryOp("=",Id('a'),IntLiteral(1)),BinaryOp("<",Id("a"),IntLiteral(1))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,314))
    def test_exp(self):
        """Simple program: int main() {} """
        input = """
           
           int main() {
               
               a || 1;
               
               
           }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([BinaryOp("||",Id("a"),IntLiteral(1))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,318))
    def test_exp1(self):
        """Simple program: int main() {} """
        input = """
           
           int main() {
               
               a && 1;
               
           }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([BinaryOp("&&",Id("a"),IntLiteral(1))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,319))
    def test_exp2(self):
        """Simple program: int main() {} """
        input = """
           
           int main() {
               
               a != 1;
               
           }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([BinaryOp("!=",Id("a"),IntLiteral(1))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,320))
    def test_exp2(self):
        """Simple program: int main() {} """
        input = """
           
           int main() {
               
               a == 1;
               
           }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([BinaryOp("==",Id("a"),IntLiteral(1))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,320))
    def test_exp3(self):
        """Simple program: int main() {} """
        input = """
           
           int main() {
               
               a < 1;
               
           }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([BinaryOp("<",Id("a"),IntLiteral(1))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,321))
    def test_exp4(self):
        """Simple program: int main() {} """
        input = """
           
           int main() {
               
               a <= 1;
               
           }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([BinaryOp("<=",Id("a"),IntLiteral(1))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,322))
    def test_exp5(self):
        """Simple program: int main() {} """
        input = """
           
           int main() {
               
               a >= 1;
               
           }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([BinaryOp(">=",Id("a"),IntLiteral(1))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,323))
    def test_exp6(self):
        """Simple program: int main() {} """
        input = """
           
           int main() {
               
               a + 1;
               
           }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([BinaryOp("+",Id("a"),IntLiteral(1))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,324))
    def test_exp7(self):
        """Simple program: int main() {} """
        input = """
           
           int main() {
               
               a - 1;
               
           }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([BinaryOp("-",Id("a"),IntLiteral(1))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,325))
    def test_exp8(self):
        """Simple program: int main() {} """
        input = """
           
           int main() {
               
               a * 1;
               
           }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([BinaryOp("*",Id("a"),IntLiteral(1))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,326))
    def test_exp9(self):
        """Simple program: int main() {} """
        input = """
           
           int main() {
               
               a % 1;
               
           }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([BinaryOp("%",Id("a"),IntLiteral(1))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,327))
    def test_exp10(self):
        """Simple program: int main() {} """
        input = """
           
           int main() {
               
               !a;
               
           }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([UnaryOp("!",Id("a"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,328))
    def test_exp11(self):
        """Simple program: int main() {} """
        input = """
           
           int main() {
               
               -a;
               
           }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([UnaryOp("-",Id("a"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,329))
    def test_exp12(self):
        """Simple program: int main() {} """
        input = """
           
           int main() {
               
               a[12];
               
           }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([ArrayCell(Id('a'),IntLiteral(12))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,330))
    def test_exp13(self):
        """Simple program: int main() {} """
        input = """
           
           int main() {
               
               foo()[12];
               
           }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([ArrayCell(CallExpr(Id('foo'),[]),IntLiteral(12))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,331))
    def test_exp14(self):
        """Simple program: int main() {} """
        input = """
           
           int main() {
               
               (foo()[12]);
               
           }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([ArrayCell(CallExpr(Id('foo'),[]),IntLiteral(12))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,332))
    def test_exp15(self):
        """Simple program: int main() {} """
        input = """
           
           int main() {
               
               foo(a,b,cd);
               
           }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([CallExpr(Id('foo'),[Id("a"),Id("b"),Id("cd")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,333))
    def test_exp16(self):
        """Simple program: int main() {} """
        input = """
           
           int main() {
               
               foo(a,b,cd[10]);
               
           }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([CallExpr(Id('foo'),[Id("a"),Id("b"),ArrayCell(Id("cd"),IntLiteral(10))])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,334))
    def test_exp17(self):
        """Simple program: int main() {} """
        input = """
           
           int main() {
               
               -a = b + 1  <= c;
               
           }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([BinaryOp("=",UnaryOp("-",Id('a')),BinaryOp("<=",BinaryOp("+",Id("b"),IntLiteral(1)),Id("c")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,335))
    def test_exp18(self):
        """Simple program: int main() {} """
        input = """
           
           int main() {
               
               -a = b + 1  % c;
               
           }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([BinaryOp("=",UnaryOp("-",Id("a")),BinaryOp("+",Id("b"),BinaryOp("%",IntLiteral("1"),Id("c"))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,336))
    def test_exp19(self):
        """Simple program: int main() {} """
        input = """
           
           int main() {
               
               -a = b + 1  % c * (b+c);
               
           }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",UnaryOp("-",Id("a")),BinaryOp("+",Id("b"),BinaryOp("*",BinaryOp("%",IntLiteral(1),Id("c")),BinaryOp("+",Id("b"),Id("c")))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,337))
    def test_stmt(self):
        """Simple program: int main() {} """
        input = """
        
           int main() {
               
            if(a == 1)

                a = a+1;
               
           }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp("==",Id("a"),IntLiteral(1)),BinaryOp("=",Id('a'),BinaryOp('+',Id('a'),IntLiteral(1))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,338))
    def test_stmt_if(self):
        """Simple program: int main() {} """
        input = """
        
           int main() {
               
            if(a == 1){
                
                a = a+1;
            }
               
           }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp("==",Id("a"),IntLiteral(1)),Block([BinaryOp("=",Id('a'),BinaryOp("+",Id("a"),IntLiteral(1)))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,339))
    def test_stmt_do_while(self):
        """Simple program: int main() {} """
        input = """
        
           int main() {
               
            do A = A+1;
             while a < 1;
               
           }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([Dowhile([BinaryOp('=',Id('A'),BinaryOp('+',Id('A'),IntLiteral(1)))],BinaryOp('<',Id('a'),IntLiteral(1)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,340))
    def test_stmt_do_while1(self):
        """Simple program: int main() {} """
        input = """
        
           int main() {
               
            do {A = A+1;
            }
             while a < 1;
               
           }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([Dowhile([Block([BinaryOp('=',Id('A'),BinaryOp('+',Id('A'),IntLiteral(1)))])],BinaryOp('<',Id('a'),IntLiteral(1)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,341))
    def test_stmt_do_while2(self):
        """Simple program: int main() {} """
        input = """
        
           int main() {
               
            do {A = A+1;
            foo(3,4);
            }
             while a < 1;
               
           }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([Dowhile([Block([BinaryOp('=',Id('A'),BinaryOp('+',Id('A'),IntLiteral(1))),CallExpr(Id('foo'),[IntLiteral(3),IntLiteral(4)])])],BinaryOp('<',Id('a'),IntLiteral(1)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,342))
    def test_stmt_for(self):
        """Simple program: int main() {} """
        input = """
        
           int main() {
               
            for(i=0; i < n; i=i+1)

                b = b*2;
               
           }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([For(BinaryOp('=',Id('i'),IntLiteral(0)),BinaryOp('<',Id('i'),Id('n')),BinaryOp('=',Id('i'),BinaryOp('+',Id('i'),IntLiteral(1))),BinaryOp('=',Id('b'),BinaryOp('*',Id('b'),IntLiteral(2))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,343))

    def test_stmt_for1(self):
        """Simple program: int main() {} """
        input = """
        
           int main() {
               
            for(i=0; i < n; i=i+1){

                b = b*2;
                }

            
               
           }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([For(BinaryOp('=',Id('i'),IntLiteral(0)),BinaryOp('<',Id('i'),Id('n')),BinaryOp('=',Id('i'),BinaryOp('+',Id('i'),IntLiteral(1))),Block([BinaryOp('=',Id('b'),BinaryOp('*',Id('b'),IntLiteral(2)))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,344))
    def test_stmt_break(self):
        """Simple program: int main() {} """
        input = """
        
           int main() {
               
            break;

            
               
           }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([Break()]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,345))
    def test_stmt_continue(self):
        """Simple program: int main() {} """
        input = """
        
           int main() {
               
            continue;

            
               
           }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([Continue()]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,346))
    def test_stmt_return(self):
        """Simple program: int main() {} """
        input = """
        
           int main() {
               
            return;

            
               
           }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([Return()]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,347))
    def test_stmt_return1(self):
        """Simple program: int main() {} """
        input = """
        
           int main() {
               
            return(1);
               
           }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([Return(IntLiteral(1))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,348))
    def test_more(self):
        """Simple program: int main() {} """
        input = """
        
           int main() {
        
               a = 1.2e10;
               
           }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([BinaryOp('=',Id('a'),FloatLiteral(12000000000.0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,349))
    def test_more1(self):
        """Simple program: int main() {} """
        input = """
        
           int main() {
        
               a = 1.2e-10;
               
           }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([BinaryOp('=',Id('a'),FloatLiteral(1.2e-10))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,350))
    def test_more2(self):
        """Simple program: int main() {} """
        input = """
        
           int main() {
        
               a = 1.23e2;
               
           }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([BinaryOp('=',Id('a'),FloatLiteral(123.0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,351))
    def test_more3(self):
        """Simple program: int main() {} """
        input = """
        
           int main() {
        
               a = 1.23E2;
               
           }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([BinaryOp('=',Id('a'),FloatLiteral(123.0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,352))
    def test_more4(self):
        """Simple program: int main() {} """
        input = """
        
           int main() {
        
               a = "abcskd\\n";
               
           }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([BinaryOp('=',Id('a'),StringLiteral("abcskd\\n"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,353))
    def test_more5(self):
        """Simple program: int main() {} """
        input = """
        
           float a,d,e;
            string b;
            boolean c;
            
            void main() {
            }"""
        expect = str(Program([VarDecl(Id('a'),FloatType()),VarDecl(Id('d'),FloatType()),VarDecl(Id('e'),FloatType()),VarDecl(Id('b'),StringType()),VarDecl(Id('c'),BoolType()),FuncDecl(Id('main'),[],VoidType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,354))
    def test_more6(self):
        """Simple program: int main() {} """
        input = """int main(){
            
            a = 10;
            return 1;
            }
            """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([BinaryOp('=',Id('a'),IntLiteral(10)),Return(IntLiteral(1))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,355))
    def test_more7(self):
        """Simple program: int main() {} """
        input = """int main(){
            int a;
            a = 10;
            return 1;
            }
            """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl(Id('a'),IntType()),BinaryOp('=',Id('a'),IntLiteral(10)),Return(IntLiteral(1))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,356))

    def test_more8(self):
        """Simple program: int main() {} """
        input = """int main(){
            int a,b;
            a = 10;
            return 1;
            }
            """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl(Id('a'),IntType()),VarDecl(Id('b'),IntType()),BinaryOp('=',Id('a'),IntLiteral(10)),Return(IntLiteral(1))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,357))
    def test_more9(self):
        """Simple program: int main() {} """
        input = """int main(){
            int a,b,c[10];
            a = 10;
            return 1;
            }
            """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl(Id('a'),IntType()),VarDecl(Id('b'),IntType()),VarDecl(Id("c"),ArrayType(10,IntType())),BinaryOp('=',Id('a'),IntLiteral(10)),Return(IntLiteral(1))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,358))
    def test_more10(self):
        """Simple program: int main() {} """
        input = """int main(){
            int a,b,c, d[10];
            a = a-10+9*8;
            return 1;
            }
            """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl(Id('a'),IntType()),VarDecl(Id('b'),IntType()),VarDecl(Id('c'),IntType()),VarDecl(Id('d'),ArrayType(10,IntType())),BinaryOp('=',Id('a'),BinaryOp('+',BinaryOp('-',Id('a'),IntLiteral(10)),BinaryOp('*',IntLiteral(9),IntLiteral(8)))),Return(IntLiteral(1))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,359))
    def test_more11(self):
        """Simple program: int main() {} """
        input = """int main(){
            int a,b,c, d[10],e[9];
            a = a-10+9*8;
            d[0] = d[10] - e[9] - foo();
            return 1;
            }
            """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl(Id('a'),IntType()),VarDecl(Id('b'),IntType()),VarDecl(Id('c'),IntType()),VarDecl(Id('d'),ArrayType(10,IntType())),VarDecl(Id('e'),ArrayType(9,IntType())),BinaryOp('=',Id('a'),BinaryOp('+',BinaryOp('-',Id('a'),IntLiteral(10)),BinaryOp('*',IntLiteral(9),IntLiteral(8)))),BinaryOp('=',ArrayCell(Id('d'),IntLiteral(0)),BinaryOp('-',BinaryOp('-',ArrayCell(Id('d'),IntLiteral(10)),ArrayCell(Id('e'),IntLiteral(9))),CallExpr(Id('foo'),[]))),Return(IntLiteral(1))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,360))
    def test_more12(self):
        """Simple program: int main() {} """
        input = """int main(){
            int a,b,c, d[10];
            a = a-10+9*8;
            if(a <= 1)
              a = 1;
            return 1;
            }
            """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl(Id('a'),IntType()),VarDecl(Id('b'),IntType()),VarDecl(Id('c'),IntType()),VarDecl(Id('d'),ArrayType(10,IntType())),BinaryOp('=',Id('a'),BinaryOp('+',BinaryOp('-',Id('a'),IntLiteral(10)),BinaryOp('*',IntLiteral(9),IntLiteral(8)))),If(BinaryOp('<=',Id('a'),IntLiteral(1)),BinaryOp('=',Id('a'),IntLiteral(1))),Return(IntLiteral(1))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,361))
    def test_more13(self):
        """Simple program: int main() {} """
        input = """int main(){
            int a,b,c, d[10];
            a = a-10+9*8;
            if(a <= 1){
            a = 1;
            }
            return 1;
            }
            """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl(Id('a'),IntType()),VarDecl(Id('b'),IntType()),VarDecl(Id('c'),IntType()),VarDecl(Id('d'),ArrayType(10,IntType())),BinaryOp('=',Id('a'),BinaryOp('+',BinaryOp('-',Id('a'),IntLiteral(10)),BinaryOp('*',IntLiteral(9),IntLiteral(8)))),If(BinaryOp('<=',Id('a'),IntLiteral(1)),Block([BinaryOp('=',Id('a'),IntLiteral(1))])),Return(IntLiteral(1))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,362))
    def test_more14(self):
        """Simple program: int main() {} """
        input = """int main(){
            int a,b,c, d[10];
            a = a-10+9*8;
            if(a <= 1){
            a = 1;
                {
                b =10;
                for(i=1;i> 10; i=1+2)
                a = c;
                }
            }
            return 1;
            }
            """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl(Id('a'),IntType()),VarDecl(Id('b'),IntType()),VarDecl(Id('c'),IntType()),VarDecl(Id('d'),ArrayType(10,IntType())),BinaryOp('=',Id('a'),BinaryOp('+',BinaryOp('-',Id('a'),IntLiteral(10)),BinaryOp('*',IntLiteral(9),IntLiteral(8)))),If(BinaryOp('<=',Id('a'),IntLiteral(1)),Block([BinaryOp('=',Id('a'),IntLiteral(1)),Block([BinaryOp('=',Id('b'),IntLiteral(10)),For(BinaryOp('=',Id('i'),IntLiteral(1)),BinaryOp('>',Id('i'),IntLiteral(10)),BinaryOp('=',Id('i'),BinaryOp('+',IntLiteral(1),IntLiteral(2))),BinaryOp('=',Id('a'),Id('c')))])])),Return(IntLiteral(1))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,363))
    def test_more15(self):
        """Simple program: int main() {} """
        input = """
            boolean k[10];
            int main(){
            int a,b,c, d[10];
            a = a-10+9*8;
            do{
            }while(a<3);
            a =1;
            return 1;
            }
            """
        expect = str(Program([VarDecl(Id('k'),ArrayType(10,BoolType())),FuncDecl(Id('main'),[],IntType(),Block([VarDecl(Id('a'),IntType()),VarDecl(Id('b'),IntType()),VarDecl(Id('c'),IntType()),VarDecl(Id('d'),ArrayType(10,IntType())),BinaryOp('=',Id('a'),BinaryOp('+',BinaryOp('-',Id('a'),IntLiteral(10)),BinaryOp('*',IntLiteral(9),IntLiteral(8)))),Dowhile([Block([])],BinaryOp('<',Id('a'),IntLiteral(3))),BinaryOp('=',Id('a'),IntLiteral(1)),Return(IntLiteral(1))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,364))
    def test_more16(self):
        """Simple program: int main() {} """
        input = """
            boolean khoa(int a, int b){
            
            return a && b;
            }
            int main(){
            int a,b,c, d[10];
            a = a-10+9*8;
            do{
            
            }while(a<3);
            a =1;
            return 1;
            }
            """
        expect = str(Program([FuncDecl(Id('khoa'),[VarDecl(Id('a'),IntType()),VarDecl(Id('b'),IntType())],BoolType(),Block([Return(BinaryOp('&&',Id('a'),Id('b')))])),FuncDecl(Id('main'),[],IntType(),Block([VarDecl(Id('a'),IntType()),VarDecl(Id('b'),IntType()),VarDecl(Id('c'),IntType()),VarDecl(Id('d'),ArrayType(10,IntType())),BinaryOp('=',Id('a'),BinaryOp('+',BinaryOp('-',Id('a'),IntLiteral(10)),BinaryOp('*',IntLiteral(9),IntLiteral(8)))),Dowhile([Block([])],BinaryOp('<',Id('a'),IntLiteral(3))),BinaryOp('=',Id('a'),IntLiteral(1)),Return(IntLiteral(1))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,365))
    def test_more17(self):
        """Simple program: int main() {} """
        input = """
            boolean khoa(int a, int b){
            int c ;
            return A && B;
            }
            int main(){
            int a,b,c, d[10];
            a = a-10+9*8;
            do{
            
            }while(a<3);
            a =1;
            return 1;
            }
            """
        expect = str(Program([FuncDecl(Id('khoa'),[VarDecl(Id('a'),IntType()),VarDecl(Id('b'),IntType())],BoolType(),Block([VarDecl(Id('c'),IntType()),Return(BinaryOp('&&',Id('A'),Id('B')))])),FuncDecl(Id('main'),[],IntType(),Block([VarDecl(Id('a'),IntType()),VarDecl(Id('b'),IntType()),VarDecl(Id('c'),IntType()),VarDecl(Id('d'),ArrayType(10,IntType())),BinaryOp('=',Id('a'),BinaryOp('+',BinaryOp('-',Id('a'),IntLiteral(10)),BinaryOp('*',IntLiteral(9),IntLiteral(8)))),Dowhile([Block([])],BinaryOp('<',Id('a'),IntLiteral(3))),BinaryOp('=',Id('a'),IntLiteral(1)),Return(IntLiteral(1))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,366))
    def test_more18(self):
        """Simple program: int main() {} """
        input = """int main() {
            int a,b,c;
            a = a*c;
            a == b;
            
            }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl(Id('a'),IntType()),VarDecl(Id('b'),IntType()),VarDecl(Id('c'),IntType()),BinaryOp('=',Id('a'),BinaryOp('*',Id('a'),Id('c'))),BinaryOp('==',Id('a'),Id('b'))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,367))
    def test_more19(self):
        """Simple program: int main() {} """
        input = """int main() {
            int a,b,c;
            a = a*c;
            !b;
            
            }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl(Id('a'),IntType()),VarDecl(Id('b'),IntType()),VarDecl(Id('c'),IntType()),BinaryOp('=',Id('a'),BinaryOp('*',Id('a'),Id('c'))),UnaryOp('!',Id('b'))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,368))
    def test_more20(self):
        """Simple program: int main() {} """
        input = """int main() {
            int a,b,c;
            a = a*c;
            b = a || b && c - d;
            
            }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl(Id('a'),IntType()),VarDecl(Id('b'),IntType()),VarDecl(Id('c'),IntType()),BinaryOp('=',Id('a'),BinaryOp('*',Id('a'),Id('c'))),BinaryOp('=',Id('b'),BinaryOp('||',Id('a'),BinaryOp('&&',Id('b'),BinaryOp('-',Id('c'),Id('d')))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,369))
    def test_more21(self):
        """Simple program: int main() {} """
        input = """int main() {
            int a,b,c,d[10];
            a = a*c;
            a = d[b+c];
            }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl(Id('a'),IntType()),VarDecl(Id('b'),IntType()),VarDecl(Id('c'),IntType()),VarDecl(Id('d'),ArrayType(10,IntType())),BinaryOp('=',Id('a'),BinaryOp('*',Id('a'),Id('c'))),BinaryOp('=',Id('a'),ArrayCell(Id('d'),BinaryOp('+',Id('b'),Id('c'))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,370))
    def test_more22(self):
        """Simple program: int main() {} """
        input = """int main() {
            int a,b,c,d[10];
            a = a*c;
            foo(2)[3+x] = a[b[2]] + 3 ;
            
            }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl(Id('a'),IntType()),VarDecl(Id('b'),IntType()),VarDecl(Id('c'),IntType()),VarDecl(Id('d'),ArrayType(10,IntType())),BinaryOp('=',Id('a'),BinaryOp('*',Id('a'),Id('c'))),BinaryOp('=',ArrayCell(CallExpr(Id('foo'),[IntLiteral(2)]),BinaryOp('+',IntLiteral('3'),Id('x'))),BinaryOp('+',ArrayCell(Id('a'),ArrayCell(Id('b'),IntLiteral(2))),IntLiteral(3)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,371))
    def test_more23(self):
        """Simple program: int main() {} """
        input = """int main() {
            int a,b,c,d[10];
            a = a*c;
            foo(2)[3+x] = a[b[2]] + 3 ;
            a = a+b;
            
            }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl(Id('a'),IntType()),VarDecl(Id('b'),IntType()),VarDecl(Id('c'),IntType()),VarDecl(Id('d'),ArrayType(10,IntType())),BinaryOp('=',Id('a'),BinaryOp('*',Id('a'),Id('c'))),BinaryOp('=',ArrayCell(CallExpr(Id('foo'),[IntLiteral(2)]),BinaryOp('+',IntLiteral('3'),Id('x'))),BinaryOp('+',ArrayCell(Id('a'),ArrayCell(Id('b'),IntLiteral(2))),IntLiteral(3))),BinaryOp('=',Id('a'),BinaryOp('+',Id('a'),Id('b')))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,372))
    def test_more24(self):
        """Simple program: int main() {} """
        input = """int main() {
            int a,b,c,d[10];
            a = a*c;
            foo(2)[3+x] = a[b[2+(2*9)]] + 3 ;
            a = ((a+b)&&c)||d;
            
            }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl(Id('a'),IntType()),VarDecl(Id('b'),IntType()),VarDecl(Id('c'),IntType()),VarDecl(Id('d'),ArrayType(10,IntType())),BinaryOp('=',Id('a'),BinaryOp('*',Id('a'),Id('c'))),BinaryOp('=',ArrayCell(CallExpr(Id('foo'),[IntLiteral(2)]),BinaryOp('+',IntLiteral(3),Id('x'))),BinaryOp('+',ArrayCell(Id('a'),ArrayCell(Id('b'),BinaryOp('+',IntLiteral(2),BinaryOp('*',IntLiteral(2),IntLiteral(9))))),IntLiteral(3))),BinaryOp('=',Id('a'),BinaryOp('||',BinaryOp('&&',BinaryOp('+',Id('a'),Id('b')),Id('c')),Id('d')))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,373))
    def test_more25(self):
        """Simple program: int main() {} """
        input = """int main() {
            int a,b,c,d[10];
            a = a*c;
            foo(2)[3+x] = a[b[2+(2*9)]] + 3 ;
            a = ((a+b)&&c)||d;
            i = 1;
            foo(1,2) = 9;
            if (a == b ) d[0] = 1.0;
            
            }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl(Id('a'),IntType()),VarDecl(Id('b'),IntType()),VarDecl(Id('c'),IntType()),VarDecl(Id('d'),ArrayType(10,IntType())),BinaryOp('=',Id('a'),BinaryOp('*',Id('a'),Id('c'))),BinaryOp('=',ArrayCell(CallExpr(Id('foo'),[IntLiteral(2)]),BinaryOp('+',IntLiteral(3),Id('x'))),BinaryOp('+',ArrayCell(Id('a'),ArrayCell(Id('b'),BinaryOp('+',IntLiteral(2),BinaryOp('*',IntLiteral(2),IntLiteral(9))))),IntLiteral(3))),BinaryOp('=',Id('a'),BinaryOp('||',BinaryOp('&&',BinaryOp('+',Id('a'),Id('b')),Id('c')),Id('d'))),BinaryOp('=',Id('i'),IntLiteral(1)),BinaryOp('=',CallExpr(Id('foo'),[IntLiteral(1),IntLiteral(2)]),IntLiteral(9)),If(BinaryOp('==',Id('a'),Id('b')),BinaryOp('=',ArrayCell(Id('d'),IntLiteral(0)),FloatLiteral(1.0)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,374))
    def test_more26(self):
        """Simple program: int main() {} """
        input = """int main() {
            for(i = 1; i <10; i = i +2)
                if(i==1)
                i = 0;
            
            }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([For(BinaryOp('=',Id('i'),IntLiteral(1)),BinaryOp('<',Id('i'),IntLiteral(10)),BinaryOp('=',Id('i'),BinaryOp('+',Id('i'),IntLiteral(2))),If(BinaryOp('==',Id('i'),IntLiteral(1)),BinaryOp('=',Id('i'),IntLiteral(0))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,375))
    def test_more27(self):
        """Simple program: int main() {} """
        input = """int main() {
            do{
            {
            }
            
            }while( a < 3);
            }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([Dowhile([Block([Block([])])],BinaryOp('<',Id('a'),IntLiteral(3)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,376))
    def test_more28(self):
        """Simple program: int main() {} """
        input = """
            int[] foo(){
            return k;
            }
            int main() {
            getFloat();
            
            }"""
        expect = str(Program([FuncDecl(Id('foo'),[],ArrayPointerType(IntType()),Block([Return(Id('k'))])),FuncDecl(Id('main'),[],IntType(),Block([CallExpr(Id('getFloat'),[])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,377))
    def test_more247(self):
        """Simple program: int main() {} """
        input = """
            int[] foo(){
            return k;
            }
            int main() {
            int a;
            a=getFloat();
            putString(foo(3)[1]);
            }"""
        expect = str(Program([FuncDecl(Id('foo'),[],ArrayPointerType(IntType()),Block([Return(Id('k'))])),FuncDecl(Id('main'),[],IntType(),Block([VarDecl(Id('a'),IntType()),BinaryOp('=',Id('a'),CallExpr(Id('getFloat'),[])),CallExpr(Id('putString'),[ArrayCell(CallExpr(Id('foo'),[IntLiteral(3)]),IntLiteral(1))])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,378))
    def test_more29(self):
        """Simple program: int main() {} """
        input = """int main() {
            int a,b,c;
            a = a*c;
            b = khasd((khak()[a || b && c - d] % 20) - 10) && a;
            
            }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl(Id('a'),IntType()),VarDecl(Id('b'),IntType()),VarDecl(Id('c'),IntType()),BinaryOp('=',Id('a'),BinaryOp('*',Id('a'),Id('c'))),BinaryOp('=',Id('b'),BinaryOp('&&',CallExpr(Id('khasd'),[BinaryOp('-',BinaryOp('%',ArrayCell(CallExpr(Id('khak'),[]),BinaryOp('||',Id('a'),BinaryOp('&&',Id('b'),BinaryOp('-',Id('c'),Id('d'))))),IntLiteral(20)),IntLiteral(10))]),Id('a')))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,379))
    def test_more30(self):
        """Simple program: int main() {} """
        input = """int main() {
            int a,b,c,d[10];
            a = a*c;
            a = d[b+c];
            do{
            }
            {
            
            } while (a || 3 )!= 0;
            
            }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl(Id('a'),IntType()),VarDecl(Id('b'),IntType()),VarDecl(Id('c'),IntType()),VarDecl(Id('d'),ArrayType(10,IntType())),BinaryOp('=',Id('a'),BinaryOp('*',Id('a'),Id('c'))),BinaryOp('=',Id('a'),ArrayCell(Id('d'),BinaryOp('+',Id('b'),Id('c')))),Dowhile([Block([]),Block([])],BinaryOp('!=',BinaryOp('||',Id('a'),IntLiteral(3)),IntLiteral(0)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,380))
    def test_more31(self):
        """Simple program: int main() {} """
        input = """int main() {
            int a,b,c,d[10];
            a = a*c;
            a = d[b+c];
            do
            a = a +d[0];
            b = b*c;
            while (a || 3 )!= 0;
            
            }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl(Id('a'),IntType()),VarDecl(Id('b'),IntType()),VarDecl(Id('c'),IntType()),VarDecl(Id('d'),ArrayType(10,IntType())),BinaryOp('=',Id('a'),BinaryOp('*',Id('a'),Id('c'))),BinaryOp('=',Id('a'),ArrayCell(Id('d'),BinaryOp('+',Id('b'),Id('c')))),Dowhile([BinaryOp('=',Id('a'),BinaryOp('+',Id('a'),ArrayCell(Id('d'),IntLiteral(0)))),BinaryOp('=',Id('b'),BinaryOp('*',Id('b'),Id('c')))],BinaryOp('!=',BinaryOp('||',Id('a'),IntLiteral(3)),IntLiteral(0)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,381))
    def test_more32(self):
        """Simple program: int main() {} """
        input = """int main() {
            int a,b[2],c[20];
            string a1[10], c2[20];
            a = a*c;
            b = khasd((khak()[a || b && c - d] % 20) - 10) && a;
            //-c = (-a/c[0]*c[1])%c[2]+c[3]-c[4] && (c5 || c6);
            // khong phbai dang vua dau
            /* kjdadkasjdadk
           
            dalsdkasldad*/
             a = 132.e8;
            }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl(Id('a'),IntType()),VarDecl(Id('b'),ArrayType(2,IntType())),VarDecl(Id('c'),ArrayType(20,IntType())),VarDecl(Id('a1'),ArrayType(10,StringType())),VarDecl(Id('c2'),ArrayType(20,StringType())),BinaryOp('=',Id('a'),BinaryOp('*',Id('a'),Id('c'))),BinaryOp('=',Id('b'),BinaryOp('&&',CallExpr(Id('khasd'),[BinaryOp('-',BinaryOp('%',ArrayCell(CallExpr(Id('khak'),[]),BinaryOp('||',Id('a'),BinaryOp('&&',Id('b'),BinaryOp('-',Id('c'),Id('d'))))),IntLiteral(20)),IntLiteral(10))]),Id('a'))),BinaryOp('=',Id('a'),FloatLiteral(13200000000.0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,382))
    def test_more33(self):
        """Simple program: int main() {} """
        input = """int main() {
            int a,b[2],c[20];
            string a1[10], c2[20];
            a = a*c;
            b = khasd((khak()[a || b && c - d] % 20) - 10) && a;
            //-c = (-a/c[0]*c[1])%c[2]+c[3]-c[4] && (c5 || c6);
            // khong phbai dang vua dau
            
            c[20] = c[19]+132.e8;
            if(true)
            a = "abc";
            else
            c = 11;
            }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl(Id('a'),IntType()),VarDecl(Id('b'),ArrayType(2,IntType())),VarDecl(Id('c'),ArrayType(20,IntType())),VarDecl(Id('a1'),ArrayType(10,StringType())),VarDecl(Id('c2'),ArrayType(20,StringType())),BinaryOp('=',Id('a'),BinaryOp('*',Id('a'),Id('c'))),BinaryOp('=',Id('b'),BinaryOp('&&',CallExpr(Id('khasd'),[BinaryOp('-',BinaryOp('%',ArrayCell(CallExpr(Id('khak'),[]),BinaryOp('||',Id('a'),BinaryOp('&&',Id('b'),BinaryOp('-',Id('c'),Id('d'))))),IntLiteral(20)),IntLiteral(10))]),Id('a'))),BinaryOp('=',ArrayCell(Id('c'),IntLiteral(20)),BinaryOp('+',ArrayCell(Id('c'),IntLiteral(19)),FloatLiteral(13200000000.0))),If(BooleanLiteral('true'),BinaryOp('=',Id('a'),StringLiteral('abc')),BinaryOp('=',Id('c'),IntLiteral(11)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,383))

    def test_more34(self):
        """Simple program: int main() {} """
        input = """
            float a;
            int[] main(int a, float b[]) {
            F(3)[5];
            return;
            }"""
        expect = str(Program([VarDecl(Id('a'),FloatType()),FuncDecl(Id('main'),[VarDecl(Id('a'),IntType()),VarDecl(Id('b'),ArrayPointerType(FloatType()))],ArrayPointerType(IntType()),Block([ArrayCell(CallExpr(Id('F'),[IntLiteral(3)]),IntLiteral(5)),Return()]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,384))
    def test_more35(self):
       """Simple program: int main() {} """
       input = """int main() {
           c[20] = c[19]+132.e8;
           if(false)
           a = "abc";
           else
           c = 11;
           }"""
       expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([BinaryOp('=',ArrayCell(Id('c'),IntLiteral(20)),BinaryOp('+',ArrayCell(Id('c'),IntLiteral(19)),FloatLiteral(13200000000.0))),If(BooleanLiteral('false'),BinaryOp('=',Id('a'),StringLiteral('abc')),BinaryOp('=',Id('c'),IntLiteral(11)))]))]))
       self.assertTrue(TestAST.checkASTGen(input,expect,385))
    def test_more36(self):
        """ """
        input = """int fooa(int a[])
            {
                return a[0];
            }
            void main(){
                int arr[10];
                float f;
                f = 0;
                do f=f+foo(arr); f=f+1; while (foo(arr)+f)<100;
                return;
            }"""
        expect = str(Program([FuncDecl(Id("fooa"), [VarDecl(Id("a"), ArrayPointerType(IntType()))], IntType(), Block([Return(ArrayCell(Id("a"), IntLiteral(0)))])), FuncDecl(Id("main"), [], VoidType(), Block([VarDecl(Id("arr"), ArrayType(10, IntType())), VarDecl(Id("f"), FloatType()), BinaryOp(
            "=", Id("f"), IntLiteral(0)), Dowhile([BinaryOp("=", Id("f"), BinaryOp("+", Id("f"), CallExpr(Id("foo"), [Id("arr")]))), BinaryOp("=", Id("f"), BinaryOp("+", Id("f"), IntLiteral(1)))], BinaryOp("<", BinaryOp("+", CallExpr(Id("foo"), [Id("arr")]), Id("f")), IntLiteral(100))), Return()]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 386))

    def test_more37(self):
        """ """
        input = """int a;
            float bb;
            string c;
            int d[10];
            void main(){
                {

                }
                return;
            }"""
        expect = str(Program([VarDecl(Id("a"), IntType()), VarDecl(Id("bb"), FloatType()), VarDecl(Id("c"), StringType()), VarDecl(
            Id("d"), ArrayType(10, IntType())), FuncDecl(Id("main"), [], VoidType(), Block([Block([]), Return()]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 387))

    def test_more38(self):
        """ """
        input = """void main(){
                int a;
                {a =1;}
                if(a==2)
                    return;
                else                
                    return;
            }"""
        expect = str(Program([FuncDecl(Id("main"), [], VoidType(), Block([VarDecl(Id("a"), IntType()), Block(
            [BinaryOp("=", Id("a"), IntLiteral(1))]), If(BinaryOp("==", Id("a"), IntLiteral(2)), Return(), Return())]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 388))

    def test_more39(self):
        """ """
        input = """int main(){int aa,bb,cc,d;}"""
        expect = str(Program([FuncDecl(Id("main"), [], IntType(), Block([VarDecl(Id("aa"), IntType()), VarDecl(
            Id("bb"), IntType()), VarDecl(Id("cc"), IntType()), VarDecl(Id("d"), IntType())]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 389))

    def test_more40(self):
        """ """
        input = """int main(){int a[20],b,c,d;}"""
        expect = str(Program([FuncDecl(Id("main"), [], IntType(), Block([VarDecl(Id("a"), ArrayType(
            20, IntType())), VarDecl(Id("b"), IntType()), VarDecl(Id("c"), IntType()), VarDecl(Id("d"), IntType())]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 390))

    def test_more41(self):
        """ """
        input = """int main(){int aaa[12];}"""
        expect = str(Program([FuncDecl(Id("main"), [], IntType(), Block(
            [VarDecl(Id("aaa"), ArrayType(12, IntType()))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 391))
    def test_more42(self):
        """ """
        input = """int[] foo(int a,float b[]){
                int c[10];
                if(a>0) foo(a-1,b);
                else return c;
        }"""
        expect = str(Program([FuncDecl(Id("foo"), [VarDecl(Id("a"), IntType()), VarDecl(Id("b"), ArrayPointerType(FloatType()))], ArrayPointerType(IntType()), Block([VarDecl(
            Id("c"), ArrayType(10, IntType())), If(BinaryOp(">", Id("a"), IntLiteral(0)), CallExpr(Id("foo"), [BinaryOp("-", Id("a"), IntLiteral(1)), Id("b")]), Return(Id("c")))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 392))

    def test_more43(self):
        """ """
        input = """int main(){
            boolean bool; boo[2]=false;
        }"""
        expect = str(Program([FuncDecl(Id("main"), [], IntType(), Block([VarDecl(Id("bool"), BoolType(
        )), BinaryOp("=", ArrayCell(Id("boo"), IntLiteral(2)), BooleanLiteral(False))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 393))
    def test_more44(self):
        """ """
        input = """int main(){ a = b!=c;}"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",Id("a"),BinaryOp("!=",Id("b"),Id("c")))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 394))

    def test_more45(self):
        """ """
        input = """int main(){ boolean checking; checking=true;}"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl(Id("checking"),BoolType()),BinaryOp("=",Id("checking"),BooleanLiteral(True))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 395))

    def test_more46(self):
        """ """
        input = """int main(){if(bb) if (aa) if (cc) {} else {} else {} }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(Id("bb"),If(Id("aa"),If(Id("cc"),Block([]),Block([])),Block([])))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 396))
    def test_more50(self):
        """ """
        input = """
        int a; int b;
        """
        expect = str(Program([VarDecl(Id('a'),IntType()),VarDecl(Id('b'),IntType())]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 397))
    def test_more51(self):
        """ """
        input = """
        int a; float b;
        """
        expect = str(Program([VarDecl(Id('a'),IntType()),VarDecl(Id('b'),FloatType())]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 398))
    def test_more52(self):
        """ """
        input = """
        int a; float b; string c; boolean d;
        """
        expect = str(Program([VarDecl(Id('a'),IntType()),VarDecl(Id('b'),FloatType()),VarDecl(Id('c'),StringType()),VarDecl(Id('d'),BoolType())]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 399))
