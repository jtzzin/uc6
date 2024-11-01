estoque = {}

def adicionar_produtos(nome, quantidade, preco):
    if nome in estoque:
        estoque[nome] ["quantidade"] += quantidade
    else:
        estoque[nome] = {"quantidade": quantidade, "preço": preco}

def remover_produtos(nome):
    if nome in estoque:
        del estoque[nome]

def exibir_estoque():
    for produto, dados in estoque.items():
        preco_formatado = f"R$ {dados['preco']:,.2f}".replace(',' ,'X').replace(',', ',').replace('X', '.')
        print(f"produto: {produto}, quantidade: {dados["quantidade"]}, preço: {preco_formatado}")


# teste
adicionar_produtos("cadeira", 10, 120.00)
adicionar_produtos("mesa", 5, 300.00)
adicionar_produtos("cadeira", 2, 120.00) # atualiza a quantidade de cadeiras
remover_produtos("mesa")
exibir_estoque()
