import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
# test id
    def test_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc","abc,<EOF>",101))
    def test_identifier3(self):
        self.assertTrue(TestLexer.checkLexeme("aCBbdc","aCBbdc,<EOF>",102))
    def test_identifier4(self):
        self.assertTrue(TestLexer.checkLexeme("AsVN","AsVN,<EOF>",103))
    def test_identifier5(self):
        self.assertTrue(TestLexer.checkLexeme("_AsVN","_AsVN,<EOF>",104))
    def test_identifier1(self):
        """test identifiers1"""
        self.assertTrue(TestLexer.checkLexeme("____","____,<EOF>",105))
    def test_identifier2(self):
        """test identifiers2"""
        self.assertTrue(TestLexer.checkLexeme("s_2axc","s_2axc,<EOF>",106))
    def test_keyword(self):
        """test keyword"""
        self.assertTrue(TestLexer.checkLexeme("void","void,<EOF>",107))
    def test_keyword1(self):
        """test keyword"""
        self.assertTrue(TestLexer.checkLexeme("float","float,<EOF>",108))
    def test_line_comment(self):
        """test linecomment"""
        self.assertTrue(TestLexer.checkLexeme("// dfjgjdfgj","<EOF>",109))
    def test_block_comment(self):
        """test linecomment"""
        self.assertTrue(TestLexer.checkLexeme("""/*jfkv,$%$2@\ndfdf\t
            dfgjdjfgjdfg
            dfgjdfjgjdjfg*/""","<EOF>",110))
    def test_line_comment1(self):
        """test linecomment"""
        self.assertTrue(TestLexer.checkLexeme("// dfjgjdfgjd@#$fddfsdfsdf ","<EOF>",111))
    def test_operator(self):
        """test operator"""
        self.assertTrue(TestLexer.checkLexeme("+ - * /","+,-,*,/,<EOF>",112))
    def test_operator1(self):
        """test operater1"""
        self.assertTrue(TestLexer.checkLexeme("a + b = c ","a,+,b,=,c,<EOF>",113))
    def test_intlit(self):
        """test int"""
        self.assertTrue(TestLexer.checkLexeme("221144","221144,<EOF>",114))
    def test_intlit1(self):
        """test int"""
        self.assertTrue(TestLexer.checkLexeme("25aa3","25,aa3,<EOF>",115))
    def test_floatlit(self):
        """test float"""
        self.assertTrue(TestLexer.checkLexeme("1.2","1.2,<EOF>",116))
    def test_floatlit1(self):
        """test float"""
        self.assertTrue(TestLexer.checkLexeme("1e2","1e2,<EOF>",117))
    def test_floatlit2(self):
        """test float"""
        self.assertTrue(TestLexer.checkLexeme("1.","1.,<EOF>",118))
    def test_boolean(self):
        """test boolean"""
        self.assertTrue(TestLexer.checkLexeme("true","true,<EOF>",119))
    
    def test_floatlit3(self):
        """test float"""
        self.assertTrue(TestLexer.checkLexeme(".1",".1,<EOF>",120))
    def test_floatlit4(self):
        """test float"""
        self.assertTrue(TestLexer.checkLexeme("1.2E-2","1.2E-2,<EOF>",121))
    def test_floatlit5(self):
        """test float"""
        self.assertTrue(TestLexer.checkLexeme(".1E2",".1E2,<EOF>",122))
    def test_floatlit6(self):
        """test float"""
        self.assertTrue(TestLexer.checkLexeme("1.e-2 ","1.e-2,<EOF>",123))
    def test_floatlit7(self):
        """test float"""
        self.assertTrue(TestLexer.checkLexeme("128e-42 ","128e-42,<EOF>",124))
    def test_type(self):
        """test type"""
        self.assertTrue(TestLexer.checkLexeme("int a = 3; ","int,a,=,3,;,<EOF>",125))
    def test_type1(self):
        """test type"""
        self.assertTrue(TestLexer.checkLexeme("float b = 3.1e1; ","float,b,=,3.1e1,;,<EOF>",126))
    def test_string(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme("\"this is my string\"","this is my string,<EOF>",127))
    def test_string2(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme("\"this is my string\\n\"","this is my string\\n,<EOF>",129))
    def test_string_ellegal(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme('"he is \\a "',"Illegal Escape In String: he is \\a",128))
    def test_string3(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme('"he is \a"',"he is \a,<EOF>",130))
    def test_string_unclosed(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme('"he is \n a student"',"Unclosed String: he is ",131))
    def test_string4(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme('"this is\\" my string\\""','this is\\" my string\\",<EOF>',132))
    def test_string5(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme('"string1" "string2" "string3"','string1,string2,string3,<EOF>',133))
    def test_string6(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme('"this \"is\" my string"','this ,is, my string,<EOF>',134))
    def test_string_unclosed1(self):
        """test string"""
        input=""" "test string\n" """
        self.assertTrue(TestLexer.checkLexeme(input,"Unclosed String: test string",135))
    def test_string_illegal1(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme('"test string illegal \\  illegal"',"Illegal Escape In String: test string illegal \\ ",136))
    def test_string_ellegal2(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme('"test string \i illegal"',"Illegal Escape In String: test string \i",137))
    def test_string_unclosed2(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme('"test unclosed string',"Unclosed String: test unclosed string",138))
    def test_errortoken(self):
        """test errortoken"""
        self.assertTrue(TestLexer.checkLexeme("\\","Error Token \\",139))
    def test_errortoken1(self):
        """test errortoken"""
        self.assertTrue(TestLexer.checkLexeme("abc@abc","abc,Error Token @",140))
    def test_errortoken2(self):
        """test errortoken"""
        self.assertTrue(TestLexer.checkLexeme("HELLO #","HELLO,Error Token #",141))
    def test_all(self):
        """test all"""
        self.assertTrue(TestLexer.checkLexeme("if (a ==\"string\")","if,(,a,==,string,),<EOF>",142))
    def test_all1(self):
        """test all"""
        self.assertTrue(TestLexer.checkLexeme("""if (b >= .8e-2)
            {
            b=b % a
            }else{
            b=b-a;
            }   ""","if,(,b,>=,.8e-2,),{,b,=,b,%,a,},else,{,b,=,b,-,a,;,},<EOF>",143))

    def test_type_decl(self):
        """test type_decl"""
        self.assertTrue(TestLexer.checkLexeme("boolean a5;","boolean,a5,;,<EOF>",144))
    def test_type_decl1(self):
        """test type_decl"""
        self.assertTrue(TestLexer.checkLexeme("float _aw;","float,_aw,;,<EOF>",145))
    def test_type_decl2(self):
        """test type_decl"""
        self.assertTrue(TestLexer.checkLexeme("int _c_2;","int,_c_2,;,<EOF>",146))
    def test_type_decl3(self):
        """test type_decl"""
        self.assertTrue(TestLexer.checkLexeme("string value_2;","string,value_2,;,<EOF>",147))
    def test_operator2(self):
        """test operator"""
        self.assertTrue(TestLexer.checkLexeme("(!(c3 || d5)&& b2) == true ","(,!,(,c3,||,d5,),&&,b2,),==,true,<EOF>",148))
    def test_operator3(self):
        """test operator"""
        self.assertTrue(TestLexer.checkLexeme("while(_r<15.001){value = _r/2E2} ","while,(,_r,<,15.001,),{,value,=,_r,/,2E2,},<EOF>",149))
    def test_operator4(self):
        """test operator"""
        self.assertTrue(TestLexer.checkLexeme("!A||B&&C!=false","!,A,||,B,&&,C,!=,false,<EOF>",150))
    def test_block_comment1(self):
        """test linecomment"""
        self.assertTrue(TestLexer.checkLexeme("""/*jfkv,$%$2@\ndfdf\t
            dfgj1245$#&^
            dfgjdfjgj//
            djfg*/""","<EOF>",151))
    def test_string7(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme('"(a+b+c)*3==1.2"','(a+b+c)*3==1.2,<EOF>',152))
    def test_string8(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme('"\\\\ \\" \\b \\t\\r"','\\\\ \\" \\b \\t\\r,<EOF>',153))
    def test_string_unclosed3(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme('"\b"',"Unclosed String: ",154))
    def test_string_unclosed4(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme('"\f"',"Unclosed String: ",155))
    def test_string_unclosed5(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme('"\n"',"Unclosed String: ",156))
    def test_string_unclosed6(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme('"\t"',"Unclosed String: ",157))
    def test_errortoken3(self):
        """test errortoken"""
        self.assertTrue(TestLexer.checkLexeme("\f","Error Token \f",158))
    def test_string_ellegal3(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme('"test \\m illegal"',"Illegal Escape In String: test \\m",159))
    def test_string_ellegal4(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme('"\\string_illegal"',"Illegal Escape In String: \\s",160))
    def test_errortoken4(self):
        """test errortoken"""
        self.assertTrue(TestLexer.checkLexeme("a=2 $ 2","a,=,2,Error Token $",161))
    def test_errortoken5(self):
        """test errortoken"""
        self.assertTrue(TestLexer.checkLexeme("ak_47 := m416+scarl","ak_47,Error Token :",162))
    def test_errortoken6(self):
        """test errortoken"""
        self.assertTrue(TestLexer.checkLexeme("(a>b) ? a=b:a=-b;","(,a,>,b,),Error Token ?",163))
    def test_operator5(self):
        """test operator"""
        self.assertTrue(TestLexer.checkLexeme("-2 + 3*7/1.2e0","-,2,+,3,*,7,/,1.2e0,<EOF>",164))
    def test_operator6(self):
        """test operator"""
        self.assertTrue(TestLexer.checkLexeme("-.125 -3.2% 7 * 8e2","-,.125,-,3.2,%,7,*,8e2,<EOF>",165))
    def test_operator7(self):
        """test operator"""
        self.assertTrue(TestLexer.checkLexeme("x=x++;","x,=,x,+,+,;,<EOF>",166))
    def test_operator8(self):
        """test operator"""
        self.assertTrue(TestLexer.checkLexeme("if (false || true ==true && false)","if,(,false,||,true,==,true,&&,false,),<EOF>",167))
    def test_string_unclosed7(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme('"my name is:\tHieu"',"Unclosed String: my name is:",168))
    def test_string_unclosed8(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme('"my name is:\bHieu"',"Unclosed String: my name is:",169))
    def test_string_ellegal5(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme('"how does it cost ?\\w 2000d"',"Illegal Escape In String: how does it cost ?\\w",170))
    def test_string_ellegal6(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme('"what time is it ?\\m"',"Illegal Escape In String: what time is it ?\\m",171))
    def test_line_comment2(self):
        """test linecomment"""
        self.assertTrue(TestLexer.checkLexeme("//","<EOF>",172))
    def test_line_comment4(self):
        """test linecomment"""
        self.assertTrue(TestLexer.checkLexeme("///**/","<EOF>",173))
    def test_block_comment2(self):
        """test linecomment"""
        self.assertTrue(TestLexer.checkLexeme("/**/","<EOF>",174))
    def test_block_comment3(self):
        """test linecomment"""
        self.assertTrue(TestLexer.checkLexeme("/*//*/","<EOF>",175))
    def test_all3(self):
        """test all"""
        self.assertTrue(TestLexer.checkLexeme("return -1 ;","return,-,1,;,<EOF>",176))
    def test_all4(self):
        """test all"""
        self.assertTrue(TestLexer.checkLexeme("int arr[5] = {1,2,3,4,5};","int,arr,[,5,],=,{,1,,,2,,,3,,,4,,,5,},;,<EOF>",177))
    def test_all5(self):
        """test all"""
        self.assertTrue(TestLexer.checkLexeme("arr[0]=arr[1]=0.3;","arr,[,0,],=,arr,[,1,],=,0.3,;,<EOF>",178))
    def test_all6(self):
        """test all"""
        self.assertTrue(TestLexer.checkLexeme("int *ptr;","int,*,ptr,;,<EOF>",179))
    def test_all7(self):
        """test all"""
        self.assertTrue(TestLexer.checkLexeme("int *ptr;","int,*,ptr,;,<EOF>",180))
    def test_all8(self):
        """test all"""
        self.assertTrue(TestLexer.checkLexeme("if(c_b !=2 || c_b < -2.12e3)","if,(,c_b,!=,2,||,c_b,<,-,2.12e3,),<EOF>",181))
    def test_all9(self):
        """test all"""
        self.assertTrue(TestLexer.checkLexeme("while(a==3-2)","while,(,a,==,3,-,2,),<EOF>",182))
    def test_all10(self):
        """test all"""
        self.assertTrue(TestLexer.checkLexeme('"string1" == "string2"',"string1,==,string2,<EOF>",183))
    def test_all11(self):
        """test all"""
        self.assertTrue(TestLexer.checkLexeme("""//this is operator
            z=5/7.0;""","z,=,5,/,7.0,;,<EOF>",184))
    def test_all12(self):
        """test all"""
        self.assertTrue(TestLexer.checkLexeme("""/*comment
            about if*/
            if(q[2]>q[3]);""","if,(,q,[,2,],>,q,[,3,],),;,<EOF>",185))
    def test_all13(self):
        """test all"""
        self.assertTrue(TestLexer.checkLexeme("for(int i = 0; i< 15; i++)","for,(,int,i,=,0,;,i,<,15,;,i,+,+,),<EOF>",186))
    def test_all14(self):
        """test all"""
        self.assertTrue(TestLexer.checkLexeme("i += a * 24;","i,+,=,a,*,24,;,<EOF>",187))
    def test_all15(self):
        """test all"""
        self.assertTrue(TestLexer.checkLexeme('printf("Hello World!");',"printf,(,Hello World!,),;,<EOF>",188))
    def test_all16(self):
        """test all"""
        self.assertTrue(TestLexer.checkLexeme("""
            while(true)
            {
            printf(\"---\")
            }""","while,(,true,),{,printf,(,---,),},<EOF>",189))
    def test_all17(self):
        """test all"""
        self.assertTrue(TestLexer.checkLexeme("""
            do
            {
            a=a+2.3;
            }while(a<=-3.14);
            ""","do,{,a,=,a,+,2.3,;,},while,(,a,<=,-,3.14,),;,<EOF>",190))
    def test_all18(self):
        """test all"""
        self.assertTrue(TestLexer.checkLexeme("i = a = b * 34 + c5;","i,=,a,=,b,*,34,+,c5,;,<EOF>",191))
    def test_all19(self):
        """test all"""
        self.assertTrue(TestLexer.checkLexeme("""
            string str;
            str = \"num#1\\tnum#2\\t\";
            ""","string,str,;,str,=,num#1\\tnum#2\\t,;,<EOF>",192))
    def test_all20(self):
        """test all"""
        self.assertTrue(TestLexer.checkLexeme("""
            S = C * R;
            printf(\"S= %d\",S);
            ""","S,=,C,*,R,;,printf,(,S= %d,,,S,),;,<EOF>",193))
    def test_all21(self):
        """test all"""
        self.assertTrue(TestLexer.checkLexeme("""
            const int  C = 15;
            const int  R = 12;
            ""","const,int,C,=,15,;,const,int,R,=,12,;,<EOF>",194))
    def test_all22(self):
        """test all"""
        self.assertTrue(TestLexer.checkLexeme("""
            // function_decl
            int func_name();
            
            int main()
            {
            // call function
            int i = func_name();
            }
            
            // function declaration
            int func_name()
            {
            return 0;
            }
            ""","int,func_name,(,),;,int,main,(,),{,int,i,=,func_name,(,),;,},int,func_name,(,),{,return,0,;,},<EOF>",195))
    def test_all23(self):
        """test all"""
        self.assertTrue(TestLexer.checkLexeme("""
            void xuatMang(int a[MAX][MAX], int n, int m)
            {
            int i, j;
            for (i = 0; i < n; i++) {
            for (j = 0; j < m; j++) {
            printf (\"%d\", a[i][j]);
            }
            printf(\"\\n\"); // xuong dong khi het 1 dong
            }
            }
            ""","void,xuatMang,(,int,a,[,MAX,],[,MAX,],,,int,n,,,int,m,),{,int,i,,,j,;,for,(,i,=,0,;,i,<,n,;,i,+,+,),{,for,(,j,=,0,;,j,<,m,;,j,+,+,),{,printf,(,%d,,,a,[,i,],[,j,],),;,},printf,(,\\n,),;,},},<EOF>",196))
    def test_all24(self):
        """test all"""
        self.assertTrue(TestLexer.checkLexeme("""
            struct student {
            string id;
            int roll;
            string name;
            float marks;
            };
            ""","struct,student,{,string,id,;,int,roll,;,string,name,;,float,marks,;,},;,<EOF>",197))
    def test_errortoken7(self):
        """test errortoken"""
        self.assertTrue(TestLexer.checkLexeme("#include<iostream>","Error Token #",198))
    def test_string_unclosed9(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme("""\"test new line
            new line\"""","Unclosed String: test new line",199))

    def test_string9(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme('"string #1 \\b"',"string #1 \\b,<EOF>",200))
    def test_lower_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc","abc,<EOF>",301))
    def test_lower_upper_id(self):
        self.assertTrue(TestLexer.checkLexeme("aCBbdc","aCBbdc,<EOF>",302))
    def test_wrong_token(self):
        self.assertTrue(TestLexer.checkLexeme("aA?sVN","aA,Error Token ?",303))
    def test_integer(self):
        """test integers"""
        self.assertTrue(TestLexer.checkLexeme("123a123","123,a123,<EOF>",304))
    def test_string15(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme(""" "123a\\n123" ""","""123a\\n123,<EOF>""",305))
    def test_unclose_string(self):
        """test integers"""
        self.assertTrue(TestLexer.checkLexeme(""" "123a\\n123 ""","""Unclosed String: 123a\\n123 """,306))
    def test_illegal_escape(self):
        self.assertTrue(TestLexer.checkLexeme(""" 123 "123a\\m123" ""","""123,Illegal Escape In String: 123a\\m""",307))
    def test_double_slash(self):
        self.assertTrue(TestLexer.checkLexeme(""" 123 "123a\\\\123" ""","""123,123a\\\\123,<EOF>""",308))
