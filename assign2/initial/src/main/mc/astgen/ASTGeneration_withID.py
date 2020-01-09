from MCVisitor import MCVisitor
from MCParser import MCParser
from AST import *



def flatten(lst):
    list_ls = []
    for i in lst:
        if isinstance(i, list):
            list_ls.extend(i)
        else:
            list_ls.append(i)
    return list_ls
class ASTGeneration(MCVisitor):
    """def visitProgram(self,ctx:MCParser.ProgramContext):
        return Program([FuncDecl(Id("main"),[],self.visit(ctx.mctype()),Block([self.visit(ctx.body())] if ctx.body() else []))])

    def visitMctype(self,ctx:MCParser.MctypeContext):
        if ctx.INTTYPE():
            return IntType
        else:
            return VoidType

    def visitBody(self,ctx:MCParser.BodyContext):
        return self.visit(ctx.funcall())
  
  	
    def visitFuncall(self,ctx:MCParser.FuncallContext):
        return CallExpr(Id(ctx.ID().getText()),[self.visit(ctx.exp())] if ctx.exp() else [])

    def visitExp(self,ctx:MCParser.ExpContext):
        if (ctx.funcall()):
            return self.visit(ctx.funcall())
        else:
            return IntLiteral(int(ctx.INTLIT().getText()))"""

        # visit program syntax

    # program: declar+ EOF
    def visitProgram(self, ctx:MCParser.ProgramContext):
        declList = []
        for x in ctx.declar():
            decl = self.visit(x)
            if isinstance(decl, list):
                declList.extend(decl if decl else [])
            else:
                declList.append(decl)
        return Program(declList)
        # declar: vardec | funcdec
    # def visitDeclar(self, ctx:MCParser.DeclarContext):
    #     return self.visitChildren(ctx)

        #vardec: vartypes varname (COMMA varname)*? SEMI
    def visitVardec(self, ctx:MCParser.VardecContext):
        vartype = self.visit(ctx.vartypes())
        idsName = [] 
        vardecl = []
        for x in ctx.varname():
            #idsName.append(self.visitVarname(x))
            varId = self.visit(x)
            if isinstance(varId, list):
                vardecl.append(VarDecl(varId[0], ArrayType(varId[1],vartype)))
            else:
                vardecl.append(VarDecl(varId, vartype))
        return vardecl

        #return [VarDecl(id, vartype) for id in idName]

        #vartype: PRIMI
    def visitVartypes(self, ctx:MCParser.VartypesContext):
        type = ctx.PRIMI().getText()
        if type == 'int':
            return IntType()
        elif type == 'float':
            return FloatType()
        elif type == 'boolean':
            return BoolType()
        elif type == 'string':
            return StringType()


    # varname: IDEN (LS INTLIT RS)?
    def visitVarname(self, ctx:MCParser.VarnameContext):
        if ctx.LS():
            return [Id(ctx.IDEN().getText()),int(ctx.INTLIT().getText())]

        else:
            return Id(ctx.IDEN().getText())
            #funcdec: functypes IDEN LB paralist? RB blockstate;
    def visitFuncdec(self, ctx:MCParser.FuncdecContext):
        name = Id(ctx.IDEN().getText())
        functype = self.visit(ctx.functypes())
        paraLs = self.visit(ctx.paralist()) if ctx.paralist() else []
        block = self.visit(ctx.blockstate())
        return FuncDecl(name,paraLs,functype,block)

        #functypes: PRIMI | VOIDTYPE | PRIMI LS RS
    def visitFunctypes(self, ctx:MCParser.FunctypesContext):
        if ctx.getChildCount() == 3:
            type = ctx.PRIMI().getText()
            if type == 'int':
                a = IntType()     
            elif type == 'float':
                a = FloatType()  
            elif type == 'string':
                a = StringType()    
            elif type == 'boolean' :
                a = BoolType()    
            return ArrayPointerType(a)
        elif ctx.VOIDTYPE():
            return VoidType()
        else:
            type = ctx.PRIMI().getText()
            if type == 'int':
                a = IntType()
                return a
            elif type == 'float':
                a = FloatType()
                return a
            elif type == 'string':
                a = StringType()
                return a
            elif type == 'boolean' :
                a = BoolType()
                return a

        #paralist:(funcpara (COMMA funcpara))*;
    def visitParalist(self, ctx:MCParser.ParalistContext):
        return [self.visit(x) for x in ctx.funcpara()]

    #funcpara: PRIMI IDEN (LS RS)?;
    def visitFuncpara(self, ctx:MCParser.FuncparaContext):
        type = ctx.PRIMI().getText()
        if type == 'int':
            a = IntType()
        elif type == 'float':
            a = FloatType()               
        elif type == 'string':
            a = StringType()
        else :
            a = BoolType()
        if ctx.getChildCount() == 4:
            return VarDecl(Id(ctx.IDEN().getText()), ArrayPointerType(a))
        else:
            return VarDecl(Id(ctx.IDEN().getText()), a)

    #blockstate:LP manydeclar* RP;
    def visitBlockstate(self, ctx:MCParser.BlockstateContext):
        """temp = []
        if ctx.manydeclar():
            for x in ctx.manydeclar():
                one = self.visit(x)
                
                temp.append(one)
        return Block(temp)"""
        return Block(flatten([self.visit(x) for x in ctx.manydeclar()]) if ctx.manydeclar() else [])
        
           # manydeclar :vardec | statement;
    def visitManydeclar(self, ctx:MCParser.ManydeclarContext):
        return self.visitChildren(ctx)

    #statement: if_statement | ...
    def visitStatement(self, ctx:MCParser.StatementContext):
        return self.visitChildren(ctx)
 #statement specification
