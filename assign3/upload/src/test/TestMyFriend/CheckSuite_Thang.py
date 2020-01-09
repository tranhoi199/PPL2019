import unittest
from TestUtils import TestChecker
from AST import *


class CheckSuite(unittest.TestCase):
    # -----------------------------TEST REDECLARED-----------------------------

    def test_redeclared_variable_1(self):
        input = """
                    int b;
                    void main(){

                    }
                    float b;
                """
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_redeclared_variable_2(self):
        input = """
                    int a;
                    void main(){

                    }
                    int a()
                    {
                        return 1;
                    }
                """
        expect = "Redeclared Function: a"
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_redeclared_variable_3(self):
        input = """
                    int a;
                    void main(){
                        string a;
                        float c;
                        boolean d;
                        int e;

                        float a;
                    }
                """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,402))

    def test_redeclared_variable_4(self):
        input = """
                    int a;
                    string b;
                    float c;
                    boolean d;
                    void main(int a, string b, float c){

                    }
                    string d;
                """
        expect = "Redeclared Variable: d"
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_redeclared_variable_5(self):
        input = """
                    int a;
                    string b;
                    float c;
                    boolean d;
                    void main(int m, string b, float c, boolean d){
                        int m;
                    }
                """
        expect = "Redeclared Variable: m"
        self.assertTrue(TestChecker.test(input,expect,404))

    def test_redeclared_variable_6(self):
        input = """
                    int a[10];
                    string b[10];
                    float c[10];
                    boolean d[10];
                    void main(int a[], string b[], float c[], boolean d[]){
                        int a[10];
                    }
                """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,405))

    def test_redeclared_variable_7(self):
        input = """
                    int a[10];
                    void main(){

                    }
                    float a;
                """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,406))

    def test_redeclared_variable_8(self):
        input = """
                    int a;
                    void main(){
                    }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,407))

    def test_redeclared_variable_9(self):
        input = """
                    int a[7];
                    string b[8];
                    float c[9];
                    boolean d[10];
                    void main(int a[], string b[], float c[], boolean d[]){

                    }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,408))

    def test_redeclared_variable_10(self):
        input = """
                    int a[7];
                    void main(){
                        string a[1];
                        float c[2];
                        boolean d[3];
                        int e[4];

                        float a;
                    }
                """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,409))

    def test_redeclared_function_1(self):
        input = """
                    int main;
                    void main(){

                    }
                """
        expect = "Redeclared Function: main"
        self.assertTrue(TestChecker.test(input,expect,410))

    def test_redeclared_function_2(self):
        input = """void main()
                    {
                    }
                    int main;
                """
        expect = "Redeclared Variable: main"
        self.assertTrue(TestChecker.test(input,expect,411))

    def test_redeclared_function_3(self):
        input = """void main(){int a; string a;}"""
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,412))

    def test_redeclared_function_4(self):
        input = """
                    int main(){
                        return f(1);
                    }
                    int f(int a){
                        return true;
                    }
                """
        expect = "Type Mismatch In Statement: Return(BooleanLiteral(true))"
        self.assertTrue(TestChecker.test(input, expect, 413))

    def test_redeclared_function_5(self):
        input = """
                    void main(){}

                    void foo(){}

                    float foo(){return 2.5;}
                """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,416))

    def test_redeclared_parameter_1(self):
        input = """
                    void main(int a, float a){

                    }
                """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input,expect,414))

    def test_redeclared_parameter_2(self):
        input = """
                    void main(int a, string a[]){

                    }
                """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input,expect,415))

    def test_redeclared_all_1(self):
        input = """
                    void main(){
                        int main;
                        {
                            boolean main;
                            {
                                string main;
                                {
                                    float main;
                                }
                            }
                        }
                    }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,417))

    def test_redeclared_all_2(self):
        input = """
                    int a;
                    void main(int a){
                        if (a==6)
                        {
                            boolean a;
                        }
                        else{
                            string a;
                        }
                    }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,418))

    def test_redeclared_all_3(self):
        input = """
                    int a,b,c,d;
                    void main(int a, string b){
                        do{
                            int a;
                            float b;
                            string c;
                            boolean d;
                        }
                        while (a==7);
                    }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,419))

    #-----------------------------TEST UNDECLARED-----------------------------

    def test_undeclared_1(self):
        input = """
                    void main(){
                        a;
                    }
                """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,420))

    def test_undeclared_2(self):
        input = """
                    void main(){
                        a=foo();
                    }
                    int a;
                    int foo(){
                        return true;
                    }
                """
        expect = "Type Mismatch In Statement: Return(BooleanLiteral(true))"
        self.assertTrue(TestChecker.test(input,expect,421))

    def test_undeclared_3(self):
        input = """
                    int a;
                    void main(){
                        if (a>7){
                            int b;
                        }
                        else{
                            int b;
                        }
                        b;
                    }
                """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,422))

    def test_undeclared_4(self):
        input = """
                    int a;
                    void main(){
                        {{{{{{a;}}}}}}
                    }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,423))

    def test_undeclared_5(self):
        input = """
                    void main(){
                        main();
                        foo();
                    }
                """
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,424))

    def test_undeclared_6(self):
        input = """
                    void main(){
                        main();
                        foo(a);
                    }

                    int foo(string a){
                        return --5;
                    }
                """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,425))

    def test_undeclared_7(self):
        input = """
                    void main(){
                        do{
                            int a;
                            float b;
                            string c;
                        } while (a > 7);
                    }
                """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,426))

    def test_undeclared_8(self):
        input = """
                    void main(){
                        int a;
                        {
                            a;
                            {
                                boolean a;
                                a;
                                {
                                    a;
                                }
                            }
                        }
                    }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,427))

    def test_undeclared_9(self):
        input = """
                    void main(){
                        int foo;
                        foo(true);
                    }
                    int foo(boolean c){
                        return 5;
                        foo(true);
                    }
                """
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,428))

    def test_undeclared_10(self):
        input = """
                    void main(){
                    }
                    int foo(int c){
                        return 5;
                        foo(foo(5));
                    }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,429))

    #-----------------------------TEST Type Mismatch In Expression:-----------------------------

    def test_expression_1(self):
        input = """
                    void main(){
                        int a, m[10];
                        string b, n[9];
                        float c, p[8];
                        boolean d, q[7];

                        a = 6; m[1] = 5;
                        b = "hello"; n[7] = "khoa";
                        c = 5.5; p[1] = 9.9;
                        d = true; q[2] = false;
                        a = a + m[1];
                        m[1+5];
                        c > 7.3;
                        c = p[7] + a;
                        d == true;
                        q[1] == false;
                        d && q[9];
                        d || (a>1);
                        a % 9;
                        1 + 2 - 4 * 6 / 5;
                        -5; -5.5; !true; !false;
                    }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,430))

    def test_expression_2(self):
        input = """
                     void main(){
                        int a, m[10];
                        string b, n[9];
                        float c, p[8];
                        boolean d, q[7];

                        -true;
                    }
                """
        expect = "Type Mismatch In Expression: UnaryOp(-,BooleanLiteral(true))"
        self.assertTrue(TestChecker.test(input,expect,431))

    def test_expression_3(self):
        input = """
                    void main(){
                        int a, m[10];
                        string b, n[9];
                        float c, p[8];
                        boolean d, q[7];

                        -"hello";
                    }
                """
        expect = "Type Mismatch In Expression: UnaryOp(-,StringLiteral(hello))"
        self.assertTrue(TestChecker.test(input,expect,432))

    def test_expression_4(self):
        input = """
                    void main(){
                        int a, m[10];
                        string b, n[9];
                        float c, p[8];
                        boolean d, q[7];

                        !1;
                    }
                """
        expect = "Type Mismatch In Expression: UnaryOp(!,IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,433))

    def test_expression_5(self):
        input = """
                    void main(){
                        int a, m[10];
                        string b, n[9];
                        float c, p[8];
                        boolean d, q[7];

                        !5.5;
                    }
                """
        expect = "Type Mismatch In Expression: UnaryOp(!,FloatLiteral(5.5))"
        self.assertTrue(TestChecker.test(input,expect,434))

    def test_expression_6(self):
        input = """
                    void main(){
                        int a, m[10];
                        string b, n[9];
                        float c, p[8];
                        boolean d, q[7];

                        a + 6 = 7;
                    }
                """
        expect = "Not Left Value: BinaryOp(=,BinaryOp(+,Id(a),IntLiteral(6)),IntLiteral(7))"
        self.assertTrue(TestChecker.test(input,expect,435))

    def test_expression_7(self):
        input = """
                    void main(){
                        int a, m[10];
                        string b, n[9];
                        float c, p[8];
                        boolean d, q[7];

                        m = 7;
                    }
                """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(m),IntLiteral(7))"
        self.assertTrue(TestChecker.test(input,expect,436))

    def test_expression_8(self):
        input = """
                    void main(int temp[]){
                        int a, m[10];
                        string b, n[9];
                        float c, p[8];
                        boolean d, q[7];

                        temp = 7;
                    }
                """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(temp),IntLiteral(7))"
        self.assertTrue(TestChecker.test(input,expect,437))

    def test_expression_9(self):
        input = """
                    int main(int temp[]){
                        int a, m[10];
                        string b, n[9];
                        float c, p[8];
                        boolean d, q[7];

                        main = 7;
                        return 5;
                    }
                """
        expect = "Undeclared Identifier: main"
        self.assertTrue(TestChecker.test(input,expect,438))

    def test_expression_10(self):
        input = """
                    int main(int temp[]){
                        int a, m[10];
                        string b, n[9];
                        float c, p[8];
                        boolean d, q[7];

                        b = 5;
                        return 4;
                    }
                """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(b),IntLiteral(5))"
        self.assertTrue(TestChecker.test(input,expect,439))

    def test_expression_11(self):
        input = """
                    void main(int temp[]){
                        int a, m[10];
                        string b, n[9];
                        float c, p[8];
                        boolean d, q[7];

                        5+6; 5+6.5; 6.5+5; 6.5+5.5;
                        5-6; 5-6.5; 6.5-5; 6.5-5.5;
                        5*6; 5*6.5; 6.5*5; 6.5*5.5;
                        5/6; 5/6.5; 6.5/5; 6.5/5.5;
                        4 == 6;
                        a == m[6];
                        d == q[1];
                        "hello" == "hello";
                    }
                """
        expect = "Type Mismatch In Expression: BinaryOp(==,StringLiteral(hello),StringLiteral(hello))"
        self.assertTrue(TestChecker.test(input,expect,440))

    def test_expression_12(self):
        input = """
                    void main(int temp[]){
                        int a, m[10];
                        string b, n[9];
                        float c, p[8];
                        boolean d, q[7];

                        5 % 6.7;
                    }
                """
        expect = "Type Mismatch In Expression: BinaryOp(%,IntLiteral(5),FloatLiteral(6.7))"
        self.assertTrue(TestChecker.test(input,expect,441))

    def test_expression_13(self):
        input = """
                    void main(int temp[]){
                        int a, m[10];
                        string b, n[9];
                        float c, p[8];
                        boolean d, q[7];

                        5.5 == 5.5;
                    }
                """
        expect = "Type Mismatch In Expression: BinaryOp(==,FloatLiteral(5.5),FloatLiteral(5.5))"
        self.assertTrue(TestChecker.test(input,expect,442))

    def test_expression_14(self):
        input = """
                    void main(int temp[]){
                        int a, m[10];
                        string b, n[9];
                        float c, p[8];
                        boolean d, q[7];

                        m[5.5];
                    }
                """
        expect = "Type Mismatch In Expression: ArrayCell(Id(m),FloatLiteral(5.5))"
        self.assertTrue(TestChecker.test(input,expect,443))

    def test_expression_15(self):
        input = """
                    void main(int temp[]){
                        int a, m[10];
                        string b, n[9];
                        float c, p[8];
                        boolean d, q[7];

                        foo()[1] = 2;
                        m[m[m[a]]];
                        m[1] = 7;
                    }

                    int[] foo(){
                        int a[10];
                        return a;
                    }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,444))

    def test_expression_16(self):
        input = """
                    void main(int temp[]){
                        int a, m[10];
                        string b, n[9];
                        float c, p[8];
                        boolean d, q[7];

                        foo(m[1],n[2],p[3],q[4]);
                        foo(a,b,c,d);
                    }

                    int[] foo(int a, string b, float c, boolean d){
                        int k[10];
                        return k;
                    }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,445))

    def test_expression_17(self):
        input = """
                    void main(int temp[]){
                        int a, m[10];
                        string b, n[9];
                        float c, p[8];
                        boolean d, q[7];

                        foo();
                    }

                    int[] foo(int a, string b, float c, boolean d){
                        int k[10];
                        return k;
                    }
                """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[])"
        self.assertTrue(TestChecker.test(input,expect,446))

    def test_expression_18(self):
        input = """
                    void main(int temp[]){
                        int a, m[10];
                        string b, n[9];
                        float c, p[8];
                        boolean d, q[7];

                        foo(a,b,c,a);
                    }

                    int[] foo(int a, string b, float c, boolean d){
                        int k[10];
                        return k;
                    }
                """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[Id(a),Id(b),Id(c),Id(a)])"
        self.assertTrue(TestChecker.test(input,expect,447))

    def test_expression_19(self):
        input = """
                    void main(int temp[], boolean temp2[]){
                        int a, m[10];
                        string b, n[9];
                        float c, p[8];
                        boolean d, q[7];

                        foo(a,b,c,q);
                        foo(a,b,c,temp2);
                        foo(a,b,c,temp);
                    }

                    int[] foo(int a, string b, float c, boolean d[]){
                        int k[10];
                        return k;
                    }
                """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[Id(a),Id(b),Id(c),Id(temp)])"
        self.assertTrue(TestChecker.test(input,expect,448))

    def test_expression_20(self):
        input = """
                    void main(int temp[], boolean temp2[]){
                        int a, m[10];
                        string b, n[9];
                        float c, p[8];
                        boolean d, q[7];

                        foo(foo(m,b,c,q),b,c,q);
                        foo(foo(m,b,c,q),b,c,temp2);
                    }

                    int[] foo(int a[], string b, float c, boolean d[]){
                        int k[10];
                        return k;
                    }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,449))

    #-----------------------------TEST Type Mismatch In Statement:-----------------------------

    def test_statement_1(self):
        input = """
                    void main(){
                        int a, m[10];
                        string b, n[9];
                        float c, p[8];
                        boolean d, q[7];

                        if (a > 7.5) a = a +1;

                        if (a > 7.5) a = a +1;
                        else b = "hello";

                        if (!true) a = a +1;
                        else b = "hello";

                        if (!false) a = a +1;
                        else b = "hello";

                        if ((a>7) && (a <9)) a = a +1;
                        else b = "hello";

                        if ((a>7) || (a < 9)) a = a +1;
                        else b = "hello";

                        if ((d==true) || (q[5] == false)) a = a +1;
                        else b = "hello";

                        if (a > 7 || c < 9.8 && c >= 11.2 + 6 || true && a <= c) a = a +1;
                        else b = "hello";
                    }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,450))

    def test_statement_2(self):
        input = """
                    void main(){
                        int a, m[10];
                        string b, n[9];
                        float c, p[8];
                        boolean d, q[7];

                        int i;
                        for (i = 0; i < 10; i=i+1)
                            a = a + 1;

                        for (i = 0; i < 10; i=i*2)
                            a = a + 1;

                        for (-i; i < 10; -i)
                            a = a + 1;

                        for (5+6*7-10; i < 10; 5+6*7-10)
                            a = a + 1;

                        for (5%8; i < 10; 5%8)
                            a = a + 1;

                        for (m[1]; i < 10; m[1])
                            a = a + 1;

                        for (m[1]; i < 10; m[1])
                            a = a + 1;

                        for (foo(); i < 10; foo())
                            a = a + 1;

                        for (foo2()[1]; i < 10; foo2()[1])
                            a = a + 1;

                        for (foo2()[m[m[a]]]; i < 10; i = i + 1)
                            a = a + 1;
                    }

                    int foo(){
                        return 5;
                    }

                    int[] foo2(){
                        return foo2();
                    }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,451))

    def test_statement_3(self):
        input = """
                    void main(){
                        int a, m[10];
                        string b, n[9];
                        float c, p[8];
                        boolean d, q[7];

                        float i;
                        for (i = 5.5; 5 < 10; a=a+1)
                            a = a + 1;
                        a = a +1;
                    }
                """
        expect = "Type Mismatch In Statement: For(BinaryOp(=,Id(i),FloatLiteral(5.5));BinaryOp(<,IntLiteral(5),IntLiteral(10));BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)));BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1))))"
        self.assertTrue(TestChecker.test(input,expect,452))

    def test_statement_4(self):
        input = """
                    void main(){
                        int a, m[10];
                        string b, n[9];
                        float c, p[8];
                        boolean d, q[7];

                        float i;
                        for (c*a; 5 < 10; a=a+1)
                            a = a + 1;
                        a = a +1;
                    }
                """
        expect = "Type Mismatch In Statement: For(BinaryOp(*,Id(c),Id(a));BinaryOp(<,IntLiteral(5),IntLiteral(10));BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)));BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1))))"
        self.assertTrue(TestChecker.test(input,expect,453))

    def test_statement_5(self):
        input = """
                    void main(){
                        int a, m[10];
                        string b, n[9];
                        float c, p[8];
                        boolean d, q[7];

                        float i;
                        for (1; 5 +5; a=a+1)
                            a = a + 1;
                        a = a +1;
                    }
                """
        expect = "Type Mismatch In Statement: For(IntLiteral(1);BinaryOp(+,IntLiteral(5),IntLiteral(5));BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)));BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1))))"
        self.assertTrue(TestChecker.test(input,expect,454))

    def test_statement_6(self):
        input = """
                    void main(){
                        int a, m[10];
                        string b, n[9];
                        float c, p[8];
                        boolean d, q[7];

                        float i;
                        do{}
                        while(i < 7);
                        return;
                    }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,455))

    def test_statement_7(self):
        input = """
                    void main(){
                        int a[10];
                        string b[10];
                        float c[10];
                        boolean d[10];
                        foo1();
                        foo2();
                        foo3();
                        foo4();
                        foo5();
                        foo6();
                        foo7();
                        foo8();
                        foo9(a);
                        foo10(b);
                        foo11(d);
                        foo12(c);
                        foo13();
                    }

                    int foo1(){
                        return 5;
                    }

                    string foo2(){
                        return "hello";
                    }

                    boolean foo3(){
                        return true;
                    }

                    float foo4(){
                        return 5.67984 * 6 / 7 - 8;
                    }

                    int[] foo5(){
                        int a[10];
                        return a;
                    }

                    string[] foo6(){
                        string b[10];
                        return b;
                    }

                    boolean[] foo7(){
                        boolean c[10];
                        return c;
                    }

                    float[] foo8(){
                        float d[10];
                        return d;
                    }

                    int[] foo9(int x[]){
                        int a[10];
                        return x;
                    }

                    string[] foo10(string y[]){
                        string b[10];
                        return y;
                    }

                    boolean[] foo11(boolean z[]){
                        boolean c[10];
                        return z;
                    }

                    float[] foo12(float k[]){
                        float d[10];
                        return k;
                    }

                    float foo13(){
                        return 5;
                    }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,456))

    def test_statement_8(self):
        input = """
                    int main(){
                        return true;
                    }
                """
        expect = "Type Mismatch In Statement: Return(BooleanLiteral(true))"
        self.assertTrue(TestChecker.test(input,expect,457))

    def test_statement_9(self):
        input = """
                    void main(){
                        return 5;
                    }
                """
        expect = "Type Mismatch In Statement: Return(IntLiteral(5))"
        self.assertTrue(TestChecker.test(input,expect,458))

    def test_statement_10(self):
        input = """
                    float[] main(){
                        int a[10];
                        float b[10];
                        return a;
                    }
                """
        expect = "Type Mismatch In Statement: Return(Id(a))"
        self.assertTrue(TestChecker.test(input,expect,459))

    #-----------------------------TEST No Entry Point:-----------------------------

    def test_entry_point_1(self):
        input = """
                    int main;
                """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,460))

    def test_entry_point_2(self):
        input = """
                    void main(int a, string b, float c, boolean d, int e[], string f[], float g[], boolean h[]){

                    }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,461))

    def test_entry_point_3(self):
        input = """
                    int main(int a, string b, float c, boolean d, int e[], string f[], float g[], boolean h[]){
                        return 5;
                    }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,462))

    def test_entry_point_4(self):
        input = """
                    boolean main(int a, string b, float c, boolean d, int e[], string f[], float g[], boolean h[]){
                        return true;
                    }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,463))

    #-----------------------------TEST Break/Continue not in loop:-----------------------------

    def test_break_continue_1(self):
        input = """
                    void main(){
                        break;
                    }
                """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,464))

    def test_break_continue_2(self):
        input = """
                    void main(){
                        continue;
                    }
                """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,465))

    def test_break_continue_3(self):
        input = """
                    void main(){
                        int i;
                        for (i = 0; i < 10; i = i + 1){
                            break;
                            continue;
                        }

                        for (i = 0; i < 10; i = i + 1)
                            break;

                        for (i = 0; i < 10; i = i + 1)
                            continue;

                        do{
                            break;
                            continue;
                        } while (i==6);

                        do
                            break;
                            continue;
                        while (i==6);

                        for (i = 0; i < 10; i = i + 1){
                            break;
                            continue;
                            {
                                break;
                                continue;
                                {
                                    break;
                                    continue;
                                    {
                                        break;
                                        continue;
                                        if (i == 6) continue;
                                        else break;
                                    }
                                }
                            }
                        }

                        do
                        {}
                        {}
                        break;
                        {}
                        continue;
                        while (i==5);
                    }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,466))

    def test_break_continue_4(self):
        input = """
                    void main(){
                        int i;
                        do{} while(i==6);
                        for (i;i<5;i){}
                        if(i==5)
                            break;
                    }
                """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,467))

    def test_break_continue_5(self):
        input = """
                    void main(){
                        int i;

                        for (i;i<5;i)
                            continue;
                            break;
                    }
                """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,468))

    def test_break_continue_6(self):
        input = """
                    void main(){
                        int i;
                        if (i==5){
                            for (i;i<5;i){
                                break;
                            }
                            do
                                continue;
                                break;
                            while(i<5);
                            continue;
                        }
                    }
                """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,469))

    #-----------------------------TEST Unreachable function-----------------------------

    def test_unreachable_1(self):
        input = """
                    void main(){

                    }

                    int foo1(){
                        return foo1();

                    }
                    string foo2(){
                        return foo2();
                    }
                    float foo3(){
                        return foo3();
                    }
                    boolean foo4(){
                        return foo4();
                    }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,470))

    def test_unreachable_2(self):
        input = """
                    void main(){

                    }

                    int foo1(){
                        return 5;
                        {{{{foo2();}}}}
                    }
                    string foo2(){
                        return "hello";
                        {{{{foo3();}}}}
                    }
                    float foo3(){
                        return 5.5;
                        {{{{foo4();}}}}
                    }
                    boolean foo4(){
                        return false;
                        {{{{foo1();}}}}
                    }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,471))

    def test_unreachable_3(self):
        input = """
                    void main(){

                    }

                    int foo1(){
                        return 5;
                        {{{{}}}}
                    }
                    string foo2(){
                        return "hello";
                        {{{{foo3();}}}}
                    }
                    float foo3(){
                        return 5.5;
                        {{{{foo4();}}}}
                    }
                    boolean foo4(){
                        return false;
                        {{{{foo1();}}}}
                    }
                """
        expect = "Unreachable Function: foo2"
        self.assertTrue(TestChecker.test(input,expect,472))

    def test_unreachable_4(self):
        input = """
                    void main(){

                    }

                    int foo1(){
                        return 5;
                        {{{{foo2();}}}}
                    }
                    string foo2(){
                        return "hello";
                        {{{{}}}}
                    }
                    float foo3(){
                        return 5.5;
                        {{{{foo4();}}}}
                    }
                    boolean foo4(){
                        return false;
                        {{{{foo1();}}}}
                    }
                """
        expect = "Unreachable Function: foo3"
        self.assertTrue(TestChecker.test(input,expect,473))

    def test_unreachable_5(self):
        input = """
                    void main(){

                    }

                    int foo1(){
                        return 5;
                        {{{{foo2();}}}}
                    }
                    string foo2(){
                        return "hello";
                        {{{{foo3();}}}}
                    }
                    float foo3(){
                        return 5.5;
                        {{{{}}}}
                    }
                    boolean foo4(){
                        return false;
                        {{{{foo1();}}}}
                    }
                """
        expect = "Unreachable Function: foo4"
        self.assertTrue(TestChecker.test(input,expect,474))

    def test_unreachable_6(self):
        input = """
                    void main(){

                    }

                    int foo1(){
                        return 5;
                        {{{{foo2();}}}}
                    }
                    string foo2(){
                        return "hello";
                        {{{{foo3();}}}}
                    }
                    float foo3(){
                        return 5.5;
                        {{{{foo4();}}}}
                    }
                    boolean foo4(){
                        return false;
                        {{{{}}}}
                    }
                """
        expect = "Unreachable Function: foo1"
        self.assertTrue(TestChecker.test(input,expect,475))

    #-----------------------------TEST Not Left Value-----------------------------

    def test_not_left_1(self):
        input = """
                    void main(){
                        int i;
                        ((i)) = 5;
                        ((i+6)) = 5;
                    }
                """
        expect = "Not Left Value: BinaryOp(=,BinaryOp(+,Id(i),IntLiteral(6)),IntLiteral(5))"
        self.assertTrue(TestChecker.test(input,expect,476))

    def test_not_left_2(self):
        input = """
                    void main(){
                        int i, b[6];
                        b[b[b[6]]] = 5;
                        foo = foo;
                    }

                    int foo(){
                        return 5;
                        foo();
                    }
                """
        expect = "Undeclared Identifier: foo"
        self.assertTrue(TestChecker.test(input,expect,477))

    def test_not_left_3(self):
        input = """
                    void main(int a[]){
                        foo()[7] = 5;
                        a[7+a[1]] = 6;
                    }

                    int[] foo(){
                        int a[7];
                        return a;
                    }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,478))

    #-----------------------------TEST Function not return-----------------------------

    def test_not_return_0(self):
        input = """
                    int main(){

                    }
                """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,479))

    def test_not_return_1(self):
        input = """
                    int main(){
                        int i;
                        if (i==6) return 5;
                        else {
                            return 5;
                        }
                    }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,480))

    def test_not_return_2(self):
        input = """
                    int main(){
                        int i;
                        if (i==6) {
                            if (i>7)
                                return 5;
                        }
                        else {
                            return 5;
                        }
                    }
                """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,481))

    def test_not_return_3(self):
        input = """
                    int main(){
                        int i;
                        if (i==6) {
                            if (i>7)
                                return 5;
                            else return 6;
                        }
                        else {
                            return 5;
                        }

                        if (i==6) i;
                    }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,482))

    def test_not_return_4(self):
        input = """
                    int main(){
                        int i;
                        if (i==6) {

                        }
                        else {

                        }
                        return 5;
                    }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,483))

    def test_not_return_5(self):
        input = """
                    int main(){
                        int i;
                        if (i==6) {
                            {{{{return 5;}}}}
                        }
                        else {
                            {{{{{{return 5;}}}}}}
                        }
                    }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,484))

    def test_not_return_6(self):
        input = """
                    int main(){
                        int i;
                        int j;
                        if (i>-5){
                            for (i = 1; i < 10; i = i + 1)
                                if (i == 7) return 5;
                                else return 7;
                        }
                        else {
                            do
                            for (i = 1; i < 10; i = i + 1)
                            {
                                for (i = 1; i < 10; i = i + 1)
                                    return 5;
                            }
                            while (i==7);
                        }
                    }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,485))

    def test_not_return_7(self):
        input = """
                    int main(){
                        int i;
                        int j;
                        if (i>-5){
                            for (i = 1; i < 10; i = i + 1)
                                if (i == 7) return 5;
                                else return 7;
                        }
                        else {
                            do
                            {}
                            {}
                            for (i = 1; i < 10; i = i + 1)
                            {
                                for (i = 1; i < 10; i = i + 1)
                                    return 7;
                            }
                            {}
                            {}
                            while (i==7);
                        }
                    }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,486))

    def test_not_return_8(self):
        input = """
                    int main(){
                        int i;
                        int j;
                        if (i>-5){
                            for (i = 1; i < 10; i = i + 1)
                                if (i == 7) return 5;
                                else return 7;
                        }
                        else {
                            do
                            {}
                            {}
                            for (i = 1; i < 10; i = i + 1)
                            {
                                for (i = 1; i < 10; i = i + 1)
                                    do
                                        if (i==5)
                                            return 7;
                                    while (i==5);
                            }
                            {}
                            {}
                            while (i==7);
                        }
                    }
                """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,487))

    def test_not_return_9(self):
        input = """
                    int main(){
                        int i;
                        int j;
                        if (i>-5){
                            for (i = 1; i < 10; i = i + 1)
                                if (i == 7) return 5;
                                else return 7;
                        }
                        else {
                            do
                            {}
                            {}
                            for (i = 1; i < 10; i = i + 1)
                            {
                                for (i = 1; i < 10; i = i + 1)
                                    do
                                        if (i==5)
                                            return 7;
                                        else return 6;
                                    while (i==5);
                            }
                            {}
                            {}
                            while (i==7);
                        }
                    }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,488))

    def test_not_return_10(self):
        input = """
                    int main(){
                        int i;
                        for (i;i<5;i){
                            break;
                        }
                        {{{{{{return 5;}}}}}}
                    }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,489))

    def test_all_1(self):
        input = """
                    void main(){
                        a;
                        int a;
                    }
                """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,490))

    def test_all_2(self):
        input = """
                    int i;
                    boolean main(string b, float c){
                        for (i;i>10;i)
                            for (i;i>10;i)
                                for (i;i>10;i)
                                    do
                                        if (i==6)
                                            return true;
                                        else return false;
                                    while (i==7);
                    }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,491))

    def test_all_3(self):
        input = """
                    int i;
                    boolean main(string b, float c){
                        for (i;i>10;i)
                            for (i;i>10;i)
                                for (i;i>10;i)
                                    do {}{}{}{}
                                    {
                                        if (i==6)
                                            return true;
                                    }
                                    while (i==7);
                    }
                """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,492))

    def test_all_4(self):
        input = """
                    int i;
                    boolean main(string b, float c){
                        for (i;i>10;i)
                            for (i;i>10;i)
                                for (i;i>10;i)
                                    do {}{}{}{}
                                    {
                                        if (i==6)
                                            return true;
                                        {return false;}
                                        continue;
                                        break;
                                    }
                                    while (i==7);
                    }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,493))

    def test_all_5(self):
        input = """
                    int i;
                    boolean main(string b, float c){
                        for (i;i>10;i)
                            for (i;i>10;i)
                                for (i;i>10;i)
                                    do {}{}{}{}
                                    {
                                        if (i==6)
                                            return true;
                                        return false;
                                        continue;
                                        break;
                                       {
                                           for (i;i>10;i)
                                                do {}{}{}{}

                                                while(foo(5,6,4)[1] == true || foo(7,8,9)[1] != true);
                                       }
                                    }
                                    while (i==7);
                    }

                    boolean[] foo(int a, int c, int d){
                        return foo(a,c,d);
                    }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,494))

    def test_all_6(self):
        input = """
                    int i;
                    boolean z[10];
                    boolean[] main(string b, float c, boolean d[]){
                        foo(4,5,6,d);
                        return main(b,c,d);
                    }

                    boolean[] foo2(){
                        return z;
                    }

                    boolean[] foo(float a, float c, float d, boolean main2[]){
                        return main("fawe",5.5,foo(5,6,7,foo2()));
                    }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,495))

    def test_all_7(self):
        input = """
                    int a[10];
                    void main(){

                    }
                    float a;
                """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,496))

    def test_all_8(self):
        input = """
                    int a[10];
                    void main(){
                        string a[1];
                        float c[2];
                        boolean d[3];
                        int e[4];
                    }
                    float c[10];
                    int d[10];
                    boolean e[7];
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,497))

    def test_all_9(self):
        input = """
                    int a[7];
                    string b[8];
                    float c[9];
                    boolean d[10];
                    void main(int a[], string b[], float c[], boolean d[]){

                    }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,498))

    def test_all_10(self):
        input = """
                    int a[7];
                    void main(){
                        string a[1];
                        float c[2];
                        boolean d[3];
                        int e[4];

                        float a;
                    }
                """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,499))
