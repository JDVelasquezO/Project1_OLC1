class Instruccion:
    '''This is an abstract class'''


class Imprimir(Instruccion):
    '''
        Esta clase representa la instrucción imprimir.
        La instrucción imprimir únicamente tiene como parámetro una cadena
    '''

    def __init__(self, cad):
        self.cad = cad


class While(Instruccion):
    '''
        Esta clase representa la instrucción mientras.
        La instrucción mientras recibe como parámetro una expresión lógica y la lista
        de instrucciones a ejecutar si la expresión lógica es verdadera.
    '''

    def __init__(self, expLogica, instrucciones=[]):
        self.expLogica = expLogica
        self.instrucciones = instrucciones


class Definicion(Instruccion):
    '''
        Esta clase representa la instrucción de definición de variables.
        Recibe como parámetro el nombre del identificador a definir
    '''

    def __init__(self, id, row, col):
        self.id = id
        self.row = row
        self.col = col


class Asignacion(Instruccion):
    '''
        Esta clase representa la instrucción de asignación de variables
        Recibe como parámetro el identificador a asignar y el valor que será asignado.
    '''

    def __init__(self, id, expression):
        self.id = id
        self.expression = expression


class Definicion_Asignacion(Instruccion):
    def __init__(self, id, expression):
        self.id = id
        self.expression = expression


class Funcion_Main(Instruccion):
    def __init__(self, instrucciones=[]):
        self.instrucciones = instrucciones


class If(Instruccion):
    '''
        Esta clase representa la instrucción if.
        La instrucción if recibe como parámetro una expresión lógica y la lista
        de instrucciones a ejecutar si la expresión lógica es verdadera.
    '''

    def __init__(self, expLogica, instrucciones=[]):
        self.expLogica = expLogica
        self.instrucciones = instrucciones


class IfElse(Instruccion):
    '''
        Esta clase representa la instrucción if-else.
        La instrucción if-else recibe como parámetro una expresión lógica y la lista
        de instrucciones a ejecutar si la expresión lógica es verdadera y otro lista de instrucciones
        a ejecutar si la expresión lógica es falsa.
    '''

    def __init__(self, expLogica, instrIfVerdadero=[], instrIfFalso=[]):
        self.expLogica = expLogica
        self.instrIfVerdadero = instrIfVerdadero
        self.instrIfFalso = instrIfFalso


class ElseIf(Instruccion):
    def __init__(self, expLogica, instrIfVerdadero=[], instrElse=[]):
        self.expLogica = expLogica
        self.instrIfVerdadero = instrIfVerdadero
        self.instrElse = instrElse


class Break(Instruccion):
    def __init__(self, col):
        self.col = col


class Case(Instruccion):
    def __init__(self, expression, instrucciones=[], break_instr=None):
        self.expression = expression
        self.instrucciones = instrucciones
        self.break_instr = break_instr


class Switch(Instruccion):
    def __init__(self, expLogica, cases, default):
        self.expLogica = expLogica
        self.cases = cases
        self.default = default


class For(Instruccion):
    def __init__(self, exp1, expLogica, reAsign, instrucciones = []):
        self.exp1 = exp1
        self.expLogica = expLogica
        self.reAsign = reAsign
        self.instrucciones = instrucciones
