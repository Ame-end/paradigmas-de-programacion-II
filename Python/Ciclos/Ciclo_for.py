'''
Nombre: Amelia Mendoza López
Fecha:29/10/2024
Descripción: Fundamentos para el ciclo for

          CICLO FOR
El bucle for se utilizado para recorrer los elementos de un
objeto iterable (lista, tupla, conjunto, diccionario..) y
ejecutarun bloque de código. En cada paso de la iteración
se tiene en cuenta a un único elemento del objeto iterable
sobre el cuál se puede aplicar una serie de operaciones

Sintaxis
    for <elem> in <iterable>:
        <código>
'''

print("************EJEMPLO DE CICLO FOR****************")

cadena_uno = input("Ingresa una cadena: ")
# "caracter" itera dentro de cada carácter de "cadena_uno"
for caracter in cadena_uno:
    print(caracter, end="-")


print("**************")
print("*******ALUMNOS DE QUINTO SEMESTRE*******")
alumnos_quinto = [
    "Albert",
    "Kevin",
    "Elton",
    "Diana",
    "Edén",
    "Amelia",
    "Sergio"
    ]
# "alumno" itera dentro de cada carácter de "alumnos_quinto"
for alumno in alumnos_quinto:
    print(f"Hola {alumno}")

