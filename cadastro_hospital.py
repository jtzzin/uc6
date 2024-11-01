import tkinter as tk
from tkinter import messagebox, ttk
import csv
import os

# função para salvar os dados no arquivo CSV
def salvar_dados():
    nome = entry_nome.get()
    data_nas = entry_data_nasc.get()
    sexo = entry_sexo.get()
    cpf = entry_cpf.get()
    telefone = entry_telefone.get()
    endereco = f"{entry_rua.get()}, {entry_numero.get()}, {entry_bairo.get()}, {entry_cidade.get()}, {entry_estado.get()}, {entry_cep.get()}"
    email = entry_email.get()
    plano_saude = var_plano_saude.get()
    nome_plano = entry_nome_plano.get() if plano_saude == "sim" else "nao aplicavel"
    numero_plano = entry_numero_plano.get() if plano_saude == "sim" else "na aplicavel"
    data_consulta = entry_data_consulta.get()
    historico_medico = entry_historico_medico.get("1.0", tk.END).strip()
    alergias = var_alergia.get()
    descri_alergia - entry_descri_alergia.get() if alergias == "sim" else "nenhuma"
    obs = entry_obs.get("1.0", tk.END).strip()
    
    if not nome or cpf:
        messagebox.showinfo("erro", "nome e cpf são obrigatorios!")
        return
    
    arquivo_csv = "pacientes.csv"
    file_exists = os.path.isfile(arquivo_csv)
    
    with open(arquivo_csv, mode="a", newline='', encoding='utf-8') as file:
        escritor_csv = csv.writer(file)
        if not file_exists:
            escritor_csv.writerow(['nome', 'data de nascimento', 'sexo', 'cpf', 'telefone', 'endereço', 'email', 'plano de saude', 'nome do plano', 'numero do plano', 'data da primeira consulta', 'historico medico', 'alergias', 'descrição alergias', 'observações'])
            escritor_csv.writerow([nome, data_nasc, sexo, cpf, telefone, endereco, email, plano_saude, nome_plano, numero_plano, data_consulta, historico_medico, alergias, descri_alergias, obs])
    messagebox.showinfo("sucesso", "paciente cadastrado com sucesso!")
    limpar_campos()

# função para limpar os campos
def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_data_nasc.delete(0, tk.END)
    entry_cpf.delete(0, tk.END)
    entry_telefone.delete(0, tk.END)
    entry_rua.delete(0, tk.END)
    entry_bairro.delete(0, tk.END)
    entry_cidade.delete(0, tk.END)
    entry_estado.delete(0, tk.END)
    entry_cep.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_nome_plano.delete(0, tk.END)
    entry_numero_plano.delete(0, tk.END)
    entry_data_consulta.delete(0, tk.END)
    entry_historico.delete("1.0", tk.END)
    entry_desc_alergia.delete(0, tk.END)
    entry_obs.delete("1.0", tk.END)
    
# função para fechar a janela
def fechar_janela():
    janela.destroy()
    
# criando a janela principal
janela = tk.Tk()
janela.title("cadastro de pacientes - consultorio medico")
janela.geometry("650x750")
 
#Estilos e Layout
style = ttk.Style()
style.configure('TButton',font=('arial',10))
style.configure('TLabel',font=('arial',10))
 
#Variáveis de controle
var_sexo = tk.StringVar(value="masculino")
var_plano_saude = tk.StringVar(value="não")
var_alergia = tk.StringVar(value="não")
 
#Criar frame principal para espaçamento
frame_principal =ttk.Frame(janela,padding="10 10 10 10")
frame_principal.grid(row=0,column=0, sticky="nsew")
 
#Configurar grid layout para expandir
janela.columnconfigure(0, weight=1)
janela.rowconfigure(0,weight=1)
 
#Campos de entrada e seus respectivos rótulos
ttk.Label(frame_principal,text="nome Completo:").grid(row=0,column=0,sticky='w')
entry_nome = ttk.Entry(frame_principal)
entry_nome.grid(row=0,column=1,columnspan=2,sticky='ew',padx=5,pady=5)
 
ttk.Label(frame_principal,text="Data de Nascimento").grid(row=1,column=0,sticky='w')
entry_data_nasc = ttk.Entry(frame_principal)
entry_data_nasc.grid(row=1,column=1,columnspan=2,sticky='ew',padx=5,pady=5)
 
ttk.Label(frame_principal,text="sexo:").grid(row=2,column=0,sticky='w')
ttk.Radiobutton(frame_principal,text="masculino",variable=var_sexo,value="masculino").grid(row=2,column=1,sticky='w')
ttk.Radiobutton(frame_principal,text="feminino",variable=var_sexo,value="feminino").grid(row=2,column=2,sticky='w')
 
