nombreUsuario = input("Introduce el usuario : ")
print("El nombre en mayuscula :", nombreUsuario.upper())
print("El nombre en minuscula :", nombreUsuario.lower())
print("El nombre nompropio :", nombreUsuario.capitalize())
print("El nombre en mayuscula :", nombreUsuario.upper())
print("Es digito :", nombreUsuario.isdigit())

print("____________________________________________________________________________________________________")

edad = input("Ingresa tu edad : ")

while edad.isdigit() == False:
    print("Por favor ingresa un numero")

    edad = input("Ingresa tu edad : ")

if int(edad) > 18:
    print("Puedes Pasar")
else:
    print("no puedes pasar")
