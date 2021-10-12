class Token:

    def __init__(self,lexema,tipo,linea,col):
        self.lexema = lexema
        self.tipo = tipo
        self.linea = linea
        self.col = col

class Error:

    def __init__(self,lexema,tipo,linea,col):
        self.lexema = lexema
        self.tipo = tipo
        self.linea = linea
        self.col = col

class Aceptado:

    def __init__(self, entradas,tipo):
        self.entradas = entradas
        self.tipo = tipo