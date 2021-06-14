import ply.lex as lex
import ply.yacc as yacc
from expressions import *
from instructions import *

reservadas = {
    'var': 'VAR',
    'print': 'PRINT',
    'mientras': 'MIENTRAS',
    'main': 'MAIN',
    'if': 'IF',
    'else': 'ELSE'
}

tokens = [
             'PTCOMA',
             'LLAVIZQ',
             'LLAVDER',
             'PARIZQ',
             'PARDER',
             'IGUAL',
             'MAS',
             'MENOS',
             'POR',
             'DIVIDIDO',
             'MOD',
             'ELEVADO',
             'CONCAT',
             'MENQUE',
             'MAYQUE',
             'IGUALQUE',
             'NIGUALQUE',
             'DECIMAL',
             'ENTERO',
             'CADENA',
             'TRUE',
             'FALSE',
             'CHAR',
             'ID'
         ] + list(reservadas.values())

# Tokens
t_PTCOMA = r';'
t_LLAVIZQ = r'{'
t_LLAVDER = r'}'
t_PARIZQ = r'\('
t_PARDER = r'\)'
t_IGUAL = r'='
t_MAS = r'\+'
t_MENOS = r'-'
t_POR = r'\*'
t_ELEVADO = r'\*\*'
t_MOD = r'%'
t_DIVIDIDO = r'/'
# t_CONCAT = r'&'
t_MENQUE = r'<'
t_MAYQUE = r'>'
t_IGUALQUE = r'=='
t_NIGUALQUE = r'!='


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
    r'\".*?\"'
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
    ('left', 'CONCAT'),
    ('left', 'MAS', 'MENOS'),
    ('left', 'POR', 'DIVIDIDO', 'MOD'),
    ('left', 'ELEVADO'),
    ('right', 'UMENOS'),
)


# Definición de la gramática

def p_init(t):
    'init       : instrucciones'
    t[0] = t[1]


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
                        | mientras_instr
                        | if_instr
                        | if_else_instr'''
    t[0] = t[1]


# def p_beforeOfMain(t):
#     '''def_funcs_vars   : definicion_instr
#                         | asignacion_instr
#                         | empty'''
#     t[0] = t[1]


def p_func_main(t):
    'func_main  : MAIN PARIZQ PARDER LLAVIZQ instrucciones LLAVDER'
    t[0] = Funcion_Main(t[5])


def p_instruccion_imprimir(t):
    'imprimir_instr     : PRINT PARIZQ print_expresion_general PARDER def_instr_prima'
    t[0] = t[3]


def p_expresionGeneralImprimir(t):
    '''print_expresion_general  :  expresion_numerica
                                | expresion_cadena
                                | expresion_id
                                | expresion_boolean
                                | expresion_char'''
    t[0] = Imprimir(t[1])


def p_expresionId(t):
    'expresion_id   : ID'
    t[0] = ExpresionIdentificador(t[1])


def p_expresionBoolean(t):
    '''expresion_boolean  : TRUE
                          | FALSE'''

    t[0] = ExpresionBoolean(t[1])


def p_instruccion_definicion(t):
    'definicion_instr   : VAR ID def_instr_prima'
    t[0] = Definicion(t[2])


def p_instrDef_prima(t):
    '''def_instr_prima   : PTCOMA
                        | empty'''
    t[0] = t[1]


def p_empty(t):
    'empty :'
    pass


def p_asignacion_instr(t):
    'asignacion_instr   : ID IGUAL asign_expresion_general def_instr_prima'
    t[0] = Asignacion(t[1], t[3])


def p_expresionGeneralAsignar(t):
    '''asign_expresion_general  :  expresion_numerica
                            | expresion_cadena
                            | expresion_id
                            | expresion_boolean
                            | expresion_char'''
    t[0] = t[1]


def p_definicion_asignacion(t):
    'def_asig_instr     : VAR ID IGUAL asign_def_expresion_general def_instr_prima'
    t[0] = Definicion_Asignacion(t[2], t[4])


def p_expresionGeneralDefAsign(t):
    '''asign_def_expresion_general  :  expresion_numerica
                                    | expresion_cadena
                                    | expresion_id
                                    | expresion_boolean
                                    | expresion_char'''
    t[0] = t[1]


