contador = 0
miEmail = input("Indicanos tu email : ")

for i in miEmail:
    if i == "@" or i == ".":
        contador= contador+1
        email = True

if contador == 2:
    print("Si corresponde a un email")
else:
    print("No corresponde a un email")


#Con range se evalua inica en 5...terminaria en el 49....e ira de 3 en 3

for i in range(5, 50, 3):  # valor de la variable 5-valor de la variable 8-valor de la variable 11-valor de la
    # variable 14
    print(f"valor de la variable {i}")


# ejercicio de email con range

valido = False

email1 = input("Indica email : ")

for i in range(len(email1)):
    if email1[i]=="@":
        valido = True

if valido:
    print("El email es correcto")
else:
    print("Email incorrecto")
