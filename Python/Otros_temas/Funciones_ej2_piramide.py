'''
Nombre: Amelia Mendoza López
Fecha:07/11/2024
Descripción: Implementación de el ciclo for para la creación de
pirámides asi como la implementación de funciones
'''

print("************PIRÁMIDE****************")


def menu():
    print("Pirámide media orientada a la DERECHA....[1]")
    print("Pirámide media orientada a la IZQUIERDA....[2]")
    print("Pirámide media COMPLETA....[3]")
    print("Pirámide media orientada a la IZQUIERDA (vert)..........[4]")
    print("Salir....[5]")
    return int(input("Opción: "))

def numero_filas():
    return int(input("Ingrese el número de filas: "))


asterisco = "*"
espacio = " "

#Media piramide -DERECHA
def p1(filas):
    print("Pirámide media orientada a la DERECHA")
    #El ciclo itera desde 0 hasta el número de filas más uno
    for i in range(filas + 1):
        asteriscos = asterisco * i  # Se crea el estandar de asteriscos a utilizar de acuerdo al iterador
        espacios = espacio * (filas - i)  # Aumentará el número de espacios mientras el iterador aumente
        print(f"{espacios}{asteriscos}")

def p2(filas):
    print("Pirámide media orientada a la IZQUIERDA")
    for i in range(filas + 1):
        asteriscos = asterisco * i
        espacios = espacio * (filas - i)
        print(f"{asteriscos}{espacios}")


# Pirámide media COMPLETA
def p3(filas):
    print("Pirámide media COMPLETA")
    for i in range(filas + 1):
        asteriscos = asterisco * (2 * i - 1) #Incrementa en dos el valor de i y se resta uno
        #Se busca una secuencia 1,3,5
        espacios = espacio * (filas - i)
        print(f"{espacios}{asteriscos}")

def p4(filas):
    print("Pirámide media orientada a la IZQUIERDA (vert)")
    for i in range(filas, 0, -1):
        #El ciclo comienza con la impresión del número total de filas
        #decrementa hasta alcanzar a uno
        asteriscos = '*' * i #Se establece el número de asteriscos
        #La cantidad dependerá de el valor de 'i'
        print(asteriscos)
while True:
    opcion=menu()
    filas=numero_filas()
    if opcion==1:
        p1(filas)
    elif opcion==2:
        p2(filas)
    elif opcion==3:
        p3(filas)
    elif opcion==4:
        p4(filas)
