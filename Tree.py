class Tree:
    def __init__(self, instrs):
        self.instrs = instrs
        self.funcs = []
        self.excepts = []
        self.TSGlobal = None
        self.__text = None
        self.dot = ''
        self.contador = 0

    def getTextInterfaz(self):
        return self.__text

    def setTextInterfaz(self, text):
        self.__text = text

    def getInstrs(self):
        return self.instrs

    def setInstrs(self, instrs):
        self.instrs = instrs

    def getExcepts(self):
        return self.excepts

    def setExcepts(self, excepts):
        self.excepts = excepts

    def getFunctions(self):
        return self.funcs

    def getFunction(self, name):
        for func in self.funcs:
            return func if func.name == name else None

    def addFunction(self, function):
        self.funcs.append(function)

    def getTSGlobal(self):
        return self.TSGlobal

    def setTSglobal(self, TSglobal):
        self.TSGlobal = TSglobal

    def getDot(self, raiz):
        self.dot = ''
        self.dot += "digraph {\n"
        self.dot += "n0[label=\"" + raiz.getValor().replace("\"", "\\\"") + "\"];\n"
        self.contador = 1
        self.recorrerAST("n0", raiz)
        self.dot += "}"
        return self.dot

    def recorrerAST(self, idPadre, nodoPadre):
        for hijo in nodoPadre.getHijos():
            nombreHijo = "n" + str(self.contador)
            self.dot += nombreHijo + "[label=\"" + hijo.getValor().replace("\"", "\\\"") + "\"];\n"
            self.dot += idPadre + "->" + nombreHijo + ";\n"
            self.contador += 1
            self.recorrerAST(nombreHijo, hijo)
