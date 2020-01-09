import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite (unittest.TestCase):
    def test_redeclared_variable_in_global_scope(self):
        input = '''void main () {}
                int a;
                int a;
        '''
        expect = "Redeclared Variable: a"
        self.assertTrue (TestChecker.test (input, expect, 400))

    def test_redeclared_function_in_global_scope (self):
        input = ''' void foo(){}
                void main () {
                    foo();
                }
                void foo(){}

        '''
        expect = "Redeclared Function: foo"
        self.assertTrue (TestChecker.test (input, expect, 401))

    def test_redeclared_variable_in_multi_variable_declaration (self):
        input = ''' int a,b,a;
                void main () {}
        '''
        expect = "Redeclared Variable: a"
        self.assertTrue (TestChecker.test (input, expect, 402))

    def test_redeclared_variable_with_primitive_type_and_array_type (self):
        input = '''int a;
                string a[5];
                void main () {}
        '''
        expect = "Redeclared Variable: a"
        self.assertTrue (TestChecker.test (input, expect, 403))

    def test_redeclared_variable_same_name_as_existed_function(self):
        input = '''void foo(){}
                int foo;
                void main () {
                    foo();
                }
        '''
        expect = "Redeclared Variable: foo"
        self.assertTrue (TestChecker.test (input, expect, 404))

    def test_redeclared_variable_same_name_as_built_in_function (self):
        input = '''int getInt;
                void main () {}
        '''
        expect = "Redeclared Variable: getInt"
        self.assertTrue (TestChecker.test (input, expect, 405))

    def test_redeclared_function_same_name_as_built_in_function (self):
        input = ''' int[] putInt(){}
                void main () {
                    putInt();
                }
        '''
        expect = "Redeclared Function: putInt"
        self.assertTrue (TestChecker.test (input, expect, 406))

    def test_redeclared_function_same_name_as_existed_variable (self):
        input = '''int a;
                void main () { a(); }
                void a(){}
        '''
        expect = "Redeclared Function: a"
        self.assertTrue (TestChecker.test (input, expect, 407))

    def test_redeclared_variable_between_single_and_multi_variable_declaration (self):
        input = ''' int a;
                    float b,c,a;
                    void main(){}
        '''
        expect = "Redeclared Variable: a"
        self.assertTrue (TestChecker.test (input, expect, 408))

    def test_redeclared_parameter (self):
        input = ''' int a,b,c;
                void main () {
                    foo(a,b,c);
                }
                void foo(int a, int b, int a){}
        '''
        expect = "Redeclared Parameter: a"
        self.assertTrue (TestChecker.test (input, expect, 409))

    def test_redeclared_variable_same_name_as_parameter (self):
        input = '''int a,b;
                void foo(int c,int d){
                    {
                        int d;
                    }
                    int c;
                }
                void main () { foo(a,b); }
        '''
        expect = "Redeclared Variable: c"
        self.assertTrue (TestChecker.test (input, expect, 410))

    def test_redeclared_variable_in_function_body (self):
        input = '''int a;
                void main () { foo(); }
                void foo(){
                    int b;
                    boolean b[2];
                }
        '''
        expect = "Redeclared Variable: b"
        self.assertTrue (TestChecker.test (input, expect, 411))

    def test_no_entry_point_with_program_having_no_main_identifier_in_global_scope (self):
        input = '''int a;
        '''
        expect = "No Entry Point"
        self.assertTrue (TestChecker.test (input, expect, 412))

    def test_no_entry_point_with_program_having_variable_main_in_global_scope (self):
        input = '''boolean main;
        '''
        expect = "No Entry Point"
        self.assertTrue (TestChecker.test (input, expect, 413))

    def test_no_entry_point_with_program_having_variable_main_in_local_scope (self):
        input = '''
            void a () {
                int main;
            }
        '''
        expect = "No Entry Point"
        self.assertTrue (TestChecker.test (input, expect, 427))

    def test_unreachable_function_with_only_one_function_declaration (self):
        input = '''
                void foo(){}
                void main(){}
        '''
        expect = "Unreachable Function: foo"
        self.assertTrue (TestChecker.test (input, expect, 414))

    def test_unreachable_function_with_many_function_declaration(self):
        input = '''
                void foo(){}
                void oof(){}
                void main () {
                    foo();
                }
        '''
        expect = "Unreachable Function: oof"
        self.assertTrue (TestChecker.test (input, expect, 415))

    def test_unreachable_function (self):
        input = '''
                void foo(){}
                void oof(){
                    foo();
                }
                void main () {}
        '''
        expect = "Unreachable Function: oof"
        self.assertTrue (TestChecker.test (input, expect, 416))

    def test_unreachable_function_case_one_recursive_function (self):
        input = '''
                void foo(){
                    foo();
                }
                void main(){}
        '''
        expect = "Unreachable Function: foo"
        self.assertTrue (TestChecker.test (input, expect, 417))

    def test_unreachable_function_case_one_recursive_function_but_invoked_by_other_function (self):
        input = '''
                void foo(){
                    foo();
                }
                void oof(){
                    foo();
                }
                void main(){}
        '''
        expect = "Unreachable Function: oof"
        self.assertTrue (TestChecker.test (input, expect, 418))

    def test_unreachable_function_case_two_recursive_function_with_only_one_invoked_by_other_function (self):
        input = '''
                void foo(){
                    foo();
                }
                void oof(){
                    foo();
                    oof();
                }
                void main () {}'''
        expect = "Unreachable Function: oof"
        self.assertTrue (TestChecker.test (input, expect, 419))

    def test_unreachable_function_case_two_recursive_function_with_only_one_invoked_by_main_function(self):
        input = '''void foo(){
                    foo();
                }
                void oof(){
                    oof();
                }
                void main () {
                    oof();
                }'''
        expect = "Unreachable Function: foo"
        self.assertTrue (TestChecker.test (input, expect, 420))

    def test_not_left_value_case_LHS_is_IntLiteral (self):
        input = '''
                int a;
                void main(){
                    a = 2;
                    2 = a;
                }
        '''
        expect = "Not Left Value: IntLiteral(2)"
        self.assertTrue (TestChecker.test (input, expect, 421))

    def test_not_left_value_case_LHS_is_BooleanLiteral (self):
        input = '''
                int a;
                void main(){
                    true = a;
                }
        '''
        expect = "Not Left Value: BooleanLiteral(true)"
        self.assertTrue (TestChecker.test (input, expect, 422))

    def test_not_left_value_case_LHS_is_CallExpr (self):
        input = '''
                void foo(){
                    
                }
                void main(){
                    foo() = 2;
                }
        '''
        expect = "Not Left Value: CallExpr(Id(foo),[])"
        self.assertTrue (TestChecker.test (input, expect, 423))

    def test_not_left_value_case_LHS_is_UnaryOp (self):
        input = '''
                int[] foo(){
                    int b[2];
                    return b;
                }
                int a;
                void main (){
                    foo()[2] = 3;
                    -a = 2;
                }
        '''
        expect = "Not Left Value: UnaryOp(-,Id(a))"
        self.assertTrue (TestChecker.test (input, expect, 424))
    
    def test_not_left_value_case_LHS_is_BinaryOp (self):
        input = '''void main ()
        {
            int a;
            a + 1 = 2;
        }
        '''
        expect = "Not Left Value: BinaryOp(+,Id(a),IntLiteral(1))"
        self.assertTrue (TestChecker.test (input, expect, 425))

    def test_not_left_value_with_some_correct_assignment_of_arraycell (self):
        input = '''void main ()
        {
            int a[5];
            a[2] = 2;
            2 = a[3];
        }
        '''
        expect = "Not Left Value: IntLiteral(2)"
        self.assertTrue (TestChecker.test (input, expect, 426))

    
    
    def test_break_in_scope_level_2_not_in_loop (self):
        input = '''
                void main(){
                    int a;
                    break;
                }
        '''
        expect = "Break Not In Loop"
        self.assertTrue (TestChecker.test (input, expect, 428))
    
    def test_continue_in_scope_level_2_not_in_loop (self):
        input = '''
                void main(){
                    int a;
                    continue;
                }
        '''
        expect = "Continue Not In Loop"
        self.assertTrue (TestChecker.test (input, expect, 429))

    def test_break_in_scope_level_3_not_in_loop (self):
        input = '''
                void main(){
                    int a;
                    {
                        break;
                    }
                }
        '''
        expect = "Break Not In Loop"
        self.assertTrue (TestChecker.test (input, expect, 430))

    def test_continue_in_scope_level_3_not_in_loop (self):
        input = '''
                void main(){
                    float b;
                    {
                        continue;
                    }
                }
        '''
        expect = "Continue Not In Loop"
        self.assertTrue (TestChecker.test (input, expect, 431))
    
    def test_break_in_while_loop_and_continue_not_in_loop (self):
        input = '''
                int a,b;
                void main(){
                    do
                        a = a + b;
                        b = 2*b;
                        break;
                    while a<b;
                    continue;
                }
        '''
        expect = "Continue Not In Loop"
        self.assertTrue (TestChecker.test (input, expect, 432))
    
    def test_continue_in_for_loop_and_break_not_in_loop (self):
        input = '''
                int a,b,c,d;
                void main(){
                    for(a=0;a<10;a = a + 1)
                        if(a%2 == 0) continue;
                    break;
                }
        '''
        expect = "Break Not In Loop"
        self.assertTrue (TestChecker.test (input, expect, 433))

    def test_break_in_nested_for_loop_and_continue_not_in_loop (self):
        input = '''
                int a,b,c,d;
                void main(){
                    for (a = 0; a < 100; a = a + 1){
                        for (b = 0; b < 10; b = b + 1)
                            if ( a*b >= 2000) break;
                        break;
                    }
                    continue;
                }
        '''
        expect = "Continue Not In Loop"
        self.assertTrue (TestChecker.test (input, expect, 434))

    def test_continue_in_nested_while_loop_and_break_not_in_loop (self):
        input = '''
                int a,b,c,d;
                void main(){
                    do
                        do
                            a = a - 1;
                            continue;
                        while b<100;
                        continue;
                    while c<1000;
                    break;
                }
        '''
        expect = "Break Not In Loop"
        self.assertTrue (TestChecker.test (input, expect, 435))

    def test_continue_in_nested_for_while_loop_and_break_not_in_loop (self):
        input = '''
                int a,b,c,d;
                void main(){
                    do
                        for(a=1;a<100;a=b+c){
                            continue;
                        }
                        continue;
                    while d<0;
                    break;
                }
        '''
        expect = "Break Not In Loop"
        self.assertTrue (TestChecker.test (input, expect, 436))

    def test_type_mismatch_in_If_stmt_conditional_expr_is_IntType (self):
        input = '''
                void main(){
                    int a,b;
                    if(a+1) b = 2;
                }
        '''
        expect = "Type Mismatch In Statement: If(BinaryOp(+,Id(a),IntLiteral(1)),BinaryOp(=,Id(b),IntLiteral(2)))"
        self.assertTrue (TestChecker.test (input, expect, 437))

    def test_type_mismatch_in_If_stmt_conditional_expr_is_FloatType (self):
        input = '''
                void main(){
                    float a,b;
                    if(b*2.5) a = 2;
                }
        '''
        expect = "Type Mismatch In Statement: If(BinaryOp(*,Id(b),FloatLiteral(2.5)),BinaryOp(=,Id(a),IntLiteral(2)))"
        self.assertTrue (TestChecker.test (input, expect, 438))

    def test_type_mismatch_in_Dowhile_stmt_conditional_expr_is_FloatType (self):
        input = '''
                void main(){
                    float a;
                    do
                        a = a + 2.5;
                    while a - 1;
                }
        '''
        expect = "Type Mismatch In Statement: Dowhile([BinaryOp(=,Id(a),BinaryOp(+,Id(a),FloatLiteral(2.5)))],BinaryOp(-,Id(a),IntLiteral(1)))"
        self.assertTrue (TestChecker.test (input, expect, 439))
    
    def test_type_mismatch_in_Dowhile_stmt_conditional_expr_is_ArrayType (self):
        input = '''
                void main(){
                    int b;
                    boolean a[5];
                    do 
                        b = 2*b;
                    while a;
                }
        '''
        expect = "Type Mismatch In Statement: Dowhile([BinaryOp(=,Id(b),BinaryOp(*,IntLiteral(2),Id(b)))],Id(a))"
        self.assertTrue (TestChecker.test (input, expect, 440))

    def test_correct_If_stmt_and_type_mismatch_in_Dowhile_stmt_using_boolean_array (self):
        input = '''
                boolean a[2];
                float b;
                void main(){
                    if (a[1]) b = 2;
                    do
                        b = 2*b;
                    while a;
                }
        '''
        expect = "Type Mismatch In Statement: Dowhile([BinaryOp(=,Id(b),BinaryOp(*,IntLiteral(2),Id(b)))],Id(a))"
        self.assertTrue (TestChecker.test (input, expect, 441))

    def test_type_mismatch_in_For_stmt_exp1_is_FloatType (self):
        input = '''
                void main(){
                    float a;
                    int b;
                    for(a = 2.3; a <= 10; b = b + 1)
                        if(b<10) a = a * 2;
                }
        '''
        expect = "Type Mismatch In Statement: For(BinaryOp(=,Id(a),FloatLiteral(2.3));BinaryOp(<=,Id(a),IntLiteral(10));BinaryOp(=,Id(b),BinaryOp(+,Id(b),IntLiteral(1)));If(BinaryOp(<,Id(b),IntLiteral(10)),BinaryOp(=,Id(a),BinaryOp(*,Id(a),IntLiteral(2)))))"
        self.assertTrue (TestChecker.test (input, expect, 442))

    def test_type_mismatch_in_For_stmt_exp1_is_BoolType (self):
        input = '''
                int b;
                void main(){
                    boolean a;
                    for(a = true; b <= 10; b = b + 1)
                        a = !a;
                }
        '''
        expect = "Type Mismatch In Statement: For(BinaryOp(=,Id(a),BooleanLiteral(true));BinaryOp(<=,Id(b),IntLiteral(10));BinaryOp(=,Id(b),BinaryOp(+,Id(b),IntLiteral(1)));BinaryOp(=,Id(a),UnaryOp(!,Id(a))))"
        self.assertTrue (TestChecker.test (input, expect, 443))
    
    def test_type_mismatch_in_For_stmt_exp3_is_StringType (self):
        input = '''
                string s;
                void main(){
                    int a;
                    for(a = 1; a<10; s = "Int") a = a + 1;
                }
        '''
        expect = "Type Mismatch In Statement: For(BinaryOp(=,Id(a),IntLiteral(1));BinaryOp(<,Id(a),IntLiteral(10));BinaryOp(=,Id(s),StringLiteral(Int));BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1))))"
        self.assertTrue (TestChecker.test (input, expect, 444))

    def test_type_mismatch_in_For_stmt_exp2_is_IntType (self):
        input = '''
                int a;
                void main(){
                    int b,c;
                    for (a = 0; b = a + 1; a = a + 2) c = a * b;
                }
        '''
        expect = "Type Mismatch In Statement: For(BinaryOp(=,Id(a),IntLiteral(0));BinaryOp(=,Id(b),BinaryOp(+,Id(a),IntLiteral(1)));BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(2)));BinaryOp(=,Id(c),BinaryOp(*,Id(a),Id(b))))"
        self.assertTrue (TestChecker.test (input, expect, 445))

    def test_type_mismatch_in_For_stmt_exp2_is_FloatType (self):
        input = '''
                int a;
                void main(){
                    float b,c;
                    for (a = 0; b = a * 2; a = a + 1) c = a * b;
                }
        '''
        expect = "Type Mismatch In Statement: For(BinaryOp(=,Id(a),IntLiteral(0));BinaryOp(=,Id(b),BinaryOp(*,Id(a),IntLiteral(2)));BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)));BinaryOp(=,Id(c),BinaryOp(*,Id(a),Id(b))))"
        self.assertTrue (TestChecker.test (input, expect, 446))

    def test_type_mismatch_in_For_stmt_exp2_is_ArrayType (self):
        input = '''
                boolean a[2];
                int d;
                void main(){
                    float b,c;
                    for (a; b = b * b; c = c + 2) d = a * b;
                }
        '''
        expect = "Type Mismatch In Statement: For(Id(a);BinaryOp(=,Id(b),BinaryOp(*,Id(b),Id(b)));BinaryOp(=,Id(c),BinaryOp(+,Id(c),IntLiteral(2)));BinaryOp(=,Id(d),BinaryOp(*,Id(a),Id(b))))"
        self.assertTrue (TestChecker.test (input, expect, 447))

    def test_type_mismatch_in_For_stmt_with_one_correct_For_loop_and_one_incorrect_For_loop (self):
        input = '''
                int a,b,c,d;
                boolean boo;
                void main(){
                    for (a;boo;c) d = d + 1;    //correct
                    for (a;b;c) d = d * 2;      //incorrect
                }
        '''
        expect = "Type Mismatch In Statement: For(Id(a);Id(b);Id(c);BinaryOp(=,Id(d),BinaryOp(*,Id(d),IntLiteral(2))))"
        self.assertTrue (TestChecker.test (input, expect, 448))

    def test_type_mismatch_in_For_stmt_with_one_correct_For_loop_using_CallExpr_and_one_incorrect_For_loop (self):
        input = '''
                int foo(){
                    return 2;
                }
                float fly(){
                    return 3;
                }
                void main(){
                    boolean b;
                    int a;
                    for (foo(); b==true; foo() + 1) b = false;      //correct
                    for (fly(); b == true; a + 1) b = false;        //incorrect 
                }
        '''
        expect = "Type Mismatch In Statement: For(CallExpr(Id(fly),[]);BinaryOp(==,Id(b),BooleanLiteral(true));BinaryOp(+,Id(a),IntLiteral(1));BinaryOp(=,Id(b),BooleanLiteral(false)))"
        self.assertTrue (TestChecker.test (input, expect, 449))

    def test_type_mismatch_in_Return_stmt_void_function_does_not_return_empty (self):
        input = '''
                void main(){
                    return 0;
                }
        '''
        expect = "Type Mismatch In Statement: Return(IntLiteral(0))"
        self.assertTrue (TestChecker.test (input, expect, 450))
    
    def test_type_mismatch_in_Return_stmt_IntType_function_return_FloatType (self):
        input = '''
                float foo(){        //check coercions
                    int a;
                    return a;
                }
                int main(){
                    foo();
                    float b;
                    return b + 1;
                }
        '''
        expect = "Type Mismatch In Statement: Return(BinaryOp(+,Id(b),IntLiteral(1)))"
        self.assertTrue (TestChecker.test (input, expect, 451))

    def test_type_mismatch_in_Return_stmt_BoolType_function_return_StringType (self):
        input = '''
                int[] foo(){            //check ArrayPointerType function accept ArrayType in return stmt with same eleType
                    int a[5];
                    return a;           //OK
                }
                boolean main(){
                    string s;
                    s = "Hello";
                    return s;
                }
        '''
        expect = "Type Mismatch In Statement: Return(Id(s))"
        self.assertTrue (TestChecker.test (input, expect, 452))

    def test_type_mismatch_in_Return_stmt_ArrayPointerType_function_return_ArrayType_with_different_eleType (self):
        input = '''
                float[] foo(){
                    int a[5];
                    return a;       //Error, no coercions allowed
                }
                void main(){
                    foo();
                }
        '''
        expect = "Type Mismatch In Statement: Return(Id(a))"
        self.assertTrue (TestChecker.test (input, expect, 453))

    def test_type_mismatch_in_Return_stmt_ArrayPointerType_function_return_ArrayPointerType_with_different_eleType (self):
        input = '''
                int[] boo(){
                    int a[5];
                    return a;
                }
                float[] foo(){
                    return boo();
                }
                void main(){
                    foo();
                }
        '''
        expect = "Type Mismatch In Statement: Return(CallExpr(Id(boo),[]))"
        self.assertTrue (TestChecker.test (input, expect, 454))

    def test_type_mismatch_in_Return_stmt_IntType_function_but_return_empty (self):
        input = '''
                int main(){
                    return;
                }
        '''
        expect = "Type Mismatch In Statement: Return()"
        self.assertTrue (TestChecker.test (input, expect, 455))

    def test_type_mismatch_in_Return_stmt_ArrayPointerType_function_but_return_empty (self):
        input = '''
                void main(){
                    foo();
                }
                boolean[] foo(){
                    return;
                }
        '''
        expect = "Type Mismatch In Statement: Return()"
        self.assertTrue (TestChecker.test (input, expect, 456))

    def test_type_mismatch_in_Assignment_exp_LHS_is_ArrayType (self):
        input = '''
                void main(){
                    int a[5];
                    a = 2;
                }
        '''
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),IntLiteral(2))"
        self.assertTrue (TestChecker.test (input, expect, 457))

    def test_type_mismatch_in_Assignment_exp_LHS_is_IntType_and_RHS_is_FloatType (self):
        input = '''
                void main(){
                    int a,c;
                    float b;
                    a = c;      //check assigment with same type int,no error
                    b = a;      //check coercions, no error
                    a = b;      //error
                }
        '''
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),Id(b))"
        self.assertTrue (TestChecker.test (input, expect, 458))

    def test_type_mismatch_in_Assignment_exp_LHS_is_BoolType_and_RHS_is_StringType (self):
        input = '''
                void main(){
                    boolean b,c;
                    string s;
                    b = c;      //check assignment with same type boolean, no error
                    s = "Hello";
                    b = s;      //error
                }
        '''
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(b),Id(s))"
        self.assertTrue (TestChecker.test (input, expect, 459))

    def test_type_mismatch_in_Assignment_exp_LHS_is_StringType_and_RHS_is_BoolType (self):
        input = '''
                void main(){
                    string s;
                    boolean b;
                    s = b;
                }
        '''
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(s),Id(b))"
        self.assertTrue (TestChecker.test (input, expect, 460))

    def test_type_mismatch_in_Assignment_exp_LHS_is_IntType_and_RHS_is_BoolType (self):
        input = '''
                void main(){
                    int a;
                    boolean b;
                    a = b;
                }
        '''
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),Id(b))"
        self.assertTrue (TestChecker.test (input, expect, 461))

    def test_type_mismatch_in_Assignment_exp_LHS_is_FloatType_and_RHS_is_StringType (self):
        input = '''
                void main(){
                    float f;
                    string s;
                    f = s;
                }
        '''
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(f),Id(s))"
        self.assertTrue (TestChecker.test (input, expect, 462))

    def test_type_mismatch_in_UnaryOp_with_operator_not_and_IntType (self):
        input = '''
                void main(){
                    int a;
                    a = 5;
                    !a;
                }
        '''
        expect = "Type Mismatch In Expression: UnaryOp(!,Id(a))"
        self.assertTrue (TestChecker.test (input, expect, 463))

    def test_type_mismatch_in_UnaryOp_with_operator_not_and_FloatType (self):
        input = '''
                void main(){
                    float a;
                    boolean b;
                    a = 5;
                    !b;         //check operator not and booltype, no error
                    !a;
                }
        '''
        expect = "Type Mismatch In Expression: UnaryOp(!,Id(a))"
        self.assertTrue (TestChecker.test (input, expect, 464))

    def test_type_mismatch_in_UnaryOp_with_operator_not_and_StringType (self):
        input = '''
                void main(){
                    string s;
                    s = "hello";
                    !s;
                }
        '''
        expect = "Type Mismatch In Expression: UnaryOp(!,Id(s))"
        self.assertTrue (TestChecker.test (input, expect, 465))

    def test_type_mismatch_in_UnaryOp_with_operator_negation_and_StringType (self):
        input = '''
                void main(){
                    string s;
                    s = "hi";
                    -s;
                }
        '''
        expect = "Type Mismatch In Expression: UnaryOp(-,Id(s))"
        self.assertTrue (TestChecker.test (input, expect, 466))

    def test_type_mismatch_in_UnaryOp_with_operator_negation_and_BoolType (self):
        input = '''
                void main(){
                    boolean b;
                    -b;
                }
        '''
        expect = "Type Mismatch In Expression: UnaryOp(-,Id(b))"
        self.assertTrue (TestChecker.test (input, expect, 467))

    def test_type_mismatch_in_BinaryOp_with_operator_mod_and_two_FloatType_operands (self):
        input = '''
                void main(){
                    float a,b;
                    a = a % b;      //error a % b
                }
        '''
        expect = "Type Mismatch In Expression: BinaryOp(%,Id(a),Id(b))"
        self.assertTrue (TestChecker.test (input, expect, 468))

    def test_type_mismatch_in_BinaryOp_with_operator_mod_and_left_is_IntType_right_is_FloatType (self):
        input = '''
                void main(){
                    int a,b;
                    float h;
                    a = a % b;          //check mod with IntType, correct
                    a = b % h;          //error b % h
                }
        '''
        expect = "Type Mismatch In Expression: BinaryOp(%,Id(b),Id(h))"
        self.assertTrue (TestChecker.test (input, expect, 469))

    def test_type_mismatch_in_BinaryOp_with_operator_mod_and_left_is_BoolType_right_is_StringType (self):
        input = '''
                void main(){
                    boolean b;
                    string h;
                    b % h;
                }
        '''
        expect = "Type Mismatch In Expression: BinaryOp(%,Id(b),Id(h))"
        self.assertTrue (TestChecker.test (input, expect, 470))

    def test_type_mismatch_in_BinaryOp_with_operator_AND_and_left_is_IntType_right_is_BoolType (self):
        input = '''
                void main(){
                    boolean b,c;
                    int a;
                    b = b && c;             //check AND with 2 booltype operand
                    c = a && b;             //error a && b
                }
        '''
        expect = "Type Mismatch In Expression: BinaryOp(&&,Id(a),Id(b))"
        self.assertTrue (TestChecker.test (input, expect, 471))

    def test_type_mismatch_in_BinaryOp_with_operator_OR_and_left_is_BoolType_right_is_FloatType (self):
        input = '''
                void main(){
                    float f;
                    boolean b,c;
                    b = b || c;             //check OR with 2 booltype operand
                    c = b || f;             //error b || f
                }
        '''
        expect = "Type Mismatch In Expression: BinaryOp(||,Id(b),Id(f))"
        self.assertTrue (TestChecker.test (input, expect, 472))

    def test_type_mismatch_in_BinaryOp_with_operator_EQUAL_and_two_FloatType_operand (self):
        input = '''
                void main(){
                    int a,b;
                    boolean c,d;
                    float f,g;
                    a == b;         //check == with 2 IntType
                    c == d;         //check == with 2 BoolType
                    f == g;         //error
                }
        '''
        expect = "Type Mismatch In Expression: BinaryOp(==,Id(f),Id(g))"
        self.assertTrue (TestChecker.test (input, expect, 473))

    def test_type_mismatch_in_BinaryOp_with_operator_EQUAL_and_left_is_IntType_right_is_BoolType (self):
        input = '''
                void main(){
                    int a;
                    boolean b;
                    a == b;     //error
                }
        '''
        expect = "Type Mismatch In Expression: BinaryOp(==,Id(a),Id(b))"
        self.assertTrue (TestChecker.test (input, expect, 474))

    def test_type_mismatch_in_BinaryOp_with_operator_NOT_EQUAL_and_left_is_IntType_right_is_BoolType (self):
        input = '''
                float a;
                int b;
                void main(){
                    int a,c;
                    boolean b,d;
                    a != c;         //check != with 2 IntType
                    b != d;         //check != with 2 BoolType
                    a != b;         //error
                }
        '''
        expect = "Type Mismatch In Expression: BinaryOp(!=,Id(a),Id(b))"
        self.assertTrue (TestChecker.test (input, expect, 475))

    def test_type_mismatch_in_BinaryOp_with_operator_NOT_EQUAL_and_two_FloatType_operand (self):
        input = '''
                boolean b;
                void main(){
                    float a,b;
                    a != b;     //error
                }
        '''
        expect = "Type Mismatch In Expression: BinaryOp(!=,Id(a),Id(b))"
        self.assertTrue (TestChecker.test (input, expect, 476))

    def test_type_mismatch_in_BinaryOp_with_four_COMPARE_operator (self):
        input = '''
                float a;
                void main(){
                    int a,b;
                    float c,d;
                    boolean h;

                    //check with same type
                    a > b;
                    a < b;
                    a >=b;
                    a <= b;
                    c > d;
                    c >= d;
                    c < d;
                    c <= d;

                    //check coercions
                    a < c;     
                    d >= b;

                    a <= h;     //error
                }
        '''
        expect = "Type Mismatch In Expression: BinaryOp(<=,Id(a),Id(h))"
        self.assertTrue (TestChecker.test (input, expect, 477))

    def test_type_mismatch_in_BinaryOp_with_four_MATHEMATIC_operator (self):
        input = '''
                void main(){
                    int a,b;
                    float c,d;
                    string h;

                    //check with same type
                    a + b;
                    a - b;
                    a * b;
                    a / b;
                    c + d;
                    c - d;
                    c / d;
                    c * d;

                    //check coercions
                    a + c;     
                    d / b;

                    a + h;      //error
                }
        '''
        expect = "Type Mismatch In Expression: BinaryOp(+,Id(a),Id(h))"
        self.assertTrue (TestChecker.test (input, expect, 478))

    def test_type_mismatch_in_ArrayCell_index_type_is_FloatType (self):
        input = '''
                void main(){
                    int a[5];
                    a[1];       // a is ArrayType, 1 is IntType, no error
                    a[2.50];    //error
                }
        '''
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),FloatLiteral(2.5))"
        self.assertTrue (TestChecker.test (input, expect, 479))

    def test_type_mismatch_in_ArrayCell_Identifier_is_IntType_not_ArrayType (self):
        input = '''
                void main(){
                    int b;
                    b[1];       //error, b is IntType, not ArrayType
                }
        '''
        expect = "Type Mismatch In Expression: ArrayCell(Id(b),IntLiteral(1))"
        self.assertTrue (TestChecker.test (input, expect, 480))

    def test_type_mismatch_in_ArrayCell_with_ArrayPointerType (self):
        input = '''
                float[] foo(){
                    float a[5];
                    return a;
                }
                int oof(){
                    return 2;
                }
                void main(){
                    foo()[2];       //foo is ArrayPointerType, 2 is IntType, no error
                    oof()[2];       //oof is not ArrayPointerType, error
                }
        '''
        expect = "Type Mismatch In Expression: ArrayCell(CallExpr(Id(oof),[]),IntLiteral(2))"
        self.assertTrue (TestChecker.test (input, expect, 481))

    def test_type_mismatch_in_function_call_with_different_number_of_parameters (self):
        input = '''
                void foo(int a, int b){}    //foo has 2 params
                void main(){
                    int a;
                    foo(a);     //call foo with only 1 param, error
                }
        '''
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[Id(a)])"
        self.assertTrue (TestChecker.test (input, expect, 482))

    def test_type_mismatch_in_function_call_with_wrong_param_type_case_IntType_and_FloatType (self):
        input = '''
                void foo(int a, float b){}
                void main(){
                    float a,b;
                    int c;

                    foo(c,c);       //check coercions on 2nd param
                    foo(a,b);       //first param of foo is IntType, can't pass FloatType, error
                }
        '''
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[Id(a),Id(b)])"
        self.assertTrue (TestChecker.test (input, expect, 483))

    def test_type_mismatch_in_function_call_passing_ArrayType_to_ArrayPointerType_but_different_eleType (self):
        input = '''
                void foo(int a[], boolean b[]){}
                void main(){
                    int a[2];
                    boolean b[5];
                    float f[10];
                    foo(a,b);       //check same eleType, correct
                    foo(a,f);       //error
                }
        '''
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[Id(a),Id(f)])"
        self.assertTrue (TestChecker.test (input, expect, 484))
    
    def test_function_not_return_with_one_Ifnoelse_stmt (self):
        input = '''
                int a;  //line 1
                void main(){
                    foo();
                }
                int foo(){
                    { float a; }    //line 5
                    a = a / 2;          //variable a is a in line 1, not line 5
                    if (a == 5) return a;
                    a = a + 1;
                }
        '''
        expect = "Function foo Not Return "
        self.assertTrue (TestChecker.test (input, expect, 485))

    def test_function_not_return_with_one_Ifelse_stmt_but_return_in_then_branch_only (self):
        input = '''
            boolean main(){
                int a;
                foo();
                do
                    a = a + 1;
                    return true;
                while(a < 100);
            }

            float foo(){
                boolean b;
                if(b) return 1.0;
                else {
                    b = !b;
                }
            }
        '''
        expect = "Function foo Not Return "
        self.assertTrue (TestChecker.test (input, expect, 486))
    
    def test_function_not_return_with_one_Ifnoelse_and_one_Ifelse_stmt (self):
        input = '''
                int i,a;
                float main(){
                    foo();
                    for (i = 0; i<5; i = i + 1){
                        a = a * i;
                        return 0.5;
                    }
                }
                boolean foo(){
                    int a;
                    if(true) a = 1;
                    else return false;
                    int b;
                    if (b == 1) return true;
                }
        '''
        expect = "Function foo Not Return "
        self.assertTrue (TestChecker.test (input, expect, 487))

    def test_function_not_return_with_two_functions_and_2_nested_If (self):
        input = '''
                int main(){
                    foo();
                    oof();
                    { return 0; }
                }

                string foo(){                   //foo has return on all paths
                    string s1,s2;
                    boolean b,c;
                    if(b) {
                        if(c) return s1;
                        else s2 = "Hello";
                    }
                    else{
                        if(c) return s2;
                        else return s1;
                    }
                    return s1;                  //this return appears in all paths
                }

                int oof(){
                    int a,b;
                    if(a == 5){
                        if(b==6) return 1;
                        else b = b * 2;            //this path has no return -> oof not return
                    }
                    else{
                        if(b==3) return 2;
                        else return 3;
                    }
                }
        '''
        expect = "Function oof Not Return "
        self.assertTrue (TestChecker.test (input, expect, 488))

    def test_function_not_return_with_multiple_nested_Ifelse_stmt (self):
        input = '''
            float a;
            boolean b,c,d;
            float foo(){
                if(b){
                    if(c){
                        if(d){
                            return a;
                        }
                        else{
                            a = a - 1;
                        }
                        return a - 2;
                    }
                    else{
                        if(!d){
                            a = a * 2;
                        }
                        else{
                            a = a / 3;
                        }
                        return a * 5;
                    }
                }

                else{
                    if(!c){
                        if(d){
                            a = a + 7;
                        }
                        else{
                            a = a - 100;
                        }
                    }
                    else{
                        if(!d){
                            a = a * 8;
                        }
                        else{
                            a = a / 5;
                        }
                    }
                    return a * 2;
                }

            }
            int main(){         //main does not have return
                foo();
            }
        '''
        expect = "Function main Not Return "
        self.assertTrue (TestChecker.test (input, expect, 489))

    def test_test_function_not_return_with_multiple_nested_Ifelse_and_Ifnoelse_stmt (self):
        input = '''
            float a;
            boolean b,c,d;
            float foo(){                
                if(b){
                    if(c){
                        if(d){
                            return a;
                        }
                        return a - 2;
                    }
                    else{
                        if(!d){
                            a = a * 2;
                        }
                        else{
                            a = a / 3;
                        }
                        return a * 5;
                    }
                }

                else{
                    if(!c){
                        if(d){
                            return a + 7;
                        }
                        else{
                            return a - 100;
                        }
                    }
                    else{                           //this path does not have return
                        if(!d){
                            a = a * 8;
                            return a;
                        }
                        
                    }
                }

            }
            void main(){         
                foo();
            }
        '''
        expect = "Function foo Not Return "
        self.assertTrue (TestChecker.test (input, expect, 490))

    def test_undeclared_identifier_without_any_declaration (self):
        input = '''
                void main(){
                    a = 2;
                }
        '''
        expect = "Undeclared Identifier: a"
        self.assertTrue (TestChecker.test (input, expect, 491))

    def test_undeclared_identifier_with_declaration_but_in_another_function (self):
        input = '''
                void foo(){
                    int a;
                }
                void main(){
                    b = 3;          //no error, b is declared in global scope
                    a = 2;          //error
                    foo();
                }
                float b;
        '''
        expect = "Undeclared Identifier: a"
        self.assertTrue (TestChecker.test (input, expect, 492))

    def test_undeclared_identifier_with_declaration_but_after_use (self):
        input = '''
                void main(){
                    a = 2;
                    int a;
                }
        '''
        expect = "Undeclared Identifier: a"
        self.assertTrue (TestChecker.test (input, expect, 493))

    def test_undeclared_identifier_with_declaration_but_in_another_scope_level (self):
        input = '''
                void main(){
                    {int a;}
                    a = 2;
                }
        '''
        expect = "Undeclared Identifier: a"
        self.assertTrue (TestChecker.test (input, expect, 494))

    def test_undeclared_function (self):
        input = '''
                void main(){
                    oof();      //no error, oof is declared under main
                    foo();      //error
                }
                void oof(){}
        '''
        expect = "Undeclared Function: foo"
        self.assertTrue (TestChecker.test (input, expect, 495))

    def test_use_function_name_as_variable (self):
        input = '''
                void foo(){}
                void main(){
                    foo();
                    foo + 1;
                }
        '''
        expect = "Type Mismatch In Expression: Id(foo)"
        self.assertTrue (TestChecker.test (input, expect, 496))

    def test_use_variable_name_to_call_function (self):
        input = '''
                int foo;
                void main(){
                    foo();
                }
        '''
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[])"
        self.assertTrue (TestChecker.test (input, expect, 497))

    def test_use_function_name_as_ArrayCell (self):
        input = '''
                void foo(){}
                void main(){
                    foo();
                    foo[3];
                }
        '''
        expect = "Type Mismatch In Expression: ArrayCell(Id(foo),IntLiteral(3))"
        self.assertTrue (TestChecker.test (input, expect, 498))

    def test_use_ArrayType_variable_to_call_function (self):
        input = '''
                int foo[3];
                void main(){
                    foo();
                }
        '''
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[])"
        self.assertTrue (TestChecker.test (input, expect, 499))

