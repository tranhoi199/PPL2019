# Generated from main/mc/parser/MC.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MCParser import MCParser
else:
    from MCParser import MCParser

# This class defines a complete generic visitor for a parse tree produced by MCParser.

class MCVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MCParser#program.
    def visitProgram(self, ctx:MCParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#declar.
    def visitDeclar(self, ctx:MCParser.DeclarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#vardec.
    def visitVardec(self, ctx:MCParser.VardecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#vartypes.
    def visitVartypes(self, ctx:MCParser.VartypesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#varname.
    def visitVarname(self, ctx:MCParser.VarnameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#funcdec.
    def visitFuncdec(self, ctx:MCParser.FuncdecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#functypes.
    def visitFunctypes(self, ctx:MCParser.FunctypesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#arraypointer.
    def visitArraypointer(self, ctx:MCParser.ArraypointerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#funcpara.
    def visitFuncpara(self, ctx:MCParser.FuncparaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#blockState.
    def visitBlockState(self, ctx:MCParser.BlockStateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#statement.
    def visitStatement(self, ctx:MCParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#index_exp.
    def visitIndex_exp(self, ctx:MCParser.Index_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#postfix_array.
    def visitPostfix_array(self, ctx:MCParser.Postfix_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp.
    def visitExp(self, ctx:MCParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp1.
    def visitExp1(self, ctx:MCParser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp2.
    def visitExp2(self, ctx:MCParser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp3.
    def visitExp3(self, ctx:MCParser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#equal_and_not.
    def visitEqual_and_not(self, ctx:MCParser.Equal_and_notContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp4.
    def visitExp4(self, ctx:MCParser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp5.
    def visitExp5(self, ctx:MCParser.Exp5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp6.
    def visitExp6(self, ctx:MCParser.Exp6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp7.
    def visitExp7(self, ctx:MCParser.Exp7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp8.
    def visitExp8(self, ctx:MCParser.Exp8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp9.
    def visitExp9(self, ctx:MCParser.Exp9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#operands.
    def visitOperands(self, ctx:MCParser.OperandsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#literal.
    def visitLiteral(self, ctx:MCParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#call_func.
    def visitCall_func(self, ctx:MCParser.Call_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#para_list.
    def visitPara_list(self, ctx:MCParser.Para_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#if_statement.
    def visitIf_statement(self, ctx:MCParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#do_while_statement.
    def visitDo_while_statement(self, ctx:MCParser.Do_while_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#for_statement.
    def visitFor_statement(self, ctx:MCParser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#break_statement.
    def visitBreak_statement(self, ctx:MCParser.Break_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#continue_statement.
    def visitContinue_statement(self, ctx:MCParser.Continue_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#return_statement.
    def visitReturn_statement(self, ctx:MCParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp_statement.
    def visitExp_statement(self, ctx:MCParser.Exp_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#builtin_get.
    def visitBuiltin_get(self, ctx:MCParser.Builtin_getContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#builtin_put.
    def visitBuiltin_put(self, ctx:MCParser.Builtin_putContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#typeput.
    def visitTypeput(self, ctx:MCParser.TypeputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#builtin_putln.
    def visitBuiltin_putln(self, ctx:MCParser.Builtin_putlnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#typeputln.
    def visitTypeputln(self, ctx:MCParser.TypeputlnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#builtin_nline.
    def visitBuiltin_nline(self, ctx:MCParser.Builtin_nlineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#builtinfunc.
    def visitBuiltinfunc(self, ctx:MCParser.BuiltinfuncContext):
        return self.visitChildren(ctx)



del MCParser