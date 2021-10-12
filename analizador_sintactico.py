from objetos import Error, Aceptado

class Analizador_sintactico:
    def __init__(self):
        self.aceptado = []
        self.errores = []

    def analizar(self, datos):
        self.aceptado=[]
        self.errores=[]
        self.datos = datos
        self.indice = 0
        self.guardado = ""
        self.inicio()

    def inicio(self):
        pass