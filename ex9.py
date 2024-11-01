
#print(f"meu nome é Juan, prazer!", '\n')

#print(f"Eu tenho mais de 18 anos?"' \n', 19 > 18, "ok, posso beber")

class MaiorIdade:
#solicitamos o nome do usuario com o input  
    nome = input("Digite seu nome: ")

#fazemos o método de comparação para verificar a idade
    def comparar(self):
        idade = int(input("digite sua idade: "))
        sexo = input("Digite seu genero, F ou M: ")
        
        if idade >= 18 and sexo == "F":
            print(f"A {MaiorIdade.nome} é maior de idade!" '\n', "pode beber.")
        elif idade < 18 and sexo == "F":
             print(f"A {MaiorIdade.nome} é menor de idade!" '\n', "não pode beber.")
        elif idade >=18 and sexo == "M":
             print(f"O {MaiorIdade.nome} é maior de idade!" '\n', "pode beber.")
        else:
            print(f"O {MaiorIdade.nome} é menor de idade" '\n', "não pode beber")
    
"""se a idade for igual ou maior que 18, e o sexo for feminino, retorna a mensagem com o 'a'.
 e continua a verificação de idade para o sexo fem e masc
"""

teste = MaiorIdade()
teste.comparar()



      

      

    
        