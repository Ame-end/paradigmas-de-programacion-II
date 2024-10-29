# Información del programa
# Nombre: Amelia Mendoza López
# Fecha: 24/10/2024
# Descripción: Este programa utiliza ciclos `while` para imprimir números en secuencia. 
# En el primer ejemplo, se imprime una secuencia desde 1 hasta un número ingresado por el usuario.
# En el segundo ejemplo, se imprime una secuencia de números pares hasta un número dado.

print("********* CICLOS *********")
print("********  while  *******")
print("********  EJEMPLO 1 *******")
print("Impresión del 1 al número digitado por el usuario")

# Solicitar al usuario el rango final para la impresión
#Se realiza un casting de variables para converitr una cadena a entero
num = int(input("Digite el rango final: "))
input(f"Los números del 1 al {num} son:")

# Ejemplo 1: Imprimir números del 1 hasta el número ingresado
i = 1
while i <= num:
    print(i, end=" ")  # Imprime los números en la misma línea
    i += 1  # Incrementa en 1 para la siguiente iteración
print()
print("Fin de la impresión")

# EJEMPLO 2: Impresión de números pares
print("\n********  EJEMPLO 2 *******")
print("Impresión de los números pares")

# Solicitar el rango final para los números pares
num = int(input("Digite el rango final: "))
input(f"Los números pares del 1 al {num} son:")

# Imprimir solo números pares dentro del rango especificado
i = 0
while i <= num:
    if i % 2 == 0:  # Verificar si el número es par a tráves del operador mod
        print(i, end=" ")  # Imprime los números pares en la misma línea
    i += 1  # Incrementa en 1 para la siguiente iteración
print()
print("Fin de la impresión")
