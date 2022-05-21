"""3. Diseñe un algoritmo que permita hacer la siguiente conversión
• Millas a kilómetros.
• Kilómetros a millas.
Considera que
1 milla son 1.60934 kilómetros
1 kilómetro es 0.621371 millas"""
 
# conversor de millas a kilomeros y kilometros a millas

calcular = input("¿Que desea convertir millas o kilometros? ")
print("Usted desea calcular {}".format(calcular))
cantidad = float(input('Ingrese la cantidad a convertir '))

millas = (cantidad * 1.60934)


if calcular == millas :
    
    print("la conversion de millas a kilometros es: ", millas)
else:
    kilometros = (cantidad / 0.621371)
    print("la conversion de kilometros a millas es: ", kilometros)
    
