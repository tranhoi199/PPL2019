
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
                if type(x) is Return:
                    flag = True
                    break
            return flag
    def checkReturnFunctionCoersion(self, expType, funcType):
        if type(expType) is type(funcType):
            return True
        else:
            if type(funcType) is FloatType and type(expType) is IntType:
                return True
            if type(funcType) is ArrayPointerType and type(expType) in [ArrayPointerType, ArrayType]:
                return True
            return False


    def visitProgram(self, ast, c):
        # decl : List[Decl]
        # return [self.visit(x,c) for x in ast.decl]
        flag = False
        global_evi = []
        global_evi += c
        reach_fun = {}
        for x in ast.decl:
            global_evi.append(Symbol(x.variable, x.varType)) if type(x) is VarDecl else global_evi.append(Symbol(x.name.name, MType([i.varType for i in x.param], x.returnType)))
        for x in ast.decl:
            if type(x) is FuncDecl:
                reach_fun[x.name.name] = 0 if x.name.name != 'main' else 1
                if type(x.returnType) is VoidType and x.name.name == 'main' and x.param == []:
                    flag = 1
                    break
        if flag:
            reduce(lambda x,y: x + [self.visit(y,(x,global_evi,reach_fun))], ast.decl, c) #dong cuoi la c
            for k in reach_fun:
                if reach_fun[k] == 0:
                    raise UnreachableFunction(k)
        else:
            raise NoEntryPoint()
            
    def visitVarDecl(self, ast, c):
        # variable : str
        #  varType : Type
        # c = (x,global_evi), c = 
        return self.checkRedeclared(Symbol(ast.variable, ast.varType), Variable(), c[0])


    def visitFuncDecl(self,ast, c):
        # name: Id
        # param: List[VarDecl]
        # returnType: Type
        # body: Block
        #flag = [False, False]
        #kiem tra xem function co bi redeclare hay k
        sym = self.checkRedeclared( Symbol(ast.name.name, MType([i.varType for i in ast.param], ast.returnType)), Function(), c[0])
        try:
            param = reduce(lambda x, y: x + [ self.visit(y, (x, True)) ], ast.param, [] )
        except Redeclared as e: #e la redeclare lay gia tri str trong Vardecl dung e.n
            raise Redeclared(Parameter(), e.n)
        #flag_func = True #for check return stmt in block
        self.visit( ast.body,(c[0] + c[1], ast, param, sym, c[2]))
        return sym

    def visitBlock(self, ast, c):
        flag = [False, False]
        lstVar = list(filter(lambda x: type(x) is VarDecl, ast.member))
        #c[2] is param of function
        lstSymofVar = list(reduce(lambda x,y : x + [self.visit(y,(x,False))], lstVar, c[2]))

        lstStmt = list(filter(lambda x: not type(x) is VarDecl, ast.member))
        #body = list cac stmt
        #localVar + c[1] la cac bien trong ham va cac bien toan cuc
        #c[3] is symbol, c[0] is tuple of (glo_evi+builtin_funce,glo_evi)
        # False for stmt in Block

        body = list(map(lambda x: self.visit(x, (lstSymofVar + c[0], c[1] ,[],c[3], flag,c[5] if len(c) == 6 else None,c[4])), lstStmt))
        #if c[4]:

        if len(c) == 5:
            flag[1] = self.checkReturnStmt(lstStmt, flag[0])
            if not flag[0] and not flag[1] :
                raise FunctionNotReturn(c[1].name.name)
        #return self.checkReturnStmt(lstStmt, flag[0]);
    def visitReturn(self, ast , c):
        # c[2] is symbol of Func
        #if type(c[3].mtype) is MType: # chi khi return trong function moi thuc hien viec tinh toan return
            funcType = c[3].mtype.rettype
            if ast.expr and type(c[3].mtype.rettype) is VoidType:
                raise TypeMismatchInStatement(ast)
            elif type(funcType) is not VoidType:
                if ast.expr:
                    #visitId using c[0] nen truyen vao (c[0], False)
                    expType = self.visit(ast.expr, (c[0],False))

                    if self.checkReturnFunctionCoersion(expType, funcType):
                        return True
                    else:
                        raise TypeMismatchInStatement(ast)
                else:
                    raise TypeMismatchInStatement(ast)
            return True

    def visitCallExpr(self, ast, c):
        #     method:Id
        # param:List[Expr]
        at = [self.visit(x,(c[0],c[1],[], c[3], False,None, c[6])) for x in ast.param]
        
        res = self.lookup(ast.method.name,c[0],lambda x: x.name)
        if res is None or not type(res.mtype) is MType:
            raise Undeclared(Function(),ast.method.name)
        elif len(res.mtype.partype) != len(at) or any(map( lambda x: x == False,[self.checkReturnFunctionCoersion(a,b) for a,b in zip(at, res.mtype.partype)])):
            # if c[4]:
            #     raise TypeMismatchInStatement(ast)
            # else:
                raise TypeMismatchInExpression(ast)
        else:
            if ast.method.name != c[1].name.name:
                c[6][ast.method.name] = 1
            return res.mtype.rettype
    def visitId(self, ast, c):
        res = self.lookup(ast.name, list(filter(lambda x: type(x.mtype) is not MType, c[0])) , lambda x: x.name)
        if res is None:
            raise Undeclared(Identifier() ,ast.name)
        else:
            return res.mtype
    def visitArrayCell(self,ast, c):
        # arr:Expr
        # idx:Expr
        arrType = self.visit(ast.arr, c)
        idxType = self.visit(ast.idx, c)
        if type(idxType) is not IntType or type(arrType) is not ArrayType:
            raise TypeMismatchInExpression(ast)
        else:
            return arrType.eleType
    
    def visitIf(self,ast,c):
        # expr:Expr
        # thenStmt:Stmt
        # elseStmt:Stmt
        expType = self.visit(ast.expr, c[0])
    
        if type(expType) != type(BoolType()):
            raise TypeMismatchInStatement(ast)  
        else:
            if not c[3][1]:
                c[3][0] = self.checkReturnStmt(ast.thenStmt, c[3][0])
            self.visit(ast.thenStmt, (c[0], ast, [], ))

    def visitBinaryOp(self, ast, c):
        leftH = self.visit(ast.left, c)
        rightH = self.visit(ast.right, c)
        op = str(ast.op)
        if type(leftH) in [VoidType, ArrayType, ArrayPointerType] or type(rightH) in [VoidType, ArrayType, ArrayPointerType]:
            raise TypeMismatchInExpression(ast)
        if op in ['+', '-', '*', '/', '%', '<', '<=', '>', '>=', '=', '||', '&&', '==', '!=']:
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
    def visitUnaryOp(self, ast, c):
        op = str(ast.op)
        bodyType = self.visit(ast.body, c)
        if op in ['!']:
            if type(bodyType) is not BoolType:
                raise TypeMismatchInExpression(ast)
            else:
                return bodyType
        else:
            if type(bodyType) in [IntType, FloatType]:
                return bodyType
            else:
                raise TypeMismatchInExpression(ast)
    def visitDowhile(self, ast, c):
        # sl:List[Stmt]
        # exp: Expr
        flag_return = False
        expType = self.visit(ast.exp, c)
        flag_break_continue = True
        if type(expType) is not BoolType:
            raise TypeMismatchInStatement(ast)
        else:
            for x in ast.sl:
                if self.visit(x,(c[0], c[1], [],c[3], c[4], flag_break_continue)):
                    flag_return = True
                
            
            #[self.visit(x,(c[0], c[1], [],c[3], c[4], flag_break_continue)) for x in ast.sl]

    def visitFor(self, ast, c):
        # expr1:Expr
        # expr2:Expr
        # expr3:Expr
        # loop:Stmt
        exp1Type = self.visit(ast.expr1, c)
        exp2Type = self.visit(ast.expr2, c)
        exp3Type = self.visit(ast.expr3, c)
        flag_break_continue = True

        if type(exp1Type) is IntType and type(exp3Type) is IntType and type(exp2Type) is BoolType:
            return self.visit(ast.loop, (c[0], c[1], [],c[3], c[4], flag_break_continue))
        else:
            raise TypeMismatchInStatement(ast)
    def visitContinue(self, ast, c):
        #c[2] is ast of the ast of parent 
        if c[5] == True:
            return Continue()
        else:
            raise ContinueNotInLoop()
    def visitBreak(self, ast, c):
        if c[5] == True:
            return Break()
        else:
            raise BreakNotInLoop()


    def visitIntLiteral(self,ast, c): 
        return IntType() 
    def visitFloatLiteral(self,ast,c):
        return FloatType()
    def visitBooleanLiteral(self,ast,c):
        return BoolType()
    def visitStringLiteral(self,ast,c):
        return StringType()
