'''
                    AUTOR
    Nombre: Alberto Martínez Barbosa
***********************************************
Nombre del alumno: Amelia Mendoza López
Fecha:22/ 10/2024
Descripción: Muestra del comportamiento de los operadores aritméticos.
'''

"""
Los operadores aritméticos en Python son los siguientes:
- Suma (+).
- Resta (-).
- Multiplicación (*).
- División (/).
- División entera (//).
- Módulo (%).
- Exponenciación (**).
"""

# Se solicitan dos números enteros al usuario.
numero1 = int(input("Ingresa un número entero: "))
numero2 = int(input("Ingresa otro número entero: "))

# Se realizan las operaciones aritméticas.
print()
print("  ***   Ejemplos de uso de los operadores aritméticos   ***")

'''
CONCATENACIÓN con "f{" "}":
La letra "f" hace referencia a una "cadena formateada", esto indica 
la implementación de llaves dentro de la cadena, donde se 
almacenan los valores asignados a cada variable.
'''

print(f"La suma de ({numero1} + {numero2}) es: {numero1 + numero2}")
print(f"La resta de ({numero1} - {numero2}) es: {numero1 - numero2}")
print(f"La multiplicación de ({numero1} * {numero2}) es: {numero1 * numero2}")
print(f"La división de ({numero1} / {numero2}) es: {(numero1 / numero2):.2f}")    # Notar la forma para mostrar dos decimales.
print(f"La división entera de ({numero1} // {numero2}) es: {numero1 // numero2}")
print(f"El módulo de ({numero1} % {numero2}) es: {numero1 % numero2}")
print(f"La exponenciación  de ({numero1} ** {numero2}) es: {numero1 ** numero2}")

'''
 ***   Ejemplos consola  ***
 >>Número 1: 4
 >>Número 2: 8
La suma de (4 + 8) es: 12
La resta de (4 - 8) es: -4
La multiplicación de (4 * 8) es: 32
La división de (4 / 8) es: 0.50
La división entera de (4 // 8) es: 0
El módulo de (4 % 8) es: 4
La exponenciación  de (4 ** 8) es: 65536
'''