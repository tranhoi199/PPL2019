import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):
# ------------------------------------------------------------------------------------
    def test_redeclare_local(self):
        input = '''void main(){
            int a;
            a = 1;
            float a;
        }'''
        expect = 'Redeclared Variable: a'
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test_redeclare_func(self):
        input = Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl('a',IntType())])),FuncDecl(Id("main"),[],VoidType(),Block([VarDecl('b',IntType())]))])
        expect = 'Redeclared Function: main'
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test_redeclare_para(self):
        input = '''void main(int a, int b, float a){
            boolean c;
        }'''
        expect = 'Redeclared Parameter: a'
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test_redecl_paralc(self):
        input = Program([FuncDecl(Id("main"),[VarDecl("argc", IntType())],VoidType(), Block([VarDecl("argc", IntType())]))])
        expect = 'Redeclared Variable: argc'
        self.assertTrue(TestChecker.test(input, expect, 404))

    def test_builtin(self):
        input = '''void putLn(){}
        void main(){
            int a;
        }'''
        expect = 'Redeclared Function: putLn'
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_redecl_block(self):
        input = '''void main() {
            int a;
            {
                float a;
                if (a >= 1)
                {
                    boolean a;
                    a = true;
                }
                int a;
            }
        }'''
        expect = 'Redeclared Variable: a'
        self.assertTrue(TestChecker.test(input, expect, 406))

    def test_func_diffType(self):
        input = '''int foo(){ int a; return a; }
        void main(){
            int foo;
        }
        float foo(int bar) { return bar; }'''
        expect = 'Redeclared Function: foo'
        self.assertTrue(TestChecker.test(input, expect, 407))

    def test_redecl_var_after(self):
        input = '''int main(){
            main = 0;
            return main;
        }
        int main;'''
        expect = 'Redeclared Variable: main'
        self.assertTrue(TestChecker.test(input, expect, 408))

    def test_redcl_main(self):
        input = '''int main;
        void main(){
            a = 0;
        }
        int a;'''
        expect = 'Redeclared Function: main'
        self.assertTrue(TestChecker.test(input, expect, 409))

    def test_redecl_inblock(self):
        input = '''void main(){
            {   
                float a;
                a = getFloat();
                int a;
                a = getInt();
            }
        }'''
        expect = 'Redeclared Variable: a'
        self.assertTrue(TestChecker.test(input, expect, 410))

# -------------------------------------------------------------------------------------
    def test_undeclared_function(self):
        input = """int main() { foo(); }"""
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,411))

    def test_undeclared_var(self):
        input = Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",Id("a"),IntLiteral(1))]))])
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,412))

    def test_callexp_noBracket(self):
        input = '''int foo(int a){ return 3 ; }
        void main() { foo(food_bar); }'''
        expect = 'Undeclared Identifier: food_bar'
        self.assertTrue(TestChecker.test(input, expect, 413))

    def test_call_id(self):
        input = '''int foo;
        void main(){
            foo();
        }'''
        expect = 'Type Mismatch In Expression: CallExpr(Id(foo),[])'
        self.assertTrue(TestChecker.test(input, expect, 414))

    def test_use_before_decl(self):
        input = '''void main(){
            a = 1 + 1;
            float a;
            a = 0.5;
        }'''
        expect = 'Undeclared Identifier: a'
        self.assertTrue(TestChecker.test(input, expect, 415))

    def test_undecl_inStmt(self):
        input = '''void main() {
            for (a = 1; a < 4; a = a + 1)
                break;
        }'''
        expect = 'Undeclared Identifier: a'
        self.assertTrue(TestChecker.test(input, expect, 416))

    def test_decl_in_another_blck(self):
        input = '''void main(){
            if (true)
            {
                a = 1 + 1;
                a = a*a;
            }
            do {
                int a;
                a = 1 + 2;
            } while (true);
        }'''
        expect = 'Undeclared Identifier: a'
        self.assertTrue(TestChecker.test(input, expect, 417))

    def test_funcCall_in_builtin(self):
        input = """int foo(int foo) {
            return foo * foo(foo - 1);
        }
        void main(){
            int a;
            foo(a);
        }"""
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[BinaryOp(-,Id(foo),IntLiteral(1))])"
        self.assertTrue(TestChecker.test(input, expect, 418))

    def test_used_before_decl(self):
        input = '''int main(){
            if (true)
            {
                a = 1;
                {
                    float a;
                    a = 2.5;
                }
            }
            return 0;
        }'''
        expect = 'Undeclared Identifier: a'
        self.assertTrue(TestChecker.test(input, expect, 419))

    def test_decl_inside_while(self):
        input = '''void main() {
            do {
                int a;
                a = 2;
                a = a * a;
            } while (a < 16);
        }'''
        expect = 'Undeclared Identifier: a'
        self.assertTrue(TestChecker.test(input, expect, 420))

