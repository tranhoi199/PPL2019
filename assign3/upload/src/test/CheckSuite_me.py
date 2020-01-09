import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):
    def test_undeclared_function(self):
        """Simple program: int main() {} """
        input = """void main() {foo();}"""
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_diff_numofparam_stmt(self):
        """More complex program"""
        input = """void main (){
            putIntLn();
        }"""
        expect = "Type Mismatch In Expression: CallExpr(Id(putIntLn),[])"
        self.assertTrue(TestChecker.test(input,expect,401))
    
    def test_diff_numofparam_expr(self):
        """More complex program"""
        input = """void main () {
            putIntLn(getInt(4));
        }"""
        expect = "Type Mismatch In Expression: CallExpr(Id(getInt),[IntLiteral(4)])"
        self.assertTrue(TestChecker.test(input,expect,402))
    def test_undeclared_function_use_ast(self):
        """Simple program: int main() {} """
        input = Program([FuncDecl(Id("main"),[],VoidType(),Block([
            CallExpr(Id("foo"),[])]))])
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,403))
    def test_diff_numofparam_expr_use_ast(self):
        """More complex program"""
        input = Program([
                FuncDecl(Id("main"),[],VoidType(),Block([
                    CallExpr(Id("putIntLn"),[
                        CallExpr(Id("getInt"),[IntLiteral(4)])
                        ])]))])
        expect = "Type Mismatch In Expression: CallExpr(Id(getInt),[IntLiteral(4)])"
        self.assertTrue(TestChecker.test(input,expect,404))
    def test_diff_numofparam_stmt_use_ast(self):
        """More complex program"""
        input = Program([
                FuncDecl(Id("main"),[],VoidType(),Block([
                    CallExpr(Id("putIntLn"),[])]))])
        expect = "Type Mismatch In Expression: CallExpr(Id(putIntLn),[])"
        self.assertTrue(TestChecker.test(input,expect,405))
    def test_vardecl_without_main(self):
        """More complex program"""
        input = """ int a; """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,406))
    def test_vardecl_without_main2(self):
        """More complex program"""
        input = """ int a; """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,407))
    def test_redeclare_global(self):
        """More complex program"""
        input = """ int a; int a;
            void main(){
                }
            """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,408))
    def test_redeclare_global1(self):
        """More complex program"""
        input = """ int a;
            
            void main(){
                int a;
                return;
                }
            int a;
            """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,409))
    def test_unreachable(self):
        """More complex program"""
        input = """ int a;
            
            int foo(int b){
                return 10;
            }
            void main(){
                int ab;
                return;
            }
            """
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input,expect,410))
    def test_unreachable1(self):
        """More complex program"""
        input = """ int a;
            int b;
            int foo(int b){
                return 10;
            }
            void main(){
                int ab;
                }
            """
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input,expect,411))
    def test_redclare_in_func(self):
        """More complex program"""
        input = """ int a;
            int b;
            void foo(int b){
                int b;
            }
            void main(){
                int ab;

                }
            """
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input,expect,412))
    def test_redclare_in_global(self):
        """More complex program"""
        input = """ int a;
            int foo;
            void foo(int b){
                
            }
            void main(){
                int ab;
                int a;
                }
            """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,413))
    def test_redclare_in_main(self):
        """More complex program"""
        input = """ int a;
            int foo;
            void foo1(int b){
                return;
            }
            void main(){
                int ab;
                int ab;
            }
            """
        expect = "Redeclared Variable: ab"
        self.assertTrue(TestChecker.test(input,expect,414))
    def test_Undeclare(self):
        """More complex program"""
        input = """ 
            int c;
            void main(){
                int ab;
                ab;
                c;
                a;
                }
            """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,415))
    def test_miss_match_string(self):
        """More complex program"""
        input = """ 

            void main(){
                string a;
                int b;
                a = 1;
                }
            """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,416))
    def test_miss_match_boolean(self):
        """More complex program"""
        input = """ 

            void main(){
                int a;
                int b;

                a = false;
                }
            """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),BooleanLiteral(false))"
        self.assertTrue(TestChecker.test(input,expect,417))
    def test_miss_match_float(self):
        """More complex program"""
        input = """ 

            void main(){
                int a;
                int b;
                b = 2;
                a = 1.2;
                }
            """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),FloatLiteral(1.2))"
        self.assertTrue(TestChecker.test(input,expect,418))
    
    def test_miss_match_plus(self):
        """More complex program"""
        input = """ 

            void main(){
                int a;
                int b;
                b = 2;
                a = b+1.2;
                }
            """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),BinaryOp(+,Id(b),FloatLiteral(1.2)))"
        self.assertTrue(TestChecker.test(input,expect,419))
    def test_miss_match_mul(self):
        """More complex program"""
        input = """ 

            void main(){
                int a;
                int b;
                a = b*1.2;
                }
            """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),BinaryOp(*,Id(b),FloatLiteral(1.2)))"
        self.assertTrue(TestChecker.test(input,expect,420))
    def test_miss_match_divide(self):
        """More complex program"""
        input = """ 

            void main(){
                int a;
                int b;
                b = 9;
                a = b/2;
                }
            """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,421))
    def test_miss_match_divide1(self):
        """More complex program"""
        input = """ 

            void main(){
                int a;
                int b;
                b = 9.2;
                a = b/2;
                }
            """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(b),FloatLiteral(9.2))"
        self.assertTrue(TestChecker.test(input,expect,422))
    def test_miss_match_divide_with_float32(self):
        """More complex program"""
        input = """ 

            void main(){
                int a;
                float b;
                b = 9.2;
                a = b/2;
                }
            """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),BinaryOp(/,Id(b),IntLiteral(2)))"
        self.assertTrue(TestChecker.test(input,expect,423))
    def test_miss_match_assign_bool(self):
        """More complex program"""
        input = """ 

            void main(){
                boolean a;
                boolean b;
                b = "1";
                }
            """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(b),StringLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,424))

    def test_miss_match_assign_strings1(self):
        """More complex program"""
        input = """ 

            void main(){
                boolean a;
                string b;
                b = 1;

                }
            """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(b),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,425))
    def test_miss_match_assign_strings3(self):
        """More complex program"""
        input = """ 

            void main(){
                boolean a,b,c;
                int d,e;
                c = a || b && (d >= e );
                c = a || 1;
                }
            """
        expect = "Type Mismatch In Expression: BinaryOp(||,Id(a),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,426))
    def test_block_in_block(self):
        """More complex program"""
        input = """ 
            void main(){
                int ab;
                int b;
                    {
                    int ab;
                    {
                        int ab;
                        b = 1.2;
                    }
                    }
                }
            """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(b),FloatLiteral(1.2))"
        self.assertTrue(TestChecker.test(input,expect,427))
    def test_miss_match_assign_strings(self):
        """More complex program"""
        input = """ 

            void main(){
                boolean a;
                string b;
                b = 1;

                }
            """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(b),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,428))
    def test_block_in_block_with_assigns132(self):
        """More complex program"""
        input = """ 
            void main(){
                int ab;
                int b;
                    {
                    int ab;
                    {
                        int ab;
                        b = 12;
                    }
                    ab = true;
                    }
                    return;
                }
            """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(ab),BooleanLiteral(true))"
        self.assertTrue(TestChecker.test(input,expect,429))
    def test_no_return(self):
        """More complex program"""
        input = """ 
            void main(){
                    int a;
                    a = 1;
                }
            """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,430))
    def test_return_value_in_void(self):
        """More complex program"""
        input = """ 
            void main(){
                    int a;
                    a = 1;
                    return 1;
                }
            """
        expect = "Type Mismatch In Statement: Return(IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,431))
    def test_return_none_in_int(self):
        """More complex program"""
        input = """ 
        int foo(){
            return;
        }
            void main(){
                    int a;
                    a = 1;
                    return;
                }
            """
        expect = "Type Mismatch In Statement: Return()"
        self.assertTrue(TestChecker.test(input,expect,432))
    def test_return_float_in_int(self):
        """More complex program"""
        input = """ 
        int foo(){
            return 1.2;
        }
            void main(){
                    int a;
                    a = 1;
                    return;
                }
            """
        expect = "Type Mismatch In Statement: Return(FloatLiteral(1.2))"
        self.assertTrue(TestChecker.test(input,expect,433))
    def test_return_float_with_var_in_int(self):
        """More complex program"""
        input = """ 
        int foo(){
            float b;
            return b;
        }
            void main(){
                    int a;
                    a = 1;
                    return;
                }
            """
        expect = "Type Mismatch In Statement: Return(Id(b))"
        self.assertTrue(TestChecker.test(input,expect,434))
    def test_return_exp_float_with_var_in_int(self):
        """More complex program"""
        input = """ 
        int foo(){
            
            return 1.5+2;
        }
            void main(){
                    int a;
                    a = 1;
                    return;
                }
            """
        expect = "Type Mismatch In Statement: Return(BinaryOp(+,FloatLiteral(1.5),IntLiteral(2)))"
        self.assertTrue(TestChecker.test(input,expect,435))
    def test_return_exp_int_with_var_in_int(self):
        """More complex program"""
        input = """ 
        int foo(){
            int a,b,c;
            return (a+b-c)*1.2;
        }
            void main(){
                    int a;
                    a = 1;
                    return;
                }
            """
        expect = "Type Mismatch In Statement: Return(BinaryOp(*,BinaryOp(-,BinaryOp(+,Id(a),Id(b)),Id(c)),FloatLiteral(1.2)))"
        self.assertTrue(TestChecker.test(input,expect,436))

    def test_return_exp_int_with_var_in_float(self):
        """More complex program"""
        input = """ 
        float foo(){
            {
            int a,b,c;
            return (a+b-c)*1.2;
            }
        }
            void main(){
                    int a;
                    a = 1;
                    return;
                }
            """
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input,expect,437))
    def test_return_exp_in_float(self):
        """More complex program"""
        input = """ 
        int foo(){
            {
            int a,b,c;
            return (a+b-c)*1.2;
            }
            int b;
            return b/2;
        }
            void main(){
                    int a;
                    a = 1;
                    return;
                }
            """
        expect = "Type Mismatch In Statement: Return(BinaryOp(*,BinaryOp(-,BinaryOp(+,Id(a),Id(b)),Id(c)),FloatLiteral(1.2)))"
        self.assertTrue(TestChecker.test(input,expect,438))
    def test_return_arraypointer(self):
        """More complex program"""
        input = """ 
        int[] foo(int a){
            return a;
        }
            void main(){
                    int a;
                    a = 1;
                    return;
                }
            """
        expect = "Type Mismatch In Statement: Return(Id(a))"
        self.assertTrue(TestChecker.test(input,expect,439))
    def test_return_arraypointer3(self):
        """More complex program"""
        input = """ 
        int foo(){
            int a[10];
            return a[0] * 1.2;
        }
            void main(){
                    int a;
                    a = 1;
                    return;
                }
            """
        expect = "Type Mismatch In Statement: Return(BinaryOp(*,ArrayCell(Id(a),IntLiteral(0)),FloatLiteral(1.2)))"
        self.assertTrue(TestChecker.test(input,expect,440))
    def test_return_arraypointer132(self):
        """More complex program"""
        input = """ 
        int foo(){
            int a[10];
            return b[0];
        }
            void main(){
                    int a;
                    a = 1;
                    return;
                }
            """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,441))
    def test_return_string_assign323(self):
        """More complex program"""
        input = """ 
        
            void main(){
                    boolean a;
                    string b;
                    a = true;
                    b = "string";
                return 1;
                }
            """
        expect = "Type Mismatch In Statement: Return(IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,442))
    def test_return_unaryop(self):
        """More complex program"""
        input = """ 
        int foo(){
            int a[10];
            return -a[0]*1.2;
        }
            void main(){
                    int a;
                    a = 1;
                    return;
                }
            """
        expect = "Type Mismatch In Statement: Return(BinaryOp(*,UnaryOp(-,ArrayCell(Id(a),IntLiteral(0))),FloatLiteral(1.2)))"
        self.assertTrue(TestChecker.test(input,expect,443))
    def test_return_unaryop_bool(self):
        """More complex program"""
        input = """ 
        boolean foo(){
            boolean a[10];
            return !a[0] && true || false;
        }
        boolean foo1(){
            boolean a[10];
            return (!a[0] && true || false)*3;
        }
            void main(){
                    int a;
                    a = 1;
                    return;
                }
            """
        expect = "Type Mismatch In Expression: BinaryOp(*,BinaryOp(||,BinaryOp(&&,UnaryOp(!,ArrayCell(Id(a),IntLiteral(0))),BooleanLiteral(true)),BooleanLiteral(false)),IntLiteral(3))"
        self.assertTrue(TestChecker.test(input,expect,444))
    def test_dowhile_stmt(self):
        """More complex program"""
        input = """ 
        
            void main(){
                    int a;
                    int b;
                    
                    do{
                        a = a +1;
                        b = b*2;
                        do 
                            a = a*2;
                            b = b +1;
                            c = 0;
                        while a < 9;
                        return 1;
                    } while a < 10;
                    return;
                }
            """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input,expect,445))
    def test_wrong_expr_stmt(self):
        """More complex program"""
        input = """ 
        
            void main(){
                    int a;
                    int b;
                    
                    do{
                       
                    } while (a != 10) == 8 - 2;
                    return;
                }
            """
        expect = "Type Mismatch In Expression: BinaryOp(==,BinaryOp(!=,Id(a),IntLiteral(10)),BinaryOp(-,IntLiteral(8),IntLiteral(2)))"
        self.assertTrue(TestChecker.test(input,expect,446))
    def test_for_stmt(self):
        """More complex program"""
        input = """ 
        
            void main(){
                    int a;
                    int b;
                    int i;
                    for(i = 1; i < 100; i=i+1)
                        a = a+1;
                    
                }
            """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,447))
    def test_example_gloale_var(self):
        """More complex program"""
        input = """ 
        
            void main(){

        foo1() ;

        }



    void foo1(){

    putString("hello world") ;

    }
            """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,448))
    def test_break_in_for(self):
        """More complex program"""
        input = """ 
        
            void main(){
                    int a;
                    int b;
                    int i;
                    for(i = 1; i < 100; i=i+1)
                        break;
                    
                }
            """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,449))
    def test_continue_in_main(self):
        """More complex program"""
        input = """ 
        
            void main(){
                    int a;
                    int b;
                    int i;
                    for(i = 1; i < 100; i=i+1)
                        break;
                    continue;
                    
                }
            """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,450))
    def test_break_in_block_in_for(self):
        """More complex program"""
        input = """ 
        
            void main(){
                    int a;
                    int b;
                    int i;
                    for(i = 1; i < 100; i=i+1){
                        a = a + 1;
                        b = b * 2 ;
                        continue;
                    }
                    a = a * 1.3;
                    return;
                }
            """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),BinaryOp(*,Id(a),FloatLiteral(1.3)))"
        self.assertTrue(TestChecker.test(input,expect,451))
    def test_continue_in_do_while(self):
        """More complex program"""
        input = """ 
        
            void main(){
                    int a;
                    int b;
                    int i;
                    do 
                        a = a * 2;
                        b = b*10;
                        continue; 
                        break;
                    while  b < 100;
                    break;
                    return;
                }
            """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,452))
    def test_continue_in_do_while_block(self):
        """More complex program"""
        input = """ 
        
            void main(){
                    int a;
                    int b;
                    int i;
                    do 
                        a = a * 2;
                        b = b*10;
                        {
                            continue;
                        }
                    while  b < 100;
                    continue;
                    return;
                }
            """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,453))
    def test_return_in_do_while_block(self):
        """More complex program"""
        input = """ 
            int foo(int a, float a){

            }
            void main(){
                    int a;
                    int b;
                    int i;
                    return;
                    
                }
            """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input,expect,454))
    def test_callexpr(self):
        """More complex program"""
        input = """ 
            int foo(int a, float b){
                
                return 10*a;
            }
            void main(){
                    int a;
                    int b;
                    int i;
                    foo(1, true);
                    return;
                    
                }
            """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[IntLiteral(1),BooleanLiteral(true)])"
        self.assertTrue(TestChecker.test(input,expect,455))
    def test_callexpr_float_float(self):
        """More complex program"""
        input = """ 
            int foo(float a, float b){
                
                return 10;
            }
            void main(){
                    int a;
                    int b;
                    int i;
                    foo(100, 150);
                    i = a - 1.1;
                    return;  
                }
            """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(i),BinaryOp(-,Id(a),FloatLiteral(1.1)))"
        self.assertTrue(TestChecker.test(input,expect,456))
    def test_callexpr_booleans(self):
        """More complex program"""
        input = """ 
            boolean foo(boolean a, boolean b){
                
                return true;
            }
            void main(){
                    int a;
                    int b;
                    int i;
                    foo(foo(foo(false,true),false), 1);
                    i = a - 1.1;
                    return;  
                }
            """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[CallExpr(Id(foo),[CallExpr(Id(foo),[BooleanLiteral(false),BooleanLiteral(true)]),BooleanLiteral(false)]),IntLiteral(1)])"
        self.assertTrue(TestChecker.test(input,expect,457))
    def test_callexpr_1(self):
        """More complex program"""
        input = """ 
            boolean foo(boolean a, boolean b){
                
                return true;
            }
            void main(){
                    int a;
                    int b;
                    int i;
                    
                    return;  
                }
            """
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input,expect,458))
    def test_callexpr_elearning(self):
        """More complex program"""
        input = """ 
            int foo(int a){
            return 1;

            }
            void main(){

            foo(b(1));

                }   
            """
        expect = "Undeclared Function: b"
        self.assertTrue(TestChecker.test(input,expect,459))
    def test_return_in_do(self):
        """More complex program"""
        input = """ 
            int foo(int a){
            return 1;

            }
            void main(){
            int a;
            foo(a);
            do{
                return;
            } while a == 1;
            a = a + 1.2;
            }   
            """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),BinaryOp(+,Id(a),FloatLiteral(1.2)))"
        self.assertTrue(TestChecker.test(input,expect,460))
    def test_return_in_do12(self):
        """More complex program"""
        input = """ 
            
            void main(){
           
            }   
            """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,461))
    def test_return_in_do123(self):
        """More complex program"""
        input = """ 
                         

            void main(){
           
            }
            void foo(){
                {
                    {
                        {
                            do {

                            }while 1 == 1;
                        }
                    }
                }
                
            }
            """
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input,expect,462))
    def test_not_left_value(self):
        """More complex program"""
        input = """ 
            void main(){
            3 = 10;
            }
            int foo(){
                
                return 10;
                
            }
            """
        expect = "Not Left Value: IntLiteral(3)"
        self.assertTrue(TestChecker.test(input,expect,463))
    def test_e_learning1(self):
        """More complex program"""
        input = """ 
            void main(){

      int a[5];

        {

            a = 1; 

        }

        }  
            """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,464))
    def test_assign_operator_function(self):
        """More complex program"""
        input = """ 
            void main(){
            int a;
            a = foo(1);
            }
            int foo(int a){
                
                return 10;  
            }
            """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,465))
    def test_assign_operator_function_ppointer(self):
        """More complex program"""
        input = """ 
            void main(){
            int a;
            a = foo(1)[0];
            }
            int[] foo(int a){
                int b[10];
                return b;  
            }
            """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,466))
    def test_assign_operator_function_ppointer_LHS(self):
        """More complex program"""
        input = """ 
            void main(){
            int a;
            foo(1)[0] = 10;
            }
            int[] foo(int a){
                int b[10];
                return b;  
            }
            """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,467))
    def test_reach_fun(self):
        """More complex program"""
        input = """ 
            void main(){
            int a;
            foo(1)[0] = 10;
            }
            int[] foo(int a){
                int b[10];
                return b;  
            }
            void a(){
                b();
            }
            void b(){
                a();
                
            }
            """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,468))
    def test_redeclare_para(self):
        """More complex program"""
        input = """ 
            void main(){
            int a;
            foo(1)[0] = 10;
            }
            int[] foo(int a){
                int b[10];
                return b;  
            }
            void a(int a){
                int a;
            }
            """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,469))
    def test_redeclare_function(self):
        """More complex program"""
        input = """ 
            void main(){
            int a;
            foo(1)[0] = 10;
            }
            int[] foo(int a){
                int b[10];
                return b;  
            }
            int a;
            void a(int a){
                //int a;
            }
            """
        expect = "Redeclared Function: a"
        self.assertTrue(TestChecker.test(input,expect,470))
    def test_redeclare_para_(self):
        """More complex program"""
        input = """ 
            void main(){
            int a;
            foo(1)[0] = 10;
            }
            int[] foo(int a){
                int b[10];
                return b;  
            }
            int a;
            void ab(int a){
                //int a;
            }
            """
        expect = "Unreachable Function: ab"
        self.assertTrue(TestChecker.test(input,expect,471))
    def test_re_para(self):
        input = """
            void main(){a(1,2);}
            int a(int a, float a){}
            """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input,expect,472))
    def test_return_if(self):
        input = """
            void main(){ab(1,2);
            }
            int ab(int a, float b){
                if( a < 1){
                    a = a -1;
                    return 2;
                }
                else
                    b = 1;

            }
            """
        expect = "Function ab Not Return "
        self.assertTrue(TestChecker.test(input,expect,473))
    def test_return_if_in_then_(self):
        input = """
            void main(){ab(1,2);

            }
            int ab(int a, float b){
                if( a < 1)
                    return 2;
                else
                    return a = a + 1;        
            }
            int foo(int c){
                return ab(c, 1.2);
            }
            """
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input,expect,474))
    def test_binary_op_string(self):
        input = """
            void main(){
                boolean a;
                a = !true;
                float b;int c;
                
                b = -c;
                string d,f;
                d = "stromg";
                d == f;

            }
           
            """
        expect = "Type Mismatch In Expression: BinaryOp(==,Id(d),Id(f))"
        self.assertTrue(TestChecker.test(input,expect,475))
    def test_return_if_in_then1(self):
        input = """
            void main(){ab(1,2);

            }
            int ab(int a, float b){

                do{
                     b = b*10;
                     {
                        return 1;
                     }
                } while a ==1;
                    
            }
            """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,476))
    def test_return_if_in_else(self):
        input = """
            void main(){ab(1,2);
            }
            int ab(int a, float b){
                if( a < 1){
                    a = a -1;
                    //return 2;
                }
                else{
                     b = 1;
                     return 1;
                }
                return 2;
                   
            }
            """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,477))
    def test_return__in_while_if(self):
        input = """
            void main(){ab(1,2);
            }
            int ab(int a, float b){
                
                    //int b;
                if( a < 1){
                    a = a + 1;
                    b = b*2;
                    //return 1;
                    
                }
                else{
                    a = 1;
                    return 1;
                    }     
            }
            """
        expect = "Function ab Not Return "
        self.assertTrue(TestChecker.test(input,expect,478))
    def test_return__in_while_if_1(self):
        input = """
            void main(){ab(1,2);
            }
            int ab(int a, float b){
                
                do{
                    int a,b;
                if( a < 1){
                    a = a + 1;
                    b = b*2;
                    //return 1;
                }
                else{
                    a = 1;
                    return 1;
                    }     
                }while a == 1;
            }
            """
        expect = "Function ab Not Return "
        self.assertTrue(TestChecker.test(input,expect,479))
    def test_return_arraypointer_func(self):
        input = """
            void main(){ab();
            }
            int[] ab(){
                float c[10];
               return c;
            }
            """
        expect = "Type Mismatch In Statement: Return(Id(c))"
        self.assertTrue(TestChecker.test(input,expect,480))
    def test_return_arraypointer_func_float(self):
        input = """
            void main(){ab();
            }
            float[] ab(){
                float c[10];
                int d[10];
               return d;
            }
            """
        expect = "Type Mismatch In Statement: Return(Id(d))"
        self.assertTrue(TestChecker.test(input,expect,481))
    def test_undeclare_function__(self):
        input = """
        int ab() {
            return 1;
        }
        int main (int ab)
		{
            
			ab();
            return 1;
		}

            """
        expect = "Type Mismatch In Expression: CallExpr(Id(ab),[])"
        self.assertTrue(TestChecker.test(input,expect,482))
    def test_return_nhatminh(self):
        input = """
       void main() 
        {
        int d[3] ;

        d = 3 ; 
        }

            """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(d),IntLiteral(3))"
        self.assertTrue(TestChecker.test(input,expect,483))
    def test_use_before_declare(self):
        input = """
       void main() 
        {
        {
            a = 1.2;

        }
        float a;
        }

            """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,484))
    def test_re_declare(self):
        input = """
       void main() 
        {
            float a;
        {
            int a;
            a = 1.2;

        }
        
        }
            """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),FloatLiteral(1.2))"
        self.assertTrue(TestChecker.test(input,expect,485))
    def test_do_for(self):
        input = """
       int main() 
        {
           int a, b;
           for( a = 0; a <100 ; a = a+1 ){
               if(a % 2 == 1)
                     a = a*10;
                else{
                    b = b*a;
                    a = a+2;
                }
                do{
                    a = b ;
                    b = b+2;
                    break;
                }while a == 1;
                return 1;
           }
        
        }
            """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,486))
    def test_do_for_return_in_do(self):
        input = """
       int main() 
        {
           int a, b;
           for( a = 0; a <100 ; a = a+1 ){
               if(a % 2 == 1)
                     a = a*10;
                else{
                    b = b*a;
                    a = a+2;
                }
                do{
                    a = b ;
                    b = b+2;
                    break;
                    return a +b;
                }while a == 1;
                return 1;
           }
        
        }
            """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,487))
    def test_not_return(self):
        input = """
       int main() 
        {
            int a,b;
        do{
           if(a < 1)
            return 1;
            else{
                break;
                return 2;
            }
        }while b == 10;

        }
            """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,488))
    def test_var_redeclare(self):
	    input = '''int a;
				int b[5], a[10];
				void main () {}
		'''
	    expect = "Redeclared Variable: a"
	    self.assertTrue (TestChecker.test (input, expect, 489))
    
    def test_func_redeclared (self):
	    input = '''int a () {return 0;}
				void main () {}
				void b () {}
				void a () {}
		'''
	    expect = "Redeclared Function: a"
	    self.assertTrue (TestChecker.test (input, expect, 490))
    def test_not_return_in_for__(self):
        input = """
       int main() 
        {
            int a,b;
        do{
           for(b = 1; b < a; b = b+1)
                return 2;
        }while b == 10;

        }
            """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test (input, expect, 491))
    def test_not_reachable_stmt__(self):
        input = """
       int main() 
        {
            int a,b;
        do{
           for(b = 1; b < a; b = b+1)
                return 2;
            return 4;
        }while b == 10;

        }
        void a(){

        }
            """
        expect = "Unreachable Function: a"
        self.assertTrue(TestChecker.test (input, expect, 492))
    def test_not_reachable_stmt_1(self):
        input = """
       int main() 
        {
            int a,b;
        do{
           for(b = 1; b < a; b = b+1)
                return 2;
            return 4;
        }while b == 10;

        }
        void a(){
            a();
            return;
        }
            """
        expect = "Unreachable Function: a"
        self.assertTrue(TestChecker.test (input, expect, 493))
    def test_undeclare_function_A(self):
        input = """
       int main() 
        {
            int a,b;
            a();
        do{
           for(b = 1; b < a; b = b+1)
                return 2;
            return 4;
        }while b == 10;

        }
        void a(){
            a();
            return;
        }
            """
        expect = "Type Mismatch In Expression: CallExpr(Id(a),[])"
        self.assertTrue(TestChecker.test (input, expect, 494))
    def test__test_reachable_func(self):
        input = """
       int main() 
        {
           a();
           return 1;

        }
        void a(){
            a();
            return;
        }
            """
        expect = ""
        self.assertTrue(TestChecker.test (input, expect, 495))
    def test_correct_assiged_invar(self):
        input = """
        int a,b,c;
        void main(){
            a = b = c = 10;
        }   
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,496))

    def test_correct_assigned(self):
        input = """
        int a,b,c;
        void main(){ 
            a = b = c = (10+3)/4 + 5*9 - 2;
        }   
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,497))

    def test_redecalred_int_main(self):
        input = """
        int foo() {
        return 3;

        }

        void main() {

        foo[3]; 

        }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(foo),IntLiteral(3))"
        self.assertTrue(TestChecker.test(input,expect,498))
    def test_using_func_as_ID(self):
        input = """
       int foo(){
           return 1;
       }
       void main(){
           foo;
           foo();
       }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,499))
    def test_using_func_as_ID1(self):
        input = """
       
       int main(){

           return int;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,500))





