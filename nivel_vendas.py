mobile = ['moto g1', 'moto g2', 'motog3', 'motog4']
qtd = [    100,       200,       300,      400]

prod_ma_v = max(qtd)
prod_me_v = min(qtd)

produtos = prod_ma_v and prod_me_v

if prod_ma_v < prod_me_v:
    print('o produto com venda em nivel otimo foi: {}'.format(produtos))

elif prod_ma_v < prod_me_v:
    print("o produto com venda em nivel BOM foi: {}".format(produtos))
else:
    print("o produto com venda em nivel RUIM foi: {}".format(produtos))