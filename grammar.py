import ply.lex as lex
import ply.yacc as yacc
from Exception import Excepcion
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
    'continue': 'CONTINUE',
    'case': 'CASE',
    'default': 'DEFAULT',
    'true': 'TRUE',
    'false': 'FALSE',
    'for': 'FOR',
    'null': 'NULL',
    'int': 'INT',
    'double': 'DOUBLE',
    'string': 'STRING',
    'char': 'CHAR',
    'boolean': 'BOOLEAN',
    'func': 'FUNC',
    'return': 'RETURN',
    'read': 'READ'
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
             'CHARACTER',
             'ID',
             'OR',
             'AND',
             'NOT',
             'DOSPUNTOS',
             'COMA'
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
t_COMA = r','


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


def t_CHARACTER(t):
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
    err = Excepcion("Error lexico en ", f"{t.value[0]}", t.lexer.lineno, find_column(t.lexer.lexdata, t))
    errores.append(err)
    print("Caracter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)


def find_column(inp, token):
    line_start = inp.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1


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
                        | funct_instr
                        | call_instr
                        | return_instr
                        | imprimir_instr
                        | definicion_instr
                        | asignacion_instr
                        | def_asig_instr
                        | while_instr
                        | if_instr
                        | switch_instr
                        | for_instr
                        | expresion
                        | break_instr
                        | continue_instr'''
    t[0] = t[1]


def p_instrDef_prima(t):
    '''def_instr_prima   : PTCOMA
                        | empty'''
    t[0] = t[1]


def p_empty(t):
    'empty :'
    pass


# ------------------------------ MAIN -----------------------------
def p_func_main(t):
    'func_main      : MAIN PARIZQ PARDER LLAVIZQ instrucciones LLAVDER'
    t[0] = Funcion_Main(t[5], t.lineno(1), find_column(entrada, t.slice[1]))


# ------------------------------ IMPRIMIR -----------------------------
def p_instruccion_imprimir(t):
    'imprimir_instr     : PRINT PARIZQ expresion PARDER def_instr_prima'
    t[0] = Imprimir(t[3], t.lineno(1), find_column(entrada, t.slice[1]))


def p_function_imprimir(t):
    'imprimir_instr     : PRINT PARIZQ call_instr PARDER def_instr_prima'
    t[0] = Imprimir(t[3], t.lineno(1), find_column(entrada, t.slice[1]))


# ------------------------------ DEFINIR Y ASIGNAR -----------------------------
def p_instruccion_definicion(t):
    'definicion_instr   : VAR ID def_instr_prima'
    t[0] = Definicion(t[2], t.lineno(2), find_column(entrada, t.slice[2]))


def p_asignacion_instr(t):
    'asignacion_instr   : ID IGUAL expresion def_instr_prima'
    t[0] = Asignacion(t[1], t[3], t.lineno(1), find_column(entrada, t.slice[1]))


def p_definicion_asignacion(t):
    'def_asig_instr     : VAR ID IGUAL expresion def_instr_prima'
    t[0] = Definicion_Asignacion(t[2], t[4], t.lineno(2), find_column(entrada, t.slice[2]))


def p_definicion_asignacion_func(t):
    'def_asig_instr     : VAR ID IGUAL call_instr def_instr_prima'
    t[0] = Definicion_Asignacion(t[2], t[4], t.lineno(2), find_column(entrada, t.slice[2]))


# ------------------------------ IF -----------------------------
def p_if_instr(t):
    'if_instr           : IF PARIZQ expresion PARDER LLAVIZQ instrucciones LLAVDER'
    t[0] = If(t[3], t[6], t.lineno(1), find_column(entrada, t.slice[1]))


def p_if_else_instr(t):
    'if_instr      : IF PARIZQ expresion PARDER LLAVIZQ instrucciones LLAVDER ELSE LLAVIZQ instrucciones LLAVDER'
    t[0] = IfElse(t[3], t[6], t[10], t.lineno(1), find_column(entrada, t.slice[1]))


def p_else_if(t):
    'if_instr       : IF PARIZQ expresion PARDER LLAVIZQ instrucciones LLAVDER ELSE if_instr'
    t[0] = ElseIf(t[3], t[6], t[9], t.lineno(1), find_column(entrada, t.slice[1]))


# ------------------------------ WHILE -----------------------------
def p_while_instr(t):
    'while_instr     : WHILE PARIZQ expresion PARDER LLAVIZQ instrucciones LLAVDER'
    t[0] = While(t[3], t[6], t.lineno(1), find_column(entrada, t.slice[1]))


# -------------------------------- CONTINUE ---------------------------
def p_continue_instr(t):
    'continue_instr     : CONTINUE def_instr_prima'
    t[0] = Continue(t.lineno(1), find_column(entrada, t.slice[1]))


# ----------------------------- SWITCH y BREAK -----------------------------
def p_break_instr(t):
    '''break_instr    : BREAK def_instr_prima'''
    t[0] = Break(t.lineno(1), find_column(entrada, t.slice[1]))


def p_switch(t):
    'switch_instr   : SWITCH PARIZQ expresion PARDER LLAVIZQ cases LLAVDER'
    t[0] = Switch(t[3], t[6], None, t.lineno(1), find_column(entrada, t.slice[1]))


def p_switch_default(t):
    'switch_instr   : SWITCH PARIZQ expresion PARDER LLAVIZQ default_instr LLAVDER'
    t[0] = Switch(t[3], None, t[6], t.lineno(1), find_column(entrada, t.slice[1]))


def p_switch_cases(t):
    'switch_instr   : SWITCH PARIZQ expresion PARDER LLAVIZQ cases default_instr LLAVDER'
    t[0] = Switch(t[3], t[6], t[7], t.lineno(1), find_column(entrada, t.slice[1]))


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
    'case_instr     : CASE expresion DOSPUNTOS instrucciones def_instr_prima'
    t[0] = Case(t[2], t[4], t[5], t.lineno(1), find_column(entrada, t.slice[1]))


def p_default(t):
    'default_instr    : DEFAULT DOSPUNTOS instrucciones def_instr_prima'
    t[0] = Case(None, t[3], t[4], t.lineno(1), find_column(entrada, t.slice[1]))


# ------------------------------ FOR -----------------------------
def p_for(t):
    'for_instr : FOR PARIZQ expresion def_instr_prima expresion def_instr_prima expresion PARDER LLAVIZQ instrucciones LLAVDER'
    t[0] = For(t[3], t[5], t[7], t[10], t.lineno(1), find_column(entrada, t.slice[1]))


# ------------------------------ EXPRESIONES -----------------------------
def p_expresion_asignacion(t):
    'expresion :    asignacion_instr'
    t[0] = t[1]


def p_expresion_declaracion_asignacion(t):
    'expresion :    def_asig_instr'
    t[0] = t[1]


def p_null(t):
    '''expresion    : NULL'''
    t[0] = ExpresionNull(t[1], t.lineno(1), find_column(entrada, t.slice[1]))


def p_increment(t):
    '''expresion        : expresion INCREMENT def_instr_prima
                        | expresion DECREMENT def_instr_prima '''
    if t[2] == "++":
        t[0] = ExpresionIncrement(t[1], OPERACION_ARITMETICA.INCREMENTO, t.lineno(2), find_column(entrada, t.slice[2]))
    elif t[2] == "--":
        t[0] = ExpresionIncrement(t[1], OPERACION_ARITMETICA.DISMINUCION, t.lineno(2), find_column(entrada, t.slice[2]))


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
        t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.MAS, t.lineno(2),
                                find_column(entrada, t.slice[2]))
    elif t[2] == '-':
        t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.MENOS, t.lineno(2),
                                find_column(entrada, t.slice[2]))
    elif t[2] == '*':
        t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.POR, t.lineno(2),
                                find_column(entrada, t.slice[2]))
    elif t[2] == '/':
        t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.DIVIDIDO, t.lineno(2),
                                find_column(entrada, t.slice[2]))
    elif t[2] == '**':
        t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.POTENCIA, t.lineno(2),
                                find_column(entrada, t.slice[2]))
    elif t[2] == '%':
        t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.MODULO, t.lineno(2),
                                find_column(entrada, t.slice[2]))
    elif t[2] == '&&':
        t[0] = ExpresionOperacionLogica(t[1], t[3], OPERADOR_LOGICO.AND, t.lineno(2),
                                        find_column(entrada, t.slice[2]))
    elif t[2] == '||':
        t[0] = ExpresionOperacionLogica(t[1], t[3], OPERADOR_LOGICO.OR, t.lineno(2),
                                        find_column(entrada, t.slice[2]))
    elif t[2] == '>':
        t[0] = ExpresionLogica(t[1], t[3], OPERACION_LOGICA.MAYOR_QUE, t.lineno(2),
                               find_column(entrada, t.slice[2]))
    elif t[2] == '<':
        t[0] = ExpresionLogica(t[1], t[3], OPERACION_LOGICA.MENOR_QUE, t.lineno(2),
                               find_column(entrada, t.slice[2]))
    elif t[2] == '>=':
        t[0] = ExpresionLogica(t[1], t[3], OPERACION_LOGICA.MAYORIGUAL_QUE, t.lineno(2),
                               find_column(entrada, t.slice[2]))
    elif t[2] == '<=':
        t[0] = ExpresionLogica(t[1], t[3], OPERACION_LOGICA.MENORIGUAL_QUE, t.lineno(2),
                               find_column(entrada, t.slice[2]))
    elif t[2] == '==':
        t[0] = ExpresionLogica(t[1], t[3], OPERACION_LOGICA.IGUAL, t.lineno(2),
                               find_column(entrada, t.slice[2]))
    elif t[2] == '=!':
        t[0] = ExpresionLogica(t[1], t[3], OPERACION_LOGICA.DIFERENTE, t.lineno(2),
                               find_column(entrada, t.slice[2]))


def expresion_potencia(t):
    'expresion   : expresion ELEVADO A expresion'
    t[0] = ExpresionBinaria(t[1], t[4], OPERACION_ARITMETICA.POTENCIA, t.lineno(2),
                            find_column(entrada, t.slice[2]))


def p_expresion_unaria(t):
    'expresion      : MENOS expresion %prec UMENOS'
    t[0] = ExpresionNegativo(t[2], t.lineno(1), find_column(entrada, t.slice[1]))


def p_expresion_negar(t):
    'expresion      : NOT expresion %prec UNOT'
    t[0] = ExpresionLogicaNot(t[2], OPERADOR_LOGICO.NOT, t.lineno(1), find_column(entrada, t.slice[1]))


def p_expresion_agrupacion(t):
    'expresion      : PARIZQ expresion PARDER'
    t[0] = t[2]


def p_expresionId(t):
    'expresion   : ID'
    t[0] = ExpresionIdentificador(t[1], t.lineno(1), find_column(entrada, t.slice[1]))


def p_expresion_number(t):
    '''expresion        : ENTERO
                        | DECIMAL'''
    t[0] = ExpresionNumero(t[1], t.lineno(1), find_column(entrada, t.slice[1]))


def p_expresion_cadena(t):
    'expresion     : CADENA'
    t[0] = ExpresionDobleComilla(t[1], t.lineno(1), find_column(entrada, t.slice[1]))


def p_expresion_char(t):
    'expresion   : CHARACTER'
    t[0] = ExpresionSimpleComilla(t[1], t.lineno(1), find_column(entrada, t.slice[1]))


def p_expresionBoolean(t):
    '''expresion          : TRUE
                          | FALSE'''
    if t[1].lower() == 'true':
        t[0] = ExpresionBoolean(True, t.lineno(1), find_column(entrada, t.slice[1]))
    elif t[1].lower() == 'false':
        t[0] = ExpresionBoolean(False, t.lineno(1), find_column(entrada, t.slice[1]))


def p_data_types(t):
    '''expresion_data_type        : INT
                                    | DOUBLE
                                    | STRING
                                    | CHAR
                                    | BOOLEAN'''
    t[0] = t[1]


# -------------------------------- CASTEOS ----------------------------------------
def p_expresionCasteo(t):
    'expresion      : PARIZQ expresion_data_type PARDER expresion'
    t[0] = Cast(t[2], t[4], t.lineno(1), find_column(entrada, t.slice[1]))


def p_expresion_call(t):
    'expresion      : call_instr'
    t[0] = t[1]


# -------------------------------- FUNCIONES ----------------------------------------
def p_function_params(t):
    'funct_instr        : FUNC ID PARIZQ params PARDER LLAVIZQ instrucciones LLAVDER'
    t[0] = Function(t[2], t[4], t[7], t.lineno(1), find_column(entrada, t.slice[1]))


def p_function(t):
    'funct_instr        : FUNC ID PARIZQ PARDER LLAVIZQ instrucciones LLAVDER'
    t[0] = Function(t[2], [], t[6], t.lineno(1), find_column(entrada, t.slice[1]))


def p_call_func(t):
    'call_instr     : ID PARIZQ PARDER def_instr_prima'
    t[0] = Call(t[1], [], t.lineno(1), find_column(entrada, t.slice[1]))


def p_call_func_params(t):
    'call_instr     : ID PARIZQ params_call PARDER def_instr_prima'
    t[0] = Call(t[1], t[3], t.lineno(1), find_column(entrada, t.slice[1]))


def p_params(t):
    'params     : params COMA param'
    t[1].append(t[3])
    t[0] = t[1]


def p_param(t):
    'params      : param'
    t[0] = [t[1]]


def p_param_id(t):
    'param     : expresion_data_type ID'
    t[0] = {'type': t[1], 'id': t[2]}


def p_params_exp(t):
    'params_call      : params_call COMA param_call'
    t[1].append(t[3])
    t[0] = t[1]


def p_params_call_exp(t):
    'params_call     : param_call'
    t[0] = [t[1]]


def p_param_exp(t):
    'param_call     : expresion'
    t[0] = t[1]


def p_return(t):
    'return_instr   : RETURN expresion def_instr_prima'
    t[0] = Return(t[2], t.lineno(1), find_column(entrada, t.slice[1]))


def p_return_func(t):
    'return_instr   : RETURN call_instr def_instr_prima'
    t[0] = Return(t[2], t.lineno(1), find_column(entrada, t.slice[1]))


# ------------------------------------  READ -----------------------------------
def p_read(t):
    'expresion      : READ PARIZQ PARDER def_instr_prima'
    t[0] = Read(t.lineno(1), find_column(entrada, t.slice[1]))


# ---------------------------- ERROR SINTACTICO --------------------------------

errores = []


def p_error(t):
    err = Excepcion("Error sintactico en ", f"{t.value}", t.lexer.lineno, find_column(t.lexer.lexdata, t))
    errores.append(err)
    # print(find_column(t.lexer.lexdata, t))
    print("Error sintáctico en '%s'" % t)


parser = yacc.yacc()

entrada = ''


def parse(input):
    global entrada
    entrada = input
    return parser.parse(input)
