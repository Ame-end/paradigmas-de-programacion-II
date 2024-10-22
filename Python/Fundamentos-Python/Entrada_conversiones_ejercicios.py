'''
Nombre: Amelia Mendoza López
Fecha: 18/10/2024
Descripción: Se implementará la concatenación mediante llaves,
el casting de variables, así como la implementación de lower

Ejercicio:
a) Pida los datos de los profesores utilizando nombres de variables adecuadas, la función input y el casting:

Nombre (cadena).
No. de cubículo (int).
Horas de que imparte clase a la semana (float con 3 decimales).
¿Tiene más de 5 años en la unsij? (booleno).
b) Muestre los datos en consola de forma adecuada.

Nota: Asuma que el usuario siempre va a ingresar números cuando se requiera.
'''

print("++++++++++++++++ REGISTRO DE PROFESORES ++++++++++++++++")
'''
Se realiza el casting de variables con la finalizad de asignar 
el tipo de dato adecuado para cada variable
'''
nombre_profesor = input("Ingrese el nombre del profesor: ")
cubiculo_profesor = int(input("Ingrese el número de cubo del profesor: "))
horas_profesor = float(input("Horas que imparte clases a la semana: "))
# La respuesta se almacena como un dato de tipo String en la variable "tiempo_en_unsij"
tiempo_en_unsij = input("El profesor,¿Tiene más de 5 años en la UNSIJ(Si/No)?: ")
'''
1.- "Lower" convierte la cadena almacenada anteriormente a minúsculas
2.- "Lower" compara la cadena con "si"
3.- Si la comparación es exitosa se almacena "True" en la variable "tiempo_en_unsij"
4.- En caso contrario se almacenará "False"
'''
tiempo_en_unsij = tiempo_en_unsij.lower() == "si"

# Impresión de los datos del profesor
print("++++++++++++++++ DATOS DEL PROFESORES ++++++++++++++++")
print(f" El profesor {nombre_profesor} se encuentra en el cubículo {cubiculo_profesor}")
# ".3f" determinará los decimales que se encontrarán después del punto flotante
print(f" imparte {horas_profesor:.3f} horas a la semana y {tiempo_en_unsij} tiene más de")
print(" 5 años en la Univerisidad de la Sierra Juárez")
