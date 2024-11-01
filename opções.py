from tkinter import *
from tkinter .ttk import *

window = Tk()
window.title("--gerador de opções--")

selected = IntVar()

indice = '\n' + 'a opção é a numero:'

rad1 = Radiobutton(window,text='opção 1', value=1, variable=selected)
rad2 = Radiobutton(window,text='opção 2', value=1, variable=selected)
rad3 = Radiobutton(window,text='opção 3', value=1, variable=selected)

def clicked ():
    print(indice, selected.get())
btn = Button(window, text=' clique na sua escolha ', command=clicked)

rad1.grid(column=0, row=0)
rad2.grid(column=1, row=0)
