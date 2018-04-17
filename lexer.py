import ply.lex as lex

tokens = ['FINSI','FINPARA','ENTONCES','FOR','IF','DO']+[ 'NAME','SALTO','NUMBER','PLUS','MINUS','TIMES','DIVIDE', 'EQUALS','LPAREN','RPAREN','MAYOR','MENOR','MAYORIGUAL','MENORIGUAL','DIFERENTE' ]


t_ignore = ' \t'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUALS = r'\='
t_MAYOR=r'>'
t_MAYORIGUAL=r'>='
t_MENOR=r'<'
t_MENORIGUAL=r'<='
t_DIFERENTE=r'!='
t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_SALTO=r'\n '
t_LPAREN =r'\('
t_RPAREN =r'\)'


def t_FOR(t):
    r'Para'
    return t
def t_DO(t):
    r'Hacer'
    return t
def t_IF(t):
    r'Si'
    return t
def t_ENTONCES(t):
    r'Entonces'
    
    return t
def t_FINSI(t):
    r'FinSi'
    return t
def t_FINPARA(t):
    r'FinPara'
    return t
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Error handling rule

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

if __name__ == "__main__":
    lex.lex() # Build the lexer
    archivo = open("Expresiones2.txt", "r")

    lex.input(archivo.read())
    while True:
        tok = lex.token()
        if not tok: break
        print str(tok.value) + " - " + str(tok.type)
