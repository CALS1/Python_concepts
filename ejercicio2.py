from Tkinter import *

def imprimir():
	print("Acabas de presionar el boton imprimir")

ventana=Tk()
ventana.title("ejercicio 2")
botonS=Button(ventana, text="salir", fg="red", command=quit)
botonS.pack(side=LEFT)
botonI=Button(ventana, text="imprimir", fg="blue", command=imprimir)
botonI.pack(side=RIGHT)
ventana.mainloop()