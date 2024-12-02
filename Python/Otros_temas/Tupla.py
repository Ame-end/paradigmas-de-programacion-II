'''
Nombre: Amelia Mendoza López
Fecha: 13/11/2024
Descripción: Mostrar el comportamiento de una tupla, así como
de su sintaxis
'''
'''
TUPLA-No se puede añadir ni modificar
'''
#Creación de una tupla
calificaciones_parcial1=(9.6,6.3,6.0,8.7,5.0)
poo,bd,redes,arq,ing_soft=calificaciones_parcial1   #Asignación múltiple
print(calificaciones_parcial1)
#Impresión de tupla
#range-secuencia
for calificacion in calificaciones_parcial1:
    print(calificacion,end=" ")

    #Promedio
    #sum-suma                                 #leng y la tupla
                                            #Determina el tamaño de la tupla
promedio_parcial=sum(calificaciones_parcial1)/len(calificaciones_parcial1)
print()
print(f"Promedio:{promedio_parcial}")