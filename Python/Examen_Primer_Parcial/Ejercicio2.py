'''
NOMBRE: Amelia Mendoza López
FECHA:30/10/2024
DESCRIPCIÓN DEL PROBLEMA:

Este programa determina el área y el perímetro de un rectángulo o de un círculo.
Muestre el siguiente menú:

1) Calcular el área de un rectángulo.
2) Calcular el perímetro de un rectángulo.
3) Calcular el área de un círculo.
4) Calcular el perímetro de un círculo.
0) Salir.
Cualquier otro caso -> Mostrar un mensaje de "opción no válida".

'''

while True:
    print("------ ÁREA Y PERÍMETRO -------")
    print("NOTA: Ingrese cantidades flotantes"
          "si el número es entero marcar como '.00' ")
    print("Digite la opción de la figura:")
    print("ÁREA DE UN RECTÁNGULO....................[1]")
    print("PERÍMETRO DE UN RECTÁNGULO...............[2]")
    print("ÁREA DE UN CÍRCULO.......................[3]")
    print("PERÍMETRO DE UN CÍRCULO..................[4]")
    print("SALIR....................................[0]")

    opcion = int(input("OPCIÓN: "))

    if opcion == 1:
        print("ÁREA DE UN RECTÁNGULO")
        base_rect = float(input("Ingrese la BASE: "))
        altura_rect = float(input("Ingrese la ALTURA: "))
        area = base_rect * altura_rect
        print(f"El área del rectángulo es: {area}")

    elif opcion == 2:
        print("PERÍMETRO DE UN RECTÁNGULO")
        base_rect = float(input("Ingrese la BASE: "))
        altura_rect = float(input("Ingrese la ALTURA: "))
        perimetro = 2 * (base_rect + altura_rect)
        print(f"El perímetro del rectángulo es: {perimetro}")

    elif opcion == 3:
        print("ÁREA DE UN CÍRCULO")
        radio_circ = float(input("Ingrese el RADIO: "))
        area = 3.1416 * (radio_circ ** 2)
        print(f"El área del círculo es: {area}")

    elif opcion == 4:
        print("PERÍMETRO DE UN CÍRCULO")
        radio_circ = float(input("Ingrese el RADIO: "))
        perimetro = 2 * 3.1416 * radio_circ
        print(f"El perímetro del círculo es: {perimetro}")

    elif opcion == 0:
        print("Saliendo del programa.")
        break

    else:
        print("OPCIÓN INVÁLIDA.")

    print()