# -------------------------------------------------------------------------------
    def test_return_pointer(self):
        input = ''' int[] foo(int a[]) { return 1; }
        void main(){
            int a[3];
            foo(a);
        }'''
        expect = 'Type Mismatch In Statement: Return(IntLiteral(1))'
        self.assertTrue(TestChecker.test(input, expect, 421))

    def test_return_voidFunc(self):
        input = '''void foo(){ return; }
        void main(){
            return foo();
        }'''
        expect = 'Type Mismatch In Statement: Return(CallExpr(Id(foo),[]))'
        self.assertTrue(TestChecker.test(input, expect, 422))

    def test_condition_func(self):
        input = '''int foo() { return 1; }
        int main(){
            int a;
            if (foo() + 1)
                return a = 0;
            return a;
        }'''
        expect = 'Type Mismatch In Statement: If(BinaryOp(+,CallExpr(Id(foo),[]),IntLiteral(1)),Return(BinaryOp(=,Id(a),IntLiteral(0))))'
        self.assertTrue(TestChecker.test(input, expect, 423))

    def test_for_startVal(self):
        input = '''int main(){
            int a;
            for (a == 1; a < 5; a = a + 1){
                putIntLn(a);
            }
            return 0;
        }'''
        expect = 'Type Mismatch In Statement: For(BinaryOp(==,Id(a),IntLiteral(1));BinaryOp(<,Id(a),IntLiteral(5));BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)));Block([CallExpr(Id(putIntLn),[Id(a)])]))'
        self.assertTrue(TestChecker.test(input, expect, 424))

    def test_for_InitWrongType(self):
        input = '''int main(){
            int a;
            for (a = 0.25; a < 5; a = a * 2)
                putInt(a);
            return 0;
        }'''
        expect = 'Type Mismatch In Expression: BinaryOp(=,Id(a),FloatLiteral(0.25))'
        self.assertTrue(TestChecker.test(input, expect, 425))

    def test_for_startUnary(self):
        input = '''int main(){
            float a;
            a = 1;
            for (-a; a < 5; a = a + 5)
                putFloat(a);
            return a;
        }'''
        expect = 'Type Mismatch In Statement: For(UnaryOp(-,Id(a));BinaryOp(<,Id(a),IntLiteral(5));BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(5)));CallExpr(Id(putFloat),[Id(a)]))'
        self.assertTrue(TestChecker.test(input, expect, 426))

    def test_for_initFloat(self):
        input = '''void main(){
            float a;
            for (a = 0.25; a < 1; a = a + 0.05)
                putFloat(a);
        }'''
        expect = 'Type Mismatch In Statement: For(BinaryOp(=,Id(a),FloatLiteral(0.25));BinaryOp(<,Id(a),IntLiteral(1));BinaryOp(=,Id(a),BinaryOp(+,Id(a),FloatLiteral(0.05)));CallExpr(Id(putFloat),[Id(a)]))'
        self.assertTrue(TestChecker.test(input, expect, 427))

    def test_for_assignCondition(self):
        input = '''int main() {
            int a;
            for (a = 1; a = 4; a = a - 1)
                putFloat(a);
            return 0;
        }'''
        expect = 'Type Mismatch In Statement: For(BinaryOp(=,Id(a),IntLiteral(1));BinaryOp(=,Id(a),IntLiteral(4));BinaryOp(=,Id(a),BinaryOp(-,Id(a),IntLiteral(1)));CallExpr(Id(putFloat),[Id(a)]))'
        self.assertTrue(TestChecker.test(input, expect, 428))

    def test_for_unOpexp2(self):
        input = '''void main() {
            int a;
            for (a = 1; -a; a = a - 1)
                putInt(a);
        }'''
        expect = 'Type Mismatch In Statement: For(BinaryOp(=,Id(a),IntLiteral(1));UnaryOp(-,Id(a));BinaryOp(=,Id(a),BinaryOp(-,Id(a),IntLiteral(1)));CallExpr(Id(putInt),[Id(a)]))'
        self.assertTrue(TestChecker.test(input, expect, 429))

    def test_dowhile_str(self):
        input = '''void main(){
            string a;
            float var;
            a = "true";
            do 
                var = var + 1;
            while (a);
        }'''
        expect = 'Type Mismatch In Statement: Dowhile([BinaryOp(=,Id(var),BinaryOp(+,Id(var),IntLiteral(1)))],Id(a))'
        self.assertTrue(TestChecker.test(input, expect, 430))

    def test_returnInt_str(self):
        input = '''string foo(int a) { return a + 1; }
        void main(){
            int a;
            foo(a);
        }'''
        expect = 'Type Mismatch In Statement: Return(BinaryOp(+,Id(a),IntLiteral(1)))'
        self.assertTrue(TestChecker.test(input, expect, 431))

    def test_reverse_coerrene(self):
        input = '''int val(int a, float b) { return a + b; }
        void main(){
            int a;
            float b;
            putFloat(val(a, b));
        }'''
        expect = 'Type Mismatch In Statement: Return(BinaryOp(+,Id(a),Id(b)))'
        self.assertTrue(TestChecker.test(input, expect, 432))

    def test_assign_if(self):
        input = '''void main(){
            int a;
            if (a = 1) {
                return a;
            }
            else 
                return 0;
        }'''
        expect = 'Type Mismatch In Statement: If(BinaryOp(=,Id(a),IntLiteral(1)),Block([Return(Id(a))]),Return(IntLiteral(0)))'
        self.assertTrue(TestChecker.test(input, expect, 433))

    def test_return_nothing(self):
        input = '''int main(){
            int a;
            a = 1;
            return ;
        }'''
        expect = 'Type Mismatch In Statement: Return()'
        self.assertTrue(TestChecker.test(input, expect, 434))

    def test_if_id(self):
        input = '''void main(){
            float a, b;
            if (a)
                return b;
            else 
                return a;
        }'''
        expect = 'Type Mismatch In Statement: If(Id(a),Return(Id(b)),Return(Id(a)))'
        self.assertTrue(TestChecker.test(input, expect, 435))

    def test_for_in_for(self):
        input = '''void main(){
            int a[5], b[6], c[3];
            if (a[0] < b[0])
                if (a[1] < b[1])
                    if (a[3] < c[0])
                        if (c)
                            return 1;
        }'''
        expect = 'Type Mismatch In Statement: If(Id(c),Return(IntLiteral(1)))'
        self.assertTrue(TestChecker.test(input, expect, 436))

    def test_loop_countStr(self):
        input = '''void main(){
            string a;
            int strLen;
            for (a = "a"; strLen < 5; strLen = strLen + 1)
                putLn(a);
        }'''
        expect = 'Type Mismatch In Statement: For(BinaryOp(=,Id(a),StringLiteral(a));BinaryOp(<,Id(strLen),IntLiteral(5));BinaryOp(=,Id(strLen),BinaryOp(+,Id(strLen),IntLiteral(1)));CallExpr(Id(putLn),[Id(a)]))'
        self.assertTrue(TestChecker.test(input, expect, 437))

    def test_FloatPointer_inarray(self):
        input = '''float[] foo(int a)
        {
            float b[5];
            return b ;
        }
        void main() { 
            int a,b,c;
            float d,e,f ; 
            for(a = 3; foo(a)[2] > b; foo(3)[1] * b)
                d - e * f ; 
        } '''
        expect = 'Type Mismatch In Statement: For(BinaryOp(=,Id(a),IntLiteral(3));BinaryOp(>,ArrayCell(CallExpr(Id(foo),[Id(a)]),IntLiteral(2)),Id(b));BinaryOp(*,ArrayCell(CallExpr(Id(foo),[IntLiteral(3)]),IntLiteral(1)),Id(b));BinaryOp(-,Id(d),BinaryOp(*,Id(e),Id(f))))'
        self.assertTrue(TestChecker.test(input, expect, 438))

    def test_str_literal_dowhile(self):
        input = '''void main() {
            int a, b, c;
            do 
                a = b * 2;
                b = c*3;
                c = c*c;
            while ("true");
        }'''
        expect = 'Type Mismatch In Statement: Dowhile([BinaryOp(=,Id(a),BinaryOp(*,Id(b),IntLiteral(2))),BinaryOp(=,Id(b),BinaryOp(*,Id(c),IntLiteral(3))),BinaryOp(=,Id(c),BinaryOp(*,Id(c),Id(c)))],StringLiteral(true))'
        self.assertTrue(TestChecker.test(input, expect, 439))

    def test_return_in_voidFunc(self):
        input = '''void main(){
            return "ABC";
        }'''
        expect = 'Type Mismatch In Statement: Return(StringLiteral(ABC))'
        self.assertTrue(TestChecker.test(input, expect, 440))

    def test_return_void(self):
        input = '''int main(){
            return ;
        }'''
        expect = 'Type Mismatch In Statement: Return()'
        self.assertTrue(TestChecker.test(input, expect, 441))

    def test_returnPointer_intFunc(self):
        input = '''int main(){
            int a[7];
            return a;
        }'''
        expect = 'Type Mismatch In Statement: Return(Id(a))'
        self.assertTrue(TestChecker.test(input, expect, 442))

    def test_return_arrayCell_pointerFunc(self):
        input = '''int[] main(){
            int valid[5];
            valid[0] = 5;
            return valid[0];
        }'''
        expect = 'Type Mismatch In Statement: Return(ArrayCell(Id(valid),IntLiteral(0)))'
        self.assertTrue(TestChecker.test(input, expect, 443))

    def test_array_arrPointer_returnFunc(self):
        input = '''float[] glue(int a , int b []) {
            int arr[9];
            glue(3,arr);
            return arr;
        }
        void main(){
            int c[15];
            glue(2,c);
            return ; 
        }'''
        expect = 'Type Mismatch In Statement: Return(Id(arr))'
        self.assertTrue(TestChecker.test(input, expect, 444))

    def test_wrong_para_arraytype(self):
        input = '''float foo(int a[]){
            return a[1];
        }
        void main(){
            float a[5];
            foo(a);
        }'''
        expect = 'Type Mismatch In Expression: CallExpr(Id(foo),[Id(a)])'
        self.assertTrue(TestChecker.test(input, expect, 445))

