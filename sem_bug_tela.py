from tkinter import *
from tkinter.ttk import*
 
window1 = Tk()
window1.title("--Bem-Vindo ao APP--Radio")
window1.geometry('350x200')
 
rad1 = Radiobutton(window1, text='Opção A', value=1)
rad2 = Radiobutton(window1, text='Opção B', value=2)
rad3 = Radiobutton(window1, text='Opção C', value=3)
 
rad1.grid(column=0,row=0)
rad2.grid(column=1,row=0)
rad3.grid(column=2,row=0)
 
window1.mainloop()