vendas = [1300, 900, 700, 500, 400, 300, 1200]
meta = 1000

contador = 0
for maior_venda in vendas:
    if maior_venda >= meta:
        contador += 1
qtd_funcionarios = len(vendas)
print('\n' + 'a porcentagem de funcionarios qu bateram a meta de vendas foram de:')
print('{:.0%}'.format(qtd_funcionarios / contador))
