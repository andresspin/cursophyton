class Vehiculos():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enMarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self.enMarcha = True

    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True

    def estado(self):
        print("Marca: ", self.marca, "\nModelo : ", self.modelo, "\nEn Marcha: ", self.enMarcha, "\nAcelerando: ",
              self.acelera, "\nFrena : ", self.frena)


class Furgoneta(Vehiculos):
    def carga(self, cargar):
        self.cargado = cargar
        if self.cargado:
            return ""
        else:
            return "La furgoneta esta vacia"


# de esta manera se hace una clase Moto que hereda las propiedades de la clase Vehiculos
class Moto(Vehiculos):
    hstunt = ""

    def stunt(self):
        self.hstunt = "Voy en una sola rueda"

    # Para poder saber si esta en una rueda o no se sobreescribe el metodo estado de la clase Vehiculo
    # en la clase que hereda(Moto) y ya se puede utilizar el metodo stunt para retornar la frase :
    # "Voy en una sola rueda"
    def estado(self):
        print("Marca: ", self.marca, "\nModelo : ", self.modelo, "\nEn Marcha: ", self.enMarcha, "\nAcelerando: ",
              self.acelera, "\nFrena : ", self.frena, "\nManiobra : ", self.hstunt)


class Electricos(Vehiculos):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        self.autonomia = 100

    def cargarEnergia(self):
        self.cargando = True


print("-------------------------------------MOTO-----------------------------------------------------------------_____")
miMoto = Moto("Honda", "CBR")
miMoto.stunt()
miMoto.estado()
print("-------------------------------------FURGONETA-----------------------------------------------------------------")
miFurgoneta = Furgoneta("Volkswagen", "1972")
miFurgoneta.arrancar()
miFurgoneta.estado()
miFurgoneta.carga(True)
print("-------------------------------------FURGONETA-----------------------------------------------------------------")


# OJO  A ESTA CLASE--Bicileta tendra herencia multiple

class BicicletaElectrica(Electricos, Vehiculos):
    pass


miBici = BicicletaElectrica("GW", "Ocelot") # no dejaria pq el cvonstructor q usa es el de Electricos pq esta de primero
