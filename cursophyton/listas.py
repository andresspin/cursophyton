# Una lista es exactamente lo mismo que un array

miLista = ["Andres", "Sergio", "Enrique", "Messi"]

print(miLista[:])  # Todo el array
print(miLista[0])  # Andres
print(miLista[-2])  # negativo se va hacia atras y dedvuelve "Enrique"
print(miLista[0:2])  # Porcion de array devuelve el indice 0 y 1 ['Andres', 'Sergio']
print(miLista[2:3])  # Porcion de array devuelve el indice 2 ['Enrique']

# Con append, se introducira al final
miLista.append("Roman")
print(miLista[:])  # ['Andres', 'Sergio', 'Enrique', 'Messi', 'Roman']

# con insert se ubica en la posicion o indice que se indique
miLista.insert(2, "Radamel")  # ['Andres', 'Sergio', 'Radamel', 'Enrique', 'Messi', 'Roman']
print(miLista[:])

# con extend incluyes los elementos en el arreglo
miLista.extend(["Lautaro", "Enzo", "Dibu"])  # ['Andres', 'Sergio', 'Radamel', 'Enrique', 'Messi', 'Roman', 'Lautaro',
# 'Enzo', 'Dibu']
print(miLista[:])

# nos devuelve el indice del elemento
print(miLista.index("Sergio"))  # 1
print(miLista.index("Dibu"))  # 8

# comprobar si un elemento esta en una lista
print("Messi" in miLista)  # True
print("Pepe" in miLista)  # False

# eliminar elemento del array
miLista.remove("Lautaro")  # ['Andres', 'Sergio', 'Radamel', 'Enrique', 'Messi', 'Roman', 'Enzo', 'Dibu']
print(miLista[:])

# eliminar el ultimo elemento
miLista.pop()
print(miLista[:])  # ['Andres', 'Sergio', 'Radamel', 'Enrique', 'Messi', 'Roman', 'Enzo']

# agrega a la lista otra lista

miLista1 = ["Andres", 37, 1.80, True]
miLista2 = ["Sergio", 15, 1.79, False]

miLista3 = miLista1 + miLista2
print(miLista3)  # ['Andres', 37, 1.8, True, 'Sergio', 15, 1.79, False]

# repite las listas con el operador *

miLista4 = ["Andres", 37, 1.80, True] * 3
print(miLista4)  # ['Andres', 37, 1.8, True, 'Andres', 37, 1.8, True, 'Andres', 37, 1.8, True]
