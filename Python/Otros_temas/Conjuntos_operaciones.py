'''
DATOS DEL AUTOR
Nombre: Dr. Alberto Martínez Barbosa
Descripción: Ejemplos de operaciones de los conjuntos.
-----
Datos del alumno
Nombre: Amelia Mendoza López
Fecha: 02/12/2024

CONJUTOS: Conocidos como sets, son colecciones no ordenadas de
elementos únicos. Esto significa que cada elemento aparece una sola vez
en el conjunto y el orden en el que se almacenan no es importante
'''

# Se crean dos conjuntos de números.
print("Se crean dos conjuntos.")

conjuntoA = {2, 223, 12, 1, 3, 4, 1, 6}  # Permite la duplicidad de números
conjuntoB = {12, 23, 0, 6, 30, 4, 10}

print(f"Conjunto A: {conjuntoA}")
print(f"Conjunto B: {conjuntoB}")
print()

# Operaciones básicas.
print("Operaciones básicas.")

# UNIÓN - |
union = conjuntoA | conjuntoB
print(f"Unión de los conjuntos (|): {union}")  # La unión omite los valores repetidos en ambos conjuntos.

# INTERSECCIÓN - &
interseccion = conjuntoA & conjuntoB
print(f"Intersección de los conjuntos (&): {interseccion}")  # Son los valores que coinciden en ambos conjuntos.

# DIFERENCIA- (-)
diferencia = conjuntoA - conjuntoB
print(
    f"Resta de los conjuntos: {diferencia}")  # Son los valores del conjunto A menos los que coincidente con el conjunto B.
print()

print("Convertir de lista a conjunto y viceversa.")
# Estructura de una lista
lista = ["Perro", "Gato", "Ratón", "Cuyo", "Gato", "Lobo", "Perro"]
print(f"Lista original: {lista}") #Impresión de la lista

#Conversión de lista a conjunto
conjunto = set(lista) #set-toma la lista y elimina los componetes duplicados
print(f"Lista como conjunto: {conjunto}")  # No considera los valores repetidos.

lista_reconvertida = list(conjunto)#List convierte el conjunto a una lista
print(f"Lista reconvertida del conjunto: {lista_reconvertida}")
