from Node import Node
from symbolTable import TIPO_DATO as Type


class Instruccion:
    '''This is an abstract class'''


class Imprimir(Instruccion):
    '''
        Esta clase representa la instrucción imprimir.
        La instrucción imprimir únicamente tiene como parámetro una cadena
    '''

    def __init__(self, cad, row, col):
        self.cad = cad
        self.row = row
        self.col = col

    def getNode(self):
        node = Node("PRINT")
        node.agregarHijoNodo(self.cad.getNode())
        return node


class While(Instruccion):
    '''
        Esta clase representa la instrucción mientras.
        La instrucción mientras recibe como parámetro una expresión lógica y la lista
        de instrucciones a ejecutar si la expresión lógica es verdadera.
    '''

    def __init__(self, expLogica, instrucciones=[], row=0, col=0):
        self.expLogica = expLogica
        self.instrucciones = instrucciones
        self.row = row
        self.col = col

    def getNode(self):
        node = Node("WHILE")
        instrs = Node("INSTRUCTIONS")
        for instr in self.instrucciones:
            instrs.agregarHijoNodo(instr.getNode())
        node.agregarHijoNodo(instrs)
        return node


class Definicion(Instruccion):
    '''
        Esta clase representa la instrucción de definición de variables.
        Recibe como parámetro el nombre del identificador a definir
    '''

    def __init__(self, id, row, col):
        self.id = id
        self.row = row
        self.col = col

    def getNode(self):
        node = Node("DEFINITION")
        node.agregarHijo(str(self.id))
        return node


class Asignacion(Instruccion):
    '''
        Esta clase representa la instrucción de asignación de variables
        Recibe como parámetro el identificador a asignar y el valor que será asignado.
    '''

    def __init__(self, id, expression, row, col):
        self.id = id
        self.expression = expression
        self.row = row
        self.col = col

    def getNode(self):
        node = Node("ASIGNATION")
        node.agregarHijo(str(self.id))
        node.agregarHijoNodo(self.expression.getNode())
        return node


class Definicion_Asignacion(Instruccion):
    def __init__(self, id, expression, row, col):
        self.id = id
        self.expression = expression
        self.row = row
        self.col = col

    def getNode(self):
        node = Node("DEF_ASIGN")
        node.agregarHijoNodo(str(self.id))
        node.agregarHijoNodo(self.expression.getNode())
        return node


class Funcion_Main(Instruccion):
    def __init__(self, instrucciones=[], row=0, col=0):
        self.instrucciones = instrucciones
        self.row = row
        self.col = col

    def getNode(self):
        node = Node("MAIN")
        instrs = Node("INSTRUCTIONS")
        for inst in self.instrucciones:
            instrs.agregarHijoNodo(inst.getNode())
        node.agregarHijoNodo(instrs)
        return node


class If(Instruccion):
    '''
        Esta clase representa la instrucción if.
        La instrucción if recibe como parámetro una expresión lógica y la lista
        de instrucciones a ejecutar si la expresión lógica es verdadera.
    '''

    def __init__(self, expLogica, instrucciones=[], row=0, col=0):
        self.expLogica = expLogica
        self.instrucciones = instrucciones
        self.row = row
        self.col = col

    def getNode(self):
        node = Node("IF")
        instrs = Node("INSTRUCTIONS")
        for instr in self.instrucciones:
            instrs.agregarHijoNodo(instr.getNode())
        node.agregarHijoNodo(instrs)
        return node


class IfElse(Instruccion):
    '''
        Esta clase representa la instrucción if-else.
        La instrucción if-else recibe como parámetro una expresión lógica y la lista
        de instrucciones a ejecutar si la expresión lógica es verdadera y otro lista de instrucciones
        a ejecutar si la expresión lógica es falsa.
    '''

    def __init__(self, expLogica, instrIfVerdadero=[], instrIfFalso=[], row=0, col=0):
        self.expLogica = expLogica
        self.instrIfVerdadero = instrIfVerdadero
        self.instrIfFalso = instrIfFalso
        self.row = row
        self.col = col

    def getNode(self):
        node = Node("IF-ELSE")
        instrs = Node("INSTRUCTIONS")

        if self.instrIfVerdadero is not None:
            for instr in self.instrIfVerdadero:
                instrs.agregarHijoNodo(instr.getNode())
            node.agregarHijoNodo(instrs)

        if self.instrIfFalso is not None:
            for instr in self.instrIfFalso:
                instrs.agregarHijoNodo(instr.getNode())
            node.agregarHijoNodo(instrs)
        return node


