'''
Nombre: Amelia Mendoza López
Fecha:07/11/2024
Descripción: Implementación de el ciclo for para la creación de
pirámides
'''

print("************PIRÁMIDE****************")

FILAS = int(input("Ingrese el número de filas: "))
asterisco = "*"
espacio = " "


#Media piramide -DERECHA
for i in range(FILAS + 1):
    asteriscos = asterisco * i
    espacios = espacio * (FILAS - i)
    print(f"{espacios}{asteriscos}")
print()
#Media piramide -IZQUIERDA
for i in range(FILAS + 1):
    asteriscos = asterisco * i
    espacios = espacio * (FILAS - i)
    print(f"{asteriscos}{espacios}")
print()
#Media COMPLETA
for i in range( FILAS + 1):
    asteriscos = asterisco * (2 * i - 1)
    espacios = espacio * (FILAS - i)
    print(f"{espacios}{asteriscos}")
print()
#Media piramide -IZQUIERDA-verticalmente
for i in range(FILAS, 0, -1):
    asteriscos = '*' * i
    print(asteriscos)