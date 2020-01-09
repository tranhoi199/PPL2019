import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """int main() {}"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,300))

    def test_more_complex_program(self):
        """More complex program"""
        input = """int main () {
            putIntLn(4);
        }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([CallExpr(Id(putIntLn),[IntLiteral(4)])]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,301))
    
    def test_call_without_parameter(self):
        """More complex program"""
        input = """int main () {
            getIntLn();
        }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([CallExpr(Id(getIntLn),[])]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,302))
    def test_var_decl(self):
        input = """int a,b,c;"""
        expect = "Program([VarDecl(a,IntType),VarDecl(b,IntType),VarDecl(c,IntType)])"
        self.assertTrue(TestAST.checkASTGen(input,expect,303))
    def test_var_decl1(self):
        input = """float b;"""
        expect = "Program([VarDecl(b,FloatType)])"
        self.assertTrue(TestAST.checkASTGen(input,expect,304))
    def test_var_array_decl(self):
        input = """int a[5];"""
        expect = "Program([VarDecl(a,ArrayType(IntType,5))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,305))
    def test_var_array_decl1(self):
        input = """int a[5],b;"""
        expect = "Program([VarDecl(a,ArrayType(IntType,5)),VarDecl(b,IntType)])"
        self.assertTrue(TestAST.checkASTGen(input,expect,306))
    def test_var_array_decl2(self):
        input = """int a[5],b;
string e;"""
        expect = "Program([VarDecl(a,ArrayType(IntType,5)),VarDecl(b,IntType),VarDecl(e,StringType)])"
        self.assertTrue(TestAST.checkASTGen(input,expect,307))
    
    def test_func_decl(self):
        input = """float foo(int a, int b){
}"""
        expect = "Program([FuncDecl(Id(foo),[VarDecl(a,IntType),VarDecl(b,IntType)],FloatType,Block([]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,308))
    def test_func_decl1(self):
        input = """boolean main(string a1, float arr[],boolean flag){
}"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(a1,StringType),VarDecl(arr,ArrayTypePointer(FloatType)),VarDecl(flag,BoolType)],BoolType,Block([]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,309))
    def test_func_var_decl(self):
        input = """float a[3], b;
int[] foo(string a1, float arr[],int b[]){
}"""
        expect = "Program([VarDecl(a,ArrayType(FloatType,3)),VarDecl(b,FloatType),FuncDecl(Id(foo),[VarDecl(a1,StringType),VarDecl(arr,ArrayTypePointer(FloatType)),VarDecl(b,ArrayTypePointer(IntType))],ArrayTypePointer(IntType),Block([]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,310))
    def test_stmt_simple(self):
        input = """
int main(){
    continue;
    return;
}"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([Continue(),Return()]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,311))
    def test_stmt_simple1(self):
        input = """
float foo(float a){
    break;
    int a, arr[3];
}"""
        expect = "Program([FuncDecl(Id(foo),[VarDecl(a,FloatType)],FloatType,Block([Break(),VarDecl(a,IntType),VarDecl(arr,ArrayType(IntType,3))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,312)) 
    def test_stmt_simple2(self):
        input = """
float foo(float a){
    (1+2);
    return 1+2;
}"""
        expect = "Program([FuncDecl(Id(foo),[VarDecl(a,FloatType)],FloatType,Block([BinaryOp(+,IntLiteral(1),IntLiteral(2)),Return(BinaryOp(+,IntLiteral(1),IntLiteral(2)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,313)) 
    def test_stmt_simple3(self):
        input = """
void foo(float a){
    if (a == 1){
        break;
    }
}"""
        expect = "Program([FuncDecl(Id(foo),[VarDecl(a,FloatType)],VoidType,Block([If(BinaryOp(==,Id(a),IntLiteral(1)),Block([Break()]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,314))
    def test_stmt_simple4(self):
        input = """
void foo(){
for(i=1;i<2;i=i+1) continue;
}"""
        expect = "Program([FuncDecl(Id(foo),[],VoidType,Block([For(BinaryOp(=,Id(i),IntLiteral(1));BinaryOp(<,Id(i),IntLiteral(2));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Continue())]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,315))
    def test_stmt_simple5(self):
        input = """
void foo(int a, int b){
    do a+1; while a=a*a;
}"""
        expect = "Program([FuncDecl(Id(foo),[VarDecl(a,IntType),VarDecl(b,IntType)],VoidType,Block([Dowhile([BinaryOp(+,Id(a),IntLiteral(1))],BinaryOp(=,Id(a),BinaryOp(*,Id(a),Id(a))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,316))
    def test_stmt_simple6(self):
        input = """
float x,y;
void foo(int a, int b){
    int a,b,c,d;
    if (a ==1) {
        a=3;
    }
}"""
        expect = "Program([VarDecl(x,FloatType),VarDecl(y,FloatType),FuncDecl(Id(foo),[VarDecl(a,IntType),VarDecl(b,IntType)],VoidType,Block([VarDecl(a,IntType),VarDecl(b,IntType),VarDecl(c,IntType),VarDecl(d,IntType),If(BinaryOp(==,Id(a),IntLiteral(1)),Block([BinaryOp(=,Id(a),IntLiteral(3))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,317))
    def test_arraycell_simple(self):
        input = """
int main(){
    a[ 1 + x] = true && false;
}"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([BinaryOp(=,ArrayCell(Id(a),BinaryOp(+,IntLiteral(1),Id(x))),BinaryOp(&&,BooleanLiteral(true),BooleanLiteral(false)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,318)) 
    def test_funcall_simple(self):
        input = """
int main(){
    foo(a,1.23);
    string arr[5];
}"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([CallExpr(Id(foo),[Id(a),FloatLiteral(1.23)]),VarDecl(arr,ArrayType(StringType,5))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,319))
    def test_funcall_simple1(self):
        input = """
