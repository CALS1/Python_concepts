# -*- coding: cp1252 -*-
import random
from Tkinter import *
def pantalla():
        for i in range(0,9):
            for y in range(0,9): 
                entradax=IntVar()
                numero=Entry(sudoku,textvariable=entradax,width=10).grid(row=i,column=y)
                entradax.set('')
            for i in range(0,3):
                for y in range(3,6): 
                    numero=Entry(sudoku,textvariable=entradax,width=10,background="gray").grid(row=i,column=y)
            for i in range(3,6):
                for y in range(0,3): 
                    numero=Entry(sudoku,textvariable=entradax,width=10,background="gray").grid(row=i,column=y)
            for i in range(3,6):
                for y in range(6,9): 
                    numero=Entry(sudoku,textvariable=entradax,width=10,background="gray").grid(row=i,column=y)
            for i in range(6,9):
                for y in range(3,6): 
                    numero=Entry(sudoku,textvariable=entradax,width=10,background="gray").grid(row=i,column=y)
sudoku = Tk()
sudoku.geometry("578x200+100+100")
sudoku.title("sudoku")
boton1=Button(sudoku,text="Jugar",font=("Arial",10),width=5).grid(row=10,column=0)
boton2=Button(sudoku, text="Pause", font=("Arial", 10), width=5,fg="red").grid(row=10, column=2)
buton3=Button(sudoku, text="tiempo", font=("Arial", 10), width=5, fg="blue").grid(row=10, column=4)
boton4=Button(sudoku, text="salir", font=("Arial", 10), width=5, fg="red").grid(row=10, column=6)
boton5=Button(sudoku, text="despausar", font=("Arial", 10), width=5, fg="green").grid(row=10, column=5)

pantalla()
sudoku.mainloop()