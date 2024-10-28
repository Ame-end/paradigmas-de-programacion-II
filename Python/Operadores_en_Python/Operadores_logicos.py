'''
Nombre: Amelia Mendoza López
Fecha: 20/10/2024
Descripción: Se muestra el comportamiento de los
operadores lógicos como and, or y not
'''

print("************ COMPARACIÓN DE CADENAS ************")

'''
Se pide al usuario que ingrese SI/NO,
la cadena se guarda en la variable "primer_cadena"
'''
primer_cadena = input("Ingresa SI o NO: ")
'''
            lower - Devuelve la cadena ingresada en un formato
            donde todos sus caracteres esten en minúscula.
            Y lo compará con la cadena "si", almacenando un valor 
            booleano (true/false) en "resultado"
            
'''
resultado = primer_cadena.lower() == "si"

segunda_cadena = input("Ingresa SI o NO: ")
resultado2 = segunda_cadena.lower() == "si"

'''
    Los operadores lógicos son utlizados para evaluar expresiones lógicas
    >> and: retorna un valor verdadero (true) si ambos operadores son verdaderos
    >> or: retorna un valor verdadero (true) si al menos un operador es verdadero
    >> not: invierte el valor del operador
'''
print(f"Ambos valores son iguales? {resultado and resultado2}")
print(f"Uno de los valores es verdadero? {resultado or resultado2}")
print(f"Negación del primer valor: {not resultado}")
print(f"Negación del segundo valor:  {not resultado2}")
