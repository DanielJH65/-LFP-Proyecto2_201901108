from tkinter import filedialog, messagebox,ttk
from analizador_lexico import Analizador_lexico
from html import HTML

class Logica:
    def __init__(self):
        self.entrada=Analizador_lexico()

    def salir(self):
        exit()

    def cargar_archivo(self, texto):
        try:
            ruta = filedialog.askopenfilename(defaultextension=".lfp")
            archivo=open(ruta,"r")
            self.datos = archivo.read()
            archivo.close()
            messagebox.showinfo("Archivo","Archivo leído exitosamente")
        except:
            messagebox.showerror("Archivo", "Error al abrir el archivo")
        self.mostrar_datos(texto)

    def mostrar_datos(self, texto):
        texto.delete(1.0,"end")
        texto.insert(1.0, self.datos)

    def analizar_archivo(self,text):
        self.modificado = text.get(1.0,"end")
        try:
            self.entrada.analizar(self.modificado)
        except:
            messagebox.showerror("Analizador Lexico", "Error al analizar el archivo")
        try:
            self.entrada.analizar(self.modificado)
        except:
            messagebox.showerror("Analizador Sintactico", "Error al analizar el archivo")
    
    def generar_reportes(self):
        html="""
            <div class="jumbotron my-4 mx-4">
            <br><center><h3>Listado de Tokens</h3></center><br>
            <table class="table table-hover">
                <thead>
                    <tr>
                        <th scope="col">Lexema</th>
                        <th scope="col">Tipo</th>
                        <th scope="col">Columna</th>
                        <th scope="col">Fila</th>
                    </tr>
                </thead>
                <tbody>
            """
        for i in self.entrada.tokens:
            html+=f"""
            <tr class="table-success">
                <td>{i.lexema}</td>
                <td>{i.tipo}</td>
                <td>{i.col}</td>
                <td>{i.linea}</td>
            </tr>
            """
        html+="""
                </tbody>
            </table>
            </div>
            """
        HTML.generarHTML(html,"Tabla de Tokens")
        
        if self.entrada.errores != []:
            html="""
            <div class="jumbotron my-4 mx-4">
            <br><center><h3>Listado de Errores</h3></center><br>
            <table class="table table-hover">
                <thead>
                    <tr>
                        <th scope="col">Dato</th>
                        <th scope="col>Tipo</th>
                        <th scope="col">Columna</th>
                        <th scope="col">Fila</th>
                    </tr>
                </thead>
                <tbody>
                """
            for i in self.entrada.errores:
                html+=f"""
                <tr class="table-danger">
                    <td>{i.lexema}</td>
                    <td>{i.tipo}</td>
                    <td>{i.col}</td>
                    <td>{i.linea}</td>
                </tr>
                """
            html+="""
                    </tbody>
                </table>
                </div>
                """
            HTML.generarHTML(html,"Tabla de Errores")