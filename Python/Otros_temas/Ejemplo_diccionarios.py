'''
EJEMPLO DE DICCIONARIOS
Caracteristicas:
-Los elementos se guardan desordenados
-Tiene dos elementos por posición: clave y el valor
-Aceptan diferentes tipos de datos
-Dentro de los diccionarios es posible agregar
    listas,tuplas, e inclusive otros diccionarios
'''

#Creación de un diccionario vació
            #clave y el valor
diccionario={"azul":"blue","rojo":"red","verde":"green"}

print(diccionario)

#Mostrar un elemento del diccionario a través de la clave
#Se pude mostrar el valor que tenga cada una de sus claves
print(diccionario["azul"])

#Agregar elementos al diccionario
#Se pondrá el nombre del diccionario y entre corchetes el nombre
#de la clave que deseamos agregar
diccionario["amarillo"]="yellow"
print(diccionario)

#Modificar elementos
diccionario["azul"]="BLUE"
print(diccionario)

#Eliminar elementos del diccionario
del(diccionario["verde"])
print(diccionario)

'''
        NUEVA COLECCION DE DICCIONARIO
'''
#Diccionario-nombre de personas
#lista dentro de un diccionario
diccionario={"Amelia":[19,1.55],"Alejandro":[22,1.73]}

#diccionario dentro de otro diccionario
diccionario={"Amelia":{"edad":19,"Estatura":1.55},"Alejandro":[22,1.73]}

