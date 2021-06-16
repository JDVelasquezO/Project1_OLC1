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

    def __init__(self, id):
        self.id = id


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
