class Carro():
    def desplazamiento(self):
        print("Me muevo en 4 ruedas")


class Moto():
    def desplazamiento(self):
        print("Me muevo en 2 ruedas")


class Camion():
    def desplazamiento(self):
        print("Me muevo en 6 ruedas")


print("-----------------------------------------------------------------------------------------------------------")
miVehiculo = Moto()
miVehiculo.desplazamiento()

miOtroVehiculo = Carro()
miOtroVehiculo.desplazamiento()

miTercerVehiculo = Camion()
miTercerVehiculo.desplazamiento()

print("-----------------------------------------------------------------------------------------------------------")


def desplazamientovehiculo(vehiculo):
    vehiculo.desplazamiento()


miVehiculo3 = Carro()

desplazamientovehiculo(miVehiculo3)