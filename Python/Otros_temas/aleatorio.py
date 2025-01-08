import random

input("NÚMERO ALEATORIO")
print()
ite=int(input("Ingrese numero de iteraciones"))

i=1

while i<=ite:
    num = random.randint(5, 10)
    print(num)
    i+=1
