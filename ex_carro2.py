preco_g = 4.99
distancia_km = 1500
carros = []
consumos = []

while True:
    carro = input("Informe o modelo do carro: ")
    if carro == "":
        break

    consumo = float(input("Informe o consumo do carro por km: "))
    if carro in carros:
        idx = carros.index(carro)
        consumos[idx].append(consumo)
        consumo = None
    else:
        carros.append(carro)
        consumos.append([consumo])
    print()

print(carros)
print(consumos)

media_consumos = distancia_km / consumos * preco_g
melhor_consumo = max(media_consumos)
index_melhor_consumo = media_consumos.index(melhor_consumo)

print("O carro menos economico é o:", carros[index_melhor_consumo])

for i in range(len(carros)):
    print("o carro", carros[i], "deverá consumir:", distancia_km/media_consumos[i] * preco_g,"litros de combustivel")

