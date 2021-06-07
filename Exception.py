class Excepcion:
    def __init__(self, type, desc, row, col):
        self.type = type
        self.desc = desc
        self.row = row
        self.col = col

    def toString(self):
        return f"{self.type} - {self.desc} [{str(self.row)}, {str(self.col)}]"
