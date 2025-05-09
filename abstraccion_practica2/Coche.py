from abstraccion_practica2.Vehiculo import Vehiculo


class Coche(Vehiculo):
    def __init__(self, marca, año, valor_base, tipo_combustible):
        super().__init__(marca, año, valor_base)
        self.tipo_combustible = tipo_combustible

    def calcular_impuesto(self):
        if self.tipo_combustible == "Gasolina":
            print("Impuesto agregado al auto con gasolina: ", self.valor_base * 0.10 + self.valor_base)
        elif self.tipo_combustible == "Diesel":
            print("Impuesto agregado al auto con diesel: ", self.valor_base * 0.15 + self.valor_base)
        elif self.tipo_combustible == "Electrico":
            print("Impuesto agregado al auto electrico: ", self.valor_base * 0.05 + self.valor_base)
        else:
            print("Tipo de combustible no valido.")

coche1 = Coche("vw", "2025", 30000, "Gasolina")
coche1.mostrar_info()
coche1.calcular_impuesto()