''' com essa linha de código, iremos validar e testar se os resultados são verdadeiros (e mostrar)

'''


# cria uma class para calcular dois numeros, se não for possivel, uma mensagem de "erro" aparecerá
class Calculator:
    def evaluate_expression(self, expression):
        try:
            result = eval(expression) # tenta calcular o resultado da expressão
            return result # retorna o resultado
        except Exception:
            return "Erro" # se tiver divisão por zero, retorna "erro"

# exemplos para testes usando (unitest e pytest)

if __name__ == "__main__":
    calc = Calculator() # cria uma instancia da calculadora
    
    # expresssões lógicas
    print(calc.evaluate_expression("2 + 2")) # saida 4
    print(calc.evaluate_expression("10 / 0"))# saida erro
    print(calc.evaluate_expression("5 * 6")) # saida "30"
    

# o programa irá responder se os calculos estão corretos

    
