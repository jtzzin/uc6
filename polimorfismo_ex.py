# definimos uma classe chamada "animal"
# uma classe como é um molde que define o comportamento de um tipo de objeto
class Animal:
    # metodo (função) que será compartilhada por todos os animais que criaremos
    # aqui, "emitir_som" não faz nada especifico  ainda, apenas retorna a palavra "animal"
    def emitir_som(self):
        return Animal

# criaremos uma nova classe chamada "cachoroo", que herda as caracteristicas de "animal"
# isso significa que, "cachorro", é um tipo de especifico de "animal"
class Cachorro(Animal):
    # sobrescrevemos o metodo "emitir_som" da classe "animal"
    # agora, sempre que um objeto "cachorro" chamar "emitir_som", ele vai imprimir "au au au"
    def emitir_som(self):
        print("o som que o cachorro faz é: Au Au")
        
# criamos uma outra classe chamada de "gato", que tambem herda de "animal"
class Gato(Animal):
    # repete a lógica de cima
    def emitir_som(self):
        print(f"o som que o gato faz é: '\n', miau")

# aqui, criamos um objeto do tipo "cachorro" (variavel)  chamado "cachorro"
cachorro = Cachorro()
# chamamos o metodo "emitir_som" para imprimir o som
cachorro.emitir_som()

# a variavel "gato" recebe o objeto de "Gato"
gato = Gato()
# som do gato
gato.emitir_som()
