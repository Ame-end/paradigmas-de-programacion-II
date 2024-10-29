'''
Nombre: Amelia Mendoza López
Fecha: 21/10/2024
Descripción: Implementacion del casting y operadores lógicos

Problema:
    *Programa que derminará si aplica una bonificación

    - Solicitar al usuario un número decimal con valores de compra
    - Preguntar al usuario si la compra fue a MSI (si/no)
    - Se aplicará la bonificación si la compra es mayor a 5000.00 y
        si la compra fue a MSI
    - Mostra el resultado en consola como valor booleano
'''

print("*********** BONIFICACIÓN ***********")

#Se solicita el valor de la compra y se aplica un casting
compra = float(input("Ingresa el valor de la compra: "))

# Preguntar si la compra fue a MSI
utiliza_msi = input("¿La compra fue a MSI? (si/no): ").lower()

# Dermina con las restrincciones para que se cumpla la bonificación
bonificacion = compra > 5000.00 and utiliza_msi == "si"

print("¿Aplica bonificación?:", bonificacion)
