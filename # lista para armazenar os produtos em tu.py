# lista para armazenar os produtos em tuplas

produtos = []

def adiconar_produtos(nome, preco, quantidade):
    produto = (nome, preco, quantidade)
    produtos.append(produto)

def exibir_produtos():
    for produto in produtos:
        nome, preco, quantidade = produto
        print(f"produti")
