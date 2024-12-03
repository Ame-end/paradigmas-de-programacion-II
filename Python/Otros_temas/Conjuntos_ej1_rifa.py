'''
Nombre: Amelia Mendoza López
Fecha:14/11/2024
Descripción:

RIFA DE LAPTOP 503

-Administrar las personas registradas
-1 boleto por persona

1)Ver participantes (Indicar cuantos hay)
2)Añadir participantes
3)Eliminar participantes
4)Seleccionar ganador
5)Salir
'''

import random


def main():
    participantes = set()

    while True:
        print("***  Rifa de una computadora  ***")
        print("1) Ver correos de participantes")
        print("2) Agregar correo de participante")
        print("3) Eliminar correo de participante")
        print("4) Seleccionar ganador")
        print("0) Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            if participantes:
                print("Participantes:")
                for correo in participantes:
                    print(f" {correo}")
            else:
                print("No hay participantes registrados.")

        elif opcion == "2":
            correo = input("Ingrese el correo del participante: ")
            if correo in participantes:
                print("El correo ya está registrado.")
            else:
                participantes.add(correo) #Si el correo no existiese, se deberá agregar
                #se utilizará '.add'
                print("Correo agregado con éxito.")

        elif opcion == "3":
            correo = input("Ingrese el correo del participante a eliminar: ")
            if correo in participantes:
                participantes.remove(correo) #Se eliminará el correo del participante
                #se utilizará '.remove'
                print("Correo eliminado con éxito.")
            else:
                print("El correo no está registrado.")

        elif opcion == "4":
            if participantes:
                ganador = random.choice(list(participantes))
                '''
                ->list(participantes): convierte el conjunto de participantes en una lista
                ->random.choice(lista). Selecciona un elemnto al azar en la lista
                
                Se le es asignado a ganador
                '''
                print(f"¡El ganador es: {ganador}!")
            else:
                print("No hay participantes registrados para elegir un ganador.")

        elif opcion == "0":
            print("Saliendo del programa. ¡Gracias por participar!")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

