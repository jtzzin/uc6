# exemplo de listas com indices positivos

lista = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

# exibindo os indices positivos e o valores correspondetes 
print("indices positivos:")
for i in range(len(lista)):
    print(f"indice {i}: {lista[i]}")

# exibindo os valores negativos
print("\nindices negativos:")
for i in range(-1, -len(lista)-1, -1): # indices negativos começam de -1 até -len(lista)
    print(f"indice {i}: {lista[i]}")
        