'''
NOMBRE: Amelia Mendoza López
FECHA:01/10/2024
DESCRIPCIÓN DEL PROBLEMA:

El juego mostrará las victorias del jugador,
los partidos empatados y las victorias del CPU.
Además, mostrará el siguiente menú:

1) Piedra.
2) Papel.
3) Tijera.
0) Salir.
Cualquier otro caso -> Mostrar un mensaje de "opción no válida".
'''

import random

while True:
    print("------ JUEGO: PIEDRA, PAPEL, TIJERA -------")
    print("1.- PIEDRA")
    print("2.- PAPEL")
    print("3.- TIJERA")
    print("0.- SALIR")

    menu_usuario = input("OPCIÓN: ")
    usuario = int(menu_usuario)

    if usuario == 1:
        op_usuario = "Piedra"
    elif usuario == 2:
        op_usuario = "Papel"
    elif usuario == 3:
        op_usuario = "Tijera"
    elif usuario == 0:
        print("Saliendo del programa.")
        break
    else:
        print("OPCIÓN INVÁLIDA. Intente de nuevo.")
        print()
        continue

    aleatorio_laptop = random.randint(1, 3)
    if aleatorio_laptop == 1:
        op_laptop = "Piedra"
    elif aleatorio_laptop == 2:
        op_laptop = "Papel"
    elif aleatorio_laptop == 3:
        op_laptop = "Tijera"

    if usuario == 1 and aleatorio_laptop == 1:  # Piedra vs piedra
        print(f"EL jugador es {op_usuario} y la PC es {op_laptop}. EMPATE")
    elif usuario == 1 and aleatorio_laptop == 2:  # Piedra vs papel
        print(f"EL jugador es {op_usuario} y la PC es {op_laptop}. GANA LAPTOP")
    elif usuario == 1 and aleatorio_laptop == 3:  # Piedra vs tijera
        print(f"EL jugador es {op_usuario} y la PC es {op_laptop}. GANA USUARIO")

    elif usuario == 2 and aleatorio_laptop == 1:  # Papel vs piedra
        print(f"EL jugador es {op_usuario} y la PC es {op_laptop}. GANA USUARIO")
    elif usuario == 2 and aleatorio_laptop == 2:  # Papel vs papel
        print(f"EL jugador es {op_usuario} y la PC es {op_laptop}. EMPATE")
    elif usuario == 2 and aleatorio_laptop == 3:  # Papel vs tijera
        print(f"EL jugador es {op_usuario} y la PC es {op_laptop}. GANA LAPTOP")

    elif usuario == 3 and aleatorio_laptop == 1:  # Tijera vs piedra
        print(f"EL jugador es {op_usuario} y la PC es {op_laptop}. GANA LAPTOP")
    elif usuario == 3 and aleatorio_laptop == 2:  # Tijera vs papel
        print(f"EL jugador es {op_usuario} y la PC es {op_laptop}. GANA USUARIO")
    elif usuario == 3 and aleatorio_laptop == 3:  # Tijera vs tijera
        print(f"EL jugador es {op_usuario} y la PC es {op_laptop}. EMPATE")
    print()
