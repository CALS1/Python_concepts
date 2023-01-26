from Tkinter import *


def suma():
	n1=int(varCampoN1.get())
	n2=int(varCampoN2.get())
	r=n1+n2
	varCampoResultado.set(r)

def resta():
	n1=int(varCampoN1.get())
	n2=int(varCampoN2.get())
	r=n1-n2
	varCampoResultado.set(r)

def multiplicacion():
	n1=int(varCampoN1.get())
	n2=int(varCampoN2.get())
	r=n1*n2
	varCampoResultado.set(r)

def division():
	n1=float(varCampoN1.get())
	n2=float(varCampoN2.get())
	r=n1/n2
	varCampoResultado.set(r)



root=Tk()

numeros=Frame()
numeros.pack()

etiquetaN1=Label(numeros,text="Numero 1")
etiquetaN1.grid(row=1,column=1)
etiquetaN2=Label(numeros,text="Numero 2")
etiquetaN2.grid(row=2,column=1)

varCampoN1=StringVar()
campoN1=Entry(numeros,textvariable=varCampoN1)
campoN1.grid(row=1,column=2)

varCampoN2=StringVar()
campoN2=Entry(numeros,textvariable=varCampoN2)
campoN2.grid(row=2,column=2)



operaciones=Frame()
operaciones.pack()

botonSuma=Button(operaciones, text="+",width=20,command=suma)
botonSuma.grid(row=1,column=1)

botonResta=Button(operaciones, text="-",width=20,command=resta)
botonResta.grid(row=1,column=2)

botonMult=Button(operaciones, text="x",width=20,command=multiplicacion)
botonMult.grid(row=2,column=1)

botonDiv=Button(operaciones, text="/",width=20,command=division)
botonDiv.grid(row=2,column=2)

resultado=Frame()
resultado.pack()

etiquetaResultado=Label(resultado, text="Resultado")
etiquetaResultado.grid(row=1,column=1)
varCampoResultado=StringVar()
campoResultado=Entry(resultado,textvariable=varCampoResultado)
campoResultado.grid(row=1,column=2)


root.mainloop()