#if_statement: If LB exp RB statement (Else statement)?;
    def visitIf_statement(self, ctx:MCParser.If_statementContext):
        expression = self.visit(ctx.exp())
        if_stmt = self.visit(ctx.statement(0))
        if ctx.statement(1):
            else_stmt = self.visit(ctx.statement(1))
            return If(expression, if_stmt, else_stmt)
        return If(expression, if_stmt)
        

    # do_while_statement: Do statement+ While exp  SEMI;
    def visitDo_while_statement(self, ctx:MCParser.Do_while_statementContext):
        list_stmt = [self.visit(x) for x in ctx.statement()]
        # for x in ctx.statement():
        #     temp_stmt = self.visit(x)
        #     list_stmt.append(temp_stmt)
        expression = self.visit(ctx.exp())
        return Dowhile(flatten([list_stmt]), expression)

        # for_statement: For LB exp SEMI exp SEMI exp RB statement;
    def visitFor_statement(self, ctx:MCParser.For_statementContext):
        return For(self.visit(ctx.exp(0)), self.visit(ctx.exp(1)), self.visit(ctx.exp(2)), self.visit(ctx.statement()))
        #break_statement: Break SEMI;
    def visitBreak_statement(self, ctx:MCParser.Break_statementContext):
        return Break()
        #continue_statement: Continue SEMI;
    def visitContinue_statement(self, ctx:MCParser.Continue_statementContext):
        return Continue()
        # return_statement: Return exp SEMI | Return SEMI;
    def visitReturn_statement(self, ctx:MCParser.Return_statementContext):
        if ctx.exp():
            return Return(self.visit(ctx.exp()))
        else:
            return Return()
        #exp_statement: exp SEMI;
    def visitExp_statement(self, ctx:MCParser.Exp_statementContext):
        return self.visit(ctx.exp())

        #exp: exp1 ASS exp | exp1;
    def visitExp(self, ctx:MCParser.ExpContext):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.ASS().getText(), self.visit(ctx.exp1()), self.visit(ctx.exp()))
        else:
            return self.visit(ctx.exp1())
        # exp1: exp1 LOGICALOR exp2 | exp2;
    def visitExp1(self, ctx:MCParser.Exp1Context):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.LOGICALOR().getText(), self.visit(ctx.exp1()), self.visit(ctx.exp2()))
        else:
            return self.visit(ctx.exp2())
        # exp2:  exp2 LOGICALAND exp3 | exp3;
    def visitExp2(self, ctx:MCParser.Exp2Context):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.LOGICALAND().getText(), self.visit(ctx.exp2()), self.visit(ctx.exp3()))
        else:
            return self.visit(ctx.exp3())
    #exp3: exp3: exp4 eq_and_not exp4 | exp4;
    def visitExp3(self, ctx:MCParser.Exp3Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp4(0))    
        else:
            return BinaryOp(self.visit(ctx.eq_and_not()), self.visit(ctx.exp4(0)), self.visit(ctx.exp4(1)))
             
    def visitEq_and_not(self, ctx:MCParser.Eq_and_notContext):
        if ctx.LOGICALEQ():
            return ctx.LOGICALEQ().getText()
        else:
            return ctx.NOTEQUAL().getText()
    
            # exp4: exp5 (LESSTHAN | LTOREQUAL | GREATER | GREATEREQ ) exp5 | exp5;
    def visitExp4(self, ctx:MCParser.Exp4Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp5(0))   
        else:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.exp5(0)), self.visit(ctx.exp5(1)))
            
            #exp5: exp5 (ADD | SUBTR) exp6 | exp6;
    def visitExp5(self, ctx:MCParser.Exp5Context):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.exp5()), self.visit(ctx.exp6()))
        else:
            return self.visit(ctx.exp6())
    #     #exp6: exp6 (DIVISION | MODUL | MULTI) exp7 | exp7;
    def visitExp6(self, ctx:MCParser.Exp6Context):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.exp6()), self.visit(ctx.exp7()))
        else:
            return self.visit(ctx.exp7())
            #exp7: (LOGICALNOT | SUBTR) exp7 | exp8;
    def visitExp7(self, ctx:MCParser.Exp7Context):
        if ctx.getChildCount() == 2:
            return UnaryOp(ctx.getChild(0).getText(), self.visit(ctx.exp7()))
        else:
            return self.visit(ctx.exp8())
    #         #exp8: exp9 LS exp9 RS | exp9;
    def visitExp8(self, ctx:MCParser.Exp8Context):
        if ctx.getChildCount() == 4:
            return ArrayCell(self.visit(ctx.exp9(0)), self.visit(ctx.exp9(1)))
        else:
            return self.visit(ctx.exp9(0))
    #         #exp9: LB exp RB | operands;
    def visitExp9(self, ctx:MCParser.Exp9Context):
        if ctx.getChildCount() == 3:
            return self.visit(ctx.exp())
        else:
            return self.visit(ctx.operands())

    #     #operands: literal | IDEN | call_func | operands postfix_array;
    def visitOperands(self, ctx:MCParser.OperandsContext):
        if ctx.getChildCount() == 1:
            if ctx.IDEN():
                return Id(ctx.IDEN().getText())
            elif ctx.call_func():
                return self.visit(ctx.call_func())
            elif ctx.literal():
                return self.visit(ctx.literal())
        else:
            return ArrayCell(self.visit(ctx.operands()), self.visit(ctx.postfix_array()))

    #literal: INTLIT | REAL | BOOLLIT | STRINGLIT;
    def visitLiteral(self, ctx:MCParser.LiteralContext):
        if ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.REAL():
            return FloatLiteral(float(ctx.REAL().getText()))
        elif ctx.BOOLLIT():
            if ctx.BOOLLIT().getText() == 'true':
                return BooleanLiteral(bool(True))
            else: 
                return BooleanLiteral(bool(False))
        else:
            return StringLiteral(str(ctx.STRINGLIT().getText()))


    #call_func: IDEN LB para_list? RB | builtin_get;
    def visitCall_func(self, ctx:MCParser.Call_funcContext):
    
        if ctx.para_list():
            return CallExpr(Id(ctx.IDEN().getText()), self.visit(ctx.para_list()))
        else:
            return CallExpr(Id(ctx.IDEN().getText()),[])
            #para_list: exp (COMMA exp)*;
    def visitPara_list(self, ctx:MCParser.Para_listContext):
        return flatten([self.visit(x) for x in ctx.exp()])
            #postfix_array: LS exp RS;
    def visitPostfix_array(self, ctx:MCParser.Postfix_arrayContext):
        return self.visit(ctx.exp())








