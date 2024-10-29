'''
Nombre: Amelia Mendoza López
Fecha:27/10/2024
Descripción: Determina el promedio final de un semestre
'''

print("*************CALIFICACIÓN FINAL***********")

# Solicitar las tres calificaciones parciales y la del examen ordinario
# realizar un casting de varibles para convertir a un valor entero
# la cadena ingresada por le usuario
parcial1 = float(input("Ingresa la primera calificación parcial: "))
parcial2 = float(input("Ingresa la segunda calificación parcial: "))
parcial3 = float(input("Ingresa la tercera calificación parcial: "))
ordinario = float(input("Ingresa la calificación del ordinario: "))

# Calcular el promedio
promedio = (parcial1 + parcial2 + parcial3 + ordinario) / 4

#
if promedio >= 6.0:
    mensaje = "¡Felicidades! Aprobaste."
else:
    mensaje = "Lo siento, no aprobaste."

# Se muestra el letreo establecido en el if, así como el resulado
# del promedio
print(mensaje)
print(f"Promedio: {promedio:.1f}")
