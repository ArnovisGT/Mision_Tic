def CDT(usuario:str, capital:int, tiempo:int):
    valor_perdida = 0.02
    valor_ganancia = 0.03
    if tiempo > 2:
        valor_intereses = (capital * valor_ganancia * tiempo)/12
        valor_total = (valor_intereses + capital)
        return f"Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {tiempo} meses es: {valor_total}"
    else:
        valor_a_perder = (capital * valor_perdida)
        valor_Total = (capital - valor_a_perder)
        return f"Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {tiempo} meses es: {valor_Total}"
print(CDT('AB1012', 1000000, 3))
print(CDT('ER3366',650000, 2))