grammar Covid;

/* Parser Rules */

start		: PROGRAM ID SEMI var_block? func* main ;

var_block	: VAR (tipo ids_decl SEMI)+ ;
ids_decl	: ident_decl (COMMA ident_decl)* ;
ident_decl	: ID (SQUARE_L INT_CTE SQUARE_R)? (SQUARE_L INT_CTE SQUARE_R)? ;

ids			: ident (COMMA ident)* ;
ident		: ID ident_ind? ident_ind? ;
ident_ind	: SQUARE_L expr SQUARE_R ;

tipo 		: tipo_atom | DATAFRAME ;
tipo_atom	: INT | FLOAT | CHAR | STRING ;

func		: FUNC return_type ID PARENS_L params? PARENS_R SEMI var_block? block ;
return_type : tipo_atom | VOID ;
params		: tipo_atom ID param ;
param		: COMMA tipo_atom ID param | /* empty */ ;
block		: CURLY_L statement* CURLY_R ;

main 		: MAIN PARENS_L PARENS_R SEMI var_block? block ;

statement	: assignment | call SEMI | regresa | read | write | decision | while_loop | for_loop | covid SEMI ;

assignment	: ident ASGN expr SEMI ;

call		: ID PARENS_L args PARENS_R ;
args		: expr (COMMA expr)* | /* empty */ ;

regresa 	: RETURN PARENS_L expr PARENS_R SEMI ;

read 		: INPUT PARENS_L ids PARENS_R SEMI ;
write 		: PRINT PARENS_L impr PARENS_R SEMI ;
impr		: expr imprs ;
imprs		: COMMA expr imprs | /* empty */ ;

decision	: IF PARENS_L expr PARENS_R block else_block? ;
else_block	: ELSE block ;

while_loop 	: WHILE PARENS_L expr PARENS_R block ;
for_loop 	: FOR for_asgn TO expr block ;
for_asgn	: ID ASGN expr ;

expr		: and_term exprs ;
exprs		: OR and_term exprs | /* empty */ ;
and_term	: comp_term and_terms ;
and_terms	: AND comp_term and_terms | /* empty */ ;
comp_term	: rel_term comp_op rel_term | rel_term ;
comp_op		: EQ | NE ;
rel_term	: artm_term rel_op artm_term | artm_term ;
rel_op		: LT | GT | LTE | GTE ;
artm_term	: fact_term artm_terms ;
artm_terms	: (PLUS | MINUS) fact_term artm_terms | /* empty */ ;
fact_term	: operand fact_terms ;
fact_terms	: (MULT | DIVIDE) operand fact_terms | /* empty */ ;

operand		: NOT? PARENS_L expr PARENS_R | NOT? cte | NOT? ident | NOT? call | covid  ;

cte 		: INT_CTE | FLOAT_CTE | CHAR_CTE | STRING_CTE ;

covid 		: load_file | load_data | avg | moda | rango | variance | std_dev | maxi | mini | moment
			| plot | histogram | correl ;

load_file	: LOAD_FILE PARENS_L ident COMMA (ident | STRING_CTE) COMMA ident COMMA ident PARENS_R ;
load_data	: LOAD_DATA PARENS_L ident COMMA ident COMMA ident PARENS_R ;
avg 		: AVG PARENS_L ident COMMA ident PARENS_R ;
moda 		: MODE PARENS_L ident COMMA ident PARENS_R ;
rango 		: RANGE PARENS_L ident COMMA ident PARENS_R ;
variance 	: VARIANCE PARENS_L ident COMMA ident PARENS_R ;
std_dev 	: STD_DEV PARENS_L ident COMMA ident PARENS_R ;
maxi 		: MAX PARENS_L ident COMMA ident PARENS_R ;
mini 		: MIN PARENS_L ident COMMA ident PARENS_R ;
moment 		: MOMENT PARENS_L ident COMMA ident COMMA INT_CTE PARENS_R ;
plot 		: PLOT PARENS_L ident COMMA ident COMMA ident PARENS_R ;
histogram 	: HISTOGRAM PARENS_L ident COMMA ident COMMA INT_CTE PARENS_R ;
correl 		: CORREL PARENS_L ident COMMA ident COMMA ident PARENS_R ;

/* Lexer Rules */

fragment DIGIT : [0-9];
fragment ALPHA : [a-zA-Z];

PLUS				: '+' ;
MINUS				: '-' ;
MULT				: '*' ;
DIVIDE				: '/' ;
SEMI				: ';' ;
COLON				: ':' ;
COMMA				: ',' ;
CURLY_L				: '{' ;
CURLY_R				: '}' ;
PARENS_L			: '(' ;
PARENS_R			: ')' ;
SQUARE_L			: '[' ;
SQUARE_R			: ']' ;
EQ					: '==' ;
NE					: '!=' ;
NOT					: '!' ;
LTE					: '<=' ;
GTE					: '>=' ;
LT					: '<' ;
GT					: '>' ;
OR					: '||' ;
AND					: '&&' ;
ASGN				: '=' ;
PROGRAM				: 'program' ;
VAR					: 'var' ;
IF					: 'if' ;
WHILE				: 'while' ;
FOR					: 'for' ;
TO					: 'to' ;
ELSE				: 'else' ;
INT					: 'int' ;
FLOAT				: 'float' ;
CHAR				: 'char' ;
STRING				: 'string' ;
DATAFRAME			: 'dataframe' ;
VOID				: 'void' ;
FUNC				: 'func' ;
PRINT				: 'print' ;
MAIN				: 'main' ;
RETURN				: 'return' ;
INPUT				: 'input' ;
LOAD_FILE			: 'load_file' ;
LOAD_DATA			: 'load_data' ;
AVG					: 'avg' ;
MODE				: 'mode' ;
RANGE				: 'range' ;
VARIANCE			: 'variance' ;
STD_DEV				: 'std_dev' ;
MAX					: 'max' ;
MIN					: 'min' ;
MOMENT				: 'moment' ;
PLOT				: 'plot' ;
HISTOGRAM			: 'histogram' ;
CORREL				: 'correl' ;
WS					: [ \t\n]+ -> skip;
INT_CTE				: '-'? DIGIT+ ;
FLOAT_CTE			: '-'? DIGIT+ '.' DIGIT+ ;
STRING_CTE			: '"' .*? '"' ;
CHAR_CTE			: '\'' .? '\'' ;
ID					: ALPHA (ALPHA | DIGIT | '_')* ;
LINE_CMT			: '//' ~[\r\n]* -> skip ;
BLOCK_CMT			: '/*' .*? '*/' -> skip ;
