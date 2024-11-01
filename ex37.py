qtd_estoque = [30,40,50,1200,300,800,1500,1900,2000,3500,4500,4100,500]
produto = ['Coca-cola', 'Fanta', 'IT Guaraná', 'Pepsi', 'Agua c/ gás', 'Agua s gás', 'Dolly', 'Velho Barreiro', ' Pinga 51']
estoque_minimo = 50
 
for lista, qtd1 in enumerate(qtd_estoque):
    if qtd1 < estoque_minimo:
        print('O produto {} está abaixo do nível de estoque, temos apenas {}'.format(produto[lista], qtd1), 'unidades.')
 