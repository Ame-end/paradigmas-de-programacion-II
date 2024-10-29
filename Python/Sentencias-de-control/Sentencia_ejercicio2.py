'''
Nombre: Amelia Mendoza López
Fecha:23/10/2024
Descripción: Determina a partir de dos números cual de ellos
es el menor
'''

print("********* SENTENCIAS *********")
print("********  Ejercicio 2  *******")
print(" Determina la estación del año ")

# El usuario digita el número del mes
# Se realiza un casting de variables y convierte la cadena ingresada por el usuario
# en un valor entero
num_mes = int(input("Ingresa el número de mes: "))

# Delimita el rango incorrecto para la estación del año
if num_mes > 12:
    print("INCORRECTO")
# Si el valor no entra en el rango anterior

# Elif-Es utiliza para tomar y válidar decisiones que no cumplan con
# el rango asignado en el el if

# sentecia de control - condición - operador lógico - condición
elif num_mes >= 3 and num_mes <= 5:
    num_mes = "Primavera"  # Si la condicón se cumple mostrará "Primavera"

elif num_mes >= 6 and num_mes <= 8:
    num_mes = "Verano"  # Si la condicón se cumple mostrará "Verano"

elif num_mes >= 9 and num_mes <= 11:
    num_mes = "Otoño"  # Si la condicón se cumple mostrará "Otoño"

elif num_mes == 12 or (num_mes >= 1 and num_mes <= 2):
    num_mes = "Diciembre"  # Si la condicón se cumple mostrará "Diciembre"

print(f"La estación es: {num_mes}")
