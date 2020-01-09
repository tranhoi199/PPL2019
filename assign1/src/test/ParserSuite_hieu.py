import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):

    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """int main() {}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))

    def test_more_complex_program(self):
        """More complex program"""
        input = """int main () {
            putIntLn(4);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,202))
    
    def test_wrong_miss_close(self):
        """Miss ) int main( {}"""
        input = """int main( {}"""
        expect = "Error on line 1 col 10: {"
        self.assertTrue(TestParser.checkParser(input,expect,203))
    def test_var_decl(self):
        
        input = """int a ;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,204))
    def test_exp(self):
        
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,205))
    
    def test_function_call(self):
        input = """
        int main(){
            func((arr[i])[j]);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,206))
    def test_error_missing(self):
        input = """}"""
        expect = "Error on line 1 col 0: }"
        self.assertTrue(TestParser.checkParser(input,expect,207))
    def test_var_decl1(self):
        input = """
            string _a;
            float t;
            boolean a, f2, r3, arr[5];
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,208))
    def test_var_decl_error(self):
        input = """float t =0.5;
string a, f2, r3, arr[5];
void a;
        """
        expect = "Error on line 1 col 8: ="
        self.assertTrue(TestParser.checkParser(input,expect,209))
    def test_var_decl_error1(self):
        input = """hello var;"""
        expect = "Error on line 1 col 0: hello"
        self.assertTrue(TestParser.checkParser(input,expect,210))
    def test_var_decl_void_error(self):
        input = """int main(){
    string arr[4],a2;
    void var;            
}
        """
        expect = "Error on line 3 col 4: void"
        self.assertTrue(TestParser.checkParser(input,expect,211))
    def test_array_decl_error(self):
        input = """float foo(){
    string arr[];               
}
        """
        expect = "Error on line 2 col 15: ]"
        self.assertTrue(TestParser.checkParser(input,expect,212))
    def test_valid_program(self):
        input = """
        int main(){
            do { }
            while((arr[i])[j]);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,213))
    def test_func_decl(self):
        input = """string func1(){}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,214))
    def test_func_decl1(self):
        input = """boolean func1(boolean arg1, int arg2, float arr[]){}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,215))
    def test_func_decl2(self):
        input = """float func_test (string str[], int a){
    a = a + 1;
    func_test(str[2], a+2);
            
}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,216))
    def test_func_decl3(self):
        """"""
        input = """int __foo(){
    if(var!=0) print("hello");
}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,217))
    def test_func_decl_error(self):
        """Missing ()"""
        input = """int __foo{
    var = a/b;
}"""
        expect = "Error on line 1 col 9: {"
        self.assertTrue(TestParser.checkParser(input,expect,218))
    def test_func_decl_error1(self):
        """Missing ,"""
        input = """float func(string var1, float var2 int var3){
    var1 = a/b;
    var2 + var3 = var4 % 4;
}"""
        expect = "Error on line 1 col 35: int"
        self.assertTrue(TestParser.checkParser(input,expect,219))
    def test_func_decl_error2(self):
        """having number in array"""
        input = """float func(string var1[5], int a){
    float b;
    b= 5.0;
    var1 = a % b;
}"""
    
        expect = "Error on line 1 col 23: 5"
        self.assertTrue(TestParser.checkParser(input,expect,220))
    def test_if_stmt(self):
        """test if stmt"""
        input = """int main(){
    if(a || b){
        100;
        foo(1,2);
    }
}"""
    
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,221))
    def test_if_stmt1(self):
        """test if stmt"""
        input = """float a;
int main(){
    if(true){
        printf("successful");
    }
    else
        printf("error");
}"""
    
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,222))
    def test_if_stmt2(self):

        input = """int main(){
    if(arr[i]){
        a;
        ((arr[a])[j])[k];
    }
    else{
        a && b ;
    }
}"""
    
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,223))
    def test_if_stmt_error(self):
        """missing exp in ()"""
        input = """string func(){
    if(){
        a + 2;
        ((arr[a])[j])[k];
    }
    else{
        a * b ;
        return;
    }
}"""
    
        expect = "Error on line 2 col 7: )"
        self.assertTrue(TestParser.checkParser(input,expect,224))
    def test_if_stmt3(self):
        """null block in if"""
        input = """string func(){
    if(false){
    }
    else{
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,225))
    def test_if_stmt_error1(self):
        """missing exp after else"""
        input = """string func(){
    if(9-2){
        float a;
    }
    else
}"""
        expect = "Error on line 6 col 0: }"
        self.assertTrue(TestParser.checkParser(input,expect,226))
    def test_if_stmt_error2(self):
        """more than one exp in if"""
        input = """string func(){
    if(9-2)
        float a;
        a = a + 2;     
}"""
        expect = "Error on line 3 col 8: float"
        self.assertTrue(TestParser.checkParser(input,expect,227))
    def test_if_stmt_4(self):
        """more than one exp in if"""
        input = """string func(){
    if(2)
        a = a + 2;
        float a;      
}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,228))
    def test_if_stmt_error3(self):
        """if is not followed by else"""
        input = """string func(){
    if(var1 != arr[4])
        a = a + 2;
        float a;
    else{
    }      
}"""
        expect = "Error on line 5 col 4: else"
        self.assertTrue(TestParser.checkParser(input,expect,229))
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,230))
    def test_do_while_stmt1(self):
        """test do while stmt"""
        input = """void main() {
    do{
    }
    while (1);
}
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,231))
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,232))
    def test_do_while_stmt3(self):
        """test do while stmt"""
        input = """int main () {

    do {
        func(x%4)[a[i]]; 
    }while(!5);
    return -1;
}
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,233))
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,234))
    def test_do_while_stmt_error1(self):
        """missing while"""
        input = """int main () {
    do{
        a=c= 5%4;
        cal(a,b,d);
    } 
}
"""
        expect = "Error on line 6 col 0: }"
        self.assertTrue(TestParser.checkParser(input,expect,235))
    def test_do_while_stmt_error2(self):
        """missing ; after while"""
        input = """int main () {
    do{
        a=c= 5%4;
        cal(a,b,d);
    }while(arr[true])
}
"""
        expect = "Error on line 6 col 0: }"
        self.assertTrue(TestParser.checkParser(input,expect,236))
    def test_do_while_stmt_error3(self):
        """missing exp in while()"""
        input = """void main () {
    do{
        foo(x+3);
    }while();
}
"""
        expect = "Error on line 4 col 11: )"
        self.assertTrue(TestParser.checkParser(input,expect,237))
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,238))
    def test_index_exp(self):
        """test_index_exp"""
        input = """string func() {
    foo(2)[3+x] = a[b[2]] +3;
    break;        
}
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,239))
    def test_index_exp_error(self):
        """missing exp"""
        input = """string func() {
    foo(3.1e-2)[] = a[b[2]] +3;
    continue;        
}
"""
        expect = "Error on line 2 col 16: ]"
        self.assertTrue(TestParser.checkParser(input,expect,240))
    def test_for_stmt(self):
        """test for stmt"""
        input = """boolean ptr[4],_a,_b;
