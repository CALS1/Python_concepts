from Tkinter import *
import tkMessageBox


def saludar():
	tkMessageBox.showwarning("Saludo", "Hola "+nombre.get() + " "+ apellidopaterno.get() + " "+ apellidomaterno.get())

ventana=Tk()
nombre=StringVar()
apellidopaterno=StringVar()
apellidomaterno=StringVar()
nombre.set("escribe tu nombre")
ventana.title("ejercicio 3")
ventana.geometry("400x200")
etiqueta1=Label(ventana, text="escribe tu nombre:   "). place(x=10, y=10)
nombreCaja=Entry(ventana, textvariable=nombre). place (x=120, y=10)
etiqueta2=Label(ventana, text="escribe tu apellido paterno:   "). place(x=10, y=40)
apellidopaternoCaja=Entry(ventana, textvariable=apellidopaterno). place (x=170, y=40)
etiqueta3=Label(ventana, text="escribe tu apellido materno:   "). place(x=10, y=70)
apellidomaternoCaja=Entry(ventana, textvariable=apellidomaterno). place (x=170, y=70)
boton=Button(ventana, text="Saludo personalizado", command=saludar). place(x=10, y=100)
ventana.mainloop()