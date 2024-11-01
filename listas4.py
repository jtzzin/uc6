msg1 = " o indice do produto é:"
msg2 = "e o item da lista é:"
msg3 = "a quantidade desse produto é:"

produtos = ["celular", "computador", "monitor", "placa de video", "processador"]
estoque =  [100,        200,          300,       400,              500]

i = produtos.index("celular")
print("\n" + msg1, i, msg2, produtos[i], msg3, estoque[i])
