class numerosiguais:
    def valores():
        valor = int(input("digite o valor: "))
        if valor == 500:
            print(f"os valores sao iguais, que é:", valor)
        else:
            print("o(s) valores sao diferentes, digite outro numero")
            return numerosiguais.valores()
            
teste = numerosiguais
numerosiguais.valores()
    




    
