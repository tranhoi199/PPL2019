
"""
 * @author nhphung
"""
from AST import * 
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import *

class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value
class ExpUtil():
    @staticmethod
    def isNumberType(exp):
        return type(exp) in [IntType, FloatType]
    @staticmethod
    def notNumber(exp):
        return not ExpUtil.isNumberType(exp)
    @staticmethod
    def coercions(left, right):
        return FloatType() if FloatType in [type(left), type(right)] else IntType()
class StaticChecker(BaseVisitor,Utils):

    global_envi = [
    Symbol("getInt",MType([],IntType())),
    Symbol("putInt", MType([IntType()], VoidType())),
    Symbol("putIntLn",MType([IntType()],VoidType())),
    Symbol("getFloat",MType([],FloatType())),
    Symbol("putFloat",MType([FloatType()], VoidType())),
    Symbol("putFloatLn",MType([FloatType()], VoidType())),
    Symbol("putBool", MType([BoolType()], VoidType())),
    Symbol("putBoolLn", MType([BoolType()], VoidType())),
    Symbol("putString", MType([StringType()], VoidType())),
    Symbol("putStringLn", MType([StringType()], VoidType())),
    Symbol("putLn", MType([], VoidType()))
    ]
            
    def __init__(self,ast):
        #print(ast)
        #print(ast)
        #print()
        self.ast = ast

    
    def check(self):
        return self.visit(self.ast,StaticChecker.global_envi)


    def checkRedeclared(self, sym, kind, c):
        if self.lookup(sym.name, c, lambda x: x.name):
            raise Redeclared(kind, sym.name)
        return sym
    def checkReturnStmt(self, lst, flag):
        if flag:
            return flag 
        else:
            for x in lst:
                if type(x) == Return:
                    flag = True
                    break
            return flag

    def visitProgram(self, ast, c):
        # decl : List[Decl]
        # return [self.visit(x,c) for x in ast.decl]
        flag = False
        global_evi = []
        global_evi += c
        for x in ast.decl:
            global_evi.append(Symbol(x.variable, x.varType)) if type(x) is VarDecl else global_evi.append(Symbol(x.name.name, MType([i.varType for i in x.param], x.returnType)))
        for x in ast.decl:
            if type(x) is FuncDecl:
                if type(x.returnType) is VoidType and x.name.name == 'main' and x.param == []:
                    flag = 1
                    break
        if flag:
            return reduce(lambda x,y: x + [self.visit(y,(x,global_evi))], ast.decl, c) #dong cuoi la c
        else:
            raise NoEntryPoint()

    def visitVarDecl(self, ast, c):
        # variable : str
        #  varType : Type
        return self.checkRedeclared(Symbol(ast.variable, ast.varType), Variable(), c[0])

    def visitFuncDecl(self,ast, c):
        # name: Id
        # param: List[VarDecl]
        # returnType: Type
        # body: Block
        flag = [False, False]
        #kiem tra xem function co bi redeclare hay k
        sym = self.checkRedeclared( Symbol(ast.name.name, MType([i.varType for i in ast.param], ast.returnType)), Function(), c[0])
        try:
            param = reduce(lambda x, y: x + [ self.visit(y, (x, True)) ], ast.param, [] )
        except Redeclared as e: #e la redeclare lay gia tri str trong Vardecl dung e.n
            raise Redeclared(Parameter(), e.n)
        self.visit(ast.body,(c, ast, param, sym, ast.returnType ))
        return sym

    def visitBlock(self, ast, c):
        flag = [False, False]
        lstVar = list(filter(lambda x: type(x) is VarDecl, ast.member))
        #c[2] is param of function
        lstSymofVar = reduce(lambda x,y : x + [self.visit(y,(x,False))], lstVar, c[2])

        lstStmt = list(filter(lambda x: not type(x) is VarDecl, ast.member))
        #body = list cac stmt
        #localVar + c[1] la cac bien trong ham va cac bien toan cuc
        #c[3] is symbol, c[0] is tuple of (glo_evi+builtin_funce,glo_evi)
        body = list(map(lambda x: self.visit(x, (lstSymofVar + c[0][0], ast, c[3], flag)), lstStmt))
        flag[1] = self.checkReturnStmt(lstStmt, flag[0])
        if not flag[0] and not flag[1] and not type(c[1].returnType) is VoidType:
            raise FunctionNotReturn(c[1].name.name)

    def visitCallExpr(self, ast, c):
        #     method:Id
        # param:List[Expr]
        at = [self.visit(x,(c[0],False)) for x in ast.param]
        
        res = self.lookup(ast.method.name,c[0],lambda x: x.name)
        if res is None or not type(res.mtype) is MType:
            raise Undeclared(Function(),ast.method.name)
        elif len(res.mtype.partype) != len(at):
            if c[1]:
                raise TypeMismatchInStatement(ast)
            else:
                raise TypeMismatchInExpression(ast)
        else:
            return res.mtype.rettype
    def visitId(self, ast, c):
        res = self.lookup(ast.name,list(filter(lambda x: type(x.mtype) is not MType, c[0])) , lambda x: x.name)
        if res is None:
            raise Undeclared(Identifier() ,ast.name)
        return res.mtype

    
    def visitIf(self,ast,c):
        # expr:Expr
        # thenStmt:Stmt
        # elseStmt:Stmt
        expType = self.visit(ast.expr, c[0])
    
        if type(expType) != type(BoolType()):
            raise TypeMismatchInStatement(ast)     

    def visitBinaryOp(self, ast, c):
        leftH = self.visit(ast.left, c)
        rightH = self.visit(ast.right, c)
        op = str(ast.op)
        if type(leftH) in [StringType, ArrayType, ArrayPointerType] or type(rightH) in [StringType, ArrayType, ArrayPointerType]:
            raise TypeMismatchInExpression(ast)
        if op in ['+', '-', '*', '/', '%', '<', '<=', '>', '>=', '=', '||', '&&']:
            if op in ['=']:
                if type(leftH) == type(rightH): # truong hop danh cho bool, string van thoa
                    return leftH
                else:
                    if type(leftH) is FloatType and type(rightH) is IntType:
                        return FloatType()
                    else:
                        raise TypeMismatchInExpression(ast)
            elif op in ['||', '&&']:
                if type(leftH) is BoolType and type(rightH) is BoolType:
                    return BoolType()
                else:
                    raise TypeMismatchInExpression(ast)
            elif ExpUtil.notNumber(leftH) or ExpUtil.notNumber(rightH):
                raise TypeMismatchInExpression(ast)
            
            elif op in ['%']:
                if FloatType in [type(leftH), type(rightH)]:
                    raise TypeMismatchInExpression(ast)
                return IntType()
            elif op in ['/']:
                return FloatType()
            elif op in ['+', '-', '*']:
                return ExpUtil.coercions(leftH,rightH)
            else:
                return BoolType()
            

    def visitIntLiteral(self,ast, c): 
        return IntType() 
    def visitFloatLiteral(self,ast,c):
        return FloatType()
    def visitBooleanLiteral(self,ast,c):
        return BoolType()
    def visitStringLiteral(self,ast,c):
        return StringType()
