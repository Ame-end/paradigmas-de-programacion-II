'''
Nombre: Amelia Mendoza López
Fecha:24/10/2024
Descripción:Suma acumulativa de dos valores
'''

print("********* CICLOS *********")
print("********  while  *******")
print("*****  EJERCICIO 1 *******")
print("suma acumulativa de dos valores")

num = int(input("Digite el número final: "))

# Inicializar la variable en 0
i = 0                # Contador que comienza desde 0
acumulador = 0       # Acumulador para sumar los valores de 'i'

# Ciclo while que imprime y suma números hasta el valor de 'num'
while i <= num:
    print(i, end=" ")            # Imprime el valor actual de 'i' en la misma línea
    acumulador = acumulador + i   # Agrega el valor de 'i' al acumulador
    i = i + 1                     # Incrementa 'i' en 1 para la siguiente iteración
print()  # Salto de línea final
print(f"La suma del 0 hasta {num} es: {acumulador}")



