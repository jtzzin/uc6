lista = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"] # lista com os elemtnos de -- a -- até -- j --
conversor_texto =  [letra.capitalize() for letra in lista] # apenas letras maiusculas com o método CAPITALIZE

# exibindo os indices postivos e os valores correspondentes
print("indices positivos:")
for i in range(len(conversor_texto)): 
    print(f"indice {i}: {conversor_texto[i]}")

# exibindo os indices negativos e os valores correspondentes
print("\nindices negativos:")
for i in range(-1, -len(conversor_texto)-1, -1):
    print(f"indice {i}: {conversor_texto[i]}")
    


