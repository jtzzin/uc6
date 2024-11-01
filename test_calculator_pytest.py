import pytest # importa o pytest
from calculadora import Calculator # Arquivo que ira testar com a classe/função

# cria uma instancia para a calculadora antes de cada teste
@pytest.fixture
def Calculator():
    return Calculator()

def test_addition(Calculator):
    assert Calculator.evaluate_expression("2 + 2") == 4
    
def test_subtraction(calculator):
    assert Calculator.evaluate_expression("5 - 2") == 3





    





