import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_int(self):
        """Simple program: int main() {} """
        input = """void main() {putInt(100);}"""
        expect = "100"
        self.assertTrue(TestCodeGen.test(input,expect,500))
    def test_int_ast(self):
    	input = Program([
    		FuncDecl(Id("main"),[],VoidType(),Block([
    			CallExpr(Id("putInt"),[IntLiteral(5)])]))])
    	expect = "5"
    	self.assertTrue(TestCodeGen.test(input,expect,501))
    def test_float_ast(self):
        """Simple program: int main() {} """
        input = """void main() {putFloat(10.1);}"""
        expect = "10.1"
        self.assertTrue(TestCodeGen.test(input,expect,502))
    def test_vardecl_and_putFLoat(self):
        """Simple program: int main() {} """
        input = """void main() {
            int a;
            putFloat(10.1);}"""
        expect = "10.1"
        self.assertTrue(TestCodeGen.test(input,expect,503))
    def test_global_vardecl_and_putFLoat(self):
        """Simple program: int main() {} """
        input = """
        int b;
        void main() {
            int a;
            putFloat(10.1);}"""
        expect = "10.1"
        self.assertTrue(TestCodeGen.test(input,expect,504))
    def test_putBool_ast(self):
        """Simple program: int main() {} """
        input = """
        int b;
        void main() {
            int a;
            putString("true");}"""
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,505))
    def test_int_id(self):
        """Simple program: void main() { putInt(100); } """
        input = """void main(){
            int a;
            a=1;
            putInt(a);
         }"""
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,506))
    def test_putbool_newline(self):
        input = """void main () {
         putBoolLn(true);
         }"""
        expect = "true\n"
        self.assertTrue(TestCodeGen.test(input,expect,507))
    def test_putstring_newline_ast(self):
        """Simple program: int main() {} """
        input = """
        int b;
        void main() {
            int a;
            putString("Lam assignment 4 hi vong qua mon PPL");}"""
        expect = "Lam assignment 4 hi vong qua mon PPL"
        self.assertTrue(TestCodeGen.test(input,expect,508))
    def test_putint_newline(self):
        input = """void main () {
         putIntLn(000);
         }"""
        expect = "0\n"
        self.assertTrue(TestCodeGen.test(input,expect,509))
    def test_testvarldecl_global(self):
        input = """int a;
         float b;
         void main () {
         }
         boolean c;"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,510))

    def test_arraytype(self):
        input =  """
            int arr[5];
            void main () { }
         """
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,511))
    def test_arraytype_in_main(self):
        input =  """
            
            void main () { 
                int arr[5];
                int b;
            }
         """
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,512))
    def test_floatlit_e(self):
        input = """void main() {putFloat(111.11e5);}"""
        expect = "1.1111E7"
        self.assertTrue(TestCodeGen.test(input,expect,513))

    def test_floatlit_e2(self):
        input = """void main() {putFloat(143.15e5);}"""
        expect = "1.4315E7"
        self.assertTrue(TestCodeGen.test(input,expect,514))
    def test_more_decl(self):
        input = """int a;
         float b;
         float fl1[4];
         int arr[5];
         string atr[4];
         void main () { }
         """
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,515))
    def test_put_id(self):
        
        input = """
        float b[5];
         void main () {  
             int a;
             a = 10;
             putInt(a);
         }
         """
        expect = "10"
        self.assertTrue(TestCodeGen.test(input,expect,516))
    def test_put_id_with_global_vardecl(self):
        
        input = """
        float b[5];
        int a;
         void main () {  
             
             a = 10;
             putInt(a);
         }
         """
        expect = "10"
        self.assertTrue(TestCodeGen.test(input,expect,517))
    def test_addop_putint(self):
        
        input = """
        float b[5];
         void main () {  
             int a;
             a = 10 + 20;
             putInt(a);
         }
         """
        expect = "30"
        self.assertTrue(TestCodeGen.test(input,expect,518))
    def test_addop_isub_putint(self):
        
        input = """
        float b[5];
         void main () {  
             int a;
             a = 10 - 20;
             putInt(a);
         }
         """
        expect = "-10"
        self.assertTrue(TestCodeGen.test(input,expect,519))
    def test_addop_isub_putfloat(self):
        
        input = """
        float b[5];
         void main () {  
             float a;
             a = 10 - 20;
             putFloat(a);
         }
         """
        expect = "-10.0"
        self.assertTrue(TestCodeGen.test(input,expect,520))
    def test_mulop_putfloat(self):
        
        input = """
        float b[5];
         void main () {  
             float a;
             a = 10 * 20;
             putFloat(a);
         }
         """
        expect = "200.0"
        self.assertTrue(TestCodeGen.test(input,expect,521))
    def test_divop_putInt(self):
        
        input = """
        float b[5];
         void main () {  
             int a;
             a = 10 / 3;
             putInt(a);
         }
         """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,522))
    def test_divop_putFloat_result_is_IntType(self):
        
        input = """
        float b[5];
         void main () {  
             int a;
             a = 10 / 3;
             putFloat(a);
         }
         """
        expect = "3.0"
        self.assertTrue(TestCodeGen.test(input,expect,523))
    def test_Modop_putFloat_result_is_IntType(self):
        
        input = """
        float b[5];
         void main () {  
             int a;
             a = 10 % 3;
             putInt(a);
         }
         """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,524))
    def test_gtop_putBool_r(self):
        
        input = """
        float b[5];
         void main () {  
            int a;
             a = 3 > 2;
             putBool(a);
         }
         """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,525))
    def test_gtop_varBoolType_putBool_r(self):
        
        input = """
        float b[5];
         void main () {  
            boolean a;
             a = 3 > 2;
             putBool(a);
         }
         """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,526))
    def test_iseqop_varBoolType_putBool_r(self):
        
        input = """
        float b[5];
         void main () {  
            boolean a;
             a = 3 == 2;
             putBool(a);
         }
         """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,527))
    def test_isneqop_varBoolType_putBool_r(self):
        
        input = """
        float b[5];
         void main () {  
            boolean a;
             a = 3 != 2;
             putBool(a);
         }
         """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,528))
    def test_putInt_with_operand_is_ID(self):
        
        input = """
        float b[5];
         void main () {  
           int a,b,c;
           b = 10; c =5;
           a = b+c ;
           putInt(a);

         }
         """
        expect = "15"
        self.assertTrue(TestCodeGen.test(input,expect,529))
    def test_arraycell_assign(self):
        
        input = """int arr[5];
         void main () {
          arr[0]=15;
          putIntLn(arr[0]);
         }
         """
        expect = "15\n"
        self.assertTrue(TestCodeGen.test(input,expect,530))
    def test_array_of_Float_putfloat(self):
        
        input = """
         float frr[4];
         void main () {
          frr[0] = 1.43;
          putFloatLn(frr[0]);
         }
         """
        expect = "1.43\n"
        self.assertTrue(TestCodeGen.test(input,expect,531))

    def test_arrayString_pustring(self):
        
        input = """int arr[5];
         string str[4];
         void main () {
          str[0] = "StringGlobal";
          putStringLn(str[0]);
         }
         """
        expect = "StringGlobal\n"
        self.assertTrue(TestCodeGen.test(input,expect,532))

    def test_arrayBool_putBool(self):
        
        input = """int arr[5];
         boolean b[4];
         void main () {
          b[0] = false;
          putBoolLn(b[0]);
         }
         """
        expect = "false\n"
        self.assertTrue(TestCodeGen.test(input,expect,533))
    def test_assign_with_id(self):
        
        input = """int a, b;
         void main () {
          int i;
          a = -1;
          i = a;
          putInt(i);
         }
         """
        expect = "-1"
        self.assertTrue(TestCodeGen.test(input,expect,534))

    def test_assign_id_float_2(self):
        
        input = """float a, b;
         void main () {
          float f;
          a = 11.5;
          f = a;
          putFloat(f);
         }
         """
        expect = "11.5"
        self.assertTrue(TestCodeGen.test(input,expect,535))
    def test_2_assigned_with_bool(self):
        
        input = """float fNum;
         string str2;
         void main () {
          boolean isT,isTrue;
          isT = false;
          isTrue = false;
          isT = isTrue = true;
          putBool(isT);
         }"""
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,536))

    def test_assigned_string_2(self):
        
        input = """float fNum;
         string str[4];
         void main () {
          str[0] = "null";
          str[1] = "text";
          str[2] = "notNull";
          str[0] = str[1] = "final";
          putString(str[0]);
         }"""
        expect = "final"
        self.assertTrue(TestCodeGen.test(input,expect,537))

    def test_assigned_int_arraytype_putint(self):
        
        input = """
         void main () {
          int arr[4];
          arr[0] = 1;
          arr[1] = 2;
          arr[2] = 3;
          putInt(arr[1]);
         }"""
        expect = "2"
        self.assertTrue(TestCodeGen.test(input,expect,538))
    def test_multi_assign_arraycell(self):
        
        input = """
        float fNum;
        string str[4];
        void main () {
            int arr[4];
            int a,b;
            a = b = 1;
            arr[0]= a;
            arr[1] = arr[0] = b = a;
            arr[2] = a = arr[0]= 18;
            putIntLn(arr[2]);
         }"""
        expect = "18\n"
        self.assertTrue(TestCodeGen.test(input,expect,539))

    def test_multi_assign_arraycell_coersion(self):
        
        input = """float fNum;
         string str[4];
         void main () {
          int arr[4];
          int a,b;
          float f;
          fNum = a = b = 11;
          f = arr[0]= a;
          fNum = arr[1] = arr[0] = b = a;
          putFloatLn(fNum);
         }"""
        expect = "11.0\n"
        self.assertTrue(TestCodeGen.test(input,expect,540))
    def test_add_minus_ac_literal(self):
        
        input = """int a,b,c;
            int arr[3];
            void main () {
                int iNum, i,j;
                arr[0] = 0;
                arr[1] = 1;
                arr[2] = 2;
                a = 3;
                b = a + 2;
                c = b + a + 3;
                iNum = arr[0] + c + (arr[1] - b) - (arr[2] - arr[0]);
                i = iNum - arr[0] + arr[1] - arr[2] - c;
                j = iNum - i + 11;
                putIntLn(j);
            }"""
        expect = "23\n"
        self.assertTrue(TestCodeGen.test(input,expect,541))


    def test_multiassignboolliteral(self):
        
        input = """boolean a, b;
         boolean gArr[4];
         void main () {
          boolean arr[4];
          boolean c,d;
          c = true;
          c = d = false;
          a = c;
          b = d = false;
          arr[0] = true;
          gArr[0] = arr[0] = true;
          gArr[1] = gArr[2] = arr[2] = d;
          putBoolLn(gArr[1]);
         }"""
        expect = "false\n"
        self.assertTrue(TestCodeGen.test(input,expect,542))



    def test_multi_operator_arraycel_id_lit(self):
        
        input = """int a,b,c;
        int arr[3];
        void main () {
         arr[0] = arr[1] = arr[2] = 3;
         a = 19;
         b = a + a % arr[0];
         c = b%a + arr[0]*arr[1];
         arr[2] = (c*a)%b;
         putIntLn(arr[2]);
        }"""
        expect = "10\n"
        self.assertTrue(TestCodeGen.test(input,expect,543))

    def test_multi_not_operator(self):
        
        input = """boolean isTrue;
        boolean arr[4];
        void main () {
         boolean isT, isF;
         arr[0] = arr[1] = arr[2] = false;
         isT = !arr[0];
         isF = !(!arr[1]);
         isTrue = !!!!!!isF;
         putBoolLn(isTrue);
        
        }"""
        expect = "false\n"
        self.assertTrue(TestCodeGen.test(input,expect,544))

    def test_neg_operator_ac(self):
       
        input = """int arr[4];
        void main () {
         int iNum, i , j;
         arr[0] = arr[1] = arr[2] = 10;
         i = -arr[0];
         j = -arr[1];
         iNum = i + j;
         putIntLn(iNum);
        }"""
        expect = "-20\n"
        self.assertTrue(TestCodeGen.test(input,expect,545))

    def test_gt_operator_ac_cmp(self):
        
        input = """float arr[4];
        void main () {
         int arr[4], b;
         boolean isTrue;
         arr[0] = 11;
         arr[1] = arr[0] + 2;
         isTrue = arr[1] > 12 ;
         putBoolLn(isTrue);
        }"""
        expect = "true\n"
        self.assertTrue(TestCodeGen.test(input,expect,546))

    def test_test_iseq_putbool(self):
        
        input = """
        void main () {
         boolean arr[2];
         boolean a;
         boolean isTrue;
         a = false;
         arr[0] = !a;
         isTrue = arr[0] == !a;
         putBoolLn(isTrue);
        }"""
        expect = "true\n"
        self.assertTrue(TestCodeGen.test(input,expect,547))
    def test_ifstmt_putInt(self):
            """Program => manipulate data in Main function: if no else stmt"""
            input = """
            void main () {
            int a;
            a = 1;
            if(a>1){
            a = 10;
            }
            putIntLn(a);
            }"""
            expect = "1\n"
            self.assertTrue(TestCodeGen.test(input,expect,548))

    def test_check_return_stmt(self):
        
        input = """
            void main () {
             float a;
             a = ab(2);
             putFloat(a);
            }
            float ab(int a){
            if(a==2)
             return 2*2;
            return 2.0;
        }"""
        expect = "4.0"
        self.assertTrue(TestCodeGen.test(input,expect,549))

    def test_if_else_return_void(self):
        
        input  = """
        void main () {
        
        }
        void foo(int a){
         if(a>1)
           return;
          else{
           a = a + 2;
           return;
          }
        }"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,550))

    def test_print_in_other_function(self):
        
        input = """
        void main () {
         int a;
         a = 1;
         test(a);
        }
        void test(int a){
         putInt(a);
        }"""
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,551))

    def test_if_else_assign(self):
        
        input = """
        void main () {
         int a;
         a = 2;
         if(a>1){
           a = 10;
         }
         else{
           a = 11;
         }
         putInt(a);
        }"""
        expect = "10"
        self.assertTrue(TestCodeGen.test(input,expect,552))

    def test_if_else_assign_2_test(self):
        
        input = """
        void main () {
         int a;
         a = 2;
         if(a>5){
           a = 10;
         }
         else{
           a = 11;
         }
         putInt(a);
        }"""
        expect = "11"
        self.assertTrue(TestCodeGen.test(input,expect,553))

    def test_if_else_assign(self):
        input = """
        void main () {
         int a;
         a = 2;
         if(a>5){
           if(a%2==0)
             a = a/2;
         }
         else{
           a = 11;
           if(a%3!=0)
             a = a*3;
         }
         putInt(a);
        }"""
        expect = "33"
        self.assertTrue(TestCodeGen.test(input,expect,554))

    def test_if_else_assign_2(self):
       
        input = """
        void main () {
         int a;
         a = 2;
         if(a>5){
           if(a%2==0)
             a = a*2;
           else
             a = a/2;
         }
         else{
           a = 11;
           if(a%3==0)
             a = a*3;
           else
             a = a*3/2;
         }
         putIntLn(a);
        }"""
        expect = "16\n"
        self.assertTrue(TestCodeGen.test(input,expect,555))

    def test_do_while_stmt(self):
        """Program => manipulate data in Main function: dowhile stmt simple!"""
        input = """
            void main () {
                int a;
                a = 1;
                do{
                    putInt(a);
                    a=a+1;
                } while(a<5);
            }"""
        expect = "1234"
        self.assertTrue(TestCodeGen.test(input,expect,556))

    def test_do_while_continue(self): 
        input = """
        void main () {
         int a, iSum;
         a = 0;
         iSum = 0;
         do{
         a = a + 1;
         if(a%2==0)
           continue;
         iSum = iSum + a;
         }while(a<20);
         putInt(iSum);
        }"""
        expect = "100"
        self.assertTrue(TestCodeGen.test(input,expect,557))

    def test_do_while_break(self):
        
        input = """
        void main () {
         int a, iSum;
         a = 0;
         iSum = 0;
         do{
         a = a + 1;
         if(a>17)
           break;
         iSum = iSum + a;
         }while(a<20);
         putInt(iSum);
        }"""
        expect = "153"
        self.assertTrue(TestCodeGen.test(input,expect,558))

    def test_do_while_continue_break(self):
        input = """
        void main () {
         int a, iSum;
         a = 0;
         iSum = 0;
         do{
         a = a + 1;
         if(a>17)
           break;
         if(a%2==0)
           continue;
         iSum = iSum + a;
         }while(a<20);
         putInt(iSum);
        }"""
        expect = "81"
        self.assertTrue(TestCodeGen.test(input,expect,559))

    def test_dowhile2(self):
        """Program => manipulate data in Main function: dowhile stmt inner dowhile stmt!"""
        input = """
        void main () {
         int a,b, iSum;
         a = 0;
         b = 0;
         iSum = 0;
         do{
         b = 0;
         a = a + 1;
         do{
           b = b +1;
           iSum = iSum + b;
         }while(b<a);
         iSum = iSum + a;
         }while(a<20);
         putInt(iSum);
        }"""
        expect = "1750"
        self.assertTrue(TestCodeGen.test(input,expect,560))

    def test_more_do_while(self):
        
        input = """
        void main () {
         int a,b, iSum;
         a = 0;
         b = 0;
         iSum = 0;
         do{
         b = 0;
         a = a + 1;
         do{
           b = b +1;
           if(b>10)
             break;
           if(b%2==1)
             continue;
           iSum = iSum + b;
         }while(b<a);
         if(a%b==0)
           continue;
         if(a+b>40)
           break;
         iSum = iSum + a;
         }while(a<20);
        
         putIntLn(iSum);
        }"""
        expect = "554\n"
        self.assertTrue(TestCodeGen.test(input,expect,561))

    def test_for_stmt_break(self):
        
        input = """
        void main () {
         int a;
         for(a = 0; a < 10; a = a + 1){
           putInt(a);
           break;
         }
        }"""
        expect = "0"
        self.assertTrue(TestCodeGen.test(input,expect,562))

    def test_for_stmt_continue(self):
        
        input = """
        void main () {
         int a,b, iSum;
         iSum = 0;
         for(a = 0; a < 10; a = a + 1){
           if(a%2==0)
             continue;
           iSum = iSum + a;
         }
         putInt(iSum);
        }"""
        expect = "25"
        self.assertTrue(TestCodeGen.test(input,expect,563))

    def test_for_stmt_break_1(self):
        
        input = """
        void main () {
         int a,b, iSum;
         iSum = 0;
         for(a = 0; a < 10; a = a + 1){
           if(iSum > 27)
             break;
           iSum = iSum + a;
         }
         putInt(iSum);
        }"""
        expect = "28"
        self.assertTrue(TestCodeGen.test(input,expect,564))

    def test_for_stmt_break_2(self):
        
        input = """
        void main () {
         int a,b, iSum;
         iSum = 0;
         for(a = 0; a < 10; a = a + 1){
           if(iSum > 27)
             break;
           if(a%3!=0)
             continue;
           iSum = iSum + a;
         }
         putIntLn(iSum);
        }"""
        expect = "18\n"
        self.assertTrue(TestCodeGen.test(input,expect,565))

    def test_for_stmt_break_1_continue(self):
        
        input = """
        void main () {
         int a,b, iSum;
         iSum = 0;
         for(a = 0; a < 10; a = a + 1){
           for(b = 0; b < a ; b = b + 1){
             if(a+b>17)
               break;
             if(b%2==0)
               continue;
             iSum = iSum + b;
           }
           if(iSum > 27)
             break;
           if(a%3!=0)
             continue;
           iSum = iSum + a;
         }
         putIntLn(iSum);
        }"""
        expect = "37\n"
        self.assertTrue(TestCodeGen.test(input,expect,566))

    def test_block_block(self):
        
        input = """int i,j;
        void main () {
         int a,b, iSum;
         i = 10;
         {
           float i;
           i = 11.8;
           putFloat(i);
         }
         {
           i = 11;
         }
         putIntLn(i);
        }"""
        expect = "11.811\n"
        self.assertTrue(TestCodeGen.test(input,expect,567))

    def test_block2(self):
        """Program => manipulate data in Main function: block inner block"""
        input = """int i,j;
        void main () {
         int a,b, iSum;
         i = 10;
         {
           float i;
           i = 14.3;
           {
             int i;
             i = 19;
             putInt(i);
           }
           putFloat(i);
         }
         putInt(i);
        }"""
        expect = "1914.310" 
        self.assertTrue(TestCodeGen.test(input,expect,568))

    def test_square_func_return(self):
        
        input = """int a;
        void main () {
         int b;
         b = 5;
         foo(b);
         putFloat(foo(b));
        }
        int foo(int a){
         return a*a;
        }"""
        expect = "25.0"
        self.assertTrue(TestCodeGen.test(input,expect,569))

    def test_return_1_func(self):
        
        input = """
        void main () {
         putIntLn(foo());
        }
        int foo(){
         return 1;
        }"""
        expect = "1\n"
        self.assertTrue(TestCodeGen.test(input,expect,570))
