from tkinter import filedialog, messagebox,ttk
from analizador_lexico import Analizador_lexico

class Logica:
    def __init__(self):
        pass

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