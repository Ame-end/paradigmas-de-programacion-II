'''
Nombre: Amelia Mendoza López
Fecha:23/10/2024
Descripción: Determina a partir de dos números cual de ellos
es el menor
'''

print("********* SENTENCIAS *********")
print("********  Ejercicio 1  *******")
print(" Determina si un número es menor ")

# Se realiza un castig de variables para tomar el valor entero de la cadena
# ingresada por el usuario para el primer y segundo número
num_uno = float(input("Ingresa el primer valor decimal: "))
num_dos = float(input("Ingresa el primer valor decimal: "))

# Se establecen condiciones para determinar el rango de ambos números
if num_uno > num_dos:
    print(f"El número {num_uno} es mayor que {num_dos}.")
elif num_uno < num_dos: # "elif" sustituye a "else if"
    print(f"El número {num_uno} es menor que {num_dos}.")
else:
    print("Los dos números son iguales.")
