'''
Nombre: Amelia Mendoza López
Fecha: 20/10/2024
Descripción: Se presentan los diversos tipos de asignación,
así como su funcionalidad
'''

print("*********** TIPOS DE ASIGNACIÓN ***********")

print("1.- Asignación múltiple: ")
print("Ejemplos: ")
'''
La asignación múltiple consta de un sistema en donde podremos 
asignar DIFERENTES valores a múltiples variables en una única línea 
de código, esto genera un código más compacto
NOTA: La asignación se realiza de derecha a izquierda
'''
num1, num2 = 7, 10
print(f"número 1 , número 2 = {num1} , {num2}")

num3, cad, num4 = 11, "Hola", 9
print(f"número 3 , cadena , número 4 = {num1} , {cad}, {num4}")

suma, resta = num1 + num2, num3 - num4
print(f"suma , resta = {suma} , {resta}")

print()
print("2.- Asignación encadenada: ")
print("Ejemplos: ")
'''
La asignación múltiple consta de un sistema en donde podremos 
asignar  el MISMO valor a múltiples variables en una única línea 
de código, esto genera un código más compacto
NOTA: La asignación se realiza de izquierda a derecha
'''
num5 = num6 = num7 = 12
print(f" num5 = num6 = num7 = {num5}")
print(f" num5 = num6 = num7 = {num6}")
print(f" num5 = num6 = num7 = {num7}")

print()
print("3.- Intercambio de variables: ")
print("Ejemplos: ")
'''
Permite el intercambio de variables sin 
la necesidad de utilizar una variable auxiliar 
en el momento del intercambio
'''
num8 = int(input("Ingrese número 8: "))  # casting de variables
num9 = int(input("Ingrese número 9: "))

print("++++Intercambiando++++")
print("num9 = num8 = num 8 , num 9")
num9, num8 = num8, num9
print("++ Valores Intercambiados ++")
print(f"Valor de el número 8: {num8}")
print(f"Valor del número 9: {num9}")

print()

print("3.- Múltiples valores de entrada: ")
'''
Permite asignar múltiples valores en una sola línea  de código
a travéz de el "input", pudiéndolos almacenar en dos variables distintas
'''
num10, num11 = int(input("ingresa el número 10: ")), int(input("ingresa el número 11: "))
