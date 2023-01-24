# (*ciudades) el asterisco indica podemos pasar muchos argumentos o parametros y se recibiran como tupla
# con el for anidado se accede a cada ciudad y encontrar sus letras
def devuelve_ciudades(*ciudades):
    for elemento in ciudades:
        # for subElemento in elemento:
        yield from elemento


ciudades_devueltas = devuelve_ciudades("Madrid", "Bogota", "Milan", "Manchester")

print(next(ciudades_devueltas))  # M
print(next(ciudades_devueltas))  # a
