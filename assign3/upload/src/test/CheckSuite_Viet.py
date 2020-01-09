import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):

    def test_legit_redeclared_local_variable(self):
        input = """
                int id;
                void main() {
                    int id;
                }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_legit_redeclared_variable_in_block(self):
        input = """
                void main() {
                    int id;
                    {
                    int id;
                    }
                }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,402))

    def test_redeclared_variable(self):
        input = """
                int a;
                int a;
                void main() {}
                """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test_redeclared_variable_in_function_body(self):
        input = """
                void main() {
                    int a;
                    int a;
                }
                """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 404))

    def test_redeclared_variable_in_function_param(self):
        input = """
                void main(int b, float b) {}
                """
        expect = "Redeclared Parameter: b"
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_legit_redeclared_variable_in_different_functions(self):
        input = """
                void foo(){
                    float a;
                }
                void main() {
                    foo();
                    float a;
                }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 406))

    def test_redeclare_parameter_in_function_body(self):
        input = """
                void main(float a) {
                    int a;
                }
                """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 407))

    def test_legit_redeclared_variables_in_different_scopes(self):
        input = """
                int a;
                void foo() {
                    int a;
                }
                void main() {
                    foo();
                    {
                        int a;
                        {
                        int a;
                        }
                    }
                    int a;
                }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 408))

    def test_redeclared_variable_in_block(self):
        input = """
                void main() {
                    {
                    int a;
                    int a;
                    }
                }
                """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 409))

    def test_redeclared_variable_in_while_stmt(self):
        input = """
                void main() {
                    do
                    {
                    int a;
                    int a;
                    }
                    while
                    false;
                }
                """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 410))

    def test_undeclared_identifier(self):
        input = """
                void main() {
                    a;
                }
                """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 411))

    def test_undeclared_Function(self):
        input = """
                void main() {
                    a();
                }
                """
        expect = "Undeclared Function: a"
        self.assertTrue(TestChecker.test(input, expect, 412))

    def test_declared_Function(self):
        input = """
                void a() {}
                void main() {
                    a();
                }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 413))

    def test_declared_variable_in_global(self):
        input = """
                float a;
                void main() {
                    a;
                }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 414))

    def test_declared_variable_in_parameter(self):
        input = """
                void main(int a) {
                    a;
                }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 415))

    def test_declared_variable_in_outer_scope(self):
        input = """
                void main() {
                    int a;
                    {
                        a;
                    }
                }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 416))

    def test_undeclared_variable_in_inner_scope(self):
        input = """
                void main() {
                    {
                        int a;
                    }
                    a;
                }
                """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 417))

    def test_type_mismatch_in_statement_if(self):
        input = """
                void main() {
                    if(3) 3; else 3;
                }
                """
        expect = "Type Mismatch In Statement: If(IntLiteral(3),IntLiteral(3),IntLiteral(3))"
        self.assertTrue(TestChecker.test(input, expect, 418))

    def test_type_match_in_statement_if(self):
        input = """
                void main() {
                    if (true) 3; else 3;
                }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 419))

    def test_type_match_return_Int(self):
        input = """
                int main() {
                    return 3;
                }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 420))

    def test_type_match_return_Float(self):
        input = """
                float main() {
                    return 5.2;
                }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 421))

    def test_type_match_return_String(self):
        input = """
                string main() {
                    return "viet";
                }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 422))

    def test_type_matched_return_Boolean(self):
        input = """
                boolean main() {
                    return false;
                }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 423))

    def test_type_matched_return_ArrayPointer(self):
        input = """
                int[] main() {
                    int a[3];
                    return a;
                }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 424))

    def test_type_mismatch_return(self):
        input = """
                int main() {
                    return 3.0;
                 }
                """
        expect = "Type Mismatch In Statement: Return(FloatLiteral(3.0))"
        self.assertTrue(TestChecker.test(input, expect, 425))

    def test_type_mismatch_do_while_statement(self):
        input = """
                void main() {
                    do 3; 4; while 3;
                }
                """
        expect = "Type Mismatch In Statement: Dowhile([IntLiteral(3),IntLiteral(4)],IntLiteral(3))"
        self.assertTrue(TestChecker.test(input, expect, 426))

    def test_type_match_do_while_statement(self):
        input = """
                void main() {
                    do 3; 4; while true;
                 }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 427))

    def test_type_mismatch_for_statement_first_express_not_int(self):
        input = """
                void main() {
                    for (3.0;true;3) 3;
                }
                """
        expect = "Type Mismatch In Statement: For(FloatLiteral(3.0);BooleanLiteral(true);IntLiteral(3);IntLiteral(3))"
        self.assertTrue(TestChecker.test(input, expect, 428))


    def test_type_mismatch_for_statement_second_expression_not_bool(self):
        input = """
                void main() {
                    for (1;2;3) 3;
                }
                """
        expect = "Type Mismatch In Statement: For(IntLiteral(1);IntLiteral(2);IntLiteral(3);IntLiteral(3))"
        self.assertTrue(TestChecker.test(input, expect, 429))

    def test_type_mismatch_for_statement_third_expression_not_int(self):
        input = """
                void main() {
                    for (1;true;true) 3;
                }
                """
        expect = "Type Mismatch In Statement: For(IntLiteral(1);BooleanLiteral(true);BooleanLiteral(true);IntLiteral(3))"
        self.assertTrue(TestChecker.test(input, expect, 430))

    def test_for_statement(self):
        input = """
                void main() {
                    for (1;true;3) 3;
                }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 431))

    def test_assign_statement_int(self):
        input = """void main() {
            int a;
            a = 3;
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 432))

    def test_assign_statement_Float(self):
        input = """void main() {
            float b;
            b = 3.0;
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 433))

    def test_assign_statement_String(self):
        input = """void main() {
            string b;
            b = "viet";
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 434))

    def test_assign_statement_Bool(self):
        input = """void main() {
            boolean b;
            b = true;
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 435))

    def test_type_mismatch_in_assign_statement_float_to_int(self):
        input = """void main() {
            int b;
            b = 3.0;
        }"""
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(b),FloatLiteral(3.0))"
        self.assertTrue(TestChecker.test(input, expect, 436))

    def test_type_mismatch_in_assign_statement_int_to_boolean(self):
        input = """void main() {
            boolean b;
            b = 1;
        }"""
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(b),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input, expect, 437))

    def test_type_mismatch_in_assign_statement_int_to_string(self):
        input = """void main() {
            string b;
            b = 123;
        }"""
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(b),IntLiteral(123))"
        self.assertTrue(TestChecker.test(input, expect, 438))

    def test_assign_statement_int_to_float_coerce(self):
        input = """void main() {
            float b;
            b = 3;
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 439))

    def test_assign_statement_coerce_in_operator(self):
        input = """void main() {
            float b;
            b = 3 + 2.0;
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 440))

    def test_function_call(self):
        input = """
        int foo(int a, int b){
            return a+b;
        }
        void main() {
            foo(2,3);
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 441))

    def test_type_mismatched_param_function_call_Float_to_Int(self):
        input = """
        int foo(int a, int b){
            return a+b;
        }
        void main() {
            foo(2,3.2);
        }"""
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[IntLiteral(2),FloatLiteral(3.2)])"
        self.assertTrue(TestChecker.test(input, expect, 442))

    def test_param_function_call_Int_to_Float_coerce(self):
        input = """
        int foo(int a, float b){
            return a;
        }
        void main() {
            foo(2, 3);
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 443))

    def test_param_function_call_ArrayType(self):
        input = """
        int foo(int a[], float b){
            return 3;
        }
        void main() {
            int a[3];
            foo(a, 3);
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 444))

    def test_type_mismatched_param_function_call_different_eleType(self):
        input = """
        int foo(float a[], float b){
            return 3;
        }
        void main() {
            int a[3];
            foo(a, 3);
        }"""
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[Id(a),IntLiteral(3)])"
        self.assertTrue(TestChecker.test(input, expect, 445))

    def test_param_function_call_ArrayPointerType(self):
        input = """
        int foo(float a[], float b){
            return 3;
        }
        float[] foo2(float f[]) {
            return f;
        }
        void main() {
            float a[3];
            foo(foo2(a), 3);
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 446))

    def test_function_invoked_by_itself(self):
        input = """
        void foo() {
            foo();
        }
        void main() {
        }"""
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 447))

    def test_type_mismatch_array_cell_value(self):
        input = """
        void main() {
            int a[3];
            a[2] = 3.0;
        }"""
        expect = "Type Mismatch In Expression: BinaryOp(=,ArrayCell(Id(a),IntLiteral(2)),FloatLiteral(3.0))"
        self.assertTrue(TestChecker.test(input, expect, 448))

    def test_type_mismatch_array_cell_int_type_E1(self):
        input = """
        void main() {
            int a;
            a[2];
        }"""
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),IntLiteral(2))"
        self.assertTrue(TestChecker.test(input, expect, 449))

    def test_type_mismatch_array_cell_float_type_E1(self):
        input = """
        void main() {
            float a;
            a[2];
        }"""
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),IntLiteral(2))"
        self.assertTrue(TestChecker.test(input, expect, 450))

    def test_type_match_array_cell_array_type_E1(self):
        input = """
        void main() {
            int a[3];
            a[2];
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 451))

    def test_type_match_array_cell_arrayPointer_type_E1(self):
        input = """
        int[] foo(int a[]){
            return a;
        }
        void main() {
            int a[3];
            foo(a)[2];
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 452))

    def test_type_mismatch_array_cell_string_type_E2(self):
        input = """
        void main() {
            int a[3];
            a["one"];
        }"""
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),StringLiteral(one))"
        self.assertTrue(TestChecker.test(input, expect, 453))

    def test_type_mismatch_array_cell_float_type_E2(self):
        input = """
        void main() {
            int a[3];
            a[2.0];
        }"""
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),FloatLiteral(2.0))"
        self.assertTrue(TestChecker.test(input, expect, 454))

    def test_type_mismatch_unary_operator_wrong_type(self):
        input = """
        void main() {
            boolean a;
            a = true;
            -a;
        }"""
        expect = "Type Mismatch In Expression: UnaryOp(-,Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 455))

    def test_type_match_complex_expression(self):
        input = """
        void main() {
            boolean a;
            a = false || (3 > 1);
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 456))

    def test_type_match_complex_expression2(self):
        input = """
        void main() {
            int a;
            a = 3+ 5 * (2-7)/3;
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 457))


    def test_Function_not_return(self):
        input = """
        int main(){
        }"""
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input, expect, 458))

    def test_Function_return_in_block(self):
        input = """
        int main(){
            {
                return 1;
            }
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 459))

    def test_Function_return_in_do_stmt(self):
        input = """
           int main(){
               do return 3; while false;
           }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 460))

    def test_void_type_Function_return_nothing(self):
        input = """
           void main(){
               return;
           }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 461))

    def test_return_in_if_else_statement(self):
        input = """
           int main(){
              if (true) return 3; else return 3; 
           }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 462))

    def test_function_not_return_return_only_in_if(self):
        input = """
           int main(){
              if (true) return 3;
           }"""
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input, expect, 463))

    def test_return_in_multi_blocks(self):
        input = """
           int main(){
                {
                    {
                    return 3;
                    }
                }
           }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 464))

    def test_return_in_for_statement(self):
        input = """
           int main(){
                for (1; true; 3) return 3;
           }"""
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input, expect, 465))

    def test_Break_not_in_loop(self):
        input = """
            void main(){
               break;
            }"""
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 466))

    def test_Continue_not_in_loop(self):
        input = """
            void main(){
               continue;
            }"""
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 467))

    def test_break_in_loop(self):
        input = """
            void main(){
               do break; while false;
            }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 468))

    def test_break_in_block_in_loop(self):
        input = """
            void main(){
               do {break;} while false;
            }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 469))

    def test_continue_in_block_in_loop(self):
        input = """
            void main(){
               for (1;true;2) {continue;}
            }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 470))

    def test_break_in_if_statement_in_loop(self):
        input = """
            void main(){
               for (1;true;2) {if (true) break;}
            }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 471))

    def test_break_in_if_statement_in_loop_2(self):
        input = """
            void main(){
               for (1;true;2) {if (true) {{break;}} }
            }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 472))

    def test_no_entry_point(self):
        input = """
            int a;
            """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 473))

    def test_unreachable_function(self):
        input = """
            int foo() {
                return 3;
            }
            void main() {
            }
            """
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 474))

    def test_invoke_function(self):
        input = """
            int foo() {
                return 3;
            }
            int foo2(){
                foo();
                return 1;
            }
            void main() {
                foo2();
            }
            """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 475))

    def test_invoke_function_in_block(self):
        input = """
            int foo() {
                return 3;
            }
            void main() {
                {
                foo();
                }
            }
            """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 476))

    def test_invoke_function_in_statement(self):
        input = """
            int foo() {
                return 3;
            }
            int foo2(){
                return 4;
            }
            int foo3() {
                return 5;
            }
            void main() {
                if (false) foo();
                do foo2(); while true;
                for (1;false;3) foo3();
            }
            """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 477))

    def test_not_left_value_int_lit(self):
        input = """
            void main() {
                3 = 5+7;
            }
            """
        expect = "Not Left Value: IntLiteral(3)"
        self.assertTrue(TestChecker.test(input, expect, 478))

    def test_not_left_value_float_lit(self):
        input = """
            void main() {
                3.0 = 5+7;
            }
            """
        expect = "Not Left Value: FloatLiteral(3.0)"
        self.assertTrue(TestChecker.test(input, expect, 479))

    def test_not_left_value_call_expression(self):
        input = """
            int[] foo(int a[]) {
                return a;
            }
            void main() {
                int a[3];
                foo(a) = 5+7;
            }
            """
        expect = "Not Left Value: CallExpr(Id(foo),[Id(a)])"
        self.assertTrue(TestChecker.test(input, expect, 480))

    def test_undeclared_variable_with_declared_functions_name(self):
        input = """
            int a() {
                return 3;
            }
            void main() {
                a;
            }
            """
        expect = "Type Mismatch In Expression: Id(a)"
        self.assertTrue(TestChecker.test(input, expect, 481))

    def test_type_mismatch_function_with_declared_variable_name(self):
        input = """
            int a;
            void main() {
                a();
            }
            """
        expect = "Type Mismatch In Expression: CallExpr(Id(a),[])"
        self.assertTrue(TestChecker.test(input, expect, 482))

    def test_declare_global_function_after_invoke(self):
        input = """
            void main() {
                a();
            }
            void a(){
            }
            """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 483))

    def test_declare_global_variable_after_assign(self):
        input = """
            void main() {
                a = 3;
            }
            int a;
            """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 484))

    def test_local_variable_assign(self):
        input = """
            int a;
            void main() {
                float a;
                a = 3.5;
            }
            """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 485))

    def test_local_variable_with_global_function_name(self):
        input = """
            int a() {
                return 3;
            }
            void main() {
                a();
                float a;
                a = 3.5;
            }
            """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 486))

    def test_current_scope_variable(self):
        input = """
            int a() {
                return 3;
            }
            void main() {
                a();
                boolean a;
                int b;
                {
                    int a;
                    b=3;
                    a=3;
                }
            }
            """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 487))

    def test_type_mismatch_variable_as_call_expr(self):
        input = """
            void main() {
                int a;
                a();
            }
            """
        expect = "Type Mismatch In Expression: CallExpr(Id(a),[])"
        self.assertTrue(TestChecker.test(input, expect, 488))

    def test_type_mismatch_global_variable_as_call_expr(self):
        input = """
            int a;
            void main() {
                a(3,2);
            }
            """
        expect = "Type Mismatch In Expression: CallExpr(Id(a),[IntLiteral(3),IntLiteral(2)])"
        self.assertTrue(TestChecker.test(input, expect, 489))

    def test_assign_variable_in_parameter_with_global_function_name(self):
        input = """
            void a(){}
            void b() {
                a();
            }
            void main(int a) {
                a = 2;
                b();
            }
            """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 490))

    def test_redeclared_function(self):
        input = """
            int a;
            void a(){}
            void main(){
                a();
            }
            """
        expect = "Redeclared Function: a"
        self.assertTrue(TestChecker.test(input, expect, 491))

    def test_int_type_operators(self):
        input = """
        void main(){
            int a;
            boolean b;
            a= 3+4;
            a = 3*5;
            a = 3-2;
            a = 3/5;
            a = 3%5;
            b = 4>=5;
            b = 4<=5;
            b = 4<5;
            b = 4>5;
            b = 4==5;
            b = 4!=5;
            a = 5;
            a = -5;
        }
            
            """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 492))

    def test_float_type_operators(self):
        input = """
        void main() {
            float a;
            boolean b;
            a= 3.0+4;
            a = 3.0*5;
            a = 3.0-2;
            a = 3.0/5;
            b = 4.0>=5.0;
            b = 4.0<=5.0;
            b = 4.0<5.1;
            b = 4.2>5.3;
            a = 5.2;
            a= -5.0;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 493))

    def test_boolean_type_operators(self):
        input = """
        void main() {
            boolean a;
            boolean b;
            boolean c;
            a= true;
            b = false;
            c = a == b;
            c = a != b;
            c = a && b;
            c = a||b;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 494))

    def test_builtin_function(self):
        input = """
        void main() {
            getInt();
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 495))

    def test_complex_program_check_even(self):
        input = """
        void main() {
            even(2);
        }
        int even(int x)  {
                   if(x%2==0) return 1;
                   return 0;
        }
        
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 496))

    def test_complex_program_factorial(self):
        input = """
        void main() {
            fact(5);
        }
        int fact(int f)
            {
                int c;
                int fact;
                fact=1;
                for(c=1;c<=f;c=c+1) fact=fact*c;
                return fact;
            }

        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 497))

    def test_complex_program_check_leap_year(self):
        input = """
        void main() {
            check_leap_year(1999);
        }
        int check_leap_year(int year)
            {
                if (year%400 ==0) return 1;
                if (year%100 ==0) return 0;
                if (year%4 ==0) return 1;
                return 0;
            }

        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 498))

    def test_complex_program_sum_of(self):
        input = """
        void main() {
            sumofn(5);
        }
        int sumofn(int n)
            {
                int i,x;
                x=0;
                for (i=1;i<=n;i=i+1) x=x+i;
                return x;
            }

        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 499))

    def test_complex_program_reverse(self):
        input = """
        void main() {
            reverse(123456789);
        }
        int reverse(int n)
            {
                int reverse;
                reverse=0;
                do
                    reverse = reverse*10;
                    reverse = reverse + n%10;
                    n = n/10;
                while (n != 0) ;
                return reverse;
            }

        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 500))

