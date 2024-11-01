linha = '------------------------------------------------'
import tkinter as Tk
from tkinter import *
 
root1 = Tk()
menu =Menu(root1)
root1.config(menu=menu)
filemenu= Menu(menu)
menu.add_cascade(label='Arquivo', menu= filemenu)
filemenu.add_command(label='Novo')
filemenu.add_command(label='abrir')
filemenu.add_separator()
filemenu.add_command(label='sair', command= root1.quit)
helpmenu = Menu(menu)
menu.add_cascade(label='Ajuda', menu=helpmenu)
helpmenu.add_command(label='sobre')
mainloop()