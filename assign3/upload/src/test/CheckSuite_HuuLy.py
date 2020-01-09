import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_undeclared_function(self):
        """Simple program: int main() {} """
        input = """procedure main(); begin foo();end"""
        expect = "Undeclared Procedure: foo"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_diff_numofparam_stmt(self):
        """More complex program"""
        input = """procedure main (); begin
            putIntLn();
        end"""
        expect = "Type Mismatch In Statement: CallStmt(Id(putIntLn),[])"
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_undeclared_function_use_ast(self):
        """Simple program: int main() {} """
        input = Program([FuncDecl(Id("main"),[],[],[
            CallStmt(Id("foo"),[])])])
        expect = "Undeclared Procedure: foo"
        self.assertTrue(TestChecker.test(input,expect,402))

    def test_diff_numofparam_expr_use_ast(self):
        """More complex program"""
        input = Program([
                FuncDecl(Id("main"),[],[],[
                    CallStmt(Id("putIntLn"),[])])])
                        
        expect = "Type Mismatch In Statement: CallStmt(Id(putIntLn),[])"
        self.assertTrue(TestChecker.test(input,expect,403))
    
    def test_no_entry_point(self):
        input = Program([FuncDecl(Id("bac"),[],[],[
            CallStmt(Id("getInt"),[])])])
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,404))

    def test_break_not_in_loop(self):
        input = Program([FuncDecl(Id("main"),[],[],[
            Break()])])
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,405))

    
    def test_undeclared_function(self):
        """Simple program: int main() {} """
        input = """procedure main(); begin foo();end"""
        expect = "Undeclared Procedure: foo"
        self.assertTrue(TestChecker.test(input,expect,407))

    def test_diff_numofparam_stmt(self):
        """More complex program"""
        input = """procedure main (); begin
            putIntLn();
        end"""
        expect = "Type Mismatch In Statement: CallStmt(Id(putIntLn),[])"
        self.assertTrue(TestChecker.test(input,expect,408))

    def test_undeclared_function_use_ast(self):
        """Simple program: int main() {} """
        input = Program([FuncDecl(Id("main"),[],[],[
            CallStmt(Id("foo"),[])])])
        expect = "Undeclared Procedure: foo"
        self.assertTrue(TestChecker.test(input,expect,409))

    def test_diff_numofparam_expr_use_ast(self):
        """More complex program"""
        input = Program([
                FuncDecl(Id("main"),[],[],[
                    CallStmt(Id("putIntLn"),[])])])
                        
        expect = "Type Mismatch In Statement: CallStmt(Id(putIntLn),[])"
        self.assertTrue(TestChecker.test(input,expect,410))
    
    def test_redecl4(self):
        input = """int a; void b(int c){int c;} int main(){return 9;}"""
        expect = "Redeclared Variable: c"
        self.assertTrue(TestChecker.test(input,expect,412))
    def test_redecl5(self):
        input = """int a,c; int b(int c){int c;return 9;} int main(){return 9;}"""
        expect = "Redeclared Variable: c"
        self.assertTrue(TestChecker.test(input,expect,413))
    def test_redecl6(self):
        input = """int a(int a){int b; return 9;} int b(int c){int a;return 9;} int main(){return 9;}"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,414))
    def test_redecl7(self):
        input = """  int main(){return 9;}"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,415))
    def test_redecl8(self):
        input = """  int main(int a,int b){if ( a>b ) putIntLn(9); return 9;}"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,416))

    def test_concac(self):
        input = """  void main(){}  int test(){{{return 0;}}}"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,417))

    def test_concac1(self):
        input = """  void main(){if(1>0){return; {break;}}} """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,418))

    def test_concac2(self):
        input = """  void main(){calc()[0]=4;} int[] calc(){int i[2]; return i;} """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,419))

    def test_concac56(self):
        input = """  void main(){if(1>0){return; {continue;}}} """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,420))

    def test_noentry_prog(self):
        input = """ int a;"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,421))

    def test_undeclared_function_use_ast(self):
        """Simple program: int main() {} """
        input = Program([FuncDecl(Id("main"),[],[],[
            CallStmt(Id("foo"),[])])])
        expect = "Undeclared Procedure: foo"
        self.assertTrue(TestChecker.test(input,expect,424))

    def test_diff_numofparam_expr_use_ast(self):
        """More complex program"""
        input = Program([
                FuncDecl(Id("main"),[],[],[
                    CallStmt(Id("putIntLn"),[])])])
                        
        expect = "Type Mismatch In Statement: CallStmt(Id(putIntLn),[])"
        self.assertTrue(TestChecker.test(input,expect,425))
    
    def test_no_entry_point(self):
        input = Program([FuncDecl(Id("bac"),[],[],[
            CallStmt(Id("getInt"),[])])])
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,426))
    def test_undeclared_function(self):
        """Simple program: int main() {} """
        input = """procedure main(); begin foo();end"""
        expect = "Undeclared Procedure: foo"
        self.assertTrue(TestChecker.test(input,expect,427))

    def test_diff_numofparam_stmt(self):
        """More complex program"""
        input = """procedure main (); begin
            putIntLn();
        end"""
        expect = "Type Mismatch In Statement: CallStmt(Id(putIntLn),[])"
        self.assertTrue(TestChecker.test(input,expect,428))

    def test_undeclared_function_use_ast(self):
        """Simple program: int main() {} """
        input = Program([FuncDecl(Id("main"),[],[],[
            CallStmt(Id("foo"),[])])])
        expect = "Undeclared Procedure: foo"
        self.assertTrue(TestChecker.test(input,expect,429))

    def test_diff_numofparam_expr_use_ast(self):
        """More complex program"""
        input = Program([
                FuncDecl(Id("main"),[],[],[
                    CallStmt(Id("putIntLn"),[])])])
                        
        expect = "Type Mismatch In Statement: CallStmt(Id(putIntLn),[])"
        self.assertTrue(TestChecker.test(input,expect,430))
    
    def test_no_entry_point(self):
        input = Program([FuncDecl(Id("bac"),[],[],[
            CallStmt(Id("getInt"),[])])])
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,431))
    def test_undeclared_function(self):
        """Simple program: int main() {} """
        input = """procedure main(); begin foo();end"""
        expect = "Undeclared Procedure: foo"
        self.assertTrue(TestChecker.test(input,expect,432))

    def test_diff_numofparam_stmt(self):
        """More complex program"""
        input = """procedure main (); begin
            putIntLn();
        end"""
        expect = "Type Mismatch In Statement: CallStmt(Id(putIntLn),[])"
        self.assertTrue(TestChecker.test(input,expect,433))

    def test_undeclared_function_use_ast(self):
        """Simple program: int main() {} """
        input = Program([FuncDecl(Id("main"),[],[],[
            CallStmt(Id("foo"),[])])])
        expect = "Undeclared Procedure: foo"
        self.assertTrue(TestChecker.test(input,expect,434))

    def test_diff_numofparam_expr_use_ast(self):
        """More complex program"""
        input = Program([
                FuncDecl(Id("main"),[],[],[
                    CallStmt(Id("putIntLn"),[])])])
                        
        expect = "Type Mismatch In Statement: CallStmt(Id(putIntLn),[])"
        self.assertTrue(TestChecker.test(input,expect,435))
    
    def test_no_entry_point(self):
        input = Program([FuncDecl(Id("bac"),[],[],[
            CallStmt(Id("getInt"),[])])])
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,436))
    def test_undeclared_function(self):
        """Simple program: int main() {} """
        input = """procedure main(); begin foo();end"""
        expect = "Undeclared Procedure: foo"
        self.assertTrue(TestChecker.test(input,expect,437))

    def test_diff_numofparam_stmt(self):
        """More complex program"""
        input = """procedure main (); begin
            putIntLn();
        end"""
        expect = "Type Mismatch In Statement: CallStmt(Id(putIntLn),[])"
        self.assertTrue(TestChecker.test(input,expect,438))

    def test_undeclared_function_use_ast(self):
        """Simple program: int main() {} """
        input = Program([FuncDecl(Id("main"),[],[],[
            CallStmt(Id("foo"),[])])])
        expect = "Undeclared Procedure: foo"
        self.assertTrue(TestChecker.test(input,expect,439))

    def test_diff_numofparam_expr_use_ast(self):
        """More complex program"""
        input = Program([
                FuncDecl(Id("main"),[],[],[
                    CallStmt(Id("putIntLn"),[])])])
                        
        expect = "Type Mismatch In Statement: CallStmt(Id(putIntLn),[])"
        self.assertTrue(TestChecker.test(input,expect,440))
    
    def test_no_entry_point(self):
        input = Program([FuncDecl(Id("bac"),[],[],[
            CallStmt(Id("getInt"),[])])])
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,441))
    def test_undeclared_function(self):
        """Simple program: int main() {} """
        input = """procedure main(); begin foo();end"""
        expect = "Undeclared Procedure: foo"
        self.assertTrue(TestChecker.test(input,expect,442))

    def test_diff_numofparam_stmt(self):
        """More complex program"""
        input = """procedure main (); begin
            putIntLn();
        end"""
        expect = "Type Mismatch In Statement: CallStmt(Id(putIntLn),[])"
        self.assertTrue(TestChecker.test(input,expect,443))

    def test_undeclared_function_use_ast(self):
        """Simple program: int main() {} """
        input = Program([FuncDecl(Id("main"),[],[],[
            CallStmt(Id("foo"),[])])])
        expect = "Undeclared Procedure: foo"
        self.assertTrue(TestChecker.test(input,expect,444))

    def test_diff_numofparam_expr_use_ast(self):
        """More complex program"""
        input = Program([
                FuncDecl(Id("main"),[],[],[
                    CallStmt(Id("putIntLn"),[])])])
                        
        expect = "Type Mismatch In Statement: CallStmt(Id(putIntLn),[])"
        self.assertTrue(TestChecker.test(input,expect,445))
    
    def test_no_entry_point(self):
        input = Program([FuncDecl(Id("bac"),[],[],[
            CallStmt(Id("getInt"),[])])])
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,446))
    def test_undeclared_function(self):
        """Simple program: int main() {} """
        input = """procedure main(); begin foo();end"""
        expect = "Undeclared Procedure: foo"
        self.assertTrue(TestChecker.test(input,expect,447))

    def test_diff_numofparam_stmt(self):
        """More complex program"""
        input = """procedure main (); begin
            putIntLn();
        end"""
        expect = "Type Mismatch In Statement: CallStmt(Id(putIntLn),[])"
        self.assertTrue(TestChecker.test(input,expect,448))

    def test_undeclared_function_use_ast(self):
        """Simple program: int main() {} """
        input = Program([FuncDecl(Id("main"),[],[],[
            CallStmt(Id("foo"),[])])])
        expect = "Undeclared Procedure: foo"
        self.assertTrue(TestChecker.test(input,expect,449))

    def test_diff_numofparam_expr_use_ast(self):
        """More complex program"""
        input = Program([
                FuncDecl(Id("main"),[],[],[
                    CallStmt(Id("putIntLn"),[])])])
                        
        expect = "Type Mismatch In Statement: CallStmt(Id(putIntLn),[])"
        self.assertTrue(TestChecker.test(input,expect,450))
    
    def test_no_entry_point(self):
        input = Program([FuncDecl(Id("bac"),[],[],[
            CallStmt(Id("getInt"),[])])])
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,451))
    def test_diff_numofparam_stmt(self):
        """More complex program"""
        input = """procedure main (); begin
            putIntLn();
        end"""
        expect = "Type Mismatch In Statement: CallStmt(Id(putIntLn),[])"
        self.assertTrue(TestChecker.test(input,expect,452))

    def test_undeclared_function_use_ast(self):
        """Simple program: int main() {} """
        input = Program([FuncDecl(Id("main"),[],[],[
            CallStmt(Id("foo"),[])])])
        expect = "Undeclared Procedure: foo"
        self.assertTrue(TestChecker.test(input,expect,453))

    def test_diff_numofparam_expr_use_ast(self):
        """More complex program"""
        input = Program([
                FuncDecl(Id("main"),[],[],[
                    CallStmt(Id("putIntLn"),[])])])
                        
        expect = "Type Mismatch In Statement: CallStmt(Id(putIntLn),[])"
        self.assertTrue(TestChecker.test(input,expect,454))
    
    def test_redecl4(self):
        input = """int a; void b(int c){int c;} int main(){return 9;}"""
        expect = "Redeclared Variable: c"
        self.assertTrue(TestChecker.test(input,expect,455))
    def test_redecl5(self):
        input = """int a,c; int b(int c){int c;return 9;} int main(){return 9;}"""
        expect = "Redeclared Variable: c"
        self.assertTrue(TestChecker.test(input,expect,456))
    def test_redecl6(self):
        input = """int a(int a){int b; return 9;} int b(int c){int a;return 9;} int main(){return 9;}"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,457))
    def test_redecl7(self):
        input = """  int main(){return 9;}"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,458))
