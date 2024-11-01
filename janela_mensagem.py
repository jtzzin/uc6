from tkinter import messagebox
from tkinter import *

messagebox.showinfo('Sistema lindão', 'vai corinthians')

window = Tk()
window.title("hahahahahahah")
window.geometry("700x500")

def clicked():
    messagebox.showinfo("sistema lindão", "tim maia")
    
btn = Button(window, text="clique aqui", command=clicked)
btn.grid(column=0, row=0)

window.mainloop()