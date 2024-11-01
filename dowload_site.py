from tkinter import *
from tkinter.ttk import *
root2= Tk()
progress = Progressbar(root2, orient= HORIZONTAL,
                       length=100,mode='determinate')
root2.title('--Instalação do software zyz--')
def bar():
    import time
    progress['value'] = 20
    root2.update_idletasks()
    time.sleep(1)
 
    progress['value'] = 40
    root2.update_idletasks()
    time.sleep(1)
 
    progress['value'] = 50
    root2.update_idletasks()
    time.sleep(1)
 
    progress['value'] = 60
    root2.update_idletasks()
    time.sleep(1)
 
    progress['value'] = 80
    root2.update_idletasks()
    time.sleep(1)
    progress['value'] = 10
 
progress.pack(pady=10)
Button(root2,text= '--instalar--',command= bar).pack(pady=10)
mainloop()
