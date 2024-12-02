'''
CLASES:Molde o plantilla del cual proviene nuestro objeto
en ella se establece, los atributos o métodos que tendrá
un objeto

objetos
    -Caracteristicas: atributos del objeto
    -Acciones que puede realizar: métodos

'''

#Creación de una clase
class Humano:
    # metodo init
    # self - se guarda la referencia del objeto que se este creando
    def __init__(self):  # Definir método
        self.edad = 25  # Crear un atributo
        # self.edad = edad  # Crear un atributo
        print("Soy el nuevo objeto")

    # Definir un nuevo método
    def hablar(self, mensaje):
        print(mensaje)

# Se crea una instancia de la clase humano
# O se crea un objeto que tiene como plantilla a la clase humano
# pedro = Humano(26)
pedro = Humano()
# Acceder al método
pedro.hablar('Hola')  # Cambié 'raul' por 'pedro' porque 'raul' no está definido

# Acceder a un atributo
print("Soy Pedro y tengo ", pedro.edad)
