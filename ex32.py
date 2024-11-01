vendas = [1300, 900, 700, 500, 400, 300, 1200]
meta = 1000

contador = 0
for maior_venda in vendas:
    if maior_venda >= meta:
        contador += 1
print('\n' + "a quantidade de vendedores que bateram a meta foi de:", '\n')
print('apenas', contador, 'bateram a meta de vendas em julho de 2024')