############
    def test_test_arraypointertype(self):
        """Program => Funcall is expression in BinaryOp in main function - return type of Function is ArrayPointerType - FloatType"""
        input = """
        void main () {
         float arr[3];
         arr[2]=1.5;
         foo(arr);
         arr[2] = foo(arr)[2] + 1.1;
         putFloatLn(arr[2]);
        }
        float[] foo(float x[]){
         x[2] = 5.1;
         return x;
        }
        """
        expect = "6.2\n"
        self.assertTrue(TestCodeGen.test(input,expect,571))

    def test_apt_function_string(self):
        
        input = """
        void main () {
         string arr[3];
         arr[2]="stringMain";
         arr[2] = foo(arr)[2];
         putStringLn(arr[2]);
        }
        string[] foo(string x[]){
         x[2] = "stringFoo";
         return x;
        }
        """
        expect = "stringFoo\n"
        self.assertTrue(TestCodeGen.test(input,expect,672))

    def test_test_more_func(self):
        
        input = """
        void main () {
         int a, b, res;
         a = 1;
         b = 1;
         res = foo(a,b);
         putIntLn(res);
        }
        int foo(int a, int b){
           if(a==b)
             return 111;
           else
             return 222;
        }
        """
        expect = "111\n"
        self.assertTrue(TestCodeGen.test(input,expect,673))

    def test_another_func_once_again(self):
        
        input = """void main(){
         int a, b, res;
         a = 11;
         b = 12;
         res = foo(a,b);
         putIntLn(res);
        }
        int foo(int a, int b){
         if(a!=b){
           if(a!=1){
             a = a + 1;
           }else{
             if(b==1){
               return 1;
             }else{
               a = a + 3;
             }
           }
           return a;
         }else{
           return 0;
         }
        }
        int complex(int a, int b, int c){
         if(a!=b){
           return a;
         }else{
           if(c == b){
             return c;
           }else{
             return b;
           }
         }
        }
        """
        expect = "12\n"
        self.assertTrue(TestCodeGen.test(input,expect,674))

    def test_nested_for_stmt(self):
        
        input = """void main(){
         int i,j,k;
         for(i=1;i<=7;i=i+1){
           for(j=1;j<=i;j=j+1)
             putInt(j);
           for(k=7-i;k>=1;k=k-1)
             putString("*");
           putString("");
         }
         putString("");
        }
        """
        expect = """1******12*****123****1234***12345**123456*1234567"""
        self.assertTrue(TestCodeGen.test(input,expect,675))

    def test_recursive_function(self):
        
        input = """
        int factorial(int i){
         if(i<=1){
           return 1;
         }
         return i * factorial(i - 1);
        }
        void main(){
         int i, j;
         i = 10;
         j = factorial(i);
         putIntLn(j);
        }
        """
        expect = "3628800\n"
        self.assertTrue(TestCodeGen.test(input,expect,676))

    def test_fibonacy_func(self):
        
        input = """
        int Fibonacci(int i){
         if(i==0){
           return 0;
         }
         if(i==1){
           return 1;
         }
         return Fibonacci(i - 1) + Fibonacci(i - 2);
        }
        void main(){
         int i;
         for(i = 0; i < 10; i = i + 1){
           putInt(Fibonacci(i));
         }
        }
        """
        expect = "0112358132134"
        self.assertTrue(TestCodeGen.test(input,expect,677))
    def test_do_while_stmt(self):
        """Program => manipulate data in Main function: dowhile stmt simple!"""
        input = """
            void main () {
                int a;
                a = 1;
                do{
                    putInt(a);
                    a=a+1;
                } while(a<0);
            }"""
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,578))
    def test_do_while_stmt1_print(self):
        """Program => manipulate data in Main function: dowhile stmt simple!"""
        input = """
            void main () {
                int a;
                a = 1;
                do{
                    putInt(a);
                    putInt(a*2);
                    a=a+1;
                } while(a<0);
            }"""
        expect = "12"
        self.assertTrue(TestCodeGen.test(input,expect,579))
    def test_for_stmt1_print_more(self):
        
        input = """
            void main () {
                int a;
                a = 1;
                int i;
                for(i = 0; i < 10; i = i +1)
                    if(i % 2 ==0)
                        putInt(i);
            }"""
        expect = "02468"
        self.assertTrue(TestCodeGen.test(input,expect,580))
    def test_for_stmt1_loop_with_sum_0_to_n(self):
        
        input = """
            void main () {
                int sum;
                sum = 0;
                int i;
                for(i = 0; i < 10; i = i +1)
                     sum = sum + i;
                putInt(sum);
            }"""
        expect = "45"
        self.assertTrue(TestCodeGen.test(input,expect,581))
    def test_compare_two_float(self):
        
        input = """
            void main () {
                float a,b;
                a = 2.9999;
                b = 2.9998;
                boolean gt;
                gt = a > b;
                putBool(gt);
            }"""
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,582))
    def test_sub_two_float_with_0(self):
        
        input = """
            void main () {
                float a,b;
                a = 2.9999;
                b = 2.9998;
                boolean gt;
                gt = (a - b) > 0;
                putBool(gt);
            }"""
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,583))
    def test_short_circurt(self):
        input = """
            void main () {
                boolean a,b,c;
                b = false;
                c = true;
                a = b && (1 / 0);
                putBool(a);
            }"""
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,584))
    def test_short_circurt(self):
        input = """
            void main () {
                boolean a,b,c;
                b = false;
                c = true;
                a = b && (1 / 0);
                putBool(a);
            }"""
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,584))
    def test_short_circurt1(self):
        input = """
            void main () {
                boolean a,b,c;
                b = true;
                c = true;
                a = b || (1 / 0);
                putBool(a);
            }"""
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,585))
    def test_short_circurt2(self):
        input = """
            void main () {
                boolean a,b,c;
                b = true;
                c = true;
                a = b || false || (1 / 0);
                putBool(a);
            }"""
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,586))
    def test_short_circurt4(self):
        input = """
            void main () {
                boolean a,b,c;
                b = true;
                c = true;
                a = b || false || (1 / 0);
                putBoolLn(a);
            }"""
        expect = "true\n"
        self.assertTrue(TestCodeGen.test(input,expect,587))
    def test_short_circurt6_with_global_var(self):
        input = """
            float a,b,c;
            void main () {
                boolean a,b,c;
                b = true;
                c = true;
                a = b || false || (1 / 0);
                putBoolLn(a);
            }"""
        expect = "true\n"
        self.assertTrue(TestCodeGen.test(input,expect,588))
    def test_testvarldecl_global_and_in_main(self):
        input = """int a;
         float b;
         void main () {
             int b,c;
         }
         boolean c;"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,589))

    def test_arraytype_out_and_in_func(self):
        input =  """
            int arr[5];
            void main () {
                float arr[5];
            }
         """
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,590))
        ### old testcase to reach 100 testcase :v :))) 
    def test_if_else(self):
        input = """void main(){
            if(true)
                putInt(1);
            else
                putInt(1);
         }"""
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,591))

    def test_test_function_return_92(self):
        input = """
        void main(){
            int a;
            a = 4;
            putFloatLn(foo(a));
        }
        float foo(int a){
            int foo;
            foo = 5;
            return foo + a;
        }
        """
        expect = """9.0\n"""
        self.assertTrue(TestCodeGen.test(input,expect,592))

    def test_put_value_000(self):
        input = """void main () {
         putIntLn(000);
         }"""
        expect = "0\n"
        self.assertTrue(TestCodeGen.test(input,expect,593))

    def test_putfloatln_1(self):
        input = """void main () {
         putFloatLn(1.0);
         }"""
        expect = "1.0\n"
        self.assertTrue(TestCodeGen.test(input,expect,594))

    def test_putfloatln_10(self):
        input = """void main () {
         putFloatLn(10.5);
         }"""
        expect = "10.5\n"
        self.assertTrue(TestCodeGen.test(input,expect,595))

    def test_putfloat_5(self):
        input = """void main () {
         putFloatLn(100.14);
         }"""
        expect = "100.14\n"
        self.assertTrue(TestCodeGen.test(input,expect,596))

    def test_putBoolmore(self):
        input = """void main () {
         putBoolLn(true);
         }"""
        expect = "true\n"
        self.assertTrue(TestCodeGen.test(input,expect,597))
    def test_var_decl_no_stmt(self):
        input = """int a;
         float b;
         float f[10];
         int array[10];
         string arrayString[10];
         void main () { }
         """
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,598))

    def test_putStrin_with_Stringlit(self):
        """Program => Test global variable and function whose return type is voidtype."""
        input = """
         
         void main () {
            putStringLn("Tam nay thi ket thuc testcase 100 cho roi");
         }
         """
        expect = "Tam nay thi ket thuc testcase 100 cho roi\n"
        self.assertTrue(TestCodeGen.test(input,expect,599))
        ##### dat ten trung nen chi chay ra 98 testcase
    def test_putStrin_with_Stringlit2(self):
        """Program => Test global variable and function whose return type is voidtype."""
        input = """
         
         void main () {
            putStringLn("Tam nay thi ket thuc testcase 100 cho roi");
         }
         """
        expect = "Tam nay thi ket thuc testcase 100 cho roi\n"
        self.assertTrue(TestCodeGen.test(input,expect,600))
    # def test_putStrin_with_Stringlit1(self):
    #     """Program => Test global variable and function whose return type is voidtype."""
    #     input = """
         
    #      void main () {
    #         putStringLn("Tam nay thi ket thuc testcase 100 cho roi");
    #      }
    #      """
    #     expect = "Tam nay thi ket thuc testcase 100 cho roi\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,601))

