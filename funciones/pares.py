from funciones.logica import es_par

def test_numero_par():
    assert es_par(4)==True

def test_numero_impar():
    assert es_par(7)==False