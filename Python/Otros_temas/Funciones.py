'''
Nombre: Amelia Mendoza López
Fecha:07/11/2024
Descripción: Implementación de funciones mediante una calculadora
'''

print("************FUNCIONES****************")
'''
def-palabra reservada para crear una funcion
ESTRUCTURA: 
'''


# función para mostrar menú
def menu():
    print("Suma....[1]")
    print("Resta....[2]")
    print("Multiplicación....[3]")
    print("División..........[4]")
    print("Exponenciación entera....[5]")
    print("Exponenciación........[0]")
    pass


# funcion para obtener dos números ingresados por el usuario
def numeros_recibidos():
    numero1 = int(input("Ingresa el primer número: "))
    numero2 = int(input("Ingresa el segundo número: "))
    # Retorna los valores enteros de los números ingresados
    return numero1, numero2


# Ciclo while para ejecutar el menú de opciones mientras 'i' no sea igual a 7
while True:
    menu()
    op = int(input("Ingrese la opcion"))
    numero1, numero2 = numeros_recibidos()
    if op == 0:
        print("ERROR")  # Opción incorrecta
    elif op == 1:
        print(f"La suma de ({numero1} + {numero2}) es: {numero1 + numero2}")  # Suma
    elif op == 2:
        print(f"La resta de ({numero1} - {numero2}) es: {numero1 - numero2}")  # Resta
    elif op == 3:
        print(f"La multiplicación de ({numero1} * {numero2}) es: {numero1 * numero2}")  # Multiplicación
    elif op == 4:
        print(f"La división de ({numero1} / {numero2}) es: {(numero1 / numero2):.2f}")  # División con dos decimales
    elif op == 5:
        print(f"La división entera de ({numero1} // {numero2}) es: {numero1 // numero2}")  # División entera
    elif op == 6:
        print(f"La exponenciación de ({numero1} ** {numero2}) es: {numero1 ** numero2}")  # Exponenciación