# ---------------------------------------------------------------------------------

    def test_miss_para(self):
        input = """void foo(int a){ a = 1; }
        int main () {
            foo();
        }"""
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[])"
        self.assertTrue(TestChecker.test(input,expect,446))
    
    def test_morethan_para(self):
        input = """int main () {
            int a;
            a = getInt(4);
        }"""
        expect = "Type Mismatch In Expression: CallExpr(Id(getInt),[IntLiteral(4)])"
        self.assertTrue(TestChecker.test(input,expect,447))

    def test_assign_int_array(self):
        input = '''int main() {
            int a;
            int b[3];
            a = b;
            return 0;
        }'''
        expect = 'Type Mismatch In Expression: BinaryOp(=,Id(a),Id(b))'
        self.assertTrue(TestChecker.test(input, expect, 448))

    def test_floatPara_intpass(self):
        input = '''float foo(float a[]){
            return a[0];
        }
        void main(){
            int a[5];
            foo(a);
        }'''
        expect = 'Type Mismatch In Expression: CallExpr(Id(foo),[Id(a)])'
        self.assertTrue(TestChecker.test(input, expect, 449))

    def test_assign_arr_arrPointer(self):
        input = '''int[] foo(int c[]){ return c; }
        void main(){
            int a[3], b[5];
            b = foo(a);
        }'''
        expect = 'Type Mismatch In Expression: BinaryOp(=,Id(b),CallExpr(Id(foo),[Id(a)]))'
        self.assertTrue(TestChecker.test(input, expect, 450))

    def test_pointer_plus(self):
        input = '''int[] foo(){ int a[3]; return a; }
        void main() {
            foo() + 2;
        }'''
        expect = 'Type Mismatch In Expression: BinaryOp(+,CallExpr(Id(foo),[]),IntLiteral(2))'
        self.assertTrue(TestChecker.test(input, expect, 451))

    def test_not_int(self):
        input = '''void main(){
            int a;
            boolean b;
            b = !a;
        }'''
        expect = 'Type Mismatch In Expression: UnaryOp(!,Id(a))'
        self.assertTrue(TestChecker.test(input, expect, 452))

    def test_not_float(self):
        input = '''int main(){
            float a;
            boolean bar;
            bar = !a;
        }'''
        expect = 'Type Mismatch In Expression: UnaryOp(!,Id(a))'
        self.assertTrue(TestChecker.test(input, expect, 453))

    def test_FloatInt_reverse(self):
        input = '''void main() {
            float a; int b;
            b = a;
        }'''
        expect = 'Type Mismatch In Expression: BinaryOp(=,Id(b),Id(a))'
        self.assertTrue(TestChecker.test(input, expect, 454))

    def test_negative_bool(self):
        input = '''int main(){
            boolean visited;
            return -visited;
        }'''
        expect = 'Type Mismatch In Expression: UnaryOp(-,Id(visited))'
        self.assertTrue(TestChecker.test(input, expect, 455))

    def test_plus_str(self):
        input = '''void main(){
            string a, b;
            a = "Hello";
            b = "PPL";
            a = a + b;
        }'''
        expect = 'Type Mismatch In Expression: BinaryOp(+,Id(a),Id(b))'
        self.assertTrue(TestChecker.test(input, expect, 456))
    
    def test_comp_diff_type(self):
        input = '''void main() {
            float a;
            string b;
            a > b;
        }'''
        expect = 'Type Mismatch In Expression: BinaryOp(>,Id(a),Id(b))'
        self.assertTrue(TestChecker.test(input, expect, 457))

    def test_assign_id_arrayType(self):
        input = '''void main(){
            int a[5];
            a = 1;
        }'''
        expect = 'Type Mismatch In Expression: BinaryOp(=,Id(a),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input, expect, 458))

    def test_func_cell(self):
        input = '''float a(int b) 
        { 
            return b + 2.5;
        }
        void main() { 
            a[10] ; 
        }'''
        expect = 'Type Mismatch In Expression: ArrayCell(Id(a),IntLiteral(10))'
        self.assertTrue(TestChecker.test(input, expect, 459))

    def test_varName_func(self):
        input = '''int foo() { return 1; }
        void main() {
            foo = 1;
        }'''
        expect = 'Type Mismatch In Expression: BinaryOp(=,Id(foo),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input, expect, 460))

    def test_useBuilin_asVar(self):
        input = '''int main(){
            int a;
            a = getInt;
            return a;
        }'''
        expect = 'Type Mismatch In Expression: BinaryOp(=,Id(a),Id(getInt))'
        self.assertTrue(TestChecker.test(input, expect, 461))

    def test_for_floatExp3(self):
        input = '''int main(){
            int a;
            for (a = 0; a < 10; a = a * 1.5)
                putInt(a);
            return 0;
        }'''
        expect = 'Type Mismatch In Expression: BinaryOp(=,Id(a),BinaryOp(*,Id(a),FloatLiteral(1.5)))'
        self.assertTrue(TestChecker.test(input, expect, 462))

    def test_multiunary(self):
        input = '''void main(){
            boolean visited;
            if (!-!visited)
                return;
        }'''
        expect = 'Type Mismatch In Expression: UnaryOp(-,UnaryOp(!,Id(visited)))'
        self.assertTrue(TestChecker.test(input, expect, 463))

    def test_unOp_biOp(self):
        input = '''void main() {
            int a, b;
            b = -a + !a;
        }'''
        expect = 'Type Mismatch In Expression: UnaryOp(!,Id(a))'
        self.assertTrue(TestChecker.test(input, expect, 464))

    def test_equal_Float(self):
        input = '''boolean main(){
            float a, b;
            a = 3.2;
            b = 3.21;
            return a == b;
        }'''
        expect = 'Type Mismatch In Expression: BinaryOp(==,Id(a),Id(b))'
        self.assertTrue(TestChecker.test(input, expect, 465))

    def test_assignCell_Pointer(self):
        input = '''int[] foo(int a[]){
            a[0] = 1 + 1;
            return a;
        }
        void main(){
            int a[5];
            a[1] = foo(a);
        }'''
        expect = 'Type Mismatch In Expression: BinaryOp(=,ArrayCell(Id(a),IntLiteral(1)),CallExpr(Id(foo),[Id(a)]))'
        self.assertTrue(TestChecker.test(input, expect, 466))

    def test_idx_bool(self):
        input = '''void main(){
            int a[5];
            float i, j;
            a[i] = a[j];
        }'''
        expect = 'Type Mismatch In Expression: ArrayCell(Id(a),Id(i))'
        self.assertTrue(TestChecker.test(input, expect, 467))

    def test_notCell_notation(self):
        input = '''int main(){
            int a;
            a[0] = 1;
            a[1] = 2;
        }'''
        expect = 'Type Mismatch In Expression: ArrayCell(Id(a),IntLiteral(0))'
        self.assertTrue(TestChecker.test(input, expect, 468))

    def test_wrongpara_Pointer_Cell(self):
        input = '''int cal(int a, int arr[]){
            return a + arr[0];
        }
        void main() {
            int a;
            int visited[5];
            cal(visited, a);
        }'''
        expect = 'Type Mismatch In Expression: CallExpr(Id(cal),[Id(visited),Id(a)])'
        self.assertTrue(TestChecker.test(input, expect, 469))

    def test_not_same_number_parameter(self):
        input = '''int sum3(int a, int b, int c){
            return a + b + c;
        }
        void main(){
            int a, b, c;
            c = sum3(a, b);
        }'''
        expect = 'Type Mismatch In Expression: CallExpr(Id(sum3),[Id(a),Id(b)])'
        self.assertTrue(TestChecker.test(input, expect, 470))

