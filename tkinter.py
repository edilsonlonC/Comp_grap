#modulo para fraficos
from Tkinter import *
import tkMessageBox
def function():
    tkMessageBox.showinfo("hi world","hi all")
#Create window
window=Tk()
window.geometry('1000x1000')
#event, call window
etiqueta=Label(window,text='Hola ')
etiqueta.pack()
label=Label(window,text="label")
button=Button(window,text='Hello',command=function)
entry=Entry(window)
button.pack()
label.pack()
entry.pack()
window.mainloop()
