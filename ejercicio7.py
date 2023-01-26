from Tkinter import *
import tkMessageBox
 
def pregunta():
    tkMessageBox.showwarning("mensaje", "tu seleccionaste:   "+ valor.get())

ventana=Tk()
valor=StringVar()
ventana.title("ejercicio 7")
ventana.geometry("400x300")
etiqueta=Label(ventana, text="ejemplo de Spinbox   "). place(x=20, y=10)
combo=Spinbox(ventana,values=("1","2", "3", "4", "5")). place(x=20, y=50)
etiqueta2=Label(ventana, text="ejemplo 2 de Spinbox"). place(x=20, y=100)
combo2=Spinbox(ventana, from_=1, to=10, textvariable=valor). place(x=20, y=150)
boton=Button(ventana,text="obtener calor Spinbox", command=pregunta).place(x=20, y=190)
mainloop()