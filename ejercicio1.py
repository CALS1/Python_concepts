from Tkinter import *
import time

def parpadear():
	ventana.iconify()
	time.sleep(3)
	ventana.deiconify()

ventana=Tk()
ventana.title("introduccion")
boton=Button(ventana, text="hey", command=parpadear)
boton.pack()
ventana.mainloop()
