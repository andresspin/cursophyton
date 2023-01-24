# Operadores logicos AND OR IN
# Distancia a la que vive un alumno del colegio

print("Programa de becas año 2023")
distancia_escuela = int(input("Que distancia hay de la escuela a tu casa en KM : "))
print(distancia_escuela)

num_hermanos = int(input("Introduce el numero de hermanos que tienes : "))
print(num_hermanos)

salario_familiar = int(input("Introduce el salario anual familiar : "))


if distancia_escuela>40 and num_hermanos > 2 or salario_familiar <= 20000:
    print("Felicidades obtuviste la beca")
else:
    print("Lo sentimos no aplicas para la beca")




# ejercicio de alumno que escoge asignatura
# lower y upper minusculas y mayusculas

print("Asignaturas lectivas año 2023")
print("Informatica Grafica-Pruebas de software-Usabilidad y accesibilidad")
opcion = input("Escoge la asignatura deseada : ")
asignatura = opcion.lower()

if asignatura in ("informatica grafica", "pruebas de software", "usabilidad y accesibilidad"):
    print(asignatura + " es una asignatura disponible")
else:
    print(asignatura + " no esta contemplado en el programa ")




