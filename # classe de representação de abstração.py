# classe de representação de abstração
class Carro:
    combustao = "fossil"
    t_combustao = "flex"
    t_carro = "passeio"
    fabricante = "fiat"
    modelo = 500
    ano = 2020
    cv = 69
    
    # exemplos de funções básicas do objeto "carro"
    def aceleracao(self):
        print("0 a 100 em 13 segundos")
        
    def frenagem(self):
        print("acionamento de ABS")
        
    def seguranca(self):
        print("acionamento de AirBag")
        
class Argo(Carro):
    modelo = "trekking"
    ano = 2024
    cv = 72
    
# criando uma instancia de class Argo
argo = Argo()

# chamando os metodos
argo.aceleracao()
argo.frenagem()
argo.seguranca()

# imprimindo as informações do argo
print(f"modelo:{argo.modelo}, ano: {argo.ano}, cv: {argo.cv}")
    
    