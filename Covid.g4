grammar Covid;

/* Parser Rules */

programa	: PROGRAM ID SEMI_COLON variables? bloque ;
variables	: VAR varloop;
varloop		: (idloop COLON tipo SEMI_COLON)+;
idloop		: ID (COMMA idloop)?;
tipo		: INT | FLOAT;
bloque		: OPEN_CURY_BRACE estatuto* CLOSE_CURLY_BRACE;
estatuto	: (asignacion | condicion | escritura) ;
asignacion	: ID EQUALS expression SEMI_COLON ;
condicion	: IF OPEN_PARENS expression CLOSE_PARENS bloque (ELSE bloque)? SEMI_COLON ;
escritura	: PRINT OPEN_PARENS prints CLOSE_PARENS SEMI_COLON ;
prints		: expression | STRING_CTE | expression COMMA prints | STRING_CTE COMMA prints ;
expression	: exp ((GREATER | LESSER | DIFFERENT) exp)? ;
exp 		: termino ((PLUS | MINUS) termino)* ;
termino		: factor ((MULTIPLY | DIVIDE) factor)* ;
factor		: OPEN_PARENS expression CLOSE_PARENS
			| (PLUS | MINUS)? var_cte;
var_cte		: (ID | INT_CTE | FLOAT_CTE) ;

/* Lexer Rules */

fragment DIGIT : [0-9];
fragment ALPHA : [a-zA-Z];

PLUS				: '+' ;
MINUS				: '-' ;
MULTIPLY			: '*' ;
DIVIDE				: '/' ;
SEMI_COLON			: ';' ;
COLON				: ':' ;
COMMA				: ',' ;
CURLYB_L			: '{' ;
CURLYB_R			: '}' ;
PARENS_L			: '(' ;
PARENS_R			: ')' ;
SQUAREB_L			: '[' ;
SQUAREB_R			: ']' ;
LT					: '<' ;
GT					: '>' ;
ASGN				: '=' ;
EQ					: '==' ;
DIFFERENT			: '!=' ;
LTE					: '<=' ;
GTE					: '>=' ;
OR					: '||' ;
AND					: '&&' ;
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
LOADFILE			: 'loadFile' ;
LOADDATA			: 'loadData' ;
AVG					: 'avg' ;
MODE				: 'mode' ;
RANGE				: 'range' ;
VARIANCE			: 'variance' ;
STD					: 'std' ;
MOMENT				: 'moment' ;
PLOT				: 'plot' ;
HISTOGRAM			: 'histogram' ;
CORREL				: 'correl' ;
WS					: [ \t\n]+ -> skip;
INT_CTE				: [+-]? DIGIT+ ;
FLOAT_CTE			: [+-]? DIGIT+ '.' DIGIT+ ;
STRING_CTE			: '"' (~'"')* '"' ;
CHAR_CTE			: '\'' (~'\'') '\'' ;
ID					: ALPHA (ALPHA | DIGIT | '_')* ;
