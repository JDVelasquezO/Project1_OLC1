import ply.lex as lex
import ply.yacc as yacc
from expressions import *
from instructions import *

reservadas = {
    'var': 'VAR',
    'print': 'PRINT',
    'while': 'WHILE',
    'main': 'MAIN',
    'if': 'IF',
    'else': 'ELSE',
    'switch': 'SWITCH',
    'break': 'BREAK',
    'case': 'CASE',
    'default': 'DEFAULT'
}

tokens = [
             'PTCOMA',
             'LLAVIZQ',
             'LLAVDER',
             'PARIZQ',
             'PARDER',
             'IGUAL',
             'INCREMENT',
             'DECREMENT',
             'MAS',
             'MENOS',
             'POR',
             'DIVIDIDO',
             'MOD',
             'ELEVADO',
             'MENQUE',
             'MAYQUE',
             'MAYIGUALQUE',
             'MENIGUALQUE',
             'IGUALQUE',
             'NIGUALQUE',
             'DECIMAL',
             'ENTERO',
             'CADENA',
             'TRUE',
             'FALSE',
             'CHAR',
             'ID',
             'OR',
             'AND',
             'NOT',
             'DOSPUNTOS'
         ] + list(reservadas.values())

# Tokens
t_PTCOMA = r';'
t_LLAVIZQ = r'{'
t_LLAVDER = r'}'
t_PARIZQ = r'\('
t_PARDER = r'\)'
t_IGUAL = r'='
t_INCREMENT = r'\+\+'
t_DECREMENT = r'--'
t_MAS = r'\+'
t_MENOS = r'-'
t_POR = r'\*'
t_ELEVADO = r'\*\*'
t_MOD = r'%'
t_DIVIDIDO = r'/'
t_MENQUE = r'<'
t_MAYQUE = r'>'
t_MAYIGUALQUE = r'>='
t_MENIGUALQUE = r'<='
t_IGUALQUE = r'=='
t_NIGUALQUE = r'=!'
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'
t_DOSPUNTOS = r':'


def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Float value too large %d", t.value)
        t.value = 0
    return t


def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value.lower(), 'ID')  # Check for reserved words
    return t


def t_CADENA(t):
    r'\"(\\"|.)*?\"'
    t.value = t.value[1:-1]  # remuevo las comillas

    t.value = t.value.replace('\\t', '\t')
    t.value = t.value.replace('\\n', '\n')
    t.value = t.value.replace('\\"', '\"')
    t.value = t.value.replace("\\'", "\'")
    t.value = t.value.replace('\\\\', '\\\\')

    return t


def t_CHAR(t):
    r'\'(\\\'|\\"|\t|\n|\\\\|.)\''
    t.value = t.value[1:-1]

    t.value = t.value.replace('\\t', '\t')
    t.value = t.value.replace('\\n', '\n')
    t.value = t.value.replace('\\"', '\"')
    t.value = t.value.replace("\\'", "\'")
    t.value = t.value.replace('\\\\', '\\\\')

    return t


# Comentario de múltiples líneas #* .. *#
def t_COMENTARIO_MULTILINEA(t):
    r'\#\*(.|\n)*?\*\#'
    t.lexer.lineno += t.value.count('\n')


# Comentario simple # ...
def t_COMENTARIO_SIMPLE(t):
    r'\#.*\n'
    t.lexer.lineno += 1


# Caracteres ignorados
t_ignore = " \t"


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Construyendo el analizador léxico
lexer = lex.lex()

# Asociación de operadores y precedencia


precedence = (
    ('left', 'OR', 'AND'),
    ('right', 'UNOT'),
    ('left', 'MENQUE', 'MAYQUE', 'MENIGUALQUE', 'MAYIGUALQUE', 'IGUALQUE', 'NIGUALQUE'),
    ('left', 'MAS', 'MENOS'),
    ('left', 'POR', 'DIVIDIDO', 'MOD'),
    ('left', 'ELEVADO'),
    ('right', 'UMENOS'),
    ('left', 'INCREMENT', 'DECREMENT'),
)


