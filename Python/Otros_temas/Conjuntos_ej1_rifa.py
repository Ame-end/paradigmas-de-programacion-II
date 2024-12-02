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

# Lista de participantes
participantes = []

# Función para mostrar el menú
def MENU():
    print("--- RIFA DE LAPTOP 503 ---")
    print("1. Ver participantes")
    print("2. Añadir participante")
    print("3. Eliminar participante")
    print("4. Seleccionar al ganador")
    print("5. Salir")

# Bucle principal
while True:
    MENU()
    opcion = input("Selecciona una opción: ")

    if opcion == "1":  # Ver participantes
        if not participantes:
            print("No se han registrado participantes aún")
        else:
            print(f"Participantes registrados ({len(participantes)}):")
            for i, nombre in enumerate(participantes, start=1):
                print(f"{i}. {nombre}")

    elif opcion == "2":  # Añadir participante
        nombre = input("Ingresa el nombre del participante: ").strip()
        if nombre in participantes:
            print("Este participante ya está registrado.")
        else:
            participantes.append(nombre)
            print(f"{nombre} ha sido añadido.")

    elif opcion == "3":  # Eliminar participante
        if not participantes:
            print("No hay participantes registrados para eliminar.")
        else:
            try:
                for i, nombre in enumerate(participantes, start=1):
                    print(f"{i}. {nombre}")
                indice = int(input("Ingresa el número del participante a eliminar: ")) - 1
                eliminado = participantes.pop(indice)
                print(f"{eliminado} ha sido eliminado.")
            except (ValueError, IndexError):
                print("Número inválido.")

    elif opcion == "4":  # Seleccionar ganador
        if not participantes:
            print("No hay participantes para seleccionar un ganador.")
        else:
            ganador = random.choice(participantes)
            print(f"\n¡El ganador es: {ganador}!")

    elif opcion == "5":  # Salir
        print("¡Gracias por participar en la rifa! Hasta luego.")
        break

    else:
        print("Opción no válida. Intenta de nuevo.")
