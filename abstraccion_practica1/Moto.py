from abstraccion_practica1.Vehiculo import Vehiculo


class Moto(Vehiculo):
    def __init__(self, marca):
        super().__init__(marca)

    def arrancar(self):
        print(f"La moto de marca: '{self.marca}' arranca con botón.")

moto1 = Moto("Benelli")
moto1.arrancar()