'''
Nombre: Amelia Mendoza López
Fecha: 20/ 10/2024
Descripción: Implementación del casting de variables,
así como la representación de dos operaciónes en Python
'''

print("**************** OPERACIONES ARITMÉTICAS ****************")
print("******** NOTA: Digite unicamente números enteros ********")
# Se implementa el casting de variables, con la finalidad
# de realizar operaciones aritméticas sobre los números enteros
numero_uno = int(input("Digite el primer número: "))
numero_dos = int(input("Digite el segundo número: "))

op_suma = numero_uno + numero_dos  # suma
op_resta = numero_uno - numero_dos  # resta
op_mult = numero_uno * numero_dos  # multiplicación
op_div = numero_uno / numero_dos  # división
op_mod = numero_uno % numero_dos  # módulo
op_prueb1 = numero_uno ** numero_dos  # exponente
op_prueb2 = numero_uno // numero_dos  # Obtiene el valor entero de la división

print(f"El resultado de la suma [+] entre {numero_uno} y {numero_dos} es: {op_suma}")
print(f"El resultado de la resta [-] entre {numero_uno} y {numero_dos} es: {op_resta}")
print(f"El resultado de la división [/] entre {numero_uno} y {numero_dos} es: {op_div:.3f}")
print(f"El resultado de la multiplicación [*] entre {numero_uno} y {numero_dos} es: {op_mult}")
print(f"El resultado del modúlo entre [%] {numero_uno} y {numero_dos} es: {op_mod}")
print(f"La prueba de exponenciación [**] entre {numero_uno} y {numero_dos} es: {op_prueb1}")
print(f"La prueba de división entera [//] entre {numero_uno} y {numero_dos} es: {op_prueb2}")

'''
NOTA:

CONCATENACIÓN con "f{" "}":
La letra "f" hace referencia a una "cadena formateada", esto indica 
la implementación de llaves dentro de la cadena, donde se 
almacenan los valores asignados a cada variable.
'''