ttk.Label(frame_principal,text="CPF:").grid(row=3,column=0,sticky='w')
entry_cpf =ttk.Entry(frame_principal)
entry_cpf.grid(row=3,column=1,columnspan=2,sticky='ew',padx=5,pady=5)
 
ttk.Label(frame_principal,text="telefone").grid(row=4,column=0,sticky='w')
entry_telefone =ttk.Entry(frame_principal)
entry_telefone.grid(row=4,column=1,columnspan=2,sticky='ew',padx=5,pady=5)
 
ttk.Label(frame_principal,text="endereço").grid(row=5,column=0,sticky='w')
entry_rua =ttk.Entry(frame_principal)
entry_rua.grid(row=5,column=1,columnspan=2,sticky='ew',padx=5,pady=5)
entry_numero =ttk.Entry(frame_principal,width=5)
entry_numero.grid(row=5,column=3,sticky='w',padx=5)
ttk.Label(frame_principal,text="Nº").grid(row=5,column=2,sticky='e')
 
entry_bairro = ttk.Entry(frame_principal)
entry_bairro.grid(row=6,column=1,sticky='ew',padx=5,pady=5)
ttk.Label(frame_principal,text="bairro:").grid(row=6,column=2,sticky='w')
 
entry_cidade = ttk.Entry(frame_principal)
entry_cidade.grid(row=6,column=3,sticky='ew',padx=5)
ttk.Label(frame_principal,text="cidade").grid(row=6,column=2,sticky='e')
 
entry_estado = ttk.Entry(frame_principal)
entry_estado.grid(row=7,column=1,sticky='ew',padx=5,pady=5)
ttk.Label(frame_principal,text="estado:").grid(row=7,column=0,sticky='w')
 
entry_cep = ttk.Entry(frame_principal)
entry_cep.grid(row=7,column=3,sticky='ew',padx=5)
ttk.Label(frame_principal,text="CEP:").grid(row=7,column=2,sticky='e')
 
ttk.Label(frame_principal,text="E-mail:").grid(row=8,column=0,sticky='w')
entry_email = ttk.Entry(frame_principal)
entry_email.grid(row=8,column=1,columnspan=2,sticky='ew',padx=5,pady=5)
 
ttk.Label(frame_principal,text='Plano de saude:').grid(row=9,column=0,sticky='w')
ttk.Radiobutton(frame_principal,text="sim",variable=var_plano_saude,value="sim").grid(row=9,column=1,sticky='w')
ttk.Radiobutton(frame_principal,text="não",variable=var_plano_saude,value="não").grid(row=9,column=2,sticky='w')
 
ttk.Label(frame_principal,text="nome do plano:").grid(row=10,column=0,sticky='w')
entry_nome_plano = ttk.Entry(frame_principal)
entry_nome_plano.grid(row=10,column=1,columnspan=2,sticky='ew',padx=5,pady=5)
 
ttk.Label(frame_principal,text="numero do plano:").grid(row=11,column=0,sticky='w')
entry_numero_plano = ttk.Entry(frame_principal)
entry_numero_plano.grid(row=11,column=1,columnspan=2,sticky='ew',padx=5,pady=5)
 
ttk.Label(frame_principal,text="data da primeira consulta:").grid(row=12,column=0,sticky='w')
entry_data_consulta = ttk.Entry(frame_principal)
entry_data_consulta.grid(row=12,column=1,columnspan=2,sticky='ew',padx=5,pady=5)
 
ttk.Label(frame_principal,text="historico medico:").grid(row=13,column=0,sticky='w')
entry_historico = ttk.Entry(frame_principal)
entry_historico.grid(row=13,column=1,columnspan=2,padx=5,pady=5)
 
ttk.Label(frame_principal,text='alergias:').grid(row=14,column=0,sticky='w')
ttk.Radiobutton(frame_principal,text="sim",variable=var_alergia,value="sim").grid(row=14,column=1,sticky='w')
ttk.Radiobutton(frame_principal,text="não",variable=var_alergia,value="não").grid(row=14,column=2,sticky='w')
 
ttk.Label(frame_principal,text="descrição alergias:").grid(row=15,column=0,sticky='w')
entry_desc_alergia = ttk.Entry(frame_principal)
entry_desc_alergia.grid(row=15,column=1,columnspan=2,sticky='ew',padx=5,pady=5)
 
ttk.Label(frame_principal,text="observações:").grid(row=16,column=0,sticky='w')
entry_obs = tk.Text(frame_principal,height=4,width=40)
entry_obs.grid(row=16,column=1,columnspan=3,padx=5,pady=5)
 
#Botões
btn_salvar = ttk.Button(frame_principal,text="salvar",command=salvar_dados)
btn_salvar.grid(row=17,column=1,pady=10)
 
btn_fechar = ttk.Button(frame_principal,text="fechar",command=fechar_janela)
btn_fechar.grid(row=17,column=2,pady=10)
 
#Iniciar a janela
janela.mainloop()
     

    