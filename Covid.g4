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

PLUS				: '+' ;
MINUS				: '-' ;
MULTIPLY			: '*' ;
DIVIDE				: '/' ;
SEMI_COLON			: ';' ;
COLON				: ':' ;
COMMA				: ',' ;
OPEN_CURY_BRACE		: '{' ;
CLOSE_CURLY_BRACE	: '}' ;
OPEN_PARENS			: '(' ;
CLOSE_PARENS		: ')' ;
DIFFERENT			: '<>' ;
LESSER				: '<' ;
GREATER				: '>' ;
EQUALS				: '=' ;
PROGRAM				: 'program' ;
VAR					: 'var' ;
IF					: 'if' ;
ELSE				: 'else' ;
INT					: 'int' ;
FLOAT				: 'float' ;
PRINT				: 'print' ;
WS					: [ \t\n]+ -> skip;
INT_CTE				: [+-]?[0-9]+ ;
FLOAT_CTE			: [+-]?[0-9]+ '.'[0-9]+ ;
STRING_CTE			: '"' (~'"')* '"' ;
ID					: [A-Za-z][A-Za-z0-9_]*;