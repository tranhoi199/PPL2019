
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
        if type(funcType) is FloatType and type(expType) is IntType:
            return True
        if type(funcType) is ArrayPointerType and type(expType) in [ArrayPointerType, ArrayType]:
            if type(expType.eleType) == type(funcType.eleType):
                return True
            else:
                return False
        if type(expType) is type(funcType):
            return True
        return False
    def overide_in_block(self, env, x):
        [env.remove(t) for t in env if t.name == x.variable]


    def visitProgram(self, ast, c):
        # decl : List[Decl]
        # return [self.visit(x,c) for x in ast.decl]
        flag = False
        global_evi = []
        global_evi += c
        reach_fun = {}
        
        for x in ast.decl:
            symbol = Symbol(x.variable, x.varType) if type(x) is VarDecl else Symbol(x.name.name, MType([i.varType for i in x.param], x.returnType))
            kind = Variable() if type(x) is VarDecl else Function()
            global_evi.append(self.checkRedeclared(symbol, kind ,global_evi))
           
        for x in ast.decl:
            if type(x) is FuncDecl:
                reach_fun[x.name.name] = 0 if x.name.name != 'main' else 1
                
                if  x.name.name == 'main' :
                    flag = 1     
        if flag:
            reduce(lambda x,y: x + [self.visit(y,(x,global_evi,reach_fun))], ast.decl, self.global_envi) #dong cuoi la c
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
        flag_return = False
        env = c[0] + c[1]

        sym = self.checkRedeclared(Symbol(ast.name.name, MType([i.varType for i in ast.param], ast.returnType)), Function(), c[0] )

        try:
            param = []
            for x in ast.param:
                param.append(self.visit(x,(param, True)))
                self.overide_in_block(env, x)
            
        except Redeclared as e: #e la redeclare lay gia tri str trong Vardecl dung e.n
            raise Redeclared(Parameter(), e.n)
        #flag_func = True #for check return stmt in block
        #c[2] = reach_fun
        flag_return = self.visit( ast.body,(env, ast, param, sym,None, None ,c[2]))
        if flag_return == False and type(ast.returnType) is not VoidType:
            raise FunctionNotReturn(ast.name.name)
        return sym



    def visitBlock(self, ast, c):
        
        lstVar = list(filter(lambda x: type(x) is VarDecl, ast.member))
        #c[2] is param of function
        env = c[0].copy()
        lstSymofVar = c[2].copy() #list(reduce(lambda x,y : x + [self.visit(y,(x,False))], lstVar, c[2]))

        flag_return = False
        lstStmt = list(filter(lambda x: not type(x) is VarDecl, ast.member))

        for x in ast.member:
            if type(x) is VarDecl:
                lstSymofVar.append(self.visit(x, (lstSymofVar, False)))       
                self.overide_in_block(env, x)
            else:
                env += lstSymofVar
                if self.visit(x, ( env, c[1] ,[],c[3], None,c[5] ,c[6])) is True:
                    flag_return = True
        return flag_return

    def visitReturn(self, ast , c):
        # c[2] is symbol of Func
        #if type(c[3].mtype) is MType: # chi khi return trong function moi thuc hien viec tinh toan return
            funcType = c[3].mtype.rettype
            if ast.expr and type(c[3].mtype.rettype) is VoidType:
                raise TypeMismatchInStatement(ast)
            elif type(funcType) is not VoidType:
                if ast.expr:
                    #visitId using c[0] nen truyen vao (c[0], False)
                    expType = self.visit(ast.expr, (c[0],c[1],[], c[3], None,None, c[6]))
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
        at = [self.visit(x,(c[0],c[1],[], c[3], None,None, c[6])) for x in ast.param]
        #####cho nay can sua lai neu foo[3] thi phai la type mismatch do ham foo da co
        res = self.lookup(ast.method.name,c[0],lambda x: x.name)
        if res is None :
            raise Undeclared(Function(),ast.method.name)
        elif not type(res.mtype) is MType:
            raise TypeMismatchInExpression(ast)
        elif len(res.mtype.partype) != len(at) or any(map( lambda x: x == False,[self.checkReturnFunctionCoersion(a,b) for a,b in zip(at, res.mtype.partype)])):
                raise TypeMismatchInExpression(ast)
        else:
            if ast.method.name != c[1].name.name:
                c[6][ast.method.name] = 1
            return res.mtype.rettype
    def visitId(self, ast, c):
        res = self.lookup(ast.name, c[0], lambda x: x.name)
        if res is None:
            raise Undeclared(Identifier() ,ast.name)
        else:
            return res.mtype
    def visitArrayCell(self,ast, c):
        # arr:Expr
        # idx:Expr
        flag_array_cell = True
        try:
            arrType = self.visit(ast.arr, (c[0],c[1],[], c[3], None,None, c[6]))
        except TypeMismatchInExpression:
            raise TypeMismatchInExpression(ast)
        idxType = self.visit(ast.idx, c)
        if type(idxType) is not IntType or (not type(arrType) in [ArrayType, ArrayPointerType]):
            raise TypeMismatchInExpression(ast)
        else:
            return arrType.eleType
    
    def visitIf(self,ast,c):
        # expr:Expr
        # thenStmt:Stmt
        # elseStmt:Stmt
        expType = self.visit(ast.expr, (c[0], c[1], [],c[3], c[4], c[5],c[6]))
        return_thenStmt = False
        return_elseStmt = False
        if type(expType) != type(BoolType()):
            raise TypeMismatchInStatement(ast)  
        else:
            if self.visit(ast.thenStmt, (c[0], c[1], [],c[3], c[4], c[5],c[6])) is True:
                return_thenStmt = True
            if ast.elseStmt:
                return_thenStmt = self.visit(ast.thenStmt, (c[0], c[1], [],c[3], c[4], c[5] if c[5] else False,c[6]))
                return_elseStmt = self.visit(ast.elseStmt, (c[0], c[1], [],c[3], c[4], c[5] if c[5] else False,c[6]))
                if return_thenStmt is True and return_elseStmt is True:
                    return True
                else:
                    return False
            else:
                return False


    def visitBinaryOp(self, ast, c):
        leftH = self.visit(ast.left, c)
        rightH = self.visit(ast.right, c)
        op = str(ast.op)
        if type(leftH) in [VoidType, ArrayType, ArrayPointerType] or type(rightH) in [VoidType, ArrayType, ArrayPointerType]:
            raise TypeMismatchInExpression(ast)
        if op in ['+', '-', '*', '/', '%', '<', '<=', '>', '>=', '=', '||', '&&', '==', '!=']:
            if op in ['=']:
                if type(ast.left) not in [Id, ArrayCell]:
                    raise NotLeftValue(ast.left)
                if type(leftH) == type(rightH): # truong hop danh cho bool, string van thoa
                    return leftH
                else:
                    if type(leftH) is FloatType and type(rightH) is IntType:
                        return FloatType()
                    else:
                        raise TypeMismatchInExpression(ast)
            elif type(leftH) is StringType or type(rightH) is StringType:
                raise TypeMismatchInExpression(ast)
            elif op in ['==', '!=']:
                if type(leftH) is FloatType or type(rightH) is FloatType:
                    raise TypeMismatchInExpression(ast)
                if type(leftH) == type(rightH):
                    return BoolType()
                else:
                    raise TypeMismatchInExpression(ast)
            elif op in ['||', '&&', '!']:
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
            elif op in ['+', '-', '*', '/']:
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
        break_before_return = False
        if type(expType) is not BoolType:
            raise TypeMismatchInStatement(ast)
        else:
            for x in ast.sl:
                if self.visit(x,(c[0], c[1], [],c[3], c[4], flag_break_continue,c[6])) is True:
                    flag_return = True

                
        return flag_return
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
            self.visit(ast.loop, (c[0], c[1], [],c[3], c[4], flag_break_continue, c[6]))
        else:
            raise TypeMismatchInStatement(ast)
    def visitContinue(self, ast, c):
        #c[2] is ast of the ast of parent 
        if c[5] is True:
            return "BC"
        else:
            raise ContinueNotInLoop()
    def visitBreak(self, ast, c):
        if c[5] is True:
            return "BC"
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
