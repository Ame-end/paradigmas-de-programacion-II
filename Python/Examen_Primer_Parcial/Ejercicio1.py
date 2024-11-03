'''
NOMBRE: Amelia Mendoza López
FECHA:30/10/2024
DESCRIPCIÓN DEL PROBLEMA:

Este programa imprime en consola los números, separados por comas,
del 1 hasta un número ingresado por el usuario.

Sin embargo, se deben sustituir los siguientes valores:
> 3 o sus múltiplos por la palabra "Licenciatura".
> 5 y sus múltiplos por la palabra "Informática".
Múltiplos de 3 y 5 por la frase "Licenciatura en Informática" y se
imprima un salto de línea en lugar de la coma.
'''

print("--------------- MÚLTIPLOS DE 3 Y 5 -------------------")
VALOR_FINAL = int(input("Ingrese el último valor de la lista: "))

iterador = 1

while iterador <= VALOR_FINAL:
    if iterador % 3 == 0:
        numeracion = "Licenciatura"
    elif iterador % 5 == 0:
        numeracion = "Informática"
    else:

        numeracion = iterador

    print(numeracion, end=", ")
    iterador += 1
