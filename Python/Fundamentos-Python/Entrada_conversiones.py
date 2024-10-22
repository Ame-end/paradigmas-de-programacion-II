'''
Nombre: Amelia Mendoza López
Fecha: 18/10/2024
Descripción:
Conversión de cadenas a int, float y boolean mediante la interacción con consola.
'''

# Comentar sobre las funciones anidadas.
print("****   Datos de los alumnos    *****")
nombre = input("Ingresa el nombre: ")  # Se le asigna a nombre una variable de tipo cadena
# Se realiza un casting de variables, para asignar un dato de tipo entero a semestre
semestre = int(input("Ingresa el no. de semestre: "))
# Se hace un casting de variables para asignarle un dato de tipo flotante a promedio
promedio = float(input("Ingresa el promedio: "))
es_mujer = input("¿Es mujer (Si/No)?: ")

# No es posible convertir directamente una cadena a un valor booleano.
# Por ello, utilizamos la misma variable, convertimos a  minúsculas y lo comparamos con la cadena "si".
es_mujer = es_mujer.lower() == "si"

# Se imprimen los datos del alumno.
# Comentar  qué es lo que realiza {promedio:.2f} probando con números diferentes.
print()

'''
La instrucción ".2f" se refiere a la cantidad de decimales que se encontrarán después 
del "."
2 -> hace referencia a la cantidad de decimales
f -> indica que pertence a un formato de número flotante
'''
print(
    f"El alumno {nombre} cursa el {semestre} semestre con un promedio de {promedio:.2f}. Además, es mujer: {es_mujer}."
)
