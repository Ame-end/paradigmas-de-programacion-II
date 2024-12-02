'''
Nombre.Amelia Mendoza López
Fecha:19/11/2024
Descripción: Aplicar la lógica del juego piedra-papel y tijera
mediante cuestionarios

                INVESTIGACIÓN PREVIA DE DICCIONARIOS:

Caracteristicas:
-Los elementos se guardan desordenados
-Tiene dos elementos por posición: clave y el valor
-Aceptan diferentes tipos de datos
-Dentro de los diccionarios es posible agregar
    listas,tuplas, e inclusive otros diccionarios
- Se almacenan en forma de key-valor

-> ESTRUCTURA: diccionario={'key1':valor1 ,'key2': valor2}
    Ej.diccionario={"azul":"blue","rojo":"red","verde":"green"} <-clave y el valor

    1.-Mostrar un elemento del diccionario a través de la clave
        print(diccionario["azul"])

    2.-Agregar elementos al diccionario
    Se pondrá el nombre del diccionario y entre corchetes el nombre
    de la clave que deseamos agregar
        diccionario["amarillo"]="yellow"

    3.-Modificar elementos
        diccionario["azul"]="BLUE"

    4.-Eliminar elementos del diccionario
    del(diccionario["verde"])

'''

import random

print("***********PIEDRA-PAPEL-TIJERA***************")
print("Piedra.....[1]")
print("Papel......[2]")
print("Tijeras....[3]")
jugador = int(input("Ingresa el número de tu elección: "))


# Diccionario para relacionar el menú con las opciones
MENU = {1: "Piedra", 2: "Papel", 3: "Tijera"}

# Diccionario para definir las reglas
reglas = {
    "Piedra": "Tijera",  # Piedra vence a Tijera
    "Papel": "Piedra",   # Papel vence a Piedra
    "Tijera": "Papel"    # Tijera vence a Papel
}



if jugador not in MENU:
    print("Opción no válida. Por favor elige 1, 2 o 3.")
else:
    #Jugador es la clave para acceder al menu de opciones
    opcion_jugador = MENU[jugador]

    # Se genera el número aleatorio para seleccionar la opcion de la computadora
    computadora = random.randint(1, 3)
    #se toma a "computadora" para acceder al menú
    opcion_computadora = MENU[computadora]


    print(f"Tú elegiste: {opcion_jugador}")
    print(f"La computadora eligió: {opcion_computadora}")


    if opcion_jugador == opcion_computadora:
        print("Empate", opcion_computadora)
    elif reglas[opcion_jugador] == opcion_computadora:
        print("Eres el GANADOR, la computadora seleccionó: ", opcion_computadora)
    else:
        print("PERDISTE, la computadora seleccionó: ", opcion_computadora)