# Definición de la gramática
# ------------------------------ INICIO -----------------------------
def p_init(t):
    'init       : instrucciones'
    t[0] = t[1]


# ------------------------------ INSTRUCCIONES -----------------------------
def p_instrucciones_lista(t):
    'instrucciones    : instrucciones instruccion'
    t[1].append(t[2])
    t[0] = t[1]


def p_instrucciones_instruccion(t):
    '''instrucciones    : instruccion
                         | empty'''
    t[0] = [t[1]]


def p_instruccion(t):
    '''instruccion      : func_main
                        | imprimir_instr
                        | definicion_instr
                        | asignacion_instr
                        | def_asig_instr
                        | while_instr
                        | if_instr
                        | switch_instr
                        | expresion'''
    t[0] = t[1]


# ------------------------------ MAIN -----------------------------
def p_func_main(t):
    'func_main      : MAIN PARIZQ PARDER LLAVIZQ instrucciones LLAVDER'
    t[0] = Funcion_Main(t[5])


# ------------------------------ IMPRIMIR -----------------------------
def p_instruccion_imprimir(t):
    'imprimir_instr     : PRINT PARIZQ expresion PARDER def_instr_prima'
    t[0] = Imprimir(t[3])


# ------------------------------ DEFINIR Y ASIGNAR -----------------------------
def p_instruccion_definicion(t):
    'definicion_instr   : VAR ID def_instr_prima'
    t[0] = Definicion(t[2])


def p_asignacion_instr(t):
    'asignacion_instr   : ID IGUAL expresion def_instr_prima'
    t[0] = Asignacion(t[1], t[3])


def p_definicion_asignacion(t):
    'def_asig_instr     : VAR ID IGUAL expresion def_instr_prima'
    t[0] = Definicion_Asignacion(t[2], t[4])


# ------------------------------ IF -----------------------------
def p_if_instr(t):
    'if_instr           : IF PARIZQ expresion PARDER LLAVIZQ instrucciones LLAVDER'
    t[0] = If(t[3], t[6])


def p_if_else_instr(t):
    'if_instr      : IF PARIZQ expresion PARDER LLAVIZQ instrucciones LLAVDER ELSE LLAVIZQ instrucciones LLAVDER'
    t[0] = IfElse(t[3], t[6], t[10])


def p_else_if(t):
    'if_instr       : IF PARIZQ expresion PARDER LLAVIZQ instrucciones LLAVDER ELSE if_instr'
    t[0] = ElseIf(t[3], t[6], t[9])


# ------------------------------ WHILE -----------------------------
def p_while_instr(t):
    'while_instr     : WHILE PARIZQ expresion PARDER LLAVIZQ instrucciones LLAVDER'
    t[0] = While(t[3], t[6])


# ----------------------------- SWITCH y BREAK -----------------------------
def p_break_instr(t):
    'break_instr    : BREAK'
    t[0] = Break(t[1])


def p_switch(t):
    'switch_instr   : SWITCH PARIZQ expresion PARDER LLAVIZQ cases LLAVDER'
    t[0] = Switch(t[3], t[6], None)


def p_switch_default(t):
    'switch_instr   : SWITCH PARIZQ expresion PARDER LLAVIZQ default_instr LLAVDER'
    t[0] = Switch(t[3], None, t[6])


def p_switch_cases(t):
    'switch_instr   : SWITCH PARIZQ expresion PARDER LLAVIZQ cases default_instr LLAVDER'
    t[0] = Switch(t[3], t[6], t[7])


def p_cases(t):
    'cases      :   cases case_instr'
    if t[2] != "":
        t[1].append(t[2])
    t[0] = t[1]


def p_cases_recursive(t):
    'cases      : case_instr'
    if t[1] == "":
        t[0] = []
    else:
        t[0] = [t[1]]


def p_case(t):
    'case_instr     : CASE expresion DOSPUNTOS instrucciones'
    t[0] = Case(t[2], t[4])


def p_default(t):
    'default_instr    : DEFAULT DOSPUNTOS instrucciones'
    t[0] = Case(None, t[2])


