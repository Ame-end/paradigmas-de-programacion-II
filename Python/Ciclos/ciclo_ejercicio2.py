'''
Nombre: Amelia Mendoza López
Fecha:24/10/2024
Descripción:Suma acumulativa de dos números
'''

print("********* CICLOS *********")
print("********  while  *******")
print("*****  EJERCICIO 2 *******")
print("Suma de un determinado rango")

# Solicitar al usuario el rango inicial y final
num_uno = int(input("Digite el número inicial: "))
num_dos = int(input("Digite el número final: "))

# Inicialización de variables
i = num_uno            # Contador que comienza en el número inicial ingresado
acumulador = 0         # Acumulador para sumar los valores de 'i'

# Ciclo while que imprime y suma números dentro del rango especificado
while i <= num_dos:
    print(i, end=" ")            # Imprime el valor actual de 'i' en la misma línea
    acumulador = acumulador + i   # Agrega el valor de 'i' al acumulador
    i = i + 1                     # Incrementa 'i' en 1 para la siguiente iteración
print()  # Salto de línea final
print(f"La suma del {num_uno} hasta {num_dos} es: {acumulador}")
