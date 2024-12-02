'''
NOMBRE: Amelia Mendoza López
FECHA:01/10/2024
DESCRIPCIÓN DEL PROBLEMA:

a) El número a adivinar es un número aleatorio entre 1 y 100.
b) El jugador tendrá 5 intentos para encontrar el número.
c) Como pista, el juego indicará si el número a adivinar es menor
o mayor al número ingresado, si el número no es el correcto.
d) Si el jugador adivina el número, el juego muestra un mensaje de
 felicitación y el número de intentos.
e) Si el jugador no adivina el número, el juego muestra un mensaje
con el número.
'''

import random

while True:
    print("------ ADIVINADOR -------")
    print("Intenta adivinar el número entre 1 y 100.")
    print("Tienes 5 intentos.")
    print("1.- JUGAR")
    print("2.- SALIR")

    opcion = input("OPCIÓN: ")

    if opcion == '1':
        numero_adivinar = random.randint(1, 100)
        intentos_maximos = 5
        numero_intentos = 0
        bandera = 0
        # 0 = perdió, 1 = ganó

        # Comienza el juego
        while numero_intentos < intentos_maximos:
            #print(f"{numero_adivinar}")-   Monitorea el número aleatorios
            print()
            print(f"INTENTO {numero_intentos + 1}:")
            numero_ingresado = input("Digite un número: ")
            intento_usuario = int(numero_ingresado)
            numero_intentos += 1

            if intento_usuario == numero_adivinar:
                bandera = 1
                print(f"¡Felicidades! Has adivinado el número en {numero_intentos} intento(s).")
                break

            elif intento_usuario < numero_adivinar:
                print("El número ingresado es MENOR al número a adivinar.")
            else:
                print("El número ingresado es MAYOR al número a adivinar.")

        if bandera == 0:
            print(f"Has alcanzado el máximo de intentos. El número era {numero_adivinar}.")

    elif opcion == '2':
        print("Saliendo del programa.")
        break
    else:
        print("OPCIÓN INVÁLIDA. Intente de nuevo.")

    print()
