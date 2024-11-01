lista_produto = input("insira o produto para cadastro e pressione enter para encerrar o sistema."+ "\n")
insere_lista = []

while lista_produto != '':
    insere_lista.append(lista_produto)
    lista_produto = input("insira um novo produto para cadastro.")
print("cadastro efetuado com sucesso e os produtos cadastrados foram: {}".format(insere_lista))
