#lugar donde se colocan las librerias que se van a usar durante el programa
# -*- coding: utf-8 -*-
from Tkinter import *
from tkFileDialog import askopenfilename, asksaveasfilename
import tkMessageBox

#Funciones o metodos que se van a llevar acabo para el funcinamiento del programa
	#funcion que permite darle la informacion en la casilla "Acerca de" en el menu de la barra superior 
def informacion():
	tkMessageBox.showinfo("Creado Por","                  Camilo Andres Lopez Sarmiento \n"
							"              Estudiante de Ingenieria electronica\n"
						"Universidad Pedagógica y Tecnológica de Colombia\n"
						"                                 Version 1.0" )

	#funcion que permite salir del programa al oprimir el boton "salir" que se encuentra en el menu de la barra superior en la casilla "Archivo"
def salir():
	quit()

	#funcion que permite abrir un documento o archivo en el programa al oprimir el boton "abrir" que se encuentra en el menu de la barra superior en la casilla "Archivo"
def abrir():
	global texto, textoRuta
	#abir el archivo para mirar los datos de este en la ventana
	archivoruta = askopenfilename(filetypes=[("archivos de texto","*.*")])			
	archivo = open(archivoruta,"r")
	archivotxt = archivo.read()
	archivo.close()
	#funcion que borra los datos de la venta
	texto.delete("1.0",END)
	#funcion que muestra todos los datos del documento que se desea revisar
	texto.insert(END, archivotxt)
	#funcion que nos permite visualizar la ruta en la cual se encuentra el documento
	textoRuta.set(archivoruta)	


	#funcion que permite guardar un documento o archivo en cualquier ruta de mi ordenador al oprimir el boton "Guardar como" que se encuentra en el menu de la barra superior en la casilla "Archivo"
def guardar():
	global texto, textoRuta
	#mensaje de aviso para ciertos parametros antes de guardar
	tkMessageBox.showinfo("IMPORTANTE","Al guardar el documento debe indicar su extencion\nEJEMPLO:\n *.txt , *.py, *.docx\nGracias.")
	#variable que nos permite almacenar el texto de la ventana y poderlo utilizar mejor para guardarlo en un nuevo documento o en el mismo
	t = texto.get("1.0", END) 
	#abir el archivo para sobreescribir los datos de la ventana
	archivoruta = asksaveasfilename(filetypes=[("archivos de texto","*.*")])	
	archivo = open(archivoruta, "w")
	archivotxt = archivo.write(str(t))
	archivo.close()
	#funcion que nos permite visualizar la ruta en la cual se encuentra el documento
	textoRuta.set(archivoruta)	

	#Funcion que borra el contenido y comienza uno nuevo
def nuevo():
	texto.delete("1.0",END)


#Creacion de la ventada en la cual el usuario va a poder interactuar con el programa
root = Tk()

#titulo de la ventana
root.title('Bloc de Notas')

#icono que va a llevar la ventana
icono = root.iconbitmap("block.ico")

#funcion que nos permite que tan grande quiero que sea la ventana ya sea ancha o alta
root.geometry("660x430")

#funcion que nos permite que el usuario NO pueda o SI pueda ampliar la ventana de inicio
root.resizable(width=False, height=False)

#widget que nos va a mostrar la barra de la ubicacion del archivo y los contenidos del archivo que se desa ver
menu1=Frame(root)

#funcion que nos permite colocar el widget en la ventana principal y nos perimite utilizar una barra de desplazamiento vertical
menu1.pack(fill=BOTH)

#creacion del menu de la barra superior
menubar = Menu(root)

#Funciones y creaciones de las opciones del menu de la barra superior
menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Archivo", menu=menu)
menu.add_command(label="Nuevo", command=nuevo)
menu.add_command(label="Abrir",command=abrir)
menu.add_command(label="Guardar como",command=guardar)
menu.add_separator()
menu.add_command(label="SALIR",command=salir)

menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=menu)
menu.add_command(label="Acerca de", command=informacion)

#variable donde se va almacenar la ruta del archivo y luego se podra utilizar en los metodos para ser mostrada al usuario
textoRuta=StringVar()

#primera etiqueta para darle indicaciones o informacion al usuario
etiqueta1=Label(menu1,text="Su archivo se encuentra en: ")
etiqueta1.grid(row=1,column=1,sticky=E)

#widget en el cual el usuario va a poder ver la ruta del archivo y pueda interactuar con esta ya sea copiando o cortando esta
ruta=Entry(menu1,textvariable=textoRuta,width=70)
ruta.grid(row=1,column=2,sticky=W)

#creacion de la barra de desplazamiento vertical, para moverse por el texto o la aplicacion
yscrollbar = Scrollbar(menu1)
yscrollbar.grid(row=1, column=3, rowspan=1000,sticky=NS)

"""creacion del widget de texto donde se van a almacenar todos los datos que el usuario digite y donde se va a poder
	visualizar todo el contenido del documento que el usuario elija, tambien donde el usuario va a interactuar en mayor
	medida con la aplicacion y el documento visualizado o creado"""
texto=Text(menu1,bd=0, yscrollcommand=yscrollbar.set)
texto.grid(row=2,column=1,columnspan=2)

"""Funciones para que el programa funcione correctamente y se puedan configurar la barra de dezplazamiento y el menu de la
	parte superior"""
yscrollbar.config(command=texto.yview)
root.config(menu=menubar)
root.mainloop()