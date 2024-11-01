# exemplo de erro em abertura de arquivo inexistente
with open('aequivo.txt', 'r') as file_object:
    texto = file_object.read()
    print(texto)


''' agora, o tratamento do erro '''
try:
    arquivo = open('arquivo.txt')
except FileNotFoundError as erro:
    print(f"o arquivo .TXT não foi encontrado no diretorio de projetos \n"
          f"{erro}")

with open('arquivo.txt', 'r') as file_object:
    texto = file_object.read()
    print(texto)
          