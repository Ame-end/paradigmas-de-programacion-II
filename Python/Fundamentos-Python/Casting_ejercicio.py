'''
Nombre: Amelia Mendoza López
Fecha: 14/10/2024
Descripción: El programa mostrará la conversión de un número entero
a una cadena. Así mismo realiza la conversión de entero a flotante.
Y a su vez estos valores a booleanos
Conversión de tipos de datos (casting) en Python.
'''

# *****   Conversión de número a cadena     *****
var_float = 3.14159265
var_int = 12
var_int1 = 0
print()
print("Conversión de número a cadena.")
print(f"El número {var_float} se convierten a cadena utilizando str(var_int): {str(var_float)}")
print(f"El número {var_int} se convierten a cadena utilizando str(var_int): {str(var_int)}")
print(f"El número {var_int1} se convierten a cadena utilizando str(var_int): {str(var_int1)}")

# *****   Conversión a booleano     *****
print()
print("Conversión a booleanos.")

# Valor de var_float (3.14159265)
es_verdadero = bool(var_float)
print(f"¿El valor de {var_float} es verdadero? {es_verdadero}.")

# Valor de var_int (12)
es_verdadero = bool(var_int)
print(f"¿El valor de {var_int} es verdadero? {es_verdadero}.")

# Valor de var_int1 (0)
es_verdadero = bool(var_int1)
print(f"¿El valor de {var_int1} es verdadero? {es_verdadero}.")


# *****   Conversión de cadena a entero y flotante    *****
# Definición de variables de tipo cadena
var_cadena1 = "10002"
var_cadena2 = "100.02"  # Esta cadena es un número decimal
var_cadena3 = "0"

# Conversión de cadenas a enteros y flotantes
var_int1 = int(var_cadena1)
var_float2 = float(var_cadena2)  # Convertimos primero a float
var_int2 = int(var_float2)  # Convertimos el float a entero
var_int3 = int(var_cadena3)

# Imprimiendo los resultados de la conversión
print("Conversión de cadena a entero.")
print(f"Número como cadena: {var_cadena1}.")
print(f"Número como int: {var_int1}.")
print()

print("Conversión de cadena a entero (desde decimal).")
print(f"Número como cadena: {var_cadena2}.")
print(f"Número como float: {var_float2}.")  # Mostramos el valor flotante
print(f"Número como int: {var_int2}.")
print()

print("Conversión de cadena a entero.")
print(f"Número como cadena: {var_cadena3}.")
print(f"Número como int: {var_int3}.")
print()

# *****   Conversión de estos valores a booleano     *****

print("Conversión de los valores a booleano:")

# Valor de var_cadena1 (convertido a entero 10002)
es_verdadero = bool(var_int1)
print(f"¿El valor de {var_int1} es verdadero? {es_verdadero}.")

# Valor de var_cadena2 (convertido a flotante 100.02, luego a entero 100)
es_verdadero = bool(var_float2)
print(f"¿El valor de {var_float2} es verdadero? {es_verdadero}.")

# Valor de var_cadena3 (convertido a entero 0)
es_verdadero = bool(var_int3)
print(f"¿El valor de {var_int3} es verdadero? {es_verdadero}.")
