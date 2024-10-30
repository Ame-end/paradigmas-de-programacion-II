"""
Nombre: Amelia Mendoza López
Fecha: 29 de Octubre del 2024
Descripción: Ejemplificación de una cuenta bancaria
"""

saldo_usuario = 0.0
i = 1
while i != 0:
    print("***********BANCO AZTECA***************")
    print("1. Consulta tu saldo")
    print("2. Ingresar dinero")
    print("3. Retirar dinero")
    print("0. Salir")

    op = int(input("opción: "))

    if op == 1:
        # Consultar tu saldo
        print(f"Tu saldo es de ${saldo_usuario}")
    elif op == 2:
        # Ingresar el dinero
        dinero_ingresado = float(input("Ingrese cantidad: "))
        # Actualiza el valor del saldo
        saldo_usuario += dinero_ingresado
        print(f"Saldo actual: ${saldo_usuario}")
    elif op == 3:
        # Retirar el dinero
        dinero_ingresado = float(input("Ingrese cantidad: "))
        # Actualiza el valor del saldo retirado
        saldo_usuario -= dinero_ingresado
        print(f"Saldo actual: ${saldo_usuario}")
    elif op == 0:
        # sale del ciclo
        i = 0
    else:
        print("Opcion no válida...")
