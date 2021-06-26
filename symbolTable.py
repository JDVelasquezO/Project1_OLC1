from enum import Enum
from Exception import Excepcion


class TIPO_DATO(Enum):
    NUMERO = 1
    CADENA = 2
    BOOLEAN = 3
    CHAR = 4
    NULL = 5


class Simbolo:
    'Esta clase representa un simbolo dentro de nuestra tabla de simbolos'

    def __init__(self, id, tipo, valor, params=[], row=0, col=0):
        self.id = id.lower()
        self.tipo = tipo
        self.valor = valor
        self.params = params
        self.row = row
        self.col = col


class TablaDeSimbolos:
    'Esta clase representa la tabla de simbolos'

    def __init__(self, before=None):
        self.simbolos = {}
        self.before = before

    def agregar(self, simbolo):
        if simbolo.id.lower() in self.simbolos:
            return Excepcion("Semantico", f"Variable {simbolo.id} ya existe", simbolo.row, simbolo.col)
        else:
            self.simbolos[simbolo.id.lower()] = simbolo
            return True

    def obtener(self, id):
        actualTable = self
        while actualTable is not None:
            if id.lower() in actualTable.simbolos:
                return actualTable.simbolos[id.lower()]
            else:
                actualTable = actualTable.before
                if actualTable is None: return None

        return None

    def actualizar(self, simbolo, errs):
        actualTable = self
        while actualTable is not None:
            if simbolo.id in actualTable.simbolos:
                actualTypeSimb = actualTable.simbolos[simbolo.id].tipo
                if actualTypeSimb == simbolo.tipo or actualTypeSimb is None or actualTypeSimb == TIPO_DATO.NULL:
                    actualTable.simbolos[simbolo.id] = simbolo
                    return
                err = Excepcion(">  Semantico", "Tipo de dato  diferente", simbolo.row, simbolo.col).toString()
                errs.append(err)
                print(err)
                return err
            else:
                actualTable = actualTable.before
        return Excepcion(">  Semantico", "Variable no encontrada", simbolo.row, simbolo.col)

    def isEmpty(self):
        pass
        return len(self.simbolos) == 0

    def delete_data_type(self, id):
        simbolo = self.obtener(id)
        simbolo.tipo = None
        simbolo.valor = None
        pass