# ----------------------------------------------------------------------------------------
    def test_no_return(self):
        input = '''int main(){ int a; }'''
        expect = 'Function main Not Return '
        self.assertTrue(TestChecker.test(input, expect, 471))

    def test_if_return(self):
        input = '''int main() {
            if (true)
            {
                int a;
                return 1;
            }
        }'''
        expect = 'Function main Not Return '
        self.assertTrue(TestChecker.test(input, expect, 472))

    def test_multi_if(self):
        input = '''int main() {
            int a;
            if (a == 2)
                if (a < 4)
                    return 2;
                else 
                    return 1;
        }'''
        expect = 'Function main Not Return '
        self.assertTrue(TestChecker.test(input, expect, 473))

    def test_for_if(self):
        input = '''int main(){
            int a;
            for (a = 1; a < 5; a = a + 1)
                if (a > 3)
                    return 1;
                else
                    return 2;
        }'''
        expect = 'Function main Not Return '
        self.assertTrue(TestChecker.test(input, expect, 474))

    def test_if_for_if(self):
        input = '''int main(){
            int a;
            if (a > 1)
                for (a = 2; a < 5; a = a + 1) {
                    if (a < 5)
                        return 1;
                }
            else 
                return 0;
        }'''
        expect = 'Function main Not Return '
        self.assertTrue(TestChecker.test(input, expect, 475))

    def test_do_for(self):
        input = '''int main(){
            do {
                int a;
                for (a = 1; a < 10; a = a * 2)
                    return 1;
            } while (true);
        }'''
        expect = 'Function main Not Return '
        self.assertTrue(TestChecker.test(input, expect, 476))

    def test_do_if(self):
        input = '''float main() {
            int a;
            a = getInt();
            do 
                if (a >= 1)
                    return a;
            while (a < 2);
        }'''
        expect = 'Function main Not Return '
        self.assertTrue(TestChecker.test(input, expect, 477))

    def test_else_return(self):
        input = '''float main(){
            float a;
            a = 0.5;
            if (a < 0)
                a = -a;
            else 
                return a;
        }'''
        expect = 'Function main Not Return '
        self.assertTrue(TestChecker.test(input, expect, 478))

    def test_if_for_do(self):
        input = '''int main(){
            int a, b;
            if (a < b)
                for(a = 1; a <= b; a = a + 1)
                    return a;
            else 
                do 
                    a = a * 2;
                    b = b / 2;
                    return b;
                while (true);
        }'''
        expect = 'Function main Not Return '
        self.assertTrue(TestChecker.test(input, expect, 479))

    def test_dowhile_for(self):
        input = '''int main(){
            int a;
            do 
                for (a = 1; a < 5; a = a + 1){
                    int b;
                    b = b + a;
                    return b;
                }
                return a;
            while (a == 1);
        }'''
        expect = ''
        self.assertTrue(TestChecker.test(input, expect, 480))

