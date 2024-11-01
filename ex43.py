vendas = [100, 150, 1500, 2000, 120]
loja = ['Barao geraldo', 'pipolanche do juan', 'ponto do caps', 'esquina do bairro']
meta = 1300

for lista_vendas in vendas:
    if lista_vendas < meta:
        print('a loja do bairro:', loja[3] + ', bateu a meta')
        break
