from Tkinter import *
def Ver():
   print(var.get())
root = Tk()
var = StringVar()
rad0 = chekbutton(root, text="java", variable=var, value="java", command=Ver)

rad0.pack(side=LEFT)


rad1 = chekbutton(root, text="csharp", variable=var, value="csharp", command=Ver)

rad1.pack(side=LEFT)


rad2 = chekbutton(root, text="python", variable=var, value="python", command=Ver)

rad2.pack(side=LEFT)


var.set(' ')

root.mainloop()