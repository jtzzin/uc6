from tkinter import *
from tkinter.ttk import *
 
window2 = Tk()
window2.title("--Gerador de Opçoes--")
 
selected = IntVar()
indice = '\n' + 'A opção escolhida é a numero'
 
rad4 = Radiobutton(window2, text='Opção 1', value=1,variable=selected)
rad5 = Radiobutton(window2, text='Opção 2', value=2,variable=selected)
rad6 = Radiobutton(window2, text='Opção 3', value=3,variable=selected)
 
def clicked():
    print(indice,selected.get())
btn= Button(window2, text='Clique na sua escolha', command=clicked)
 
rad4.grid(column=0,row=0)
rad5.grid(column=1,row=0)
rad6.grid(column=2,row=0)
btn.grid(column=3,row=0)
window2.mainloop()

