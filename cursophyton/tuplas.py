# TUPLAS : listas que no se pueden modificar ni realizar busquedas(index), se puede tomar una porcion pero retorna
# otra tupla, no deja añadir ni borrar(append,extend,remove) pero si se puede comprobar
# si hay un elemento emn la  tupla (element in miLista)

miTupla = (1, 2, 3)

print(miTupla[2])

# convertir tupla en lista

milista = list(miTupla)
print(milista)  # [1, 2, 3]
print(miTupla)  # (1, 2, 3)

# convertir lista en tupla
lista2 = [9, 7, 8]
tupla2 = tuple(lista2)
print(tupla2)

# validar si hay elementos en la tuipla
print(9 in tupla2)  # true
print(1 in tupla2)  # false

# saber cuantos elementos se encuentran en una tupla

print(tupla2.count(8))

# saber la longitud o cantidad de elementos de una tupla
print(len(tupla2))

# tupla unitaria(con un unico elemento) debe llevar la coma despues del elemento

tupla3 = ("Andres",)
print(len(tupla3))

# otra forma de realizar un tupla sin parentesis

tupla4 = 9, 7, 8
print(tupla4)  # (9, 7, 8)

# almacenar dentro de variables con los elelmntos de un tupla..DESEMPAQUETADO

tupla5 = ("a", 1, "b", 2, "c", 3)
letra1, num1, letra2, num2, letra3, num3 = tupla5
print(letra1)
print(num1)
print(letra2)
print(num2)
print(letra3)
print(num3)