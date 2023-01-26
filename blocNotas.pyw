from Tkinter import *

class AppUI(Frame):

	def __init__(self, master=None):
		Frame.__init__(self, master, relief=SUNKEN, bd=2)

		self.menubar = Menu(self)

		menu = Menu(self.menubar, tearoff=0)
		self.menubar.add_cascade(label="File", menu=menu)
		menu.add_command(label="Nuevo")
		menu.add_command(label="Abrir", command=abrir)
		menu.add_command(label="Guardar como", command=abrir)
		menu.add_command(label="Salir",command=exit)

		menu = Menu(self.menubar, tearoff=0)
		self.menubar.add_cascade(label="Help", menu=menu ,command=informacion)
		menu.add_command(label="acerca de")
		
		self.master.config(menu=self.menubar)

		self.canvas = Canvas(self, bg="white", width=400, height=400,
							 bd=0, highlightthickness=0)
		self.canvas.pack()

	def informacion(self):
		pass


	def exit(self):
	
		self.quit()

	def abrir():
		global texto, textoRuta
		archivoruta = abrirArchivo(filetypes=[("archivos de texto","*.txt")])
				
		archivo = open(str(archivoruta), "r")
		archivotxt = archivo.read()
		archivo.close()
		texto.insert(END, archivotxt)
		textoRuta.set(archivoruta)	


	def Guardar():
	global texto, textoRuta
	archivoruta = asksaveasfilename(filetypes=[("archivos de texto","*.txt")])
	
	archivo = open(str(archivoruta), "w")
	archivotxt = archivo.write()
	archivo.close()
	texto.insert(END, archivotxt)
	textoRuta.set(archivoruta)	


root = Tk()

app = AppUI(root)
app.pack()

root.mainloop()