qtd_c = 700
qtd_p = 700
valor_c = 3.50
valor_p = 3.30
investimento = 8000
linha = "-----------------------"

print('\n' + linha)
print(f"O total de vendas de latas da coca-cola foram de: R$ {qtd_c * valor_c:,.2F}")
print(f"O total de vendas de latas da Pepsi foram de: R$ {qtd_p * valor_p:,.2f}")
print('\n' + linha)
faturamento = (qtd_c * valor_c) + (qtd_p * valor_p)
print('\n' + linha)

print(f"O faturamento de latas de refrigerantes, somados, são de: R$ {investimento - faturamento:,.2f}" + '\n')

if investimento > faturamento:
    print("A empresa levou prejuizo nas vendas! ")
    print('\n' + linha)
else:
    print('\n' + linha)
    print("A empresa obteve lucros sobre as vendas! ")


