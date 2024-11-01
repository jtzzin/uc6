faturamento = input("Informe o valor do seu faturamento em R$: ")
custo = input("Informe o valor do seu custo em R$: ")
lucro = 0 

if faturamento == '' and custo == '':
    print('\n' + "preencha os dados corretamentes.")
else:
    print('\n' + "Dados inseridos incorretamentes.")

lucro = int(faturamento) - int(custo)
if faturamento > custo:
    print(f"A empresa obteve lucro neste mês, no valor de R$ {lucro:,.2f} ", sep='.')
else:
    print(f"A empresa obteve prejuizo neste mês, no valor de R$ {lucro:,.2f} ", sep='.')
    
