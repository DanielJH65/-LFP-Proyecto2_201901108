import re
from objetos import Error, Token

class Analizador_lexico:
    def __init__(self):
        self.tokens = []
        self.tokens_sintactico = []
        self.errores = []

    def analizar(self, datos):
        self.tokens=[]
        self.errores=[]
        reservadas = ["Claves","Registros","imprimir","imprimirln","conteo","promedio", "contarsi","datos","sumar","max","min","exportarReporte"]

        estado = 0
        linea = 1
        columna = 1
        final = '~'
        guardado = ''
        datos+=final
        i = 0

        while i < len(datos):
            a = datos[i]

            if estado == 0:
                if a == "(":
                    self.tokens.append(Token(a,"ParA",linea, columna))
                    self.tokens_sintactico.append(Token(a,"ParA",linea, columna))
                    columna+=1
                elif a == ")":
                    self.tokens.append(Token(a,"ParC",linea, columna))
                    self.tokens_sintactico.append(Token(a,"ParC",linea, columna))
                    columna+=1
                elif a == "{":
                    self.tokens.append(Token(a,"LlaveA",linea, columna))
                    self.tokens_sintactico.append(Token(a,"LlaveA",linea, columna))
                    columna+=1
                elif a == "}":
                    self.tokens.append(Token(a,"LlaveC",linea, columna))
                    self.tokens_sintactico.append(Token(a,"LlaveC",linea, columna))
                    columna+=1
                elif a == "[":
                    self.tokens.append(Token(a,"CorA",linea, columna))
                    self.tokens_sintactico.append(Token(a,"CorA",linea, columna))
                    columna+=1
                elif a == "]":
                    self.tokens.append(Token(a,"CorC",linea, columna))
                    self.tokens_sintactico.append(Token(a,"CorC",linea, columna))
                    columna+=1
                elif a == ",":
                    self.tokens.append(Token(a,"Coma",linea, columna))
                    self.tokens_sintactico.append(Token(a,"Coma",linea, columna))
                    columna+=1
                elif a == ";":
                    self.tokens.append(Token(a,"PuntoC",linea, columna))
                    self.tokens_sintactico.append(Token(a,"PuntoC",linea, columna))
                    columna+=1
                elif a=="\n":
                    linea+=1
                    columna = 0
                elif a=="\r":
                    pass
                elif a==" " or a =="\t":
                    columna+=1
                elif re.search('[A-Za-z]',a):
                    estado = 1
                    columna +=1
                    guardado+=a
                elif a == "\"":
                    self.tokens.append(Token(a,"Comillas",linea,columna))
                    self.tokens_sintactico.append(Token(a,"Comillas",linea,columna))
                    columna+=1
                    estado = 2
                elif a == "#":
                    estado = 3
                    columna+=1
                    guardado+=a
                elif a == "'":
                    estado = 4
                    columna+=1
                    guardado+=a
                elif re.search('\d',a):
                    estado = 9
                    columna+=1
                    guardado+=a
                elif a == final:
                    self.tokens.append(Token(a,"Final",linea,columna))
                    break
                else:
                    self.errores.append(Error(a,"Error Lexico",linea,columna))
                    columna+=1
            elif estado == 1:
                if re.search('[a-z]',a):
                    guardado+=a
                    columna+=1
                else:
                    if guardado in reservadas:
                        self.tokens.append(Token(guardado,guardado,linea,columna))
                        self.tokens_sintactico.append(Token(guardado,guardado,linea,columna))
                    else:
                        self.errores.append(Error(guardado,"Error Lexico",linea,columna))
                    i -= 1
                    estado = 0
                    guardado=""
            elif estado == 2:
                if a == "\"":
                    self.tokens.append(Token(guardado,"Texto",linea,columna))
                    self.tokens_sintactico.append(Token(guardado,"Texto",linea,columna))
                    columna+=1
                    self.tokens.append(Token(a,"Comillas",linea,columna))
                    self.tokens_sintactico.append(Token(a,"Comillas",linea,columna))
                    estado=0;
                    guardado=""
                elif a=="\n":
                    guardado+=a
                    linea+=1
                    columna = 0
                elif a=="\r":
                    guardado+=a
                else:
                    guardado+=a
                    columna+=1
            elif estado == 3:
                if a == "\n":
                    self.tokens.append(Token(guardado,"Comentario",linea,columna))
                    columna = 1
                    estado=0;
                    guardado=""
                else:
                    guardado+=a
                    columna+=1
            elif estado == 4:
                if a == "'":
                    estado = 5
                    columna+=1
                    guardado+=a
                else:
                    self.errores.append(Error(guardado,"Error Lexico",linea,columna))
                    guardado=""
                    estado = 0
                    i-=1
            elif estado == 5:
                if a == "'":
                    estado = 6
                    columna+=1
                    guardado+=a
                else:
                    self.errores.append(Error(guardado,"Error Lexico",linea,columna))
                    guardado=""
                    estado = 0
                    i-=1
            elif estado == 6:
                if a == "'":
                    estado = 7
                    columna+=1
                    guardado+=a
                elif a=="\n":
                    guardado+=a
                    linea+=1
                    columna = 0
                elif a=="\r":
                    guardado+=a
                else:
                    guardado+=a
                    columna+=1
            elif estado == 7:
                if a == "'":
                    estado == 8
                    columna+=1
                    guardado+=a
                else:
                    self.errores.append(Error(guardado,"Error Lexico",linea,columna))
                    guardado=""
                    estado = 0
                    i-=1
            elif estado == 8:
                if a == "'":
                    guardado+=a
                    self.tokens.append(Token(guardado,"ComentarioMulti",linea,columna))
                    guardado = ""
                    estado = 0
                else:
                    self.errores.append(Error(guardado,"Error Lexico",linea,columna))
                    guardado=""
                    estado = 0
                    i-=1
            elif estado == 9:
                if re.search('\d',a):
                    guardado+=a
                    columna+=1
                elif re.search('\.',a):
                    guardado+=a
                    estado = 10
                    columna+=1
                else:
                    self.tokens.append(Token(guardado,"entero",linea,columna))
                    self.tokens_sintactico.append(Token(guardado,"entero",linea,columna))
                    guardado=""
                    i-=1
                    estado=0
            elif estado == 10:
                if re.search('\d',a):
                    guardado+=a
                    columna+=1
                    estado = 11
                else:
                    self.errores.append(Error(guardado,"Error Lexico",linea,columna))
                    guardado=""
                    estado = 0
                    i-=1
            elif estado == 11:
                if re.search('\d',a):
                    guardado+=a
                    columna+=1
                    self.tokens.append(Token(guardado,"decimal",linea,columna))
                    self.tokens_sintactico.append(Token(guardado,"decimal",linea,columna))
                    guardado = ""
                    estado = 0
                else:
                    self.errores.append(Error(guardado,"Error Lexico",linea,columna))
                    estado = 0
                    guardado=""
                    i-=1
            i+=1