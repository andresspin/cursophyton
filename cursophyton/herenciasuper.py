class Persona():
    def __init__(self, nombre, edad, lugar_residencia):
        self.nombre = nombre
        self.edad = edad
        self.lugar_residencia = lugar_residencia

    def descripcion(self):
        print("Nombre: ", self.nombre, "\nEdad: ", self.edad, "\nResidencia :", self.lugar_residencia)


class Empleado(Persona):
    def __init__(self, salario, antiguedad, nombre_empl, edad_empl, residencia_empl):
        super().__init__(nombre_empl, edad_empl, residencia_empl)  # esta llamando al metodo constructor (init) de la
        # clase padre
        self.salario = salario
        self.antiguedad = antiguedad

    def descripcion(self):
        super().descripcion()
        print("Salario : ", self.salario, "\nAntoguedad : ", self.antiguedad)

print("-------------------------------------------------------------------------")
andres = Persona("Andres", 37, "Bogota")
andres.descripcion()

print("-------------------------------------------------------------------------")
enrique = Empleado(1500, 15, "Enrique", 63, "Colombia")
enrique.descripcion()

print("-------------------------------------------------------------------------")

#isinstance

print(isinstance(enrique, Persona))
print(isinstance(enrique, Empleado))
