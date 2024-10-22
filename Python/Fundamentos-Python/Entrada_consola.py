'''
Nombre: Amelia Mendoza López
Fecha: 19/10/2024
Descripción:Entrada de datos por consola para interactuar con el usuario con valores dinámicos.
'''
#

# Comentar sobre la función input.

numero1_cadena = input(
    "Introduce un número decimal: ")  # La variable "numero1_cadena" almacenará un dato de tipo cadena
numero2_cadena = input(
    "Introduce otro número decimal: ")  # la variable "numero2_cadena" almacenará un dato de tipo cadena
resultado_cadena = numero1_cadena + numero2_cadena  # Verificar qué es lo que realiza esta instrucción (ver el print).
print()
'''
Ejemplo de lo que se mostrará en pantalla
numero1_cadena = "24.1"
numero2_cadena = "5.10"
La impresión es una concetenación de ambas cadenas: "24.15.10" con la 
instrucción qué se presenta en la línea número 10 del código
'''
print(" ****  Recibir número sin un casting de varibles  ****")
print(f"El resultado de {numero1_cadena} y {numero2_cadena} es: {resultado_cadena}")

'''
El objetivo del programa es la suma de dos números decimales y
para ello, es necesario realizar un casting de variables 

Almacena un dato de tipo String -> numero1_cadena = input("Introduce un número decimal: ")
Pasa el dato de tipo String a Flotante -> numero1_float = float(numero1_cadena)
esto permite realizar la adicion de una cantidad a otra
'''
# Comentar por qué se realiza el casting de variables.
numero1_float = float(numero1_cadena)
numero2_float = float(numero2_cadena)
'''
Ejemplo de lo que se mostrará en pantalla
numero1_cadena = 24.1
numero2_cadena = 5.10
La impresión es una concatenación de ambos valores flotantes: 29.200000000000003 
'''
resultado_float = numero1_float + numero2_float  # Verificar qué es lo que realiza de esta manera y compáralo.
print()
print(" ****  Casting de varibles  ****")
print(f"El resultado de {numero1_float} y {numero2_float} es: {resultado_float}")
