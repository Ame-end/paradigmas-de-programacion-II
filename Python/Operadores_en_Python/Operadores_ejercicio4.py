'''
Nombre:Amelia Mendoza López
Fecha:
Descripción:Implementación de los operadores lógicos

Problema.
    * Determinará (T/F) de acuerdo con la expresión (exp1 ó exp2)
        y (exp3 ó exp4)
    a)Pida al usuario con valores booleanos (V/F)
    b) Obtener el resultado de la expresión booleana de acuerdo a
        los valores ingresados
    c) Muestre el resultado en consola con valores booleano(T/F)
'''
print("************ EVALUAR EXPRESIONES ************")

# Se solicitan los valores booleanos del usuario y convertirlos a True o False
# Lower - convierte la respuesta del usuario a minúsculas y comparamos con "v"

exp1 = input("Digíte el valor para exp1 (V/F): ")
resuExp1 = exp1.lower() == "v"  # True si el usuario ingresa "V", False en caso contrario

exp2 = input("Digíte el valor para exp2 (V/F): ")
resuExp2 = exp2.lower() == "v"  # True si el usuario ingresa "V", False en caso contrario

exp3 = input("Digíte el valor para exp3 (V/F): ")
resuExp3 = exp3.lower() == "v"  # True si el usuario ingresa "V", False en caso contrario

exp4 = input("Digíte el valor para exp4 (V/F): ")
resuExp4 = exp4.lower() == "v"  # True si el usuario ingresa "V", False en caso contrario

# Se aplica el comportamiento del operador "and" el cual se encuentra anidada con el resultado
# booleano de los operadores or
resultado = (resuExp1 or resuExp2) and (resuExp3 or resuExp4)

# Mostrar el resultado en consola como valor booleano (True o False)
print("Resultado de la expresión:", resultado)
