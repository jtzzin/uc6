nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
altura = float(input("Digite a sua altura: "))

print(f"Nome: {nome}, Idade: {idade}, Altura: {altura:.2f}")

if idade >= 18:
    print(f"Você pode digiri.")
else:
    print(f"Você não pode digirir.")