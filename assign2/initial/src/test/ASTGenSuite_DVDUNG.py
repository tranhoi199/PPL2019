import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):

    def test_1(self):
        """AST_Test_1"""
        input = """int main() {}"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,301))
    def test_2(self):
        """AST_Test_2"""
        input = """int main () {
            putIntLn(4);
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("putIntLn"),[IntLiteral(4)])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,302))
    def test_3(self):
        """AST_Test_3"""
        input="""int main(){int a,b,c,d;}"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",IntType())]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,303))
    def test_4(self):
        """AST_Test_4"""
        input="""int main(){int a[10],b,c,d;}"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",ArrayType(10,IntType())),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",IntType())]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,304))
    def test_5(self):
        """AST_Test_5"""
        input="""int main(){
                int a;
                b=10;
                }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",IntType()),BinaryOp("=",Id("b"),IntLiteral(10))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,305))
    def test_6(self):
        """AST_Test_6"""
        input = """int[] foo(int a,float b[]) {
                int c[3];
                if(a>0) foo(a-1,b);
                else return c;
        }"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl("a",IntType()),VarDecl("b",ArrayPointerType(FloatType()))],ArrayPointerType(IntType()),Block([VarDecl("c",ArrayType(3,IntType())),If(BinaryOp(">",Id("a"),IntLiteral(0)),CallExpr(Id("foo"),[BinaryOp("-",Id("a"),IntLiteral(1)),Id("b")]),Return(Id("c")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,306))
    def test_7(self):
        """AST_Test_7"""
        input = """int main(){
            boolean c;
            int i;
            i=a+3;
            if (i>0){
                int d;
                d=i+3;
                putInt(d);
            }
            return i;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("c",BoolType()),VarDecl("i",IntType()),BinaryOp("=",Id("i"),BinaryOp("+",Id("a"),IntLiteral(3))),If(BinaryOp(">",Id("i"),IntLiteral(0)),Block([VarDecl("d",IntType()),BinaryOp("=",Id("d"),BinaryOp("+",Id("i"),IntLiteral(3))),CallExpr(Id("putInt"),[Id("d")])])),Return(Id("i"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,307))
    
    def test_8(self):
        """AST_Test_8"""
        input = """int main(){
            foo(2)[3+x]=a[b[2]]+3;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",ArrayCell(CallExpr(Id("foo"),[IntLiteral(2)]),BinaryOp("+",IntLiteral(3),Id("x"))),BinaryOp("+",ArrayCell(Id("a"),ArrayCell(Id("b"),IntLiteral(2))),IntLiteral(3)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,308))
    def test_9(self):
        """AST_Test_9"""
        input = """int main(){
            int n;
            n=10;
            if (n>10)
            {
                printName();
            }
            else{
                n=n+1;
            }
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("n",IntType()),BinaryOp("=",Id("n"),IntLiteral(10)),If(BinaryOp(">",Id("n"),IntLiteral(10)),Block([CallExpr(Id("printName"),[])]),Block([BinaryOp("=",Id("n"),BinaryOp("+",Id("n"),IntLiteral(1)))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,309))
    def test_10(self):
        """AST_Test_10"""
        input = """int main(){
            if (n>1)
            {
                printName();    
            }
            {
                printAge();
            }
            {
                printAddress();
            }
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp(">",Id("n"),IntLiteral(1)),Block([CallExpr(Id("printName"),[])])),Block([CallExpr(Id("printAge"),[])]),Block([CallExpr(Id("printAddress"),[])])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,310))
    def test_11(self):
        """AST_Test_7"""
        input = """int main(){
            if (n)
            {
                printName();    
            }
            else
            {

            }
          
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(Id("n"),Block([CallExpr(Id("printName"),[])]),Block([]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,311))
    def test_12(self):
        """AST_Test_12"""
        input = """int main(){
            do{
                int a;
                a=10;
                
            }
            {

            }while("string");
          
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Dowhile([Block([VarDecl("a",IntType()),BinaryOp("=",Id("a"),IntLiteral(10))]),Block([])],StringLiteral("string"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,312))
    def test_13(self):
        """AST_Test_13"""
        input = """int main(){
            do{
                int a;
                a=110;    
            }
            {

            }while "string" ;
          
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Dowhile([Block([VarDecl("a",IntType()),BinaryOp("=",Id("a"),IntLiteral(110))]),Block([])],StringLiteral("string"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,313))
    def test_14(self):
        """AST_Test14"""
        input = """int main(){
            for (i=0;i<10;i=i+1)
            {
                print("This is PPL");
            }   
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),IntLiteral(10)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([CallExpr(Id("print"),[StringLiteral("This is PPL")])]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,314))
    def test_15(self):
        """AST_Test_15"""
        input = """int main(){
            for (i=0;i<10;i=i+1)
            {
                print("This is PPL");
            }
            {

            } 
            {

            }  
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),IntLiteral(10)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([CallExpr(Id("print"),[StringLiteral("This is PPL")])])),Block([]),Block([])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,315))
    def test_16(self):
        """AST_Test_16"""
        input = """int main(){
            for (i=0;i<10;i=i+1)
            {
                print("This is PPL");
                if (i==5)
                {
                    break;
                }
            }
             
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),IntLiteral(10)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([CallExpr(Id("print"),[StringLiteral("This is PPL")]),If(BinaryOp("==",Id("i"),IntLiteral(5)),Block([Break()]))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,316))
    def test_17(self):
        """AST_Test_17"""
        input = """int main(){
            for (i=0;i<10;i=i+1)
            {
                print("This is PPL");
                if (i==5)
                {
                    continue;
                }
            }
             
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),IntLiteral(10)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([CallExpr(Id("print"),[StringLiteral("This is PPL")]),If(BinaryOp("==",Id("i"),IntLiteral(5)),Block([Continue()]))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,317))
    def test_18(self):
        """AST_Test_18"""
        input = """int main(){
            int i;
            i=10;
            print(i);
            system("pause");
            return 0;
            
             
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("i",IntType()),BinaryOp("=",Id("i"),IntLiteral(10)),CallExpr(Id("print"),[Id("i")]),CallExpr(Id("system"),[StringLiteral("pause")]),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,318))
    def test_19(self):
        """AST_Test_19"""
        input = """void main(){
            int i;
            i=10;
            print(i);
            system("pause");
            return;
            
             
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("i",IntType()),BinaryOp("=",Id("i"),IntLiteral(10)),CallExpr(Id("print"),[Id("i")]),CallExpr(Id("system"),[StringLiteral("pause")]),Return()]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,319))
    def test_20(self):
        """AST_Test_20"""
        input = """int main(){
            i=1;
            i+2;
            100;
            foo(1,2); 
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",Id("i"),IntLiteral(1)),BinaryOp("+",Id("i"),IntLiteral(2)),IntLiteral(100),CallExpr(Id("foo"),[IntLiteral(1),IntLiteral(2)])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,320))
    def test_21(self):
        """AST_Test_21"""
        input = """int main(){
            boolean check;
            check=true;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("check",BoolType()),BinaryOp("=",Id("check"),BooleanLiteral(True))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,321))
    def test_22(self):
        """AST_Test_22"""
        input = """int main(){
            int a;
            a=10+4+3;
            print(a);
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",IntType()),BinaryOp("=",Id("a"),BinaryOp("+",BinaryOp("+",IntLiteral(10),IntLiteral(4)),IntLiteral(3))),CallExpr(Id("print"),[Id("a")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,322))
    def test_23(self):
        """AST_Test_23"""
        input = """int main(){
            int a;
            a=10=4=3;
            print(a);
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",IntType()),BinaryOp("=",Id("a"),BinaryOp("=",IntLiteral(10),BinaryOp("=",IntLiteral(4),IntLiteral(3)))),CallExpr(Id("print"),[Id("a")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,323))
    def test_24(self):
        """AST_Test_24"""
        input = """int main(){
            if(b) if (a) {} else {} else {} 
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(Id("b"),If(Id("a"),Block([]),Block([])),Block([]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,324))
    def test_25(self):
        """AST_Test_25"""
        input = """int main(){
            if(b) if (a) if (c) {} else {} else {} 
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(Id("b"),If(Id("a"),If(Id("c"),Block([]),Block([])),Block([])))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,325))
    def test_26(self):
        """AST_Test_26"""
        input = """int i;
        int f(){
            return 200;
        }
        void main(){
            int test;
            test=f();
            putIntLn(test);
            {
                int i;
                int test;
                int f;
                test=f=i=100;
                putIntLn(i);
                putIntLn(test);
                putIntLn(f);

            }
            putIntLn(test);
        }
            
        
        """
        expect = str(Program([VarDecl("i",IntType()),FuncDecl(Id("f"),[],IntType(),Block([Return(IntLiteral(200))])),FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("test",IntType()),BinaryOp("=",Id("test"),CallExpr(Id("f"),[])),CallExpr(Id("putIntLn"),[Id("test")]),Block([VarDecl("i",IntType()),VarDecl("test",IntType()),VarDecl("f",IntType()),BinaryOp("=",Id("test"),BinaryOp("=",Id("f"),BinaryOp("=",Id("i"),IntLiteral(100)))),CallExpr(Id("putIntLn"),[Id("i")]),CallExpr(Id("putIntLn"),[Id("test")]),CallExpr(Id("putIntLn"),[Id("f")])]),CallExpr(Id("putIntLn"),[Id("test")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,326))
    def test_27(self):
        """AST_Test_27"""
        input = """int main(){
        float array[2];}
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("array",ArrayType(2,FloatType()))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,327))
    def test_28(self):
        """AST_Test_28"""
        input = """
        int checkPointerType(int a[]){}
        """
        expect = str(Program([FuncDecl(Id("checkPointerType"),[VarDecl("a",ArrayPointerType(IntType()))],IntType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,328))
    def test_29(self):
        """AST_Test_29"""
        input = """
        int main(){
            foo(2)+foo(3);
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("+",CallExpr(Id("foo"),[IntLiteral(2)]),CallExpr(Id("foo"),[IntLiteral(3)]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,329))
    def test_30(self):
        """AST_Test_30"""
        input = """
        //Dang Van Dung
        int main(){
        //Dang Van Dung
            int a;
    }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",IntType())]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,330))
    def test_31(self):
        """AST_Test_31"""
        input = """
            int main(){
           a[b[c[foo(foo(2))]]];
           }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([ArrayCell(Id("a"),ArrayCell(Id("b"),ArrayCell(Id("c"),CallExpr(Id("foo"),[CallExpr(Id("foo"),[IntLiteral(2)])]))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,331))
    def test_32(self):
        """AST_Test_32"""
        input = """
           void main(){
            a[b[c[foo(2)]]];
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([ArrayCell(Id("a"),ArrayCell(Id("b"),ArrayCell(Id("c"),CallExpr(Id("foo"),[IntLiteral(2)]))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,332))
    def test_33(self):
        """AST_Test_33"""
        input = """
            int main(){
        array[foo(2)]==b=a;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",BinaryOp("==",ArrayCell(Id("array"),CallExpr(Id("foo"),[IntLiteral(2)])),Id("b")),Id("a"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,333))
    def test_34(self):
        """AST_Test_34"""
        input = """
           int computeSum(int a[],int n){
                int sum;
                sum=0;
                for (i=0;i<n;i=i+1){
                    sum=sum+a[i];
                }
                return sum;

                }
        """
        expect = str(Program([FuncDecl(Id("computeSum"),[VarDecl("a",ArrayPointerType(IntType())),VarDecl("n",IntType())],IntType(),Block([VarDecl("sum",IntType()),BinaryOp("=",Id("sum"),IntLiteral(0)),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),Id("n")),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([BinaryOp("=",Id("sum"),BinaryOp("+",Id("sum"),ArrayCell(Id("a"),Id("i"))))])),Return(Id("sum"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,334))
    def test_35(self):
        """AST_Test_35"""
        input = """
        int main (){
            foo;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Id("foo")]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,335))
    def test_36(self):
        """AST_Test_36"""
        input = """
            void main() {
        value = func()[func()[func(10)]];
        }

        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("=",Id("value"),ArrayCell(CallExpr(Id("func"),[]),ArrayCell(CallExpr(Id("func"),[]),CallExpr(Id("func"),[IntLiteral(10)]))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,336))
    def test_37(self):
        """AST_Test_37"""
        input = """
            int main(){
           int number;
           number=foo(10)[3*foo(a[a10[a[10]]])];
           }    
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("number",IntType()),BinaryOp("=",Id("number"),ArrayCell(CallExpr(Id("foo"),[IntLiteral(10)]),BinaryOp("*",IntLiteral(3),CallExpr(Id("foo"),[ArrayCell(Id("a"),ArrayCell(Id("a10"),ArrayCell(Id("a"),IntLiteral(10))))]))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,337))
    def test_38(self):
        """AST_Test_38"""
        input = """
            int main(){
           int number;
           number=foo(((a[10])[10])[20]);
           }    
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("number",IntType()),BinaryOp("=",Id("number"),CallExpr(Id("foo"),[ArrayCell(ArrayCell(ArrayCell(Id("a"),IntLiteral(10)),IntLiteral(10)),IntLiteral(20))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,338))
    def test_39(self):
        """AST_Test_39"""
        input = """
            int main(){
           foo(foo(10),foo(10)[20]<10==50=10==20=20==20);
        }
        
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("foo"),[CallExpr(Id("foo"),[IntLiteral(10)]),BinaryOp("=",BinaryOp("==",BinaryOp("<",ArrayCell(CallExpr(Id("foo"),[IntLiteral(10)]),IntLiteral(20)),IntLiteral(10)),IntLiteral(50)),BinaryOp("=",BinaryOp("==",IntLiteral(10),IntLiteral(20)),BinaryOp("==",IntLiteral(20),IntLiteral(20))))])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,339))
    def test_40(self):
        """AST_Test_40"""
        input = """
            int main(){
           foo(foo(10==10=10==10)[10[1]]==10=10==10,foo(10)[20==10=20==10=120]<10==50=10==20=20==20);   
        }
        
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("foo"),[BinaryOp("=",BinaryOp("==",ArrayCell(CallExpr(Id("foo"),[BinaryOp("=",BinaryOp("==",IntLiteral(10),IntLiteral(10)),BinaryOp("==",IntLiteral(10),IntLiteral(10)))]),ArrayCell(IntLiteral(10),IntLiteral(1))),IntLiteral(10)),BinaryOp("==",IntLiteral(10),IntLiteral(10))),BinaryOp("=",BinaryOp("==",BinaryOp("<",ArrayCell(CallExpr(Id("foo"),[IntLiteral(10)]),BinaryOp("=",BinaryOp("==",IntLiteral(20),IntLiteral(10)),BinaryOp("=",BinaryOp("==",IntLiteral(20),IntLiteral(10)),IntLiteral(120)))),IntLiteral(10)),IntLiteral(50)),BinaryOp("=",BinaryOp("==",IntLiteral(10),IntLiteral(20)),BinaryOp("==",IntLiteral(20),IntLiteral(20))))])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,340))
    def test_41(self):
        """AST_Test_41"""
        input = """
             int main(){
                a[0.5]=0.5<a=b>c=d<e==f;
            }

        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",ArrayCell(Id("a"),FloatLiteral(0.5)),BinaryOp("=",BinaryOp("<",FloatLiteral(0.5),Id("a")),BinaryOp("=",BinaryOp(">",Id("b"),Id("c")),BinaryOp("==",BinaryOp("<",Id("d"),Id("e")),Id("f")))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,341))
    def test_42(self):
        """AST_Test_42"""
        input = """
        int main(){
            int number;
            number[4]=foo[(1)[1]];
        }

        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("number",IntType()),BinaryOp("=",ArrayCell(Id("number"),IntLiteral(4)),ArrayCell(Id("foo"),ArrayCell(IntLiteral(1),IntLiteral(1))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,342))
    def test_43(self):
        """AST_Test_43"""
        input = """
        void foo(int a[]){foo()[(2+4)*3] = b+3;}

        """
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl("a",ArrayPointerType(IntType()))],VoidType(),Block([BinaryOp("=",ArrayCell(CallExpr(Id("foo"),[]),BinaryOp("*",BinaryOp("+",IntLiteral(2),IntLiteral(4)),IntLiteral(3))),BinaryOp("+",Id("b"),IntLiteral(3)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,343))
    def test_44(self):
        """AST_Test_44"""
        input = """float test(){
            int a[4],b[5],c[6],d;
            {
                a=2;
                b=3;
                c=4;
                d=a+b+c;
            }
        }"""
        expect = str(Program([FuncDecl(Id("test"),[],FloatType(),Block([VarDecl("a",ArrayType(4,IntType())),VarDecl("b",ArrayType(5,IntType())),VarDecl("c",ArrayType(6,IntType())),VarDecl("d",IntType()),Block([BinaryOp("=",Id("a"),IntLiteral(2)),BinaryOp("=",Id("b"),IntLiteral(3)),BinaryOp("=",Id("c"),IntLiteral(4)),BinaryOp("=",Id("d"),BinaryOp("+",BinaryOp("+",Id("a"),Id("b")),Id("c")))])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,344))
    def test_45(self):
        """AST_Test_45"""
        input = """int main(){
            a<=3;
        }"""
        expect = "successful"
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("<=",Id("a"),IntLiteral(3))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,345))
    def test_46(self):
        """AST_Test_46"""
        input = """int main(){
            a-b-c; 
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("-",BinaryOp("-",Id("a"),Id("b")),Id("c"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,346))
    def test_47(self):
        """AST_Test_47"""
        input = """void main(){
          float a,b;
          a=1.3;
          b=1.2;
          print(a+b);
          if (a>=b) {
              continue;
          } else return;
          for (i=0;i<=10;i=i+1) {
              print(i);
          }
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",FloatType()),VarDecl("b",FloatType()),BinaryOp("=",Id("a"),FloatLiteral(1.3)),BinaryOp("=",Id("b"),FloatLiteral(1.2)),CallExpr(Id("print"),[BinaryOp("+",Id("a"),Id("b"))]),If(BinaryOp(">=",Id("a"),Id("b")),Block([Continue()]),Return()),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<=",Id("i"),IntLiteral(10)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([CallExpr(Id("print"),[Id("i")])]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,347))
    def test_48(self):
        """AST_Test_48"""
        input = """int[] check(int b[]) {
        int a[1];
        boolean c;
        c=true;
        if (!c) return a;
        else return b ;
        }"""
        expect = str(Program([FuncDecl(Id("check"),[VarDecl("b",ArrayPointerType(IntType()))],ArrayPointerType(IntType()),Block([VarDecl("a",ArrayType(1,IntType())),VarDecl("c",BoolType()),BinaryOp("=",Id("c"),BooleanLiteral(True)),If(UnaryOp("!",Id("c")),Return(Id("a")),Return(Id("b")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,348))
    def test_49(self):
        """AST_Test_49"""
        input = """float test(){
            foo(2)[a[2+x]] = a[b[2]] +3;
        }"""
        expect = str(Program([FuncDecl(Id("test"),[],FloatType(),Block([BinaryOp("=",ArrayCell(CallExpr(Id("foo"),[IntLiteral(2)]),ArrayCell(Id("a"),BinaryOp("+",IntLiteral(2),Id("x")))),BinaryOp("+",ArrayCell(Id("a"),ArrayCell(Id("b"),IntLiteral(2))),IntLiteral(3)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,349))
    def test_50(self):
        """AST_Test_50"""
        input = """void main(){
           int a,b,c;
           a=b=c=1;
           float f[6];
           if (a==b) f[0]=1;
        }   
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),BinaryOp("=",Id("a"),BinaryOp("=",Id("b"),BinaryOp("=",Id("c"),IntLiteral(1)))),VarDecl("f",ArrayType(6,FloatType())),If(BinaryOp("==",Id("a"),Id("b")),BinaryOp("=",ArrayCell(Id("f"),IntLiteral(0)),IntLiteral(1)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,350))
    def test_51(self):
        """AST_Test_51"""
        input = """
        void cacul(int a,int b,int c){
            if ((a<b)<c) {
                for (i=0;i<10000000000;i=i+1){
                    for (j=0;j<10000000000;j=j+1){
                        for (k=0;k<10000000000;k=k+1) {
                            for (l=0;l<10000000000;l=l+1) {
                                for (m=0;m<10000000000;m=m+1) {
                                    for (n=0;n<10000000000;n=n+1) {
                                        if (i==9999999999) break; else {
                                            print(a+b+c);
                                            }
                                    }
                                }
                            }
                        }
                    }
                }
            }
            return ;
        }   
        void main(){
            cacul(69,69,69);
        }
        
        """
        expect = str(Program([FuncDecl(Id("cacul"),[VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType())],VoidType(),Block([If(BinaryOp("<",BinaryOp("<",Id("a"),Id("b")),Id("c")),Block([For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),IntLiteral(10000000000)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([For(BinaryOp("=",Id("j"),IntLiteral(0)),BinaryOp("<",Id("j"),IntLiteral(10000000000)),BinaryOp("=",Id("j"),BinaryOp("+",Id("j"),IntLiteral(1))),Block([For(BinaryOp("=",Id("k"),IntLiteral(0)),BinaryOp("<",Id("k"),IntLiteral(10000000000)),BinaryOp("=",Id("k"),BinaryOp("+",Id("k"),IntLiteral(1))),Block([For(BinaryOp("=",Id("l"),IntLiteral(0)),BinaryOp("<",Id("l"),IntLiteral(10000000000)),BinaryOp("=",Id("l"),BinaryOp("+",Id("l"),IntLiteral(1))),Block([For(BinaryOp("=",Id("m"),IntLiteral(0)),BinaryOp("<",Id("m"),IntLiteral(10000000000)),BinaryOp("=",Id("m"),BinaryOp("+",Id("m"),IntLiteral(1))),Block([For(BinaryOp("=",Id("n"),IntLiteral(0)),BinaryOp("<",Id("n"),IntLiteral(10000000000)),BinaryOp("=",Id("n"),BinaryOp("+",Id("n"),IntLiteral(1))),Block([If(BinaryOp("==",Id("i"),IntLiteral(9999999999)),Break(),Block([CallExpr(Id("print"),[BinaryOp("+",BinaryOp("+",Id("a"),Id("b")),Id("c"))])]))]))]))]))]))]))]))])),Return()])),FuncDecl(Id("main"),[],VoidType(),Block([CallExpr(Id("cacul"),[IntLiteral(69),IntLiteral(69),IntLiteral(69)])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,351))
    def test_52(self):
        """AST_Test_52"""
        input = """float test(int a,float b){
            int a,b;
            a=10;
            {
                int a[5];
            }
            {
                do 
                    if (a=10) {
                        if (a==2) {
                            for (x;y;z) {
                                for(a;b;c){
                                    for (t;u;v) {
                                        break;
                                    }
                                }
                            }
                        }
                    } else break;
                    a=a-1;
                 while a>0;
            }
        }"""
        expect = str(Program([FuncDecl(Id("test"),[VarDecl("a",IntType()),VarDecl("b",FloatType())],FloatType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),BinaryOp("=",Id("a"),IntLiteral(10)),Block([VarDecl("a",ArrayType(5,IntType()))]),Block([Dowhile([If(BinaryOp("=",Id("a"),IntLiteral(10)),Block([If(BinaryOp("==",Id("a"),IntLiteral(2)),Block([For(Id("x"),Id("y"),Id("z"),Block([For(Id("a"),Id("b"),Id("c"),Block([For(Id("t"),Id("u"),Id("v"),Block([Break()]))]))]))]))]),Break()),BinaryOp("=",Id("a"),BinaryOp("-",Id("a"),IntLiteral(1)))],BinaryOp(">",Id("a"),IntLiteral(0)))])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,352))
    def test_53(self):
        """AST_Test_53"""
        input = """float test(int a,float b){
            int a,b;
            a=10;
            {
                int a[5];
            }
            {
                do {}
                    
                while (a>0);
            }
        }"""
        expect = str(Program([FuncDecl(Id("test"),[VarDecl("a",IntType()),VarDecl("b",FloatType())],FloatType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),BinaryOp("=",Id("a"),IntLiteral(10)),Block([VarDecl("a",ArrayType(5,IntType()))]),Block([Dowhile([Block([])],BinaryOp(">",Id("a"),IntLiteral(0)))])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,353))
    def test_54(self):
        """AST_Test_54"""
        input = """int add(int a,int b){
            return a+b;
        }
            void main(){
                a=5;
                b=6;
                print(add(a,b));
            }"""
        expect = str(Program([FuncDecl(Id("add"),[VarDecl("a",IntType()),VarDecl("b",IntType())],IntType(),Block([Return(BinaryOp("+",Id("a"),Id("b")))])),FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("=",Id("a"),IntLiteral(5)),BinaryOp("=",Id("b"),IntLiteral(6)),CallExpr(Id("print"),[CallExpr(Id("add"),[Id("a"),Id("b")])])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,354))
    def test_55(self):
        """AST_Test_55"""
        input="""
        void main() 
        {
            if (a) b(); else c();
            do {
                for (i = 0; i < 1000; i = i + 1)foo();
                if (value == 1000) {
                    abc();
                } else {
                    if (a)
                        if (b)
                            foo();
                        else 
                            baz();
                }
            } while (value != 2000);
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([If(Id("a"),CallExpr(Id("b"),[]),CallExpr(Id("c"),[])),Dowhile([Block([For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),IntLiteral(1000)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),CallExpr(Id("foo"),[])),If(BinaryOp("==",Id("value"),IntLiteral(1000)),Block([CallExpr(Id("abc"),[])]),Block([If(Id("a"),If(Id("b"),CallExpr(Id("foo"),[]),CallExpr(Id("baz"),[])))]))])],BinaryOp("!=",Id("value"),IntLiteral(2000)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,355))
    def test_56(self):
        """AST_Test_56"""
        input="""
        void foo() {
            a = a * b + c / d;
        }
        """
        expect = str(Program([FuncDecl(Id("foo"),[],VoidType(),Block([BinaryOp("=",Id("a"),BinaryOp("+",BinaryOp("*",Id("a"),Id("b")),BinaryOp("/",Id("c"),Id("d"))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,356))
    def test_57(self):
        """AST_Test_57"""
        input="""
        void main() {
            a = b / (c / d) / (e % (f * g));
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("=",Id("a"),BinaryOp("/",BinaryOp("/",Id("b"),BinaryOp("/",Id("c"),Id("d"))),BinaryOp("%",Id("e"),BinaryOp("*",Id("f"),Id("g")))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,357))
    def test_58(self):
        """AST_Test_58"""
        input="""
        boolean test() {
            boolean b;
            b=((a && b)|| (a!=3));
            }
        
        """
        expect = str(Program([FuncDecl(Id("test"),[],BoolType(),Block([VarDecl("b",BoolType()),BinaryOp("=",Id("b"),BinaryOp("||",BinaryOp("&&",Id("a"),Id("b")),BinaryOp("!=",Id("a"),IntLiteral(3))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,358))
    def test_59(self):
        """AST_Test_59"""
        input="""
        void main() {
            if (a == b)
                if (c == d)
                    foo();
                else
                {
                 

                }
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([If(BinaryOp("==",Id("a"),Id("b")),If(BinaryOp("==",Id("c"),Id("d")),CallExpr(Id("foo"),[]),Block([])))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,359))
    def test_60(self):
        """AST_Test_60"""
        input="""
        int foo(int value) {
            if (value > 0)
                return value;
            else return foo(-value);
        }
        """
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl("value",IntType())],IntType(),Block([If(BinaryOp(">",Id("value"),IntLiteral(0)),Return(Id("value")),Return(CallExpr(Id("foo"),[UnaryOp("-",Id("value"))])))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,360))
    def test_61(self):
        """AST_Test_62"""
        input="""
        void func() {
            a = ((((((((b))))))));
        }
        """
        expect = str(Program([FuncDecl(Id("func"),[],VoidType(),Block([BinaryOp("=",Id("a"),Id("b"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,361))
    def test_62(self):
        """AST_Test_62"""
        input="""
        int[] func(int a[],int a[],int a[]) {}
        """
        expect = str(Program([FuncDecl(Id("func"),[VarDecl("a",ArrayPointerType(IntType())),VarDecl("a",ArrayPointerType(IntType())),VarDecl("a",ArrayPointerType(IntType()))],ArrayPointerType(IntType()),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,362))
    def test_63(self):
        """AST_Test_63"""
        input="""
        int[] func() {}
        """
        expect = str(Program([FuncDecl(Id("func"),[],ArrayPointerType(IntType()),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,363))
    def test_64(self):
        """AST_Test_64"""
        input="""
        int func() {
            value = s[1] + b[2-d[3+e[5-f[6-sin(8)]]]];
        }
        """
        expect = str(Program([FuncDecl(Id("func"),[],IntType(),Block([BinaryOp("=",Id("value"),BinaryOp("+",ArrayCell(Id("s"),IntLiteral(1)),ArrayCell(Id("b"),BinaryOp("-",IntLiteral(2),ArrayCell(Id("d"),BinaryOp("+",IntLiteral(3),ArrayCell(Id("e"),BinaryOp("-",IntLiteral(5),ArrayCell(Id("f"),BinaryOp("-",IntLiteral(6),CallExpr(Id("sin"),[IntLiteral(8)])))))))))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,364))
    def test_65(self):
        """AST_Test_65"""
        input="""
        int func() {
            int i;
            do
                {
                    int j;
                }
            while ((i=i - 1)>0);
        }
        """
        expect = str(Program([FuncDecl(Id("func"),[],IntType(),Block([VarDecl("i",IntType()),Dowhile([Block([VarDecl("j",IntType())])],BinaryOp(">",BinaryOp("=",Id("i"),BinaryOp("-",Id("i"),IntLiteral(1))),IntLiteral(0)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,365))
    def test_66(self):
        """AST_Test_66"""
        input="""
        int foo(){
            for (i = 0; i < 10; i = i + 1)
                for (i = 0; i < 10; i = i + 1)
                    for (i = 0; i < 10; i = i + 1)
                        for (i = 0; i < 10; i = i + 1)
                            i = i - 1;
        }
        """
        expect = str(Program([FuncDecl(Id("foo"),[],IntType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),IntLiteral(10)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),IntLiteral(10)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),IntLiteral(10)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),IntLiteral(10)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),BinaryOp("=",Id("i"),BinaryOp("-",Id("i"),IntLiteral(1)))))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,366))
    def test_67(self):
        """AST_Test_67"""
        input="""
        int foo(){
            int value[3];
            value[0] = 1;
            value[1] = 2;
            value[2] = value[value[0]];
        }
        """
        expect = str(Program([FuncDecl(Id("foo"),[],IntType(),Block([VarDecl("value",ArrayType(3,IntType())),BinaryOp("=",ArrayCell(Id("value"),IntLiteral(0)),IntLiteral(1)),BinaryOp("=",ArrayCell(Id("value"),IntLiteral(1)),IntLiteral(2)),BinaryOp("=",ArrayCell(Id("value"),IntLiteral(2)),ArrayCell(Id("value"),ArrayCell(Id("value"),IntLiteral(0))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,367))
    def test_68(self):
        """AST_Test_68"""
        input="""
        int a(){{{(a);}}}
        int foo() {
            
        }
        """
        expect = str(Program([FuncDecl(Id("a"),[],IntType(),Block([Block([Block([Id("a")])])])),FuncDecl(Id("foo"),[],IntType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,368))
    def test_69(self):
        """AST_Test_69"""
        input="""
        void foo() {
            if (a == b)
                if (c == d)
                    if (e == f)
                        if (a)
                            if (b)
                                if(c)
                                    foo();
                                else
                                    a;
                            else
                                b;
                        else 
                            c;
                    else 
                        d;
        }
        """
        expect = str(Program([FuncDecl(Id("foo"),[],VoidType(),Block([If(BinaryOp("==",Id("a"),Id("b")),If(BinaryOp("==",Id("c"),Id("d")),If(BinaryOp("==",Id("e"),Id("f")),If(Id("a"),If(Id("b"),If(Id("c"),CallExpr(Id("foo"),[]),Id("a")),Id("b")),Id("c")),Id("d"))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,369))
    def test_70(self):
        """AST_Test_70"""
        input="""
        void main(string s[]) {
           s= /* comment */b;
           // int s[b];
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("s",ArrayPointerType(StringType()))],VoidType(),Block([BinaryOp("=",Id("s"),Id("b"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,370))
    def test_71(self):
        """AST_Test_71"""
        input="""
        void main(){
            if ( a && b )
            {
                if( a || b )
                    a || b ;
            }
            else
                a && b ;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([If(BinaryOp("&&",Id("a"),Id("b")),Block([If(BinaryOp("||",Id("a"),Id("b")),BinaryOp("||",Id("a"),Id("b")))]),BinaryOp("&&",Id("a"),Id("b")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,371))
    def test_72(self):
        """AST_Test_72"""
        input="""
        int main(){
            if (a == b){
                if((a == b)){
                    if(((a == b))){ return 1; }
                    else{
                        return 0;
                    }
                }
            }
            else{
                if(a != b)
                {
                    return 0; 
                }
                else
                    return 1;
                
            }
        }
        """          
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp("==",Id("a"),Id("b")),Block([If(BinaryOp("==",Id("a"),Id("b")),Block([If(BinaryOp("==",Id("a"),Id("b")),Block([Return(IntLiteral(1))]),Block([Return(IntLiteral(0))]))]))]),Block([If(BinaryOp("!=",Id("a"),Id("b")),Block([Return(IntLiteral(0))]),Return(IntLiteral(1)))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,372))
    def test_73(self):
        """AST_Test_73"""
        input="""
        void main(){
        do
            {int a;}
            a = 0;
            a = a + 1;
            do
                {boolean b;}
                b = true;
                b = false; 
                do
                    do{}
                    while b == 1;
                while b != 1;
            while a == 0;
        while a != 0;
        } 
        """          
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([Dowhile([Block([VarDecl("a",IntType())]),BinaryOp("=",Id("a"),IntLiteral(0)),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),Dowhile([Block([VarDecl("b",BoolType())]),BinaryOp("=",Id("b"),BooleanLiteral(True)),BinaryOp("=",Id("b"),BooleanLiteral(False)),Dowhile([Dowhile([Block([])],BinaryOp("==",Id("b"),IntLiteral(1)))],BinaryOp("!=",Id("b"),IntLiteral(1)))],BinaryOp("==",Id("a"),IntLiteral(0)))],BinaryOp("!=",Id("a"),IntLiteral(0)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,373))
    def test_74(self):
        """AST_Test_56"""
        input="""
        int foo(int a, float b[])
        {
            boolean c;
            int i;
            i = a + 3 ;
            if (i > 0) {
                int d;
                d = i + 3;
                putInt( d );
            }
            return i;
        }
        """
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl("a",IntType()),VarDecl("b",ArrayPointerType(FloatType()))],IntType(),Block([VarDecl("c",BoolType()),VarDecl("i",IntType()),BinaryOp("=",Id("i"),BinaryOp("+",Id("a"),IntLiteral(3))),If(BinaryOp(">",Id("i"),IntLiteral(0)),Block([VarDecl("d",IntType()),BinaryOp("=",Id("d"),BinaryOp("+",Id("i"),IntLiteral(3))),CallExpr(Id("putInt"),[Id("d")])])),Return(Id("i"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,374))
    def test_75(self):
        """AST_Test_75"""
        input="""
        int i;
        int f() {
            return 200;
        }
        void main () {
            int main ;
            main = f() ;
            putIntLn( main ) ;
            {
                int i ;
                int main ;
                int f ;
                main = f = i = 100;
                putIntLn( i ) ;
                putIntLn( main ) ;
                putIntLn ( f ) ;
            }
            putIntLn( main ) ;
        }
        """
        expect = str(Program([VarDecl("i",IntType()),FuncDecl(Id("f"),[],IntType(),Block([Return(IntLiteral(200))])),FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("main",IntType()),BinaryOp("=",Id("main"),CallExpr(Id("f"),[])),CallExpr(Id("putIntLn"),[Id("main")]),Block([VarDecl("i",IntType()),VarDecl("main",IntType()),VarDecl("f",IntType()),BinaryOp("=",Id("main"),BinaryOp("=",Id("f"),BinaryOp("=",Id("i"),IntLiteral(100)))),CallExpr(Id("putIntLn"),[Id("i")]),CallExpr(Id("putIntLn"),[Id("main")]),CallExpr(Id("putIntLn"),[Id("f")])]),CallExpr(Id("putIntLn"),[Id("main")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,375))
    def test_76(self):
        """AST_Test_76"""
        input="""
        int checkPrimeNumber(int n)
        {
            int j, flag;
            flag = 1;
            for(j = 2; j <= n/2; j = j + 1)
            {
                if (n%j == 0)
                {
                    flag =0 ;
                    break;
                }
            }
            return flag;
        }
        """
        expect = str(Program([FuncDecl(Id("checkPrimeNumber"),[VarDecl("n",IntType())],IntType(),Block([VarDecl("j",IntType()),VarDecl("flag",IntType()),BinaryOp("=",Id("flag"),IntLiteral(1)),For(BinaryOp("=",Id("j"),IntLiteral(2)),BinaryOp("<=",Id("j"),BinaryOp("/",Id("n"),IntLiteral(2))),BinaryOp("=",Id("j"),BinaryOp("+",Id("j"),IntLiteral(1))),Block([If(BinaryOp("==",BinaryOp("%",Id("n"),Id("j")),IntLiteral(0)),Block([BinaryOp("=",Id("flag"),IntLiteral(0)),Break()]))])),Return(Id("flag"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,376))
    def test_77(self):
        """AST_Test_77"""
        input="""
        void main(){
            if ( a && b )
            {
                if( a || b ){a || b ;}
                else
                {}
            }
            else{a && b ;}
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([If(BinaryOp("&&",Id("a"),Id("b")),Block([If(BinaryOp("||",Id("a"),Id("b")),Block([BinaryOp("||",Id("a"),Id("b"))]),Block([]))]),Block([BinaryOp("&&",Id("a"),Id("b"))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,377))
    def test_78(self):
        """AST_Test_78"""
        input="""
        float main(float main, float main){}
        int main(){}
        """
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("main",FloatType()),VarDecl("main",FloatType())],FloatType(),Block([])),FuncDecl(Id("main"),[],IntType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,378))
    def test_79(self):
        """AST_Test_79"""
        input="""
        int main(){
            do {} while a<2;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Dowhile([Block([])],BinaryOp("<",Id("a"),IntLiteral(2)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,379))
    def test_80(self):
        """AST_Test_80"""
        input="""
        int main(){
            !a;
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([UnaryOp("!",Id("a"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,380))
    def test_81(self):
        """AST_Test_81"""
        input="""
        float test(int a,float b){
            int a,b;
            a=10;
            {
                int a[5];
            }
            {
                do 
                    if (a=10) {
                        if (a==2) {
                            for (x;y;z) {
                                for(a;b;c){
                                    for (t;u;v) {
                                        break;
                                    }
                                }
                            }
                        }
                    } else break;
                    a=a-1;
                 while a>0;
            }
        }
        """
        expect = str(Program([FuncDecl(Id("test"),[VarDecl("a",IntType()),VarDecl("b",FloatType())],FloatType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),BinaryOp("=",Id("a"),IntLiteral(10)),Block([VarDecl("a",ArrayType(5,IntType()))]),Block([Dowhile([If(BinaryOp("=",Id("a"),IntLiteral(10)),Block([If(BinaryOp("==",Id("a"),IntLiteral(2)),Block([For(Id("x"),Id("y"),Id("z"),Block([For(Id("a"),Id("b"),Id("c"),Block([For(Id("t"),Id("u"),Id("v"),Block([Break()]))]))]))]))]),Break()),BinaryOp("=",Id("a"),BinaryOp("-",Id("a"),IntLiteral(1)))],BinaryOp(">",Id("a"),IntLiteral(0)))])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,381))
    def test_82(self):
        """AST_Test_82"""
        input="""
        float test(){
            int a[4],b[5],c[6],d;
            {
                a=2;
                b=3;
                c=4;
                d=a+b+c;
            }
        }
        """
        expect = str(Program([FuncDecl(Id("test"),[],FloatType(),Block([VarDecl("a",ArrayType(4,IntType())),VarDecl("b",ArrayType(5,IntType())),VarDecl("c",ArrayType(6,IntType())),VarDecl("d",IntType()),Block([BinaryOp("=",Id("a"),IntLiteral(2)),BinaryOp("=",Id("b"),IntLiteral(3)),BinaryOp("=",Id("c"),IntLiteral(4)),BinaryOp("=",Id("d"),BinaryOp("+",BinaryOp("+",Id("a"),Id("b")),Id("c")))])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,382))
    def test_83(self):
        """AST_Test_83"""
        input="""
        void main(){
            int array[5];
        }   
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("array",ArrayType(5,IntType()))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,383))
    def test_84(self):
        """AST_Test_84"""
        input="""
        int main() { 
            int i;
            i = 20; 
            if (i < 15) 
                printf("i is smaller than 15"); 
            else
                printf("i is greater than 15");      
            return 0;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("i",IntType()),BinaryOp("=",Id("i"),IntLiteral(20)),If(BinaryOp("<",Id("i"),IntLiteral(15)),CallExpr(Id("printf"),[StringLiteral("i is smaller than 15")]),CallExpr(Id("printf"),[StringLiteral("i is greater than 15")])),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,384))
    def test_85(self):
        """AST_Test_85"""
        input="""
        int main()
        {
            int i, j;
            do{
                j = 1;
                do{
                    j = j + 1;
                } while ( j <= 10 );
                i = i + 1;
            } while ( i <= 10 );
            return 0;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("i",IntType()),VarDecl("j",IntType()),Dowhile([Block([BinaryOp("=",Id("j"),IntLiteral(1)),Dowhile([Block([BinaryOp("=",Id("j"),BinaryOp("+",Id("j"),IntLiteral(1)))])],BinaryOp("<=",Id("j"),IntLiteral(10))),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))])],BinaryOp("<=",Id("i"),IntLiteral(10))),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,385))
    def test_86(self):
        """AST_Test_86"""
        input="""
        int main(){
            for(i = 0; i < 10 ; i = i + 1)
                if( i == 0)
            break ;
            else
                continue;
                int j;
                j = 10;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),IntLiteral(10)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),If(BinaryOp("==",Id("i"),IntLiteral(0)),Break(),Continue())),VarDecl("j",IntType()),BinaryOp("=",Id("j"),IntLiteral(10))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,386))
    def test_87(self):
        """AST_Test_87"""
        input="""
        int main(int argc){
            int a;
            { 

            }
            return 0 + 0;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("argc",IntType())],IntType(),Block([VarDecl("a",IntType()),Block([]),Return(BinaryOp("+",IntLiteral(0),IntLiteral(0)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,387))
    def test_88(self):
        """AST_Test_88"""
        input="""
        int main(){
            ((arr))[5];
            ((foo()))[5]; 
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([ArrayCell(Id("arr"),IntLiteral(5)),ArrayCell(CallExpr(Id("foo"),[]),IntLiteral(5))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,388))
    def test_89(self):
        """AST_Test_89"""
        input="""
        int main(){
            arr [(arr[5])]; 
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([ArrayCell(Id("arr"),ArrayCell(Id("arr"),IntLiteral(5)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,389))
    def test_90(self):
        """AST_Test_56"""
        input="""
        int main(){
            arr[((i))];
            
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([ArrayCell(Id("arr"),Id("i"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,390))
    def test_91(self):
        """AST_Test_91"""
        input="""
        int main(){
            func(arr[num], arr[num + 1], arr[num + 2]);
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("func"),[ArrayCell(Id("arr"),Id("num")),ArrayCell(Id("arr"),BinaryOp("+",Id("num"),IntLiteral(1))),ArrayCell(Id("arr"),BinaryOp("+",Id("num"),IntLiteral(2)))])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,391))
    def test_92(self):
        """AST_Test_92"""
        input="""
        void main(){
        do {} {} {} {} {} {}{}{}{}{}{}{}{{}{}{}{}{}{{}{}{}{}{}{}{}}}
        {} 
        while a == b ;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([Dowhile([Block([]),Block([]),Block([]),Block([]),Block([]),Block([]),Block([]),Block([]),Block([]),Block([]),Block([]),Block([]),Block([Block([]),Block([]),Block([]),Block([]),Block([]),Block([Block([]),Block([]),Block([]),Block([]),Block([]),Block([]),Block([])])]),Block([])],BinaryOp("==",Id("a"),Id("b")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,392))
    def test_93(self):
        """AST_Test_93"""
        input="""
        boolean[] main(){}
        """
        expect = str(Program([FuncDecl(Id("main"),[],ArrayPointerType(BoolType()),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,393))
    def test_94(self):
        """AST_Test_94"""
        input="""
        float foo(int a, string str[], float f, boolean bool[]){}
        """
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl("a",IntType()),VarDecl("str",ArrayPointerType(StringType())),VarDecl("f",FloatType()),VarDecl("bool",ArrayPointerType(BoolType()))],FloatType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,394))
    def test_95(self):
        """AST_Test_95"""
        input="""
        void main(){
            if ( a && b )
                if( a || b )
                    a || b ;
            else
                a && b ;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([If(BinaryOp("&&",Id("a"),Id("b")),If(BinaryOp("||",Id("a"),Id("b")),BinaryOp("||",Id("a"),Id("b")),BinaryOp("&&",Id("a"),Id("b"))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,395))
    def test_96(self):
        """AST_Test_96"""
        input="""
        void main(){
            if (a && b)
            if (a || b)
            if (a == b)
            if (a != b)
            if (a > b)
            if (a < b){}
            else
            {if (a >= b){}}
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([If(BinaryOp("&&",Id("a"),Id("b")),If(BinaryOp("||",Id("a"),Id("b")),If(BinaryOp("==",Id("a"),Id("b")),If(BinaryOp("!=",Id("a"),Id("b")),If(BinaryOp(">",Id("a"),Id("b")),If(BinaryOp("<",Id("a"),Id("b")),Block([]),Block([If(BinaryOp(">=",Id("a"),Id("b")),Block([]))])))))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,396))
    def test_97(self):
        """AST_Test_97"""
        input="""
        void main(){
        do {
            do {} while (a<0);
            do {{{int i;}}} while b<0;
        } {} {} {} {} do {{if(a){}}} while 5 == 0 ;
        while 5 >= 10 ;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([Dowhile([Block([Dowhile([Block([])],BinaryOp("<",Id("a"),IntLiteral(0))),Dowhile([Block([Block([Block([VarDecl("i",IntType())])])])],BinaryOp("<",Id("b"),IntLiteral(0)))]),Block([]),Block([]),Block([]),Block([]),Dowhile([Block([Block([If(Id("a"),Block([]))])])],BinaryOp("==",IntLiteral(5),IntLiteral(0)))],BinaryOp(">=",IntLiteral(5),IntLiteral(10)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,397))
    def test_98(self):
        """AST_Test_98"""
        input="""
        float exception(boolean a){}
        """
        expect = str(Program([FuncDecl(Id("exception"),[VarDecl("a",BoolType())],FloatType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,398))
    def test_99(self):
        """AST_Test_99"""
        input="""
        int a;
        string str(int dfx){
            int a;
        }
        """
        expect = str(Program([VarDecl("a",IntType()),FuncDecl(Id("str"),[VarDecl("dfx",IntType())],StringType(),Block([VarDecl("a",IntType())]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,399))
    def test_100(self):
        """AST_Test_100"""
        input="""
        void main(){
            for (x; x< 0; x=x+1)
                return exp;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([For(Id("x"),BinaryOp("<",Id("x"),IntLiteral(0)),BinaryOp("=",Id("x"),BinaryOp("+",Id("x"),IntLiteral(1))),Return(Id("exp")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,400))
    