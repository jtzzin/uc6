msg_help = input('--Digite o pedido de ajuda em Morse:')
print(linha)
tabela_morse = ['...---...','S.O.S']
 
if msg_help == tabela_morse[0]:
    print('\n')
    print('O código digitado foi: {} e foi ACEITO!, a mensagem é: {}'.format(msg_help,tabela_morse[1]))
    print(linha)
else:
    print('\n' + linha)
    print('O código NÃO confere com a tabela morse, referente a mensagem: {}'.format(tabela_morse[1]))
    print(linha)