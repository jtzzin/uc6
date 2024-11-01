cod_bac = 'BAC001'
cod_bsa = 'BSA001'
linha = '---------------------'
print('\n' + linha)

bebida = input("Informe o código do produto em letras maiuscula: ")
if 'BAC' in bebida:
    print('\n' + linha)
    print("Esse é um código de bebida alcoólica e o código do produto é:", cod_bac)
    print(linha)
else:
    print("Esse é o código de bebida sem alcoól e o código é: ", cod_bsa)
    print(linha)



