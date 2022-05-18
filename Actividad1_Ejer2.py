"""Diseñe un algoritmo para calcular la longitud de la hipotenusa (es decir, el lado más largo de un
triángulo rectángulo, el opuesto al ángulo recto) utilizando el Teorema de Pitágoras:
c = √ a2 + b2
Considera que
Para calcular una raíz cuadrada, toda la formula tiene que ser elevada a 0.5, en Python seria
**0.5, donde el operador matemático seria ** exponente"""
from calendar import c


a = float(input("Ingrese el lado opuesto: "))
b = float(input("Ingrese el lado adyacente: "))

hipotenusa = ((a**2 + b**2)**0.5)
print("la longitud de la hipotenusa es: {}".format(hipotenusa))
