from Tkinter import *


ventana=Tk()
ventana.title("ejercicio 3")
ventana.geometry("400x200")
imagen = PhotoImage(file="12.gif")
fondo=Label(ventana, image=imagen).place(x=0, y=0)
boton=Button(ventana, text="jeje"). place(x=50, y=100)
ventana.mainloop()