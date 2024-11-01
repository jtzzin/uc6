'''
projeto 1° - Calculadora com python e Tkinter com layout insirado no estilo "PyPhone"
esta aplicação cria uma calculadora simples usando o modelo tkinter.
ela permite ao usuario realizar operações básicas como adição, subtração, multiplicação e divisão
'''

# importando o modulo tkinter para criar a interface grafica (GUI)
import tkinter as tk

# função que será chamada quando o usuario clicar em um botão da calculadora
def click(event):
    #captura o texto do botão que foi clicado
    text = event.widget.cget('text')
    
    # verifica se o botão clicado foi "=" (para calcular o resultado)
    if text == "=":
        try:
            # avalia a expressão contida na tela (usando eval)
            result = eval(screen.get())
            screen.set(result) # exibe o resultado na tela
        except Exception as e:
            # caso haja erro na expressão (ex: divisão por zero), exibe "Erro" na tela
            screen.set("Erro")
    # Se o botão clicado for "C", limpa a tela da calculadora
    elif text == "c":
        screen.set("")
        
    # caso contrario (para qualquer outro botão), adiciona o texto do botão a expressão na tela
    else:
        screen.set(screen.get() + text)
        
# configuração da janela principal da calculadora
root = tk.Tk() # cria uma nova janela
root.title("calculadora - PyCPhone") # define o titulo da janela
root.geometry("350x500") # define o tamanho da janela (largura x altura)
root.config(bg='#F0F0F0') # configura a cor do fundo da janela (cinza claro, estilo windows)

# variavel para armazenar o texto que sera exibido na tela da calculadora
screen = tk.StringVar()

# caixa de entrada onde as expressões e resultados serão exibidos
entry = tk.Entry(root, textvar=screen, font="Arial 24", bd=10, insertwidth=2, width=14, justify='right')
# configura a aparencia da caixa de entrada (fonte, borda, alinhamento a direita)
entry.pack(fill='both', ipadx=8, padx=10, pady=20) # posiciona a caixa na interface

# lista de botões da calculadoora, organizados por linha
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['c', '0', '=', '+']
]

# função para criar os botões com o estilo especifico
def create_button(frame, text, color='#FFFFFF', bg='#C0C0C0'):
    # cria um botão com o texto, cor do texto, cor do fundo e estilo desejado
    button = tk.Button(frame, text=text, font='Arial 20', padx=20, pady=20, bg=bg, fg=color, borderwidth=0)
   # posiciona o botão no frame (linha) e ajusta o tamanho para preencher o espaço disponivel
    button.pack(side='left', expand=True, fill='both', padx=5, pady=5)
    # associa a função click ao evento de cliqye do botão
    button.bind('<Button-1>', click)
    return button

# laço para criar e organizar os botões na interface
for row in buttons:
        # cria um frame (Linha) para organizar os botões da calculadora
    frame = tk.Frame(root, bg='#F0F0F0') # cor de fundo similar a calculadora do windows
    frame.pack(expand=True, fill='both') # ajusta o frame para preencher o espaço disponivel
    
    # para cada botão na linha, cria o botão com as cores e comportamentos apropriados
for row in buttons:
    frame = tk.Frame(root,bg="#F0F0F0")
    frame.pack(expand=True,fill="both")
    for button_text in row:
        if button_text in ["+","+","*","/","="]:
            create_button(frame,button_text,color="#FFFFFF", bg="#FFA500")
        elif button_text == "c":
            create_button(frame,button_text, color="#FFFFFF", bg="#FF6347")
        else:
            create_button(frame,button_text)
 
root.mainloop()
 
        