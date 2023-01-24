#Continue -pass-else
#Continue : salta u omite una iteracion del while
#pass: Devuelve null sin entrar en el bucle while
#else: O si no


for letra in "Phyton":
    if letra == "h":
        continue
        #omitira la linea del print
    print("viendo la letra " + letra)


nombre = "Andres Espinosa"
contador = 0
for i in nombre:
    if i == " ":
        continue
    contador += 1
print(contador)


#while True:
 #pass  para implementar mas tarde omite el bucvle





email2 = input("Email aqui : ")

for i in email2:
    if i == "@":
        arroba = True
        break;
else:
    arroba = False

print(arroba)