from abstraccion_practica1.Vehiculo import Vehiculo

class Auto(Vehiculo):
    def __init__(self, marca):
        super().__init__(marca)

    def arrancar(self):
        print(f"El auto de marca: {self.marca} arranca con llave.")

auto1 = Auto("Audi A1")
auto1.arrancar()