# ------------------------------ EXPRESIONES -----------------------------
def p_increment(t):
    '''expresion        : expresion INCREMENT def_instr_prima
                        | expresion DECREMENT def_instr_prima '''
    if t[2] == "++":
        t[0] = ExpresionIncrement(t[1], OPERACION_ARITMETICA.INCREMENTO)
    elif t[2] == "--":
        t[0] = ExpresionIncrement(t[1], OPERACION_ARITMETICA.DISMINUCION)


def p_expresion_binaria(t):
    '''expresion        : expresion MAS expresion
                        | expresion MENOS expresion
                        | expresion POR expresion
                        | expresion DIVIDIDO expresion
                        | expresion ELEVADO expresion
                        | expresion MOD expresion
                        | expresion AND expresion
                        | expresion OR expresion
                        | expresion MAYQUE expresion
                        | expresion MENQUE expresion
                        | expresion MAYIGUALQUE expresion
                        | expresion MENIGUALQUE expresion
                        | expresion IGUALQUE expresion
                        | expresion NIGUALQUE expresion'''
    if t[2] == '+':
        t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.MAS)
    elif t[2] == '-':
        t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.MENOS)
    elif t[2] == '*':
        t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.POR)
    elif t[2] == '/':
        t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.DIVIDIDO)
    elif t[2] == '**':
        t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.POTENCIA)
    elif t[2] == '%':
        t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.MODULO)
    elif t[2] == '&&':
        t[0] = ExpresionOperacionLogica(t[1], t[3], OPERADOR_LOGICO.AND)
    elif t[2] == '||':
        t[0] = ExpresionOperacionLogica(t[1], t[3], OPERADOR_LOGICO.OR)
    elif t[2] == '>':
        t[0] = ExpresionLogica(t[1], t[3], OPERACION_LOGICA.MAYOR_QUE)
    elif t[2] == '<':
        t[0] = ExpresionLogica(t[1], t[3], OPERACION_LOGICA.MENOR_QUE)
    elif t[2] == '>=':
        t[0] = ExpresionLogica(t[1], t[3], OPERACION_LOGICA.MAYORIGUAL_QUE)
    elif t[2] == '<=':
        t[0] = ExpresionLogica(t[1], t[3], OPERACION_LOGICA.MENORIGUAL_QUE)
    elif t[2] == '==':
        t[0] = ExpresionLogica(t[1], t[3], OPERACION_LOGICA.IGUAL)
    elif t[2] == '=!':
        t[0] = ExpresionLogica(t[1], t[3], OPERACION_LOGICA.DIFERENTE)


def expresion_potencia(t):
    'expresion   : expresion ELEVADO A expresion'
    t[0] = ExpresionBinaria(t[1], t[4], OPERACION_ARITMETICA.POTENCIA)


def p_expresion_unaria(t):
    'expresion      : MENOS expresion %prec UMENOS'
    t[0] = ExpresionNegativo(t[2])


def p_expresion_negar(t):
    'expresion      : NOT expresion %prec UNOT'
    t[0] = ExpresionLogicaNot(t[2], OPERADOR_LOGICO.NOT)


def p_expresion_agrupacion(t):
    'expresion      : PARIZQ expresion PARDER'
    t[0] = t[2]


def p_expresionId(t):
    'expresion   : ID'
    t[0] = ExpresionIdentificador(t[1])


def p_expresion_number(t):
    '''expresion        : ENTERO
                        | DECIMAL'''
    t[0] = ExpresionNumero(t[1])


def p_expresion_cadena(t):
    'expresion     : CADENA'
    t[0] = ExpresionDobleComilla(t[1])


def p_expresion_char(t):
    'expresion   : CHAR'
    t[0] = ExpresionSimpleComilla(t[1])


def p_expresionBoolean(t):
    '''expresion          : TRUE
                          | FALSE'''
    t[0] = ExpresionBoolean(t[1])


def p_instrDef_prima(t):
    '''def_instr_prima   : PTCOMA
                        | empty'''
    t[0] = t[1]


def p_empty(t):
    'empty :'
    pass


def p_error(t):
    print(t)
    print("Error sintáctico en '%s'" % t.value)


parser = yacc.yacc()


def parse(input):
    return parser.parse(input)
