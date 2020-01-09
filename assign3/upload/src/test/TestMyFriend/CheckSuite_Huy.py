import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite (unittest.TestCase):
	def test_var_redecl1 (self):
		input = '''void main () {}
				int a;
				int b, a;
		'''
		expect = "Redeclared Variable: a"
		self.assertTrue (TestChecker.test (input, expect, 400))

	def test_var_redecl2 (self):
		input = '''int a;
				int b;
				int a;
				void main () {}
		'''
		expect = "Redeclared Variable: a"
		self.assertTrue (TestChecker.test (input, expect, 401))

	def test_var_redecl3 (self):
		input = '''int a[5];
				int a;
				void main () {}
		'''
		expect = "Redeclared Variable: a"
		self.assertTrue (TestChecker.test (input, expect, 402))

	def test_var_redecl4 (self):
		input = '''int a;
				int b[5], a[10];
				void main () {}
		'''
		expect = "Redeclared Variable: a"
		self.assertTrue (TestChecker.test (input, expect, 403))

	def test_var_redecl6 (self):
		input = '''int a[5];
				int a[10];
				void main () {}
		'''
		expect = "Redeclared Variable: a"
		self.assertTrue (TestChecker.test (input, expect, 404))

	def test_func_redecl1 (self):
		input = '''void main () {}
				void main () {}
		'''
		expect = "Redeclared Function: main"
		self.assertTrue (TestChecker.test (input, expect, 405))

	def test_func_redecl2 (self):
		input = '''void main () {}
				//int b () {}
				void main () {}
		'''
		expect = "Redeclared Function: main"
		self.assertTrue (TestChecker.test (input, expect, 406))

	def test_func_redecl3 (self):
		input = '''int a () { return 0;}
				void main () {}
				void a () {}
		'''
		expect = "Redeclared Function: a"
		self.assertTrue (TestChecker.test (input, expect, 407))

	def test_func_redecl4 (self):
		input = '''int a () {return 0;}
				void main () {}
				void b () {}
				void a () {}
		'''
		expect = "Redeclared Function: a"
		self.assertTrue (TestChecker.test (input, expect, 408))

	def test_func_redecl5 (self):
		input = '''void a () {}
				void a (int b) {}
				void main () {}
		'''
		expect = "Redeclared Function: a"
		self.assertTrue (TestChecker.test (input, expect, 409))

	def test_func_redecl6 (self):
		input = '''int a;
				void main () {}
				void a (int b) {}
		'''
		expect = "Redeclared Function: a"
		self.assertTrue (TestChecker.test (input, expect, 410))

	def test_param_redecl1 (self):
		input = '''void main (int a) {}
		'''
		expect = ""
		self.assertTrue (TestChecker.test (input, expect, 411))

	def test_param_redecl2 (self):
		input = '''void main (int b, int b) {}
		'''
		expect = "Redeclared Parameter: b"
		self.assertTrue (TestChecker.test (input, expect, 412))

	def test_param_redecl3 (self):
		input = '''void main (int b, int c, int b) {}
		'''
		expect = "Redeclared Parameter: b"
		self.assertTrue (TestChecker.test (input, expect, 413))

	def test_param_redecl4 (self):
		input = '''void main (int b, float b) {}
		'''
		expect = "Redeclared Parameter: b"
		self.assertTrue (TestChecker.test (input, expect, 414))

	def test_param_redecl5 (self):
		input = '''void main (int b[], int b[]) {}
		'''
		expect = "Redeclared Parameter: b"
		self.assertTrue (TestChecker.test (input, expect, 415))

	def test_param_redecl6 (self):
		input = '''void main (int b[], float b[]) {}
		'''
		expect = "Redeclared Parameter: b"
		self.assertTrue (TestChecker.test (input, expect, 416))

	def test_no_entry1 (self):
		input = '''int a;'''
		expect = "No Entry Point"
		self.assertTrue (TestChecker.test (input, expect, 417))

	def test_no_entry2 (self):
		input = '''void main () {}'''
		expect = ""
		self.assertTrue (TestChecker.test (input, expect, 418))

	def test_no_entry3 (self):
		input = '''int main () {return 0;}'''
		expect = ""
		self.assertTrue (TestChecker.test (input, expect, 419))

	def test_no_entry4 (self):
		input = '''int main (int a) {return 0;}'''
		expect = ""
		self.assertTrue (TestChecker.test (input, expect, 420))

	def test_no_entry5 (self):
		input = '''void main (int a) {}'''
		expect = ""
		self.assertTrue (TestChecker.test (input, expect, 421))

	def test_no_entry6 (self):
		input = '''int a;'''
		expect = "No Entry Point"
		self.assertTrue (TestChecker.test (input, expect, 422))

	def test_var_redecl_in_func1 (self):
		input = '''void main ()
		{
			int a;
			int a;
		}
		'''
		expect = "Redeclared Variable: a"
		self.assertTrue (TestChecker.test (input, expect, 423))
	
	def test_var_redecl_in_func2 (self):
		input = '''void main ()
		{
			int a;
			int b;
			int a;
		}
		'''
		expect = "Redeclared Variable: a"
		self.assertTrue (TestChecker.test (input, expect, 424))

	def test_var_redecl_in_func3 (self):
		input = '''void main ()
		{
			int a[5];
			int b, c;
			float a;
		}
		'''
		expect = "Redeclared Variable: a"
		self.assertTrue (TestChecker.test (input, expect, 425))

	def test_var_redecl_in_func4 (self):
		input = '''void main ()
		{
			int a[10];
			float a[15];
		}
		'''
		expect = "Redeclared Variable: a"
		self.assertTrue (TestChecker.test (input, expect, 426))
	
	def test_var_redecl_in_func5 (self):
		input = '''void main (int a)
		{
			a = 5;
		}
		int a;
		void a () {}
		'''
		expect = "Redeclared Function: a"
		self.assertTrue (TestChecker.test (input, expect, 427))
	
	def test_var_redecl_in_func6 (self):
		input = '''void main (int a)
		{
			int a[5];
		}
		'''
		expect = "Redeclared Variable: a"
		self.assertTrue (TestChecker.test (input, expect, 428))
	
	def test_var_redecl_in_func7 (self):
		input = '''void main (int a[])
		{
			int a;
		}
		'''
		expect = "Redeclared Variable: a"
		self.assertTrue (TestChecker.test (input, expect, 429))

	def test_var_redecl_in_func8 (self):
		input = '''void main (int a)
		{
			float a;
		}
		'''
		expect = "Redeclared Variable: a"
		self.assertTrue (TestChecker.test (input, expect, 430))

	def test_var_undecl1 (self):
		input = '''void main ()
		{
			int a;
			a = 2;
		}
		'''
		expect = ""
		self.assertTrue (TestChecker.test (input, expect, 431))
	
	def test_var_undecl2 (self):
		input = '''int a;
		void main ()
		{
			a = 2;
		}
		'''
		expect = ""
		self.assertTrue (TestChecker.test (input, expect, 432))
	
	def test_var_undecl3 (self):
		input = '''
		void main ()
		{
			a = 2;
		}
		int a;
		'''
		expect = ""
		self.assertTrue (TestChecker.test (input, expect, 433))

	def test_var_undecl4 (self):
		input = '''void main (int a)
		{
			a = 2;
		}
		'''
		expect = ""
		self.assertTrue (TestChecker.test (input, expect, 434))

	def test_var_undecl5 (self):
		input = '''void main (int a)
		{
			{
			int a;
			a = 2;}
		}
		'''
		expect = ""
		self.assertTrue (TestChecker.test (input, expect, 435))

	def test_var_undecl6 (self):
		input = '''void main ()
		{
			int a;
			{
			int a;
			a = 2;}
		}
		'''
		expect = ""
		self.assertTrue (TestChecker.test (input, expect, 436))

	def test_var_undecl7 (self):
		input = '''void main ()
		{
			int a;
			{
			a = 2;}
		}
		'''
		expect = ""
		self.assertTrue (TestChecker.test (input, expect, 437))

	def test_func_undecl1 (self):
		input = '''void main (int a)
		{
			f ();
		}
		'''
		expect = "Undeclared Function: f"
		self.assertTrue (TestChecker.test (input, expect, 438))

	def test_func_undecl2 (self):
		input = '''void main (int a)
		{
			a ();
		}
		'''
		expect = "Undeclared Function: a"
		self.assertTrue (TestChecker.test (input, expect, 439))
	
	def test_func_undecl3 (self):
		input = '''void main (int a)
		{
			getInt ();
		}
		'''
		expect = ""
		self.assertTrue (TestChecker.test (input, expect, 440))

	def test_func_undecl4 (self):
		input = '''void main (int a)
		{
			main (1);
		}
		'''
		expect = ""
		self.assertTrue (TestChecker.test (input, expect, 441))

	def test_func_undecl5 (self):
		input = '''void main (int a)
		{
			a ();
		}
		int a () {}
		'''
		expect = "Undeclared Function: a"
		self.assertTrue (TestChecker.test (input, expect, 442))

	def test_func_undecl6 (self):
		input = '''void main ()
		{
			a ();
		}
		int a;
		'''
		expect = "Undeclared Function: a"
		self.assertTrue (TestChecker.test (input, expect, 443))
	
	def test_redecl1 (self):
		input = '''void main ()
		{
			a ();
		}
		int a;
		void a () {}
		'''
		expect = "Redeclared Function: a"
		self.assertTrue (TestChecker.test (input, expect, 444))

	def test_redecl2 (self):
		input = '''
        int a;
		void a() {
            
        }
        void main ()
		{
			a = 5;
		}

		'''
		expect = "Redeclared Function: a"
		self.assertTrue (TestChecker.test (input, expect, 445))

	def test_unreachable_func1 (self):
		input = '''void main ()
		{
		}
		void a () {}
		'''
		expect = "Unreachable Function: a"
		self.assertTrue (TestChecker.test (input, expect, 446))

	def test_unreachable_func2 (self):
		input = '''void main ()
		{
			a ();
		}
		void a () {}
		'''
		expect = ""
		self.assertTrue (TestChecker.test (input, expect, 447))

	def test_unreachable_func3 (self):
		input = '''void main ()
		{
			{a ();}
		}
		void a () {}
		'''
		expect = ""
		self.assertTrue (TestChecker.test (input, expect, 448))

	def test_unreachable_func4 (self):
		input = '''void main ()
		{
		}
		void a () {}
		void b () {a () ;}
		'''
		expect = "Unreachable Function: b"
		self.assertTrue (TestChecker.test (input, expect, 449))

	def test_unreachable_func5 (self):
		input = '''void main ()
		{
			a ();
		}
		void a () {b ();}
		void b () {}
		'''
		expect = ""
		self.assertTrue (TestChecker.test (input, expect, 450))
	
	def test_unreachable_func6 (self):
		input = '''void main ()
		{
			a ();
		}
		void a () {b ();}
		void b () {c ();}
		void c () {}
		'''
		expect = ""
		self.assertTrue (TestChecker.test (input, expect, 451))

	def test_unreachable_func7 (self):
		input = '''void main ()
		{
		}
		void a () {b ();}
		void b () {}
		'''
		expect = "Unreachable Function: a"
		self.assertTrue (TestChecker.test (input, expect, 452))

	def test_break1 (self):
		input = '''void main ()
		{
			do
			{}
			while (true);
		}
		'''
		expect = ""
		self.assertTrue (TestChecker.test (input, expect, 453))

	def test_break2 (self):
		input = '''void main ()
		{
			for (1;true;1)
			{
			}
		}
		'''
		expect = ""
		self.assertTrue (TestChecker.test (input, expect, 454))

	def test_break3 (self):
		input = '''void main ()
		{
			do
			{break;}
			while (true);
		}
		'''
		expect = ""
		self.assertTrue (TestChecker.test (input, expect, 455))

	def test_break4 (self):
		input = '''void main ()
		{
			for (1;true;1)
			{
				break;
			}
		}
		'''
		expect = ""
		self.assertTrue (TestChecker.test (input, expect, 456))

	def test_break5 (self):
		input = '''void main ()
		{
			break;
		}
		'''
		expect = "Break Not In Loop"
		self.assertTrue (TestChecker.test (input, expect, 457))

	def test_break6 (self):
		input = '''void main ()
		{
			do
			{break; break;}
			while (true);
		}
		'''
		expect = ""
		self.assertTrue (TestChecker.test (input, expect, 458))

	def test_break7 (self):
		input = '''void main ()
		{
			do
			{break; {break;}} break;
			while (true);
		}
		'''
		expect = ""
		self.assertTrue (TestChecker.test (input, expect, 459))

	def test_break8 (self):
		input = '''void main ()
		{
			do
			break;
			{
				for (1;true;1)
				{
					break;
					{break;}
				}
				break;
			}
			break;
			while (true);
		}
		'''
		expect = ""
		self.assertTrue (TestChecker.test (input, expect, 460))

	def test_continue1 (self):
		input = '''void main ()
		{
			do
			{continue;}
			while (true);
		}
		'''
		expect = ""
		self.assertTrue (TestChecker.test (input, expect, 461))

	def test_continue2 (self):
		input = '''void main ()
		{
			continue;
		}
		'''
		expect = "Continue Not In Loop"
		self.assertTrue (TestChecker.test (input, expect, 462))

	def test_continue3 (self):
		input = '''void main ()
		{
			do
			{}
			while (true);
			continue;
		}
		'''
		expect = "Continue Not In Loop"
		self.assertTrue (TestChecker.test (input, expect, 463))

	def test_continue4 (self):
		input = '''void main ()
		{
			do
			continue;
			{
				continue; {continue;}
				for (1;true;1)
				{
					continue;
					continue;
					{continue;}
					for (1;true;1)
					{
						continue;
					}
				}
			}
			continue;
			while (true);
		}
		'''
		expect = ""
		self.assertTrue (TestChecker.test (input, expect, 464))

	def test_notleftvalue1 (self):
		input = '''void main ()
		{
			int a;
			a = 5;
		}
		'''
		expect = ""
		self.assertTrue (TestChecker.test (input, expect, 465))

	def test_notleftvalue2 (self):
		input = '''void main ()
		{
			5 = 5;
		}
		'''
		expect = "Not Left Value: BinaryOp(=,IntLiteral(5),IntLiteral(5))"
		self.assertTrue (TestChecker.test (input, expect, 466))

	def test_notleftvalue3 (self):
		input = '''void main ()
		{
			int a[5];
			a[1] = 5;
		}
		'''
		expect = ""
		self.assertTrue (TestChecker.test (input, expect, 467))

	def test_notleftvalue4 (self):
		input = '''void main ()
		{
			a ()[5] = 4;
		}
		int[] a () {int x[5];return x;}
		'''
		expect = ""
		self.assertTrue (TestChecker.test (input, expect, 468))

	def test_type_expression1 (self):
		input = '''void main ()
		{
			int a;
			a = 5;
			a = -1;
			a = 5 - 1;
			string b;
			b = "abc";
			boolean c;
			c = true;
			c = !false;
			c = true == true;
			c = true != false;
			c = 5 > 4;
			c = -4 > -9.0;
			c = 5 < 4;
			c = 5 < 4.0;
			c = -5 >= 9;
			c = 5 >= 0.9;
			c = 5 <= 0;
			c = 5 <= -1.0;
			c = 1.0 > 9;
			c = 1.0 > 0.1;
			c = 1.0 >= 9;
			c = 1.0 >= 0.1;
			c = 1.0 < 9;
			c = 1.0 < 0.1;
			c = 1.0 <= 9;
			c = 1.0 <= 9.0;
			c = 1 == 1;

			float d;
			d = 5.0;
			d = 2;
			d = -2;
			d = -2.0;
			d = 2 + 4;
			d = -2 + 1 - 0.1;
			d = -2.1 + 4;
			d = 5.0 + 4;
		}
		'''
		expect = ""
		self.assertTrue (TestChecker.test (input, expect, 469))

	def test_type_expression2 (self):
		input = '''void main ()
		{
			int a;
			a = 5.0;
		}
		'''
		expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),FloatLiteral(5.0))"
		self.assertTrue (TestChecker.test (input, expect, 470))

	def test_type_expression3 (self):
		input = '''void main ()
		{
			int a[5];
			a = 10;
		}
		'''
		expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),IntLiteral(10))"
		self.assertTrue (TestChecker.test (input, expect, 471))

	def test_type_expression4 (self):
		input = '''void main ()
		{
			int a[5];
			a = 5.0;
		}

		'''
		expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),FloatLiteral(5.0))"
		self.assertTrue (TestChecker.test (input, expect, 472))

	def test_type_expression5 (self):
		input = '''void main ()
		{
			int a;
			a = 5 + 5.0;
		}
		'''
		expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),BinaryOp(+,IntLiteral(5),FloatLiteral(5.0)))"
		self.assertTrue (TestChecker.test (input, expect, 473))

	def test_type_expression6 (self):
		input = '''void main ()
		{
			int a;
			a = 5 > 3;
		}
		'''
		expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),BinaryOp(>,IntLiteral(5),IntLiteral(3)))"
		self.assertTrue (TestChecker.test (input, expect, 474))

	def test_type_expression7 (self):
		input = '''void main ()
		{
			boolean a;
			a = !4;
		}
		'''
		expect = "Type Mismatch In Expression: UnaryOp(!,IntLiteral(4))"
		self.assertTrue (TestChecker.test (input, expect, 475))

	def test_type_expression8 (self):
		input = '''void main ()
		{
			int a;
			a = 1 == 2;
		}
		'''
		expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),BinaryOp(==,IntLiteral(1),IntLiteral(2)))"
		self.assertTrue (TestChecker.test (input, expect, 476))

	def test_type_expression9 (self):
		input = '''void main ()
		{
			int a[5];
			a[1.0] = 5;
		}
		'''
		expect = "Type Mismatch In Expression: ArrayCell(Id(a),FloatLiteral(1.0))"
		self.assertTrue (TestChecker.test (input, expect, 477))

	def test_type_expression10 (self):
		input = '''void main ()
		{
			int a[5];
			a[1==1] = 1;
		}
		'''
		expect = "Type Mismatch In Expression: ArrayCell(Id(a),BinaryOp(==,IntLiteral(1),IntLiteral(1)))"
		self.assertTrue (TestChecker.test (input, expect, 478))

	def test_type_expression11 (self):
		input = '''void main ()
		{
			f (1, 2);
		}
		int f (int a, int b) {return 5;}
		'''
		expect = ""
		self.assertTrue (TestChecker.test (input, expect, 479))

	def test_type_expression12 (self):
		input = '''void main ()
		{
			f (1);
		}
		int f (int a, int b) {return 1;}
		'''
		expect = "Type Mismatch In Expression: CallExpr(Id(f),[IntLiteral(1)])"
		self.assertTrue (TestChecker.test (input, expect, 480))

	def test_type_expression13 (self):
		input = '''void main ()
		{
			f (1, 2, 3);
		}
		int f (int a, int b) {return 1;}
		'''
		expect = "Type Mismatch In Expression: CallExpr(Id(f),[IntLiteral(1),IntLiteral(2),IntLiteral(3)])"
		self.assertTrue (TestChecker.test (input, expect, 481))

	def test_type_expression14 (self):
		input = '''void main ()
		{
			f (1.0, 2);
		}
		int f (int a, int b) {return 1;}
		'''
		expect = "Type Mismatch In Expression: CallExpr(Id(f),[FloatLiteral(1.0),IntLiteral(2)])"
		self.assertTrue (TestChecker.test (input, expect, 482))

	def test_type_expression15 (self):
		input = '''void main ()
		{
			int c[5];
			float d[4];
			f (1, 2.0);
			f (1, 2);
			f (c[0], d[4]);
			f (1+2, 0.1-3);
			f2 (true, !false);
			f2 (2==2, 3>4.0);
			f3 (c);
			f3 (f4 ());
		}
		int f (int a, float b) {return 1;}
		int f2 (boolean a, boolean b) {return 1;}
		int f3 (int a[]) {return 1;}
		int[] f4 () {int x[5]; return x;}
		'''
		expect = ""
		self.assertTrue (TestChecker.test (input, expect, 483))

	def test_type_expression16 (self):
		input = '''void main ()
		{
			f (1, 2);
		}
		int f (int a[], int b) {return 1;}
		'''
		expect = "Type Mismatch In Expression: CallExpr(Id(f),[IntLiteral(1),IntLiteral(2)])"
		self.assertTrue (TestChecker.test (input, expect, 484))
	
	def test_type_expression17 (self):
		input = '''void main ()
		{
			int a[5];
			f (f2 (), 2);
			f3 (a);
		}
		int f (int a[], int b) {return 1;}
		int[] f2 () {int x[5]; return x;}
		int f3 (float a[]) {return 1;}
		'''
		expect = "Type Mismatch In Expression: CallExpr(Id(f3),[Id(a)])"
		self.assertTrue (TestChecker.test (input, expect, 485))

	def test_type_expression18 (self):
		input = '''void main ()
		{
			f ( f2() );
		}
		int f (boolean a[]) {
            return 1;
        }
		int[] f2 () {
            int x[5];
            return x;
        }
		'''
		expect = "Type Mismatch In Expression: CallExpr(Id(f),[CallExpr(Id(f2),[])])"
		self.assertTrue (TestChecker.test (input, expect, 486))
	
	def test_type_statement1 (self):
		input = '''void main ()
		{
			int a;
			boolean b;
			int c[5];
			boolean d[5];
			if (true) {}
			if (!true) {} else {}
			if (2!=3) {}
			for (1;true;c[3]) {}
			for (a;b;a) {}
			if (b)
			{
				do {} while (true);
				do {} while (b);
				do {} while (!b);
				do {} while (1>3);
				do {} while (d[5]);
			}
			else {}
		}
		'''
		expect = ""
		self.assertTrue (TestChecker.test (input, expect, 487))

	def test_type_statement2 (self):
		input = '''void main ()
		{
			if (1) {}
		}
		'''
		expect = "Type Mismatch In Statement: If(IntLiteral(1),Block([]))"
		self.assertTrue (TestChecker.test (input, expect, 488))

	def test_type_statement3 (self):
		input = '''void main ()
		{
			boolean a[5];
			if (a) {}
		}
		'''
		expect = "Type Mismatch In Statement: If(Id(a),Block([]))"
		self.assertTrue (TestChecker.test (input, expect, 489))

	def test_type_statement4 (self):
		input = '''void main ()
		{
			for (1;1;1) {}
		}
		'''
		expect = "Type Mismatch In Statement: For(IntLiteral(1);IntLiteral(1);IntLiteral(1);Block([]))"
		self.assertTrue (TestChecker.test (input, expect, 490))

	def test_type_statement5 (self):
		input = '''void main ()
		{
			int a;
			for (1;a;1) {}
		}
		'''
		expect = "Type Mismatch In Statement: For(IntLiteral(1);Id(a);IntLiteral(1);Block([]))"
		self.assertTrue (TestChecker.test (input, expect, 491))

	def test_type_statement6 (self):
		input = '''void main ()
		{
			int a[5];
			for (a;true;1) {}
		}
		'''
		expect = "Type Mismatch In Statement: For(Id(a);BooleanLiteral(true);IntLiteral(1);Block([]))"
		self.assertTrue (TestChecker.test (input, expect, 492))

	def test_type_statement7 (self):
		input = '''void main ()
		{
			do {} while (1);
		}
		'''
		expect = "Type Mismatch In Statement: Dowhile([Block([])],IntLiteral(1))"
		self.assertTrue (TestChecker.test (input, expect, 493))

	def test_type_statement8 (self):
		input = '''void main ()
		{
			int a;
			do {} while (a);
		}
		'''
		expect = "Type Mismatch In Statement: Dowhile([Block([])],Id(a))"
		self.assertTrue (TestChecker.test (input, expect, 494))

	def test_func_not_ret1 (self):
		input = '''int main ()
		{
			int a;
			a = 5;
		}
		'''
		expect = "Function main Not Return "
		self.assertTrue (TestChecker.test (input, expect, 495))

	def test_func_not_ret2 (self):
		input = '''int main ()
		{
			if (true)
			{
				return 1;
			}
			else
			{
			}
		}
		'''
		expect = "Function main Not Return "
		self.assertTrue (TestChecker.test (input, expect, 496))

	def test_func_not_ret3 (self):
		input = '''int main ()
		{
			for (1;true;1)
			{
				break;
				return 1;
			}
			do
			{
				break;
				{{return 1;}}
			}
			while (true);
		}
		'''
		expect = ""
		self.assertTrue (TestChecker.test (input, expect, 497))

	def test_func_not_ret4 (self):
		input = '''int main ()
		{
			if (true)
			{{{
				for (1;true;1) {{{ do {return 1;} while (true); }}}
				do { if (false) {return 1;} else {return 1;} } while (true);
			}}}
			else
			{
				if (true) {if (true) {return 1;} else {}}
				else { if (true) {return 1;} else {return 1;}}
			}
		}
		'''
		expect = "Function main Not Return "
		self.assertTrue (TestChecker.test (input, expect, 498))

	def test_func_not_ret5 (self):
		input = '''void main ()
		{
			return;
		}
		'''
		expect = ""
		self.assertTrue (TestChecker.test (input, expect, 499))

