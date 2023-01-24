# evaluar el salario de algunos trabajadores de una empresa

salario_presidente = int(input("introduce salario presidente :"))
print("Salario Presidente : " + str(salario_presidente))

salario_director = int(input("introduce salario director :"))
print("Salario director : " + str(salario_director))

salario_jefe_area = int(input("introduce salario jefe de area : "))
print("Salario jefe de area : " + str(salario_jefe_area))

salario_administrativo = int(input("introduce salario administrativo : "))
print("Salario administrativo : " + str(salario_administrativo))

if salario_administrativo < salario_jefe_area < salario_director < salario_presidente:
    print("Todo funciona correctamente")
else:
    print("Algo falla en esta empresa")
