try:
    arquivo = open('arquivo.txt')
except FileNotFoundError as erro:
    print(f"o arquivo .TXT não foi encontrado no diretorio de projetos \n"
          f"{erro}")

with open('arquivo.txt', 'r') as file_object:
    texto = file_object.read()
    print(texto)

# tratamento do erro de --'arquivo inexistente: FileNotFoundError' -- com TRY e EXCEPT
    