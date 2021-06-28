class Tree:
    def __init__(self, instrs):
        self.instrs = instrs
        self.funcs = []
        self.excepts = []
        self.TSGlobal = None

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