int func() {
    for( i =0;i <=5;i=i+1)
        func2(ptr[2],_a,_b);     
}
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,241))
    def test_for_stmt1(self):
        """test for stmt"""
        input = """int ptr[4],_a,_b;
void func() {
    for( i =0;i <=5;i=i+1){
        func2(ptr[2],_a,_b);
        func3();
    }    
}
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,242))
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,243))
    def test_for_stmt3(self):
        """test for stmt"""
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,244))
    def test_for_stmt_error(self):
        """missing exp3"""
        input = """int main() {
    for(i = 5;i >=5;)
        -2.14E2+8;
}
"""
        expect = "Error on line 2 col 20: )"
        self.assertTrue(TestParser.checkParser(input,expect,245))
    def test_for_stmt_error1(self):
        """for is followed by ;"""
        input = """int main() {
    for(i = 5;i >=5;i=8);{
        exp1;
        exp2;
    }
}
"""
        expect = "Error on line 2 col 24: ;"
        self.assertTrue(TestParser.checkParser(input,expect,246))
    def test_for_stmt_error2(self):
        """using , instead ;"""
        input = """int main() {
    for(i = 5,i!=2,i=i-1)
        exp;
}
"""
        expect = "Error on line 2 col 13: ,"
        self.assertTrue(TestParser.checkParser(input,expect,247))
    def test_for_stmt_error3(self):
        """missing exp"""
        input = """float[] func(string a, string b){
    for(i = 5;i==2;i=i-1)
}
"""
        expect = "Error on line 3 col 0: }"
        self.assertTrue(TestParser.checkParser(input,expect,248))
    def test_all_stmt(self):
        """test all stmt"""
        input = """string[] ABS(string a, int w[]){
    {
    }
    {    
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,249))
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,250))
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,251))
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,252))
    def test_all_stmt4(self):
        """test all stmt"""
        input = """int trim(string s[])
{
    int n;
    for (n = strlen(s)-1; n >= 0; n= n /2)
    if (s[n] != " " && s[n] != "\\t" && s[n] != "\\n")
        break;
    s[n+1] = "0";
    return n;
}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,253))
    def test_all_stmt5(self):
        """test all stmt"""
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,254))
    def test_all_stmt_error(self):
        """missing ; after return"""
        input = """int main()
{
    float number1;
    number1=-12.5e2;
    printf("number1 = ", number1);
    return 0
}"""
        expect = "Error on line 7 col 0: }"
        self.assertTrue(TestParser.checkParser(input,expect,255))
    def test_all_stmt_error1(self):
        """missing } """
        input = """int main()
{
    if( a &&b){
        string str[2];
        foo(str[3],"string");
    return 0 ;
}"""
        expect = "Error on line 7 col 1: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,256))
    def test_all_stmt_error2(self):
        """using ; in func call """
        input = """int[] main(int a, float a[])
{
    func(a;"aaaaaaa");
}"""
        expect = "Error on line 3 col 10: ;"
        self.assertTrue(TestParser.checkParser(input,expect,257))
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,258))
    def test_for_stmt_error4(self):
        """more than 3 exp in for loop"""
        input = """int main()
{
   int i,j;
   for (i=1; i<3 || j<5; i=i+1;j=j+1)
   {
	    printf("%d, %d",i ,j);
   }
   return 0;
}"""
        expect = "Error on line 4 col 30: ;"
        self.assertTrue(TestParser.checkParser(input,expect,259))
    def test_func_call(self):
        """test function call"""
        input = """int main()
{
    func1(foo(x%2),foo(foo(x+3,5.01*0.e-2),foo("string \\\\")));
    return 0;
}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,260))
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,261))
    def test_all_stmt_error3(self):
        """break followed by exp"""
        input = """int main()
{
    for(exp1;exp2;exp3){
        do{
            break 1;
        }while(true);
    }       
}"""
        expect = "Error on line 5 col 18: 1"
        self.assertTrue(TestParser.checkParser(input,expect,262))
    def test_all_stmt_error4(self):
        """func declaration in func declaration"""
        input = """int main( )
{
    float(int a, int b){

    }      
}"""
        expect = "Error on line 3 col 9: ("
        self.assertTrue(TestParser.checkParser(input,expect,263))
    def test_invalid_program(self):
        """having exp  in function"""
        input = """int a;
        a = a+2;
        int main(){

        } 
        """
        expect = "Error on line 2 col 8: a"
        self.assertTrue(TestParser.checkParser(input,expect,264))
    def test_invalid_program1(self):
        """missing id"""
        input = """string[] func(boolean a,int b,string ){
            {    
            }
        }
        """
        expect = "Error on line 1 col 37: )"
        self.assertTrue(TestParser.checkParser(input,expect,265))
    def test_invalid_program2(self):
        """if stmt followed by var decl"""
        input = """string[] func(boolean a,int b,string c[]){
            if( b || true ==a)
                string a;
                a = " ";
        }
        """
        expect = "Error on line 3 col 16: string"
        self.assertTrue(TestParser.checkParser(input,expect,266))
    def test_invalid_program3(self):
        """mising index of array element"""
        input = """float func(boolean a,int b,string c[]){
            string str;
            if( b || true ==a)
                str = " ";
                str = c[];
        }
        """
        expect = "Error on line 5 col 24: ]"
    
        self.assertTrue(TestParser.checkParser(input,expect,267))
    def test_invalid_program4(self):
        """ID  is siminar with some keyword """
        input = """float int(){
            func();
            return 0.0;
        }
        """
        expect = "Error on line 1 col 6: int"
    
        self.assertTrue(TestParser.checkParser(input,expect,268))
    def test_invalid_program5(self):
        """ID  is siminar with some keyword """
        input = """void func(){
            int continue;
            continue == continue && false;
        }
        """
        expect = "Error on line 2 col 16: continue"    
        self.assertTrue(TestParser.checkParser(input,expect,269))
    def test_invalid_program6(self):
        """ID  is siminar with some keyword """
        input = """void func( int arr1[], float arr2[]){
            for = int + 1;
        }
        """
        expect = "Error on line 2 col 16: ="   
        self.assertTrue(TestParser.checkParser(input,expect,270))
    def test_invalid_program7(self):
        """void array pointer"""
        input = """void[] func(){
    {
    }
}"""
        expect = "Error on line 1 col 4: ["   
        self.assertTrue(TestParser.checkParser(input,expect,271))
    
    def test_valid_program1(self):
        input = """int main(string args[]){
    int a , b , c ;
    a=b=c=5;
    float f[5] ;
    if ( a==b) f[0] = 1.0;
}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,272))
    def test_valid_program2(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,273))
    def test_valid_program3(self):
        input = """int main(){
    float a , b , c, d;
    a+ -2 *!5 *b /c &&d;
    return -1;
}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,274))
    def test_valid_program4(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,275))
    def test_valid_program5(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,276))
    def test_valid_program6(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,277))
    def test_valid_program7(self):
        input = """int[] func(){
    int arr[3];
    arr[3]=(arr[0] + arr[1]) % (arr[arr[3-1]]);
    return arr[3];
}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,278))
    def test_invalid_program8(self):
        """return must be followed by exp"""
        input = """int[] func(){
    int arr[3];
    arr[3]= a - b* d --2 % (4<=3);
    return arr[];
}"""
        expect = "Error on line 4 col 15: ]"
        self.assertTrue(TestParser.checkParser(input,expect,279))
    def test_invalid_program9(self):
        """error with exp !"""
        input = """float func(){
    float a,b,d,arr[3];
    foo(a%5)[2] / b !c * d; 
    return 1.0;
}"""
        expect = "Error on line 3 col 20: !"
        self.assertTrue(TestParser.checkParser(input,expect,280))
    def test_valid_program8(self):
        input = """float main(){
    true||false &&1*-2;
    return -3.;
}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,281))
    def test_valid_program9(self):
        input = """void main(){
    if(a >= b = c - d % 2.e2)
        a && b  != d  + c / -a+ !true;
    else
        func(a,b,c,d);
}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,282))
    def test_valid_program10(self):
        input = """void main(){
    if(a >= b = c - d % 2.e2)
        a && b  != d  + c / -a+ !true;
    else
        func(a,b,c,d);
}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,283))
    def test_valid_program11(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,284))
    def test_valid_program12(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,285))
    def test_valid_program13(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,286))
    def test_valid_program14(self):
        input = """int main(int a, float b)
{

    main(a,b);
    main(a,b);
    return a;
    continue;
    break;
}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,287))
    def test_invalid_program10(self):
        """break followed by id"""
        input = """int[] main(int a, float b)
{
    foo(a,b);
    break a;
}"""
        expect = "Error on line 4 col 10: a"
        self.assertTrue(TestParser.checkParser(input,expect,288))
    def test_invalid_program11(self):
        """break followed by id"""
        input = """int main(int a, float b)
{

    true;
    1.0;
    foo(a;b);
    return 1;
}"""
        expect = "Error on line 6 col 9: ;"
        self.assertTrue(TestParser.checkParser(input,expect,289))
    def test_invalid_program12(self):
        """else is illegal"""
        input = """void main()
{
    if(-1)
        var=a-b;
        100+-100;
    else
        {
        }

}"""
        expect = "Error on line 6 col 4: else"
        self.assertTrue(TestParser.checkParser(input,expect,290))
    def test_invalid_program13(self):
        """else is illegal"""
        input = """void main()
{
    if(-1)
        var=a-b;
        100+-100;
    else
        {
        }

}"""
        expect = "Error on line 6 col 4: else"
        self.assertTrue(TestParser.checkParser(input,expect,291))
    def test_invalid_program14(self):
        """exp +2 error"""
        input = """void main()
{
    if(-1 / 2 -0.01 ==  8 && -1 || + 2)
        do{

        }while(true);
}"""
        expect = "Error on line 3 col 35: +"
        self.assertTrue(TestParser.checkParser(input,expect,292))
    def test_invalid_program15(self):
        """exp +2 error"""
        input = """void main()
{
    if(-1 /2 ==  8 && -1 || -2)
        do{
            for(int i= 0 ; i>= 2; i = i * i){
                continue;
            } 
        }while(true);
}"""
        expect = "Error on line 5 col 16: int"
        self.assertTrue(TestParser.checkParser(input,expect,293))
    def test_valid_program15(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,294))
    def test_valid_program16(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,295))
    def test_valid_program17(self):
        input = """string a[2];
