produtos= ['moto g1', 'moto g2', 'motog3', 'motog4']
vendas =  [    100,       200,       300,      400]
prod_ma_v = max(vendas)

p = vendas.index(prod_ma_v)
prod_ma_v = produtos [p]

v = produtos.index(prod_ma_v)
verif_ma_v = vendas [v]

print("quantidade do produto mais vendido foi {} unidades da motorola e o modelo mais vendido foi: {} ".format(verif_ma_v, prod_ma_v))

