'''
Nombre del alumno: Amelia Mendoza López
Fecha: 11/11/2024
Descripción:Fundamentos y ejemplificación del comportamiento de listas
'''

#creación de una lista
alumnos=["Amelia","Albert"]
print(alumnos)
print()
#append-añade un elemento al final de la lista /
alumnos.append("Kevin")
print(alumnos)
print()
alumnos.append("Diana")
print(alumnos)
#insert-Añadir en un índice específico
alumnos.insert(3,"Elton")
print(alumnos)
print()
alumnos.insert(4,"Magdiel")
print(alumnos)
print()
#append-añade un elemento al final de la lista /
alumnos.append("Eden")
print(alumnos)
print()
#APPEND-añade un elemento al final de la lista /
alumnos.append("Sergio")
print(alumnos)
print()
alumnos.insert(7,"Magdiel")
print(alumnos)
print()
alumnos.insert(9,"Magdiel")
print(alumnos)
print()
#REMOVE- Borra un elemento por su valor
alumnos.remove("Magdiel")
print(alumnos)
print()
#POP-Eliminar por su índice
alumnos.pop(6)  #manera de objetos
print(alumnos)
print()
#Otra manera de eliminiar por índice
#DEL-borra por indice
del alumnos[7]    #Manera de índice
'''
FUNCIONES COMUNES
'''
#alumnos.len() #el tamañp de la lista
alumnos.sort() # ordena
alumnos.sort(reverse=True) #ordenar al revés
print(len(alumnos))
#como declarar una lista vacía
#alumnos=[]





