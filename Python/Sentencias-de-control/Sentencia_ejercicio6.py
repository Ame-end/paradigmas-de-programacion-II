'''
Nombre: Amelia Mendoza López
Fecha:27/10/2024
Descripción: Determina el promedio final de un semestre
'''

print("*************TOUR TURISTÍCO ECOTURIXTLÁN***********")

#Precio de adulto: $200
#Precio de niño: $100

# Solicita el nombre de la persona a cargo
nombre = input("Ingresa el nombre de la persona a cargo: ")

# Establecer los precios
adulto_precio = 200.0
niño_precio = 100.0

# Pedr la cantidad de adultos y niños para el ingreso del tour
num_adultos = int(input("Ingresa el número de adultos: "))
num_niños = int(input("Ingresa el número de niños: "))

# Preguntar el día de la semana
dia_semana = input("Ingresa el día de la semana de la visita: ").lower()


# Calcula el costo total sin descuento
costo_total = (num_adultos * adulto_precio) + (num_niños * niño_precio)
descuento=costo_total*0.10
# Aplicar descuento del 10% si el día es lunes, martes o jueves
if dia_semana =="lunes" or dia_semana=="martes" or dia_semana=="jueves":
    costo_final=costo_total-descuento  # Aplicar el descuento del 10%

# Muestra los detalles del cliente y el costo total
print(f"La reserva para {nombre}:")
print(f"Día de la visita: {dia_semana}")
print(f"Total a pagar: ${costo_total:.2f}")
