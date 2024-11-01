import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
 
def save_cliente_data():
    name = entry_name.get()
    email = entry_email.get()
    phone = entry_phone.get()
 
    if name and email and phone:
        data = f"nome: {name}, email: {email}, telefone: {phone} \n"
        with open("clientes.txt","a") as file:
            file.write(data)
        messagebox.showinfo("Sucesso", "Dados salvos com sucesso!")
        clear_fields()
    else:
        messagebox.showwarning("Aviso", "Todos os campos devem ser preenchidos.")
 
def clear_fields():
    entry_name.delete(0, tk.END)
    entry_email.delete(0,tk.END)
    entry_phone.delete(0,tk.END)
 
def search_cliente():
    search_name = entry_search.get().lower()
    if not search_name:
        messagebox.showwarning("aviso", "Digite um nome para buscar")
        return
    try:
        with open("Clientes.txt", "r") as file:
            found = False
            for line in file:
                if search_name in line.lower():
                    messagebox.showinfo("cliente encontrado", f"dados: {line}")
                    found = True
                    break
            if not found:
                messagebox.showinfo("Cliente não Encontrado", "nenhum cliente encontrado com esse nome")
    except FileNotFoundError:
        messagebox.showwarning("Erro", "O arquivo de clientes não foi encontrado")
 
def apply_style():
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("TButton", font=("Segoe UI",10),padding=6,relief="flat",background="#0078D7",foreground="white")
    style.map("TButton",background=[("active", "#005A9E")])
    style.configure("TLabel", font=("Segoe UI",11), padding=5,background="#F3F3F3", foreground ="#333")
    style.configure("TFrame",background ="#F3F3F3")
 
root = tk.Tk()
root.title("Cadastro de cliente")
root.geometry("440x460")
root.resizable(False,False)
root.configure(bg="#F3F3F3")
 
apply_style()
 
main_frame = ttk.Frame(root, padding=20)
main_frame.pack(expand=True, fill=tk.BOTH)
 
label_name = ttk.Label(main_frame,text="Nome:")
label_name.grid(row=0,column=0,sticky=tk.E, padx=10,pady=10)
entry_name = ttk.Entry(main_frame,width=30)
entry_name.grid(row=0,column=1,pady=10)
 
 
label_email = ttk.Label(main_frame, text="Email:")
label_email.grid(row=1,column=0,sticky=tk.E,padx=10,pady=10)
entry_email = ttk.Entry(main_frame,width=30)
entry_email.grid(row=1,column=1,pady=10)
 
label_phone = ttk.Label(main_frame, text="telefone:")
label_phone.grid(row=2,column=0, sticky=tk.E, padx=10,pady=10)
entry_phone = ttk.Entry(main_frame,width=30)
entry_phone.grid(row=2,column=1,pady=10)
 
save_button = ttk.Button(main_frame, text="salvar",command=save_cliente_data)
save_button.grid(row=3,columnspan=2,pady=20,ipadx=10)
 
separator = ttk.Separator(main_frame,orient="horizontal")
separator.grid(row=4,columnspan=2,sticky="ew",pady=20)
 
label_search = ttk.Label(main_frame,text="Buscar Cliente:")
label_search.grid(row=5,column=0,sticky=tk.E,padx=10,pady=10)
entry_search = ttk.Entry(main_frame,width=30)
entry_search.grid(row=5,column=1, pady=10)
 
search_button = ttk.Button(main_frame,text="buscar", command=search_cliente)
search_button.grid(row=6,columnspan=2,pady=10,ipadx=10)
 
footer_label = ttk.Label(root, text="2024 cadastro de clientes", font=("Segoe UI", 9),background="#F3F3F3", foreground="#666")
footer_label.pack(side=tk.BOTTOM, pady=10)
 
root.mainloop()
