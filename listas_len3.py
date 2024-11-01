lista = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

#transformando todos os elementos para minusculas, mesmo que já estejam.
conversor_texto = [letra.lower() for letra in lista]

print("Indices positivos:")
for i in range(len(conversor_texto)):
    print(f"indice {i}: {conversor_texto[i]}")

print("indices negativos:")
for i in range(-1, -len(conversor_texto)-1, -1): # indices negativos começam de -1 até -len (lista)
    print(f"indice {i}: {conversor_texto[i]}")
    