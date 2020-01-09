import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):
    def test1_UndeclaredIdentifier(self):
        """Undeclared Identifier: exp"""
        input = """
        int a;
        float b;
        string c;
        int d[10];
        void main(){
            {
                if(exp)
                    return;
            }
            return;
        }
        """
        expect = "Undeclared Identifier: exp"
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test2_UndeclaredIdentifier(self):
        """Undeclared Identifier: somethingjustlikethis"""
        input = """
        void main()
        {
            {
                int a,b;
                boolean c,d;
                a = 10 ;
                b = 5;
                c = true;
                d = c == (a>b);
            }
            {
                somethingjustlikethis = a+b; 
            }
            return;
        }
        """
        expect = "Undeclared Identifier: somethingjustlikethis"
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test3_UndeclaredIdentifier(self):
        """Undeclared Identifier: i"""
        input = """
        int[] foo()
        {
            int a[5];
            return a;
        }
        void main()
        {
            do
                foo();
            while i;
            return;
        }
        """
        expect = "Undeclared Identifier: i"
        self.assertTrue(TestChecker.test(input,expect,403))

    def test4_UndeclaredFunction(self):
        """Undeclared Function: foo2"""
        input = """
        int foo(int a, int b){ return a+b;}
        int main(){
                return a+b+foo2();
            }
        int a,b;
        """
        expect = "Undeclared Function: foo2"
        self.assertTrue(TestChecker.test(input,expect,404))

    def test5_UndeclaredFunction(self):
        """Undeclared Function: multi"""
        input = """
        void main(){
            string str;
            str = "Chery Chery Lady\\n";
            int a;
            a = multi(10);
            return;
        }
        """
        expect = "Undeclared Function: multi"
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test6_UndeclaredFunction(self):
        """Undeclared Function: foo1"""
        input = """
        int foo()
            {
                return 1;
            }
        int main()
        {
            int a;
            a=foo();
            return foo1();
        }
        """
        expect = "Undeclared Function: foo1"
        self.assertTrue(TestChecker.test(input, expect, 406))

    def test7_UndeclaredFunction(self):
        """Undeclared Function: convertBoolean"""
        input = """
        void main(){
            int a;
            {a =1;}
            if(convertBoolean(a))
                return;
            else                
                return;
        }
        """
        expect = "Undeclared Function: convertBoolean"
        self.assertTrue(TestChecker.test(input, expect, 407))

    def test8_UndeclaredFunction(self):
        """Undeclared Function: foo2"""
        input = """
        int foo(int a){
            if((a%2)==0)
                a=a+1;
            else
                do 
                    a=a-1;
                while a > 0;
            return a;
        }
        void main(){
            int a,b[10],i;
            a=10;
            for(i=0;i<10;i=i+1)
                b[i]=foo(a)+foo2(a);                
            return;
        }
        """
        expect = "Undeclared Function: foo2"
        self.assertTrue(TestChecker.test(input,expect,408))

    #---Test Type Mismatch In Statement

    def test9_TypeMismatchInStatement(self):
        """Type Mismatch In Statement: If"""
        input = """
        void main(){
            int a;
            {a =1;}
            if(a)
                return;
            else                
                return;
        }
        """
        expect = "Type Mismatch In Statement: If(Id(a),Return(),Return())"
        self.assertTrue(TestChecker.test(input, expect, 409))

    def test10_TypeMismatchInStatement(self):
        """Type Mismatch In Statement: If"""
        input = """
        int foo(int a){
            if((a%2)+1.0)
                a=a+1;
            else
                return a+1;
            return a;
        }
        void main(){              
            return;
        }
        """
        expect = "Type Mismatch In Statement: If(BinaryOp(+,BinaryOp(%,Id(a),IntLiteral(2)),FloatLiteral(1.0)),BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1))),Return(BinaryOp(+,Id(a),IntLiteral(1))))"
        self.assertTrue(TestChecker.test(input, expect, 410))

    def test11_TypeMismatchInStatement(self):
        """Type Mismatch In Statement: If"""
        input = """
        void main(){
            int a;
            float b[10];
            foo(a,b);              
            return;
        }
        int[] foo(int a,float b[]) {
            int c[3];
            if(a*2) foo(a-1,b);
            else return c;
        }
        """
        expect = "Type Mismatch In Statement: If(BinaryOp(*,Id(a),IntLiteral(2)),CallExpr(Id(foo),[BinaryOp(-,Id(a),IntLiteral(1)),Id(b)]),Return(Id(c)))"
        self.assertTrue(TestChecker.test(input, expect, 411))

    def test12_TypeMismatchInStatement(self):
        """Type Mismatch In Statement: For"""
        input = """
        void main(){
            float i, temp;
            for(i=1.0;i<10;i=i+1)
                {
                    if(temp<10)
                        temp=temp+1;
                }
            return;
        }
        """
        expect = "Type Mismatch In Statement: For(BinaryOp(=,Id(i),FloatLiteral(1.0));BinaryOp(<,Id(i),IntLiteral(10));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([If(BinaryOp(<,Id(temp),IntLiteral(10)),BinaryOp(=,Id(temp),BinaryOp(+,Id(temp),IntLiteral(1))))]))"
        self.assertTrue(TestChecker.test(input, expect, 412))

    def test13_TypeMismatchInStatement(self):
        """Type Mismatch In Statement: For"""
        input = """
        void main(){
            int i, temp;
            for(i=1;i=i+1;i=i+1)
                {
                    if(temp<10)
                        temp=temp+1;
                }
            return;
        }
        """
        expect = "Type Mismatch In Statement: For(BinaryOp(=,Id(i),IntLiteral(1));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([If(BinaryOp(<,Id(temp),IntLiteral(10)),BinaryOp(=,Id(temp),BinaryOp(+,Id(temp),IntLiteral(1))))]))"
        self.assertTrue(TestChecker.test(input,expect,413))

    def test14_TypeMismatchInStatement(self):
        """Type Mismatch In Statement: For"""
        input = """
        void main(){
            int i, temp;
            for(i=1;i<10;1.1e-1)
                {
                    if(temp<10)
                        temp=temp+1;
                    i=i+1;
                }
            return;
        }
        """
        expect = "Type Mismatch In Statement: For(BinaryOp(=,Id(i),IntLiteral(1));BinaryOp(<,Id(i),IntLiteral(10));FloatLiteral(0.11);Block([If(BinaryOp(<,Id(temp),IntLiteral(10)),BinaryOp(=,Id(temp),BinaryOp(+,Id(temp),IntLiteral(1)))),BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)))]))"
        self.assertTrue(TestChecker.test(input,expect,414))

    def test15_entry_width_Ovar(self):
        """Test no entry with vardecl"""
        input = """
        int main, entry[10];
        int mai1n(int argv, string argc){
            return 0;
        }
        string str, s;
        float tfloat;
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,415))

    def test16_entry_with_OFunc(self):
        """Test noentry with funcdecl"""
        input = """
        string foo2(){return "07111999";}
        int mai1n(int argv, string argc){
            return 0;
        }
        float foo(){return 07111999;}
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,416))

    def test17_entry_with_FaV(self):
        """test no entry with small vardecl-funcdecl"""
        input = """
        int main, entry[10];
        string foo2(){return "07111999";}
        int mai1n(int argv, string argc){
            return 0;
        }
        string str, s;
        float tfloat;
        float foo(){return 07111999;}
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,417))

    def test18_entry_with_more_type1(self):
        """test no entry with vardecl-funcdecl"""
        input = """
        int main, entry[10];
        string foo2(){return "07111999";}
        int mai1n(int argv, string argc){
            return 0;
        }
        string str, s;float tfloat;float foo(){return 14541999;}
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,418))

    def test19_entry_with_more_type2(self):
        """test no entry with vardecl-funcdecl"""
        input = """
        int main, entry[10];
        string foo2(){return "07111999";}
        int mai1n(int argv, string argc){
            return 0;
        }
        string str, s; float tfloat;float foo(){return 07111999;}
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,419))


    def test20_global_vWF_rede(self):
        """test Redeclared function main"""
        input = """
        int main1, entry[10];
        float tfloat;
        float main;
        string foo2(){return "07111999";}
        int main(int argv, string argc){
            return 0;
        }
        """
        expect = "Redeclared Function: main"
        self.assertTrue(TestChecker.test(input,expect,420))



    def test21_left_value_failed2(self):
        """test left value content id"""
        input = """
        float tfloat;
        float foo2(){
            float tfloat;
            boolean boo;
            return 1.e-3;
        }
        int main(int argc, string args, boolean argv, float flo){
            foo2();
            int c,b;
            b + c = 1;
            return 0;
        }
        """
        expect = "Not Left Value: BinaryOp(+,Id(b),Id(c))"
        self.assertTrue(TestChecker.test(input,expect,421))

    def test22_left_value_failed3(self):
        """test left value content type failed"""
        input = """
        float tfloat;
        float foo2(){
            float tfloat;
            boolean boo;
            return 1.e-3;
        }
        int main(int argc, string args, boolean argv, float flo){
            foo2();
            main() = 0;
            return 0;
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(main),[])"
        self.assertTrue(TestChecker.test(input,expect,422))

    def test23_left_value_failed4(self):
        """test left value content expression simple"""
        input = """
        float tfloat[4];
        float foo2(){
            float tfloat;
            boolean boo;
            return 1.e-3;
        }
        int main(int argc, string args, boolean argv, float flo){
            argc + tfloat[1] = 10.0;
            //foo2() = 0;
            return 0;
        }
        """
        expect = "Not Left Value: BinaryOp(+,Id(argc),ArrayCell(Id(tfloat),IntLiteral(1)))"
        self.assertTrue(TestChecker.test(input,expect,423))

    def test24_left_value_failed5(self):
        """test left value content expression with call """
        input = """
        float tfloat[4];
        float foo2(){
            float tfloat;
            boolean boo;
            return 1.e-3;
        }
        int main(int argc, string args, boolean argv, float flo){
            //argc + tfloat[1] = 10.0;
            int some;
            foo2() + some = 0;
            return 0;
        }
        """
        expect = "Not Left Value: BinaryOp(+,CallExpr(Id(foo2),[]),Id(some))"
        self.assertTrue(TestChecker.test(input,expect,424))

    def test25_stmt_miss_mat1ch(self):
        """test left value statement return"""
        input = """
        float tfloat[4];
        float foo2(){
            float tfloat;
            boolean boo;
            return true;
        }
        int main(int argc, string args, boolean argv, float flo){
            //argc + tfloat[1] = 10.0;
            foo2();
            return 0;
        }
        """
        expect = "Type Mismatch In Statement: Return(BooleanLiteral(true))"
        self.assertTrue(TestChecker.test(input,expect,425))

    def test26_stmt_m2iss_mat1ch(self):
        """test left value exp string type"""
        input = """
        float tfloat[4];
        float foo2(){
            float tfloat;
            boolean boo;
            return 1.0;
        }
        int main(int argc, string args, boolean argv, float flo){
            //argc + tfloat[1] = 10.0;
            foo2();
            0 = 0;
            return 0;
        }
        """
        expect = "Not Left Value: IntLiteral(0)"
        self.assertTrue(TestChecker.test(input,expect,426))

    def test27_stmt_miss2_mat1ch(self):
        """test left value exp booleantype"""
        input = """
        float tfloat[4];
        float foo2(){
            float tfloat;
            boolean boo;
            return 1.0;
        }
        int main(int argc, string args, boolean argv, float flo){
            //argc + tfloat[1] = 10.0;
            foo2();
            1 = 0;
            return 0;
        }
        """
        expect = "Not Left Value: IntLiteral(1)"
        self.assertTrue(TestChecker.test(input,expect,427))

    def test28_stmt_miss3_mat1ch(self):
        """test left value expression corresponding bool->int"""
        input = """
        float tfloat[4];
        float foo2(){
            float tfloat;
            boolean boo;
            return 1.0;
        }
        int main(int argc, string args, boolean argv, float flo){
            //argc + tfloat[1] = 10.0;
            foo2();
            argc = true;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(argc),BooleanLiteral(true))"
        self.assertTrue(TestChecker.test(input,expect,428))

    def test29_stmt_miss4_mat1ch(self):
        """test left value expression corresponding float->int"""
        input = """
        float tfloat[4];
        float foo2(){
            float tfloat;
            boolean boo;
            return 1.0;
        }
        int main(int argc, string args, boolean argv, float flo){
            //argc + tfloat[1] = 10.0;
            foo2();
            argc = flo;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(argc),Id(flo))"
        self.assertTrue(TestChecker.test(input,expect,429))

    def test30_stmt_miss5_mat1ch(self):
        """test left value expression corresponding (expression float)->int"""
        input = """
        float tfloat[4];
        float foo2(){
            float tfloat;
            boolean boo;
            return 1.0;
        }
        int main(int argc, string args, boolean argv, float flo){
            //argc + tfloat[1] = 10.0;
            foo2();
            int x;
            x = 1 + 2 + 3 + 4 + 5 + 6 -1.3;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(x),BinaryOp(-,BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(+,IntLiteral(1),IntLiteral(2)),IntLiteral(3)),IntLiteral(4)),IntLiteral(5)),IntLiteral(6)),FloatLiteral(1.3)))"
        self.assertTrue(TestChecker.test(input,expect,430))

    def test31_stmt_miss6_mat1ch(self):
        """test left value Statement corresponding return float[]->int[]"""
        input = """
        float tfloat[4];
        float foo2(){
            float tfloat;
            boolean boo;
            return 1.0;
        }
        int[] main(int argc, string args, boolean argv, float flo){
            //argc + tfloat[1] = 10.0;
            foo2();
            return tfloat;
        }
        """
        expect = "Type Mismatch In Statement: Return(Id(tfloat))"
        self.assertTrue(TestChecker.test(input,expect,431))

    def test32_stmt_miss7_mat1ch(self):
        """test left value Statement corresponding return int[]->float[]"""
        input = """
        float tfloat[4];
        float foo2(){
            float tfloat;
            boolean boo;
            return 1.0;
        }
        float[] main(int argc[], string args, boolean argv, float flo){
            //argc + tfloat[1] = 10.0;
            foo2();
            int a[5];
            return a;
        }
        """
        expect = "Type Mismatch In Statement: Return(Id(a))"
        self.assertTrue(TestChecker.test(input,expect,432))

    def test33_stmt_miss8_mat1ch(self):
        """test left value Statement corresponding float->float[]"""
        input = """
        float tfloat[4];
        float foo2(){
            float tfloat;
            boolean boo;
            return 1.0;
        }
        float[] main(int argc[], string args, boolean argv, float flo){
            //argc + tfloat[1] = 10.0;
            foo2();
            int a[5];
            return 1.1/1.0-10;
        }
        """
        expect = "Type Mismatch In Statement: Return(BinaryOp(-,BinaryOp(/,FloatLiteral(1.1),FloatLiteral(1.0)),IntLiteral(10)))"
        self.assertTrue(TestChecker.test(input,expect,433))

    def test34_stmt_miss9_mat1ch(self):
        """test left value Statement corresponding for condition"""
        input = """
        float tfloat[4];
        float foo2(){
            float tfloat;
            boolean boo;
            return 1.0;
        }
        float[] main(int argc[], string args, boolean argv, float flo){
            //argc + tfloat[1] = 10.0;
            foo2();
            for(1;1;1)
                argc[1] = -10;
        }
        """
        expect = "Type Mismatch In Statement: For(IntLiteral(1);IntLiteral(1);IntLiteral(1);BinaryOp(=,ArrayCell(Id(argc),IntLiteral(1)),UnaryOp(-,IntLiteral(10))))"
        self.assertTrue(TestChecker.test(input,expect,434))

    def test35_stmt_miss10_mat1ch(self):
        """test left value Statement corresponding for condition"""
        input = """
        float tfloat[4];
        float foo2(){
            float tfloat;
            boolean boo;
            return 1.0;
        }
        float[] main(int argc[], string args, boolean argv, float flo){
            //argc + tfloat[1] = 10.0;
            foo2();
            for(10;false;true){
                argc[1] = 0;
                }
        }
        """
        expect = "Type Mismatch In Statement: For(IntLiteral(10);BooleanLiteral(false);BooleanLiteral(true);Block([BinaryOp(=,ArrayCell(Id(argc),IntLiteral(1)),IntLiteral(0))]))"
        self.assertTrue(TestChecker.test(input,expect,435))

    def test36_stmt_miss11_mat1ch(self):
        """test left value exp corresponding string->array[int]"""
        input = """
        float tfloat[4];
        float foo2(){
            float tfloat;
            boolean boo;
            return 1.0;
        }
        float[] main(int argc[], string args, boolean argv, float flo){
            //argc + tfloat[1] = 10.0;
            foo2();
            return tfloat;
            do{
                int f;
            }
            while(argc[1] <= "10.1");
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(<=,ArrayCell(Id(argc),IntLiteral(1)),StringLiteral(10.1))"
        self.assertTrue(TestChecker.test(input,expect,436))

    def test37_exp_miss12_mat1ch(self):
        """test left value exp corresponding int->array[int]"""
        input = """
        float tfloat[4];
        float[] main(int argc[], string args, boolean argv, float flo){
            //argc + tfloat[1] = 10.0;
            return tfloat;
            do{
                int f;
            }
            while(argc[1] == 10.1);
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(==,ArrayCell(Id(argc),IntLiteral(1)),FloatLiteral(10.1))"
        self.assertTrue(TestChecker.test(input,expect,437))

    def test38_stmt_miss13_mat1ch(self):
        """test left value exp corresponding string->array[float]"""
        input = """
        float tfloat[4];
        float[] main(int argc[], string args, boolean argv, float flo){
            //argc + tfloat[1] = 10.0;
            do{
                int f;
            }
            while(argv = true);
            return args;
        }
        """
        expect = "Type Mismatch In Statement: Return(Id(args))"
        self.assertTrue(TestChecker.test(input,expect,438))

    def test39_exp_miss14_mat1ch(self):
        """test left value exp corresponding boolean->array[int]"""
        input = """
        float tfloat[4];
        float[] main(int argc[], string args, boolean argv, float flo){
            //argc + tfloat[1] = 10.0;
            do{
                int f;
            }
            while(argc[1] = true);
            return args;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,ArrayCell(Id(argc),IntLiteral(1)),BooleanLiteral(true))"
        self.assertTrue(TestChecker.test(input,expect,439))

    def test40_exp_miss15_mat1ch(self):
        """test left value exp corresponding % with float"""
        input = """
        float tfloat[4];
        void foo(){}
        float[] main(int argc[], string args, boolean argv, float flo){
            //argc + tfloat[1] = 10.0;
            flo = argc[1] = argc[2] = argc[3];
            foo();
            do{
                int f;
            }
            while(argc[0]%10.1);
            
            return tfloat;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(%,ArrayCell(Id(argc),IntLiteral(0)),FloatLiteral(10.1))"
        self.assertTrue(TestChecker.test(input,expect,440))

    def test41_stmy_miss0_mat1ch(self):
        """test left value exp corresponding if type"""
        input = """
        float tfloat[4];
        void foo(){}
        float[] main(int argc[], string args,
         boolean argv, float flo){
            //argc + tfloat[1] = 10.0;
            return tfloat;
            if(1 == 2){
                if (true == false){
                    return tfloat;
                }

            }
            else {
                if (argc[1] + 10)
                {
                    return tfloat;
                }
            }
            foo();
        }
        """
        expect = "Type Mismatch In Statement: If(BinaryOp(+,ArrayCell(Id(argc),IntLiteral(1)),IntLiteral(10)),Block([Return(Id(tfloat))]))"
        self.assertTrue(TestChecker.test(input,expect,441))

    def test42_stmt_miss0_mat1ch(self):
        """test left value exp corresponding return string->float[]"""
        input = """
        float tfloat[4];
        void foo(){}
        float[] main(int argc[],
         string args, boolean argv, float flo){
            //argc + tfloat[1] = 10.0;
            if(1 == 2){
                if (true == false){
                    return tfloat;
                }
            }
            else {
                if (true)
                {
                    return tfloat;
                }
            }
            foo();
            return args;
        }
        """
        expect = "Type Mismatch In Statement: Return(Id(args))"
        self.assertTrue(TestChecker.test(input,expect,442))

    def test43_exp_mismatch(self):
        """test left value exp corresponding ! with not booleantype"""
        input = """
        float tfloat[4];
        void foo(){}
        float[] main(int argc[], 
        string args, boolean argv, float flo){
            int a;
            a = !true + !false + !1;
            foo();
            return tfloat;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(+,UnaryOp(!,BooleanLiteral(true)),UnaryOp(!,BooleanLiteral(false)))"
        self.assertTrue(TestChecker.test(input,expect,443))

    def test44_exp_mismatch1(self):
        """test left value exp corresponding - with not int & float"""
        input = """
        float tfloat[4];
        void foo(){}
        float[] main(int 
        argc[], string args, boolean argv, float flo){
            int a;
            a = 1 -- 10 --20 -- 30.0 - -true;
            foo();
            return tfloat;
        }
        """
        expect = "Type Mismatch In Expression: UnaryOp(-,BooleanLiteral(true))"
        self.assertTrue(TestChecker.test(input,expect,444))

    def test45_exp_mismatch2(self):
        """test left value exp corresponding string->array[float]"""
        input = """
        float tfloat[4];
        void foo(){}
        float[] main(int argc[], string args, boolean argv, float flo){
            int a;
            a = argc[0] + --10 --20 -- 30.0;
            foo();
            return tfloat;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),BinaryOp(-,BinaryOp(-,BinaryOp(+,ArrayCell(Id(argc),IntLiteral(0)),UnaryOp(-,UnaryOp(-,IntLiteral(10)))),UnaryOp(-,IntLiteral(20))),UnaryOp(-,FloatLiteral(30.0))))"
        self.assertTrue(TestChecker.test(input,expect,445))

    def test46_exp_mismatch3(self):
        """test left value exp corresponding expwith string & int"""
        input = """
        float tfloat[4];
        void foo(){}
        float[] main(int argc[], string args, boolean argv, 
        float flo){
            int a;
            a = args + -- 10 --20 -- 30.0;
            foo();
            return tfloat;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(+,Id(args),UnaryOp(-,UnaryOp(-,IntLiteral(10))))"
        self.assertTrue(TestChecker.test(input,expect,446))

    def test47_exp_mis_somematch4(self):
        """test left value exp corresponding string->float"""
        input = """
        float tfloat[4];
        void foo(){}
        float[] main(int argc[], 
        string args, boolean argv, float flo){
            int a;
            flo = 1.1;
            flo = 1.0;
            flo = "LongDepTrai";
            foo();
            return tfloat;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(flo),StringLiteral(LongDepTrai))"
        self.assertTrue(TestChecker.test(input,expect,447))

    def test48_exp_mis_somematch5(self):
        """test left value exp corresponding - with booleantype"""
        input = """
        float tfloat[4];
        void foo(){}
        float[] main(int argc[], 
        string args, boolean argv, float flo){
            int a;
            flo = 1.1;
            flo = 1.0;
            flo = 1+2-3*4/5%-argv;
            foo();
            return tfloat;
        }
        """
        expect = "Type Mismatch In Expression: UnaryOp(-,Id(argv))"
        self.assertTrue(TestChecker.test(input,expect,448))

    def test49_exp_mismatc_someh6(self):
        """test left value exp corresponding - with boolean"""
        input = """
        float tfloat[4];
        void foo(){}
        float[] main(int argc[], string args, 
        boolean argv, float flo){
            int a;
            flo = 1.1;
            flo = 1.0;
            flo = 1+2-3*4/5%-!argv;
            foo();
            return args;
        }
        """
        expect = "Type Mismatch In Expression: UnaryOp(-,UnaryOp(!,Id(argv)))"
        self.assertTrue(TestChecker.test(input,expect,449))

    def test50_exp_mismat_somech7(self):
        """test left value exp corresponding string + string"""
        input = """
        float tfloat[4];
        void foo(){}
        float[] main(int argc[], string args, boolean argv, float flo){
            int a;
            flo = 1.1;
            flo = 1.0;
            args = "Long" + 
            "Is" +"Very"+"HandSome";
            foo();
            return args;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(+,StringLiteral(Long),StringLiteral(Is))"
        self.assertTrue(TestChecker.test(input,expect,450))

    def test51_exp_mismat8ch_some(self):
        """test left value exp corresponding boolean => int"""
        input = """
        float tfloat[4];
        void foo(){}
        float[] main(int 
        argc[], string args, boolean argv, float flo){
            int a;
            flo = 1.1;
            flo = 1.0;
            argv = true;
            argv = !(true&&false||true>=10);
            foo();
            return argv;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(>=,BooleanLiteral(true),IntLiteral(10))"
        self.assertTrue(TestChecker.test(input,expect,451))

    def test52_exp_9mismatch_some(self):
        """test left value exp corresponding boolean || int"""
        input = """
        float tfloat[4];
        void foo(){}
        float[] main(int argc[], string args, boolean argv, float flo){
            int a;
            flo = 1.1;
            flo = 1.0;
            argv = 1 < 2 -!(true||1.0);
            foo();
            return argv;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(||,BooleanLiteral(true),FloatLiteral(1.0))"
        self.assertTrue(TestChecker.test(input,expect,452))

    def test53_exp10_mismatch_some(self):
        """test left value exp corresponding operator - with boolean"""
        input = """
        float tfloat[4];
        void foo(){}
        float[] main(int argc[], string args, boolean argv, float flo){
            int a;
            flo = 1.1;
            flo = 1.0;
            argv = 1 < 2 -!(true||((((((((((!false))))))))))&&1);
            foo();
            return argv;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(&&,UnaryOp(!,BooleanLiteral(false)),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,453))

    def test54_exp11_mismatch_some(self):
        """test left value exp corresponding arrayPointer => array"""
        input = """
        float tfloat[4];
        //float[] foo(){return tfloat;}
        float[] foo2(){return tfloat;}
        float[] main(int argc[], string args, boolean argv, float flo){
            float f[10];
            f = foo2();
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(f),CallExpr(Id(foo2),[]))"
        self.assertTrue(TestChecker.test(input,expect,454))

    def test55_exp_mis12match_some(self):
        """test left value exp corresponding string + string -> string"""
        input = """
        float tfloat[4];
        //float[] foo(){return tfloat;}
        //float[] foo2(){return tfloat;}
        float[] main(int argc[], string args, boolean argv, float flo){
            float f[10];
            args = "123"+"234";
            return tfloat;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(+,StringLiteral(123),StringLiteral(234))"
        self.assertTrue(TestChecker.test(input,expect,455))

    def test56_exp_mis13match_some(self):
        """test left value is intType"""
        input = """
        float tfloat[4];
        //float[] foo(){return tfloat;}
        float[] foo2(

        ){
            return tfloat;
            }
        int foo(){
            return 1;
        }
        float[] main(int argc[], string args, boolean argv, float flo){
            float f[10];
            foo2()[2] = 123456;
            foo() = 1;
            return tfloat;
        }
        """
        expect = "Not Left Value: CallExpr(Id(foo),[])"
        self.assertTrue(TestChecker.test(input,expect,456))

    def test57_exp_mis14match_some(self):
        """test left value is void type"""
        input = """
        float tfloat[4];
        void test(){}
        float[] main(int argc[], string args, boolean argv, float flo){
            float f[10];
            test() = 123321;
            return tfloat;
        }
        """

        expect = "Type Mismatch In Expression: BinaryOp(=,CallExpr(Id(test),[]),IntLiteral(123321))"
        self.assertTrue(TestChecker.test(input,expect,457))

    def test58_exp_mismatch15_some(self):
        """test continue outside"""
        input = """
        float tfloat[4];
        float[] Function(float a[], float b[]){return tfloat;}

        float[] main(int argc[], string args, boolean argv, float flo){

            Function(tfloat, Function(tfloat, tfloat));
            
            continue;
            return tfloat;
        }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,458))

    def test59_exp_mismatch16_some(self):
        """test index is float"""
        input = """
        float tfloat[4];
        void test(){}
        //float[] foo2(){return tfloat;}
        float[] main(int argc[], 
        string args,
         boolean argv, float flo){
            float f[10];
            f[argc[1]*10/3+1.1];
            return tfloat;
        }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(f),BinaryOp(+,BinaryOp(/,BinaryOp(*,ArrayCell(Id(argc),IntLiteral(1)),IntLiteral(10)),IntLiteral(3)),FloatLiteral(1.1)))"
        self.assertTrue(TestChecker.test(input,expect,459))

    def test60_exp_mismatch17_some(self):
        """test index is booleantype"""
        input = """
        float tfloat[4];
        void test(){}
        //float[] foo2(){return tfloat;}
        float[] main(int argc[], string args, boolean argv, float flo){
            float f[10];
            f[!!!!!true];
            return tfloat;
        }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(f),UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,BooleanLiteral(true)))))))"
        self.assertTrue(TestChecker.test(input,expect,460))
    def test61_UnreachableFunction(self):
        """Unreachable Function: foo"""
        input = """
        int foo(int a){
            if (a>0)
                return foo(a-1);
            else
                return 0;
        }
        void main()
        {
            return;
        }
        """
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 461))

    def test62_UnreachableFunction(self):
        """no error"""
        input = """
        int foo1()
        {
            foo2();
            return 1;
        }
        int foo2()
        {
            foo1();
            return 1;
        }
        void main(){}
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 462))

    def test63_UnreachableFunction(self):
        """no error"""
        input = """
        void foo1()
        {
            foo2();
        }
        void foo2()
        {
            foo3();
        }
        void foo3()
        {
            foo1();
        }
        void main(){}
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 463))

    def test64_UnreachableFunction(self):
        """Unreachable Function: foo1"""
        input = """
        void foo1()
        {
            foo2();
            foo3();
        }
        void foo2(){}
        void foo3(){}
        void main(){}
        """
        expect = "Unreachable Function: foo1"
        self.assertTrue(TestChecker.test(input, expect, 464))

    #---Test Not Left Value

    def test65_NotLeftValue(self):
        """Not Left Value"""
        input = """
        void main(){
            1+1=2; 
        }
        """
        expect = "Not Left Value: BinaryOp(+,IntLiteral(1),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,465))

    def test66_NotLeftValue(self):
        """Not Left Value"""
        input = """
        int foo(){ 
            return 0; 
        }
        void main(){
            foo()=1;
        }
        """
        expect = "Not Left Value: CallExpr(Id(foo),[])"
        self.assertTrue(TestChecker.test(input, expect, 466))

    def test67_NotLeftValue(self):
        """Not Left Value"""
        input = """
        int x;
        void main(){
            x+1=2;
        }
        """
        expect = "Not Left Value: BinaryOp(+,Id(x),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input, expect, 467))

    def test68_NotLeftValue(self):
        """Not Left Value"""
        input = """
        void main(){
            float arr[10];
            arr[0]+arr[1]=arr[2]+3;
        }
        """
        expect = "Not Left Value: BinaryOp(+,ArrayCell(Id(arr),IntLiteral(0)),ArrayCell(Id(arr),IntLiteral(1)))"
        self.assertTrue(TestChecker.test(input, expect, 468))

    def test69_NotLeftValue(self):
        """Not Left Value"""
        input = """
        int foo(int a){
            return a;
        }
        void main(){
            a+foo(a)=foo(a)+a;
        }
        int a;
        """
        expect = "Not Left Value: BinaryOp(+,Id(a),CallExpr(Id(foo),[Id(a)]))"
        self.assertTrue(TestChecker.test(input,expect,469))

    #---Test More Complex Program

    def test70_True(self):
        """no error"""
        input = """
        int i;
        int f(){
            return 200;
        }
        void main(){
            int test;
            test=f();
            putIntLn(test);
            {
                int i, test, f;
                test=f=i=100;
                putIntLn(i);
                putIntLn(test);
                putIntLn(f);
            }
            putIntLn(test);
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 470))

    def test71_exp_mismatch18_some(self):
        """test index is stringtype"""
        input = """
        float tfloat[4];
        void test(){}
        //float[] foo(){return tfloat;}
        //float[] foo2(){return tfloat;}
        float[] main(int argc[], string args, boolean argv, float flo){
            float f[10];
            f["LongLML"];
            return tfloat;
        }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(f),StringLiteral(LongLML))"
        self.assertTrue(TestChecker.test(input,expect,471))

    def test72_exp_mismatch19_some(self):
        """test mismatch expression call different length param"""
        input = """
        float tfloat[4];
        void test(){}
        float[] foo(){return tfloat;}
        float[] foo2(){return tfloat;}
        float[] main(int argc[], string args, boolean argv, float flo){
            float f[10];
            foo2(foo(3));
            return tfloat;
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[IntLiteral(3)])"
        self.assertTrue(TestChecker.test(input,expect,472))

    def test73_exp_mismatch20_some(self):
        """test mismatch expression call different length param"""
        input = """
        float tfloat[4];
        void test(){}
        float[] foo(){return tfloat;}
        float[] foo2(){return tfloat;}
        float[] main(int argc[], string args, boolean argv, float flo){
            float f[10];
            foo2(foo(),1,2,3);
            return tfloat;
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo2),[CallExpr(Id(foo),[]),IntLiteral(1),IntLiteral(2),IntLiteral(3)])"
        self.assertTrue(TestChecker.test(input,expect,473))

    def test74_deep_block_decl(self):
        """test redeclared with scope 1st"""
        input = """
        int i;
        float f;
        string str;
        boolean boo;
        void main(int argc[], string args, boolean argv, float flo){
            string str,str2;
            {
                string str2;
                {
                    boolean str2;
                    {
                        float str2;
                    }
                }
            }
            int str;
        }
        """
        expect = "Redeclared Variable: str"
        self.assertTrue(TestChecker.test(input,expect,474))

    def test75_deep_block_return(self):
        """test break with scope"""
        input = """
        int i;
        float f;
        string str;
        boolean boo;
        float main(int argc[], string args, boolean argv, float flo){
            string str,str2;
            {
                string str2;
                {
                    boolean str2;
                    {
                        return 0;
                    }
                }
            }
            break;
        }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,475))

    def test76_deep_block_if(self):
        """test return with path"""
        input = """
        int i;
        float f;
        string str;
        boolean boo;
        float main(int argc[], string args, boolean argv, float flo){
            if(true){
                if(false){
                    if(true)
                        return 0;

                }
                return 0;
            }
            else
                if(argv){
                    return 0;
                }
        }
        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,476))

    def test77_deep_block_if2(self):
        """test return with execute path 2rd"""
        input = """
        int i;
        float f;
        string str;
        boolean boo;
        int main(){
            if(true){
                if(boo){
                    {{return 0;}}
                }
                else{
                    return 0;
                }
            }
            else{
                if(boo){
                    return 0;
                }
                else{
                    return 1;
                }
            }
            foo();
        }
        int foo(){
            return 1.1;
        }
        """
        expect = "Type Mismatch In Statement: Return(FloatLiteral(1.1))"
        self.assertTrue(TestChecker.test(input,expect,477))

    def test78_deep_block_declared_twice(self):
        """test statement value with scope"""
        input = """
        int i;
        float f;
        string str;
        boolean boo;
        int main(){
            float c;
            {
                int c;
                {
                    boolean c;
                    {
                        string c;
                        c = "Long Dep Trai";
                    }
                    !c;
                }
                c = c%10;
            }
            boo = !(c >= 10);
            return c/1.1;
        }
        """
        expect = "Type Mismatch In Statement: Return(BinaryOp(/,Id(c),FloatLiteral(1.1)))"
        self.assertTrue(TestChecker.test(input,expect,478))

    def test79_deep_block_declared_tri(self):
        """test statement return float->int"""
        input = """
        int i;
        float f;
        string str;
        boolean boo;
        int main(){
            {
                int f; boolean i;
                {
                    f = f%10;
                }
                i = true&&false||(10<=5);
            }
            return f/.1;
        }
        """
        expect = "Type Mismatch In Statement: Return(BinaryOp(/,Id(f),FloatLiteral(0.1)))"
        self.assertTrue(TestChecker.test(input,expect,479))


    def test80_deep_block_do_4th(self):
        """test break stmt outside loop deep block"""
        input = """
        int i;
        float f;
        string str;
        boolean boo;
        int main(){
            int str;
            do{
                if(false){
                    if(true){
                        if (1 <= 10){
                            return 10;
                        }
                        else {
                            continue;
                        }
                    }
                    else{
                    }
                }
            }while(true);
            break;
            return 1;
        }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,480))

    def test81_deep_block_do_5th(self):
        """test stmt for expr"""
        input = """
        int i;
        float f;
        string str;
        boolean boo;
        int main(){
            for(10;true;1e1){
                "haha";
            }
        }
        """
        expect = "Type Mismatch In Statement: For(IntLiteral(10);BooleanLiteral(true);FloatLiteral(10.0);Block([StringLiteral(haha)]))"
        self.assertTrue(TestChecker.test(input,expect,481))

    def test82_unrechable_func_1st(self):
        """test unrechable function recursive"""
        input = """
        void foo(){}
        void foo1(){foo();}
        void foo2(){foo1();}
        void foo3(){foo2(); foo3();}
        int main(){
            do
                return 1;
            while(true);
        }
        """
        expect = "Unreachable Function: foo3"
        self.assertTrue(TestChecker.test(input,expect,482))

    def test83_unrechable_func_2nd(self):
        """test call exp  failed"""
        input = """
        void foo(){}
        void foo1(){foo();}
        void foo2(){foo2();}
        void foo3(){foo3();}
        int main(){
            foo1();
            foo3();
            float foo3;
            foo3();
            do
                return 1;
            while(true);
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo3),[])"
        self.assertTrue(TestChecker.test(input,expect,483))

    def test84_unrechable_func_3rd(self):
        """test call stmt failed"""
        input = """
        void foo(){}
        void foo1(){foo();}
        void foo2(boolean f){foo2(foo3());}
        boolean foo3(){return foo3();}
        int main(){
            foo1();
            float main;
            main = 1e10-10e1;
            string foo2;
            foo2(true);
            do
                return 1;
            while(true);
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo2),[BooleanLiteral(true)])"
        self.assertTrue(TestChecker.test(input,expect,484))

    def test85_all_check_1st(self):
        """test large code example expression failed 1st"""
        input = """
        void println(string str){}
        void save(int len){}
        void main(){
            int TimeRemaining,len,Per;
                    println("How many incorrect times do you want to get? ");
                    save(TimeRemaining);
                    println("what minimum word lengh do you want? ");
                    save(len);
                    //fstream f;
                    //f.open("input.txt",ios::in);
                    string data;
                    string List[255];
                    int NumOfWord,n;
                    List[-1] = "1005199"&&Per;
                    NumOfWord=0;
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(&&,StringLiteral(1005199),Id(Per))"
        self.assertTrue(TestChecker.test(input,expect,485))

    def test86_all_check_2nd(self):
        """test large code example expression failed 2nd"""
        input = """
        void println(string str){}
        void save(int len){}
        void getline(int l, int data){}
        void main(){
            int data,f,NumOfWord;
            string List[255];
            do{
                        getline(f,data);
                        if (data!=1) List[NumOfWord]=data;

                    }while(data!=1);
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,ArrayCell(Id(List),Id(NumOfWord)),Id(data))"
        self.assertTrue(TestChecker.test(input,expect,486))

    def test87_all_check_3rd(self):
        """test large code example stmt failed 3rd"""
        input = """
        //void println(string str){}
        //void save(int len){}
        void getline(int l, int data){}
        void main(){
            int data,f,NumOfWord;
            string List[255];
            do{
                getline(f,data);
            }while(data!=1);
            for(1;true;1){
                return 0;
            }
        }
        """
        expect = "Type Mismatch In Statement: Return(IntLiteral(0))"
        self.assertTrue(TestChecker.test(input,expect,487))

    def test88_all_check_4th(self):
        """test large code example break failed 4th"""
        input = """
        //void println(string str){}
        //void save(int len){}
        void getline(int l, int data){}
        void main(){
            int data,f,NumOfWord;
            string List[255];
            do{
                getline(f,data);
            }while(data!=1);
            for(1;true;1){
                return;
            }
            if(true){
                break;
            }
        }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,488))

    def test89_all_check_5th(self):
        """test large code example return failed 5th"""
        input = """
        //void println(string str){}
        //void save(int len){}
        void getline(int l, int data){}
        int main(){
            int data,f,NumOfWord;
            string List[255];
            do{
                getline(f,data);
            }while(data!=1);
            for(1;true;1){
                boolean b;
                b = !true&&false||(10.1>10);
            }
            if(true){
                return 0;
            }
            for(1;true;1)
                return 0;
        }
        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,489))

    def test90_all_check_6th(self):
        """test large code example declared failed 6th"""
        input = """
        //void println(string str){}
        //void save(int len){}
        void getline(int l, int data){}
        int main(float flo){
            int data,f,NumOfWord;
            string List[255];
            do{
                getline(f,data);
            }while(data!=1);
            for(1;true;1){
                boolean b;
                b = !true&&false||(10.1>10);
            }
            if(true){
                return 0;
            }
            else{
                return 0;
            }
            int flo;
        }
        """
        expect = "Redeclared Variable: flo"
        self.assertTrue(TestChecker.test(input,expect,490))

    def test91_all_check_7th(self):
        """test large code example left expression failed 7th"""
        input = """
        //void println(string str){}
        //void save(int len){}
        void getline(int l, int data){}
        int main(float flo){
            int data,f,NumOfWord;
            string List[255];
            do{
                getline(f,data);
            }while(data!=1);
            for(1;true;1){
                boolean b;
                b = !true&&false||(10.1>10);
            }
            if(true){
                return 0;
            }
            else{
                return 0;
            }
            10.1=-10;
        }
        """
        expect = "Not Left Value: FloatLiteral(10.1)"
        self.assertTrue(TestChecker.test(input,expect,491))

    def test92_all_check_8th(self):
        """test large code example left undeclared indentifier failed 8th"""
        input = """
        //void println(string str){}
        //void save(int len){}
        void getline(int l, int data){}
        int main(float flo){
            int data,f,NumOfWord;
            string List[255];
            do{
                getline(f,data);
            }while(data!=1);
            for(1;true;1){
                boolean b;
                b = !true&&false||(10.1>10);
            }
            if(true){
                return 0;
            }
            else{
                return 0;
            }
            floas;

        }
        """
        expect = "Undeclared Identifier: floas"
        self.assertTrue(TestChecker.test(input,expect,492))

    def test93_all_check_9th(self):
        """test large code example left expression failed 7th"""
        input = """
        //void println(string str){}
        //void save(int len){}
        void getline(int l, int data){}
        int main(float flo){
            int data,f,NumOfWord;
            string List[255];
            do{
                getline(f,data);
            }while(data!=1);
            for(1;true;1){
                boolean b;
                b = !true&&false||(10.1>10);
            }
            if(true){
                return 0;
            }
            else{
                return 0;
            }
            flo + data = 10;
        }
        """
        expect = "Not Left Value: BinaryOp(+,Id(flo),Id(data))"
        self.assertTrue(TestChecker.test(input,expect,493))

    def test94_all_check_10th(self):
        """test large code example left stmt return failed 7th"""
        input = """
        //void println(string str){}
        //void save(int len){}
        // void reduce
        void getline(int l, int data){}
        int main(float flo){
            int data,f,NumOfWord;
            string List[255];
            do{
                getline(f,data);
            }while(data!=1);
            for(1;true;1){
                boolean b;
                b = !true&&false||(10.1>10);
            }
            if(true){
                return 0;
            }
            else{
                return 0;
            }
            return flo;
        }
        // This is the end of Assignment 3
        // Share to be better 
        """
        expect = "Type Mismatch In Statement: Return(Id(flo))"
        self.assertTrue(TestChecker.test(input,expect,494))
    def test95_global_vWF1_rede(self):
        """test redeclared function in global scope"""
        input = """
        int main1, entry[10];
        float tfloat;
        string foo2(){return "07111999";}
        int main(int argv, string argc){
            return 0;
        }
        void foo2(){}
        """
        expect = "Redeclared Function: foo2"
        self.assertTrue(TestChecker.test(input,expect,495))

    def test96_global_vWF2_rede(self):
        """test redeclared array scope"""
        input = """
        int main1, entry[10], entry;
        float tfloat;
        string foo2(){return "07111999";}
        int main(int argv, string argc){
            return 0;
        }
        void foo2(){}
        """
        expect = "Redeclared Variable: entry"
        self.assertTrue(TestChecker.test(input,expect,496))

    def test97_global_para_rede(self):
        """test redeclared parameter in main"""
        input = """
        float tfloat;
        string foo2(){return "07111999";}
        int main(int argv, string argc, boolean argv){
            return 0;
        }
        """
        expect = "Redeclared Parameter: argv"
        self.assertTrue(TestChecker.test(input,expect,497))



    def test98_global_para_rede_2dift(self):
        """test redeclared another type parameter in main"""
        input = """
        float tfloat;
        string foo2(){return "07111999";}
        int main(int argc, string argc, boolean argv, float flo){
            return 0;
        }
        """
        expect = "Redeclared Parameter: argc"
        self.assertTrue(TestChecker.test(input,expect,498))

    def test99_global_para_rede_3dift(self):
        """test redeclared param inside"""
        input = """
        float tfloat;
        string foo2(){return "07111999";}
        int main(int argc, string flo, boolean argv, float flo){
            return 0;
        }
        """
        expect = "Redeclared Parameter: flo"
        self.assertTrue(TestChecker.test(input,expect,499))

    def test100_global_val_rede(self):
        """test redeclared local scope main"""
        input = """
        float tfloat;
        string foo2(){
            float tfloat;
            return "07111999";
        }
        int main(int argc, string args, boolean argv, float flo){
            int argc, argc[2];
            foo2();
            return 0;
        }
        """
        expect = "Redeclared Variable: argc"
        self.assertTrue(TestChecker.test(input,expect,500))
