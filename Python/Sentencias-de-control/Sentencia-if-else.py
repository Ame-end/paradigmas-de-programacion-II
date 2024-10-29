'''
Nombre: Amelia Mendoza López
Fecha:23/10/2024
Descripción: Determina el comportamiento de las sentencias de codición if/else
así como la categoria de cada número
'''

print("************* NÚMEROS PARES E IMPARES ****************")

# Se realiza un casting de varibles (string-int)
# Se pide un número por consola
num = int(input("Ingresa un número: "))

# Se determina a través de el operador mod (%)
if num % 2 == 0:
    print("El número es PAR")
else:
    print("El número es IMPAR")
