meta = 1000
valor_vendas = [
    ['Juan Thales', 1200],
    ['Juan an', 1000],
    ['Thales Juan', 900],
    ['Thales', 800],

]
print("o valor da meta do mes de julho é de: R$",meta, '\n')
for item in valor_vendas:
    if item[1] > meta:
        print(" vendedor {} bateu a meta, com o valor de vendas de R$ {}".format(item[0], item[1]))
    else:
        print("\n" + 'vendedor {} não bateu a meta, com o valor de vendas de R$ {}'.format(item[0], item[1]))
        