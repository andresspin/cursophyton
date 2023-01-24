print("Verificacion de acceso")

edad_usuario = int(input("Introduce tu edad : "))

if edad_usuario > 18 :
    print("Puedes pasar")
elif edad_usuario> 100 :        #recuerda que el elif es para incluir el else en todos los if
    print("Edad incorrecta")
else:
    print("No puedes pasar")

print("El programa ha finalizado")


print("Verificacion de Notas______________________________________________________________________")

nota_alumno = int(input("Introduce tu nota : "))

if nota_alumno < 5:
    print("Insuficiente")
elif nota_alumno < 6:        #recuerda que el elif es para incluir el else en todos los if
    print("Aceptable")
elif nota_alumno < 9:
    print("Notable")
else:
    print("Excelente")

print("El programa ha finalizado")



