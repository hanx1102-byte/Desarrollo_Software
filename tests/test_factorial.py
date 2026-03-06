from funciones.logica_factorial import factorial

def test_factorial_numero_positivo():
    assert factorial(5)==120

def test_factorial_cero():
    assert factorial(0)==1