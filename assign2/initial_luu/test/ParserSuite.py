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
    def test_simple_program1(self):
        """Simple program: int main() {} """
        input = """void main() {
            
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,204))
    def test_simple_program2(self):
        """Simple program: int main() {} """
        input = """
            float a;
            void main() {
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,205))
    def test_simple_program3(self):
        """Simple program: int main() {} """
        input = """
            float a;
            string b;
            void main() {
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,206))
    def test_simple_program4(self):
        """Simple program: int main() {} """
        input = """
            float a;
            string b;
            boolean c;
            void main() {
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,207))
    def test_simple_program5(self):
        """Simple program: int main() {} """
        input = """
            
            float a,d,e;
            string b;
            boolean c;
            
            void main() {
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,208))
    def test_simple_progra6(self):
        """Simple program: int main() {} """
        input = """
            
            float a,d,e,i[10];
            string b;
            boolean c;
            
            void main() {
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,209))
    def test_simple_progra6(self):
        """Simple program: int main() {} """
        input = """
            float hk(){
            float a,d,e,i[10];
            string b;
            boolean c;
            }
            void main() {
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,209))
    def test_simple_progra7(self):
        """Simple program: int main() {} """
        input = """
            float hk(){
            float a,d,e,i[10];
            string b;
            boolean c;
            }
            void main() {
            float a,d,e,i[10];
            string b;
            boolean c;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,210))
    def test_simple_progra8(self):
        """Simple program: int main() {} """
        input = """
            float hk(){
            float a,d,e,i[10];
            string b;
            boolean c;
            return a;
            }
            void main() {
            
            float a,d,e,i[10];
            string b;
            boolean c;
            
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,211))
    def test_simple_program9(self):
        """Simple program: int main() {} """
        input = """int akdjak;
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,212))
    def test_simple_program10(self):
        """Simple program: int main() {} """
        input = """int main(){
            int a,b,c, d[10];
            return 1;
            }
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,213))
    def test_simple_program11(self):
        """Simple program: int main() {} """
        input = """int main(){
            int a,b,c, d[10];
            a = 10;
            return 1;
            }
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,214))
    def test_simple_program12(self):
        """Simple program: int main() {} """
        input = """int main(){
            int a,b,c, d[10];
            a = a-10;
            return 1;
            }
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,215))
    def test_simple_program13(self):
        """Simple program: int main() {} """
        input = """int main(){
            int a,b,c, d[10];
            a = a-10+9*8;
            return 1;
            }
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,216))
    def test_simple_program14(self):
        """Simple program: int main() {} """
        input = """int main(){
            int a,b,c, d[10],e[9];
            a = a-10+9*8;
            d[0] = d[10] - e[9] - foo();
            return 1;
            }
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,217))
    def test_simple_program15(self):
        """Simple program: int main() {} """
        input = """int main(){
            int a,b,c, d[10];
            a = a-10+9*8;
            if(a <= 1)
              a = 1;
            return 1;
            }
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,218))
    def test_simple_program16(self):
        """Simple program: int main() {} """
        input = """int main(){
            int a,b,c, d[10];
            a = a-10+9*8;
            if(a <= 1){
            a = 1;
            }
            return 1;
            }
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,219))
    def test_simple_program17(self):
        """Simple program: int main() {} """
        input = """int main(){
            int a,b,c, d[10];
            a = a-10+9*8;
            if(a <= 1){
            a = 1;
                {
                b =10;
                for(i=1;i> 10; i=1+2)
                a = c;
                }
            }
            return 1;
            }
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,220))
    def test_simple_program18(self):
        """Simple program: int main() {} """
        input = """int main(){
            int a,b,c, d[10];
            a = a-10+9*8;
            if(a <= 1){
            a = 1;
            {
            b =10;
            for(i=1;i> 10; i=1+2)
            a = c;
            continue;
            }
            }
            return 1;
            }
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,221))
    def test_simple_program19(self):
        """Simple program: int main() {} """
        input = """int main(){
            int a,b,c, d[10];
            a = a-10+9*8;
            if(a <= 1){
            a = 1;
                {
            b =10;
            for(i=1;i> 10; i=1+2)
            a = c;
                }
                break;
            }
            return 1;
            }
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,222))
    def test_simple_program20(self):
        """Simple program: int main() {} """
        input = """int main(){
            int a,b,c, d[10];
            a = a-10+9*8;
            for(i = 0; i < 10; i=i+1)
            a =1;
            return 1;
            }
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,223))
    def test_simple_program21(self):
        """Simple program: int main() {} """
        input = """int main(){
            int a,b,c, d[10];
            a = a-10+9*8;
            for(i = 0; i < 10; i=i+1)
            
            return 1;
            }
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,224))
    def test_simple_program22(self):
        """Simple program: int main() {} """
        input = """int main(){
            int a,b,c, d[10];
            a = a-10+9*8;
            do{
            
            }while(a<3);
            a = 1;
            return 1;
            }
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,225))
    def test_simple_program23(self):
        """Simple program: int main() {} """
        input = """
            boolean k[10];
            int main(){
            int a,b,c, d[10];
            a = a-10+9*8;
            do{
            
            }while(a<3);
            a =1;
            return 1;
            }
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,226))
    def test_simple_program24(self):
        """Simple program: int main() {} """
        input = """
            boolean khoa(int a, int b){
            
            return a && b;
            }
            int main(){
            int a,b,c, d[10];
            a = a-10+9*8;
            do{
            
            }while(a<3);
            a =1;
            return 1;
            }
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,227))
    def test_simple_program25(self):
        """Simple program: int main() {} """
        input = """
            boolean khoa(int a, int b){
            int c ;
            return A && B;
            }
            int main(){
            int a,b,c, d[10];
            a = a-10+9*8;
            do{
            
            }while(a<3);
            a =1;
            return 1;
            }
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,228))
    def test_simple_program26(self):
        """Simple program: int main() {} """
        input = """int main() {
            int a,b,c;
            a = a*c;
            
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,229))
    def test_simple_program27(self):
        """Simple program: int main() {} """
        input = """int main() {
            int a,b,c;
            a = a*c;
            -b;
            
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,230))
    def test_simple_program28(self):
        """Simple program: int main() {} """
        input = """int main() {
            int a,b,c;
            a = a*c;
            !b;
            
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,231))
    def test_simple_program29(self):
        """Simple program: int main() {} """
        input = """int main() {
            int a,b,c;
            a = a*c;
            a == b;
            
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,232))
    def test_simple_program30(self):
        """Simple program: int main() {} """
        input = """int main() {
            int a,b,c;
            a = a*c;
            a != b;
            
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,233))
    def test_simple_program31(self):
        """Simple program: int main() {} """
        input = """int main() {
            int a,b,c;
            a = a*c;
            b = a || b && c - d;
            
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,234))
    def test_simple_program32(self):
        """Simple program: int main() {} """
        input = """int main() {
            int a,b,c,d[10];
            a = a*c;
            a = d[b+c];
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,235))
    def test_simple_program33(self):
        """Simple program: int main() {} """
        input = """int main() {
            int a,b,c,d[10];
            a = a*c;
            a = b = c;
            
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,236))
    def test_simple_program34(self):
        """Simple program: int main() {} """
        input = """int main() {
            int a,b,c,d[10];
            a = a*c;
            foo(2)[3+x] = a[b[2]] + 3 ;
            
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,237))
    def test_simple_program35(self):
        """Simple program: int main() {} """
        input = """int main() {
            int a,b,c,d[10];
            a = a*c;
            foo(2)[3+x] = a[b[2]] + 3 ;
            a = a+b;
            
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,238))
    def test_simple_program36(self):
        """Simple program: int main() {} """
        input = """int main() {
            int a,b,c,d[10];
            a = a*c;
            foo(2)[3+x] = a[b[2+(2*9)]] + 3 ;
            a = ((a+b)&&c)||d;
            
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,239))
    def test_simple_program37(self):
        """Simple program: int main() {} """
        input = """int main() {
            int a,b,c,d[10];
            a = a*c;
            foo(2)[3+x] = a[b[2+(2*9)]] + 3 ;
            a = ((a+b)&&c)||d;
            i = 1;
            foo(1,2) = 9;
            if (a == b ) d[0] = 1.0;
            
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,240))
    def test_simple_program38(self):
        """Simple program: int main() {} """
        input = """int main() {
            for(i = 1; i <10; i = i +2)
                if(i==1)
                i = 0;
            
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,241))
    def test_simple_program39(self):
        """Simple program: int main() {} """
        input = """int main() {
            for(i = 1; i <10; i = i +2)
            foo(2);
            return 0;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,242))
    def test_simple_program42(self):
        """Simple program: int main() {} """
        input = """int main() {
            
            if(i==1)
            b = 2;
           
            
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,243))
    def test_simple_program40(self):
        """Simple program: int main() {} """
        input = """int main() {
            do{
            }while a < 3;
            
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,244))
    def test_simple_program41(self):
        """Simple program: int main() {} """
        input = """int main() {
            do{
            {
            }
            
            }while( a < 3);
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,245))
    def test_simple_program43(self):
        """Simple program: int main() {} """
        input = """
            int[] foo(){
            
            }
            int main() {
            
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,246))

    def test_simple_program44(self):
        """Simple program: int main() {} """
        input = """
            int[] foo(){
            return k;
            }
            int main() {
            
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,247))
    def test_simple_program45(self):
        """Simple program: int main() {} """
        input = """
            int[] foo(){
            return k;
            }
            int main() {
            getInt();
            
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,248))
    def test_simple_program46(self):
        """Simple program: int main() {} """
        input = """
            int[] foo(){
            return k;
            }
            int main() {
            getFloat();
            
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,249))
    def test_simple_program47(self):
        """Simple program: int main() {} """
        input = """
            int[] foo(){
            return k;
            }
            int main() {
            int a;
            a=getFloat();
            
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,250))
    def test_simple_program48(self):
        """Simple program: int main() {} """
        input = """
            int[] foo(){
            return k;
            }
            int main() {
            int a;
            a=getFloat();
            putString(foo(3)[1]);
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,251))
    def test_simple_program49(self):
        """Simple program: int main() {} """
        input = """
            int[] foo(){
            return k;
            }
            int main() {
            if(true)
             a =10;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,252))
    def test_simple_program50(self):
        """Simple program: int main() {} """
        input = """int main() {
            int a,b,c;
            a = a*c;
            b = khak()[a || b && c - d];
            
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,253))
    def test_simple_program51(self):
        """Simple program: int main() {} """
        input = """int main() {
            int a,b,c;
            a = a*c;
            b = khasd((khak()[a || b && c - d] % 20) - 10) && a;
            
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,254))
    def test_simple_program52(self):
        """Simple program: int main() {} """
        input = """int main() {
            int a,b,c,d[10];
            a = a*c;
            a = d[b+c];
            
            return foo(10)[0];
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,255))
    def test_simple_program53(self):
        """Simple program: int main() {} """
        input = """int main() {
            int a,b,c,d[10];
            a = a*c;
            a = d[b+c];
            do{
            }
            {
            
            } while (a || 3 )!= 0;
            
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,256))
    def test_simple_program54(self):
        """Simple program: int main() {} """
        input = """int main() {
            int a,b,c,d[10];
            a = a*c;
            a = d[b+c];
            do
            a = a +d[0];
            while (a || 3 )!= 0;
            
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,257))
    def test_simple_program55(self):
        """Simple program: int main() {} """
        input = """int main() {
            int a,b,c,d[10];
            a = a*c;
            a = d[b+c];
            do
            a = a +d[0];
            b = b*c;
            while (a || 3 )!= 0;
            
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,258))
    def test_simple_program56(self):
        """Simple program: int main() {} """
        input = """int main() {
            int a,b,c;
            a = a*c;
            b = khasd((khak()[a || b && c - d] % 20) - 10) && a;
            -c;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,259))
    def test_simple_program57(self):
        """Simple program: int main() {} """
        input = """int main() {
            int a,b[2],c[20];
            string a1[10], c2[20];
            a = a*c;
            b = khasd((khak()[a || b && c - d] % 20) - 10) && a;
            -c = c[1];
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,260))
    def test_simple_program58(self):
        """Simple program: int main() {} """
        input = """int main() {
            int a,b[2],c[20];
            string a1[10], c2[20];
            a = a*c;
            b = khasd((khak()[a || b && c - d] % 20) - 10) && a;
            -c = c / a;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,261))
    def test_simple_program59(self):
        """Simple program: int main() {} """
        input = """int main() {
            int a,b[2],c[20];
            string a1[10], c2[20];
            a = a*c;
            b = khasd((khak()[a || b && c - d] % 20) - 10) && a;
            -c = c * a;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,262))
    def test_simple_program60(self):
        """Simple program: int main() {} """
        input = """int main() {
            int a,b[2],c[20];
            string a1[10], c2[20];
            a = a*c;
            b = khasd((khak()[a || b && c - d] % 20) - 10) && a;
            -c = c * a;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,263))
    def test_simple_program61(self):
        """Simple program: int main() {} """
        input = """int main() {
            int a,b[2],c[20];
            string a1[10], c2[20];
            a = a*c;
            b = khasd((khak()[a || b && c - d] % 20) - 10) && a;
            -c = c % a;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,264))
    def test_simple_program62(self):
        """Simple program: int main() {} """
        input = """int main() {
            int a,b[2],c[20];
            string a1[10], c2[20];
            a = a*c;
            b = khasd((khak()[a || b && c - d] % 20) - 10) && a;
            -c = c < a;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,265))
    def test_simple_program63(self):
        """Simple program: int main() {} """
        input = """int main() {
            int a,b[2],c[20];
            string a1[10], c2[20];
            a = a*c;
            b = khasd((khak()[a || b && c - d] % 20) - 10) && a;
            -c = c <= a;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,266))
    def test_simple_program64(self):
        """Simple program: int main() {} """
        input = """int main() {
            int a,b[2],c[20];
            string a1[10], c2[20];
            a = a*c;
            b = khasd((khak()[a || b && c - d] % 20) - 10) && a;
            -c = c >= a;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,267))
    def test_simple_program65(self):
        """Simple program: int main() {} """
        input = """int main() {
            int a,b[2],c[20];
            string a1[10], c2[20];
            a = a*c;
            b = khasd((khak()[a || b && c - d] % 20) - 10) && a;
            -c = (-a/c[0]*c[1])%c[2]+c[3]-c[4] && (c5 || c6);
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,268))
    def test_simple_program66(self):
        """Simple program: int main() {} """
        input = """int main() {
            int a,b[2],c[20];
            string a1[10], c2[20];
            a = a*c;
            b = khasd((khak()[a || b && c - d] % 20) - 10) && a;
            //-c = (-a/c[0]*c[1])%c[2]+c[3]-c[4] && (c5 || c6);
            // khong phbai dang vua dau
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,269))
    def test_simple_program67(self):
        """Simple program: int main() {} """
        input = """int main() {
            int a,b[2],c[20];
            string a1[10], c2[20];
            a = a*c;
            b = khasd((khak()[a || b && c - d] % 20) - 10) && a;
            //-c = (-a/c[0]*c[1])%c[2]+c[3]-c[4] && (c5 || c6);
            // khong phbai dang vua dau
            /* kjdadkasjdadk
            
            dalsdkasldad*/
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,270))
    def test_simple_program68(self):
        """Simple program: int main() {} """
        input = """int main() {
            int a,b[2],c[20];
            string a1[10], c2[20];
            a = a*c;
            b = khasd((khak()[a || b && c - d] % 20) - 10) && a;
            //-c = (-a/c[0]*c[1])%c[2]+c[3]-c[4] && (c5 || c6);
            // khong phbai dang vua dau
            /* kjdadkasjdadk
            a = "abcd";
            dalsdkasldad*/
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,271))
    def test_simple_program69(self):
        """Simple program: int main() {} """
        input = """int main() {
            int a,b[2],c[20];
            string a1[10], c2[20];
            a = a*c;
            b = khasd((khak()[a || b && c - d] % 20) - 10) && a;
            //-c = (-a/c[0]*c[1])%c[2]+c[3]-c[4] && (c5 || c6);
            // khong phbai dang vua dau
            /* kjdadkasjdadk
           
            dalsdkasldad*/
             a = 132.e8;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,272))
    def test_simple_program70(self):
        """Simple program: int main() {} """
        input = """int main() {
            int a,b[2],c[20];
            string a1[10], c2[20];
            a = a*c;
            b = khasd((khak()[a || b && c - d] % 20) - 10) && a;
            //-c = (-a/c[0]*c[1])%c[2]+c[3]-c[4] && (c5 || c6);
            // khong phbai dang vua dau
            /* kjdadkasjdadk
            
            dalsdkasldad*/
            c[20] = c[19]+132.e8;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,273))
    def test_simple_program71(self):
        """Simple program: int main() {} """
        input = """int main() {
            int a,b[2],c[20];
            string a1[10], c2[20];
            a = a*c;
            b = khasd((khak()[a || b && c - d] % 20) - 10) && a;
            //-c = (-a/c[0]*c[1])%c[2]+c[3]-c[4] && (c5 || c6);
            // khong phbai dang vua dau
            
            c[20] = c[19]+132.e8;
            if(true)
            a = "abc";
            else
            c = 11;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,274))
    def test_simple_program72(self):
        """Simple program: int main() {} """
        input = """int main() {
            int a,b[2],c[20];
            string a1[10], c2[20];
            a = a*c;
            b = khasd((khak()[a || b && c - d] % 20) - 10) && a;
            //-c = (-a/c[0]*c[1])%c[2]+c[3]-c[4] && (c5 || c6);
            // khong phbai dang vua dau
            
            c[20] = c[19]+132.e8;
            if(a == false)
            a = "abc";
            else
            c = false;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,275))
    def test_simple_program73(self):
        """Simple program: int main() {} """
        input = """int main() {
            int a,b[2],c[20];
            string a1[10], c2[20];
            a = a*c;
            b = khasd((khak()[a || b && c - d] % 20) - 10) && a;
            //-c = (-a/c[0]*c[1])%c[2]+c[3]-c[4] && (c5 || c6);
            // khong phbai dang vua dau
            
            c[20] = c[19]+132.e8;
            if(a == false)
            a = "abc";
            else
            c = false;
            c = true + c;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,276))
    def test_simple_program74(self):
        """Simple program: int main() {} """
        input = """int main() {
            int a,b[2],c[20];
            string a1[10], c2[20];
            a = a*c;
            b = khasd((khak()[a || b && c - d] % 20) - 10) && a;
            //-c = (-a/c[0]*c[1])%c[2]+c[3]-c[4] && (c5 || c6);
            // khong phbai dang vua dau
            
            c[20] = c[19]+132.e8;
            if(a == false)
            a = "abc";
            else
            c = false;
            c = true + c;
            a = "xyz\\n";
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,277))

    def test_simple_program75(self):
        """Simple program: int main() {} """
        input = """int main() {
            int a,b[2],c[20];
            string a1[10], c2[20];
            a = a*c;
            b = khasd((khak()[a || b && c - d] % 20) - 10) && a;
            //-c = (-a/c[0]*c[1])%c[2]+c[3]-c[4] && (c5 || c6);
            // khong phbai dang vua dau
            
            c[20] = c[19]+132.e8;
            if(a == false)
            a = "abc";
            else
            c = false;
            c = true + c;
            a = "xyz\\t";
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,278))
    def test_simple_program76(self):
        """Simple program: int main() {} """
        input = """int main() {
            int a,b[2],c[20];
            string a1[10], c2[20];
            a = a*c;
            b = khasd((khak()[a || b && c - d] % 20) - 10) && a;
            //-c = (-a/c[0]*c[1])%c[2]+c[3]-c[4] && (c5 || c6);
            // khong phbai dang vua dau
            
            c[20] = c[19]+132.e8;
            if(a == false)
            a = "abc";
            else
            c = false;
            c = true + c;
            a = "xyz\\t";
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,279))
    def test_simple_program77(self):
        """Simple program: int main() {} """
        input = """int main() {
            int a,b[2],c[20];
            string a1[10], c2[20];
            a = a*c;
            b = khasd((khak()[a || b && c - d] % 20) - 10) && a;
            //-c = (-a/c[0]*c[1])%c[2]+c[3]-c[4] && (c5 || c6);
            // khong phbai dang vua dau
            
            c[20] = c[19]+132.e8;
            if(a == false)
            a = "abc";
            else
            c = false;
            c = true + c;
            a = "xyz\\"";
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,280))
    def test_simple_program78(self):
        """Simple program: int main() {} """
        input = """int main() {
            int a,b[2],c[20];
            string a1[10], c2[20];
            a = a*c;
            b = khasd((khak()[a || b && c - d] % 20) - 10) && a;
            //-c = (-a/c[0]*c[1])%c[2]+c[3]-c[4] && (c5 || c6);
            // khong phbai dang vua dau
            
            c[20] = c[19]+132.e8;
            if(a == false)
            a = "abc";
            else
            c = false;
            c = true + c;
            a = "xyz\\r";
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,281))
    def test_simple_program79(self):
        """Simple program: int main() {} """
        input = """int main() {
            int a,b[2],c[20];
            string a1[10], c2[20];
            a = a*c;
            b = khasd((khak()[a || b && c - d] % 20) - 10) && a;
            //-c = (-a/c[0]*c[1])%c[2]+c[3]-c[4] && (c5 || c6);
            // khong phbai dang vua dau
            
            c[20] = c[19]+132.e8;
            if(a == false)
            a = "abc";
            else
            c = false;
            c = true + c;
            a = "xyz\\r  \\t \\b";
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,282))
    def test_simple_program80(self):
        """Simple program: int main() {} """
        input = """int main() {
            int a,b[2],c[20];
            string a1[10], c2[20];
            a = a*c;
            b = khasd((khak()[a || b && c - d] % 20) - 10) && a;
            //-c = (-a/c[0]*c[1])%c[2]+c[3]-c[4] && (c5 || c6);
            // khong phbai dang vua dau
            
            c[20] = c[19]+132.e8;
            if(a == false)
            a = "abc";
            else
            c = false;
            c = true + c;
            a = "xyz\\r  \\t \\b";
            c = 1.3;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,283))
    def test_simple_program81(self):
        """Simple program: int main() {} """
        input = """int main() {
            int a,b[2],c[20];
            string a1[10], c2[20];
            a = a*c;
            b = khasd((khak()[a || b && c - d] % 20) - 10) && a;
            //-c = (-a/c[0]*c[1])%c[2]+c[3]-c[4] && (c5 || c6);
            // khong phbai dang vua dau
            
            c[20] = c[19]+132.e8;
            if(a == false)
            a = "abc";
            else
            c = false;
            c = true + c;
            a = "xyz\\r  \\t \\b";
            c = 1.3+1.3;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,284))
    def test_simple_program82(self):
        """Simple program: int main() {} """
        input = """int main() {
            int a,b[2],c[20];
            string a1[10], c2[20];
            a = a*c;
            b = khasd((khak()[a || b && c - d] % 20) - 10) && a;
            //-c = (-a/c[0]*c[1])%c[2]+c[3]-c[4] && (c5 || c6);
            // khong phbai dang vua dau
            
            c[20] = c[19]+132.e8;
            if(a == false)
            a = "abc";
            else
            c = false || true;
            c = true + c;
            a = "xyz\\r  \\t \\b";
            c = 1.3+1.3;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,285))
    def test_simple_program83(self):
        """Simple program: int main() {} """
        input = """int main() {
            int a,b[2],c[20];
            string a1[10], c2[20];
            a = a*c;
            b = khasd((khak()[a || b && c - d] % 20) - 10) && a;
            //-c = (-a/c[0]*c[1])%c[2]+c[3]-c[4] && (c5 || c6);
            // khong phbai dang vua dau
            c[20] = c[19]+132.e8;
            if(a == false)
            a = "abc";
            else
            c = false || true;
            c = true + c;
            a = "xyz\\r  \\t \\b" + "jakdakdjas";
            c = 1.3+1.3;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,286))
    def test_simple_program84(self):
        """Simple program: int main() {} """
        input = """int main() {
            int a,b[2],c[20];
            string a1[10], c2[20];
            a = a*c;
            b = khasd((khak()[a || b && c - d] % 20) - 10) && a;
            //-c = (-a/c[0]*c[1])%c[2]+c[3]-c[4] && (c5 || c6);
            // khong phbai dang vua dau
            c[20] = c[19]+132.e8;
            if(a == false)
            a = "abc";
            else
            c = false || true;
            c = true + c;
            a = "xyz\\r  \\t \\b" + "jakdakdjas";
            c = 1.3+1.3;
            do{
            c = 1.3+90;
            }while b >0;
            return 1;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,287))
    def test_simple_program85(self):
        """Simple program: int main() {} """
        input = """int main() {
            int a,b[2],c[20];
            string a1[10], c2[20];
            a = a*c;
            b = khasd((khak()[a || b && c - d] % 20) - 10) && a;
            //-c = (-a/c[0]*c[1])%c[2]+c[3]-c[4] && (c5 || c6);
            // khong phbai dang vua dau
            c[20] = c[19]+132.e8;
            if(a == false)
            a = "abc";
            else
            c = false || true;
            c = true + c;
            a = "xyz\\r  \\t \\b" + "jakdakdjas";
            c = 1.3+1.3;
            do{
            c = 1.3+90;
            d && d || d - -d;
            }while b >0;
            return 1;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,288))
    def test_simple_program86(self):
        """Simple program: int main() {} """
        input = """int main() {
            int a,b[2],c[20];
            string a1[10], c2[20];
            a = a*c;
            b = khasd((khak()[a || b && c - d] % 20) - 10) && a;
            //-c = (-a/c[0]*c[1])%c[2]+c[3]-c[4] && (c5 || c6);
            // khong phbai dang vua dau
            c[20] = c[19]+132.e8;
            if(a == false)
            a = "abc";
            else
            c = false || true;
            c = true + c;
            a = "xyz\\r  \\t \\b" + "jakdakdjas";
            c = 1.3+1.3;
            do{
            c = d + -3;
            d && d || d - -d;
            }while b >0;
            return 1;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,289))
    def test_simple_program87(self):
        """Simple program: int main() {} """
        input = """int main() {
            int a,b[2],c[20];
            string a1[10], c2[20];
            a = a*c;
            b = khasd((khak()[a || b && c - d] % 20) - 10) && a;
            //-c = (-a/c[0]*c[1])%c[2]+c[3]-c[4] && (c5 || c6);
            // khong phbai dang vua dau
            c[20] = c[19]+132.e8;
            if(a == false)
            a = "abc";
            else
            c = false || true;
            c = true + c;
            a = "xyz\\r  \\t \\b" + "jakdakdjas";
            c = 1.3+1.3;
            do{
            c = (d * -3) / (-2);
            d && d || d - -d;
            }while b >0;
            return 1;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,290))
    def test_simple_program88(self):
        """Simple program: int main() {} """
        input = """int main() {
            int a,b[2],c[20];
            string a1[10], c2[20];
            a = a*c;
            b = khasd((khak()[a || b && c - d] % 20) - 10) && a;
            //-c = (-a/c[0]*c[1])%c[2]+c[3]-c[4] && (c5 || c6);
            // khong phbai dang vua dau
            c[20] = c[19]+132.e8;
            if(a == false)
            a = "abc";
            else
            c = false || true;
            c = true + c;
            a = "xyz\\r  \\t \\b" + "jakdakdjas";
            c = 1.3+1.3;
            do{
            c = (d * -3) / (-2);
            d && d || d - (--d);
            }while b >0;
            return 1;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,291))
    def test_simple_program89(self):
        """Simple program: int main() {} """
        input = """int main() {
            int a,b[2],c[20];
            string a1[10], c2[20];
            a = a*c;
            b = khasd((khak()[a || b && c - d] % 20) - 10) && a;
            //-c = (-a/c[0]*c[1])%c[2]+c[3]-c[4] && (c5 || c6);
            // khong phbai dang vua dau
            c[20] = c[19]+132.e8;
            if(a == false)
            a = "abc";
            else
            c = false || true;
            c = true + c;
            a = "xyz\\r  \\t \\b" + "jakdakdjas";
            c = 1.3+1.3;
            do{
            c = (d * -3) / (-2);
            a = -a -(d && d || d - (--d));
            }while b >0;
            return 1;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,292))
    def test_simple_program90(self):
        """Simple program: int main() {} """
        input = """int main() {
            int a,b[2],c[20];
            string a1[10], c2[20];
            a = a*c;
            b = khasd((khak()[a || b && c - d] % 20) - 10) && a;
            //-c = (-a/c[0]*c[1])%c[2]+c[3]-c[4] && (c5 || c6);
            // khong phbai dang vua dau
            c[20] = c[19]+132.e8;
            if(a == false)
            a = "abc";
            else
            c = false || true;
            c = true + c;
            a = "xyz\\r  \\t \\b" + "jakdakdjas";
            c = 1.3+1.3;
            do{
            c = (d * -3) / (-2);
            a = -a -(d && d || d - (--d));
            }while true;
            return 1;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,293))
    def test_simple_program91(self):
        """Simple program: int main() {} """
        input = """int main() {
            int a,b[2],c[20];
            string a1[10], c2[20];
            a = a*c;
            b = khasd((khak()[a || b && c - d] % 20) - 10) && a;
            //-c = (-a/c[0]*c[1])%c[2]+c[3]-c[4] && (c5 || c6);
            // khong phbai dang vua dau
            c[20] = c[19]+132.e8;
            if(a == false)
            a = "abc";
            else
            c = false || true;
            c = true + c;
            a = "xyz\\r  \\t \\b" + "jakdakdjas";
            c = 1.3+1.3;
            do{
            c = (d * -3) / (-2);
            a = -a -(d && d || d - (--d));
            }while true && false;
            return 1;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,294))
    def test_simple_program92(self):
        """Simple program: int main() {} """
        input = """int main() {
            int a,b[2],c[20];
            string a1[10], c2[20];
            a = a*c;
            b = khasd((khak()[a || b && c - d] % 20) - 10) && a;
            //-c = (-a/c[0]*c[1])%c[2]+c[3]-c[4] && (c5 || c6);
            // khong phbai dang vua dau
            c[20] = c[19]+132.e8;
            if(a == false)
            a = "abc";
            else
            c = false || true;
            c = true + c;
            -c[1] = c >= d;
            a = "xyz\\r  \\t \\b" + "jakdakdjas";
            c = 1.3+1.3;
            do
            b =10;
            while true && false;
            return 1;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,295))
    def test_simple_program93(self):
        """Simple program: int main() {} """
        input = """
            int a,b[2],c[20];
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,296))
    def test_simple_program94(self):
        """Simple program: int main() {} """
        input = """
            boolean a,b[2],c[20];
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,297))
    def test_simple_program95(self):
        """Simple program: int main() {} """
        input = """
            string a,b[2],c[20];
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,298))
    def test_simple_program96(self):
        """Simple program: int main() {} """
        input = """
            float a,b[2],c[20];
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,299))
    def test_simple_program97(self):
        """Simple program: int main() {} """
        input = """
            float a;
            int[] main(int a, float b[]) {
            F(3)[5];
            return;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,300))