# ---------------------------------------------------------------------------------------
    def test_break_block(self):
        input = '''void main(){
            int a;
            a = 1;
            break;
            a = 1 * 1;
        }'''
        expect = 'Break Not In Loop'
        self.assertTrue(TestChecker.test(input, expect, 481))

    def test_break_if(self):
        input = '''int main(){
            int a, b;
            if (a > b)
                break;
            else
                return b;
            return a;
        }'''
        expect = 'Break Not In Loop'
        self.assertTrue(TestChecker.test(input, expect, 482))

    def test_continue_if(self):
        input = '''int main(){
            if (1 == 1)
            {
                continue;
                int a;
                a = 1;
                return 1;
            }
            return 0;
        }'''
        expect = 'Continue Not In Loop'
        self.assertTrue(TestChecker.test(input, expect, 483))

    def test_break_in_MultiIf(self):
        input = '''void main(){
            int a;
            if (a == 6)
            {
                int b;
                {
                    b = 1;
                    break;
                    b = 2;
                }
                b = 3;
            }
        }'''
        expect = 'Break Not In Loop'
        self.assertTrue(TestChecker.test(input, expect, 484))

    def test_break_outside_loop(self):
        input = '''void main(){
            int a;
            if (true) {
                for (a = 1; a < 5; a = a + 1)
                    a = a - 2;
                break;
            }
        }'''
        expect = 'Break Not In Loop'
        self.assertTrue(TestChecker.test(input, expect, 485))

