def adicao(x, y):
    return x + y
def subtracao(x, y):
    return x - y
def multiplicacao(x, y):
    return x * y
def divisao(x, y):
    return x // y

lo = '------------'
print(lo + '\n' + 'selecione uma das operacoes:' + '\n')
print('1 - Adicao')
print('2-   Subtracao')
print('3 - Multiplicacao')
print('4 - Divisao')
print(lo + '\n')

while True:
    calculo = input("insira uma das opcoes: 1 2 3 ou 4: ")

    if calculo in ('1','2', '3', '4'):
        try:
            num1 = int(input("insira o primeiro numero: "))
            num2 = int(input("insira o segundo numero:" ))
        except ValueError:
            print('\n' + 'o valor inserido é inválido' + '\n')
            continue
        if calculo == '1':
            print(num1, '+',num2, ' => o resultado do calculo é:',adicao(num1, num2))
        elif calculo == '2':
            print(num1,'-',num2, ' => o resultado do calculo é:',subtracao(num1, num2))
        elif calculo == '3':
            print(num1, '*',num2, ' => o resultado do calculo é:',multiplicacao(num1, num2))
        elif calculo == '4':
            print(num1, '//',num2, ' => o resultado do calculo é:',divisao(num1, num2))

        novo_calculo = input("deseja efetuar mais algum calculo? (sim/nao): ")
        if novo_calculo == 'nao':
            break
        else:
            print('\n' + '|--erro--|-- opcao invalida--' + '\n')
            