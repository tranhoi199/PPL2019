import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """int main() {}"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,300))

    def test_more_complex_program1(self):
        """More complex program"""
        input = """int main () {
            putIntLn(4);
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("putIntLn"),[IntLiteral(4)])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,301))
    
    def test_call_without_parameter2(self):
        """More complex program"""
        input = """int main () {
            getIntLn();
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("getIntLn"),[])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,302))
    def test_call_without_parameter3(self):
        """More complex program"""
        input = """int main () {
            getIntLn(4.5);
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("getIntLn"),[FloatLiteral(4.5)])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,303))
    def test_call_without_parameter4(self):
        """More complex program"""
        input = """int main () {
            getIntLn(a);
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("getIntLn"),[Id("a")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,304))
    def test_call_without_parameter5(self):
        """More complex program"""
        input = """int main () {
            getIntLn(abc);
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("getIntLn"),[Id("abc")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,305))
    def test_call_without_parameter6(self):
        """More complex program"""
        input = """int main () {
            getIntLn("abc_a");
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("getIntLn"),[StringLiteral("abc_a")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,306))
    def test_call_without_parameter7(self):
        """More complex program"""
        input = """int main () {
            int a;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl(Id("a"),IntType())]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,307))
    def test_call_without_parameter8(self):
        """More complex program"""
        input = """int main () {
            int a[5];
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl(ArrayCell(Id("a"),IntLiteral(5)),IntType())]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,308))
    def test_call_without_parameter9(self):
        """More complex program"""
        input = """int main () {
            int a; break;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl(Id("a"),IntType()),Break()]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,309))
    def test_call_without_parameter10(self):
        """More complex program"""
        input = """int main () {
            {
            int a; continue;
            }
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Block([VarDecl(Id("a"),IntType()),Continue()])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,310))
    def test_call_without_parameter11(self):
        """More complex program"""
        input = """int main () {
            {
            int a;
            a=5;
            }
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Block([VarDecl(Id("a"),IntType()),BinaryOp("=",Id("a"),IntLiteral(5))])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,311))
    def test_call_without_parameter12(self):
        """More complex program"""
        input = """int main () {
            {
            int a;
            a=5;
            {
                b=2;
                }
            }
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Block([VarDecl(Id("a"),IntType()),BinaryOp("=",Id("a"),IntLiteral(5)),Block([BinaryOp("=",Id("b"),IntLiteral(2))])])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,312))
    def test_call_without_parameter13(self):
        """More complex program"""
        input = """int main () {
            a>5;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp(">",Id("a"),IntLiteral(5))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,313))
    def test_call_func14(self):
        """ Test Call Function """
        input = """
        int main(int c[]){
            int a;
            a = div(fun1(fun2(a[9],8),4),10);
            return a;
        }"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(Id(c),ArrayTypePointer(IntType))],IntType,Block([VarDecl(Id(a),IntType),BinaryOp(=,Id(a),CallExpr(Id(div),[CallExpr(Id(fun1),[CallExpr(Id(fun2),[ArrayCell(Id(a),IntLiteral(9)),IntLiteral(8)]),IntLiteral(4)]),IntLiteral(10)])),Return(Id(a))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,314))
    def test_call_without_parameter15(self):
        """More complex program"""
        input = """int main () {
            if (a>5) b=5;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp(">",Id("a"),IntLiteral(5)),BinaryOp("=",Id("b"),IntLiteral(5)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,315))
    def test_call_without_parameter16(self):
        """More complex program"""
        input = """int main () {
            do a=a+1; 
            while (a<=4);
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Dowhile([BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1)))],BinaryOp("<=",Id("a"),IntLiteral(4)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,316))
    def test_call_without_parameter17(self):
        """More complex program"""
        input = """int main () {
            if (a>5) b=5; else b=6;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp(">",Id("a"),IntLiteral(5)),BinaryOp("=",Id("b"),IntLiteral(5)),BinaryOp("=",Id("b"),IntLiteral(6)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,317))
    def test_call_without_parameter18(self):
        """More complex program"""
        input = """int main () {
            for (i = 1;i < 10;i = i + 1){
                a=a+1;
            }
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(1)),BinaryOp("<",Id("i"),IntLiteral(10)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1)))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,318))
    def test_call_without_parameter19(self):
        """More complex program"""
        input = """int main () {
            float a;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl(Id("a"),FloatType())]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,319))
    def test_call_without_parameter20(self):
        """More complex program"""
        input = """int main () {
            a>5;
            return;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp(">",Id("a"),IntLiteral(5)),Return()]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,320))
    def test_call_without_parameter21(self):
        """More complex program"""
        input = """int main () {
            float a;
            int b;
            if (a>=b) b+1;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl(Id("a"),FloatType()),VarDecl(Id("b"),IntType()),If(BinaryOp(">=",Id("a"),Id("b")),BinaryOp("+",Id("b"),IntLiteral(1)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,321))
    def test_call_without_parameter22(self):
        """More complex program"""
        input = """int main () {
            a=0+1-2;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",Id("a"),BinaryOp("-",BinaryOp("+",IntLiteral(0),IntLiteral(1)),IntLiteral(2)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,322))
    def test_call_without_parameter23(self):
        """More complex program"""
        input = """int main () {
            for (i=0;i<5;i=i+1)
            a=a+1;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),IntLiteral(5)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,323))
    def test_call_without_parameter24(self):
        """More complex program"""
        input = """void main () {
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,324))
    def test_call_without_parameter25(self):
        """More complex program"""
        input = """int foo(int a, int b) {
        }"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType())],IntType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,325))
    def test_call_without_parameter26(self):
        """More complex program"""
        input = """int foo(int a) {
            return 1;
            break;
        }"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),IntType())],IntType(),Block([Return(IntLiteral(1)),Break()]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,326))
    def test_call_without_parameter27(self):
        """More complex program"""
        input = """int foo(int a, int b){
            printf("Nhap so 1:");
            s=input;
            printf("Nhap so 2:");
            r=input;
        }"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType())],IntType(),Block([CallExpr(Id("printf"),[StringLiteral("Nhap so 1:")]),BinaryOp("=",Id("s"),Id("input")),CallExpr(Id("printf"),[StringLiteral("Nhap so 2:")]),BinaryOp("=",Id("r"),Id("input"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,327))
    def test_call_without_parameter28(self):
        """More complex program"""
        input = """int main(){
            a[5] = 5;
            foo();
            return;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",ArrayCell(Id("a"),IntLiteral(5)),IntLiteral(5)),CallExpr(Id("foo"),[]),Return()]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,328))
    def test_call_without_parameter29(self):
        """More complex program"""
        input = """int main(){
            a[5] = 5;
            foo();
            return;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",ArrayCell(Id("a"),IntLiteral(5)),IntLiteral(5)),CallExpr(Id("foo"),[]),Return()]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,329))
    def test_call_without_parameter30(self):
        """More complex program"""
        input = """boolean foo(int a, float b){
        }"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),FloatType())],BoolType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,330))
    def test_call_without_parameter31(self):
        """More complex program"""
        input = """int foo(){
            int a;
            int b;
            a = a-b;
        }"""
        expect = str(Program([FuncDecl(Id("foo"),[],IntType(),Block([VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),BinaryOp("=",Id("a"),BinaryOp("-",Id("a"),Id("b")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,331))
    def test_call_without_parameter32(self):
        """More complex program"""
        input = """int main(){
            string a[10];
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl(ArrayCell(Id("a"),IntLiteral("10")),StringType())]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,332))
    def test_call_without_parameter33(self):
        """More complex program"""
        input = """int main(){
            a = foo(b);
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",Id("a"),CallExpr(Id("foo"),[Id("b")]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,333))
    def test_call_without_parameter34(self):
        """More complex program"""
        input = """int main(){
            if (a==b)
            c = true;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp("==",Id("a"),Id("b")),BinaryOp("=",Id("c"),BooleanLiteral("true")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,334))
    def test_call_without_parameter35(self):
        """More complex program"""
        input = """int main(){
            float a;
            string b;
            if (b = "a")
            c = true;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl(Id("a"),FloatType()),VarDecl(Id("b"),StringType()),If(BinaryOp("=",Id("b"),StringLiteral("a")),BinaryOp("=",Id("c"),BooleanLiteral("true")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,335))
    def test_call_without_parameter36(self):
        """More complex program"""
        input = """int main(){
            if (a==b)
            c = true; else c = false;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp("==",Id("a"),Id("b")),BinaryOp("=",Id("c"),BooleanLiteral("true")),BinaryOp("=",Id("c"),BooleanLiteral("false")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,336))
    def test_call_without_parameter37(self):
        """More complex program"""
        input = """void main(){
            if (a==b) c = true;
            if (a!=b) c = false;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([If(BinaryOp("==",Id("a"),Id("b")),BinaryOp("=",Id("c"),BooleanLiteral("true"))),If(BinaryOp("!=",Id("a"),Id("b")),BinaryOp("=",Id("c"),BooleanLiteral("false")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,337))
    def test_call_without_parameter38(self):
        """More complex program"""
        input = """int main(){
            if (a>=b) return 1;
            else break;    
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp(">=",Id("a"),Id("b")),Return(IntLiteral(1)),Break())]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,338))
    def test_call_without_parameter39(self):
        """More complex program"""
        input = """int main(){
            if ((a>=b) || (a>5)) 
            return 1;   
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp("||",BinaryOp(">=",Id("a"),Id("b")),BinaryOp(">",Id("a"),IntLiteral(5))),Return(IntLiteral(1)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,339))
    def test_call_without_parameter40(self):
        """More complex program"""
        input = """int main(){
            if ((a>=b) && (b>c)){
                break;
                continue;
            }
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp("&&",BinaryOp(">=",Id("a"),Id("b")),BinaryOp(">",Id("b"),Id("c"))),Block([Break(),Continue()]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,340))
    def test_call_without_parameter41(self):
        """More complex program"""
        input = """int main(){
            do a=a+1;
            while ((a>=b) || (a>5));        
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Dowhile([BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1)))],BinaryOp("||",BinaryOp(">=",Id("a"),Id("b")),BinaryOp(">",Id("a"),IntLiteral(5))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,341))
    def test_call_without_parameter42(self):
        """More complex program"""
        input = """int main(){
            do {
                if (a%5=1)
                return true;
            }
            while (a>5);        
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Dowhile([Block([If(BinaryOp("=",BinaryOp("%",Id("a"),IntLiteral(5)),IntLiteral(1)),Return(BooleanLiteral("true")))])],BinaryOp(">",Id("a"),IntLiteral(5)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,342))
    def test_call_without_parameter43(self):
        """More complex program"""
        input = """int main(){
            for (i=1;i<5;i=i+1)
            a=a+b*c;        
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(1)),BinaryOp("<",Id("i"),IntLiteral(5)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),BinaryOp("*",Id("b"),Id("c")))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,343))
    def test_call_without_parameter44(self):
        """More complex program"""
        input = """int main(){
            for (i=1;i<5;i=i+1)
            a = "abc";      
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(1)),BinaryOp("<",Id("i"),IntLiteral(5)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),BinaryOp("=",Id("a"),StringLiteral("abc")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,344))
    def test_call_without_parameter45(self):
        """More complex program"""
        input = """int main(){
            for (i=1;i<5;i=i+1)
            a = 1.234;      
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(1)),BinaryOp("<",Id("i"),IntLiteral(5)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),BinaryOp("=",Id("a"),FloatLiteral(1.234)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,345))
    def test_call_without_parameter46(self):
        """More complex program"""
        input = """int main(){  
            a;    
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Id("a")]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,346))
    def test_call_without_parameter47(self):
        """More complex program"""
        input = """int main(){  
            5;    
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([IntLiteral(5)]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,347))
    def test_call_without_parameter48(self):
        """More complex program"""
        input = """int main(){  
            "hasagi";    
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([StringLiteral("hasagi")]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,348))
    def test_call_without_parameter49(self):
        """More complex program"""
        input = """int main(){  
            true;    
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BooleanLiteral("true")]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,349))
    def test_call_without_parameter50(self):
        """More complex program"""
        input = """int main(){  
            1.333;    
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([FloatLiteral(1.333)]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,350))
    def test_call_without_parameter51(self):
        """More complex program"""
        input = """int isInterrupt;
                 int countNumber;
                 //countNumber = 0;
                 void ISR(int isInterrupt){
                     interruptEnable(true);
                     interruptSet(10);
                     interrupt();
                 }
                 int main(){
                     int count;
                     count = 0;
                     do{
                         checkInterrupt();
                         if(countNumber % 3 == 0) return interruptVector[countNumber];
                         else
                             for(count; count+count; isInterrupt)
                                 countNumber = checkInterrupt(interruptVector[countNumber[count]]);
                         noInterrupt();
                     }
                     while(true);
                 }"""
        expect = str(Program([VarDecl(Id("isInterrupt"),IntType()),VarDecl(Id("countNumber"),IntType()),FuncDecl(Id("ISR"),[VarDecl(Id("isInterrupt"),IntType())],VoidType(),Block([CallExpr(Id("interruptEnable"),[BooleanLiteral("true")]),CallExpr(Id("interruptSet"),[IntLiteral(10)]),CallExpr(Id("interrupt"),[])])),FuncDecl(Id("main"),[],IntType(),Block([VarDecl(Id("count"),IntType()),BinaryOp("=",Id("count"),IntLiteral(0)),Dowhile([Block([CallExpr(Id("checkInterrupt"),[]),If(BinaryOp("==",BinaryOp("%",Id("countNumber"),IntLiteral(3)),IntLiteral(0)),Return(ArrayCell(Id("interruptVector"),Id("countNumber"))),For(Id("count"),BinaryOp("+",Id("count"),Id("count")),Id("isInterrupt"),BinaryOp("=",Id("countNumber"),CallExpr(Id("checkInterrupt"),[ArrayCell(Id("interruptVector"),ArrayCell(Id("countNumber"),Id("count")))])))),CallExpr(Id("noInterrupt"),[])])],BooleanLiteral("true"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,351))
    def test_call_without_parameter52(self):
        """More complex program"""
        input = """int main(){
            do a; while true;
        return exit(0);
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Dowhile([Id("a")],BooleanLiteral("true")),Return(CallExpr(Id("exit"),[IntLiteral(0)]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,352))
    def test_call_without_parameter53(self):
        """More complex program"""
        input = """ int main(){
            a[b[c]];
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([ArrayCell(Id("a"),ArrayCell(Id("b"),Id("c")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,353))
    def test_call_without_parameter54(self):
        """More complex program"""
        input = """ int main(){
            a[b[5]];
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([ArrayCell(Id("a"),ArrayCell(Id("b"),IntLiteral(5)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,354))
    def test_call_without_parameter55(self):
        """More complex program"""
        input = """ void main(){
            a[5] = b[4]+c[3]-d[2]>e[1];
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("=",ArrayCell(Id("a"),IntLiteral(5)),BinaryOp(">",BinaryOp("-",BinaryOp("+",ArrayCell(Id("b"),IntLiteral(4)),ArrayCell(Id("c"),IntLiteral(3))),ArrayCell(Id("d"),IntLiteral(2))),ArrayCell(Id("e"),IntLiteral(1))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,355))
    def test_call_without_parameter56(self):
        """More complex program"""
        input = """ int main(){
            a[b[5]];
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([ArrayCell(Id("a"),ArrayCell(Id("b"),IntLiteral(5)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,356))
    def test_call_without_parameter57(self):
        """More complex program"""
        input = """
 				float x;
 				string y[1];
 				"""
        expect = str(Program([VarDecl(Id("x"),FloatType()),VarDecl(ArrayCell(Id("y"),IntLiteral(1)),StringType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,357))
    def test_call_without_parameter58(self):
        """More complex program"""
        input = """
 				boolean a;
 				string d(){}
 				"""
        expect = str(Program([VarDecl(Id("a"),BoolType()),FuncDecl(Id("d"),[],StringType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,358))
    def test_call_without_parameter59(self):
        """More complex program"""
        input = """int main(){
                if (a!=5) 
                    do b=b+1; while (c!=5);
        }			
 				"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp("!=",Id("a"),IntLiteral(5)),Dowhile([BinaryOp("=",Id("b"),BinaryOp("+",Id("b"),IntLiteral(1)))],BinaryOp("!=",Id("c"),IntLiteral(5))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,359))
    def test_call_without_parameter60(self):
        """More complex program"""
        input = """
 				float nomoreassignment(){
                    break;
                 }
 				"""
        expect = str(Program([FuncDecl(Id("nomoreassignment"),[],FloatType(),Block([Break()]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,360))
    def test_call_without_parameter61(self):
        """More complex program"""
        input = """
 				float nomoreassignment(){
                    break;
                    return a[5];
                 }
 				"""
        expect = str(Program([FuncDecl(Id("nomoreassignment"),[],FloatType(),Block([Break(),Return(ArrayCell(Id("a"),IntLiteral(5)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,361))
    def test_call_without_parameter62(self):
        """More complex program"""
        input = """
 				float nomoreassignment(){
                    if (ass3 == 1)
                    break;        
                 }
 				"""
        expect = str(Program([FuncDecl(Id("nomoreassignment"),[],FloatType(),Block([If(BinaryOp("==",Id("ass3"),IntLiteral(1)),Break())]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,362))
    def test_call_without_parameter63(self):
        """More complex program"""
        input = """ int main(){
            leuleu() = 2;
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",CallExpr(Id("leuleu"),[]),IntLiteral(2))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,363))
    def test_call_without_parameter64(self):
        """More complex program"""
        input = """ int main(){
            if (ass3 == 1) continue;
            else {
                continue;
                break;
            }
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp("==",Id("ass3"),IntLiteral(1)),Continue(),Block([Continue(),Break()]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,364))
    def test_call_without_parameter65(self):
        """More complex program"""
        input = """ int main(){
            {
                {
                    a=1;
                }
            }
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Block([Block([BinaryOp("=",Id("a"),IntLiteral(1))])])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,365))
    def test_call_without_parameter66(self):
        """More complex program"""
        input = """ int main(){
            {
                if ((s1) && (s2))
                a[5] = 0;
            }
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Block([If(BinaryOp("&&",Id("s1"),Id("s2")),BinaryOp("=",ArrayCell(Id("a"),IntLiteral(5)),IntLiteral(0)))])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,366))
    def test_call_without_parameter67(self):
        """More complex program"""
        input = """int main(){
            string nope;
            nope="nope";
        } 
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl(Id("nope"),StringType()),BinaryOp("=",Id("nope"),StringLiteral("nope"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,367))
    def test_call_without_parameter68(self):
        """More complex program"""
        input = """void foo(){
            {int a;}
        } 
        """
        expect = str(Program([FuncDecl(Id("foo"),[],VoidType(),Block([Block([VarDecl(Id("a"),IntType())])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,368))
    def test_call_without_parameter69(self):
        """More complex program"""
        input = """int main(){
            void foo(){
                a=1;
                }
        } 
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([])),FuncDecl(Id("foo"),[],VoidType(),Block([BinaryOp("=",Id("a"),IntLiteral(1))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,369))
    def test_call_without_parameter70(self):
        """More complex program"""
        input = """void foo(){
            {}
        } 
        """
        expect = str(Program([FuncDecl(Id("foo"),[],VoidType(),Block([Block([])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,370))
    def test_call_without_parameter71(self):
        """More complex program"""
        input = """void foo(){
            {
                {}
            }
        } 
        """
        expect = str(Program([FuncDecl(Id("foo"),[],VoidType(),Block([Block([Block([])])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,371))
    def test_call_without_parameter72(self):
        input = """void foo(int BBB){
                     if(AAA == 0)
                         BBB("CCC");
                     else
                         BBB("BBB");
                     return;
                 }
 				"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl(Id("BBB"),IntType())],VoidType(),Block([If(BinaryOp("==",Id("AAA"),IntLiteral(0)),CallExpr(Id("BBB"),[StringLiteral("CCC")]),CallExpr(Id("BBB"),[StringLiteral("BBB")])),Return()]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,372))
    def test_call_without_parameter73(self):
        """More complex program"""
        input = """
 				void amIEmpty(int a){
                     if(falling)
                         Flying();
                     int var;
                     float var[3];
                 }
 				"""
        expect = str(Program([FuncDecl(Id("amIEmpty"),[VarDecl(Id("a"),IntType())],VoidType(),Block([If(Id("falling"),CallExpr(Id("Flying"),[])),VarDecl(Id("var"),IntType()),VarDecl(ArrayCell(Id("var"),IntLiteral(3)),FloatType())]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,373))
    def test_call_without_parameter74(self):
        """More complex program"""
        input = """
 				void main(){
                     if(a){
                         b;
                         c;
                     }
                     return;
                 }
 				"""
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([If(Id("a"),Block([Id("b"),Id("c")])),Return()]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,374))
    def test_call_without_parameter75(self):
        """More complex program"""
        input = """
 				void main(){
                    if(a)
                        if(b)
                            if(c)
                            d;
                    return;
                 }
 				"""
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([If(Id("a"),If(Id("b"),If(Id("c"),Id("d")))),Return()]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,375))
    def test_call_without_parameter76(self):
        """More complex program"""
        input = """
 				int main(){
                    printf("Hasagi");
                 }
 				"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("printf"),[StringLiteral("Hasagi")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,376))
    def test_call_without_parameter77(self):
        """More complex program"""
        input = """
 				int main(){
                    if (a(b))
                        if(c(d))
                        e;
                        else f;
                    else g;
                 }
 				"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(CallExpr(Id("a"),[Id("b")]),If(CallExpr(Id("c"),[Id("d")]),Id("e"),Id("f")),Id("g"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,377))
    def test_call_without_parameter78(self):
        """More complex program"""
        input = """
 				int main(){
                    if (a)
                        b;
                    else 
                        if (c)
                        d;
                        else e;
                        }
 				"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(Id("a"),Id("b"),If(Id("c"),Id("d"),Id("e")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,378))
    def test_call_without_parameter79(self):
        """More complex program"""
        input = """
 				int main(){
                    if (a)
                        b();
                    else 
                        c();
                        }
 				"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(Id("a"),CallExpr(Id("b"),[]),CallExpr(Id("c"),[]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,379))
    def test_call_without_parameter80(self):
        """More complex program"""
        input = """int main(){
        {
            {
                {
                    i + love + you + much + MAD ;
                }
            }
        }
      }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Block([Block([Block([BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",Id("i"),Id("love")),Id("you")),Id("much")),Id("MAD"))])])])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,380))
    def test_call_without_parameter81(self):
        """More complex program"""
        input = """int main(){
           a(b,c,d[anh+yeu+em]);
           -a * b + d - 120;
        
      }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("a"),[Id("b"),Id("c"),ArrayCell(Id("d"),BinaryOp("+",BinaryOp("+",Id("anh"),Id("yeu")),Id("em")))]),BinaryOp("-",BinaryOp("+",BinaryOp("*",UnaryOp("-",Id("a")),Id("b")),Id("d")),IntLiteral(120))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,381))
    def test_call_without_parameter82(self):
        """More complex program"""
        input = """
 				int main(){
                    DT=D+T;
                        }
 				"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",Id("DT"),BinaryOp("+",Id("D"),Id("T")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,382))
    def test_call_without_parameter83(self):
        """More complex program"""
        input = """
 				int main(){
                    if (a||b||c)
                        dosth;
                        }
 				"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp("||",BinaryOp("||",Id("a"),Id("b")),Id("c")),Id("dosth"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,383))
    def test_call_without_parameter84(self):
        """More complex program"""
        input = """
 				int main(){
                    if (a && b && c)
                        dosth;      
                        }
 				"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp("&&",BinaryOp("&&",Id("a"),Id("b")),Id("c")),Id("dosth"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,384))
    def test_call_without_parameter85(self):
        """More complex program"""
        input = """
 				int main(){
                    if (a || b && c)
                        dosth;
                        }
 				"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp("||",Id("a"),BinaryOp("&&",Id("b"),Id("c"))),Id("dosth"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,385))
    def test_call_without_parameter86(self):
        """More complex program"""
        input = """
 				int main(){
                    if ((a>b) || (b <c) && (a=3))
                        noo;
                        }
 				"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp("||",BinaryOp(">",Id("a"),Id("b")),BinaryOp("&&",BinaryOp("<",Id("b"),Id("c")),BinaryOp("=",Id("a"),IntLiteral(3)))),Id("noo"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,386))
    def test_call_without_parameter87(self):
        """More complex program"""
        input = """
 				int main(){
                    a-b || b-c;
                    }
 				"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("-",BinaryOp("||",BinaryOp("-",Id("a"),Id("b")),Id("b")),Id("c"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,387))
    def test_call_without_parameter88(self):
        """More complex program"""
        input = """
 				int main(){
                    do a*b%c-d;
                    while (a!=0);
                    }
 				"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Dowhile([BinaryOp("-",BinaryOp("%",BinaryOp("*",Id("a"),Id("b")),Id("c")),Id("d"))],BinaryOp("!=",Id("a"),IntLiteral(0)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,388))
    def test_call_without_parameter89(self):
        """More complex program"""
        input = """
 				int main(){
                    !-2;
                        }
 				"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([UnaryOp("!",UnaryOp("-",IntLiteral(2)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,389))
    def test_call_without_parameter90(self):
        """More complex program"""
        input = """int main(){
            1.2 + 2;
            }
 				
 				"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("+",FloatLiteral(1.2),IntLiteral(2))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,390))
    def test_call_without_parameter91(self):
        """More complex program"""
        input = """
 				int main(){
                    a=foo()+2;
                    }
 				"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",Id("a"),BinaryOp("+",CallExpr(Id("foo"),[]),IntLiteral(2)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,391))
    def test_call_without_parameter92(self):
        """More complex program"""
        input = """
 				int main(){
                    a=funcall(a,2,b);
                    }
 				"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",Id("a"),CallExpr(Id("funcall"),[Id("a"),IntLiteral(2),Id("b")]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,392))
    def test_call_without_parameter93(self):
        """More complex program"""
        input = """
 				int main(){
                    break;
                    continue;
                    return 1;
                        }
 				"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Break(),Continue(),Return(IntLiteral(1))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,393))
    def test_call_without_parameter94(self):
        """More complex program"""
        input = """
 				int main(){
                    f[abb[e(10*2)]] = 312120*3232;
                        }
 				"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",ArrayCell(Id("f"),ArrayCell(Id("abb"),CallExpr(Id("e"),[BinaryOp("*",IntLiteral(10),IntLiteral(2))]))),BinaryOp("*",IntLiteral(312120),IntLiteral(3232)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,394))
    def test_call_without_parameter95(self):
        """More complex program"""
        input = """
 				int main(){
                    return a+b>2;
                    }
 				"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Return(BinaryOp(">",BinaryOp("+",Id("a"),Id("b")),IntLiteral(2)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,395))
    def test_call_without_parameter96(self):
        """More complex program"""
        input = """
 				int main(){
                    abc = def = m+2;
                    }
 				"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",Id("abc"),BinaryOp("=",Id("def"),BinaryOp("+",Id("m"),IntLiteral(2))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,396))
    def test_call_without_parameter97(self):
        """More complex program"""
        input = """
 				int main(){
                    do a;
                    while (a!=1);
                    }
 				"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Dowhile([Id("a")],BinaryOp("!=",Id("a"),IntLiteral(1)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,397))
    def test_call_without_parameter98(self):
        """More complex program"""
        input = """int main(){
        {
           {
            int a;
            2;
            string_Lit;
            true;
            a();
           }
        }
      }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Block([Block([VarDecl(Id("a"),IntType()),IntLiteral(2),Id("string_Lit"),BooleanLiteral("true"),CallExpr(Id("a"),[])])])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,398))
    def test_call_without_parameter399(self):
        """More complex program"""
        input = """
 				int main(){
                    plzquamon5cham();
                    }
 				"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("plzquamon5cham"),[])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,399))
    
    
    
    