from objetos import Error, Token

class Analizador_lexico:
    def __init__(self) -> None:
        self.tokens = []
        self.tokens_sintactico = []
        self.errores = []

    def analizar(self, datos):
        self.tokens=[]
        self.errores=[]
        reservadas = ["Claves","Registros","imprimir","imprimirln","conteo","promedio", "contarsi","datos","sumar","max","min","exportarReporte"]

        linea = 1
        columna = 1
        final = '~'
        guardado = ''
        datos+=final
        i = 0

        while i < len(datos):
            a = datos[i]
            i+=1