'''
Nombre del alumno: Amelia Mendoza López
Fecha: 11/2024
Descripción:


'''
import random

print("***********PIEDRA-PAPEL-TIJERA-SPOCK-LAGARTO***************")
print("Piedra.....[1]")
print("Papel......[2]")
print("Tijera.....[3]")
print("Spock......[4]")
print("Lagarto....[5]")
jugador = int(input("Ingresa el número de tu elección: "))

# Diccionario para relacionar el menú con las opciones
MENU = {1: "Piedra", 2: "Papel", 3: "Tijera", 4: "Spock", 5: "Lagarto"}

# Diccionario para definir las reglas
reglas = {
    "Piedra": ["Tijera", "Lagarto"],
    "Papel": ["Piedra", "Spock"],
    "Tijera": ["Papel", "Lagarto"],
    "Lagarto": ["Spock", "Papel"],
    "Spock": ["Tijera", "Piedra"]
}

if jugador not in MENU:
    print("Opción no válida. Por favor elige un número entre 1 y 5.")
else:
    # Jugador selecciona su opción
    opcion_jugador = MENU[jugador]

    # La computadora elige una opción aleatoria
    computadora = random.randint(1, 5)
    opcion_computadora = MENU[computadora]

    print(f"Tú elegiste: {opcion_jugador}")
    print(f"La computadora eligió: {opcion_computadora}")

    # Verificar el resultado
    if opcion_jugador == opcion_computadora:
        print(f"Empate. Ambos eligieron {opcion_computadora}.")
    elif opcion_computadora in reglas[opcion_jugador]:
        print(f"¡Ganaste! {opcion_jugador} vence a {opcion_computadora}.")
    else:
        print(f"Perdiste. {opcion_computadora} vence a {opcion_jugador}.")




