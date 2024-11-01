produtos = ['coca cola', 'fanta uva', 'pepsi', 'limonada']
producao = ['15000', '12000', '11000', '10000']

qtd = len(produtos)
for indices in range(qtd):
    print("o produto: {} -> foi fabricado: {} unidades em 18/09/2024".format(produtos[indices], producao[indices]))
    