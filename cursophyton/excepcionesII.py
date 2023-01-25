def divide():
    try:
        op1 = (float(input("Introduce el primer numero : ")))
        op2 = (float(input("Introduce el segundo numero : ")))
        print("La division es : " + str(op1 / op2))
    except ValueError:
        print("el valor introducido es errado")
    except ZeroDivisionError:
        print("No se puede dividir entre cero")
    finally:
        print("Calculo finalizado")


divide()
