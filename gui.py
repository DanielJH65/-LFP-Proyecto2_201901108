from tkinter import *
from tkinter import ttk
from logica import Logica

class Gui:

    def __init__(self):
        self.l = Logica()
        self.principal()
    
    def principal(self):
        self.root = Tk()
        self.root.title("Proyecto 2 - 201901108")
        self.root.resizable(0,0)
        self.root.geometry("600x600")
        self.frame = ttk.Frame(self.root)
        self.frame.grid(column=0, row=0, sticky=(N,W,E,S))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.cargar = ttk.Button(self.frame, text="Abrir", command=self.abrir) #Botón Abrir
        self.cargar.grid(column=0,row=0, sticky=(E,W))
        self.analizar = ttk.Button(self.frame, text="Analizar", command=self.analizador) #Botón Analizar
        self.analizar.grid(column=1,row=0, sticky=(E,W))
        self.reportes = ttk.Button(self.frame, text="Reportes", command=self.l.generar_reportes) #Botón Reportes
        self.reportes.grid(column=2,row=0, sticky=(E,W))
        self.salir = ttk.Button(self.frame, text="Salir", command=self.l.salir) #Botón Salir
        self.salir.grid(column=6,row=0, sticky=(E,W))
        ttk.Label(self.frame,text="").grid(column=0,row=1, columnspan=9)
        
        self.area_texto = Text(self.frame, width=45, height=32)
        self.area_texto.grid(column=0,row=2,columnspan=4)
        self.consola = Label(self.frame,width=25, height=32, background="white")
        self.consola.grid(column=6,row=2,columnspan=4)
        ttk.Label(self.frame, text="    ").grid(column=5,row=2)

        self.root.mainloop()

    def abrir(self):
        self.l.cargar_archivo(self.area_texto)

    def analizador(self):
        self.l.analizar_archivo(self.area_texto)