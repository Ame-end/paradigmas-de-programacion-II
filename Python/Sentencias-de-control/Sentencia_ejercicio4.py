'''
Nombre: Amelia Mendoza López
Fecha:24/10/2024
Descripción: Implementación de condicionales
'''

print("************* RESTRICCIÓN DE EDAD***********")
# Solicitar edad
#Realiza un casting de varibles
edad = int(input("Ingresa tu edad: "))

# Solicitar cantidad de dinero
dinero = float(input("Ingresa el dinero con el que cuentas: "))

# Verificar las condiciones de entrada
if edad >= 18 and dinero >= 250.0:
    mensaje = "¡Bienvenido a tu mejor bar!"
else:
    mensaje = "Lo sentimos, ya estamos por cerrar!"

print(mensaje)
