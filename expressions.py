from enum import Enum
from symbolTable import TIPO_DATO as Type


class OPERACION_ARITMETICA(Enum):
    MAS = 1
    MENOS = 2
    POR = 3
    DIVIDIDO = 4
    POTENCIA = 5
    MODULO = 6
    INCREMENTO = 7
    DISMINUCION = 8


class OPERACION_LOGICA(Enum):
    MAYOR_QUE = 1
    MENOR_QUE = 2
    MAYORIGUAL_QUE = 3
    MENORIGUAL_QUE = 4
    IGUAL = 5
    DIFERENTE = 6


class OPERADOR_LOGICO(Enum):
    AND = 1
    OR = 2
    NOT = 3


class ExpresionNumerica:
    '''
        Esta clase representa una expresión numérica
    '''


class ExpresionBinaria(ExpresionNumerica):
    '''
        Esta clase representa la Expresión Aritmética Binaria.
        Esta clase recibe los operandos y el operador
    '''

    def __init__(self, exp1, exp2, operador, row, col):
        self.exp1 = exp1
        self.exp2 = exp2
        self.operador = operador
        self.row = row
        self.col = col


class ExpresionNegativo(ExpresionNumerica):
    '''
        Esta clase representa la Expresión Aritmética Negativa.
        Esta clase recibe la expresion
    '''

    def __init__(self, exp, row, col):
        self.exp = exp
        self.row = row
        self.col = col


class ExpresionIncrement(ExpresionNumerica):
    def __init__(self, expression, operation, row, col):
        self.expression = expression
        self.operation = operation
        self.row = row
        self.col = col


class ExpresionNumero(ExpresionNumerica):
    '''
        Esta clase representa una expresión numérica entera o decimal.
    '''

    def __init__(self, val=0, row=0, col=0):
        self.val = val
        self.row = row
        self.col = col


class ExpresionIdentificador(ExpresionNumerica):
    '''
        Esta clase representa un identificador.
    '''

    def __init__(self, id="", row=0, col=0):
        self.id = id
        self.row = row
        self.col = col


class ExpresionCadena:
    '''
        Esta clase representa una Expresión de tipo cadena.
    '''


class ExpresionConcatenar(ExpresionCadena):
    '''
        Esta clase representa una Expresión de tipo cadena.
        Recibe como parámetros las 2 expresiones a concatenar
    '''

    def __init__(self, exp1, exp2, row, col):
        self.exp1 = exp1
        self.exp2 = exp2
        self.row = row
        self.col = col


class ExpresionDobleComilla(ExpresionCadena):
    '''
        Esta clase representa una cadena entre comillas doble.
        Recibe como parámetro el valor del token procesado por el analizador léxico
    '''

    def __init__(self, val, row, col):
        self.val = val
        self.row = row
        self.col = col


class ExpresionCadenaNumerico(ExpresionCadena):
    '''
        Esta clase representa una expresión numérica tratada como cadena.
        Recibe como parámetro la expresión numérica
    '''

    def __init__(self, exp, row, col):
        self.exp = exp
        self.row = row
        self.col = col


class ExpresionLogica:
    '''
        Esta clase representa la expresión lógica.
        Esta clase recibe los operandos y el operador
    '''

    def __init__(self, exp1, exp2, operador, row, col):
        self.exp1 = exp1
        self.exp2 = exp2
        self.operador = operador
        self.row = row
        self.col = col


class ExpresionOperacionLogica:
    def __init__(self, exp1, exp2, operador, row, col):
        self.exp1 = exp1
        self.exp2 = exp2
        self.operador = operador
        self.row = row
        self.col = col


class ExpresionLogicaNot:
    def __init__(self, exp1, operador, row, col):
        self.exp1 = exp1
        self.operador = operador
        self.row = row
        self.col = col


class ExpresionBoolean:
    def __init__(self, exp, row, col):
        self.val = exp
        self.row = row
        self.col = col


class ExpresionChar:
    ''' Abstract class for chars '''


class ExpresionSimpleComilla(ExpresionChar):
    def __init__(self, val, row, col):
        self.val = val
        self.row = row
        self.col = col


class ExpresionNull:
    def __init__(self, exp, row, col):
        self.exp = exp
        self.row = row
        self.col = col


class Cast:
    def __init__(self, data, value, row, col):
        self.data = data
        self.value = value
        self.col = col
        self.row = row


class Function:
    def __init__(self, name, params, instructions, row, col):
        self.id = name
        self.params = params
        self.instructions = instructions
        self.row = row
        self.col = col
        self.type = Type.NULL


class Call:
    def __init__(self, name, params, row, col):
        self.name = name
        self.params = params
        self.row = row
        self.col = col


class Return:
    def __init__(self, exp, row, col):
        self.exp = exp
        self.row = row
        self.col = col


class toNative:
    def __init__(self, name, exp):
        self.name = name
        self.exp = exp


class Read:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.type = Type.CADENA
