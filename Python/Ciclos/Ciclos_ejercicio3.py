'''
Nombre: Amelia Mendoza López
Fecha: 20/10/2024
Descripción: Se realiza un calculadora para ejemplicar el comportamiento del ciclo while
'''

print("************ CALCULADORA ************")

# Se realiza el casting de variables para realizar la conversión
# de la parte cadena a entero
numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))

print("Suma....[1]")
print("Resta....[2]")
print("Multiplicación....[3]")
print("División..........[4]")
print("Exponenciación entera....[5]")
print("Exponenciación........[0]")
print()
op = int(input("Digite operación"))

i = 0

# Ciclo while para ejecutar el menú de opciones mientras 'i' no sea igual a 7
while i != 7:
    # Evaluación de la operación a realizar basada en el valor de 'op'
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
