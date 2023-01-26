import Tkinter

def salir():
	exit(otra_ventana)

root = Tkinter.Tk()
root.title("Ventana padre")
# Creamos una ventana hija de root
otra_ventana = Tkinter.Toplevel(root)
otra_ventana.title("Ventana hija")
# Este es solo para decoracion
etiqueta = Tkinter.Label(otra_ventana, text='Este es un ejemplo de transient')
etiqueta.pack()

botonSuma=Tkinter.Button(otra_ventana, text="+",width=20,command=salir)
botonSuma.pack()
# Posicionamos las dos ventanas para que sea mas claro el ejemplo
root.geometry("400x400+100+100")
otra_ventana.geometry("200x200+150+150")
# Y ahora si llamamos a este metodo

root.mainloop()



#Creacion de la ventada en la cual el usuario va a poder interactuar con el programa
root = Tk()

#titulo de la ventana
root.title('Bloc de Notas')

#icono que va a llevar la ventana
icono = root.iconbitmap("block.ico")

#funcion que nos permite que tan grande quiero que sea la ventana ya sea ancha o alta
root.geometry("660x430")