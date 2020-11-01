from tkinter import *
raiz=Tk()
raiz.title("profundidades")
raiz.iconbitmap("escafandra.ico")

opciones=Frame(raiz, width=100, height=100)
opciones.pack()

imagen=PhotoImage(file="busqueda profunda.gif")
titulo=Label(opciones, image=imagen)
titulo.grid(row=0,column=0)

class boton():
    def __init__(self,texto,pocicion):
        self.texto=texto
        self.pocicion=pocicion
    def desplega(self):
        self.texto=Button(opciones,text=self.texto)
        self.texto.grid(row=self.pocicion, column=0, pady=5, padx=5)


tutorial=boton("tutorial",1)
tutorial.desplega()

dosj=boton("dos jugadores",2)
dosj.desplega()
tresj=boton("tres jugadores",3)
tresj.desplega()

raiz.mainloop()