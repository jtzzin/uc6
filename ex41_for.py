produtos = ['PC desktop', 'notebook', 'teclado', 'mouse', 'mousepad']
vendas_2019 = ['1500',     '1300',     '1400',    '1600',  '1210']
vendas_2020 = ['1800',     '1700',     '1600',    '1900',  '1220']

for i, lista_produtos in enumerate(produtos):
    if vendas_2019[i] > vendas_2020[i]:
        crescimento = vendas_2020[i] / vendas_2019[i] - 1
    print('{} vendeu {} unidades em 2019, e em 2020 vendeu {} unidades.'.format(lista_produtos,vendas_2019[i], vendas_2020[i]))
    
