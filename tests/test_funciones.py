from src.funciones import promedio_notas
import pytest
 
def test_promedio_normal():
  
    assert promedio_notas([3.0, 4.0, 5.0]) == 4.0
 
def test_promedio_limites():
   
    assert promedio_notas([0.0, 5.0]) == 2.5
 
def test_promedio_vacio():
    
        assert promedio_notas([]) == 0

