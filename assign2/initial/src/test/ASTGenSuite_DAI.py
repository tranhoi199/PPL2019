import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    
    def test_var_decl(self):
        input = """float a,b,c,f[5]; 
        int m[1],n;"""
        expect = "Program([VarDecl(a,FloatType),VarDecl(b,FloatType),VarDecl(c,FloatType),VarDecl(f,ArrayType(FloatType,5)),VarDecl(m,ArrayType(IntType,1)),VarDecl(n,IntType)])"
        self.assertTrue(TestAST.checkASTGen(input,expect,300))

    def test_var_decl1(self):
        input = """float a,b[5];"""
        expect = "Program([VarDecl(a,FloatType),VarDecl(b,ArrayType(FloatType,5))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,301))

    def test_var_decl2(self):
        input = """int a,b,c[2];"""
        expect = "Program([VarDecl(a,IntType),VarDecl(b,IntType),VarDecl(c,ArrayType(IntType,2))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,302))

    def test_var_decl3(self):
        input = """int a;"""
        expect = "Program([VarDecl(a,IntType)])"
        self.assertTrue(TestAST.checkASTGen(input,expect,303))

    def test_var_decl4(self):
        input = """int a,b,c[2];
        string ss;
        boolean bo;
        """
        expect = "Program([VarDecl(a,IntType),VarDecl(b,IntType),VarDecl(c,ArrayType(IntType,2)),VarDecl(ss,StringType),VarDecl(bo,BoolType)])"
        self.assertTrue(TestAST.checkASTGen(input,expect,304))

    def test_var_decl5(self):
        input = """int a,b,c[2];
        string ss;
        float num;"""
        expect = "Program([VarDecl(a,IntType),VarDecl(b,IntType),VarDecl(c,ArrayType(IntType,2)),VarDecl(ss,StringType),VarDecl(num,FloatType)])"
        self.assertTrue(TestAST.checkASTGen(input,expect,305))

    def test_func_decl(self):
        input = """int foo(int a,float b[]){
            break;
            continue;
            int a, b[5];
        }"""
        expect = "Program([FuncDecl(Id(foo),[VarDecl(a,IntType),VarDecl(b,ArrayTypePointer(FloatType))],IntType,Block([Break(),Continue(),VarDecl(a,IntType),VarDecl(b,ArrayType(IntType,5))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,306))

    def test_func_decl1(self):
        input = """int foo(int a,float b[]){
            int a;
        }"""
        expect = "Program([FuncDecl(Id(foo),[VarDecl(a,IntType),VarDecl(b,ArrayTypePointer(FloatType))],IntType,Block([VarDecl(a,IntType)]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,307))

    def test_func_decl2(self):
        input = """void foo(int a){
            int a; a =7;
        }"""
        expect = "Program([FuncDecl(Id(foo),[VarDecl(a,IntType)],VoidType,Block([VarDecl(a,IntType),BinaryOp(=,Id(a),IntLiteral(7))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,308))

    def test_func_decl3(self):
        input = """int foo(int a,float b[]){
            if (a==1)  break;
        }"""
        expect = "Program([FuncDecl(Id(foo),[VarDecl(a,IntType),VarDecl(b,ArrayTypePointer(FloatType))],IntType,Block([If(BinaryOp(==,Id(a),IntLiteral(1)),Break())]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,309))

    def test_func_decl4(self):
        input = """int foo(int a,float b[]){
            if (a==1)  continue;
        }"""
        expect = "Program([FuncDecl(Id(foo),[VarDecl(a,IntType),VarDecl(b,ArrayTypePointer(FloatType))],IntType,Block([If(BinaryOp(==,Id(a),IntLiteral(1)),Continue())]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,310))

    def test_func_decl5(self):
        input = """int foo(int a,float b[]){
            if (a==1)  return;
        }"""
        expect = "Program([FuncDecl(Id(foo),[VarDecl(a,IntType),VarDecl(b,ArrayTypePointer(FloatType))],IntType,Block([If(BinaryOp(==,Id(a),IntLiteral(1)),Return())]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,311))

    def test_func_decl6(self):
        input = """int foo(int a,float b[]){
            if (a==1)  return 1;
        }"""
        expect = "Program([FuncDecl(Id(foo),[VarDecl(a,IntType),VarDecl(b,ArrayTypePointer(FloatType))],IntType,Block([If(BinaryOp(==,Id(a),IntLiteral(1)),Return(IntLiteral(1)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,312))

    def test_func_decl7(self):
        input = """int foo(int a,float b[]){
            if (a==1)  return "My name is Dai";
        }"""
        expect = "Program([FuncDecl(Id(foo),[VarDecl(a,IntType),VarDecl(b,ArrayTypePointer(FloatType))],IntType,Block([If(BinaryOp(==,Id(a),IntLiteral(1)),Return(StringLiteral(My name is Dai)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,313))

    def test_func_decl8(self):
        input = """int foo(int a,float b[]){
            if (a==1)  return true;
        }"""
        expect = "Program([FuncDecl(Id(foo),[VarDecl(a,IntType),VarDecl(b,ArrayTypePointer(FloatType))],IntType,Block([If(BinaryOp(==,Id(a),IntLiteral(1)),Return(BooleanLiteral(true)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,314))

    def test_func_decl9(self):
        input = """int foo(int a,float b[]){
            if (a==1)  return false;
        }"""
        expect = "Program([FuncDecl(Id(foo),[VarDecl(a,IntType),VarDecl(b,ArrayTypePointer(FloatType))],IntType,Block([If(BinaryOp(==,Id(a),IntLiteral(1)),Return(BooleanLiteral(false)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,315))

    def test_func_decl10(self):
        input = """int foo(int a,float b[]){
            for(i=0;i<5;i=i+1) a = 7;
        }"""
        expect = "Program([FuncDecl(Id(foo),[VarDecl(a,IntType),VarDecl(b,ArrayTypePointer(FloatType))],IntType,Block([For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(<,Id(i),IntLiteral(5));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));BinaryOp(=,Id(a),IntLiteral(7)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,316))

    def test_func_decl11_for(self):
        input = """int foo(int a,float b[]){
            for(i=0;i<5;i=i+1) { a = a +1 ;}
        }"""
        expect = "Program([FuncDecl(Id(foo),[VarDecl(a,IntType),VarDecl(b,ArrayTypePointer(FloatType))],IntType,Block([For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(<,Id(i),IntLiteral(5));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,317))


    def test_func_decl12_do_while(self):
        input = """int foo(int a,float b[]){
            do a = a - 1; while (a == true) ;
        }"""
        expect = "Program([FuncDecl(Id(foo),[VarDecl(a,IntType),VarDecl(b,ArrayTypePointer(FloatType))],IntType,Block([Dowhile([BinaryOp(=,Id(a),BinaryOp(-,Id(a),IntLiteral(1)))],BinaryOp(==,Id(a),BooleanLiteral(true)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,318))

    
    def test_func_decl13_do_while(self):
        input = """int foo(){
            do { a = a + 1;} while a < 10 ;
        }"""
        expect = "Program([FuncDecl(Id(foo),[],IntType,Block([Dowhile([Block([BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)))])],BinaryOp(<,Id(a),IntLiteral(10)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,319))

    def test_func_decl14_do_while(self):
        input = """int foo(int a){
            do { 
                int a; a = 7; 
                if ( a  == 7) a= a-1;
            } while true;
        }"""
        expect = "Program([FuncDecl(Id(foo),[VarDecl(a,IntType)],IntType,Block([Dowhile([Block([VarDecl(a,IntType),BinaryOp(=,Id(a),IntLiteral(7)),If(BinaryOp(==,Id(a),IntLiteral(7)),BinaryOp(=,Id(a),BinaryOp(-,Id(a),IntLiteral(1))))])],BooleanLiteral(true))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,320))

    def test_func_decl15_funcall(self):
        input = """void foo(int a[]){
            print(7);
        }"""
        expect = "Program([FuncDecl(Id(foo),[VarDecl(a,ArrayTypePointer(IntType))],VoidType,Block([CallExpr(Id(print),[IntLiteral(7)])]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,321))

    def test_func_decl16_funcall(self):
        input = """int foo(int a){
            float a ;
            a = 1; b= 2;
            sum(a,b);
        }"""
        expect = "Program([FuncDecl(Id(foo),[VarDecl(a,IntType)],IntType,Block([VarDecl(a,FloatType),BinaryOp(=,Id(a),IntLiteral(1)),BinaryOp(=,Id(b),IntLiteral(2)),CallExpr(Id(sum),[Id(a),Id(b)])]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,322))

    

    def test_func_decl17(self):
        input = """int foo(int a){
            a != b;
        }"""
        expect = "Program([FuncDecl(Id(foo),[VarDecl(a,IntType)],IntType,Block([BinaryOp(!=,Id(a),Id(b))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,323))

    def test_func_decl18(self):
        input = """int foo(float num){
            a = b&&c + d;
        }"""
        expect = "Program([FuncDecl(Id(foo),[VarDecl(num,FloatType)],IntType,Block([BinaryOp(=,Id(a),BinaryOp(&&,Id(b),BinaryOp(+,Id(c),Id(d))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,324))

    def test_func_decl19(self):
        input = """int foo(int a[]){
            a = !b;
        }"""
        expect = "Program([FuncDecl(Id(foo),[VarDecl(a,ArrayTypePointer(IntType))],IntType,Block([BinaryOp(=,Id(a),UnaryOp(!,Id(b)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,325))

    def test_func_decl20(self):
        input = """int foo(int a,float b[], string d, boolean e){
            
        }"""
        expect = "Program([FuncDecl(Id(foo),[VarDecl(a,IntType),VarDecl(b,ArrayTypePointer(FloatType)),VarDecl(d,StringType),VarDecl(e,BoolType)],IntType,Block([]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,326))

    def test_func_decl21(self):
        input = """int foo(int a){
            tb = average(a,b,c);
            print(tb);
        }"""
        expect = "Program([FuncDecl(Id(foo),[VarDecl(a,IntType)],IntType,Block([BinaryOp(=,Id(tb),CallExpr(Id(average),[Id(a),Id(b),Id(c)])),CallExpr(Id(print),[Id(tb)])]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,327))

    def test_func_decl22_for_if(self):
        input = """int foo(int a){
            for(i = 0;i!= 100; i=i+1){
                if(i%2==0) i=i*2;
                else i = i -1;
            }
        }"""
        expect = "Program([FuncDecl(Id(foo),[VarDecl(a,IntType)],IntType,Block([For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(!=,Id(i),IntLiteral(100));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([If(BinaryOp(==,BinaryOp(%,Id(i),IntLiteral(2)),IntLiteral(0)),BinaryOp(=,Id(i),BinaryOp(*,Id(i),IntLiteral(2))),BinaryOp(=,Id(i),BinaryOp(-,Id(i),IntLiteral(1))))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,328))

    def test_func_decl23(self):
        input = """int main() {
            if(true) a=10;
        }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([If(BooleanLiteral(true),BinaryOp(=,Id(a),IntLiteral(10)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,329))

    def test_var_many_decl(self):
        input = """int a; float b,c,d[3]; boolean e; string s; """
        expect = "Program([VarDecl(a,IntType),VarDecl(b,FloatType),VarDecl(c,FloatType),VarDecl(d,ArrayType(FloatType,3)),VarDecl(e,BoolType),VarDecl(s,StringType)])"
        self.assertTrue(TestAST.checkASTGen(input,expect,330))

    def test_func_decl24(self):
        input = """void b(int a[],int b){
                          int a;a=1;println(a);
                          {
                            int b;b=1;
                            println(b);
                          }
                }"""
        expect = "Program([FuncDecl(Id(b),[VarDecl(a,ArrayTypePointer(IntType)),VarDecl(b,IntType)],VoidType,Block([VarDecl(a,IntType),BinaryOp(=,Id(a),IntLiteral(1)),CallExpr(Id(println),[Id(a)]),Block([VarDecl(b,IntType),BinaryOp(=,Id(b),IntLiteral(1)),CallExpr(Id(println),[Id(b)])])]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,331))

    def test_func_decl25(self):
        input = """void Calculate(){}"""
        expect = "Program([FuncDecl(Id(Calculate),[],VoidType,Block([]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,332))

    def test_func_decl26(self):
        input = """void foo(){
                boolean b ;
                b = true;
                if( !b == false) 
                    println(" b is true");
            }"""
        expect = "Program([FuncDecl(Id(foo),[],VoidType,Block([VarDecl(b,BoolType),BinaryOp(=,Id(b),BooleanLiteral(true)),If(BinaryOp(==,UnaryOp(!,Id(b)),BooleanLiteral(false)),CallExpr(Id(println),[StringLiteral( b is true)]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,333))

    def test_func_decl27(self):
        input = """
        void main(){
            int oddSum, evenSum,arr[10],i;
            oddSum = evenSum =0;
            for(i=0;i<10;i=i+1)
                arr[i]=i;
            for(i=0;i<10;i=i+1){
                if(arr[i]%2==0)
                    evenSum = evenSum + arr[i];
                else
                    oddSum = oddSum + arr[i];
            }        
        }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([VarDecl(oddSum,IntType),VarDecl(evenSum,IntType),VarDecl(arr,ArrayType(IntType,10)),VarDecl(i,IntType),BinaryOp(=,Id(oddSum),BinaryOp(=,Id(evenSum),IntLiteral(0))),For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(<,Id(i),IntLiteral(10));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));BinaryOp(=,ArrayCell(Id(arr),Id(i)),Id(i))),For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(<,Id(i),IntLiteral(10));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([If(BinaryOp(==,BinaryOp(%,ArrayCell(Id(arr),Id(i)),IntLiteral(2)),IntLiteral(0)),BinaryOp(=,Id(evenSum),BinaryOp(+,Id(evenSum),ArrayCell(Id(arr),Id(i)))),BinaryOp(=,Id(oddSum),BinaryOp(+,Id(oddSum),ArrayCell(Id(arr),Id(i)))))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,334))

    def test_func_decl28(self):
        input = """
                void main(){
                    int mark;
                }
                void result(int mark){
                  if(mark<5)
                    println("Trung binh");
                  else if (5<=mark&&mark<8)
                    println("Kha");
                  else
                    println("Gioi");
                }        
        """
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([VarDecl(mark,IntType)])),FuncDecl(Id(result),[VarDecl(mark,IntType)],VoidType,Block([If(BinaryOp(<,Id(mark),IntLiteral(5)),CallExpr(Id(println),[StringLiteral(Trung binh)]),If(BinaryOp(&&,BinaryOp(<=,IntLiteral(5),Id(mark)),BinaryOp(<,Id(mark),IntLiteral(8))),CallExpr(Id(println),[StringLiteral(Kha)]),CallExpr(Id(println),[StringLiteral(Gioi)])))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,335))

    def test_func_decl29(self):
        input = """
                void main(){
                    int i;
                    for(i=0;i<10;i=i+1)
                    {
                      println(i);
                      if(i == 5)
                        continue;
                      if(i==9)
                        break;
                    }
                }        
        """
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([VarDecl(i,IntType),For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(<,Id(i),IntLiteral(10));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([CallExpr(Id(println),[Id(i)]),If(BinaryOp(==,Id(i),IntLiteral(5)),Continue()),If(BinaryOp(==,Id(i),IntLiteral(9)),Break())]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,336))

    def test_func_decl30(self):
        input = """
                void main(){
                    int i;
                    i = 0;
                    do 
                      println(i);
                      i=i+1;
                      if(i==9)
                        break;
                    while(i<10);
                }         
        """
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([VarDecl(i,IntType),BinaryOp(=,Id(i),IntLiteral(0)),Dowhile([CallExpr(Id(println),[Id(i)]),BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1))),If(BinaryOp(==,Id(i),IntLiteral(9)),Break())],BinaryOp(<,Id(i),IntLiteral(10)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,337))

    def test_func_decl31(self):
        input = """
                void main(){
                    do {
                      println(i);
                      i=i+1;
                      if(i==9)
                        break;
                      else if(i==5)
                        continue;
                    }
                    while(i<10);
                }         
        """
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([Dowhile([Block([CallExpr(Id(println),[Id(i)]),BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1))),If(BinaryOp(==,Id(i),IntLiteral(9)),Break(),If(BinaryOp(==,Id(i),IntLiteral(5)),Continue()))])],BinaryOp(<,Id(i),IntLiteral(10)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,338))

    def test_func_decl32(self):
        input = """
                void main(){
                  for(i=0;i<5;i=i+1)
                    for(j=10;j>5;j=j-1)
                    {
                      temp = a[i];
                      a[i]=a[j];
                      a[j] = temp;
                    }
                }         
        """
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(<,Id(i),IntLiteral(5));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));For(BinaryOp(=,Id(j),IntLiteral(10));BinaryOp(>,Id(j),IntLiteral(5));BinaryOp(=,Id(j),BinaryOp(-,Id(j),IntLiteral(1)));Block([BinaryOp(=,Id(temp),ArrayCell(Id(a),Id(i))),BinaryOp(=,ArrayCell(Id(a),Id(i)),ArrayCell(Id(a),Id(j))),BinaryOp(=,ArrayCell(Id(a),Id(j)),Id(temp))])))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,339))

    def test_func_decl33(self):
        input = """
                void main(){
                  for(i=0;i<5;i=i+1){
                    do{
                      temp = a[i];
                      a[i]=a[j];
                      a[j] = temp;
                      j = j-1;
                    }
                    while (j<5);
                  }
                }        
        """
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(<,Id(i),IntLiteral(5));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([Dowhile([Block([BinaryOp(=,Id(temp),ArrayCell(Id(a),Id(i))),BinaryOp(=,ArrayCell(Id(a),Id(i)),ArrayCell(Id(a),Id(j))),BinaryOp(=,ArrayCell(Id(a),Id(j)),Id(temp)),BinaryOp(=,Id(j),BinaryOp(-,Id(j),IntLiteral(1)))])],BinaryOp(<,Id(j),IntLiteral(5)))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,340))

    def test_func_decl34(self):
        input = """
                int main(){
                  int a;a=0;
                  if(a+1)
                    println("Hello");
                }        
        """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(a,IntType),BinaryOp(=,Id(a),IntLiteral(0)),If(BinaryOp(+,Id(a),IntLiteral(1)),CallExpr(Id(println),[StringLiteral(Hello)]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,341))

    def test_func_decl35(self):
        input = """
                int main(){
                  int a;a=0;
                  if(a==0){
                      int b;
                      b=foo(2)[3];
                  }
                }       
        """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(a,IntType),BinaryOp(=,Id(a),IntLiteral(0)),If(BinaryOp(==,Id(a),IntLiteral(0)),Block([VarDecl(b,IntType),BinaryOp(=,Id(b),ArrayCell(CallExpr(Id(foo),[IntLiteral(2)]),IntLiteral(3)))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,342))

    def test_func_decl36(self):
        input = """
                int main(){
                  int a;
                  for(a=0;a+3;a=a+1)
                    a=a-1;
                }        
        """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(a,IntType),For(BinaryOp(=,Id(a),IntLiteral(0));BinaryOp(+,Id(a),IntLiteral(3));BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)));BinaryOp(=,Id(a),BinaryOp(-,Id(a),IntLiteral(1))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,343))

    def test_func_decl37(self):
        input = """
                int main(){
                  boolean a;
                  a=true;
                  do { }
                  while a+3 ;
                }       
        """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(a,BoolType),BinaryOp(=,Id(a),BooleanLiteral(true)),Dowhile([Block([])],BinaryOp(+,Id(a),IntLiteral(3)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,344))

    def test_func_decl38(self):
        input = """
        int foo() {
          a=b[d]+ 12[10];
        }
        """
        expect = "Program([FuncDecl(Id(foo),[],IntType,Block([BinaryOp(=,Id(a),BinaryOp(+,ArrayCell(Id(b),Id(d)),ArrayCell(IntLiteral(12),IntLiteral(10))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,345))

    def test_func_decl39(self):
        input = """
        int foo() {
          foo(2)[3]=arr[7]=true;
        }
        """
        expect = "Program([FuncDecl(Id(foo),[],IntType,Block([BinaryOp(=,ArrayCell(CallExpr(Id(foo),[IntLiteral(2)]),IntLiteral(3)),BinaryOp(=,ArrayCell(Id(arr),IntLiteral(7)),BooleanLiteral(true)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,346))

    def test_func_decl40(self):
        input = """
        int foo() {
          foo(2)[3]=a||b&&(c-35.4e10)*9+10.0/4+true;
        }
        """
        expect = "Program([FuncDecl(Id(foo),[],IntType,Block([BinaryOp(=,ArrayCell(CallExpr(Id(foo),[IntLiteral(2)]),IntLiteral(3)),BinaryOp(||,Id(a),BinaryOp(&&,Id(b),BinaryOp(+,BinaryOp(+,BinaryOp(*,BinaryOp(-,Id(c),FloatLiteral(354000000000.0)),IntLiteral(9)),BinaryOp(/,FloatLiteral(10.0),IntLiteral(4))),BooleanLiteral(true)))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,347))

    def test_func_decl41(self):
        input = """
        int foo() {
          foo[3]= ((1+3*5)==(c-9.0+true))!=foo(3.4,1*5e10,"string");
        }
        """
        expect = "Program([FuncDecl(Id(foo),[],IntType,Block([BinaryOp(=,ArrayCell(Id(foo),IntLiteral(3)),BinaryOp(!=,BinaryOp(==,BinaryOp(+,IntLiteral(1),BinaryOp(*,IntLiteral(3),IntLiteral(5))),BinaryOp(+,BinaryOp(-,Id(c),FloatLiteral(9.0)),BooleanLiteral(true))),CallExpr(Id(foo),[FloatLiteral(3.4),BinaryOp(*,IntLiteral(1),FloatLiteral(50000000000.0)),StringLiteral(string)])))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,348))

    def test_func_decl42(self):
        input = """
        int foo() {
          foo[3]= ((1+3*5==9)>=(c-9.0+true!=3))<foo(3.4!=5,1*5e10<4,"string");
        }
        """
        expect = "Program([FuncDecl(Id(foo),[],IntType,Block([BinaryOp(=,ArrayCell(Id(foo),IntLiteral(3)),BinaryOp(<,BinaryOp(>=,BinaryOp(==,BinaryOp(+,IntLiteral(1),BinaryOp(*,IntLiteral(3),IntLiteral(5))),IntLiteral(9)),BinaryOp(!=,BinaryOp(+,BinaryOp(-,Id(c),FloatLiteral(9.0)),BooleanLiteral(true)),IntLiteral(3))),CallExpr(Id(foo),[BinaryOp(!=,FloatLiteral(3.4),IntLiteral(5)),BinaryOp(<,BinaryOp(*,IntLiteral(1),FloatLiteral(50000000000.0)),IntLiteral(4)),StringLiteral(string)])))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,349))

    def test_func_decl43(self):
        input = """
        int foo() {
          foo[3]= a(ab[10[1]])[c+2] ;
        }
        """
        expect = "Program([FuncDecl(Id(foo),[],IntType,Block([BinaryOp(=,ArrayCell(Id(foo),IntLiteral(3)),ArrayCell(CallExpr(Id(a),[ArrayCell(Id(ab),ArrayCell(IntLiteral(10),IntLiteral(1)))]),BinaryOp(+,Id(c),IntLiteral(2))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,350))

    def test_func_decl44(self):
        input = """
        int foo() {
          true;
          false;
        }
        """
        expect = "Program([FuncDecl(Id(foo),[],IntType,Block([BooleanLiteral(true),BooleanLiteral(false)]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,351))

    def test_func_decl45(self):
        input = """
        int foo() {
          100;
          12.2e2;
        }
        """
        expect = "Program([FuncDecl(Id(foo),[],IntType,Block([IntLiteral(100),FloatLiteral(1220.0)]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,352))

    def test_func_decl46(self):
        input = """
        int foo() {
          "string";
        }
        """
        expect = "Program([FuncDecl(Id(foo),[],IntType,Block([StringLiteral(string)]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,353))

    def test_func_decl47(self):
        input = """
        int foo() {
          arr[3];
          arr(2)[3];
        }
        """
        expect = "Program([FuncDecl(Id(foo),[],IntType,Block([ArrayCell(Id(arr),IntLiteral(3)),ArrayCell(CallExpr(Id(arr),[IntLiteral(2)]),IntLiteral(3))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,354))

    def test_func_decl48(self):
        input = """
        int foo() {
          foo();
          foo(3);
          Caculate("",true);
          c==d=f=g;
        }
        """
        expect = "Program([FuncDecl(Id(foo),[],IntType,Block([CallExpr(Id(foo),[]),CallExpr(Id(foo),[IntLiteral(3)]),CallExpr(Id(Caculate),[StringLiteral(),BooleanLiteral(true)]),BinaryOp(=,BinaryOp(==,Id(c),Id(d)),BinaryOp(=,Id(f),Id(g)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,355))

    def test_func_decl49(self):
        input = """
        int foo() {
          if(a==1)
            foo(a);
          else a;
        }
        """
        expect = "Program([FuncDecl(Id(foo),[],IntType,Block([If(BinaryOp(==,Id(a),IntLiteral(1)),CallExpr(Id(foo),[Id(a)]),Id(a))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,356))

    def test_func_decl50(self):
        input = """
        int foo() {
          if(a==1)
          {
            if(a)
              c=10.45E-10;
            else
              for(i=0;i=1;i)
                1230;
          }
        }
        """
        expect = "Program([FuncDecl(Id(foo),[],IntType,Block([If(BinaryOp(==,Id(a),IntLiteral(1)),Block([If(Id(a),BinaryOp(=,Id(c),FloatLiteral(1.045e-09)),For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(=,Id(i),IntLiteral(1));Id(i);IntLiteral(1230)))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,357))

    def test_func_decl51(self):
        input = """
        int foo() {
          if(a==1)
          {
            if(a)
              c=10.45E-10;
            else
              return 1;
          }
        }
        """
        expect = "Program([FuncDecl(Id(foo),[],IntType,Block([If(BinaryOp(==,Id(a),IntLiteral(1)),Block([If(Id(a),BinaryOp(=,Id(c),FloatLiteral(1.045e-09)),Return(IntLiteral(1)))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,358))

    def test_func_decl52(self):
        input = """
        int foo() {
          for(1;true;3)
            a=a+1;
        }
        """
        expect = "Program([FuncDecl(Id(foo),[],IntType,Block([For(IntLiteral(1);BooleanLiteral(true);IntLiteral(3);BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,359))

    def test_func_decl53(self):
        input = """
        int foo() {
          for(a;b;c)
            break ;
        }
        """
        expect = "Program([FuncDecl(Id(foo),[],IntType,Block([For(Id(a);Id(b);Id(c);Break())]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,360))

    def test_func_decl54(self):
        input = """
          int a;
          int main () {
             int b;
             b = a+3;
          }
        """
        expect = "Program([VarDecl(a,IntType),FuncDecl(Id(main),[],IntType,Block([VarDecl(b,IntType),BinaryOp(=,Id(b),BinaryOp(+,Id(a),IntLiteral(3)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,361))

    def test_func_decl55(self):
        input = """
        int main() {
            !a[-3];
        }
        """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([UnaryOp(!,ArrayCell(Id(a),UnaryOp(-,IntLiteral(3))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,362))

    def test_func_decl56(self):
        input = """
        int main() {
            !a[b[m[7]]];
        }
        """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([UnaryOp(!,ArrayCell(Id(a),ArrayCell(Id(b),ArrayCell(Id(m),IntLiteral(7)))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,363))

    def test_func_decl57(self):
        input = """
        int main() {
            -a[12];
        }
        """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([UnaryOp(-,ArrayCell(Id(a),IntLiteral(12)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,364))

    def test_func_decl58(self):
        input = """
        int main() {
            -a[a[6]];
        }
        """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([UnaryOp(-,ArrayCell(Id(a),ArrayCell(Id(a),IntLiteral(6))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,365))

    def test_func_decl59(self):
        input = """
        int foo() {
            do
            {}{}{}
            while(1);
        }
        """
        expect = "Program([FuncDecl(Id(foo),[],IntType,Block([Dowhile([Block([]),Block([]),Block([])],IntLiteral(1))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,366))

    def test_func_decl60(self):
        input = """
        int foo() {
            do
            { 1; }{}{}
            while(1);
        }
        """
        expect = "Program([FuncDecl(Id(foo),[],IntType,Block([Dowhile([Block([IntLiteral(1)]),Block([]),Block([])],IntLiteral(1))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,367))

    def test_func_decl61(self):
        input = """
        int main(){
          int a;
          a = b && c + d;
        }
        """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(a,IntType),BinaryOp(=,Id(a),BinaryOp(&&,Id(b),BinaryOp(+,Id(c),Id(d))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,368))

    def test_func_decl62(self):
        input = """
        int main(){
          int a;
          a = b && c + d && f || e;
        }
        """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(a,IntType),BinaryOp(=,Id(a),BinaryOp(||,BinaryOp(&&,BinaryOp(&&,Id(b),BinaryOp(+,Id(c),Id(d))),Id(f)),Id(e)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,369))

    def test_func_decl63(self):
        input = """
        int main(){
          int a;
          a = 5<  (b <7);
        }
        """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(a,IntType),BinaryOp(=,Id(a),BinaryOp(<,IntLiteral(5),BinaryOp(<,Id(b),IntLiteral(7))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,370))

    def test_func_decl64(self):
        input = """
        string upper(string arr, int n) {
          for (i = 0; i < n; i=i+1) {
            if (arr[i] >= "0" && arr[i] <= "9") continue;
            if (arr[i] >= "a" && arr[i] <= "z") {
              arr[i] = "A" - ("a" - arr[i]);
            }
          }
          return arr;
        }
        """
        expect = "Program([FuncDecl(Id(upper),[VarDecl(arr,StringType),VarDecl(n,IntType)],StringType,Block([For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(<,Id(i),Id(n));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([If(BinaryOp(&&,BinaryOp(>=,ArrayCell(Id(arr),Id(i)),StringLiteral(0)),BinaryOp(<=,ArrayCell(Id(arr),Id(i)),StringLiteral(9))),Continue()),If(BinaryOp(&&,BinaryOp(>=,ArrayCell(Id(arr),Id(i)),StringLiteral(a)),BinaryOp(<=,ArrayCell(Id(arr),Id(i)),StringLiteral(z))),Block([BinaryOp(=,ArrayCell(Id(arr),Id(i)),BinaryOp(-,StringLiteral(A),BinaryOp(-,StringLiteral(a),ArrayCell(Id(arr),Id(i)))))]))])),Return(Id(arr))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,371))

    def test_func_decl65(self):
        input = """
            boolean isIsomorphic(string s, string t) {
            if (s_length() != t_length())
                    return false;

            dodai   = s_length();
            compare = "";
            for (i = 0; i < dodai; i=i+1) {
                    compare = " ";
            }
            return compare == t;
            }
        """
        expect = "Program([FuncDecl(Id(isIsomorphic),[VarDecl(s,StringType),VarDecl(t,StringType)],BoolType,Block([If(BinaryOp(!=,CallExpr(Id(s_length),[]),CallExpr(Id(t_length),[])),Return(BooleanLiteral(false))),BinaryOp(=,Id(dodai),CallExpr(Id(s_length),[])),BinaryOp(=,Id(compare),StringLiteral()),For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(<,Id(i),Id(dodai));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([BinaryOp(=,Id(compare),StringLiteral( ))])),Return(BinaryOp(==,Id(compare),Id(t)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,372))

    def test_func_decl66(self):
        input = """
        int main(){
            print(arr[i]) ;
        }
  
        """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([CallExpr(Id(print),[ArrayCell(Id(arr),Id(i))])]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,373))

    def test_func_decl67(self):
        input = """
        int main(){
            print((arr[i])[j]) ;
        }
  
        """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([CallExpr(Id(print),[ArrayCell(ArrayCell(Id(arr),Id(i)),Id(j))])]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,374))

    def test_func_decl68(self):
        input = """
        int main(){
            do { }
            while(arr[i]);
        }
  
        """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([Dowhile([Block([])],ArrayCell(Id(arr),Id(i)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,375))

    def test_func_decl69(self):
        input = """
        int fibonacci(int N){
          if (N == 0) return  0;
          else if (N == 1) return 1;
          else return fibonacci(N - 1) + fibonacci(N - 2);
        }
        """
        expect = "Program([FuncDecl(Id(fibonacci),[VarDecl(N,IntType)],IntType,Block([If(BinaryOp(==,Id(N),IntLiteral(0)),Return(IntLiteral(0)),If(BinaryOp(==,Id(N),IntLiteral(1)),Return(IntLiteral(1)),Return(BinaryOp(+,CallExpr(Id(fibonacci),[BinaryOp(-,Id(N),IntLiteral(1))]),CallExpr(Id(fibonacci),[BinaryOp(-,Id(N),IntLiteral(2))])))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,376))

    def test_func_decl70(self):
        input = """
        int minimum(int b[], int begin, int end){
          if (begin < end){
            if (b[begin] < b[begin + 1]) 
               small = b[begin];
            minimum(b, begin + 1, end);
          }
          return small;
        }
        """
        expect = "Program([FuncDecl(Id(minimum),[VarDecl(b,ArrayTypePointer(IntType)),VarDecl(begin,IntType),VarDecl(end,IntType)],IntType,Block([If(BinaryOp(<,Id(begin),Id(end)),Block([If(BinaryOp(<,ArrayCell(Id(b),Id(begin)),ArrayCell(Id(b),BinaryOp(+,Id(begin),IntLiteral(1)))),BinaryOp(=,Id(small),ArrayCell(Id(b),Id(begin)))),CallExpr(Id(minimum),[Id(b),BinaryOp(+,Id(begin),IntLiteral(1)),Id(end)])])),Return(Id(small))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,377))

    def test_func_decl71(self):
        input ="""
        int a[10];
        void printArray(int begin, int end){
          if(begin < end){ 
            cout(a[begin]);
            printArray(begin + 1, end);
          }
        }
        """
        expect = "Program([VarDecl(a,ArrayType(IntType,10)),FuncDecl(Id(printArray),[VarDecl(begin,IntType),VarDecl(end,IntType)],VoidType,Block([If(BinaryOp(<,Id(begin),Id(end)),Block([CallExpr(Id(cout),[ArrayCell(Id(a),Id(begin))]),CallExpr(Id(printArray),[BinaryOp(+,Id(begin),IntLiteral(1)),Id(end)])]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,378))

    def test_func_decl72(self):
        input = """
        void isPrime(int a, int b){
        for (i = a; counter=0; i <= b)
          for (j = 2; j <= sqrt(i); j)
            if (i%j == 0) counter=couter+1;
          if (counter == 0 && i!=1) cout(i);
        }
        """
        expect = "Program([FuncDecl(Id(isPrime),[VarDecl(a,IntType),VarDecl(b,IntType)],VoidType,Block([For(BinaryOp(=,Id(i),Id(a));BinaryOp(=,Id(counter),IntLiteral(0));BinaryOp(<=,Id(i),Id(b));For(BinaryOp(=,Id(j),IntLiteral(2));BinaryOp(<=,Id(j),CallExpr(Id(sqrt),[Id(i)]));Id(j);If(BinaryOp(==,BinaryOp(%,Id(i),Id(j)),IntLiteral(0)),BinaryOp(=,Id(counter),BinaryOp(+,Id(couter),IntLiteral(1)))))),If(BinaryOp(&&,BinaryOp(==,Id(counter),IntLiteral(0)),BinaryOp(!=,Id(i),IntLiteral(1))),CallExpr(Id(cout),[Id(i)]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,379))

    def test_func_decl73(self):
        input = """
        void foo(float a [] ){ }
        void goo(float x[]) { 
          float y[10]; 
          int z [10]; 
          foo(x); //CORRECT 
          foo(y); //CORRECT 
          }
        """
        expect = "Program([FuncDecl(Id(foo),[VarDecl(a,ArrayTypePointer(FloatType))],VoidType,Block([])),FuncDecl(Id(goo),[VarDecl(x,ArrayTypePointer(FloatType))],VoidType,Block([VarDecl(y,ArrayType(FloatType,10)),VarDecl(z,ArrayType(IntType,10)),CallExpr(Id(foo),[Id(x)]),CallExpr(Id(foo),[Id(y)])]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,380))

    def test_func_decl74(self):
        input = """
        boolean isLeapYear(int year){
          if (year < 0 )
            cout ("This is a invalid Year." ,endl);
          else
            if (year % 400 == 0 || (year % 4 == 0 && year % 100 != 0))
              return true;
            else
              return false;
            }
        """
        expect = "Program([FuncDecl(Id(isLeapYear),[VarDecl(year,IntType)],BoolType,Block([If(BinaryOp(<,Id(year),IntLiteral(0)),CallExpr(Id(cout),[StringLiteral(This is a invalid Year.),Id(endl)]),If(BinaryOp(||,BinaryOp(==,BinaryOp(%,Id(year),IntLiteral(400)),IntLiteral(0)),BinaryOp(&&,BinaryOp(==,BinaryOp(%,Id(year),IntLiteral(4)),IntLiteral(0)),BinaryOp(!=,BinaryOp(%,Id(year),IntLiteral(100)),IntLiteral(0)))),Return(BooleanLiteral(true)),Return(BooleanLiteral(false))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,381))

    def test_func_decl75(self):
        input = """
        void many_for(){
          for (i = 0; i < 2; i)
            for (j = 0; j < 2; j)
              for (k = 0; k < 2; k)
                (c[i])[j] = (a[i])[k]*(b[k])[j];
        }
        """
        expect = "Program([FuncDecl(Id(many_for),[],VoidType,Block([For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(<,Id(i),IntLiteral(2));Id(i);For(BinaryOp(=,Id(j),IntLiteral(0));BinaryOp(<,Id(j),IntLiteral(2));Id(j);For(BinaryOp(=,Id(k),IntLiteral(0));BinaryOp(<,Id(k),IntLiteral(2));Id(k);BinaryOp(=,ArrayCell(ArrayCell(Id(c),Id(i)),Id(j)),BinaryOp(*,ArrayCell(ArrayCell(Id(a),Id(i)),Id(k)),ArrayCell(ArrayCell(Id(b),Id(k)),Id(j)))))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,382))

    def test_func_decl76(self):
        input = """
        void printPrime(int arr[], int N)
        {
          if (N == 0) return;
          else if (isPrime(arr))
              cout(arr);
          printPrime(arr+1, N-1);  
        }
        """
        expect = "Program([FuncDecl(Id(printPrime),[VarDecl(arr,ArrayTypePointer(IntType)),VarDecl(N,IntType)],VoidType,Block([If(BinaryOp(==,Id(N),IntLiteral(0)),Return(),If(CallExpr(Id(isPrime),[Id(arr)]),CallExpr(Id(cout),[Id(arr)]))),CallExpr(Id(printPrime),[BinaryOp(+,Id(arr),IntLiteral(1)),BinaryOp(-,Id(N),IntLiteral(1))])]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,383))

    def test_program(self):
        input=""" 
        float a; string b[5];
        int[] foo(){
            a = "Dai" ;
        }
        """
        expect = "Program([VarDecl(a,FloatType),VarDecl(b,ArrayType(StringType,5)),FuncDecl(Id(foo),[],ArrayTypePointer(IntType),Block([BinaryOp(=,Id(a),StringLiteral(Dai))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,384))

    def test_func_decl78(self):
        input=""" 
        int main(int argv[]){
            a = foo(b,c);
            print(a);
        }"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(argv,ArrayTypePointer(IntType))],IntType,Block([BinaryOp(=,Id(a),CallExpr(Id(foo),[Id(b),Id(c)])),CallExpr(Id(print),[Id(a)])]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,385))

    def test_func_decl79(self):
        input=""" 
        float[] main(int a[], string b[]){
            return "Tan Dai";
        }"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(a,ArrayTypePointer(IntType)),VarDecl(b,ArrayTypePointer(StringType))],ArrayTypePointer(FloatType),Block([Return(StringLiteral(Tan Dai))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,386))

    def test_func_decl80(self):
        input=""" 
        float[] main(int a[], string b[]){
            return 1.2+2.3;
        }"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(a,ArrayTypePointer(IntType)),VarDecl(b,ArrayTypePointer(StringType))],ArrayTypePointer(FloatType),Block([Return(BinaryOp(+,FloatLiteral(1.2),FloatLiteral(2.3)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,387))

    def test_func_decl81(self):
        input=""" 
        int[] main(int a[], string b[]){
            return 1;
        }"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(a,ArrayTypePointer(IntType)),VarDecl(b,ArrayTypePointer(StringType))],ArrayTypePointer(IntType),Block([Return(IntLiteral(1))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,388))

    def test_func_decl82(self):
        input=""" 
        string[] main(int a[], string b[]){
            if(True) break;
            else if (false) continue;
            break;
        }"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(a,ArrayTypePointer(IntType)),VarDecl(b,ArrayTypePointer(StringType))],ArrayTypePointer(StringType),Block([If(Id(True),Break(),If(BooleanLiteral(false),Continue())),Break()]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,389))

    def test_func_decl83(self):
        input=""" 
        boolean[] main(int a[], string b[]){
            return true || false;
        }"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(a,ArrayTypePointer(IntType)),VarDecl(b,ArrayTypePointer(StringType))],ArrayTypePointer(BoolType),Block([Return(BinaryOp(||,BooleanLiteral(true),BooleanLiteral(false)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,390))

    def test_func_decl84(self):
        input=""" 
        float Caculate(int a) {return a*a;}"""
        expect = "Program([FuncDecl(Id(Caculate),[VarDecl(a,IntType)],FloatType,Block([Return(BinaryOp(*,Id(a),Id(a)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,391))

    def test_func_decl85(self):
        input=""" 
        void print(string name) {
            print(name);
        }
        """
        expect = "Program([FuncDecl(Id(print),[VarDecl(name,StringType)],VoidType,Block([CallExpr(Id(print),[Id(name)])]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,392))

    def test_func_decl86(self):
        input=""" 
        int a; float b[5];
        void set(int a,float b[]){
            a = a; b=b;
        }"""
        expect = "Program([VarDecl(a,IntType),VarDecl(b,ArrayType(FloatType,5)),FuncDecl(Id(set),[VarDecl(a,IntType),VarDecl(b,ArrayTypePointer(FloatType))],VoidType,Block([BinaryOp(=,Id(a),Id(a)),BinaryOp(=,Id(b),Id(b))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,393))

    def test_func_decl87(self):
        input=""" 
        int test(){
            do a = a*10; { {} } { } while ( true);
        }"""
        expect = "Program([FuncDecl(Id(test),[],IntType,Block([Dowhile([BinaryOp(=,Id(a),BinaryOp(*,Id(a),IntLiteral(10))),Block([Block([])]),Block([])],BooleanLiteral(true))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,394))

    def test_func_decl88(self):
        input=""" 
        void test_div(int a, int b){
            if(b!=0) return a/b;
            else return "b equal 0";
        }"""
        expect = "Program([FuncDecl(Id(test_div),[VarDecl(a,IntType),VarDecl(b,IntType)],VoidType,Block([If(BinaryOp(!=,Id(b),IntLiteral(0)),Return(BinaryOp(/,Id(a),Id(b))),Return(StringLiteral(b equal 0)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,395))

    def test_func_decl89(self):
        input=""" 
        int main(){
            int a; a=1;
            a -b;
            a>=b;
            a % b;
        }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(a,IntType),BinaryOp(=,Id(a),IntLiteral(1)),BinaryOp(-,Id(a),Id(b)),BinaryOp(>=,Id(a),Id(b)),BinaryOp(%,Id(a),Id(b))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,396))

    def test_simple_program(self):
        input = """int main() {}"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,397))

    def test_more_complex_program(self):
  
        input = """int main () {
            putIntLn(4);
        }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([CallExpr(Id(putIntLn),[IntLiteral(4)])]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,398))
    
    def test_call_without_parameter(self):
    
        input = """int main () {
            getIntLn();
        }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([CallExpr(Id(getIntLn),[])]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,399))

    def test_call_without_parameter1(self):

        input ="""
        void print_finish(){
            print("haha done :v");
        }
        """
        expect = "Program([FuncDecl(Id(print_finish),[],VoidType,Block([CallExpr(Id(print),[StringLiteral(haha done :v)])]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,400))
   