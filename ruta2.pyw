# -*- coding: utf-8 -*-
from Tkinter import *
from tkFileDialog import askopenfilename, asksaveasfilename


def abrir():
	global texto, textoRuta
	archivoruta = askopenfilename(filetypes=[("archivos de texto","*.txt")])
	#archivoruta = asksaveasfilename(filetypes=[("archivos de texto","*.txt")],
	print archivoruta
	archivo = open(archivoruta, "r")
	archivotxt = archivo.read()
	archivo.close()
	texto.insert(END, archivotxt)
	textoRuta.set(archivoruta)	



ventana=Tk()

miFrame=Frame(ventana)
miFrame.pack()

boton1=Button(miFrame,text="Mostrar ruta",command=abrir)
boton1.grid(row=1,column=1)

textoRuta=StringVar()
ruta=Entry(miFrame,textvariable=textoRuta,width=70)
ruta.grid(row=1,column=2)

texto=Text(miFrame)
texto.grid(row=2,column=1,columnspan=2)

ventana.mainloop()