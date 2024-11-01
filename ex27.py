linha = "--------------"
print(linha + '\n')

meta = 40000
vendas = 45000

if vendas > meta:
    print("meta batida, parábens!!")
elif vendas > (meta * 2):
    bonus = 0.07 * vendas
    print(f"A equipe vendas CORINTHIANS obteve um bonus de R$ {bonus:,.2f}")
else:
    bonus = 0.03 * vendas
    print(f"A equipe timão obteve um bonus de R$ {bonus:,.2f}")

    print('\n' + linha)