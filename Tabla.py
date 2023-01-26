# -*- coding: utf-8 -*-
import sqlite3
import os

id=0
def crearTabla ( ):

	con=sqlite3.connect("C:\Users\parce_000\Desktop\clase 09-04\Tabla")
	cursor = con.cursor()

	print u"\nLa base de datos se abrio correctamente"

	cursor.execute('''CREATE TABLE PERSONAS
		(ID INT PRIMARY KEY   NOT NULL,
		CEDULA          INT   NOT NULL,
		NOMBRE          TEXT  NOT NULL,
		APELLIDO        TEXT  NOT NULL,
		EDAD            INT   ,
		DIRECCION       CHAR(50),
		TELEFONO        INT)''')

	print u"Tabla creada con éxito\n"
	con.close()

def insertarPersonas ():
	global id
	while True:
		os.system("cls")
		print "\n1. Agregar una persona \n2. Salir"
		op=input("\nEliga una opcion: ")
		print u"\nNOTA: No utilizar tildes ni cualquier otro caracter especial ejemplo: (Ó, Ü, á, é, í, ú, ü)\n"
		if op==1:
			con=sqlite3.connect("C:\Users\parce_000\Desktop\clase 09-04\Tabla")
			cursor = con.cursor()
			print u"\nLa base de datos se abrió correctamente\n "
			id+=1
			ced=raw_input("Digite su numero de Cedula: ")		
			nom=raw_input("Digite su primer Nombre: ")
			ape=raw_input("Digite su primer Apellido: ")
			edad=raw_input("Digite su Edad: ")
			print u"\nDigite su Dirección separada por guiones ( - ), \nEjemplo: Carrera-12-numero-34-56...\n"
			dirc=raw_input()
			tel=raw_input("Digite su numero de telefono: ")

			cursor.execute('''INSERT INTO PERSONAS(ID, CEDULA, NOMBRE, APELLIDO, EDAD, DIRECCION, TELEFONO) \
			                VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s')'''%(id, ced, nom, ape, edad, dirc, tel))
			con.commit()
		
			print "\nSe guardo correctamente"
			con.close()
			os.system("pause")
		elif op==2:
			break
		else:
			print u"No es una opción"

def listarPersonas ():
	os.system("cls")
	con=sqlite3.connect("C:\Users\parce_000\Desktop\clase 09-04\Tabla")
	cursor = con.cursor()
	print u"\nLa base de datos se abrió correctamente\n "
	cursor.execute("SELECT ID, CEDULA, NOMBRE, APELLIDO, EDAD, DIRECCION, TELEFONO FROM PERSONAS")

	for i in cursor:
		print u"ID = %s"%(i[0])
		print u"CÉDULA = %s"%(i[1])
		print u"NOMBRE = %s"%(i[2])
		print u"APELLIDO = %s"%(i[3])
		print u"EDAD = %s"%(i[4])
		print u"DIRECCIóN = %s"%(i[5])
		print u"TELéFONO = %s\n"%(i[6])

	print u"operación satisfactoria\n"

	con.close()
	os.system("pause")

while True:
	os.system("cls")
	print "\n 1. Crear Tabla\n 2. Insertar Personas\n 3. Listar Personas\n 4. Salir\n "
	menu=input("\nEliga una opcion: ")
	if menu==1:
		crearTabla()
	elif menu==2:
		insertarPersonas()
	elif menu==3:
		listarPersonas()
	elif menu==4:
		break
	else:
		print u"no es una opción"



