'''
Nombre: Amelia Mendoza López
Fecha: 19/10/2024
Descripción: Se realizaran operaciones aritméticas con dos números flotantes y se
mostrarán en consola.

Ejercicio:
a) Pida 2 números decimales por consola al usuario utilizando la función input.
b) Muestre los resultados de las operaciones básicas con esos números: suma, resta, multiplicación y división
'''

print("**************** OPERACIONES BÁSICAS ****************")
print("**************** números decimal ****************")
# Se realiza un  casting de variables donde se extraen valores flotantes para ambas cadenas
numero_uno = float(input("Digite el primer número: "))
numero_dos = float(input("Digite el segundo número"))

# Se muestra la concatenación de números con letreros, y se muestra el resultado final
print(f"El resultado de la suma entre {numero_uno} y {numero_dos} es: {numero_uno + numero_dos}")
print(f"El resultado de la resta entre {numero_uno} y {numero_dos} es: {numero_uno - numero_dos}")
print(f"El resultado de la división entre {numero_uno} y {numero_dos} es: {numero_uno / numero_dos}")
print(f"El resultado de la multiplicación entre {numero_uno} y {numero_dos} es: {numero_uno * numero_dos}")
