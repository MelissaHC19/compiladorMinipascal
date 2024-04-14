'''ANALIZADOR LEXICO PARA MINIPASCAL'''
import ply.lex as lex
import sys

# lista de tokens
tokens = (
    # Reserverd words
    'ABSOLUTE',
    'AND',
    'ARRAY',
    'ASM',
    'BEGIN',
    'CASE',
    'CONST',
    'CONSTRUCTOR',
    'DESTRUCTOR',
    'DIV',
    'DO',
    'DOWNTO',
    'ELSE',
    'END',
    'FILE',
    'FOR',
    'FUNCTION',
    'GOTO',
    'IF',
    'IMPLEMENTATION',
    'IN',
    'INHERITED',
    'INLINE',
    'INTERFACE',
    'LABEL',
    'MOD',
    'NIL',
    'NOT',
    'OBJECT',
    'OF',
    'OPERATOR',
    'OR',
    'PACKED',
    'PROCEDURE',
    'PROGRAM',
    'RECORD',
    'REINTRODUCE',
    'REPEAT',
    'SELF',
    'SET',
    'SHL',
    'SHR',
    'STRING',
    'THEN',
    'TO',
    'TYPE',
    'UNIT',
    'UNTIL',
    'USES',
    'VAR',
    'WHILE',
    'WITH',
    'XOR',
    'FORWARD',
	'LETTER',
	'DIGIT',

    # Symbols
    'SQUOTE',
	'QUOTE',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'EQUAL',
    'NOTEQUAL',
    'LESS',
    'GREATER',
    'LESSEQUAL',
    'GREATEREQUAL',
    'LBRACKET',
    'RBRACKET',
    'DOT',
    'COMMA',
    'LPAREN',
    'RPAREN',
    'COLON',
    'SEMICOLON',
    'UPARROW',
    'AT',
    'LBLOCK',
    'RBLOCK',
    'BUCKS',
    'HASHTAG',
    'AMPERSANT',
    'PERCENT',
    'ASSIGN',
    'PLUSEQUAL',
    'MINUSEQUAL',
    'TIMESEQUAL',
    'DIVIDEEQUAL',

    # Others
    'ID',
    'NUMBER',
	'ANY_CHARACTER_EXCEPT_QUOTE',
	'RANGE_OPERATOR',
)

# Regular expressions rules for a simple tokens
def t_comments(t):
    r'\(\*(.|\n)*?\*\)|{(.|\n)*?}'
    t.lexer.lineno += t.value.count('\n')

def t_comments_C99(t):
    r'//((.)*)?(\n)?'
    t.lexer.lineno += 1

t_ignore = ' \t'

t_SQUOTE = r'\''
t_QUOTE = r'\"'
t_PLUS   = r'\+'
t_MINUS  = r'-'
t_TIMES  = r'\*'
t_DIVIDE = r'\/'
t_EQUAL = r'='
t_NOTEQUAL = r'<>'
t_LESS   = r'<'
t_GREATER = r'>'
t_LESSEQUAL = r'<='
t_GREATEREQUAL = r'>='
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_DOT = r'\.'
t_COMMA  = r','
t_LPAREN = r'\('
t_RPAREN  = r'\)'
t_COLON   = r':'
t_SEMICOLON = ';'
t_UPARROW = r'\^'
t_AT= r'@'
t_LBLOCK = r'{'
t_RBLOCK = r'}'
t_BUCKS = r'\$'
t_HASHTAG = r'\#'
t_AMPERSANT = r'\&'
t_PERCENT= r'%'
t_ASSIGN = r':='
t_PLUSEQUAL = r'\+='
t_MINUSEQUAL = r'-='
t_TIMESEQUAL = r'\*='
t_DIVIDEEQUAL = r'\/='
#t_ANY_CHARACTER_EXCEPT_QUOTE = r'[^"]'
t_RANGE_OPERATOR = r'\.\.'

def t_ABSOLUTE(t):
	r'ABSOLUTE'
	return t

def t_AND(t):
	r'AND'
	return t

