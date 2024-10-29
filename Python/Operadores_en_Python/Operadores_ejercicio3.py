'''
Nombre: Amelia Mendoza López
Fecha: 21/10/2024
Descripción: Se realiza un sistema de autentificación

Problema:
    a) Internamente declare dos cadenas constantes, para el usuario
       y otra para la contraseña
    c) Pida al usuario una cadena con la contraseña
    d) Si ambas cadenas son iguales a las cadenas declaradas internamente
       entonces el usuario se autenticó correctamente
    d) Muestre el resultado en consola con valor booleano (true/false)
    nota: No se implementará "lower"
'''
print("************ Autentificación del usuario ************")

# Declaración de usuario y contraseña constantes
usuario_interno = "usuario01"
contraseña_interno = "KwA123"

# Solicitar nombre de usuario y contraseña al usuario
nombre_usuario = input("Ingresa tu usuario: ")
contraseña_usuario = input("Ingresa tu contraseña: ")

# Verificar si el usuario y la contraseña son correctos a través de la condición lógica "and"
# El valor booleano se almacena en la variable "verificar"
verificar = (nombre_usuario == usuario_interno) and (contraseña_usuario == contraseña_interno)

print("¿Usuario autentificado?:",verificar)