int main(){
    do{
    }
    if (str == "string")
        return -1;
    while (1.2e3 >= x);
}"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([Dowhile([Block([]),If(BinaryOp(==,Id(str),StringLiteral(string)),Return(UnaryOp(-,IntLiteral(1))))],BinaryOp(>=,FloatLiteral(1200.0),Id(x)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,320))
    def test_funcall_simple2(self):
        input = """
int x,y,arr[6];
boolean flag;
void main(){
    for(x=0;y=x % -2.32;x=x+1){
        arr[x]= !1;
    }
}"""
        expect = "Program([VarDecl(x,IntType),VarDecl(y,IntType),VarDecl(arr,ArrayType(IntType,6)),VarDecl(flag,BoolType),FuncDecl(Id(main),[],VoidType,Block([For(BinaryOp(=,Id(x),IntLiteral(0));BinaryOp(=,Id(y),BinaryOp(%,Id(x),UnaryOp(-,FloatLiteral(2.32))));BinaryOp(=,Id(x),BinaryOp(+,Id(x),IntLiteral(1)));Block([BinaryOp(=,ArrayCell(Id(arr),Id(x)),UnaryOp(!,IntLiteral(1)))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,321))
    def test_exp_simple(self):
        input = """
        int foo (float a, int arr[]) 
        {
            int a , b , c ;
            float a[5],d ;
            string str;
            a = b + c;
            if (a > b) a = a -2;
            if(false) a = a+2;
        }
"""
        expect = """Program([FuncDecl(Id(foo),[VarDecl(a,FloatType),VarDecl(arr,ArrayTypePointer(IntType))],IntType,Block([VarDecl(a,IntType),VarDecl(b,IntType),VarDecl(c,IntType),VarDecl(a,ArrayType(FloatType,5)),VarDecl(d,FloatType),VarDecl(str,StringType),BinaryOp(=,Id(a),BinaryOp(+,Id(b),Id(c))),If(BinaryOp(>,Id(a),Id(b)),BinaryOp(=,Id(a),BinaryOp(-,Id(a),IntLiteral(2)))),If(BooleanLiteral(false),BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(2))))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,322))
    def test_func_call(self):

        input = """
        int main(){
            func((arr[i])[j]);
        }
        """
        expect = """Program([FuncDecl(Id(main),[],IntType,Block([CallExpr(Id(func),[ArrayCell(ArrayCell(Id(arr),Id(i)),Id(j))])]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,323))
    def test_simple_program2(self):
        input = """
        int main(){
            do { }
            while((arr[i])[j]);
        }
        """
        expect = """Program([FuncDecl(Id(main),[],IntType,Block([Dowhile([Block([])],ArrayCell(ArrayCell(Id(arr),Id(i)),Id(j)))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,324))
    def test_simple_program3(self):
        input = """boolean func1(boolean arg1, int arg2, float arr[]){}"""
        expect = """Program([FuncDecl(Id(func1),[VarDecl(arg1,BoolType),VarDecl(arg2,IntType),VarDecl(arr,ArrayTypePointer(FloatType))],BoolType,Block([]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,325))
    def test_func_decl3(self):
        input = """float func_test(string str[], int a){
    a = a + 1;
    func_test(str[2], a+2);            
}"""
        expect = """Program([FuncDecl(Id(func_test),[VarDecl(str,ArrayTypePointer(StringType)),VarDecl(a,IntType)],FloatType,Block([BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1))),CallExpr(Id(func_test),[ArrayCell(Id(str),IntLiteral(2)),BinaryOp(+,Id(a),IntLiteral(2))])]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,326))
    def test_func_decl4(self):
        input = """int __foo(){
    if(var!=0) print("hello");
}"""
        expect ="""Program([FuncDecl(Id(__foo),[],IntType,Block([If(BinaryOp(!=,Id(var),IntLiteral(0)),CallExpr(Id(print),[StringLiteral(hello)]))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,327))
    def test_do_while_stmt(self):
        """test do while stmt"""
        input = """void main() {
    do{
    print("statement 1");
    }
    {
    print("statement 2");
    }
    while (true);
}
"""
        expect = """Program([FuncDecl(Id(main),[],VoidType,Block([Dowhile([Block([CallExpr(Id(print),[StringLiteral(statement 1)])]),Block([CallExpr(Id(print),[StringLiteral(statement 2)])])],BooleanLiteral(true))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,328))
    def test_do_while_stmt2(self):
        """test do while stmt"""
        input = """int main () {
    /* local variable definition */
    int a;
    a = 0;
    /* do loop execution */
    do {
        printf("value of a: ", a);
        a = a + 1;
    }while( a < 20 );
    return 0;
}
"""
        expect="""Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(a,IntType),BinaryOp(=,Id(a),IntLiteral(0)),Dowhile([Block([CallExpr(Id(printf),[StringLiteral(value of a: ),Id(a)]),BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)))])],BinaryOp(<,Id(a),IntLiteral(20))),Return(IntLiteral(0))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,329))
    def test_do_while_stmt4(self):
        """test do while stmt"""
        input = """int main () {
    do{
        //comment1
        a=b=c==d;
    }while(false);
}
string foo(string a){
    //comment2
    a = k;
    return a;
}
"""
        expect = """Program([FuncDecl(Id(main),[],IntType,Block([Dowhile([Block([BinaryOp(=,Id(a),BinaryOp(=,Id(b),BinaryOp(==,Id(c),Id(d))))])],BooleanLiteral(false))])),FuncDecl(Id(foo),[VarDecl(a,StringType)],StringType,Block([BinaryOp(=,Id(a),Id(k)),Return(Id(a))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,330))
    def test_do_while_stmt5(self):
        """"""
        input = """int main () {
    if(-5.0)
        do{
            !a;
            string a,b,arr[4];
        }while(arr[true]);
    else
        print("error");
}
"""
        expect = """Program([FuncDecl(Id(main),[],IntType,Block([If(UnaryOp(-,FloatLiteral(5.0)),Dowhile([Block([UnaryOp(!,Id(a)),VarDecl(a,StringType),VarDecl(b,StringType),VarDecl(arr,ArrayType(StringType,4))])],ArrayCell(Id(arr),BooleanLiteral(true))),CallExpr(Id(print),[StringLiteral(error)]))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,331))
    def test_for_stmt(self):
        """test for stmt"""
        input = """boolean ptr[4],_a,_b;
int func() {
    for( i =0;i <=5;i=i+1)
        func2(ptr[2],_a,_b);     
}
"""
        expect = """Program([VarDecl(ptr,ArrayType(BoolType,4)),VarDecl(_a,BoolType),VarDecl(_b,BoolType),FuncDecl(Id(func),[],IntType,Block([For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(<=,Id(i),IntLiteral(5));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));CallExpr(Id(func2),[ArrayCell(Id(ptr),IntLiteral(2)),Id(_a),Id(_b)]))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,332)) 
    def test_for_stmt2(self):
        """test for stmt"""
        input = """float a;
string b;
int[] func(int a, string b) {
    for(!2;-3;5){
        a=a+b;
        func(a,b);
    }    
}
"""
        expect = """Program([VarDecl(a,FloatType),VarDecl(b,StringType),FuncDecl(Id(func),[VarDecl(a,IntType),VarDecl(b,StringType)],ArrayTypePointer(IntType),Block([For(UnaryOp(!,IntLiteral(2));UnaryOp(-,IntLiteral(3));IntLiteral(5);Block([BinaryOp(=,Id(a),BinaryOp(+,Id(a),Id(b))),CallExpr(Id(func),[Id(a),Id(b)])]))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,333))
    def test_for_stmt3(self):
        input = """int main()
{
    int num, count, sum;
    sum =0;
    printf("Enter a positive integer: ");
    scanf("%d", num);
    // for loop terminates when num is less than count
    for(count = 1; count <= num; count = count + 1)
    {
        sum =sum + count;
    }
    printf("Sum = %d", sum);
    return 0;
}
"""
        expect = """Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(num,IntType),VarDecl(count,IntType),VarDecl(sum,IntType),BinaryOp(=,Id(sum),IntLiteral(0)),CallExpr(Id(printf),[StringLiteral(Enter a positive integer: )]),CallExpr(Id(scanf),[StringLiteral(%d),Id(num)]),For(BinaryOp(=,Id(count),IntLiteral(1));BinaryOp(<=,Id(count),Id(num));BinaryOp(=,Id(count),BinaryOp(+,Id(count),IntLiteral(1)));Block([BinaryOp(=,Id(sum),BinaryOp(+,Id(sum),Id(count)))])),CallExpr(Id(printf),[StringLiteral(Sum = %d),Id(sum)]),Return(IntLiteral(0))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,334))
    def test_all_stmt(self):
        input = """string[] ABS(string a, int w[]){
    {
    }
    {    
    }
}
"""
        expect = """Program([FuncDecl(Id(ABS),[VarDecl(a,StringType),VarDecl(w,ArrayTypePointer(IntType))],ArrayTypePointer(StringType),Block([Block([]),Block([])]))])"""    
        self.assertTrue(TestAST.checkASTGen(input,expect,335))
    def test_all_stmt1(self):
        """test all stmt"""
        input = """int[] ABS(int a, float b){
    int a;
    a =8;
    if(-5 == a){
        a = a+1;
    }
    else
        continue;
    return a;
}
"""
        expect = """Program([FuncDecl(Id(ABS),[VarDecl(a,IntType),VarDecl(b,FloatType)],ArrayTypePointer(IntType),Block([VarDecl(a,IntType),BinaryOp(=,Id(a),IntLiteral(8)),If(BinaryOp(==,UnaryOp(-,IntLiteral(5)),Id(a)),Block([BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)))]),Continue()),Return(Id(a))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,336))
    def test_all_stmt2(self):
        """test all stmt"""
        input = """int main()
{
    int i;
    float number, sum;
    sum = 0.0 ;
    for(i=1; i <= 10;i = i *i)
    {
        printf("Enter a n%d: ",i);
        scanf("%lf", number);
        if(number < 0.0)
        {
            continue;
        }
        sum =sum+ number; 
    }
    printf("Sum = %.2lf",sum);
    return 0;
}
"""
        expect = """Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(i,IntType),VarDecl(number,FloatType),VarDecl(sum,FloatType),BinaryOp(=,Id(sum),FloatLiteral(0.0)),For(BinaryOp(=,Id(i),IntLiteral(1));BinaryOp(<=,Id(i),IntLiteral(10));BinaryOp(=,Id(i),BinaryOp(*,Id(i),Id(i)));Block([CallExpr(Id(printf),[StringLiteral(Enter a n%d: ),Id(i)]),CallExpr(Id(scanf),[StringLiteral(%lf),Id(number)]),If(BinaryOp(<,Id(number),FloatLiteral(0.0)),Block([Continue()])),BinaryOp(=,Id(sum),BinaryOp(+,Id(sum),Id(number)))])),CallExpr(Id(printf),[StringLiteral(Sum = %.2lf),Id(sum)]),Return(IntLiteral(0))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,337))
    def test_all_stmt3(self):
        """test all stmt"""
        input = """int main(){
    do
        {
        statement1;
        if (condition)
            break;
        statement2;
    }while (test_condition);
}
"""
        expect = """Program([FuncDecl(Id(main),[],IntType,Block([Dowhile([Block([Id(statement1),If(Id(condition),Break()),Id(statement2)])],Id(test_condition))]))])"""           
        self.assertTrue(TestAST.checkASTGen(input,expect,338))
    def test_all_stmt4(self):
        input = """int trim(string s[])
{
    int n;
    for (n = strlen(s)-1; n >= 0; n= n /2)
    if (s[n] != " " && s[n] != "\\t" && s[n] != "\\n")
        break;
    s[n+1] = "0";
    return n;
}"""
        expect = "Program([FuncDecl(Id(trim),[VarDecl(s,ArrayTypePointer(StringType))],IntType,Block([VarDecl(n,IntType),For(BinaryOp(=,Id(n),BinaryOp(-,CallExpr(Id(strlen),[Id(s)]),IntLiteral(1)));BinaryOp(>=,Id(n),IntLiteral(0));BinaryOp(=,Id(n),BinaryOp(/,Id(n),IntLiteral(2)));If(BinaryOp(&&,BinaryOp(&&,BinaryOp(!=,ArrayCell(Id(s),Id(n)),StringLiteral( )),BinaryOp(!=,ArrayCell(Id(s),Id(n)),StringLiteral(\\t))),BinaryOp(!=,ArrayCell(Id(s),Id(n)),StringLiteral(\\n))),Break())),BinaryOp(=,ArrayCell(Id(s),BinaryOp(+,Id(n),IntLiteral(1))),StringLiteral(0)),Return(Id(n))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,339))
    def test_all_stmt5(self):
        input = """int main()
{
    float number1;
    number1=13.5;
    float number2;
    number2 = 12.4;
    printf("number1 = %f\\n", number1);
    printf("number2 = %lf", number2);
    return 0;
}"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(number1,FloatType),BinaryOp(=,Id(number1),FloatLiteral(13.5)),VarDecl(number2,FloatType),BinaryOp(=,Id(number2),FloatLiteral(12.4)),CallExpr(Id(printf),[StringLiteral(number1 = %f\\n),Id(number1)]),CallExpr(Id(printf),[StringLiteral(number2 = %lf),Id(number2)]),Return(IntLiteral(0))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,340))
    def test_for_stmt4(self):
        """nested for loop"""
        input = """int[] main(int i, float a[])
{
    for (i=0; i<2; i=-i+1 )
    {
	    for (j=0; j<4; j= j%2)
	    {
	        printf("%d, %d\\n",i ,j);
	    }
    }
   return 0;
}"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(i,IntType),VarDecl(a,ArrayTypePointer(FloatType))],ArrayTypePointer(IntType),Block([For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(<,Id(i),IntLiteral(2));BinaryOp(=,Id(i),BinaryOp(+,UnaryOp(-,Id(i)),IntLiteral(1)));Block([For(BinaryOp(=,Id(j),IntLiteral(0));BinaryOp(<,Id(j),IntLiteral(4));BinaryOp(=,Id(j),BinaryOp(%,Id(j),IntLiteral(2)));Block([CallExpr(Id(printf),[StringLiteral(%d, %d\\n),Id(i),Id(j)])]))])),Return(IntLiteral(0))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,341))
    def test_func_call1(self):
        """test function call"""
        input = """int main()
{
    func1(foo(x%2),foo(foo(x+3,5.01*0.e-2),foo("string \\\\")));
    return 0;
}"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([CallExpr(Id(func1),[CallExpr(Id(foo),[BinaryOp(%,Id(x),IntLiteral(2))]),CallExpr(Id(foo),[CallExpr(Id(foo),[BinaryOp(+,Id(x),IntLiteral(3)),BinaryOp(*,FloatLiteral(5.01),FloatLiteral(0.0))]),CallExpr(Id(foo),[StringLiteral(string \\\\)])])]),Return(IntLiteral(0))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,342))
    def test_all_stmt6(self):
        """test all stmt"""
        input = """int main()
{
    for(exp1;exp2;exp3){
        do{
            {}
            {}
            {}
        }while(exp4);
    }       
}"""
        expect = """Program([FuncDecl(Id(main),[],IntType,Block([For(Id(exp1);Id(exp2);Id(exp3);Block([Dowhile([Block([Block([]),Block([]),Block([])])],Id(exp4))]))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,343))
    def test_simple_program4(self):
        input = """int main(string args[]){
    int a , b , c ;
    a=b=c=5;
    float f[5] ;
    if ( a==b) f[0] = 1.0;
}"""
        expect = """Program([FuncDecl(Id(main),[VarDecl(args,ArrayTypePointer(StringType))],IntType,Block([VarDecl(a,IntType),VarDecl(b,IntType),VarDecl(c,IntType),BinaryOp(=,Id(a),BinaryOp(=,Id(b),BinaryOp(=,Id(c),IntLiteral(5)))),VarDecl(f,ArrayType(FloatType,5)),If(BinaryOp(==,Id(a),Id(b)),BinaryOp(=,ArrayCell(Id(f),IntLiteral(0)),FloatLiteral(1.0)))]))])"""        
        self.assertTrue(TestAST.checkASTGen(input,expect,344))
    def test_simple_program5(self):
        input = """
        float[] main(int a[],string b[]){
            return "1asd";
        }"""
        expect = """Program([FuncDecl(Id(main),[VarDecl(a,ArrayTypePointer(IntType)),VarDecl(b,ArrayTypePointer(StringType))],ArrayTypePointer(FloatType),Block([Return(StringLiteral(1asd))]))])"""        
        self.assertTrue(TestAST.checkASTGen(input,expect,345))
    def test_simple_program6(self):
        input = """int main(string args[]){
    int a , b , c, d;
    boolean e ,f;
    if(a == b || c != d)
        a = b = e || f <= a + b - c * d + !b - foo()[i];
    else
        {   
        }
    return -1;
}"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(args,ArrayTypePointer(StringType))],IntType,Block([VarDecl(a,IntType),VarDecl(b,IntType),VarDecl(c,IntType),VarDecl(d,IntType),VarDecl(e,BoolType),VarDecl(f,BoolType),If(BinaryOp(||,BinaryOp(==,Id(a),Id(b)),BinaryOp(!=,Id(c),Id(d))),BinaryOp(=,Id(a),BinaryOp(=,Id(b),BinaryOp(||,Id(e),BinaryOp(<=,Id(f),BinaryOp(-,BinaryOp(+,BinaryOp(-,BinaryOp(+,Id(a),Id(b)),BinaryOp(*,Id(c),Id(d))),UnaryOp(!,Id(b))),ArrayCell(CallExpr(Id(foo),[]),Id(i))))))),Block([])),Return(UnaryOp(-,IntLiteral(1)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,346))
    def test_simple_program7(self):
        input = """
string a[5];
int main(){
    float a , b , c, d;
    a+ -2 *!5 *b /c &&d;
    return -1;
}"""
        expect = """Program([VarDecl(a,ArrayType(StringType,5)),FuncDecl(Id(main),[],IntType,Block([VarDecl(a,FloatType),VarDecl(b,FloatType),VarDecl(c,FloatType),VarDecl(d,FloatType),BinaryOp(&&,BinaryOp(+,Id(a),BinaryOp(/,BinaryOp(*,BinaryOp(*,UnaryOp(-,IntLiteral(2)),UnaryOp(!,IntLiteral(5))),Id(b)),Id(c))),Id(d)),Return(UnaryOp(-,IntLiteral(1)))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,347))
    def test_simple_program8(self):
        input = """int main(){
    int dividend, divisor, quotient, remainder;
    printf("Enter dividend: ");
    scanf("%d", dividend);
    printf("Enter divisor: ");
    scanf("%d", divisor);
    // Computes quotient
    quotient = dividend / divisor;
    // Computes remainder
    remainder = dividend %  divisor;
    printf("Quotient = %d", quotient);
    printf("Remainder = %d", remainder);
    return 0;
}"""
        expect = """Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(dividend,IntType),VarDecl(divisor,IntType),VarDecl(quotient,IntType),VarDecl(remainder,IntType),CallExpr(Id(printf),[StringLiteral(Enter dividend: )]),CallExpr(Id(scanf),[StringLiteral(%d),Id(dividend)]),CallExpr(Id(printf),[StringLiteral(Enter divisor: )]),CallExpr(Id(scanf),[StringLiteral(%d),Id(divisor)]),BinaryOp(=,Id(quotient),BinaryOp(/,Id(dividend),Id(divisor))),BinaryOp(=,Id(remainder),BinaryOp(%,Id(dividend),Id(divisor))),CallExpr(Id(printf),[StringLiteral(Quotient = %d),Id(quotient)]),CallExpr(Id(printf),[StringLiteral(Remainder = %d),Id(remainder)]),Return(IntLiteral(0))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,348))
    def test_simple_program9(self):
        input = """int main()
{
    int number, i;
    printf("Enter a positive integer: ");
    scanf("%d",number);
    printf("Factors of %d are: ", number);
    for(i=1; i <= number; i=i+1)
    {
        if (number%i == 0)
        {
            printf("%d ",i);
        }
    }
    return 0;
}"""
        expect = """Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(number,IntType),VarDecl(i,IntType),CallExpr(Id(printf),[StringLiteral(Enter a positive integer: )]),CallExpr(Id(scanf),[StringLiteral(%d),Id(number)]),CallExpr(Id(printf),[StringLiteral(Factors of %d are: ),Id(number)]),For(BinaryOp(=,Id(i),IntLiteral(1));BinaryOp(<=,Id(i),Id(number));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([If(BinaryOp(==,BinaryOp(%,Id(number),Id(i)),IntLiteral(0)),Block([CallExpr(Id(printf),[StringLiteral(%d ),Id(i)])]))])),Return(IntLiteral(0))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,349))
    def test_simple_program10(self):
        input = """int main()
{
    int n, i, flag;
    flag =0;
    printf("Enter a positive integer: ");
    scanf("%d", n);
    for(i = 2; i <= n/2; i=i+1)
    {
        // condition for nonprime number
        if(n%i == 0)
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
          printf("%d is a prime number.", n);
        else
          printf("%d is not a prime number.", n);
    }
    
    return 0;
}"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(n,IntType),VarDecl(i,IntType),VarDecl(flag,IntType),BinaryOp(=,Id(flag),IntLiteral(0)),CallExpr(Id(printf),[StringLiteral(Enter a positive integer: )]),CallExpr(Id(scanf),[StringLiteral(%d),Id(n)]),For(BinaryOp(=,Id(i),IntLiteral(2));BinaryOp(<=,Id(i),BinaryOp(/,Id(n),IntLiteral(2)));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([If(BinaryOp(==,BinaryOp(%,Id(n),Id(i)),IntLiteral(0)),Block([BinaryOp(=,Id(flag),IntLiteral(1)),Break()]))])),If(BinaryOp(==,Id(n),IntLiteral(1)),Block([CallExpr(Id(printf),[StringLiteral(1 is neither a prime nor a composite number.)])]),Block([If(BinaryOp(==,Id(flag),IntLiteral(0)),CallExpr(Id(printf),[StringLiteral(%d is a prime number.),Id(n)]),CallExpr(Id(printf),[StringLiteral(%d is not a prime number.),Id(n)]))])),Return(IntLiteral(0))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,350))
    def test_simple_program11(self):
        input = """int[] func(){
    int arr[3];
    arr[3]=(arr[0] + arr[1]) % (arr[arr[3-1]]);
    return arr[3];
}"""
        expect = "Program([FuncDecl(Id(func),[],ArrayTypePointer(IntType),Block([VarDecl(arr,ArrayType(IntType,3)),BinaryOp(=,ArrayCell(Id(arr),IntLiteral(3)),BinaryOp(%,BinaryOp(+,ArrayCell(Id(arr),IntLiteral(0)),ArrayCell(Id(arr),IntLiteral(1))),ArrayCell(Id(arr),ArrayCell(Id(arr),BinaryOp(-,IntLiteral(3),IntLiteral(1)))))),Return(ArrayCell(Id(arr),IntLiteral(3)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,351))
    def test_simple_program12(self):
        input = """boolean arr[4];
int[] func(){
    int arr[3];
    arr[3]= a - b* d --2 % (4<=3);
    return arr[0];
}"""
        expect = "Program([VarDecl(arr,ArrayType(BoolType,4)),FuncDecl(Id(func),[],ArrayTypePointer(IntType),Block([VarDecl(arr,ArrayType(IntType,3)),BinaryOp(=,ArrayCell(Id(arr),IntLiteral(3)),BinaryOp(-,BinaryOp(-,Id(a),BinaryOp(*,Id(b),Id(d))),BinaryOp(%,UnaryOp(-,IntLiteral(2)),BinaryOp(<=,IntLiteral(4),IntLiteral(3))))),Return(ArrayCell(Id(arr),IntLiteral(0)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,352))
    def test_simple_program13(self):
        input = """float main(){
    true||false &&1*-2;
    return -3.;
}"""
        expect = "Program([FuncDecl(Id(main),[],FloatType,Block([BinaryOp(||,BooleanLiteral(true),BinaryOp(&&,BooleanLiteral(false),BinaryOp(*,IntLiteral(1),UnaryOp(-,IntLiteral(2))))),Return(UnaryOp(-,FloatLiteral(3.0)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,353))
    def test_simple_program14(self):
        input = """float func(){
    float a,b,d,arr[3];
    foo(a%5)[2] / b; 
    return 1.0;
}"""
        expect = "Program([FuncDecl(Id(func),[],FloatType,Block([VarDecl(a,FloatType),VarDecl(b,FloatType),VarDecl(d,FloatType),VarDecl(arr,ArrayType(FloatType,3)),BinaryOp(/,ArrayCell(CallExpr(Id(foo),[BinaryOp(%,Id(a),IntLiteral(5))]),IntLiteral(2)),Id(b)),Return(FloatLiteral(1.0))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,354))
    def test_if_else_stmt(self):
        input = """void main(){
    if(a >= b = c - d % 2.e2)
        a && b  != d  + c / -a+ !true;
    else
        func(a,b,c,d);
}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([If(BinaryOp(=,BinaryOp(>=,Id(a),Id(b)),BinaryOp(-,Id(c),BinaryOp(%,Id(d),FloatLiteral(200.0)))),BinaryOp(&&,Id(a),BinaryOp(!=,Id(b),BinaryOp(+,BinaryOp(+,Id(d),BinaryOp(/,Id(c),UnaryOp(-,Id(a)))),UnaryOp(!,BooleanLiteral(true))))),CallExpr(Id(func),[Id(a),Id(b),Id(c),Id(d)]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,355))
    def test_if_else_stmt1(self):
        input = """
boolean a;
void main(){
    if(a = false)
        for(i = 0; i <= 5; i = i * 1.1){
            continue;
        }
    else
        main(1);
}"""
        expect = "Program([VarDecl(a,BoolType),FuncDecl(Id(main),[],VoidType,Block([If(BinaryOp(=,Id(a),BooleanLiteral(false)),For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(<=,Id(i),IntLiteral(5));BinaryOp(=,Id(i),BinaryOp(*,Id(i),FloatLiteral(1.1)));Block([Continue()])),CallExpr(Id(main),[IntLiteral(1)]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,356))
    def test_simple_program15(self):
        input = """int a,b;
    float c,d;
    //comment
    void main(){
        if(a <= b +c / 2+ f(a+3)[2])
            a = b  != d  + c / -a + 0.012E-2;
        else
            func(a,b);
    }
    int func(string a, string b){
        return func(a,b);
    }"""
        expect = "Program([VarDecl(a,IntType),VarDecl(b,IntType),VarDecl(c,FloatType),VarDecl(d,FloatType),FuncDecl(Id(main),[],VoidType,Block([If(BinaryOp(<=,Id(a),BinaryOp(+,BinaryOp(+,Id(b),BinaryOp(/,Id(c),IntLiteral(2))),ArrayCell(CallExpr(Id(f),[BinaryOp(+,Id(a),IntLiteral(3))]),IntLiteral(2)))),BinaryOp(=,Id(a),BinaryOp(!=,Id(b),BinaryOp(+,BinaryOp(+,Id(d),BinaryOp(/,Id(c),UnaryOp(-,Id(a)))),FloatLiteral(0.00012)))),CallExpr(Id(func),[Id(a),Id(b)]))])),FuncDecl(Id(func),[VarDecl(a,StringType),VarDecl(b,StringType)],IntType,Block([Return(CallExpr(Id(func),[Id(a),Id(b)]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,357))   
    def test_simple_program16(self):
        input = """int main()
{
    string c;
    c = "A";
    if( (c>="a" && c<="z") || (c>="A" && c<="Z"))
        printf("%c is an alphabet.",c);
    else
        printf("%c is not an alphabet.",c);
    return 0;
}"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(c,StringType),BinaryOp(=,Id(c),StringLiteral(A)),If(BinaryOp(||,BinaryOp(&&,BinaryOp(>=,Id(c),StringLiteral(a)),BinaryOp(<=,Id(c),StringLiteral(z))),BinaryOp(&&,BinaryOp(>=,Id(c),StringLiteral(A)),BinaryOp(<=,Id(c),StringLiteral(Z)))),CallExpr(Id(printf),[StringLiteral(%c is an alphabet.),Id(c)]),CallExpr(Id(printf),[StringLiteral(%c is not an alphabet.),Id(c)])),Return(IntLiteral(0))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,358))
    def test_simple_program17(self):
        input = """int i ;
int f ( ) {
    return 200;
}
void main ( ) {
    int main ;
    main = f ( ) ;
    putIntLn ( main ) ;
    {
        int i ;
        int main ;
        int f ;
        main = f = i = 100;
        putIntLn ( i ) ;
        putIntLn ( main ) ;
        putIntLn ( f ) ;
    }
    putIntLn ( main ) ;
}"""
        expect = "Program([VarDecl(i,IntType),FuncDecl(Id(f),[],IntType,Block([Return(IntLiteral(200))])),FuncDecl(Id(main),[],VoidType,Block([VarDecl(main,IntType),BinaryOp(=,Id(main),CallExpr(Id(f),[])),CallExpr(Id(putIntLn),[Id(main)]),Block([VarDecl(i,IntType),VarDecl(main,IntType),VarDecl(f,IntType),BinaryOp(=,Id(main),BinaryOp(=,Id(f),BinaryOp(=,Id(i),IntLiteral(100)))),CallExpr(Id(putIntLn),[Id(i)]),CallExpr(Id(putIntLn),[Id(main)]),CallExpr(Id(putIntLn),[Id(f)])]),CallExpr(Id(putIntLn),[Id(main)])]))])"             
        self.assertTrue(TestAST.checkASTGen(input,expect,359)) 
    def test_simple_program18(self):
        input = """int main(int a, float b)
{

    main(a,b);
    main(a,b);
    return a;
    continue;
    break;
}"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(a,IntType),VarDecl(b,FloatType)],IntType,Block([CallExpr(Id(main),[Id(a),Id(b)]),CallExpr(Id(main),[Id(a),Id(b)]),Return(Id(a)),Continue(),Break()]))])"    
        self.assertTrue(TestAST.checkASTGen(input,expect,360))
    def test_funccall(self):
        input = """int[] main(int a, float b)
{
    foo(a,b);
    break;
}"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(a,IntType),VarDecl(b,FloatType)],ArrayTypePointer(IntType),Block([CallExpr(Id(foo),[Id(a),Id(b)]),Break()]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,361))
    def test_exp_stmt(self):
        input = """int main(int a, float b)
{

    true + false;
    1.0E-2;
    foo(a,b);
    return foo(1,1.2e-3);
}"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(a,IntType),VarDecl(b,FloatType)],IntType,Block([BinaryOp(+,BooleanLiteral(true),BooleanLiteral(false)),FloatLiteral(0.01),CallExpr(Id(foo),[Id(a),Id(b)]),Return(CallExpr(Id(foo),[IntLiteral(1),FloatLiteral(0.0012)]))]))])"         
        self.assertTrue(TestAST.checkASTGen(input,expect,362))
    def test_exp_stmt1(self):
        input = """void main()
{
    if(-1){
        var=a-b;
        100+-100;
    }
    else
        {
        }

}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([If(UnaryOp(-,IntLiteral(1)),Block([BinaryOp(=,Id(var),BinaryOp(-,Id(a),Id(b))),BinaryOp(+,IntLiteral(100),UnaryOp(-,IntLiteral(100)))]),Block([]))]))])"         
        self.assertTrue(TestAST.checkASTGen(input,expect,363))
    def test_simple_program19(self):
        input = """void main()
{
    if(-1 / 2 -0.01 ==  8 && -1 ||1)
        do{

        }while(true);
}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([If(BinaryOp(||,BinaryOp(&&,BinaryOp(==,BinaryOp(-,BinaryOp(/,UnaryOp(-,IntLiteral(1)),IntLiteral(2)),FloatLiteral(0.01)),IntLiteral(8)),UnaryOp(-,IntLiteral(1))),IntLiteral(1)),Dowhile([Block([])],BooleanLiteral(true)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,364))
    def test_simple_program20(self):
        input = """void main()
{
    if(-1 /2 ==  8 && -1 || -2)
        do{
            for(i= 0 ; i>= 2; i = i * i){
                continue;
            } 
        }while(true);
}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([If(BinaryOp(||,BinaryOp(&&,BinaryOp(==,BinaryOp(/,UnaryOp(-,IntLiteral(1)),IntLiteral(2)),IntLiteral(8)),UnaryOp(-,IntLiteral(1))),UnaryOp(-,IntLiteral(2))),Dowhile([Block([For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(>=,Id(i),IntLiteral(2));BinaryOp(=,Id(i),BinaryOp(*,Id(i),Id(i)));Block([Continue()]))])],BooleanLiteral(true)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,365))
    def test_simple_program21(self):
        input = """int main(int a, float b)
{
    if(-1 /2 ==  8 && -1 || -2)
        do{
            for(i= 0 ; i>= 2; i = i * i)
                continue;
            {
            }
        }
        {
            100;           
        }
        while(true);
}"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(a,IntType),VarDecl(b,FloatType)],IntType,Block([If(BinaryOp(||,BinaryOp(&&,BinaryOp(==,BinaryOp(/,UnaryOp(-,IntLiteral(1)),IntLiteral(2)),IntLiteral(8)),UnaryOp(-,IntLiteral(1))),UnaryOp(-,IntLiteral(2))),Dowhile([Block([For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(>=,Id(i),IntLiteral(2));BinaryOp(=,Id(i),BinaryOp(*,Id(i),Id(i)));Continue()),Block([])]),Block([IntLiteral(100)])],BooleanLiteral(true)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,366))
    def test_simple_program22(self):
        input = """int main(int a, float b)
{
    if(-1 /2 ==  8 && -1 || -2)
        do{
            for(i= 0 ; i>= 2; i = i * i)
                9+2 * 12.1E-2 && false = 2 % -2 ;
            {
                if (exp)
                    stmt1;
                else
                    stmt2;
            }
        }
        {
            a=9>1==2 || 6<=5;           
        }
        while(1>=2);
}"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(a,IntType),VarDecl(b,FloatType)],IntType,Block([If(BinaryOp(||,BinaryOp(&&,BinaryOp(==,BinaryOp(/,UnaryOp(-,IntLiteral(1)),IntLiteral(2)),IntLiteral(8)),UnaryOp(-,IntLiteral(1))),UnaryOp(-,IntLiteral(2))),Dowhile([Block([For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(>=,Id(i),IntLiteral(2));BinaryOp(=,Id(i),BinaryOp(*,Id(i),Id(i)));BinaryOp(=,BinaryOp(&&,BinaryOp(+,IntLiteral(9),BinaryOp(*,IntLiteral(2),FloatLiteral(0.121))),BooleanLiteral(false)),BinaryOp(%,IntLiteral(2),UnaryOp(-,IntLiteral(2))))),Block([If(Id(exp),Id(stmt1),Id(stmt2))])]),Block([BinaryOp(=,Id(a),BinaryOp(||,BinaryOp(==,BinaryOp(>,IntLiteral(9),IntLiteral(1)),IntLiteral(2)),BinaryOp(<=,IntLiteral(6),IntLiteral(5))))])],BinaryOp(>=,IntLiteral(1),IntLiteral(2))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,367))
    def test_simple_program23(self):
        input = """string a[2];
int a;
string func(int a, int b, int c){
    func(func(),func(),a* a[1]+a[2]/a[0]);
    return func();
}"""
        expect = "Program([VarDecl(a,ArrayType(StringType,2)),VarDecl(a,IntType),FuncDecl(Id(func),[VarDecl(a,IntType),VarDecl(b,IntType),VarDecl(c,IntType)],StringType,Block([CallExpr(Id(func),[CallExpr(Id(func),[]),CallExpr(Id(func),[]),BinaryOp(+,BinaryOp(*,Id(a),ArrayCell(Id(a),IntLiteral(1))),BinaryOp(/,ArrayCell(Id(a),IntLiteral(2)),ArrayCell(Id(a),IntLiteral(0))))]),Return(CallExpr(Id(func),[]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,368))
    def test_simple_program24(self):
        input = """void main(){
    main = (1 < 2) + 3 >= 2 + - 1.3e2;
    main(main);
}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([BinaryOp(=,Id(main),BinaryOp(>=,BinaryOp(+,BinaryOp(<,IntLiteral(1),IntLiteral(2)),IntLiteral(3)),BinaryOp(+,IntLiteral(2),UnaryOp(-,FloatLiteral(130.0))))),CallExpr(Id(main),[Id(main)])]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,369))
    def test_simple_program25(self):
        input = """
float a,b;
int main(){
    if(b<=c)
        func(1);
}"""
        expect = "Program([VarDecl(a,FloatType),VarDecl(b,FloatType),FuncDecl(Id(main),[],IntType,Block([If(BinaryOp(<=,Id(b),Id(c)),CallExpr(Id(func),[IntLiteral(1)]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,370))
    def test_simple_program26(self):
        input = """int main(){
    a = 9.0e2 * 2 -2 + -(5 % 2) / !-3;
    func(main(2),150);
    if(-100)
        {  
        }
        else
            -200;
    return a;
}"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([BinaryOp(=,Id(a),BinaryOp(+,BinaryOp(-,BinaryOp(*,FloatLiteral(900.0),IntLiteral(2)),IntLiteral(2)),BinaryOp(/,UnaryOp(-,BinaryOp(%,IntLiteral(5),IntLiteral(2))),UnaryOp(!,UnaryOp(-,IntLiteral(3)))))),CallExpr(Id(func),[CallExpr(Id(main),[IntLiteral(2)]),IntLiteral(150)]),If(UnaryOp(-,IntLiteral(100)),Block([]),UnaryOp(-,IntLiteral(200))),Return(Id(a))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,371))
    def test_simple_program27(self):
        input = """int main(){
    a = 9.0e2 * 2 -2 + -(5 % 2) / !-3;
    func(a,150);
    if(true)
        {
            do{
                a=2/4-3+2.01 % 5;    
            }while (flag == true);
        }
        else
            -200;
    return a;
}"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([BinaryOp(=,Id(a),BinaryOp(+,BinaryOp(-,BinaryOp(*,FloatLiteral(900.0),IntLiteral(2)),IntLiteral(2)),BinaryOp(/,UnaryOp(-,BinaryOp(%,IntLiteral(5),IntLiteral(2))),UnaryOp(!,UnaryOp(-,IntLiteral(3)))))),CallExpr(Id(func),[Id(a),IntLiteral(150)]),If(BooleanLiteral(true),Block([Dowhile([Block([BinaryOp(=,Id(a),BinaryOp(+,BinaryOp(-,BinaryOp(/,IntLiteral(2),IntLiteral(4)),IntLiteral(3)),BinaryOp(%,FloatLiteral(2.01),IntLiteral(5))))])],BinaryOp(==,Id(flag),BooleanLiteral(true)))]),UnaryOp(-,IntLiteral(200))),Return(Id(a))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,372))
    def test_exp_stmt2(self):
        input = """
int a;
void foo(){
    n = (((((n))/3)));
}
"""
        expect = "Program([VarDecl(a,IntType),FuncDecl(Id(foo),[],VoidType,Block([BinaryOp(=,Id(n),BinaryOp(/,Id(n),IntLiteral(3)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,373))
    def test_func_decl5(self):

        input = """int __foo(int a[] ,int b){
    var = var1 == a/b;
}"""
        expect = "Program([FuncDecl(Id(__foo),[VarDecl(a,ArrayTypePointer(IntType)),VarDecl(b,IntType)],IntType,Block([BinaryOp(=,Id(var),BinaryOp(==,Id(var1),BinaryOp(/,Id(a),Id(b))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,374))
    def test_func_decl6(self):

        input = """float func(string var1, float var2, int var3){
    var1 = ((a/b));
    var2  + var3= (var1 && var2 || var3);
}"""
        expect = "Program([FuncDecl(Id(func),[VarDecl(var1,StringType),VarDecl(var2,FloatType),VarDecl(var3,IntType)],FloatType,Block([BinaryOp(=,Id(var1),BinaryOp(/,Id(a),Id(b))),BinaryOp(=,BinaryOp(+,Id(var2),Id(var3)),BinaryOp(||,BinaryOp(&&,Id(var1),Id(var2)),Id(var3)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,375))
    def test_func_decl7(self):
        input = """float func(string str, int a){
    float b;
    var1 =false + (b == 5.0);
    var2 = a / b;
    if (var1 != var2)
        return -1;
}"""
    
        expect = "Program([FuncDecl(Id(func),[VarDecl(str,StringType),VarDecl(a,IntType)],FloatType,Block([VarDecl(b,FloatType),BinaryOp(=,Id(var1),BinaryOp(+,BooleanLiteral(false),BinaryOp(==,Id(b),FloatLiteral(5.0)))),BinaryOp(=,Id(var2),BinaryOp(/,Id(a),Id(b))),If(BinaryOp(!=,Id(var1),Id(var2)),Return(UnaryOp(-,IntLiteral(1))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,376))
    def test_if_else_stmt2(self):
        """missing exp in ()"""
        input = """string func(){
    if((func(1))){
        a + 2;
        ((arr[a])[j])[k];
    }
    else{
        a * b ;
        return;
    }
}"""
    
        expect = "Program([FuncDecl(Id(func),[],StringType,Block([If(CallExpr(Id(func),[IntLiteral(1)]),Block([BinaryOp(+,Id(a),IntLiteral(2)),ArrayCell(ArrayCell(ArrayCell(Id(arr),Id(a)),Id(j)),Id(k))]),Block([BinaryOp(*,Id(a),Id(b)),Return()]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,377))
    def test_if_else_stmt3(self):

        input = """
float arr[4];
string func(){
    if(9-2){
        float a;
    }
    else
        arr[1+arr[i * i]];
}"""
        expect = "Program([VarDecl(arr,ArrayType(FloatType,4)),FuncDecl(Id(func),[],StringType,Block([If(BinaryOp(-,IntLiteral(9),IntLiteral(2)),Block([VarDecl(a,FloatType)]),ArrayCell(Id(arr),BinaryOp(+,IntLiteral(1),ArrayCell(Id(arr),BinaryOp(*,Id(i),Id(i))))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,378))
    def test_if_else_stmt4(self):
        """if is not followed by else"""
        input = """string func(){
    if(a == arr[4]){
        a = a + 2;
        float a;
    }
    else{
        /*comment*/
        break;
    }      
}"""
        expect = "Program([FuncDecl(Id(func),[],StringType,Block([If(BinaryOp(==,Id(a),ArrayCell(Id(arr),IntLiteral(4))),Block([BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(2))),VarDecl(a,FloatType)]),Block([Break()]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,379))
    def test_do_while_stmt6(self):
        input = """int main () {
    do{
        a=c= 5%4;
        cal(a,b,d);
    }while a != b * d + a <= b - (c && d); 
}
"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([Dowhile([Block([BinaryOp(=,Id(a),BinaryOp(=,Id(c),BinaryOp(%,IntLiteral(5),IntLiteral(4)))),CallExpr(Id(cal),[Id(a),Id(b),Id(d)])])],BinaryOp(!=,Id(a),BinaryOp(<=,BinaryOp(+,BinaryOp(*,Id(b),Id(d)),Id(a)),BinaryOp(-,Id(b),BinaryOp(&&,Id(c),Id(d))))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,380))
    def test_index_exp(self):
        input = """string func() {
    foo(3.1e-2)[func()] = a[b[2]] +3;
    continue;        
}
"""
        expect = "Program([FuncDecl(Id(func),[],StringType,Block([BinaryOp(=,ArrayCell(CallExpr(Id(foo),[FloatLiteral(0.031)]),CallExpr(Id(func),[])),BinaryOp(+,ArrayCell(Id(a),ArrayCell(Id(b),IntLiteral(2))),IntLiteral(3))),Continue()]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,381))  
    def test_for_stmt5(self):
        input = """int main() {
    int arr[10];
    for(i = 5;(i >=5 && i % 2 == 0); i = i-1)
        arr[i] = i * i;
}
"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(arr,ArrayType(IntType,10)),For(BinaryOp(=,Id(i),IntLiteral(5));BinaryOp(&&,BinaryOp(>=,Id(i),IntLiteral(5)),BinaryOp(==,BinaryOp(%,Id(i),IntLiteral(2)),IntLiteral(0)));BinaryOp(=,Id(i),BinaryOp(-,Id(i),IntLiteral(1)));BinaryOp(=,ArrayCell(Id(arr),Id(i)),BinaryOp(*,Id(i),Id(i))))]))])"    
        self.assertTrue(TestAST.checkASTGen(input,expect,382))
    def test_for_stmt6(self):

        input = """int main() {
    for(i = 0;(i < 100 || i % 2 ==1) && true;i = i * 2){
        exp1;
        exp2;
        if (exp1 = false)
            break;
    }
}
"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(&&,BinaryOp(||,BinaryOp(<,Id(i),IntLiteral(100)),BinaryOp(==,BinaryOp(%,Id(i),IntLiteral(2)),IntLiteral(1))),BooleanLiteral(true));BinaryOp(=,Id(i),BinaryOp(*,Id(i),IntLiteral(2)));Block([Id(exp1),Id(exp2),If(BinaryOp(=,Id(exp1),BooleanLiteral(false)),Break())]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,383))
    def test_block_nested(self):
        input = """int main() {
    {
        {
            {
            }
        }
    }
}
"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([Block([Block([Block([])])])]))])"    
        self.assertTrue(TestAST.checkASTGen(input,expect,384))
    def test_all_stmt7(self):
        input = """int main()
{
    float number1;
    number1=-12.5e2;
    printf("number1 = ", number1);
    return 0.0;
}"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(number1,FloatType),BinaryOp(=,Id(number1),UnaryOp(-,FloatLiteral(1250.0))),CallExpr(Id(printf),[StringLiteral(number1 = ),Id(number1)]),Return(FloatLiteral(0.0))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,385))
    def test_all_stmt8(self):
        input = """int[] main()
{
    if( a &&b){
        string str[2];
        foo(str[3],"string");   
    }
     return 0 ;
}"""
        expect = "Program([FuncDecl(Id(main),[],ArrayTypePointer(IntType),Block([If(BinaryOp(&&,Id(a),Id(b)),Block([VarDecl(str,ArrayType(StringType,2)),CallExpr(Id(foo),[ArrayCell(Id(str),IntLiteral(3)),StringLiteral(string)])])),Return(IntLiteral(0))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,386))
    def test_many_funcdecl(self):

        input = """
float func(int a,float b){
    return a+b;
}
int[] main(int a, float a[])
{
    b = 1.0e-2;
    func(a,b);
}"""
        expect = "Program([FuncDecl(Id(func),[VarDecl(a,IntType),VarDecl(b,FloatType)],FloatType,Block([Return(BinaryOp(+,Id(a),Id(b)))])),FuncDecl(Id(main),[VarDecl(a,IntType),VarDecl(a,ArrayTypePointer(FloatType))],ArrayTypePointer(IntType),Block([BinaryOp(=,Id(b),FloatLiteral(0.01)),CallExpr(Id(func),[Id(a),Id(b)])]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,387))
    def test_many_funcdecl1(self):
        input = """
string [] foo1(string a){
    a = "string";
    return a ;
}
void foo2(){
}
int main()
{
    for(exp1;exp2;exp3){
        do{
            continue;
        }while(true);
    }       
}"""
        expect = "Program([FuncDecl(Id(foo1),[VarDecl(a,StringType)],ArrayTypePointer(StringType),Block([BinaryOp(=,Id(a),StringLiteral(string)),Return(Id(a))])),FuncDecl(Id(foo2),[],VoidType,Block([])),FuncDecl(Id(main),[],IntType,Block([For(Id(exp1);Id(exp2);Id(exp3);Block([Dowhile([Block([Continue()])],BooleanLiteral(true))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,388))
    def test_many_funcdecl2(self):
        input = """
int func1(int a, int b){
    b = a + b;
    return b ;
}
void func2(){
}
boolean check( int n){
    if (n % 2 == 0)
        return true;
    else
        return false;
}
int main()
{
    int a,b,n;
    func1(a,b);
    check(n);
}"""
        expect = "Program([FuncDecl(Id(func1),[VarDecl(a,IntType),VarDecl(b,IntType)],IntType,Block([BinaryOp(=,Id(b),BinaryOp(+,Id(a),Id(b))),Return(Id(b))])),FuncDecl(Id(func2),[],VoidType,Block([])),FuncDecl(Id(check),[VarDecl(n,IntType)],BoolType,Block([If(BinaryOp(==,BinaryOp(%,Id(n),IntLiteral(2)),IntLiteral(0)),Return(BooleanLiteral(true)),Return(BooleanLiteral(false)))])),FuncDecl(Id(main),[],IntType,Block([VarDecl(a,IntType),VarDecl(b,IntType),VarDecl(n,IntType),CallExpr(Id(func1),[Id(a),Id(b)]),CallExpr(Id(check),[Id(n)])]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,389))
    def test_many_funcdecl3(self):
        input = """
void reverseSentence(string c)
{
    if( c != "\\n")
    {
        reverseSentence();
        printf("%c",c);
    }
}
void main(string str)
{
    reverseSentence(str);
}"""   

        expect = "Program([FuncDecl(Id(reverseSentence),[VarDecl(c,StringType)],VoidType,Block([If(BinaryOp(!=,Id(c),StringLiteral(\\n)),Block([CallExpr(Id(reverseSentence),[]),CallExpr(Id(printf),[StringLiteral(%c),Id(c)])]))])),FuncDecl(Id(main),[VarDecl(str,StringType)],VoidType,Block([CallExpr(Id(reverseSentence),[Id(str)])]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,390))
    def test_simple_program28(self):
        input = """
void func( int arr1[], float arr2[]){
    var = 1.0 + 1;
    printf(var);
}
int main(){
    string arr[10];
    func(arr[0],arr[1]);
}
"""
        expect = "Program([FuncDecl(Id(func),[VarDecl(arr1,ArrayTypePointer(IntType)),VarDecl(arr2,ArrayTypePointer(FloatType))],VoidType,Block([BinaryOp(=,Id(var),BinaryOp(+,FloatLiteral(1.0),IntLiteral(1))),CallExpr(Id(printf),[Id(var)])])),FuncDecl(Id(main),[],IntType,Block([VarDecl(arr,ArrayType(StringType,10)),CallExpr(Id(func),[ArrayCell(Id(arr),IntLiteral(0)),ArrayCell(Id(arr),IntLiteral(1))])]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,391))
    def test_simple_program29(self):
        input = """
int checkPrimeNumber(int n)
{
    int j, flag;
    flag = 1;
    for(j=2; j <= n/2; j = j + 1)
    {
        if (n % j == 0)
        {
            flag =0;
            break;
        }
    }
    return flag;
}
int main(){
    checkPrimeNumber(5);
    return 1;
}
"""
        expect = "Program([FuncDecl(Id(checkPrimeNumber),[VarDecl(n,IntType)],IntType,Block([VarDecl(j,IntType),VarDecl(flag,IntType),BinaryOp(=,Id(flag),IntLiteral(1)),For(BinaryOp(=,Id(j),IntLiteral(2));BinaryOp(<=,Id(j),BinaryOp(/,Id(n),IntLiteral(2)));BinaryOp(=,Id(j),BinaryOp(+,Id(j),IntLiteral(1)));Block([If(BinaryOp(==,BinaryOp(%,Id(n),Id(j)),IntLiteral(0)),Block([BinaryOp(=,Id(flag),IntLiteral(0)),Break()]))])),Return(Id(flag))])),FuncDecl(Id(main),[],IntType,Block([CallExpr(Id(checkPrimeNumber),[IntLiteral(5)]),Return(IntLiteral(1))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,392))
    def test_do_while_stmt7(self):
        input = """
int main(){
    do {        
    }
    a = a+1;
    true;
    {
    }while 1;
}
"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([Dowhile([Block([]),BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1))),BooleanLiteral(true),Block([])],IntLiteral(1))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,393))
    def test_simple_program30(self):
        input = """
void main(){
    if("string"){
        for(n = 1 && i = 100; n<=i; i = i-5 && n = n * 2){
            break;
        }
    }
}
"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([If(StringLiteral(string),Block([For(BinaryOp(=,Id(n),BinaryOp(=,BinaryOp(&&,IntLiteral(1),Id(i)),IntLiteral(100)));BinaryOp(<=,Id(n),Id(i));BinaryOp(=,Id(i),BinaryOp(=,BinaryOp(&&,BinaryOp(-,Id(i),IntLiteral(5)),Id(n)),BinaryOp(*,Id(n),IntLiteral(2))));Block([Break()]))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,394))
    def test_for_stmt_nested(self):
        input = """
void main(){
    for(exp1;exp2;exp3){ for(exp1;exp2;exp3){ for(exp1;exp2;exp3){for(exp1;exp2;exp3){}}}}
}
"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([For(Id(exp1);Id(exp2);Id(exp3);Block([For(Id(exp1);Id(exp2);Id(exp3);Block([For(Id(exp1);Id(exp2);Id(exp3);Block([For(Id(exp1);Id(exp2);Id(exp3);Block([]))]))]))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,395))  
    def test_do_while_stmt_nested(self):
        input = """
void main(){
    do do do do {} while exp; while exp; while exp; while exp;
}
"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([Dowhile([Dowhile([Dowhile([Dowhile([Block([])],Id(exp))],Id(exp))],Id(exp))],Id(exp))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,396)) 
    def test_if_stmt_nested(self):
        input = """
void main(){
    if (1)
        if(1)
            if(1)
                if(1)
                    print("Hello");
                else{
                }
            else{
            }
        else{
        }
    else{
    }
}
"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([If(IntLiteral(1),If(IntLiteral(1),If(IntLiteral(1),If(IntLiteral(1),CallExpr(Id(print),[StringLiteral(Hello)]),Block([])),Block([])),Block([])),Block([]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,397))
    def test_funcall_nested(self):
        input = """
string foo(string c){
    return c;
}
void main(){
    str= "Hello";
    foo(foo(foo(foo(foo(foo(str))))));
}
"""
        expect = "Program([FuncDecl(Id(foo),[VarDecl(c,StringType)],StringType,Block([Return(Id(c))])),FuncDecl(Id(main),[],VoidType,Block([BinaryOp(=,Id(str),StringLiteral(Hello)),CallExpr(Id(foo),[CallExpr(Id(foo),[CallExpr(Id(foo),[CallExpr(Id(foo),[CallExpr(Id(foo),[CallExpr(Id(foo),[Id(str)])])])])])])]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,398)) 
    def test_all_nested(self):
        input = """

void main(){
    if (1)
        if(1)
            if(1)
                if(1)
                    do do do do {} while exp; while exp; while exp; while exp;
                else{
                    for(exp1;exp2;exp3){ for(exp1;exp2;exp3){ for(exp1;exp2;exp3){for(exp1;exp2;exp3){}}}}
                }
            else{
            }
        else{
        }
    else{
    }
}
"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([If(IntLiteral(1),If(IntLiteral(1),If(IntLiteral(1),If(IntLiteral(1),Dowhile([Dowhile([Dowhile([Dowhile([Block([])],Id(exp))],Id(exp))],Id(exp))],Id(exp)),Block([For(Id(exp1);Id(exp2);Id(exp3);Block([For(Id(exp1);Id(exp2);Id(exp3);Block([For(Id(exp1);Id(exp2);Id(exp3);Block([For(Id(exp1);Id(exp2);Id(exp3);Block([]))]))]))]))])),Block([])),Block([])),Block([]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,399))   





          





    


            








            


        
        



    



    

    
           
