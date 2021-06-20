from enum import Enum


class TIPO_DATO(Enum):
    NUMERO = 1
    CADENA = 2
    BOOLEAN = 3
    CHAR = 4
    NULL = 5


class Simbolo:
    'Esta clase representa un simbolo dentro de nuestra tabla de simbolos'

    def __init__(self, id, tipo, valor, row, col):
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
            return Exception("Semantico", f"Variable {simbolo.id} ya existe", simbolo.row, simbolo.col)
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
                actualSimb = actualTable.simbolos[simbolo.id].tipo
                if actualSimb == simbolo.tipo or actualSimb is None:
                    actualTable.simbolos[simbolo.id] = simbolo
                    return
                print(Exception("Semantico", "Tipo de dato  diferente", simbolo.row, simbolo.col))
                return Exception("Semantico", "Tipo de dato  diferente", simbolo.row, simbolo.col)
            else:
                actualTable = actualTable.before
        return Exception("Semantico", "Variable no encontrada", simbolo.row, simbolo.col)

    def isEmpty(self):
        pass
        return len(self.simbolos) == 0

    def delete_data_type(self, id):
        simbolo = self.obtener(id)
        simbolo.tipo = None
        simbolo.valor = None
        pass
