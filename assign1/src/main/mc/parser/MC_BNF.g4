grammar MC;

@lexer::header {
from lexererr import *
}

@lexer::member {
def emit(self):
tk = self.type
if tk == UNCLOSE_STRING:
result = super.emit();
raise UncloseString(result.text);
elif tk == ILLEGAL_ESCAPE:
result = super.emit();
raise IllegalEscape(result.text);
elif tk == ERROR_CHAR:
result = super.emit();
raise ErrorToken(result.text);
else:
return super.emit();
}

options{
language=Python3;
}

//program  : mctype 'main' LB RB LP body? RP EOF ;
program: declar+ EOF;

VOIDTYPE: 'void' ;
//INTTYPE: 'int' ;


declar: manydecl ;

manydecl: decl manydecl | decl;

decl: vardec | funcdec;

vardec: vartypes  manyvar  SEMI;

manyvar: varname manyvarp ;

manyvarp: (COMMA varname manyvarp)?;

vartypes: PRIMI ;

varname: IDEN (LS INTLIT RS)?;

funcdec: functypes IDEN LB manyfuncpara?  RB blockState;

manyfuncpara: funcpara manylp;

manylp: (COMMA funcpara manylp)?;

functypes: PRIMI | VOIDTYPE | arraypointer;

arraypointer: PRIMI LS RS;


funcpara: PRIMI IDEN (LS RS)?;

blockState: LP many_var_st RP;

many_var_st: one_var_st many_var_st | ;

one_var_st: vardec | statement;



statement: if_statement
|do_while_statement
|for_statement
|break_statement
|continue_statement
|return_statement
|exp_statement
|blockState
//|assign_statement
|builtinfunc
;



/*assign_statement: assign_body SEMI;

assign_body: assign_lhs ASS assign_tail;

assign_lhs: IDEN | index_exp;*/

index_exp: operands postfix_array;

postfix_array: LS exp RS;

//assign_tail: assign_lhs ASS assign_tail | exp;

exp: exp1 ASS exp | exp1;

exp1: exp1 LOGICALOR exp2 | exp2;

exp2:  exp2 LOGICALAND exp3 | exp3;

exp3: exp4 equal_and_not exp4 | exp4;

equal_and_not: LOGICALEQ | NOTEQUAL;

exp4: exp5 (LESSTHAN | LTOREQUAL | GREATER | GREATEREQ ) exp5 | exp5;

exp5: exp5 (ADD | SUBTR) exp6 | exp6;

exp6: exp6 (DIVISION | MODUL | MULTI) exp7 | exp7;

exp7: (LOGICALNOT | SUBTR) exp7 | exp8;

exp8: exp9 LS exp9 RS | exp9;

exp9: LB exp RB | operands;

operands: literal | IDEN | call_func | operands postfix_array;

literal: INTLIT | REAL | BOOLLIT | STRINGLIT;

call_func: IDEN LB para_list? RB | builtin_get;

para_list: exp (COMMA exp)*;

// statement specification
if_statement: If LB exp RB statement (Else statement)?;

do_while_statement: Do statement+ While exp  SEMI;

for_statement: For LB exp SEMI exp SEMI exp RB statement;

break_statement: Break SEMI;

continue_statement: Continue SEMI;

return_statement: Return exp SEMI  | Return SEMI;

exp_statement: exp SEMI;

builtin_get:  ('getInt' | 'getFloat') LB RB ;

builtin_put: 'put' typeput  LB exp RB;

typeput: ('Int' | 'Float' | 'String' | 'Bool');

builtin_putln: 'put' typeputln LB exp RB;

typeputln: ('IntLn' | 'FloatLn' | 'StringLn' | 'BoolLn');

builtin_nline: 'putLn' LB RB;

builtinfunc: builtin_get | builtin_put | builtin_putln | builtin_nline;



INTLIT: DIGIT+;

REAL: (REAL_DEC REAL_EXP?) | (DIGIT+ REAL_EXP);

BOOLLIT: 'true' | 'false';




BlockComment
:   '/*' .*? '*/'
-> skip
;

LineComment
:   '//' ~[\r\n]*
-> skip
;

// Operator
ADD: '+';
MULTI: '*';
LOGICALNOT: '!';
LOGICALOR: '||' ;
NOTEQUAL: '!=';
LESSTHAN: '<';
LTOREQUAL: '<=';
ASS: '=';
SUBTR: '-';
DIVISION: '/';
MODUL: '%';
LOGICALAND: '&&';
LOGICALEQ: '==';
GREATER: '>';
GREATEREQ: '>=';

//keyword
PRIMI: (INT | BOOLEAN | FLOAT | STRING);

If: 'if';

Else: 'else';

Do: 'do';

While: 'while';

For: 'for';

Break: 'break';

Continue: 'continue';

Return: 'return';

LB: '(' ;

RB: ')' ;

LP: '{';

RP: '}';

LS: '[';

RS: ']';

SEMI: ';' ;

COMMA: ',';



fragment DIGIT: [0-9];

fragment REAL_DEC: (DIGIT+ '.' DIGIT*) | (DIGIT* '.' DIGIT+);

fragment REAL_EXP: [Ee][-]?DIGIT+;

fragment DOUQUOTES: '"';

fragment STR_CHAR: ~[\b\t\n\f\r"'\\] | ESC_SEQ ;

fragment ESC_SEQ: '\\' [btnfr"'\\] ;

fragment ESC_ILLEGAL: '\\' ~[btnfr"'\\] | ~'\\' ;

fragment BOOLEAN: 'boolean';

fragment FLOAT: 'float';

fragment STRING: 'string';

fragment INT: 'int';

IDEN: ([a-zA-Z_])([a-zA-Z0-9]|'_')*;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines





STRINGLIT: '"' STR_CHAR* '"'
{
temp = self.text;
self.text = temp[1:-1]
};

UNCLOSE_STRING: '"' STR_CHAR* ( [\b\t\n\f\r\\] | EOF )
{
y = str(self.text)
p = ['\b', '\t', '\n', '\f', '\r', "'", '\\']
if y[-1] in p:
    raise UncloseString(y[1:-1])
else:
    raise UncloseString(y[1:])
}


;

ILLEGAL_ESCAPE: '"' STR_CHAR* ESC_ILLEGAL
{
y = str(self.text)
raise IllegalEscape(y[1:])
}
;

ERROR_CHAR: .
{
raise ErrorToken(self.text);
};




