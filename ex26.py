linha = '--------------'
print(linha + '\n')
faturamento = int(input("Informe o faturamento mensal: "))
print(linha)
custo = int(input("Informe o custo mensal: "))
print(linha)

meta = 3000
print(linha + '\n')
print(f"O valor da venda mensal foi de: R$ {faturamento - custo:.2f}")

if faturamento > custo and meta >= faturamento:
    print(linha + '\n')
    print("A sua empresa está dando lucros! ")
else:
    print("A sua empresa está dando prejuizo! ")
    print(linha + '\n')
    

