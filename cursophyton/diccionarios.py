# DICCIONARIOS son como array asociativo u objeto

miDiccionario = {"Alemania": "Berlin", "Francia": "Paris", "England": "London"}

# accedemos a cada elemento asi

print(miDiccionario["Francia"])  # Paris
print(miDiccionario["Alemania"]) # Berlin
print(miDiccionario)             # {'Alemania': 'Berlin', 'Francia': 'Paris', 'England': 'London'}


# agregar elementos a un diccionario
miDiccionario["Italia"] = "Milan"
print(miDiccionario)          # {'Alemania': 'Berlin', 'Francia': 'Paris', 'England': 'London', 'Italia': 'Milan'}

# sobreescribir o asignar un valor auna clave
miDiccionario["Italia"] = "Roma"
print(miDiccionario)          # {'Alemania': 'Berlin', 'Francia': 'Paris', 'England': 'London', 'Italia': 'Roma'}

# como eliminar elementos
del miDiccionario["England"]
print(miDiccionario)


# se pueden crear claves con todo tipo de dato
miDiccionario2 = {"Andres" : "Espinosa", 9: "Falcao", "lalala": 1.5}
print(miDiccionario2)


# asignar clave a cada valor

tuplap = ["España", "Francia", "England", "Alemania"]
miDiccionario3 = {tuplap[0]: "Madrid", tuplap[1]: "Paris", tuplap[2]: "London", tuplap[3]: "Berlin"}
print(miDiccionario3)
print(miDiccionario3["Francia"])


# asignar una serie de valores desde un tupla

miDiccionario3 = {"Nombre": "Radamel", 9: "Falcao", "lalala": 1.5, "titulos": {"temporadas": [2011, 2012, 2014, 2017]}}
print(miDiccionario3)

# acceder a claves y valores

print(miDiccionario3.keys())   # dict_keys(['Nombre', 9, 'lalala', 'titulos'])
print(miDiccionario3.values()) # dict_values(['Radamel', 'Falcao', 1.5, {'temporadas': [2011, 2012, 2014, 2017]}])
print(len(miDiccionario3))