def p_mientras_instr(t):
    'mientras_instr     : MIENTRAS PARIZQ expresion_logica PARDER LLAVIZQ instrucciones LLAVDER'
    t[0] = Mientras(t[3], t[6])


def p_if_instr(t):
    'if_instr           : IF PARIZQ expresion_logica PARDER LLAVIZQ instrucciones LLAVDER'
    t[0] = If(t[3], t[6])


def p_if_else_instr(t):
    'if_else_instr      : IF PARIZQ expresion_logica PARDER LLAVIZQ instrucciones LLAVDER ELSE LLAVIZQ instrucciones LLAVDER'
    t[0] = IfElse(t[3], t[6], t[10])


def p_expresion_binaria(t):
    '''expresion_numerica : expresion_numerica MAS expresion_numerica
                        | expresion_numerica MENOS expresion_numerica
                        | expresion_numerica POR expresion_numerica
                        | expresion_numerica DIVIDIDO expresion_numerica
                        | expresion_numerica ELEVADO expresion_numerica
                        | expresion_numerica MOD expresion_numerica
                        | expresion_numerica MAS expresion_char
                        | expresion_cadena MAS expresion_cadena
                        | expresion_cadena MAS expresion_numerica
                        | expresion_cadena MAS expresion_char
                        | expresion_numerica MAS expresion_cadena
                        | expresion_char MAS expresion_char
                        | expresion_char MAS expresion_cadena
                        | expresion_char MAS expresion_numerica'''
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


def expresion_potencia(t):
    '''expresion_potencia   : expresion_numerica ELEVADO A expresion_numerica'''
    t[0] = ExpresionBinaria(t[1], t[4], OPERACION_ARITMETICA.POTENCIA)


def p_expresion_unaria(t):
    'expresion_numerica : MENOS expresion_numerica %prec UMENOS'
    t[0] = ExpresionNegativo(t[2])


def p_expresion_agrupacion(t):
    'expresion_numerica : PARIZQ expresion_numerica PARDER'
    t[0] = t[2]


def p_expresion_number(t):
    '''expresion_numerica : ENTERO
                        | DECIMAL'''
    t[0] = ExpresionNumero(t[1])


def p_expresion_id(t):
    'expresion_numerica   : ID'
    t[0] = ExpresionIdentificador(t[1])


def p_expresion_char(t):
    'expresion_char   : CHAR'
    t[0] = ExpresionSimpleComilla(t[1])


# def p_expresion_concatenacion(t):
#     '''expresion_cadena     : expresion_cadena MAS expresion_cadena
#                             | expresion_cadena MAS expresion_numerica
#                             | expresion_cadena MAS expresion_char
#                             | expresion_cadena MAS expresion_id
#                             | expresion_numerica MAS expresion_cadena
#                             | expresion_char MAS expresion_cadena
#                             | expresion_id MAS expresion_cadena'''
#     t[0] = ExpresionConcatenar(t[1], t[3])


def p_expresion_cadena(t):
    'expresion_cadena     : CADENA'
    t[0] = ExpresionDobleComilla(t[1])


def p_expresion_cadena_numerico(t):
    'expresion_cadena     : expresion_numerica'
    t[0] = ExpresionCadenaNumerico(t[1])


def p_expresion_logica(t):
    '''expresion_logica : expresion_numerica MAYQUE expresion_numerica
                        | expresion_numerica MENQUE expresion_numerica
                        | expresion_numerica IGUALQUE expresion_numerica
                        | expresion_numerica NIGUALQUE expresion_numerica'''
    if t[2] == '>':
        t[0] = ExpresionLogica(t[1], t[3], OPERACION_LOGICA.MAYOR_QUE)
    elif t[2] == '<':
        t[0] = ExpresionLogica(t[1], t[3], OPERACION_LOGICA.MENOR_QUE)
    elif t[2] == '==':
        t[0] = ExpresionLogica(t[1], t[3], OPERACION_LOGICA.IGUAL)
    elif t[2] == '!=':
        t[0] = ExpresionLogica(t[1], t[3], OPERACION_LOGICA.DIFERENTE)


def p_error(t):
    print(t)
    print("Error sintáctico en '%s'" % t.value)


parser = yacc.yacc()


def parse(input):
    return parser.parse(input)
