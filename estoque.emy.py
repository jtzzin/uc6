estoque = {}
 
def adicionar_produto(nome,quantidade,preco):
    if nome in estoque:
        estoque[nome]['quantidade'] += quantidade
    else:
        estoque[nome] = {'quantidade': quantidade, 'preco':preco}
 
def  remover_produto(nome):
    if nome in estoque:
        del estoque[nome]
 
def exibir_estoque():
    for produto,dados in estoque.items():
        preco_formatado = f"R${dados['preco']:,.2f}".replace(',','x').replace('.',',').replace('x','.')
        print(f"Produto:{produto},quantidade: {dados['quantidade']}, preço: {preco_formatado}")
 
 
adicionar_produto('Cadeira',10,120.00)
adicionar_produto('Mesa',5,300.00)
adicionar_produto('cadeira',2,120.00)
remover_produto('mesa')
exibir_estoque()



