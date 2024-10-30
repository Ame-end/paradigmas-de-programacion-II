'''
Nombre: Amelia Mendoza López
Fecha:24/10/2024
Descripción:
'''

# Solicitar la cantidad comprada
compra = float(input("Cantidad de la compra en 'La cona': "))

# Preguntar si tiene membresía
membresia = input("¿Cuenta con membresía?: ")

tiene_membresia=membresia.lower()=="si"

# Calcular el descuento según las condiciones
if tiene_membresia:
    if compra >= 1000.0:
        descuento = 0.08  # 8% de descuento si la compra es mayor o igual a 1000
    else:
        descuento = 0.05  # 5% de descuento en cualquier compra con membresía
else:
    descuento = 0.0  # Sin membresía, sin descuento
    print("No tiene descuento, ¡le invitamos a ser miembro!")

# Calcular total a pagar con el descuento aplicado
total_descuento = compra * descuento
total_pagar = compra - total_descuento

# Mostrar el descuento y el total a pagar con dos decimales
print(f"Descuento aplicado: ${total_descuento:.2f}")
print(f"Total a pagar: ${total_pagar:.2f}")
