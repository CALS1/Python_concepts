from Tkinter import *
import ttk

ventana=Tk()
notebook=ttk. Notebook(ventana)
notebook.pack(fill="both", expand="yes")
pes0=ttk.Frame(notebook)
pes1=ttk.Frame(notebook)
notebook.add(pes0,text="titulo 1")
notebook.add(pes1,text="titulo 2")
ventana.geometry("300x300")
ventana.mainloop()