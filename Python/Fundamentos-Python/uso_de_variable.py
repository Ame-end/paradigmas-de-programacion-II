# Programa original elaborado por: Dr.Alberto Martínez Barbosa

"""
Nombre del alumno: Amelia Mendoza López
Descripción:
Fecha: 13/10/2024
"""
# Notas:
# En Python to.do es un objeto.
# Variable - una variable es un nombre que almacena un valor guardado en la memoria temporal.

# Toda variable requiere un valor inicial
semestre = 4         # "semestre" es una variable, que apunta a un objeto de tipo Int con valor de 3
print(semestre)      # imprime 3 como valor actual de semestre
semestre = 5         #La variable pierede el dato anterior, apuntando a un nuevo objeto de tipo Int con valor de 4
                     #perdiendo la referencia a la variable 3
print(semestre)      #imprime 4 como valor actual del semestre

# Creación de nuevas variables
nombre = "Amelia"   # "nombre" es una variable que almacena un dato de de tipo String
altura = 1.55       # "altura" es una variable que almacena un dato de tipo Float
edad = 19           # "edad" es una variable que almacena un dato de tipo Int

# Se imprimen las variables, añadiendo información adicional para comprender lo que se imprime
print("Nombre:", nombre) #Se mostrará: "Nombre: Amelia"
print("Semestre:", semestre) #Se mostrará: "Semestre: 5"
print("Altura: ", altura, "m.") #Se mostrará: "Altura: 1.55"
print("Edad: ", edad, "años.") #Se mostrará: "Edad: 19"

# Se modifican los valores de las variables y se mandan a imprimir
altura = 1.50 # altura aún almacena un dato de tipo Float, pero actualiza su valor
edad = 20 ## altura aún almacena un dato de tipo Int, pero actualiza su valor
print()
print("Valores modificados:") #Letrero para los valores modificados"
print("Nombre:", nombre) #Se mostrará: "Nombre: Amelia"
print("Semestre:", semestre) #Se mostrará: "Semestre: 5"
print("Altura: ", altura, "m.") #Se mostrará: "Altura: 1.50"
print("Edad: ", edad, "años.") #Se mostrará: "Edad: 20"

# Nota del autor: En Python, las variables son dinámicas, por lo que pueden
# almacenar otro tipo de dato en cualquier momento

edad = "treinta y uno"      # edad antes tenía el valor de 31 (Int)
print()
print("Edad (con otro tipo de dato):", edad)

#NOTA DEL AUTOR:
# Reglas para los nombres de las variables en Python:
# - Utilizar únicamente letras (mayúsculas o minúsculas), números y el guion bajo
# - La variable no puede iniciar con números
# - No se pueden utilizar palabras reservadas, ejemplos: if, else, True, class
# - Es sensible a mayúsculas y minúsculas. Por ejemplo, las palabras "Hola", "hola" y "HOLA" son consideradas diferentes.

#NOTAS DEL AUTOR:
# Buenas prácticas
# - Utilizar minúsculas para las palabras
# - Separar las palabras con el guion bajo
# - Utilizar nombres descriptivos de acuerdo a su uso. Por ejemplo: edad, en lugar de e.

# Ejemplos correctos y con buenas prácticas
fecha_nacimiento = "20 de diciembre del 2004" #Se le asigna un tipo una cadena, representando la fecha de nacimiento
clase = "Paradigmas de programación II"
horas_estudio = 4 #emplea el "_" para ejemplificar el espacion en blanco
nombre = "Amelia"
es_estudiante = True #La variable "es_estudiante" almacena un valor booleano, indicando que la persona es estudiante

# Ejemplos incorrectos (líneas comentadas porque marcan error) o de malas prácticas
f = "1 de enero del 2000" #mala práctica, pues "f" no es un nombre apropiado que pudiese describir la fecha de nacimiento
fechanacimiento = "1 de enero del 2000" #deberia separarse por "_", es el ejemplo de una mala práctica
# class = "Paradigmas de programación II" -> "class" es una palabra reservada y no es correcto implementarla como un nombre de
                                            #variable
# 8horas_estudio = 8 #Los nombres de variables no deben iniciar con números
Nombre = "A m e l i a"
NOMBRE = "AMELIA"

# Notar que las variables 'nombre', 'Nombre' y 'NOMBRE', son distintas
print()
print("Las variables son sensibles a mayúsculas y minúsculas:")
#Aunque la palabra sea la misma, python tomará a cada una de ellas como variables distintas
print("Variable nombre:", nombre)
print("Variable Nombre:", Nombre)
print("Variable NOMBRE:", NOMBRE)

