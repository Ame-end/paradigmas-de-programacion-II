'''
Nombre: Amelia Mendoza López
Fecha: 20/10/2024
Descripción: Se muestra el comportamiento de los
operadores relacionales y su comportamiento con dos
números flotantes
'''

print("**************** OPERADORES RELACIONALES ****************")
'''
CONCEPTO:Los operadores relacionales se utilizan en programación
 para comparar dos valores y establecer la relación que tienen. 
El resultado de la comparación es un valor booleano 
(verdadero o falso)  si la comparación llegará a ser cierta o falsa
'''
# Se aplica un casting de variables para tomar el valor flotante de la cadena
num_uno = float(input("Ingrese el primer valor decimal: "))
num_dos = float(input("Ingrese el segundo valor decimal: "))

# Mayor que
print(f"¿El número: {num_uno} es mayor que: {num_dos} ? {num_uno > num_dos}")

# Menor que
print(f"¿El número: {num_uno} es menor que: {num_dos} ? {num_uno < num_dos}")

# Mayor o igual que
print(f"¿El número: {num_uno} es mayor o igual que: {num_dos} ? {num_uno >= num_dos}")

# Menor o igual que
print(f"el número: {num_uno}. es menor o igual que: {num_dos} ? {num_uno <= num_dos}")

# Igual igual
print(f"el número: {num_uno}. es igual que: {num_dos} ? {num_uno == num_dos}")

# Diferente
print(f"el número: {num_uno}. es diferente que: {num_dos} ? {num_uno != num_dos}")
