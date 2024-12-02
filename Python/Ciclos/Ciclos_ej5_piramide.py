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
print("Pirámide media orientada a la DERECHA")
#El ciclo itera desde 0 hasta el número de filas más uno
for i in range(FILAS + 1):
    asteriscos = asterisco * i  # Se crea el estandar de asteriscos a utilizar de acuerdo al iterador
    espacios = espacio * (FILAS - i)  # Aumentará el número de espacios mientras el iterador aumente
    print(f"{espacios}{asteriscos}")
print()


print("Pirámide media orientada a la IZQUIERDA")
for i in range(FILAS + 1):
    asteriscos = asterisco * i
    espacios = espacio * (FILAS - i)
    print(f"{asteriscos}{espacios}")
print()

# Pirámide media COMPLETA
print("Pirámide media COMPLETA")
for i in range(FILAS + 1):
    asteriscos = asterisco * (2 * i - 1) #Incrementa en dos el valor de i y se resta uno
    #Se busca una secuencia 1,3,5  
    espacios = espacio * (FILAS - i)
    print(f"{espacios}{asteriscos}")
print()

print("Pirámide media orientada a la IZQUIERDA - verticalmente")
for i in range(FILAS, 0, -1):
    #El ciclo comienza con la impresión del número total de filas
    #decrementa hasta alcanzar a uno
    asteriscos = '*' * i #Se establece el número de asteriscos
    #La cantidad dependerá de el valor de 'i'
    print(asteriscos)
