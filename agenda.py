agenda = {}

def adicionar_contato(nome, telefone):
    agenda[nome] = telefone
 

def remover_contato(nome):
    if nome in agenda:
        del agenda[nome]

def buscar_contato(nome):
    telefone = agenda.get(nome)
    if telefone:
        return f"o telefone encontrado foi: {telefone}"
    else:
        return "contato nao econtrado"
    
def exibir_contato():
    for nome, telefone in agenda.items():
        print(f"nome: {nome}, telefone: {telefone}")

# teste
adicionar_contato("juan", "12234-42412")
adicionar_contato("bar do bebo", "4444-0000")
remover_contato("juan")
print(buscar_contato("bar do bebo")) # exibe a msg com o telefone
exibir_contato() # exibe todos os contatos

