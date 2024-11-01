produto = input("\n" + "insira o nome de um equipamento eletronico: ")
produtos = ["celualr", "computador", "monitor", "placa de video", "processador"]
estoque =  [100,        200,          300,       400,              500]

if produto in produtos:
    i = produtos.index(produto)
    qtd_estoque = estoque[i]
    print("\n" + "a quantidade do produto: {} em estoque é de: {} unidades.".format(produto, qtd_estoque))
else:
    print("\n" + "-- ATENÇÃO!!-- O produto {} não existe em nosso estoque".format(produto))
    