def t_ARRAY(t):
	r'ARRAY'
	return t

def t_ASM(t):
	r'ASM'
	return t

def t_BEGIN(t):
	r'BEGIN'
	return t

def t_CASE(t):
	r'CASE'
	return t

def t_CONST(t):
	r'CONST'
	return t

def t_CONSTRUCTOR(t):
	r'CONSTRUCTOR'
	return t

def t_DESTRUCTOR(t):
	r'DESTRUCTOR'
	return t

def t_DIV(t):
	r'DIV'
	return t

def t_DO(t):
	r'DO'
	return t

def t_DOWNTO(t):
	r'DOWNTO'
	return t

def t_ELSE(t):
	r'ELSE'
	return t

def t_END(t):
	r'END'
	return t

def t_FILE(t):
	r'FILE'
	return t

def t_FOR(t):
	r'FOR'
	return t

def t_FUNCTION(t):
	r'FUNCTION'
	return t

def t_GOTO(t):
	r'GOTO'
	return t

def t_IF(t):
	r'IF'
	return t

def t_IMPLEMENTATION(t):
	r'IMPLEMENTATION'
	return t

def t_IN(t):
	r'IN'
	return t

def t_INHERITED(t):
	r'INHERITED'
	return t

def t_INLINE(t):
	r'INLINE'
	return t

def t_INTERFACE(t):
	r'INTERFACE'
	return t

def t_LABEL(t):
	r'LABEL'
	return t

def t_MOD(t):
	r'MOD'
	return t

def t_NIL(t):
	r'NIL'
	return t

def t_NOT(t):
	r'NOT'
	return t

def t_OBJECT(t):
	r'OBJECT'
	return t

def t_OF(t):
	r'OF'
	return t

def t_OPERATOR(t):
	r'OPERATOR'
	return t

def t_OR(t):
	r'OR'
	return t

def t_PACKED(t):
    r'PACKED'
    return t

def t_PROCEDURE(t):
    r'PROCEDURE'
    return t

def t_PROGRAM(t):
    r'PROGRAM'
    return t

def t_RECORD(t):
    r'RECORD'
    return t

def t_REINTRODUCE(t):
    r'REINTRODUCE'
    return t

def t_REPEAT(t):
    r'REPEAT'
    return t

def t_SELF(t):
    r'SELF'
    return t

def t_SET(t):
    r'SET'
    return t

def t_SHL(t):
    r'SHL'
    return t

def t_SHR(t):
    r'SHR'
    return t

def t_STRING(t):
    r'STRING'
    return t

def t_THEN(t):
    r'THEN'
    return t

def t_TO(t):
    r'TO'
    return t

def t_TYPE(t):
    r'TYPE'
    return t

def t_UNIT(t):
    r'UNIT'
    return t

def t_UNTIL(t):
    r'UNTIL'
    return t

def t_USES(t):
    r'USES'
    return t

def t_VAR(t):
    r'VAR'
    return t

def t_WHILE(t):
    r'WHILE'
    return t

def t_WITH(t):
    r'WITH'
    return t

def t_XOR(t):
    r'XOR'
    return t

def t_FORWARD(t):
	r'FORWARD'
	return t

def t_ErrorCadena(t):
	r'\d+(\.\d+)?[a-zA-Z]+'
	print ("Lexical error: " + str(t.value))
	t.lexer.skip(1)

def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t

def t_ID(t):
    r'\w+(_\d\w)?'
    return t

def t_LETTER(t):
    r'\w'
    return t

def t_DIGIT(t):
    r'\d'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print ("Lexical error: " + str(t.value[0]))
    t.lexer.skip(1)
    
def test(data, lexer):
	lexer.input(data)
	while True:
		tok = lexer.token()
		if not tok:
			break
		print (tok)

lexer = lex.lex()

if __name__ == '__main__':
	if (len(sys.argv) > 1):
		fin = sys.argv[1]
	else:
		fin = 'prueba.txt'
	f = open(fin, 'r')
	data = f.read()
	print (data)
	lexer.input(data)
	test(data, lexer)