import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):

    #PROGRAM_STATEMENT
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """int main() {}"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 301))

    def test_more_complex_program(self):
        """More complex program"""
        input = """int main () {
            putIntLn(4);
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("putIntLn"),[IntLiteral(4)])]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 302))

    def test_more_complex_program1(self):
        """More complex program"""
        input = """int main () {

        }
        int a;
        int[] foo(int a[]){
        int a[1];

        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([])),VarDecl("a",IntType()),FuncDecl(Id("foo"),[VarDecl("a",ArrayPointerType(IntType()))],ArrayPointerType(IntType()),Block([VarDecl("a",ArrayType(1,IntType()))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 303))

    def test_program2(self):
        input = """
        int a;
        float doubleThing(int a){
            if (a != 1)
                return a*a;
            else 
                return 1;
            do {
                "nothing in here";
                //this is nothing in here
            }while(exp);
        }
                """
        expect = str(Program([VarDecl("a",IntType()),FuncDecl(Id("doubleThing"),[VarDecl("a",IntType())],FloatType(),Block([If(BinaryOp("!=",Id("a"),IntLiteral(1)),Return(BinaryOp("*",Id("a"),Id("a"))),Return(IntLiteral(1))),Dowhile([Block([StringLiteral("nothing in here")])],Id("exp"))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 304))

    def test_program4(self):
        input = """
        void printArray(int a,int m, int n){
            retunr;
        }
                """
        expect = str(Program([FuncDecl(Id("printArray"),[VarDecl("a",IntType()),VarDecl("m",IntType()),VarDecl("n",IntType())],VoidType(),Block([Id("retunr")]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 305))

    def test_program9(self):
        input = """
        int main() {
            if (!true) {
                {}
                do {
                    if (false) a; 
                } while (a==b);
            } else return b;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(UnaryOp("!",BooleanLiteral("true")),Block([Block([]),Dowhile([Block([If(BooleanLiteral("false"),Id("a"))])],BinaryOp("==",Id("a"),Id("b")))]),Return(Id("b")))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 306))

    def test_program10(self):
        input = """
        int main() {
            if (true)
                return a;
            else 
                return b;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BooleanLiteral("true"),Return(Id("a")),Return(Id("b")))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 307))

    def test_program11(self):
        input = """
        boolean Multiple(int n,int m){
            if (n % m == 0)
            return 1;
            return 0;
        }
        void main(){
            int a,b;
            scanf("a = %d",a);
            scanf("b = %d",b);
            if (isMultiple(a,b))
                return true;
            else 
                return false;
        }
                """
        expect = str(Program([FuncDecl(Id("Multiple"),[VarDecl("n",IntType()),VarDecl("m",IntType())],BoolType(),Block([If(BinaryOp("==",BinaryOp("%",Id("n"),Id("m")),IntLiteral(0)),Return(IntLiteral(1))),Return(IntLiteral(0))])),FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),CallExpr(Id("scanf"),[StringLiteral("a = %d"),Id("a")]),CallExpr(Id("scanf"),[StringLiteral("b = %d"),Id("b")]),If(CallExpr(Id("isMultiple"),[Id("a"),Id("b")]),Return(BooleanLiteral("true")),Return(BooleanLiteral("false")))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 308))

    def test_program14(self):
        input = """
        int main() {
            {a="dang";}
            {
            float a;
                a=6;
                b=5;
            }
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Block([BinaryOp("=",Id("a"),StringLiteral("dang"))]),Block([VarDecl("a",FloatType()),BinaryOp("=",Id("a"),IntLiteral(6)),BinaryOp("=",Id("b"),IntLiteral(5))])]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 309))

    def test_program16(self):
        input = """
        boolean testExp(){
           int n;
           //n = (l *(h == (m||(j[]>=(-a[]+!b)/c)%d)&&f)<=k);
           n=(1+2);
           if (n)
            return 1;
           else 
            return 0;
        }
        """
        expect = str(Program([FuncDecl(Id("testExp"),[],BoolType(),Block([VarDecl("n",IntType()),BinaryOp("=",Id("n"),BinaryOp("+",IntLiteral(1),IntLiteral(2))),If(Id("n"),Return(IntLiteral(1)),Return(IntLiteral(0)))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 310))

    def test_program19(self):
        input = """
        int main()
        {
        print("dang: %d");
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("print"),[StringLiteral("dang: %d")])]))]))

        self.assertTrue(TestAST.checkASTGen(input, expect, 311))

    def test_program20(self):
        input = """
        int Fibonaci(int i) {
            if (i == 0) { return 0; }
            if(i == 1) { return 1;}
            return Fibonaci(i-1) + Fibonaci(i-2);
        }

        int  main() {
            int i;
            for (i = 0; i < 10; i=i+1) { printf("%f", Fibonaci(i)); }
            printf("===========================");
            return 0;
        }
        """
        expect = str(Program([FuncDecl(Id("Fibonaci"),[VarDecl("i",IntType())],IntType(),Block([If(BinaryOp("==",Id("i"),IntLiteral(0)),Block([Return(IntLiteral(0))])),If(BinaryOp("==",Id("i"),IntLiteral(1)),Block([Return(IntLiteral(1))])),Return(BinaryOp("+",CallExpr(Id("Fibonaci"),[BinaryOp("-",Id("i"),IntLiteral(1))]),CallExpr(Id("Fibonaci"),[BinaryOp("-",Id("i"),IntLiteral(2))])))])),FuncDecl(Id("main"),[],IntType(),Block([VarDecl("i",IntType()),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),IntLiteral(10)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([CallExpr(Id("printf"),[StringLiteral("%f"),CallExpr(Id("Fibonaci"),[Id("i")])])])),CallExpr(Id("printf"),[StringLiteral("===========================")]),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 312))

    def test_program24(self):
        input = """
        boolean[] func(int a, float b[]){ 
            int a;
            if(a>0) foo(a>0,b-1);
            }             
        """
        expect = str(Program([FuncDecl(Id("func"),[VarDecl("a",IntType()),VarDecl("b",ArrayPointerType(FloatType()))],ArrayPointerType(BoolType()),Block([VarDecl("a",IntType()),If(BinaryOp(">",Id("a"),IntLiteral(0)),CallExpr(Id("foo"),[BinaryOp(">",Id("a"),IntLiteral(0)),BinaryOp("-",Id("b"),IntLiteral(1))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 313))


    def test_program25(self):
        input = """int main(int a) {
        do{} while(a==1);
        }       
        """
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("a",IntType())],IntType(),Block([Dowhile([Block([])],BinaryOp("==",Id("a"),IntLiteral(1)))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 314))

    #14

    #VARIABLE_STATEMENT

    def test_variable_declaration(self):
        input = """
        int a,b,c,d[1];
        float a[6],c[4],a;
        """
        expect=str(Program([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",ArrayType(1,IntType())),VarDecl("a",ArrayType(6,FloatType())),VarDecl("c",ArrayType(4,FloatType())),VarDecl("a",FloatType())]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 315))

    def test_variable_declaration_3(self):
        input = """
        float a,b,c[5]
        ; a==5;
        int main(){
        print("Nguyen Tran Minh Dang");
        }
        """
        expect = str(Program([VarDecl("a",FloatType()),VarDecl("b",FloatType()),VarDecl("c",ArrayType(5,FloatType())),FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("print"),[StringLiteral("Nguyen Tran Minh Dang")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,316))

    def test_variable_declaration_4(self):
        input = """
        int a[2],b[3],c[4],d[5],e[5]
            ;float f,g,h;
            string i,j,k[12];
            boolean l,m[20],n[5];
        """
        expect = str(Program([VarDecl("a",ArrayType(2,IntType())),VarDecl("b",ArrayType(3,IntType())),VarDecl("c",ArrayType(4,IntType())),VarDecl("d",ArrayType(5,IntType())),VarDecl("e",ArrayType(5,IntType())),VarDecl("f",FloatType()),VarDecl("g",FloatType()),VarDecl("h",FloatType()),VarDecl("i",StringType()),VarDecl("j",StringType()),VarDecl("k",ArrayType(12,StringType())),VarDecl("l",BoolType()),VarDecl("m",ArrayType(20,BoolType())),VarDecl("n",ArrayType(5,BoolType()))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,317))

    def test_variable_declaration_5(self):
        input = """
        int a,b,c,d[1];
        float a[6],c[4],a;
        void main(int a, float b){
        int a,b,c,d[3];
        float d[8],e[10],f;
        string str;
        str="Nguyen Tran Minh Dang";
        }
        """
        expect=str(Program([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",ArrayType(1,IntType())),VarDecl("a",ArrayType(6,FloatType())),VarDecl("c",ArrayType(4,FloatType())),VarDecl("a",FloatType()),FuncDecl(Id("main"),[VarDecl("a",IntType()),VarDecl("b",FloatType())],VoidType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",ArrayType(3,IntType())),VarDecl("d",ArrayType(8,FloatType())),VarDecl("e",ArrayType(10,FloatType())),VarDecl("f",FloatType()),VarDecl("str",StringType()),BinaryOp("=",Id("str"),StringLiteral("Nguyen Tran Minh Dang"))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 318))

    def test_variable_declaration_6(self):
        input = """
                int a,b,c,d[1];
                arr[0]=a;
                arr[1]=b;
                }
                """
        expect = str(Program([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",ArrayType(1,IntType()))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 319))

    #5

    #FUNCTION_STATEMENT

    def test_function_declaration(self):
        input = """int main() {
        float a;
        float b,c;
        a=b=c=1;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",FloatType()),VarDecl("b",FloatType()),VarDecl("c",FloatType()),BinaryOp("=",Id("a"),BinaryOp("=",Id("b"),BinaryOp("=",Id("c"),IntLiteral(1))))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 320))

    def test_function_declaration1(self):
        input = """int main() {}
        string _main() {}
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([])),FuncDecl(Id("_main"),[],StringType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 321))

    def test_function_delaration2(self):
        input = """int main() {continue;}
        float func(int a[],int b){


        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Continue()])),FuncDecl(Id("func"),[VarDecl("a",ArrayPointerType(IntType())),VarDecl("b",IntType())],FloatType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 322))

    def test_function_declaration3(self):
        input = """int main() {continue;}
        float func(int a[],int b){
            float y[10];
            foo(z);
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Continue()])),FuncDecl(Id("func"),[VarDecl("a",ArrayPointerType(IntType())),VarDecl("b",IntType())],FloatType(),Block([VarDecl("y",ArrayType(10,FloatType())),CallExpr(Id("foo"),[Id("z")])]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 323))


    def test_function_declaration4(self):
        input = """int main() {continue;}
        void func(int a[],int b,int c){
        foo(2,3,4)[x+3]=a[b[2]]+3;
        return 1;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Continue()])),FuncDecl(Id("func"),[VarDecl("a",ArrayPointerType(IntType())),VarDecl("b",IntType()),VarDecl("c",IntType())],VoidType(),Block([BinaryOp("=",ArrayCell(CallExpr(Id("foo"),[IntLiteral(2),IntLiteral(3),IntLiteral(4)]),BinaryOp("+",Id("x"),IntLiteral(3))),BinaryOp("+",ArrayCell(Id("a"),ArrayCell(Id("b"),IntLiteral(2))),IntLiteral(3))),Return(IntLiteral(1))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 324))

    def test_function_declaration_5(self):
        input = """int main() {}"""
        expect = str(Program([FuncDecl(Id("main"), [], IntType(), Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 325))

    def test_function_declaration_6(self):
        input = """
        float main(int a) {}
        string[] foo(int b[]) { a=b[5]+2}"""
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("a",IntType())],FloatType(),Block([])),FuncDecl(Id("foo"),[VarDecl("b",ArrayPointerType(IntType()))],ArrayPointerType(StringType()),Block([BinaryOp("=",Id("a"),BinaryOp("+",ArrayCell(Id("b"),IntLiteral(5)),IntLiteral(2)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,326))

    def test_function_declaration_7(self):
        input = """int main() {
            foo(5);
        }
        void foo() {
            print("Hello Minh Dang");
            a = (a %6)&&((a<5));
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("foo"),[IntLiteral(5)])])),FuncDecl(Id("foo"),[],VoidType(),Block([CallExpr(Id("print"),[StringLiteral("Hello Minh Dang")]),BinaryOp("=",Id("a"),BinaryOp("&&",BinaryOp("%",Id("a"),IntLiteral(6)),BinaryOp("<",Id("a"),IntLiteral(5))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,327))

    def test_function_declaration_8(self):
        input = """void main(int a[], float b[], int c, boolean d[]) {
            foo(x);
            string str;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("a",ArrayPointerType(IntType())),VarDecl("b",ArrayPointerType(FloatType())),VarDecl("c",IntType()),VarDecl("d",ArrayPointerType(BoolType()))],VoidType(),Block([CallExpr(Id("foo"),[Id("x")]),VarDecl("str",StringType())]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,328))

    def test_function_declaration_9(self):
        input = """void main(int a[], float b[], int c, boolean d[]) {
                    int a,b,c[10];
                    string str="Tui lam test case chan lam roi!!!";
                    NGHI_LAM("cuc ki muon nghi");
                }"""
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("a",ArrayPointerType(IntType())),VarDecl("b",ArrayPointerType(FloatType())),VarDecl("c",IntType()),VarDecl("d",ArrayPointerType(BoolType()))],VoidType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",ArrayType(10,IntType())),VarDecl("str",StringType()),StringLiteral("Tui lam test case chan lam roi!!!"),CallExpr(Id("NGHI_LAM"),[StringLiteral("cuc ki muon nghi")])]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 329))

    def test_function_declaration_10(self):
        input = """void main() {
            boolean x;
            int y;
            x = true;
            y = getInt();
            if (y > 10)
                if ( y > 15)
                    x = !x && (y>20);
                else
                    x = x && (y >15 );
            else x = x && (y > 7);
            foo(x);
        }
                }"""
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("x",BoolType()),VarDecl("y",IntType()),BinaryOp("=",Id("x"),BooleanLiteral("true")),BinaryOp("=",Id("y"),CallExpr(Id("getInt"),[])),If(BinaryOp(">",Id("y"),IntLiteral(10)),If(BinaryOp(">",Id("y"),IntLiteral(15)),BinaryOp("=",Id("x"),BinaryOp("&&",UnaryOp("!",Id("x")),BinaryOp(">",Id("y"),IntLiteral(20)))),BinaryOp("=",Id("x"),BinaryOp("&&",Id("x"),BinaryOp(">",Id("y"),IntLiteral(15))))),BinaryOp("=",Id("x"),BinaryOp("&&",Id("x"),BinaryOp(">",Id("y"),IntLiteral(7))))),CallExpr(Id("foo"),[Id("x")])]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 330))

    def test_function_declaration_11(self):
        input = """void main() {
            boolean x;
            int y;
            x = true;
            y = getInt();
            if (y > 10)
                if ( y > 15 && y < 50)
                    x = !x && (y>20);
                else
                    x = x && (y >15 );
            else
                if (y >5 ) x= !x && (y > 7);
                else {
                    x = !x && y >2;
                    putString("ahihi");
                }
            call(x);
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("x",BoolType()),VarDecl("y",IntType()),BinaryOp("=",Id("x"),BooleanLiteral("true")),BinaryOp("=",Id("y"),CallExpr(Id("getInt"),[])),If(BinaryOp(">",Id("y"),IntLiteral(10)),If(BinaryOp("&&",BinaryOp(">",Id("y"),IntLiteral(15)),BinaryOp("<",Id("y"),IntLiteral(50))),BinaryOp("=",Id("x"),BinaryOp("&&",UnaryOp("!",Id("x")),BinaryOp(">",Id("y"),IntLiteral(20)))),BinaryOp("=",Id("x"),BinaryOp("&&",Id("x"),BinaryOp(">",Id("y"),IntLiteral(15))))),If(BinaryOp(">",Id("y"),IntLiteral(5)),BinaryOp("=",Id("x"),BinaryOp("&&",UnaryOp("!",Id("x")),BinaryOp(">",Id("y"),IntLiteral(7)))),Block([BinaryOp("=",Id("x"),BinaryOp("&&",UnaryOp("!",Id("x")),BinaryOp(">",Id("y"),IntLiteral(2)))),CallExpr(Id("putString"),[StringLiteral("ahihi")])]))),CallExpr(Id("call"),[Id("x")])]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 331))

    def test_function_declaration_12(self):
        input = """
           int main() {
                float a,b,c;
               a <=1;
               a+2= b || c;
           }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",FloatType()),VarDecl("b",FloatType()),VarDecl("c",FloatType()),BinaryOp("<=",Id("a"),IntLiteral(1)),BinaryOp("=",BinaryOp("+",Id("a"),IntLiteral(2)),BinaryOp("||",Id("b"),Id("c")))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 332))

    def test_function_declaration_13(self):
        input = """
           void main() {
              b[5];
              c!=d;
           }"""
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([ArrayCell(Id("b"),IntLiteral(5)),BinaryOp("!=",Id("c"),Id("d"))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 333))

    def test_function_declaration_14(self):
        input="""int i ;
            int f() {
                return 200;
            }
            """
        expect = str(Program([VarDecl("i",IntType()),FuncDecl(Id("f"),[],IntType(),Block([Return(IntLiteral(200))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 334))

    def test_function_declaration15(self):
        input = """
        void main(){   
            
            getString("Ngan ngam lam roi :v");
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([CallExpr(Id("getString"),[StringLiteral("Ngan ngam lam roi :v")])]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 335))

    #16

    #IF_STATEMENT

    def test_if(self):
        input = """int main() {
        if(a=1)
        a=b=c=1;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp("=",Id("a"),IntLiteral(1)),BinaryOp("=",Id("a"),BinaryOp("=",Id("b"),BinaryOp("=",Id("c"),IntLiteral(1)))))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 336))

    def test_if1(self):
        input = """int main() {
        if(x == 0) a = 0;
        if(true) b=5;
        if(a > 5) a = s = f; else x = 0; 
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp("==",Id("x"),IntLiteral(0)),BinaryOp("=",Id("a"),IntLiteral(0))),If(BooleanLiteral("true"),BinaryOp("=",Id("b"),IntLiteral(5))),If(BinaryOp(">",Id("a"),IntLiteral(5)),BinaryOp("=",Id("a"),BinaryOp("=",Id("s"),Id("f"))),BinaryOp("=",Id("x"),IntLiteral(0)))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 337))

    def test_if2(self):
        input = """int main() {
        if(x = 5) if (x == 6) if (x != 7) a = 0;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp("=",Id("x"),IntLiteral(5)),If(BinaryOp("==",Id("x"),IntLiteral(6)),If(BinaryOp("!=",Id("x"),IntLiteral(7)),BinaryOp("=",Id("a"),IntLiteral(0)))))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 338))

    def test_if3(self):
        input = """int main() {
        if(x = 5) 
        if (x == 6) 
        if (x != 7) 
        a = 0;
        else a=1;
        else a+2;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp("=",Id("x"),IntLiteral(5)),If(BinaryOp("==",Id("x"),IntLiteral(6)),If(BinaryOp("!=",Id("x"),IntLiteral(7)),BinaryOp("=",Id("a"),IntLiteral(0)),BinaryOp("=",Id("a"),IntLiteral(1))),BinaryOp("+",Id("a"),IntLiteral(2))))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 339))

    def test_if4(self):
        input = """void main(){
        int a;
        a=0;
        if (a=a+1 >1)
        print("in a ra man hinh");
        else
             if (a<1) 
                break;
            else
            print("Khong in a ra man hinh");
        
        }
                """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()),BinaryOp("=",Id("a"),IntLiteral(0)),If(BinaryOp("=",Id("a"),BinaryOp(">",BinaryOp("+",Id("a"),IntLiteral(1)),IntLiteral(1))),CallExpr(Id("print"),[StringLiteral("in a ra man hinh")]),If(BinaryOp("<",Id("a"),IntLiteral(1)),Break(),CallExpr(Id("print"),[StringLiteral("Khong in a ra man hinh")])))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 340))

    def test_if5(self):
        input="""int main(){if(bb) if (aa) if (cc) {} else {} else {} }"""
        expect=str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(Id("bb"),If(Id("aa"),If(Id("cc"),Block([]),Block([])),Block([])))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 341))

    #6

    #DO_WHILE_STATEMENT

    def test_Dowhile(self):
        input = """int main() {
        do{} while(a==1);
        }       
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Dowhile([Block([])],BinaryOp("==",Id("a"),IntLiteral(1)))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 342))

    def test_Dowhile1(self):
        input = """
        int main(){
        do a=1; while i==1;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Dowhile([BinaryOp("=",Id("a"),IntLiteral(1))],BinaryOp("==",Id("i"),IntLiteral(1)))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 343))


    def test_Dowhile2(self):
        input = """
        int main(){
        do a=1; {} foo(); while(a&&1);
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Dowhile([BinaryOp("=",Id("a"),IntLiteral(1)),Block([]),CallExpr(Id("foo"),[])],BinaryOp("&&",Id("a"),IntLiteral(1)))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 344))

    def test_Dowhile3(self):
        input = """
        int main(){
        do a=1; {} foo(); while(a&&1);
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Dowhile([BinaryOp("=",Id("a"),IntLiteral(1)),Block([]),CallExpr(Id("foo"),[])],BinaryOp("&&",Id("a"),IntLiteral(1)))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 345))

    def test_Dowhile4(self):
        input="""boolean[] main(int a,float b[]){  
        do a==1;
        print("Nguyen Tran Minh Dang");
        foo(a[7]);
        while(true);
        }
        """
        expect=str(Program([FuncDecl(Id("main"),[VarDecl("a",IntType()),VarDecl("b",ArrayPointerType(FloatType()))],ArrayPointerType(BoolType()),Block([Dowhile([BinaryOp("==",Id("a"),IntLiteral(1)),CallExpr(Id("print"),[StringLiteral("Nguyen Tran Minh Dang")]),CallExpr(Id("foo"),[ArrayCell(Id("a"),IntLiteral(7))])],BooleanLiteral("true"))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 346))

    def test_Dowhile6(self):
        input="""boolean[] main(int a,float b[]){  
        do for(i=1;a+3;foo(a[9]))
            continue;
        break;
        } while(5E-1);
        }
        """
        expect=str(Program([FuncDecl(Id("main"),[VarDecl("a",IntType()),VarDecl("b",ArrayPointerType(FloatType()))],ArrayPointerType(BoolType()),Block([Dowhile([For(BinaryOp("=",Id("i"),IntLiteral(1)),BinaryOp("+",Id("a"),IntLiteral(3)),CallExpr(Id("foo"),[ArrayCell(Id("a"),IntLiteral(9))]),Continue()),Break()],FloatLiteral(0.5))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 347))

    def test_Dowhile7(self):
        input = """void main(){
        do print("a",b=4,a[5]);
        while (true)

        }
                """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([Dowhile([CallExpr(Id("print"),[StringLiteral("a"),BinaryOp("=",Id("b"),IntLiteral(4)),ArrayCell(Id("a"),IntLiteral(5))])],BooleanLiteral("true"))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 348))

    def test_Dowhile8(self):
        input = """void main(){
        do print("a",b=4,a[5]);
        while ("true")

        }
                """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([Dowhile([CallExpr(Id("print"),[StringLiteral("a"),BinaryOp("=",Id("b"),IntLiteral(4)),ArrayCell(Id("a"),IntLiteral(5))])],StringLiteral("true"))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 349))

    def test_Dowhile10(self):
        input = """
           int main() {
            do DANG = DANG+1;
             while a < 1;

           }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Dowhile([BinaryOp("=",Id("DANG"),BinaryOp("+",Id("DANG"),IntLiteral(1)))],BinaryOp("<",Id("a"),IntLiteral(1)))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 350))

    #9

    #FOR_STATEMENT
    def test_for(self):
        input = """int main() {}
        float func(int a){
        for(a=1;b=2;c=3) a=1;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([])),FuncDecl(Id("func"),[VarDecl("a",IntType())],FloatType(),Block([For(BinaryOp("=",Id("a"),IntLiteral(1)),BinaryOp("=",Id("b"),IntLiteral(2)),BinaryOp("=",Id("c"),IntLiteral(3)),BinaryOp("=",Id("a"),IntLiteral(1)))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 351))

    def test_for1(self):
        input = """int main() {}
        float func(int a){
        for(a=1;b=2;c=3) {a==3; int a; b=c=6<=a=1;}
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([])),FuncDecl(Id("func"),[VarDecl("a",IntType())],FloatType(),Block([For(BinaryOp("=",Id("a"),IntLiteral(1)),BinaryOp("=",Id("b"),IntLiteral(2)),BinaryOp("=",Id("c"),IntLiteral(3)),Block([BinaryOp("==",Id("a"),IntLiteral(3)),VarDecl("a",IntType()),BinaryOp("=",Id("b"),BinaryOp("=",Id("c"),BinaryOp("=",BinaryOp("<=",IntLiteral(6),Id("a")),IntLiteral(1))))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 352))

    def test_for3(self):
        input = """int main() {}
        float func(int a){
        for(a=1;b=2;c=3) {a==3; int a; b=c=6<=a=1;}
        if(a=1) if(c=3) {} {}
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([])),FuncDecl(Id("func"),[VarDecl("a",IntType())],FloatType(),Block([For(BinaryOp("=",Id("a"),IntLiteral(1)),BinaryOp("=",Id("b"),IntLiteral(2)),BinaryOp("=",Id("c"),IntLiteral(3)),Block([BinaryOp("==",Id("a"),IntLiteral(3)),VarDecl("a",IntType()),BinaryOp("=",Id("b"),BinaryOp("=",Id("c"),BinaryOp("=",BinaryOp("<=",IntLiteral(6),Id("a")),IntLiteral(1))))])),If(BinaryOp("=",Id("a"),IntLiteral(1)),If(BinaryOp("=",Id("c"),IntLiteral(3)),Block([]))),Block([])]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 353))

    def test_for4(self):
        input = """int main() {}
        float func(int a){
        for(a=1;b=2;c=3) {a==3; int a; b=c=6<=a=1;}
        if(a=3) if(a) {a&&b} (a==1)<=a=1;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([])),FuncDecl(Id("func"),[VarDecl("a",IntType())],FloatType(),Block([For(BinaryOp("=",Id("a"),IntLiteral(1)),BinaryOp("=",Id("b"),IntLiteral(2)),BinaryOp("=",Id("c"),IntLiteral(3)),Block([BinaryOp("==",Id("a"),IntLiteral(3)),VarDecl("a",IntType()),BinaryOp("=",Id("b"),BinaryOp("=",Id("c"),BinaryOp("=",BinaryOp("<=",IntLiteral(6),Id("a")),IntLiteral(1))))])),If(BinaryOp("=",Id("a"),IntLiteral(3)),If(Id("a"),Block([BinaryOp("&&",Id("a"),Id("b"))]))),BinaryOp("=",BinaryOp("<=",BinaryOp("==",Id("a"),IntLiteral(1)),Id("a")),IntLiteral(1))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 354))

    def test_for5(self):
        input = """int main() {}
        float func(int a){
        for(a=1;b=2;c=3) {a==3; int a; b=c=6<=a=1;}
        if(x=y) if(!r) {} (a==1);
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([])),FuncDecl(Id("func"),[VarDecl("a",IntType())],FloatType(),Block([For(BinaryOp("=",Id("a"),IntLiteral(1)),BinaryOp("=",Id("b"),IntLiteral(2)),BinaryOp("=",Id("c"),IntLiteral(3)),Block([BinaryOp("==",Id("a"),IntLiteral(3)),VarDecl("a",IntType()),BinaryOp("=",Id("b"),BinaryOp("=",Id("c"),BinaryOp("=",BinaryOp("<=",IntLiteral(6),Id("a")),IntLiteral(1))))])),If(BinaryOp("=",Id("x"),Id("y")),If(UnaryOp("!",Id("r")),Block([]))),BinaryOp("==",Id("a"),IntLiteral(1))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 355))

    def test_for9(self):
        input = """
        void main(){
        for(i-1;i;9-0)
        for(a*5; 5&&true;23==false) {}
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([For(BinaryOp("-",Id("i"),IntLiteral(1)),Id("i"),BinaryOp("-",IntLiteral(9),IntLiteral(0)),For(BinaryOp("*",Id("a"),IntLiteral(5)),BinaryOp("&&",IntLiteral(5),BooleanLiteral("true")),BinaryOp("==",IntLiteral(23),BooleanLiteral("false")),Block([])))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 356))

    def test_for10(self):
        input = """
        int main() {
            int i,j;
            for(i=0; i<=10 ; i=i+1)
                if (i%2 == 0) break; else continue;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("i",IntType()),VarDecl("j",IntType()),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<=",Id("i"),IntLiteral(10)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),If(BinaryOp("==",BinaryOp("%",Id("i"),IntLiteral(2)),IntLiteral(0)),Break(),Continue()))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 357))

    def test_for11(self):
        input = """
           int main() {
            for(i=0; i < n; i=i+1)
                a=a+1;
                return 0;
           }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),Id("n")),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1)))),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 358))

    #8

    #CALL_STATEMENT

    def test_call(self):
        input = """
        int main() {
            set(doc));

            return 0;
        }
        int func(){ 
            int a;
            a = main();
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("set"),[Id("doc")]),Return(IntLiteral(0))])),FuncDecl(Id("func"),[],IntType(),Block([VarDecl("a",IntType()),BinaryOp("=",Id("a"),CallExpr(Id("main"),[]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 359))

    def test_functcall(self):
        input = """boolean[] func() {
        foo(foo(5))
        temp(temp())}"""
        expect = str(Program([FuncDecl(Id("func"),[],ArrayPointerType(BoolType()),Block([CallExpr(Id("foo"),[CallExpr(Id("foo"),[IntLiteral(5)])]),CallExpr(Id("temp"),[CallExpr(Id("temp"),[])])]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 360))

    def test_call1(self):
        input = """void main(){
        print("a",b=4,a[5]);
        call(call(54E-1,a<=3));
        }
                """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([CallExpr(Id("print"),[StringLiteral("a"),BinaryOp("=",Id("b"),IntLiteral(4)),ArrayCell(Id("a"),IntLiteral(5))]),CallExpr(Id("call"),[CallExpr(Id("call"),[FloatLiteral(5.4),BinaryOp("<=",Id("a"),IntLiteral(3))])])]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 361))

    def test_call2(self):
        input="""
            boolean[] main(int a[], float b) {
            foo(3)[5];
            return 5;
            }
            """
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("a",ArrayPointerType(IntType())),VarDecl("b",FloatType())],ArrayPointerType(BoolType()),Block([ArrayCell(CallExpr(Id("foo"),[IntLiteral(3)]),IntLiteral(5)),Return(IntLiteral(5))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 362))

    def test_call3(self):
        input=""" float a;
            boolean[] main(int a[], float b) {
            foo(3)[5];
            return;
            }
            float[] temp(){}
            """
        expect = str(Program([VarDecl("a",FloatType()),FuncDecl(Id("main"),[VarDecl("a",ArrayPointerType(IntType())),VarDecl("b",FloatType())],ArrayPointerType(BoolType()),Block([ArrayCell(CallExpr(Id("foo"),[IntLiteral(3)]),IntLiteral(5)),Return()])),FuncDecl(Id("temp"),[],ArrayPointerType(FloatType()),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 363))

    def test_call4(self):
        input="""
        void main(){
        print("Banana la chuoi");
        n=log(10e2);
        Naichuoi(n);
        return "chuoi";
        }
        int[] NaiChuoi(int n){
        return n;}"""
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([CallExpr(Id("print"),[StringLiteral("Banana la chuoi")]),BinaryOp("=",Id("n"),CallExpr(Id("log"),[FloatLiteral(1000.0)])),CallExpr(Id("Naichuoi"),[Id("n")]),Return(StringLiteral("chuoi"))])),FuncDecl(Id("NaiChuoi"),[VarDecl("n",IntType())],ArrayPointerType(IntType()),Block([Return(Id("n"))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 364))

    def test_call5(self):
        input = """
        void main(int x, int y, int z[], boolean l) { AAAA("chan qua !!!");}
        
        """
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("x",IntType()),VarDecl("y",IntType()),VarDecl("z",ArrayPointerType(IntType())),VarDecl("l",BoolType())],VoidType(),Block([CallExpr(Id("AAAA"),[StringLiteral("chan qua !!!")])]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 365))

    #7

    #OTHER STATEMENT


    def test_type(self):
        input = """
                boolean boo;
                int foo(boolean boo){
                boo = true;
                }
                """
        expect = str(Program([VarDecl("boo",BoolType()),FuncDecl(Id("foo"),[VarDecl("boo",BoolType())],IntType(),Block([BinaryOp("=",Id("boo"),BooleanLiteral("true"))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 366))

    def test_continue(self):
        input = """int main() {continue;}
        float func(int a){
        for(a=1;b=2;c||6) {a==3; int a; b=c=6<=a=1;}

        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Continue()])),FuncDecl(Id("func"),[VarDecl("a",IntType())],FloatType(),Block([For(BinaryOp("=",Id("a"),IntLiteral(1)),BinaryOp("=",Id("b"),IntLiteral(2)),BinaryOp("||",Id("c"),IntLiteral(6)),Block([BinaryOp("==",Id("a"),IntLiteral(3)),VarDecl("a",IntType()),BinaryOp("=",Id("b"),BinaryOp("=",Id("c"),BinaryOp("=",BinaryOp("<=",IntLiteral(6),Id("a")),IntLiteral(1))))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 367))

    def test_return(self):
        input = """int main() {continue;}
        void func(int a[]){
            retrun;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Continue()])),FuncDecl(Id("func"),[VarDecl("a",ArrayPointerType(IntType()))],VoidType(),Block([Id("retrun")]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 368))

    def test_return1(self):
        input = """int main(int a[],int b) {
        do{} while(a==1);
        return a==1 && a<9;
        }       
        """
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("a",ArrayPointerType(IntType())),VarDecl("b",IntType())],IntType(),Block([Dowhile([Block([])],BinaryOp("==",Id("a"),IntLiteral(1))),Return(BinaryOp("&&",BinaryOp("==",Id("a"),IntLiteral(1)),BinaryOp("<",Id("a"),IntLiteral(9))))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 369))

    def test_return2(self):
        input="""
        void main(){
        print("Banana la chuoi");
        return "chuoi";
        }
        int[] NaiChuoi(int n){
        return n;}"""
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([CallExpr(Id("print"),[StringLiteral("Banana la chuoi")]),Return(StringLiteral("chuoi"))])),FuncDecl(Id("NaiChuoi"),[VarDecl("n",IntType())],ArrayPointerType(IntType()),Block([Return(Id("n"))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 370))

    def test_break3(self):
        input = """
        int main() {
            break;
            continue;
            for ("i=0";"i<10";i=i-1)
                break;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Break(),Continue(),For(StringLiteral("i=0"),StringLiteral("i<10"),BinaryOp("=",Id("i"),BinaryOp("-",Id("i"),IntLiteral(1))),Break())]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 371))

    def test_block(self):
        input = """int main() {
        foo(5);
        foo();
        {}
        {   {}   }
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("foo"),[IntLiteral(5)]),CallExpr(Id("foo"),[]),Block([]),Block([Block([])])]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 372))

    def test_block1(self):
        input = """int[] main(int a[],float c) {
        {(a+b)-4;
        {print("DAI HOC BACH KHOA TP.HCM"); {continue; break;}}}
        }"""
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("a",ArrayPointerType(IntType())),VarDecl("c",FloatType())],ArrayPointerType(IntType()),Block([Block([BinaryOp("-",BinaryOp("+",Id("a"),Id("b")),IntLiteral(4)),Block([CallExpr(Id("print"),[StringLiteral("DAI HOC BACH KHOA TP.HCM")]),Block([Continue(),Break()])])])]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 373))

    def test_block2(self):
        input = """int[] main(int a[],float c) {
        {a=1{b=2{c=3}{d=4}}}
        }"""
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("a",ArrayPointerType(IntType())),VarDecl("c",FloatType())],ArrayPointerType(IntType()),Block([Block([BinaryOp("=",Id("a"),IntLiteral(1)),Block([BinaryOp("=",Id("b"),IntLiteral(2)),Block([BinaryOp("=",Id("c"),IntLiteral(3))]),Block([BinaryOp("=",Id("d"),IntLiteral(4))])])])]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 374))

    def test_block3(self):
        input = """int[] main(int a[],float c) {
        {a=1{b=2{c=3}{d=4}}}
        {i=1;}{j=2}{+k=3+4;}
        }"""
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("a",ArrayPointerType(IntType())),VarDecl("c",FloatType())],ArrayPointerType(IntType()),Block([Block([BinaryOp("=",Id("a"),IntLiteral(1)),Block([BinaryOp("=",Id("b"),IntLiteral(2)),Block([BinaryOp("=",Id("c"),IntLiteral(3))]),Block([BinaryOp("=",Id("d"),IntLiteral(4))])])]),Block([BinaryOp("=",Id("i"),IntLiteral(1))]),Block([BinaryOp("=",Id("j"),IntLiteral(2))]),Block([BinaryOp("=",Id("k"),BinaryOp("+",IntLiteral(3),IntLiteral(4)))])]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 375))

    def test_block4(self):
        input = """int[] main(int a[],float c) {
        {a=1{b=2{c=3}{d=4}}}
        {i=1;}{j=2}{+k=3+4;}
        
        foo(a[a%3-6+1%2 || true],6);
        }"""
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("a",ArrayPointerType(IntType())),VarDecl("c",FloatType())],ArrayPointerType(IntType()),Block([Block([BinaryOp("=",Id("a"),IntLiteral(1)),Block([BinaryOp("=",Id("b"),IntLiteral(2)),Block([BinaryOp("=",Id("c"),IntLiteral(3))]),Block([BinaryOp("=",Id("d"),IntLiteral(4))])])]),Block([BinaryOp("=",Id("i"),IntLiteral(1))]),Block([BinaryOp("=",Id("j"),IntLiteral(2))]),Block([BinaryOp("=",Id("k"),BinaryOp("+",IntLiteral(3),IntLiteral(4)))]),CallExpr(Id("foo"),[ArrayCell(Id("a"),BinaryOp("||",BinaryOp("+",BinaryOp("-",BinaryOp("%",Id("a"),IntLiteral(3)),IntLiteral(6)),BinaryOp("%",IntLiteral(1),IntLiteral(2))),BooleanLiteral("true"))),IntLiteral(6)])]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 376))

    #11

    #EXPRESSION_STATEMENT

    def test_index(self):
        input = """int main() {continue;}
        float func(int a[]){
        foo(2)[x+3]=a[b[2]]+3;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Continue()])),FuncDecl(Id("func"),[VarDecl("a",ArrayPointerType(IntType()))],FloatType(),Block([BinaryOp("=",ArrayCell(CallExpr(Id("foo"),[IntLiteral(2)]),BinaryOp("+",Id("x"),IntLiteral(3))),BinaryOp("+",ArrayCell(Id("a"),ArrayCell(Id("b"),IntLiteral(2))),IntLiteral(3)))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 377))

    def test_index1(self):
        input = """int main() {continue;}
        float func(int a[]){
        foo(2)[a[x+3]]=a[b[2]]+3;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Continue()])),FuncDecl(Id("func"),[VarDecl("a",ArrayPointerType(IntType()))],FloatType(),Block([BinaryOp("=",ArrayCell(CallExpr(Id("foo"),[IntLiteral(2)]),ArrayCell(Id("a"),BinaryOp("+",Id("x"),IntLiteral(3)))),BinaryOp("+",ArrayCell(Id("a"),ArrayCell(Id("b"),IntLiteral(2))),IntLiteral(3)))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 378))

    def test_index2(self):
        input = """int main() {continue;}
        float[] func(int a[]){
        foo(2)[x+3]=(a[b[2] % 2]+3) - foo(4)-arr[3];
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Continue()])),FuncDecl(Id("func"),[VarDecl("a",ArrayPointerType(IntType()))],ArrayPointerType(FloatType()),Block([BinaryOp("=",ArrayCell(CallExpr(Id("foo"),[IntLiteral(2)]),BinaryOp("+",Id("x"),IntLiteral(3))),BinaryOp("-",BinaryOp("-",BinaryOp("+",ArrayCell(Id("a"),BinaryOp("%",ArrayCell(Id("b"),IntLiteral(2)),IntLiteral(2))),IntLiteral(3)),CallExpr(Id("foo"),[IntLiteral(4)])),ArrayCell(Id("arr"),IntLiteral(3))))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 379))

    def test_index3(self):
        input = """int main() {continue;}
        void func(int a[]){
        foo(2)[x+3]=a[b[2]]+3;
        return 1;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Continue()])),FuncDecl(Id("func"),[VarDecl("a",ArrayPointerType(IntType()))],VoidType(),Block([BinaryOp("=",ArrayCell(CallExpr(Id("foo"),[IntLiteral(2)]),BinaryOp("+",Id("x"),IntLiteral(3))),BinaryOp("+",ArrayCell(Id("a"),ArrayCell(Id("b"),IntLiteral(2))),IntLiteral(3))),Return(IntLiteral(1))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 380))

    def test_Expression(self):
        input = """
        int main(){
        a=(2+3)+b[3*3+4-2-(4&&2)];
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",Id("a"),BinaryOp("+",BinaryOp("+",IntLiteral(2),IntLiteral(3)),ArrayCell(Id("b"),BinaryOp("-",BinaryOp("-",BinaryOp("+",BinaryOp("*",IntLiteral(3),IntLiteral(3)),IntLiteral(4)),IntLiteral(2)),BinaryOp("&&",IntLiteral(4),IntLiteral(2))))))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 381))

    def test_assign1(self):
        input = """
        int main()
        {
        int a[4];
        a=b=c==d[5];
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",ArrayType(4,IntType())),BinaryOp("=",Id("a"),BinaryOp("=",Id("b"),BinaryOp("==",Id("c"),ArrayCell(Id("d"),IntLiteral(5)))))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 382))

    def test_assign2(self):
        input = """
        int main()
        {
        foo(1,2);
        f[0]=1.2e-1;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("foo"),[IntLiteral(1),IntLiteral(2)]),BinaryOp("=",ArrayCell(Id("f"),IntLiteral(0)),FloatLiteral(0.12))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 383))

    def test_assign3(self):
        input = """void main(){
            foo()[20] = 100;
            Tohka="Yum Yum";
            foo(a, b, 10)[0] = 2;
            Kurumi[4] = "ara ara";
            Title = "Date A Live";
            a = 16.5e-6;  //Word Art Online
            b="chap123"; //Tokyo goul 
            return;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("=",ArrayCell(CallExpr(Id("foo"),[]),IntLiteral(20)),IntLiteral(100)),BinaryOp("=",Id("Tohka"),StringLiteral("Yum Yum")),BinaryOp("=",ArrayCell(CallExpr(Id("foo"),[Id("a"),Id("b"),IntLiteral(10)]),IntLiteral(0)),IntLiteral(2)),BinaryOp("=",ArrayCell(Id("Kurumi"),IntLiteral(4)),StringLiteral("ara ara")),BinaryOp("=",Id("Title"),StringLiteral("Date A Live")),BinaryOp("=",Id("a"),FloatLiteral(1.65e-05)),BinaryOp("=",Id("b"),StringLiteral("chap123")),Return()]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 384))

    def test_expression(self):
        input = """int main() {
                    a = 1 + 2;
                }"""
        expect = str(Program([FuncDecl(Id("main"), [], IntType(),Block([BinaryOp("=", Id("a"), BinaryOp("+", IntLiteral(1), IntLiteral(2)))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 385))

    def test_expression1(self):
        input="""int main() {
            int a,b,c;
            a = a*c;
            b = foo((foo()[a || b && c - d] % 20) - 10) && a;
            }
            """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),BinaryOp("=",Id("a"),BinaryOp("*",Id("a"),Id("c"))),BinaryOp("=",Id("b"),BinaryOp("&&",CallExpr(Id("foo"),[BinaryOp("-",BinaryOp("%",ArrayCell(CallExpr(Id("foo"),[]),BinaryOp("||",Id("a"),BinaryOp("&&",Id("b"),BinaryOp("-",Id("c"),Id("d"))))),IntLiteral(20)),IntLiteral(10))]),Id("a")))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 386))

    def test_expression2(self):
        input="""void main() {
            int a,b,c,d[1];
            a = a*c;
            a = d[b+c];
            do{
            }
            {         
            } while (a || 3 && true )!= 0;
            
            }
            """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",ArrayType(1,IntType())),BinaryOp("=",Id("a"),BinaryOp("*",Id("a"),Id("c"))),BinaryOp("=",Id("a"),ArrayCell(Id("d"),BinaryOp("+",Id("b"),Id("c")))),Dowhile([Block([]),Block([])],BinaryOp("!=",BinaryOp("||",Id("a"),BinaryOp("&&",IntLiteral(3),BooleanLiteral("true"))),IntLiteral(0)))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 387))

    def test_expression3(self):
        input = """void main() {
            int a,b,c,d[1];
            a = a*c;
            a = d[b+c];
            do
            a = c +d[0] + a;
            b = b*c;
            while (a || 3 && true )!= 0;         
            }
            """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",ArrayType(1,IntType())),BinaryOp("=",Id("a"),BinaryOp("*",Id("a"),Id("c"))),BinaryOp("=",Id("a"),ArrayCell(Id("d"),BinaryOp("+",Id("b"),Id("c")))),Dowhile([BinaryOp("=",Id("a"),BinaryOp("+",BinaryOp("+",Id("c"),ArrayCell(Id("d"),IntLiteral(0))),Id("a"))),BinaryOp("=",Id("b"),BinaryOp("*",Id("b"),Id("c")))],BinaryOp("!=",BinaryOp("||",Id("a"),BinaryOp("&&",IntLiteral(3),BooleanLiteral("true"))),IntLiteral(0)))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 388))

    def test_expression4(self):
        input="""string[] Kirito() {
            string str[10], str[20];
            int a,b[1],c[2];
            a = -12.E-2;
            a = a*c;
            b = foo((foo()[a || b && c - d] % 20) - 10) && a;
            // Isuka Shidou
            /* Akatsuki Kojou
           
            la de tu chan to*/
            """
        expect = str(Program([FuncDecl(Id("Kirito"),[],ArrayPointerType(StringType()),Block([VarDecl("str",ArrayType(10,StringType())),VarDecl("str",ArrayType(20,StringType())),VarDecl("a",IntType()),VarDecl("b",ArrayType(1,IntType())),VarDecl("c",ArrayType(2,IntType())),BinaryOp("=",Id("a"),UnaryOp("-",FloatLiteral(0.12))),BinaryOp("=",Id("a"),BinaryOp("*",Id("a"),Id("c"))),BinaryOp("=",Id("b"),BinaryOp("&&",CallExpr(Id("foo"),[BinaryOp("-",BinaryOp("%",ArrayCell(CallExpr(Id("foo"),[]),BinaryOp("||",Id("a"),BinaryOp("&&",Id("b"),BinaryOp("-",Id("c"),Id("d"))))),IntLiteral(20)),IntLiteral(10))]),Id("a")))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 389))

    def test_expression5(self):
        input="""int main() {  
            c[20] = c[10]+202.e-8;
            if(false)
            a = "Hinata";
            else
            b=15;
           }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",ArrayCell(Id("c"),IntLiteral(20)),BinaryOp("+",ArrayCell(Id("c"),IntLiteral(10)),FloatLiteral(2.02e-06))),If(BooleanLiteral("false"),BinaryOp("=",Id("a"),StringLiteral("Hinata")),BinaryOp("=",Id("b"),IntLiteral(15)))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 390))

    def test_expression6(self):
        input="""void main(){
            int a;
            a = a-10+9*8/2;
            return 1;
            }"""
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()),BinaryOp("=",Id("a"),BinaryOp("+",BinaryOp("-",Id("a"),IntLiteral(10)),BinaryOp("/",BinaryOp("*",IntLiteral(9),IntLiteral(8)),IntLiteral(2)))),Return(IntLiteral(1))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 391))

    def test_expression7(self):
        """Simple program: int main() {} """
        input = """int main() {
            a = a*c;
            !b;

            }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",Id("a"),BinaryOp("*",Id("a"),Id("c"))),UnaryOp("!",Id("b"))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 392))

    def test_expression8(self):
        """Simple program: int main() {} """
        input = """int main() {
            int a,b,c;
            a = a*c;
            foo(2)[3+x] = a[b[2]] + 3 ;
            a = a+b;
            }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),BinaryOp("=",Id("a"),BinaryOp("*",Id("a"),Id("c"))),BinaryOp("=",ArrayCell(CallExpr(Id("foo"),[IntLiteral(2)]),BinaryOp("+",IntLiteral(3),Id("x"))),BinaryOp("+",ArrayCell(Id("a"),ArrayCell(Id("b"),IntLiteral(2))),IntLiteral(3))),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),Id("b")))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 393))

    def test_expression9(self):
        input = """
           int main() {
               -a = b + 1  % c;
           }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",UnaryOp("-",Id("a")),BinaryOp("+",Id("b"),BinaryOp("%",IntLiteral(1),Id("c"))))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 394))

    def test_expression10(self):
        input = """
           int main() {
               -a = b + 1  % c * (b+c);
           }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",UnaryOp("-",Id("a")),BinaryOp("+",Id("b"),BinaryOp("*",BinaryOp("%",IntLiteral(1),Id("c")),BinaryOp("+",Id("b"),Id("c")))))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 395))

    def test_expression11(self):
        input="""void main(int x, int y[], int z, boolean l[]) {
            putIntLn(x);
            string s;
            a<=b!=(-c || true);
        }"""
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("x",IntType()),VarDecl("y",ArrayPointerType(IntType())),VarDecl("z",IntType()),VarDecl("l",ArrayPointerType(BoolType()))],VoidType(),Block([CallExpr(Id("putIntLn"),[Id("x")]),VarDecl("s",StringType()),BinaryOp("!=",BinaryOp("<=",Id("a"),Id("b")),BinaryOp("||",UnaryOp("-",Id("c")),BooleanLiteral("true")))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 396))

    def test_expression12(self):
        input = """
        int main(int x, int y[], int z, boolean l[]) {
            putIntLn(x);
            string s;
            float a[5],b,c,d;
            boolean x[10];
            x= x + 5;
            s = "Khong muon lam nua";
            return x;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("x",IntType()),VarDecl("y",ArrayPointerType(IntType())),VarDecl("z",IntType()),VarDecl("l",ArrayPointerType(BoolType()))],IntType(),Block([CallExpr(Id("putIntLn"),[Id("x")]),VarDecl("s",StringType()),VarDecl("a",ArrayType(5,FloatType())),VarDecl("b",FloatType()),VarDecl("c",FloatType()),VarDecl("d",FloatType()),VarDecl("x",ArrayType(10,BoolType())),BinaryOp("=",Id("x"),BinaryOp("+",Id("x"),IntLiteral(5))),BinaryOp("=",Id("s"),StringLiteral("Khong muon lam nua")),Return(Id("x"))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 397))

    def test_expression_13(self):
        input = """
        float main(int x, float y[], int z, boolean l[]) {
            putIntLn(x);
            string s;
            float a[5],b,c,d;
            boolean x[10];
            x= x + 5;
            b = 1e2;
            y[0]= x + b;
            s = "Tha cho em di";
            return y[0];
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("x",IntType()),VarDecl("y",ArrayPointerType(FloatType())),VarDecl("z",IntType()),VarDecl("l",ArrayPointerType(BoolType()))],FloatType(),Block([CallExpr(Id("putIntLn"),[Id("x")]),VarDecl("s",StringType()),VarDecl("a",ArrayType(5,FloatType())),VarDecl("b",FloatType()),VarDecl("c",FloatType()),VarDecl("d",FloatType()),VarDecl("x",ArrayType(10,BoolType())),BinaryOp("=",Id("x"),BinaryOp("+",Id("x"),IntLiteral(5))),BinaryOp("=",Id("b"),FloatLiteral(100.0)),BinaryOp("=",ArrayCell(Id("y"),IntLiteral(0)),BinaryOp("+",Id("x"),Id("b"))),BinaryOp("=",Id("s"),StringLiteral("Tha cho em di")),Return(ArrayCell(Id("y"),IntLiteral(0)))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 398))


    def test_string(self):
        input = """
           int main() {

               a = "abcskd\\n";

           }"""
        expect = str(
            Program([FuncDecl(Id('main'), [], IntType(), Block([BinaryOp('=', Id('a'), StringLiteral("abcskd\\n"))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 399))

    def test_string1(self):
        """test return value type"""
        input = """string main(string lastname, string firstname) {
            return firstname + lastname;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("lastname",StringType()),VarDecl("firstname",StringType())],StringType(),Block([Return(BinaryOp("+",Id("firstname"),Id("lastname")))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 400))



