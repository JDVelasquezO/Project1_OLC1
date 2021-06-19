from enum import Enum


class TIPO_DATO(Enum):
    NUMERO = 1
    CADENA = 2
    BOOLEAN = 3
    CHAR = 4
    NULL = 5


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

    def __init__(self, before=None):
        self.simbolos = {}
        self.before = before

    def agregar(self, simbolo):
        if simbolo.id.lower() in self.simbolos:
            return Exception("Semantico", f"Variable {simbolo.id} ya existe", 0, 0)
        else:
            self.simbolos[simbolo.id.lower()] = simbolo
            return True

    def obtener(self, id):
        actualTable = self
        while actualTable is not None:
            if id.lower() in actualTable.simbolos:
                return actualTable.simbolos[id]
            else:
                actualTable = actualTable.before
                if actualTable is None: return None

        return None

    def actualizar(self, simbolo):
        actualTable = self
        while actualTable is not None:
            if simbolo.id in actualTable.simbolos:
                actualTable.simbolos[simbolo.id] = simbolo
                return
            else:
                actualTable = actualTable.before
        return Exception("Semantico", "Tipo de dato  diferente")

    def isEmpty(self):
        pass
        return len(self.simbolos) == 0
