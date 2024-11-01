from tkinter import ttk
from tkinter import Tk
 
root = Tk()
frm = ttk.Frame(root, padding=10)
root.title(' uaaaa')
frm.grid()
ttk.Label(frm, text='olá mundo ->').grid(column=0,row=0)
ttk.Button(frm, text='fechar',command= root.destroy).grid(column=1,row=0)
root.mainloop()
 
linha = '------------------------------------------------'
 
import tkinter as tk
class App(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.pack()
 
        self.entrythingy =tk.Entry()
        self.entrythingy.pack()
 
        self.contents = tk.StringVar()
        self.contents.set('Apagar>Digite>Enter')
        self.entrythingy["textvariable"] = self.contents
 
        self.entrythingy.bind('<Key-Return >',
        self.print_contents)
 
    def print_contents(self,event):
        print('A palavra que digitou é:',
              self.contents.get())
       
root = tk.Tk()
myapp = App(root)
myapp.mainloop()
 
linha = '------------------------------------------------'
import tkinter as tk
from tkinter import *
 
master = Tk()
var1 = IntVar()
Checkbutton(master, text='masculino', variable=var1).grid(row=0,sticky=W)
var2 = IntVar()
Checkbutton(master, text='Feminino', variable=var2).grid(row=1,sticky=W)
mainloop()
 
linha = '------------------------------------------------'
 
import tkinter as Tk
from tkinter import *
master1 = Tk()
Label(master1, text='Nome:').grid(row=0)
Label(master1, text='sobrenome:').grid(row=1)
e1 = Entry(master1)
e2 = Entry(master1)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
mainloop()
 
linha = '------------------------------------------------'
 
import tkinter as Tk
from tkinter import *
 
top = Tk()
lb = Listbox(top)
lb.insert(1,'Python')
lb.insert(2,'Java')
lb.insert(3,'C++')
lb.insert(4,'PHP')
lb.insert(5,'C#')
lb.insert(6,'R')
lb.pack()
top.mainloop()
 
linha = '------------------------------------------------'
from tkinter import *
top1= Tk()
mb= Menubutton(top1, text='Menu principal')
mb.grid()
mb.menu = Menu(mb, tearoff=0)
mb['menu'] = mb.menu
cVar = IntVar()
aVar = IntVar()
mb.menu.add_checkbutton(label='contato', variable= cVar)
mb.menu.add_checkbutton(label='sobre', variable= aVar)
mb.pack()
top1.mainloop()