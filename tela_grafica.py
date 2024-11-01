from tkinter import ttk
from tkinter import Tk
 
root = Tk()
frm = ttk.Frame(root, padding=10)
root.title(' uaaaa')
frm.grid()
ttk.Label(frm, text='olá mundo ->').grid(column=0,row=0)
ttk.Button(frm, text='fechar',command= root.destroy).grid(column=1,row=0)
root.mainloop()