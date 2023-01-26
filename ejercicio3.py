from Tkinter import *

ventana=Tk()
ventana.title("ejercicio 3")
ventana.geometry("400x200")
botonS=Button(ventana, text="posicion diferente").place(x=10, y=10)
etiqueta=Label(ventana, text="posicion diferente"). place(x=200, y=10)
etiqueta2=Label(ventana, text="posicion diferente"). place(x=10, y=40)
boton2=Button(ventana, text="imprimir", fg="blue").place(x=200, y=40)
ventana.mainloop()