def promedio_notas(notas):
    if not notas:   
        return 0

    notas_validas = [n for n in notas if 0 <= n <= 5]
 
    if not notas_validas:
        return 0
 
    resultado = sum(notas_validas) / len(notas_validas)
    return round(resultado, 2) 
