'''
Nombre.Amelia Mendoza López
Fecha:19/11/2024
Descripción: Implementación de diccionarios

'''
import random
'''
    Las tijeras cortan el papel.
    El papel cubre la piedra.
    La piedra aplasta el lagarto.
    El lagarto envenena a Spock.
    Spock aplasta las tijeras.
    Las tijeras decapitan el lagarto.
    El lagarto se come el papel.
    El papel refuta a Spock.
    Spock vaporiza la piedra.
    La piedra aplasta a las tijeras.
'''

print("***********PIEDRA-PAPEL-TIJERA-SPOCK-LAGARTO***************")
print("Piedra.....[1]")
print("Papel......[2]")
print("Tijera.....[3]")
print("Spock......[4]")
print("Lagarto....[5]")
jugador = int(input("Ingresa el número de tu elección: "))

# Diccionario para relacionar el menú con las opciones
MENU = {1: "Piedra", 2: "Papel", 3: "Tijera", 4: "Spock", 5: "Lagarto"}

# Se delimita su comportamiento
reglas = {
    #Clave ->  valor
    "Piedra": ["Tijera", "Lagarto"],
    "Papel": ["Piedra", "Spock"],
    "Tijera": ["Papel", "Lagarto"],
    "Lagarto": ["Spock", "Papel"],
    "Spock": ["Tijera", "Piedra"]
    #Define al ganador sobre los [perdedores]

}

if jugador not in MENU:
    print("Opción no válida. Por favor elige un número entre 1 y 5.")
else:
    # Jugador selecciona su opción
    opcion_jugador = MENU[jugador]

    #Se utiliza randint para establecer la opción de la computadora
    computadora = random.randint(1, 5)
    opcion_computadora = MENU[computadora]

    print(f"Tú elegiste: {opcion_jugador}")
    print(f"La computadora eligió: {opcion_computadora}")

    #Mostarará el empate si ambas opciones fuesen iguales
    if opcion_jugador == opcion_computadora:
        print(f"Empate. Ambos eligieron {opcion_computadora}.")
    #Se menciona que si eln
    elif opcion_computadora in reglas[opcion_jugador]:
        print(f"¡Ganaste! {opcion_jugador} vence a {opcion_computadora}.")
    else:
        print(f"Perdiste. {opcion_computadora} vence a {opcion_jugador}.")
