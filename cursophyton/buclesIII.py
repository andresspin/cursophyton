i=1

while i<=10:
    print("Ejecucion" + str(i))
    i=i+1

print("Termino la ejecucion")



edad = int(input("ingresa la edad : "))

while edad < 0 or edad > 100:
    print("Esta edad es incorrecta no sirve")
    edad = int(input("ingresa la edad : "))

print("Gracias por colaborar")
print("Edad del aspirante " + str(edad))