# ----------------------------------------------------------------------------------------
    def test_no_mainFunc(self):
        input = '''boolean ex() {
            return main();
        }'''
        expect = 'No Entry Point'
        self.assertTrue(TestChecker.test(input, expect, 486))

    def test_only_decl(self):
        input = '''int a, b, c;'''
        expect = 'No Entry Point'
        self.assertTrue(TestChecker.test(input, expect, 487))

    def test_decl_mainvar(self):
        input = '''int main;
        int foo(){
            bar();
            return 1;
        }
        void bar(){
            int a, b;
            foo();
        }'''
        expect =  'No Entry Point'
        self.assertTrue(TestChecker.test(input, expect, 488))

    def test_no_mainkw(self):
        input = '''int a;
        int cal(int a, int b){
            return a + b;
        }'''
        expect = 'No Entry Point'
        self.assertTrue(TestChecker.test(input, expect, 489))
        
# # --------------------------------------------------------------------------------------
    def test_2_diff_funccall(self):
        input = '''int main(){
            return 0;
        }
        int cal1(int a){
            return a;
        }
        int cal2(){
            return cal1(cal2());
        }'''
        expect = 'Unreachable Function: cal2'
        self.assertTrue(TestChecker.test(input, expect, 490))
    
    def test_func_notcall(self):
        input = '''int foo() { return 0; }
        int main(){ return 1; }'''
        expect = 'Unreachable Function: foo'
        self.assertTrue(TestChecker.test(input, expect, 491))

    def test_call_itself(self):
        input = """int[] foo(int a, int b[], int c[])
        {
            int arr[9];
            foo(3,arr,foo(12,arr,arr));
            return arr ;
        }
        void main(){
            return ; 
        }"""
        expect = 'Unreachable Function: foo'
        self.assertTrue(TestChecker.test(input, expect, 492))

