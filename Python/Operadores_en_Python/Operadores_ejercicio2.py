'''
Nombre: Amelia Mendoza López
Fecha: 21/10/2024
Descripción: Se muestra el comportamiento de los
operadores lógicos como and, or y not
'''

print("************ UNIVERSIDAD DE LA SIERRA JUÁREZ ************")

# Solicitar al usuario si es estudiante de la UNSIJ
cadena_estudiante = input("¿Es estudiante de la UNSIJ?: ")

# Lower convierte la respuesta a minúsculas y verificar si es "si"
# el resultado booleano se almacena en la variable "estudiante"
estudiante = cadena_estudiante.lower() == "si"

# Solicitar al usuario si es profesor de la UNSIJ
cadena_profesor = input("¿Es profesor de la UNSIJ?: ")

# Lower convierte la respuesta a minúsculas y verificar si es "si"
# el resultado booleano se almacena en la variable "profesor"
profesor = cadena_profesor.lower() == "si"

# Si la varible 'estudiante' o 'profesor' es verdadero, el resultado será True
print(f"¿Pertenece a la comunidad de la UNSIJ?: {estudiante or profesor}")
