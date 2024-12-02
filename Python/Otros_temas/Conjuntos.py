'''
Nombre: Amelia Mendoza López
Fecha:13/11/2024
Descripción:

ordenados: Lista y tuplas
mutables:conjuntos,listas
desordenados: conjuntos
'''
'''
Los conjuntos funcionan para un solo valor
'''

# Conjunto vacío
Conjunto1 = set()  # Crea el conjunto vacío
Conjunto2 = {10, 5, 24, 11, 8, 7, 21, 9}
print(Conjunto2)

# Añadir elementos
Conjunto1.add(80)
Conjunto1.add(111)
Conjunto1.add(10)
Conjunto1.add(5)
Conjunto1.add(24)
print(Conjunto1)

Conjunto1.add(80)
print(80)

Conjunto1.remove(111)
# Conjunto1.remove(111)- REMOVE Funciona unicamente si el elemento existe
Conjunto1.discard(111)  # DISCARD-No genera error si ya no se encuentra el número que queremos eliminar
Conjunto1.discard(10)

# OPERACIONES

    # Unión
conjunto_UNION = Conjunto1 | Conjunto2
print(conjunto_UNION)
    # Intersección
conjunto_INTERSECCION = Conjunto1 & Conjunto2
print(conjunto_INTERSECCION)
    # Resta
RESTA_conjuntos=Conjunto2-Conjunto1
print(RESTA_conjuntos)

alumnos_LISTA=["Albert","Kevin","Elton","Diana","Edén","Amelia","Sergio"]
alumnos_LISTA.append("Elton")
#Transformar de lista a conjuntos
alumnos_conjunto=set(alumnos_LISTA)
print(f"CONJUNTOS: {alumnos_conjunto}")
print(f"LISTA: {alumnos_LISTA}")

nombre=input("Ingresa un nombre")
#LOWER-convertimos a minusculas
#STRIP-Remueve los espacios al inicio-Espacios iniciales y finales _AMELIA_
nombre=nombre.strip().lower()
if nombre in alumnos_conjunto: #Se revisa que nombre este en alumnos conjunto
    print("Se encuentra en el conjunto")
else:
    print("Se añadió al conjunto")
alumnos_conjunto.add(nombre)