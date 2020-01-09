import unittest
from TestUtils import TestAST
from AST import*


class ASTGenSuite(unittest.TestCase):

    def test_1(self):
        """ """
        input = """int a[1], b;
            void main(){
                int i, temp;
                for(i=1;i<10;i=i+1)
                    {
                        if(temp<10)
                            temp=temp+1;
                    }
                return;
            }"""
        expect = str(Program([VarDecl("a",ArrayType(1,IntType())),VarDecl("b",IntType()),FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("i",IntType()),VarDecl("temp",IntType()),For(BinaryOp("=",Id("i"),IntLiteral(1)),BinaryOp("<",Id("i"),IntLiteral(10)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([If(BinaryOp("<",Id("temp"),IntLiteral(10)),BinaryOp("=",Id("temp"),BinaryOp("+",Id("temp"),IntLiteral(1))))])),Return()]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 301))

    def test_2(self):
        """ """
        input = """int foo(int a[])
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
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl("a",ArrayPointerType(IntType()))],IntType(),Block([Return(ArrayCell(Id("a"),IntLiteral(0)))])),FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("arr",ArrayType(10,IntType())),VarDecl("f",FloatType()),BinaryOp("=",Id("f"),IntLiteral(0)),Dowhile([BinaryOp("=",Id("f"),BinaryOp("+",Id("f"),CallExpr(Id("foo"),[Id("arr")]))),BinaryOp("=",Id("f"),BinaryOp("+",Id("f"),IntLiteral(1)))],BinaryOp("<",BinaryOp("+",CallExpr(Id("foo"),[Id("arr")]),Id("f")),IntLiteral(100))),Return()]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 302))

    def test_3(self):
        """ """
        input = """int a;
            float b;
            string c;
            int d[10];
            void main(){
                {

                }
                return;
            }"""
        expect = str(Program([VarDecl("a",IntType()),VarDecl("b",FloatType()),VarDecl("c",StringType()),VarDecl("d",ArrayType(10,IntType())),FuncDecl(Id("main"),[],VoidType(),Block([Block([]),Return()]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 303))

    def test_4(self):
        """ """
        input = """void main(){
                {
                    int a,b;
                    boolean c,d;
                    a = 10 ;
                    b = 5;
                    c = true;
                    d = c == (a>b);
                }
                {
                    a = a+b; 
                }
                return;
            }"""
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",BoolType()),VarDecl("d",BoolType()),BinaryOp("=",Id("a"),IntLiteral(10)),BinaryOp("=",Id("b"),IntLiteral(5)),BinaryOp("=",Id("c"),BooleanLiteral(True)),BinaryOp("=",Id("d"),BinaryOp("==",Id("c"),BinaryOp(">",Id("a"),Id("b"))))]),Block([BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),Id("b")))]),Return()]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 304))

    def test_5(self):
        """ """
        input = """int[] foo(){
                int a[5];
                return a;
            }
            void main(){
                foo();
                return;
            }"""
        expect = str(Program([FuncDecl(Id("foo"),[],ArrayPointerType(IntType()),Block([VarDecl("a",ArrayType(5,IntType())),Return(Id("a"))])),FuncDecl(Id("main"),[],VoidType(),Block([CallExpr(Id("foo"),[]),Return()]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 305))

    def test_6(self):
        """ """
        input = """void main(){
                return;
            }
            int a,b;"""
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([Return()])),VarDecl("a",IntType()),VarDecl("b",IntType())]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 306))

    def test_7(self):
        """ """
        input = """void main(){
                string str;
                str = "Chery Chery Lady\\n";
                int a;
                a = 10;
                return;
            }"""
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("str",StringType()),BinaryOp("=",Id("str"),StringLiteral("Chery Chery Lady\\n")),VarDecl("a",IntType()),BinaryOp("=",Id("a"),IntLiteral(10)),Return()]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 307))

    def test_8(self):
        """ """
        input = """
            int foo()
            {
                return 1;
            }
            void main()
            {
                int a;
                a=foo();
                return;
            }"""
        expect = str(Program([FuncDecl(Id("foo"),[],IntType(),Block([Return(IntLiteral(1))])),FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()),BinaryOp("=",Id("a"),CallExpr(Id("foo"),[])),Return()]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 308))

    def test_9(self):
        """ """
        input = """void main(){
                int a;
                {a =1;}
                if(a==1)
                    return;
                else                
                    return;
            }"""
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()),Block([BinaryOp("=",Id("a"),IntLiteral(1))]),If(BinaryOp("==",Id("a"),IntLiteral(1)),Return(),Return())]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 309))

    def test_10(self):
        """ """
        input = """int foo(int a){
                if((a%2)==0)
                    a=a+1;
                else
                    do a=a-1;
                    while a > 0;
                return a;
            }
            void main(){
                int a,b[10],i;
                a=10;
                for(i=0;i<10;i=i+1)
                    b[i]=foo(a);                
                return;
            }"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl("a",IntType())],IntType(),Block([If(BinaryOp("==",BinaryOp("%",Id("a"),IntLiteral(2)),IntLiteral(0)),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),Dowhile([BinaryOp("=",Id("a"),BinaryOp("-",Id("a"),IntLiteral(1)))],BinaryOp(">",Id("a"),IntLiteral(0)))),Return(Id("a"))])),FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()),VarDecl("b",ArrayType(10,IntType())),VarDecl("i",IntType()),BinaryOp("=",Id("a"),IntLiteral(10)),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),IntLiteral(10)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),BinaryOp("=",ArrayCell(Id("b"),Id("i")),CallExpr(Id("foo"),[Id("a")]))),Return()]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 310))

    def test_11(self):
        """ """
        input = """int main(){int a,b,c,d;}"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",IntType())]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 311))

    def test_12(self):
        """ """
        input = """int main(){int a[10],b,c,d;}"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",ArrayType(10,IntType())),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",IntType())]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 312))

    def test_13(self):
        """ """
        input = """int main(){int a[10];}"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",ArrayType(10,IntType()))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 313))

    def test_14(self):
        """ """
        input = """int main(){float a,b,c,d[10];}"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",FloatType()),VarDecl("b",FloatType()),VarDecl("c",FloatType()),VarDecl("d",ArrayType(10,FloatType()))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 314))

    def test_15(self):
        """ """
        input = """void foo(int i){}
                int child_of_foo(float f)
                {
        }"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl("i",IntType())],VoidType(),Block([])),FuncDecl(Id("child_of_foo"),[VarDecl("f",FloatType())],IntType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 315))

    def test_16(self):
        """ """
        input = """int[] foo(int a,float b[]) {
                int c[3];
                if(a>0) foo(a-1,b);
                else return c;
        }"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl("a",IntType()),VarDecl("b",ArrayPointerType(FloatType()))],ArrayPointerType(IntType()),Block([VarDecl("c",ArrayType(3,IntType())),If(BinaryOp(">",Id("a"),IntLiteral(0)),CallExpr(Id("foo"),[BinaryOp("-",Id("a"),IntLiteral(1)),Id("b")]),Return(Id("c")))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 316))

    def test_17(self):
        """ """
        input = """int main(){
            boolean boo; boo[2]=false;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("boo",BoolType()),BinaryOp("=",ArrayCell(Id("boo"),IntLiteral(2)),BooleanLiteral(False))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 317))

    def test_18(self):
        """ """
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
        self.assertTrue(TestAST.checkASTGen(input, expect, 318))

    def test_19(self):
        """ """
        input = """int main(){
            int a[1];
            a=foo(2)[3+x]=a[b[2]]+3;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",ArrayType(1,IntType())),BinaryOp("=",Id("a"),BinaryOp("=",ArrayCell(CallExpr(Id("foo"),[IntLiteral(2)]),BinaryOp("+",IntLiteral(3),Id("x"))),BinaryOp("+",ArrayCell(Id("a"),ArrayCell(Id("b"),IntLiteral(2))),IntLiteral(3))))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 319))

    def test_20(self):
        """ """
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
        self.assertTrue(TestAST.checkASTGen(input, expect, 320))

    def test_21(self):
        """ """
        input = """void main( ){ if (a) if (b) if (c) a; else a; else b;}"""
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([If(Id("a"),If(Id("b"),If(Id("c"),Id("a"),Id("a")),Id("b")))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 321))

    def test_22(self):
        """ """
        input = """int main(){"return";}"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([StringLiteral("return")]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 322))

    def test_23(self):
        """ """
        input = """int main(){
            if (n)
            {
                printName();    
            }
            else
            {
                putInt(10);
            }          
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(Id("n"),Block([CallExpr(Id("printName"),[])]),Block([CallExpr(Id("putInt"),[IntLiteral(10)])]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 323))

    def test_24(self):
        """ """
        input = """int main(){
            do{
                int a;
                a=10;
                
            }
            {

            }while("string");
          
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Dowhile([Block([VarDecl("a",IntType()),BinaryOp("=",Id("a"),IntLiteral(10))]),Block([])],StringLiteral("string"))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 324))

    def test_25(self):
        """ """
        input = """int main(){
            int i;
            for (i=0;i<10;i=i+1)
            {
                print("PPL");
            }   
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("i",IntType()),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),IntLiteral(10)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([CallExpr(Id("print"),[StringLiteral("PPL")])]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 325))

    def test_26(self):
        """ """
        input = """int main(){
            int a,b[10];
            for (i=0;i<10;i=i+1)
            {
                a=i;
                b[i]=i+(a+i)*a;
            }   
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",IntType()),VarDecl("b",ArrayType(10,IntType())),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),IntLiteral(10)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([BinaryOp("=",Id("a"),Id("i")),BinaryOp("=",ArrayCell(Id("b"),Id("i")),BinaryOp("+",Id("i"),BinaryOp("*",BinaryOp("+",Id("a"),Id("i")),Id("a"))))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 326))

    def test_27(self):
        """ """
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
        self.assertTrue(TestAST.checkASTGen(input, expect, 327))

    def test_28(self):
        """ """
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
        self.assertTrue(TestAST.checkASTGen(input, expect, 328))

    def test_29(self):
        """ """
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
        self.assertTrue(TestAST.checkASTGen(input, expect, 329))

    def test_30(self):
        """ """
        input = """int main(){
            for (i=0;i<10;i=i+1)
            {
                print("This is PPL");
                if (i==5)
                {
                    continue;
                }
                else
                {
                    break;
                }
            }
             
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),IntLiteral(10)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([CallExpr(Id("print"),[StringLiteral("This is PPL")]),If(BinaryOp("==",Id("i"),IntLiteral(5)),Block([Continue()]),Block([Break()]))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 330))

    def test_31(self):
        """ """
        input = """int main(){
            int i;
            i=10;
            print(i);
            system("pause");
            return 0;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("i",IntType()),BinaryOp("=",Id("i"),IntLiteral(10)),CallExpr(Id("print"),[Id("i")]),CallExpr(Id("system"),[StringLiteral("pause")]),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 331))

    def test_32(self):
        """ """
        input = """int main(){
            int i, a[1];
            i=1;
            a[0]=i+2;
            a[1]=100;
            foo(1,2);
            return 0; 
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("i",IntType()),VarDecl("a",ArrayType(1,IntType())),BinaryOp("=",Id("i"),IntLiteral(1)),BinaryOp("=",ArrayCell(Id("a"),IntLiteral(0)),BinaryOp("+",Id("i"),IntLiteral(2))),BinaryOp("=",ArrayCell(Id("a"),IntLiteral(1)),IntLiteral(100)),CallExpr(Id("foo"),[IntLiteral(1),IntLiteral(2)]),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 332))

    def test_33(self):
        """ """
        input = """int main(){
            i=foo(1);
            i=foo(i+2);
            i=100*i+foo(1,2);
            putInt(foo(1,2));
            return 0; 
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",Id("i"),CallExpr(Id("foo"),[IntLiteral(1)])),BinaryOp("=",Id("i"),CallExpr(Id("foo"),[BinaryOp("+",Id("i"),IntLiteral(2))])),BinaryOp("=",Id("i"),BinaryOp("+",BinaryOp("*",IntLiteral(100),Id("i")),CallExpr(Id("foo"),[IntLiteral(1),IntLiteral(2)]))),CallExpr(Id("putInt"),[CallExpr(Id("foo"),[IntLiteral(1),IntLiteral(2)])]),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 333))

    def test_34(self):
        """ """
        input = """int main(){
            int a,b,c;
            a=b=c=5;
            float f[5];
            if (a==b) f[0]=1.0; 
            return a+foo();     
        }
        int foo(){
            return 0;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),BinaryOp("=",Id("a"),BinaryOp("=",Id("b"),BinaryOp("=",Id("c"),IntLiteral(5)))),VarDecl("f",ArrayType(5,FloatType())),If(BinaryOp("==",Id("a"),Id("b")),BinaryOp("=",ArrayCell(Id("f"),IntLiteral(0)),FloatLiteral(1.0))),Return(BinaryOp("+",Id("a"),CallExpr(Id("foo"),[])))])),FuncDecl(Id("foo"),[],IntType(),Block([Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 334))

    def test_35(self):
        """ """
        input = """int main(){        
        {
            return 0;
        }
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Block([Return(IntLiteral(0))])]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 335))

    def test_36(self):
        """ """
        input = """int main(){
            boolean check;
            if(!check) print(check);
            else {
                print(!check);
            }                  
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("check",BoolType()),If(UnaryOp("!",Id("check")),CallExpr(Id("print"),[Id("check")]),Block([CallExpr(Id("print"),[UnaryOp("!",Id("check"))])]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 336))

    def test_37(self):
        """ """
        input = """int main(){ a=b==c;}"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",Id("a"),BinaryOp("==",Id("b"),Id("c")))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 337))

    def test_38(self):
        """ """
        input = """int main(){ boolean check; check=true;}"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("check",BoolType()),BinaryOp("=",Id("check"),BooleanLiteral(True))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 338))

    def test_39(self):
        """ """
        input = """int main(){if(b) if (a) if (c) {} else {} else {} }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(Id("b"),If(Id("a"),If(Id("c"),Block([]),Block([])),Block([])))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 339))

    def test_40(self):
        """ """
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
        }"""
        expect = str(Program([VarDecl("i",IntType()),FuncDecl(Id("f"),[],IntType(),Block([Return(IntLiteral(200))])),FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("test",IntType()),BinaryOp("=",Id("test"),CallExpr(Id("f"),[])),CallExpr(Id("putIntLn"),[Id("test")]),Block([VarDecl("i",IntType()),VarDecl("test",IntType()),VarDecl("f",IntType()),BinaryOp("=",Id("test"),BinaryOp("=",Id("f"),BinaryOp("=",Id("i"),IntLiteral(100)))),CallExpr(Id("putIntLn"),[Id("i")]),CallExpr(Id("putIntLn"),[Id("test")]),CallExpr(Id("putIntLn"),[Id("f")])]),CallExpr(Id("putIntLn"),[Id("test")])]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 340))

    def test_41(self):
        """ """
        input = """int main(){
        float array[2];}"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("array",ArrayType(2,FloatType()))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 341))

    def test_42(self):
        """ """
        input = """void main()
        {
            int a,b,c[2]; 
            c[a+b]=c[a-b]=c[-a];
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",ArrayType(2,IntType())),BinaryOp("=",ArrayCell(Id("c"),BinaryOp("+",Id("a"),Id("b"))),BinaryOp("=",ArrayCell(Id("c"),BinaryOp("-",Id("a"),Id("b"))),ArrayCell(Id("c"),UnaryOp("-",Id("a")))))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 342))

    def test_43(self):
        """ """
        input = """int x,y[8];
        int a,b,c;
        void main(){
            array[d[r[a(10)]]];
        }
        void rescusive(int i,float z){
            int x;
            int c;
            if(exp)
                stamentt;
            else
                stmt;
            for(w;i;z){
                int x;
                if(a==5)
                    x=5;
            
                for (exp1;exp2;exp3) printf();
                int x,y,arr[69];
            }
            return ;
        }"""
        expect = str(Program([VarDecl("x",IntType()),VarDecl("y",ArrayType(8,IntType())),VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),FuncDecl(Id("main"),[],VoidType(),Block([ArrayCell(Id("array"),ArrayCell(Id("d"),ArrayCell(Id("r"),CallExpr(Id("a"),[IntLiteral(10)]))))])),FuncDecl(Id("rescusive"),[VarDecl("i",IntType()),VarDecl("z",FloatType())],VoidType(),Block([VarDecl("x",IntType()),VarDecl("c",IntType()),If(Id("exp"),Id("stamentt"),Id("stmt")),For(Id("w"),Id("i"),Id("z"),Block([VarDecl("x",IntType()),If(BinaryOp("==",Id("a"),IntLiteral(5)),BinaryOp("=",Id("x"),IntLiteral(5))),For(Id("exp1"),Id("exp2"),Id("exp3"),CallExpr(Id("printf"),[])),VarDecl("x",IntType()),VarDecl("y",IntType()),VarDecl("arr",ArrayType(69,IntType()))])),Return()]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 343))

    def test_44(self):
        """ """
        input = """void func(){if(a<=b) {return a;}}"""
        expect = str(Program([FuncDecl(Id("func"),[],VoidType(),Block([If(BinaryOp("<=",Id("a"),Id("b")),Block([Return(Id("a"))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 344))

    def test_45(self):
        """ """
        input = """int main(){{{{{}}}}}"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Block([Block([Block([Block([])])])])]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 345))

    def test_46(self):
        """ """
        input = """string test(int test[],string test1){
            boolean check;
            check = false;
            if (check==true) 
                a=2; 
            else a=3;
        }"""
        expect = str(Program([FuncDecl(Id("test"),[VarDecl("test",ArrayPointerType(IntType())),VarDecl("test1",StringType())],StringType(),Block([VarDecl("check",BoolType()),BinaryOp("=",Id("check"),BooleanLiteral(False)),If(BinaryOp("==",Id("check"),BooleanLiteral(True)),BinaryOp("=",Id("a"),IntLiteral(2)),BinaryOp("=",Id("a"),IntLiteral(3)))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 346))

    def test_47(self):
        """ """
        input = """string test(int test[],string test1){
            if (a>b+c) 
                a=2; else a=3;
            return "kael99";
        }"""
        expect = str(Program([FuncDecl(Id("test"),[VarDecl("test",ArrayPointerType(IntType())),VarDecl("test1",StringType())],StringType(),Block([If(BinaryOp(">",Id("a"),BinaryOp("+",Id("b"),Id("c"))),BinaryOp("=",Id("a"),IntLiteral(2)),BinaryOp("=",Id("a"),IntLiteral(3))),Return(StringLiteral("kael99"))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 347))

    def test_48(self):
        """ """
        input = """float test(){
            int a[4],b[5],c[6],d;
            {
            }
        }"""
        expect = str(Program([FuncDecl(Id("test"),[],FloatType(),Block([VarDecl("a",ArrayType(4,IntType())),VarDecl("b",ArrayType(5,IntType())),VarDecl("c",ArrayType(6,IntType())),VarDecl("d",IntType()),Block([])]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 348))

    def test_49(self):
        """ """
        input = """int main(){
            int a[4],i;
            do putInt(4); i=i+1; while a[-foo(i)]==true;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",ArrayType(4,IntType())),VarDecl("i",IntType()),Dowhile([CallExpr(Id("putInt"),[IntLiteral(4)]),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))],BinaryOp("==",ArrayCell(Id("a"),UnaryOp("-",CallExpr(Id("foo"),[Id("i")]))),BooleanLiteral(True)))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 349))

    def test_50(self):
        """ """
        input = """int main(){
            do{} while a==true;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Dowhile([Block([])],BinaryOp("==",Id("a"),BooleanLiteral(True)))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 350))

    def test_51(self):
        """ """
        input = """int[] main(){ return getChild(tree,root);}"""
        expect = str(Program([FuncDecl(Id("main"),[],ArrayPointerType(IntType()),Block([Return(CallExpr(Id("getChild"),[Id("tree"),Id("root")]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 351))

    def test_52(self):
        """ """
        input = """int main(){
            boolean a;
            return !a;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",BoolType()),Return(UnaryOp("!",Id("a")))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 352))

    def test_53(self):
        """ """
        input = """int main(){
            if (a>b) 
                c=a; 
            else c=b; 
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp(">",Id("a"),Id("b")),BinaryOp("=",Id("c"),Id("a")),BinaryOp("=",Id("c"),Id("b")))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 353))

    def test_54(self):
        """ """
        input = """int main(){
            if (a<b) c=a; 
            else 
                if(c<b)
                    c=b;
                else
                    c=b;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp("<",Id("a"),Id("b")),BinaryOp("=",Id("c"),Id("a")),If(BinaryOp("<",Id("c"),Id("b")),BinaryOp("=",Id("c"),Id("b")),BinaryOp("=",Id("c"),Id("b"))))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 354))

    def test_55(self):
        """ """
        input = """int main(){
            for (i=0;i<10;i=i+1) 
                {
                    putInt(1);
                }
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),IntLiteral(10)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([CallExpr(Id("putInt"),[IntLiteral(1)])]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 355))

    def test_56(self):
        """ """
        input = """int main(){
             return a=b=c;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Return(BinaryOp("=",Id("a"),BinaryOp("=",Id("b"),Id("c"))))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 356))

    def test_57(self):
        """ """
        input = """int main(){
            a || b || c || d && e && f; 
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("||",BinaryOp("||",BinaryOp("||",Id("a"),Id("b")),Id("c")),BinaryOp("&&",BinaryOp("&&",Id("d"),Id("e")),Id("f")))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 357))

    def test_58(self):
        """ """
        input = """ int foo(){return 1;}
        int main(){
           return foo(2)[x+3];
        }"""
        expect = str(Program([FuncDecl(Id("foo"),[],IntType(),Block([Return(IntLiteral(1))])),FuncDecl(Id("main"),[],IntType(),Block([Return(ArrayCell(CallExpr(Id("foo"),[IntLiteral(2)]),BinaryOp("+",Id("x"),IntLiteral(3))))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 358))

    def test_59(self):
        """ """
        input = """int main(){
           foo(foo(2)[x+3])[1];
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([ArrayCell(CallExpr(Id("foo"),[ArrayCell(CallExpr(Id("foo"),[IntLiteral(2)]),BinaryOp("+",Id("x"),IntLiteral(3)))]),IntLiteral(1))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 359))

    def test_60(self):
        """ """
        input = """int[] main(){
           a=foo(2)[x+3]+foo(1)[x+2];
           return a;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],ArrayPointerType(IntType()),Block([BinaryOp("=",Id("a"),BinaryOp("+",ArrayCell(CallExpr(Id("foo"),[IntLiteral(2)]),BinaryOp("+",Id("x"),IntLiteral(3))),ArrayCell(CallExpr(Id("foo"),[IntLiteral(1)]),BinaryOp("+",Id("x"),IntLiteral(2))))),Return(Id("a"))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 360))

    def test_61(self):
        """ """
        input = """int main(){
            return a+foo(a+b,c*d); 
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Return(BinaryOp("+",Id("a"),CallExpr(Id("foo"),[BinaryOp("+",Id("a"),Id("b")),BinaryOp("*",Id("c"),Id("d"))])))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 361))

    def test_62(self):
        """ """
        input = """int main(){
            a=1/2+3*4-5/6;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",Id("a"),BinaryOp("-",BinaryOp("+",BinaryOp("/",IntLiteral(1),IntLiteral(2)),BinaryOp("*",IntLiteral(3),IntLiteral(4))),BinaryOp("/",IntLiteral(5),IntLiteral(6))))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 362))

    def test_63(self):
        """ """
        input = """int main(){
            return foo(2.0)[x+3]+2*foo(1.1e-2)[-x]*(x+1)-6%3;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Return(BinaryOp("-",BinaryOp("+",ArrayCell(CallExpr(Id("foo"),[FloatLiteral(2.0)]),BinaryOp("+",Id("x"),IntLiteral(3))),BinaryOp("*",BinaryOp("*",IntLiteral(2),ArrayCell(CallExpr(Id("foo"),[FloatLiteral(0.011)]),UnaryOp("-",Id("x")))),BinaryOp("+",Id("x"),IntLiteral(1)))),BinaryOp("%",IntLiteral(6),IntLiteral(3))))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 363))

    def test_64(self):
        """ """
        input = """void main(){
            a[b[c[foo(d)]]];
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([ArrayCell(Id("a"),ArrayCell(Id("b"),ArrayCell(Id("c"),CallExpr(Id("foo"),[Id("d")]))))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 364))

    def test_65(self):
        """ """
        input = """void main(){
            return !foo(a[b[c[foo(d)]]]);
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([Return(UnaryOp("!",CallExpr(Id("foo"),[ArrayCell(Id("a"),ArrayCell(Id("b"),ArrayCell(Id("c"),CallExpr(Id("foo"),[Id("d")]))))])))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 365))

    def test_66(self):
        """ """
        input = """int[] main(){
            int x[1];
            funcall(x);
            return x;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],ArrayPointerType(IntType()),Block([VarDecl("x",ArrayType(1,IntType())),CallExpr(Id("funcall"),[Id("x")]),Return(Id("x"))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 366))

    def test_67(self):
        """ """
        input = """void main(){
            if(a>0) 
                if(!b) 
                    if(b==c) break; 
                    else continue; 
                else return;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([If(BinaryOp(">",Id("a"),IntLiteral(0)),If(UnaryOp("!",Id("b")),If(BinaryOp("==",Id("b"),Id("c")),Break(),Continue()),Return()))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 367))

    def test_68(self):
        """ """
        input = """int main(){
            do {
                foo(5);
            }
            while true;
            int a;
            a = 5;
            return a;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Dowhile([Block([CallExpr(Id("foo"),[IntLiteral(5)])])],BooleanLiteral(True)),VarDecl("a",IntType()),BinaryOp("=",Id("a"),IntLiteral(5)),Return(Id("a"))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 368))

    def test_69(self):
        """ """
        input = """int main(){
            str = "string\\\\";
            return length(str);
            }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",Id("str"),StringLiteral("string\\\\")),Return(CallExpr(Id("length"),[Id("str")]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 369))

    def test_70(self):
        """ """
        input = """int main(){
            string a,b,c;
            a="";
            b="b";
            c="c";
            for(a="";length(a)<20;a=append(a,a))
            {
                b=b*2;
                c=c+b;
            }
            return length(b);
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",StringType()),VarDecl("b",StringType()),VarDecl("c",StringType()),BinaryOp("=",Id("a"),StringLiteral("")),BinaryOp("=",Id("b"),StringLiteral("b")),BinaryOp("=",Id("c"),StringLiteral("c")),For(BinaryOp("=",Id("a"),StringLiteral("")),BinaryOp("<",CallExpr(Id("length"),[Id("a")]),IntLiteral(20)),BinaryOp("=",Id("a"),CallExpr(Id("append"),[Id("a"),Id("a")])),Block([BinaryOp("=",Id("b"),BinaryOp("*",Id("b"),IntLiteral(2))),BinaryOp("=",Id("c"),BinaryOp("+",Id("c"),Id("b")))])),Return(CallExpr(Id("length"),[Id("b")]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 370))

    def test_71(self):
        """ """
        input = """int foo (int a , float b[])
        {
            boolean c ;
            int i ;
            i = a + 3 ;
            if (i > 0)
            {
                int d ;
                d = i + 3;
                putInt(d);
            }
            return i;
        }"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl("a",IntType()),VarDecl("b",ArrayPointerType(FloatType()))],IntType(),Block([VarDecl("c",BoolType()),VarDecl("i",IntType()),BinaryOp("=",Id("i"),BinaryOp("+",Id("a"),IntLiteral(3))),If(BinaryOp(">",Id("i"),IntLiteral(0)),Block([VarDecl("d",IntType()),BinaryOp("=",Id("d"),BinaryOp("+",Id("i"),IntLiteral(3))),CallExpr(Id("putInt"),[Id("d")])])),Return(Id("i"))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 371))

    def test_72(self):
        """ """
        input = """int main()
        {
            a = !b + -a;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",Id("a"),BinaryOp("+",UnaryOp("!",Id("b")),UnaryOp("-",Id("a"))))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 372))

    def test_73(self):
        """ """
        input = """int main()
        {
            a = a * b < (c > d);
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",Id("a"),BinaryOp("<",BinaryOp("*",Id("a"),Id("b")),BinaryOp(">",Id("c"),Id("d"))))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 373))

    def test_74(self):
        """ """
        input = """int main() {
            a = a + b < c == d;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",Id("a"),BinaryOp("==",BinaryOp("<",BinaryOp("+",Id("a"),Id("b")),Id("c")),Id("d")))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 374))

    def test_75(self):
        """ """
        input = """int main() {
            return foo(foo(2))[3+x] = a[b[c[2]]] +3;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Return(BinaryOp("=",ArrayCell(CallExpr(Id("foo"),[CallExpr(Id("foo"),[IntLiteral(2)])]),BinaryOp("+",IntLiteral(3),Id("x"))),BinaryOp("+",ArrayCell(Id("a"),ArrayCell(Id("b"),ArrayCell(Id("c"),IntLiteral(2)))),IntLiteral(3))))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 375))

    def test_76(self):
        """ """
        input = """int[] foo (int b[]){
            int a[69];
            if (b>c)
                return a+1;
            else
                return b-1;
        }"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl("b",ArrayPointerType(IntType()))],ArrayPointerType(IntType()),Block([VarDecl("a",ArrayType(69,IntType())),If(BinaryOp(">",Id("b"),Id("c")),Return(BinaryOp("+",Id("a"),IntLiteral(1))),Return(BinaryOp("-",Id("b"),IntLiteral(1))))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 376))

    def test_77(self):
        """ """
        input = """int main(){
            do
            {
                {
                    if (b>c)
                        return a+1;
                    else
                        return b-1;                    
                }
            }
            {
                a+b;
            }
            while (a<5);
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Dowhile([Block([Block([If(BinaryOp(">",Id("b"),Id("c")),Return(BinaryOp("+",Id("a"),IntLiteral(1))),Return(BinaryOp("-",Id("b"),IntLiteral(1))))])]),Block([BinaryOp("+",Id("a"),Id("b"))])],BinaryOp("<",Id("a"),IntLiteral(5)))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 377))

    def test_78(self):
        """ """
        input = """int main(){
            do
                print("Thang dep trai\\n");
            while
                true;
            }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Dowhile([CallExpr(Id("print"),[StringLiteral("Thang dep trai\\n")])],BooleanLiteral(True))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 378))

    def test_79(self):
        """ """
        input = """int main(){
            int a[10];
            return foo(a[10]);	
            }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",ArrayType(10,IntType())),Return(CallExpr(Id("foo"),[ArrayCell(Id("a"),IntLiteral(10))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 379))

    def test_80(self):
        """ """
        input = """int main(){
                foo(a,b);
            }
            void foo(int a[], float b){
                if (a == 0) 
                    return a;
                else {
                    foo(b,a);
                }
            }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("foo"),[Id("a"),Id("b")])])),FuncDecl(Id("foo"),[VarDecl("a",ArrayPointerType(IntType())),VarDecl("b",FloatType())],VoidType(),Block([If(BinaryOp("==",Id("a"),IntLiteral(0)),Return(Id("a")),Block([CallExpr(Id("foo"),[Id("b"),Id("a")])]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 380))

    def test_81(self):
        """ """
        input = """int main(){
            string a;
            a=upcase(a);
            return count(a,"handsome");
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",StringType()),BinaryOp("=",Id("a"),CallExpr(Id("upcase"),[Id("a")])),Return(CallExpr(Id("count"),[Id("a"),StringLiteral("handsome")]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 381))

    def test_82(self):
        """ """
        input = """int main()
        {
            int fp;
            int c;
            fp = fopen(__FILE__,"r");
            do {
                c = getc(fp);
                putchar(c);
            }
            while(c != EOF);
            fclose(fp);
            return 0;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("fp",IntType()),VarDecl("c",IntType()),BinaryOp("=",Id("fp"),CallExpr(Id("fopen"),[Id("__FILE__"),StringLiteral("r")])),Dowhile([Block([BinaryOp("=",Id("c"),CallExpr(Id("getc"),[Id("fp")])),CallExpr(Id("putchar"),[Id("c")])])],BinaryOp("!=",Id("c"),Id("EOF"))),CallExpr(Id("fclose"),[Id("fp")]),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 382))

    def test_83(self):
        """ """
        input = """int main()
        {
            int i, n, t1, t2, nextTerm;
            printf("Enter the number of terms: ");
            scanf(n);
            printf("Fibonacci Series: ");
            for (i = 1; i <= n; i=i+1)
            {
                printf(t1);
                nextTerm = t1 + t2;
                t1 = t2;
                t2 = nextTerm;
            }
            return 0;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("i",IntType()),VarDecl("n",IntType()),VarDecl("t1",IntType()),VarDecl("t2",IntType()),VarDecl("nextTerm",IntType()),CallExpr(Id("printf"),[StringLiteral("Enter the number of terms: ")]),CallExpr(Id("scanf"),[Id("n")]),CallExpr(Id("printf"),[StringLiteral("Fibonacci Series: ")]),For(BinaryOp("=",Id("i"),IntLiteral(1)),BinaryOp("<=",Id("i"),Id("n")),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([CallExpr(Id("printf"),[Id("t1")]),BinaryOp("=",Id("nextTerm"),BinaryOp("+",Id("t1"),Id("t2"))),BinaryOp("=",Id("t1"),Id("t2")),BinaryOp("=",Id("t2"),Id("nextTerm"))])),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 383))

    def test_84(self):
        """ """
        input = """int main()
        {
            float number;
            printf("Enter a number: ");
            scanf(number);
            if (number <= 0.0)
            {
                if (number == 0.0)
                    printf("You entered 0.");
                else
                    printf("You entered a negative number.");
            }
            else
                printf("You entered a positive number.");
            return 0;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("number",FloatType()),CallExpr(Id("printf"),[StringLiteral("Enter a number: ")]),CallExpr(Id("scanf"),[Id("number")]),If(BinaryOp("<=",Id("number"),FloatLiteral(0.0)),Block([If(BinaryOp("==",Id("number"),FloatLiteral(0.0)),CallExpr(Id("printf"),[StringLiteral("You entered 0.")]),CallExpr(Id("printf"),[StringLiteral("You entered a negative number.")]))]),CallExpr(Id("printf"),[StringLiteral("You entered a positive number.")])),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 384))

    def test_85(self):
        """ """
        input = """int main()
        {
            float number;
            printf("Enter a number: ");
            scanf(number);
            // true if number is less than 0
            if (number < 0.0)
                printf("You entered a negative number.");
                // true if number is greater than 0
            else 
                if ( number > 0.0)
                    printf("You entered a positive number");
                    // if both test expression is evaluated to false
                else
                    printf("You entered 0.");
            return 0;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("number",FloatType()),CallExpr(Id("printf"),[StringLiteral("Enter a number: ")]),CallExpr(Id("scanf"),[Id("number")]),If(BinaryOp("<",Id("number"),FloatLiteral(0.0)),CallExpr(Id("printf"),[StringLiteral("You entered a negative number.")]),If(BinaryOp(">",Id("number"),FloatLiteral(0.0)),CallExpr(Id("printf"),[StringLiteral("You entered a positive number")]),CallExpr(Id("printf"),[StringLiteral("You entered 0.")]))),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 385))

    def test_86(self):
        """ """
        input = """int main()
        {
            int n, i, flag;
            printf("Enter a positive integer: ");
            scanf(n);
            for(i = 2; i <= n/2; i=i+1)
                {
                    // condition for nonprime number
                    if((n%i) == 0)
                    {
                        flag = 1;
                        break;
                    }
                }
            if (n == 1) 
                {
                    printf("1 is neither a prime nor a composite number.");
                }
            else 
                {
                    if (flag == 0)
                        printf(n);
                    else
                        printf(n);
                }
    
            return 0;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("n",IntType()),VarDecl("i",IntType()),VarDecl("flag",IntType()),CallExpr(Id("printf"),[StringLiteral("Enter a positive integer: ")]),CallExpr(Id("scanf"),[Id("n")]),For(BinaryOp("=",Id("i"),IntLiteral(2)),BinaryOp("<=",Id("i"),BinaryOp("/",Id("n"),IntLiteral(2))),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([If(BinaryOp("==",BinaryOp("%",Id("n"),Id("i")),IntLiteral(0)),Block([BinaryOp("=",Id("flag"),IntLiteral(1)),Break()]))])),If(BinaryOp("==",Id("n"),IntLiteral(1)),Block([CallExpr(Id("printf"),[StringLiteral("1 is neither a prime nor a composite number.")])]),Block([If(BinaryOp("==",Id("flag"),IntLiteral(0)),CallExpr(Id("printf"),[Id("n")]),CallExpr(Id("printf"),[Id("n")]))])),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 386))

    def test_87(self):
        """ """
        input = """int main()
        {
            int low, high, i, flag;
            printf("Enter two numbers(intervals): ");
            scanf(low, high);
            printf(low, high);
            do
            {
                flag = 0;
                for(i = 2; i <= low/2; i=i+1)
                {
                    if(low % i == 0)
                        {
                            flag = 1;
                            break;
                        }
                }
                 if (flag == 0)
                    printf(low);
                low=low+1;
            }
            while (low < high);
            return 0;
            }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("low",IntType()),VarDecl("high",IntType()),VarDecl("i",IntType()),VarDecl("flag",IntType()),CallExpr(Id("printf"),[StringLiteral("Enter two numbers(intervals): ")]),CallExpr(Id("scanf"),[Id("low"),Id("high")]),CallExpr(Id("printf"),[Id("low"),Id("high")]),Dowhile([Block([BinaryOp("=",Id("flag"),IntLiteral(0)),For(BinaryOp("=",Id("i"),IntLiteral(2)),BinaryOp("<=",Id("i"),BinaryOp("/",Id("low"),IntLiteral(2))),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([If(BinaryOp("==",BinaryOp("%",Id("low"),Id("i")),IntLiteral(0)),Block([BinaryOp("=",Id("flag"),IntLiteral(1)),Break()]))])),If(BinaryOp("==",Id("flag"),IntLiteral(0)),CallExpr(Id("printf"),[Id("low")])),BinaryOp("=",Id("low"),BinaryOp("+",Id("low"),IntLiteral(1)))])],BinaryOp("<",Id("low"),Id("high"))),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 387))

    def test_88(self):
        """ """
        input = """int main()
        {
            int low, high, i, flag, temp;
            printf("Enter two numbers(intevals): ");
            scanf(low, high);
            //swapping numbers if low is greater than high
            if (low > high)
            {
                temp = low;
                low = high;
                high = temp;
            }
            printf(low, high);
            do
            {
                int a;
                for(i = 2; i <= low/2; i=i+1)
                {
                    if(low % i == 0)
                    {
                        flag = 1;
                        break;
                    }
                }                
            }
            {
                flag = 0;
                for(i = 2; i <= low/2; i=i+1)
                {
                    if(low % i == 0)
                    {
                        flag = 1;
                        break;
                    }
                }
                if (flag == 0)
                    printf(low);
                low=low+1;
            }
            while (low < high);
            return 0;
            }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("low",IntType()),VarDecl("high",IntType()),VarDecl("i",IntType()),VarDecl("flag",IntType()),VarDecl("temp",IntType()),CallExpr(Id("printf"),[StringLiteral("Enter two numbers(intevals): ")]),CallExpr(Id("scanf"),[Id("low"),Id("high")]),If(BinaryOp(">",Id("low"),Id("high")),Block([BinaryOp("=",Id("temp"),Id("low")),BinaryOp("=",Id("low"),Id("high")),BinaryOp("=",Id("high"),Id("temp"))])),CallExpr(Id("printf"),[Id("low"),Id("high")]),Dowhile([Block([VarDecl("a",IntType()),For(BinaryOp("=",Id("i"),IntLiteral(2)),BinaryOp("<=",Id("i"),BinaryOp("/",Id("low"),IntLiteral(2))),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([If(BinaryOp("==",BinaryOp("%",Id("low"),Id("i")),IntLiteral(0)),Block([BinaryOp("=",Id("flag"),IntLiteral(1)),Break()]))]))]),Block([BinaryOp("=",Id("flag"),IntLiteral(0)),For(BinaryOp("=",Id("i"),IntLiteral(2)),BinaryOp("<=",Id("i"),BinaryOp("/",Id("low"),IntLiteral(2))),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([If(BinaryOp("==",BinaryOp("%",Id("low"),Id("i")),IntLiteral(0)),Block([BinaryOp("=",Id("flag"),IntLiteral(1)),Break()]))])),If(BinaryOp("==",Id("flag"),IntLiteral(0)),CallExpr(Id("printf"),[Id("low")])),BinaryOp("=",Id("low"),BinaryOp("+",Id("low"),IntLiteral(1)))])],BinaryOp("<",Id("low"),Id("high"))),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 388))

    def test_89(self):
        """ """
        input = """// user-defined function to check prime number
        int checkPrimeNumber(int n)
        {
            int j, flag;
            for(j=2; j <= n/2; j=j+1)
            {
                if (n%j == 0)
                {
                    flag =0;
                    break;
                }
            }
        return flag;
        }

        int main()
        {
            int n1, n2, i, flag;
            printf("Enter two positive integers: ");
            scanf(n1, n2);
            printf(n1, n2);
            for(i=n1+1; i<n2; i=i+1)
            {
                // i is a prime number, flag will be equal to 1
                flag = checkPrimeNumber(i);
                if(flag == 1)
                printf(i);
            }
            return 0;
        }"""
        expect = str(Program([FuncDecl(Id("checkPrimeNumber"),[VarDecl("n",IntType())],IntType(),Block([VarDecl("j",IntType()),VarDecl("flag",IntType()),For(BinaryOp("=",Id("j"),IntLiteral(2)),BinaryOp("<=",Id("j"),BinaryOp("/",Id("n"),IntLiteral(2))),BinaryOp("=",Id("j"),BinaryOp("+",Id("j"),IntLiteral(1))),Block([If(BinaryOp("==",BinaryOp("%",Id("n"),Id("j")),IntLiteral(0)),Block([BinaryOp("=",Id("flag"),IntLiteral(0)),Break()]))])),Return(Id("flag"))])),FuncDecl(Id("main"),[],IntType(),Block([VarDecl("n1",IntType()),VarDecl("n2",IntType()),VarDecl("i",IntType()),VarDecl("flag",IntType()),CallExpr(Id("printf"),[StringLiteral("Enter two positive integers: ")]),CallExpr(Id("scanf"),[Id("n1"),Id("n2")]),CallExpr(Id("printf"),[Id("n1"),Id("n2")]),For(BinaryOp("=",Id("i"),BinaryOp("+",Id("n1"),IntLiteral(1))),BinaryOp("<",Id("i"),Id("n2")),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([BinaryOp("=",Id("flag"),CallExpr(Id("checkPrimeNumber"),[Id("i")])),If(BinaryOp("==",Id("flag"),IntLiteral(1)),CallExpr(Id("printf"),[Id("i")]))])),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 389))

    def test_90(self):
        """ """
        input = """int main()
        {
            int n1, n2;    
            printf("Enter two positive integers: ");
            scanf(n1,n2);
            do
            {
                if(n1 > n2)
                    n1 = n1 - n2;
                else
                    n2 = n2 - n1;
            }
            while(n1!=n2);
            printf("GCD = ",n1);
            return 0;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("n1",IntType()),VarDecl("n2",IntType()),CallExpr(Id("printf"),[StringLiteral("Enter two positive integers: ")]),CallExpr(Id("scanf"),[Id("n1"),Id("n2")]),Dowhile([Block([If(BinaryOp(">",Id("n1"),Id("n2")),BinaryOp("=",Id("n1"),BinaryOp("-",Id("n1"),Id("n2"))),BinaryOp("=",Id("n2"),BinaryOp("-",Id("n2"),Id("n1"))))])],BinaryOp("!=",Id("n1"),Id("n2"))),CallExpr(Id("printf"),[StringLiteral("GCD = "),Id("n1")]),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 390))

    def test_91(self):
        """ """
        input = """int addNumbers(int n)
        {
            if(n != 0)
            return n + addNumbers(n-1);
            else
            return n;
        }
        int main()
        {
            int num;
            printf("Enter a positive integer: ");
            scanf(num);
            printf("Sum = ",addNumbers(num));
            return 0;
        }"""
        expect = str(Program([FuncDecl(Id("addNumbers"),[VarDecl("n",IntType())],IntType(),Block([If(BinaryOp("!=",Id("n"),IntLiteral(0)),Return(BinaryOp("+",Id("n"),CallExpr(Id("addNumbers"),[BinaryOp("-",Id("n"),IntLiteral(1))]))),Return(Id("n")))])),FuncDecl(Id("main"),[],IntType(),Block([VarDecl("num",IntType()),CallExpr(Id("printf"),[StringLiteral("Enter a positive integer: ")]),CallExpr(Id("scanf"),[Id("num")]),CallExpr(Id("printf"),[StringLiteral("Sum = "),CallExpr(Id("addNumbers"),[Id("num")])]),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 391))

    def test_92(self):
        """ """
        input = """int main()
        {
            int n, i, sum;
    
            printf("Enter a positive integer: ");
            scanf(n);
            for(i=1; i <= n; i=i+1)
            {
                sum = sum+i;
            }
            printf("Sum = ",sum);
            return 0;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("n",IntType()),VarDecl("i",IntType()),VarDecl("sum",IntType()),CallExpr(Id("printf"),[StringLiteral("Enter a positive integer: ")]),CallExpr(Id("scanf"),[Id("n")]),For(BinaryOp("=",Id("i"),IntLiteral(1)),BinaryOp("<=",Id("i"),Id("n")),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([BinaryOp("=",Id("sum"),BinaryOp("+",Id("sum"),Id("i")))])),CallExpr(Id("printf"),[StringLiteral("Sum = "),Id("sum")]),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 392))

    def test_93(self):
        """ """
        input = """int main()
        {
            int number, i;
            printf("Enter a positive integer: ");
            scanf(number);
            printf(number);
            for(i=1; i <= number; i=i+1)
            {
                if (number%i == 0)
                {
                    printf(i);
                }
            }
            return 0;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("number",IntType()),VarDecl("i",IntType()),CallExpr(Id("printf"),[StringLiteral("Enter a positive integer: ")]),CallExpr(Id("scanf"),[Id("number")]),CallExpr(Id("printf"),[Id("number")]),For(BinaryOp("=",Id("i"),IntLiteral(1)),BinaryOp("<=",Id("i"),Id("number")),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([If(BinaryOp("==",BinaryOp("%",Id("number"),Id("i")),IntLiteral(0)),Block([CallExpr(Id("printf"),[Id("i")])]))])),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 393))

    def test_94(self):
        """ """
        input = """int main()
        {
            int n, reversedInteger, remainder, originalInteger;
            printf("Enter an integer: ");
            scanf(n);
            originalInteger = n;
            // reversed integer is stored in variable 
            do
            {
                remainder = n%10;
                reversedInteger = reversedInteger*10 + remainder;
                n = n / 10;
            }
            while( n!=0 );
            // palindrome if orignalInteger and reversedInteger are equal
            if (originalInteger == reversedInteger)
                printf(originalInteger);
            else
                printf(originalInteger);
    
            return 0;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("n",IntType()),VarDecl("reversedInteger",IntType()),VarDecl("remainder",IntType()),VarDecl("originalInteger",IntType()),CallExpr(Id("printf"),[StringLiteral("Enter an integer: ")]),CallExpr(Id("scanf"),[Id("n")]),BinaryOp("=",Id("originalInteger"),Id("n")),Dowhile([Block([BinaryOp("=",Id("remainder"),BinaryOp("%",Id("n"),IntLiteral(10))),BinaryOp("=",Id("reversedInteger"),BinaryOp("+",BinaryOp("*",Id("reversedInteger"),IntLiteral(10)),Id("remainder"))),BinaryOp("=",Id("n"),BinaryOp("/",Id("n"),IntLiteral(10)))])],BinaryOp("!=",Id("n"),IntLiteral(0))),If(BinaryOp("==",Id("originalInteger"),Id("reversedInteger")),CallExpr(Id("printf"),[Id("originalInteger")]),CallExpr(Id("printf"),[Id("originalInteger")])),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 394))

    def test_95(self):
        """ """
        input = """int main()
        {
            int dividend, divisor, quotient, remainder;
            printf("Enter dividend: ");
            scanf(dividend);
            printf("Enter divisor: ");
            scanf(divisor);
            // Computes quotient
            quotient = dividend / divisor;
            // Computes remainder
            remainder = dividend % divisor;
            printf("Quotient = ", quotient);
            printf("Remainder = ", remainder);
            return 0;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("dividend",IntType()),VarDecl("divisor",IntType()),VarDecl("quotient",IntType()),VarDecl("remainder",IntType()),CallExpr(Id("printf"),[StringLiteral("Enter dividend: ")]),CallExpr(Id("scanf"),[Id("dividend")]),CallExpr(Id("printf"),[StringLiteral("Enter divisor: ")]),CallExpr(Id("scanf"),[Id("divisor")]),BinaryOp("=",Id("quotient"),BinaryOp("/",Id("dividend"),Id("divisor"))),BinaryOp("=",Id("remainder"),BinaryOp("%",Id("dividend"),Id("divisor"))),CallExpr(Id("printf"),[StringLiteral("Quotient = "),Id("quotient")]),CallExpr(Id("printf"),[StringLiteral("Remainder = "),Id("remainder")]),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 395))

    def test_96(self):
        """ """
        input = """void getFibonacii(int a,int b, int n)
        {   
            int sum;
            if(n>0)
            {
                sum=a+b;
                printf(sum);
                a=b;
                b=sum;
                getFibonacii(a,b,n-1);
            }
        }
        int main()
        {
            int a,b,sum,n;
            int i;
     
            a=0;        //first term
            b=1;        //second term
     
            printf("Enter total number of terms: ");
            scanf(n);
     
            printf("Fibonacii series is : ");
            //print a and b as first and second terms of series
            printf(a,b);
            //call function with (n-2) terms
            getFibonacii(a,b,n-2);
  
            return 0;
        }"""
        expect = str(Program([FuncDecl(Id("getFibonacii"),[VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("n",IntType())],VoidType(),Block([VarDecl("sum",IntType()),If(BinaryOp(">",Id("n"),IntLiteral(0)),Block([BinaryOp("=",Id("sum"),BinaryOp("+",Id("a"),Id("b"))),CallExpr(Id("printf"),[Id("sum")]),BinaryOp("=",Id("a"),Id("b")),BinaryOp("=",Id("b"),Id("sum")),CallExpr(Id("getFibonacii"),[Id("a"),Id("b"),BinaryOp("-",Id("n"),IntLiteral(1))])]))])),FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("sum",IntType()),VarDecl("n",IntType()),VarDecl("i",IntType()),BinaryOp("=",Id("a"),IntLiteral(0)),BinaryOp("=",Id("b"),IntLiteral(1)),CallExpr(Id("printf"),[StringLiteral("Enter total number of terms: ")]),CallExpr(Id("scanf"),[Id("n")]),CallExpr(Id("printf"),[StringLiteral("Fibonacii series is : ")]),CallExpr(Id("printf"),[Id("a"),Id("b")]),CallExpr(Id("getFibonacii"),[Id("a"),Id("b"),BinaryOp("-",Id("n"),IntLiteral(2))]),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 396))

    def test_97(self):
        """ """
        input = """int getPower(int b,int p)
        {
            int result;
            if(p==0)
                return result;
            result=b*(getPower(b,p-1));  //call function again
        }
        int main()
        {
            int base,power;
            int result;
     
            printf("Enter value of base: ");
            scanf(base);
     
            printf("Enter value of power: ");
            scanf(power);
     
            result=getPower(base,power);
     
            printf(base,power,result);
     
            return 0;
        }"""
        expect = str(Program([FuncDecl(Id("getPower"),[VarDecl("b",IntType()),VarDecl("p",IntType())],IntType(),Block([VarDecl("result",IntType()),If(BinaryOp("==",Id("p"),IntLiteral(0)),Return(Id("result"))),BinaryOp("=",Id("result"),BinaryOp("*",Id("b"),CallExpr(Id("getPower"),[Id("b"),BinaryOp("-",Id("p"),IntLiteral(1))])))])),FuncDecl(Id("main"),[],IntType(),Block([VarDecl("base",IntType()),VarDecl("power",IntType()),VarDecl("result",IntType()),CallExpr(Id("printf"),[StringLiteral("Enter value of base: ")]),CallExpr(Id("scanf"),[Id("base")]),CallExpr(Id("printf"),[StringLiteral("Enter value of power: ")]),CallExpr(Id("scanf"),[Id("power")]),BinaryOp("=",Id("result"),CallExpr(Id("getPower"),[Id("base"),Id("power")])),CallExpr(Id("printf"),[Id("base"),Id("power"),Id("result")]),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 397))


    def test_simple_program(self):
        """Simple program: int main() {}"""
        input = """int main() {}"""
        expect = str(Program([FuncDecl(Id("main"), [], IntType(), Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,398))

    def test_more_complex_program(self):
        """More complex program"""
        input = """int main () {
            putIntLn(4);
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("putIntLn"),[IntLiteral(4)])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,399))

    def test_call_without_parameter(self):
        """More complex program"""
        input = """int main () {
            getIntLn();
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("getIntLn"),[])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,400))
