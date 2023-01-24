import math

print("Calcula la raiz cuadrada")

numero = int(input("Ingrese un numero : "))

intentos = 0


while numero < 0:
    print("No se puede hallar la raiz de un numero negativo")

    if intentos == 2:
        print("Demasiados intentos")
        break;

    numero = int(input("Ingrese un numero"))
    if numero < 0:
        intentos = intentos+1

if intentos < 2:
    solucion= math.sqrt(numero)
    print("La raiz cuadrada de "+str(numero)+" es "+str(solucion))