class ElseIf(Instruccion):
    def __init__(self, expLogica, instrIfVerdadero=[], instrElse=None, row=0, col=0):
        self.expLogica = expLogica
        self.instrIfVerdadero = instrIfVerdadero
        self.instrElse = instrElse
        self.row = row
        self.col = col

    def getNode(self):
        node = Node("IF-ELSE")
        instrs = Node("INSTRUCTIONS")

        if len(self.instrIfVerdadero) > 0:
            for instr in self.instrIfVerdadero:
                instrs.agregarHijoNodo(instr.getNode())
            node.agregarHijoNodo(instrs)

        elseNode = Node("ELSE")
        elseNode.agregarHijoNodo(self.instrElse.getNode())
        node.agregarHijoNodo(elseNode)

        # if len(self.instrElse) > 0:
        #     for instr in self.instrElse:
        #         instrs.agregarHijoNodo(instr.getNode())
        #     node.agregarHijoNodo(instrs)
        return node


class Break(Instruccion):
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def getNode(self):
        node = Node("BREAK")
        return node


class Continue(Instruccion):
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def getNode(self):
        node = Node("CONTINUE")
        return node


class Case(Instruccion):
    def __init__(self, expression, instrucciones=[], break_instr=None, row=0, col=0):
        self.expression = expression
        self.instrucciones = instrucciones
        self.break_instr = break_instr
        self.row = row
        self.col = col

    def getNode(self):
        node = Node("CASE")
        instrs = Node("INTRUCTIONS")
        for inst in self.instrucciones:
            instrs.agregarHijoNodo(inst.getNode())
        node.agregarHijoNodo(instrs)
        return node


class Switch(Instruccion):
    def __init__(self, expLogica, cases, default, row, col):
        self.expLogica = expLogica
        self.cases = cases
        self.default = default
        self.row = row
        self.col = col

    def getNode(self):
        node = Node("SWITCH")
        cases = Node("CASES")
        for case in self.cases:
            cases.agregarHijoNodo(case.getNode())
        node.agregarHijoNodo(cases)
        return node


class For(Instruccion):
    def __init__(self, exp1, expLogica, reAsign, instrucciones = [], row=0, col=0):
        self.exp1 = exp1
        self.expLogica = expLogica
        self.reAsign = reAsign
        self.instrucciones = instrucciones
        self.row = row
        self.col = col

    def getNode(self):
        node = Node("FOR")
        instrs = Node("INTRUCTIONS")
        for instr in self.instrucciones:
            instrs.agregarHijoNodo(instr.getNode())
        node.agregarHijoNodo(instrs)
        return node


class Cast:
    def __init__(self, data, value, row, col):
        self.data = data
        self.value = value
        self.col = col
        self.row = row

    def getNode(self):
        node = Node("CAST")
        node.agregarHijo(str(self.data))
        node.agregarHijo(str(self.value))
        node.agregarHijoNodo(node)
        return node


class Function:
    def __init__(self, name, params, instructions, row, col):
        self.id = name
        self.params = params
        self.instructions = instructions
        self.row = row
        self.col = col
        self.type = Type.NULL

    def getNode(self):
        node = Node("FUNCTION")
        node.agregarHijo(str(self.id))
        node.agregarHijo("(")
        params = Node("PARAMS")
        for param in self.params:
            p = Node("PARAM")
            p.agregarHijo(param)
            params.agregarHijoNodo(p)
        node.agregarHijo(")")
        node.agregarHijo("{")

        instrs = Node("INSTRUCTIONS")
        for instr in self.instructions:
            instrs.agregarHijoNodo(instr.getNode())
        node.agregarHijoNodo(instrs)
        node.agregarHijo("}")

        return node


class Call:
    def __init__(self, name, params, row, col):
        self.name = name
        self.params = params
        self.row = row
        self.col = col

    def getNode(self):
        node = Node("CALL FUNCTION")
        node.agregarHijo(str(self.name))
        parameters = Node("PARAMS")
        for p in self.params:
            parameters.agregarHijoNodo(p.getNode())
        node.agregarHijoNodo(parameters)
        return node


class Return:
    def __init__(self, exp, row, col):
        self.exp = exp
        self.row = row
        self.col = col

    def getNode(self):
        node = Node("RETURN")
        node.agregarHijoNodo(self.exp.getNode())
        return node


class toNative:
    def __init__(self, name, exp):
        self.name = name
        self.exp = exp

    def getNode(self):
        node = Node("TO NATIVE")
        node.agregarHijo(str(self.name))
        node.agregarHijoNodo(self.exp.getNode())
        return node


class Read:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.type = Type.CADENA
