import unittest # importa a biblioteca para testes
from calculadora import Calculator # importa a classe calculator vem do arquivo 

# define uma nova classe de teste, no qual herda as funções do unittest
class TestCalculatorLogic(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator() # cria a instancia da calculadora
        
    def test_addition(self):
        self.assertEqual(self.calculator.evaluate_expression("2+2"), 4)
        
    def test_subtraction(self):
        self.assertEqual(self.calculator.evaluate_expression("5-3"), 2)
    
    def test_multiplication(self):
        self.assertEqual(self.calculator.evaluate_expression("4*5"), 20)
        
# executa os testes, terminal (diretamente)
if __name__ == '__main__':
    unittest.main()
        

# executando!!!

#python -m unittest test_calculator.py


