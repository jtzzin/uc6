estoque = [
    ['1000', '2000', '3000', '4000', '5000'],
    ['1100', '2100', '3100', '4100', '5100'],
    ['1200', '2200', '3200', '4200', '5200'],
    ['1300', '2300', '3300', '4300', '5300'],
]
fabricas = ['lex1', 'lex2', 'lex3', 'lex4', 'lex5']
estoque_min = 7000
for i, lista in enumerate(estoque):
    for qtd in lista:
        if qtd < estoque_min:
            print('As empresas com estoque abaixo de:', estoque_min, 'unidades, sao as fabricas:' ,fabricas[i])
        else:
            print('As empresas com estoque acima de:', estoque_min, 'unidades, sao as fabricas:' ,fabricas[i])
            
