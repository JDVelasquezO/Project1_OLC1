from enum import Enum


class TIPO_DATO(Enum):
    NUMERO = 1
    CADENA = 2


class Simbolo:
    'Esta clase representa un simbolo dentro de nuestra tabla de simbolos'

    def __init__(self, id, tipo, valor, row=0, col=0):
        self.id = id.lower()
        self.tipo = tipo
        self.valor = valor
        self.row = row
        self.col = col


class TablaDeSimbolos:
    'Esta clase representa la tabla de simbolos'

    def __init__(self, simbolos={}):
        self.simbolos = simbolos

    def agregar(self, simbolo):
        self.simbolos[simbolo.id] = simbolo

    def obtener(self, id):
        if not id in self.simbolos:
            print('Error: variable ', id, ' no definida.')

        return self.simbolos[id]

    def actualizar(self, simbolo):
        if not simbolo.id in self.simbolos:
            print('Error: variable ', simbolo.id, ' no definida.')
        else:
            self.simbolos[simbolo.id] = simbolo

    def isEmpty(self):
        pass
        return len(self.simbolos) == 0