# -----------------------------------------------------------------------------------
    def test_multi_assign(self):
        input = '''void main(){
            int a, b, c;
            a * b = c = 2 ;
        }'''
        expect = 'Not Left Value: BinaryOp(*,Id(a),Id(b))'
        self.assertTrue(TestChecker.test(input, expect, 493))

    def test_func_with_para(self):
        input = '''int foo(int a) {
            a= a + 1;
            return a;
        }    
        void main(){
            int a;
            foo(a) = a;
        }'''
        expect = 'Not Left Value: CallExpr(Id(foo),[Id(a)])'
        self.assertTrue(TestChecker.test(input, expect, 494))

    def test_assign_voidFunc(self):
        input = '''void cal(int a, int b){
            a = a + b;
        }
        int main(){
            int a, b, s;
            cal(a, b) = s; 
            return 0;
        }'''
        expect = 'Not Left Value: CallExpr(Id(cal),[Id(a),Id(b)])'
        self.assertTrue(TestChecker.test(input, expect, 495))

    def test_assign_void(self):
        input = '''void foo(){
            int a ;
        }
        void main(){
            float a ;
            foo() = a ;
        }'''
        expect = 'Not Left Value: CallExpr(Id(foo),[])'
        self.assertTrue(TestChecker.test(input, expect, 496))

    def test_assign_func2func(self):
        input = '''int foo() {
            do
                return 1;
                continue;
            while(false);
        }

        int goo(){  
            do
                continue;
                return 1;
            while(false);
        }
        void main(){
            foo() = goo();
        }'''
        expect = 'Not Left Value: CallExpr(Id(foo),[])'
        self.assertTrue(TestChecker.test(input, expect, 497))

    def test_assign_literal(self):
        input = '''void main(){
            int a;
            5 = a;
        }'''
        expect = 'Not Left Value: IntLiteral(5)'
        self.assertTrue(TestChecker.test(input, expect, 499))

    def test_pointer_assign(self):
        input = '''int[] foo(){ int a[3]; return a; }
        void main() {
            foo() = 2;
        }'''
        expect = 'Not Left Value: CallExpr(Id(foo),[])'
        self.assertTrue(TestChecker.test(input, expect, 500))

    def test_binaryLHS(self):
        input = '''void main(){
            int a;
            a + 1 = 3;
        }'''
        expect = 'Not Left Value: BinaryOp(+,Id(a),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input, expect, 498))