int a;
string func(int a, int b, int c){
    func(func(),func(),a* a[1]+a[2]/a[0]);
    return func();
}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,296))
    def test_valid_program18(self):
        input = """void main(){
    main = (1 < 2) + 3 >= 2 + - 1.3e2;
    main(main);
}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,297))
    def test_invalid_program16(self):
        """error with exp has associativity none"""
        input = """int main(){
        if(a<b<=c)
            func(1);
}"""
        expect = "Error on line 2 col 14: <="
        self.assertTrue(TestParser.checkParser(input,expect,298))
    def test_invalid_program17(self):
        """missing ) after if"""
        input = """int main(){
    a = 9.0e2 * 2 -2 + -(5 % 2) / !-3;
    func(main(),150);
    if(-100
        {  
        }
        else
            -200;
    return a;
}"""
        expect = "Error on line 5 col 8: {"
        self.assertTrue(TestParser.checkParser(input,expect,299))
    def test_invalid_program18(self):
        """missing while"""
        input = """int main(){
    a = 9.0e2 * 2 -2 + -(5 % 2) / !-3;
    func(a,150);
    if(true)
        {
            do{
                a=2/4-3+2.01 % 5;    
            }
        }
        else
            -200;
    return a;
}"""
        expect = "Error on line 9 col 8: }"
        self.assertTrue(TestParser.checkParser(input,expect,300))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    