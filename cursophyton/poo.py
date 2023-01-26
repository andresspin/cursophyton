# los objetos tienen propiedades-estado-comportamiento

class Coche():

    def __init__(self):  # aqui se crea el constructor
        self.largoChasis = 250  # propiedades
        self.anchoChasis = 120
        self.__ruedas = 4  # Encapsulamiento = no permitira cambiar la pripiedad con los dos guines bajos
        self.enMarcha = False

    # metodos
    def arrancar(self, arranquemos):
        self.enMarcha = arranquemos
        if self.enMarcha:
            chequeo = self.__chequeo_interno()

        if self.enMarcha and chequeo:
            return "el coche esta en marcha"

        elif self.enMarcha and chequeo == False:
            return "Algo paso en el chequeo no se puede arrancar"
        else:
            return "el coche esta quieto"

    def estado(self):
        print("El vehiculo tiene : ", self.__ruedas, "ruedas. Un ancho de ", self.anchoChasis, "y un largo de : ",
              self.largoChasis)

    def __chequeo_interno(self):         # tamien se hace el metodo encapsulado
        print("realizando chequeo interno")
        self.gasolina = "ok"
        self.aceite = "ok"
        self.puertas = "cerradas"

        if self.gasolina == "ok" and self.aceite == "ok" and self.puertas == "cerradas":
            return True
        else:
            return False


# aqui se crea un objeto o un ejemplar
miFerrari = Coche()

# se accede a las propiedades
print(miFerrari.arrancar(True))
miFerrari.estado()

print("-------------------------------Aqui crearemos el otro objeto o instancia---------------------------")

miBmw = Coche()
miBmw.ruedas = 5
print(miBmw.arrancar(False))
miBmw.estado()

# Encapsulacion = Proteger las propiedades para no modificarlas fuera de la clase self.__ruedas
