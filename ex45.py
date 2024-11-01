produtos = [
    ['maça',5],
    ['banana',15],
    ['goiaba',25],
    ['manga',35],
]
produtos = []

while True:
    produto = input("insira o produto: ")
    if not produto:
        break
    qtd = int(input("qual é a quantidade de produto:"))
    produtos.append([produto, qtd])
print("os produtos e quantidades cadastrados foram:", produtos)
