# lanzamiento de excepciones - instruccion raise
import math


# def evalua_edad(edad):
#   if edad < 0:
#      raise TypeError("No hay edades negativas")

# if edad < 20:
#       return "Eres muy joven"
#   elif edad < 40:
#      return "eres juven"
#   elif edad < 65:
#      return "eres madurio"
#   elif edad < 100:
#      return "vas a morir"


# print(evalua_edad(-15))

def calculaRaiz(num1):
    if num1 < 0:
        raise ValueError("El numero no puede ser negativo")
    else:
        return math.sqrt(num1)


op1 = int(input("Introduce el numero : "))

try:
    print(calculaRaiz(op1))

except ValueError as ErrorDeNegativo:
    print(ErrorDeNegativo)

print("Termina programa")
