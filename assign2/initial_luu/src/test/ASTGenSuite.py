import unittest
from TestUtils import TestAST
from AntiAST.py import *

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
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl(Id('a'),IntType()),VarDecl(Id('b'),IntType()),VarDecl(Id('c'),IntType()),VarDecl(Id('d'),ArrayType(10,IntType())),BinaryOp('=',Id('a'),BinaryOp('+',BinaryOp('-',Id('a'),IntLiteral(10)),BinaryOp('*',IntLiteral(9),IntLiteral(8)))),If(BinaryOp('<=',Id('a'),IntLiteral(1)),Block([BinaryOp('=',Id('a'),IntLiteral(1)),Block([BinaryOp('=',Id('b'),IntLiteral(10)),For(BinaryOp('=',Id('i'),IntLiteral(1)),BinaryOp('>',Id('i'),IntLiteral(10)),BinaryOp('=',Id('i'),BinaryOp('+',IntLiteral(1),IntLiteral(2))),BinaryOp('=',Id('a'),Id('c')))])])),Return(IntLiteral(1))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,364))
