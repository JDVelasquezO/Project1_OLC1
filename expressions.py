from enum import Enum
from Node import Node


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

    def getNode(self):
        node = Node("EXPRESION BINARIA")
        node.agregarHijoNodo(self.exp1.getNode())
        node.agregarHijo(str(self.operador))
        node.agregarHijoNodo(self.exp2.getNode())
        return node


class ExpresionNegativo(ExpresionNumerica):
    '''
        Esta clase representa la Expresión Aritmética Negativa.
        Esta clase recibe la expresion
    '''

    def __init__(self, exp, row, col):
        self.exp = exp
        self.row = row
        self.col = col

    def getNode(self):
        node = Node("EXPRESION NEGATIVA")
        node.agregarHijo(str(self.exp.operador))
        node.agregarHijoNodo(self.exp.getNode())
        return node


class ExpresionIncrement(ExpresionNumerica):
    def __init__(self, expression, operation, row, col):
        self.expression = expression
        self.operation = operation
        self.row = row
        self.col = col

    def getNode(self):
        node = Node("INCREMENTO")
        node.agregarHijoNodo(self.expression.getNode())
        node.agregarHijo(str(self.operation))


class ExpresionNumero(ExpresionNumerica):
    '''
        Esta clase representa una expresión numérica entera o decimal.
    '''

    def __init__(self, val=0, row=0, col=0):
        self.val = val
        self.row = row
        self.col = col

    def getNode(self):
        node = Node("NUMBER")
        node.agregarHijo(str(self.val))
        return node


class ExpresionIdentificador(ExpresionNumerica):
    '''
        Esta clase representa un identificador.
    '''

    def __init__(self, id="", row=0, col=0):
        self.id = id
        self.row = row
        self.col = col

    def getNode(self):
        node = Node("IDENTIFICATOR")
        node.agregarHijo(str(self.id))
        return node


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

    def getNode(self):
        node = Node("CONCATENATION")
        node.agregarHijoNodo(self.exp1.getNode())
        node.agregarHijo("+")
        node.agregarHijoNodo(self.exp2.getNode())
        return node


class ExpresionDobleComilla(ExpresionCadena):
    '''
        Esta clase representa una cadena entre comillas doble.
        Recibe como parámetro el valor del token procesado por el analizador léxico
    '''

    def __init__(self, val, row, col):
        self.val = val
        self.row = row
        self.col = col

    def getNode(self):
        node = Node("DOUBLE QUOTE STRING")
        node.agregarHijo(str(self.val))
        return node


class ExpresionCadenaNumerico(ExpresionCadena):
    '''
        Esta clase representa una expresión numérica tratada como cadena.
        Recibe como parámetro la expresión numérica
    '''

    def __init__(self, exp, row, col):
        self.exp = exp
        self.row = row
        self.col = col

    def getNode(self):
        node = Node("NUMBER STRING")
        node.agregarHijoNodo(self.exp.getNode())
        return node


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

    def getNode(self):
        node = Node("LOGIC EXPRESSION")
        node.agregarHijoNodo(self.exp1.getNode())
        node.agregarHijo(str(self.operador))
        node.agregarHijoNodo(self.exp2.getNode())
        return node


class ExpresionOperacionLogica:
    def __init__(self, exp1, exp2, operador, row, col):
        self.exp1 = exp1
        self.exp2 = exp2
        self.operador = operador
        self.row = row
        self.col = col

    def getNode(self):
        node = Node("OPERATION LOGIC")
        node.agregarHijoNodo(self.exp1.getNode())
        node.agregarHijo(str(self.operador))
        node.agregarHijoNodo(self.exp2.getNode())
        return node


class ExpresionLogicaNot:
    def __init__(self, exp1, operador, row, col):
        self.exp1 = exp1
        self.operador = operador
        self.row = row
        self.col = col

    def getNode(self):
        node = Node("LOGICAL NEGATION")
        node.agregarHijo(str(self.operador))
        node.agregarHijoNodo(self.exp1.getNode())
        return node


class ExpresionBoolean:
    def __init__(self, exp, row, col):
        self.val = exp
        self.row = row
        self.col = col

    def getNode(self):
        node = Node("BOOLEAN")
        node.agregarHijo(str(self.val))
        return node


class ExpresionChar:
    ''' Abstract class for chars '''


class ExpresionSimpleComilla(ExpresionChar):
    def __init__(self, val, row, col):
        self.val = val
        self.row = row
        self.col = col

    def getNode(self):
        node = Node("CHAR")
        node.agregarHijo(str(self.val))
        return node


class ExpresionNull:
    def __init__(self, exp, row, col):
        self.exp = exp
        self.row = row
        self.col = col

    def getNode(self):
        node = Node("NULL")
        node.agregarHijo("null")
        return node
