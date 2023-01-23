print("Programa de evaluacion de notas de alumnos")

# con esta instruccion  se detiene el programa hasta ingresar un valor
nota_alumno = input("introduce la nota del alumno: ")


def evaluacion(nota):
    valoracion = "Aprobado"
    if nota < 5:
        valoracion = "Reprobado"
    return valoracion


print(evaluacion(int(nota_alumno)))
# print(evaluacion(8))
# print(evaluacion(4))


# condicional que nos permite introducir por teclado la info
