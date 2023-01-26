from Tkinter import *


def suma():
	n1=int(verCampo1.get())
	n2=int(verCampo2.get())
	r=n1+n2
	verCampoResultado.set(r)
def resta():
	n1=int(verCampo1.get())
	n2=int(verCampo2.get())
	r=n1-n2
	verCampoResultado.set(r)
def multiplicacion():
	n1=int(verCampo1.get())
	n2=int(verCampo2.get())
	r=n1*n2
	verCampoResultado.set(r)
def division():
	n1=float(verCampo1.get())
	n2=float(verCampo2.get())
	r=n1/n2
	verCampoResultado.set(r)


ventana=Tk()

numeros=Frame()
numeros.pack()

etiqueta1=Label(numeros, text="NUMERO 1")
etiqueta1.grid(row=1 , column=1)
etiqueta2=Label(numeros, text="NUMERO 2")
etiqueta2.grid(row=2 , column=1)

verCampo1=StringVar()
campo1=Entry(numeros, textvariable=verCampo1)
campo1.grid(row=1 , column=2)

verCampo2=StringVar()
campo2=Entry(numeros, textvariable=verCampo2)
campo2.grid(row=2 , column=2)

operaciones=Frame().pack()

botonSuma=Button(operaciones, text=" + " ,width=20, command=suma)
botonSuma.grid(row=1, column=1)

botonResta=Button(operaciones, text=" - " ,width=20,command=resta)
botonResta.grid(row=1, column=2)

botonMultiplicacion=Button(operaciones, text=" x " ,width=20,command=multiplicacion)
botonMultiplicacion.grid(row=2, column=1)

botonDivision=Button(operaciones, text=" / " ,width=20,command=division)
botonDivision.grid(row=2, column=2)

resultado=Frame().pack()

etiqueta3=Label(resultado, text="Resultado")
etiqueta3.grid(row=1, column=1)

campoResultado=Entry()
campoResultado.grid(row=1, column=2)

verCampoResultado=StringVar()
campoResultado=Entry(resultado,textvariable=verCampoResultado)
campoResultado.grid(row=1,column=2)

ventana.mainloop()






		
