'''
Nombre: Amelia Mendoza López
Fecha:23/10/2024
Descripción: Determina el grupo de edad al que
pertenece cada persona, de acuerdo a su edad
'''

print("**************** GRUPO DE EDAD ******************")

edad = int(input("Ingresa tu edad: "))
# Se evaluará el rango de edad a la que pertence cada persona
if edad < 15:
    print("Grupo de edad: Niños y adolescentes")
# Se aplica un operador lógico para determinar cada uno de los rangos
# y verificar que la edad que el usario ingreso este dentro del rango
elif edad >= 15 and edad <= 24:
    print("Grupo de edad: Jóvenes")  # jóvenes

elif edad >= 25 and edad <= 44:
    print("Grupo de edad: Adultos jóvenes")  # adultos jóvenes

elif edad >= 45 and edad <= 60:
    print("Grupo de edad: Adultos maduros")  # adultos maduros

elif edad > 60:
    print("Grupo de edad: Adultos mayores")  # adultos mayores
