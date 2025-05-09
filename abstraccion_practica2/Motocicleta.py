from abstraccion_practica2.Vehiculo import Vehiculo


class Motocicleta(Vehiculo):
    def __init__(self, marca, año, valor_base, cilindrada):
        super().__init__(marca, año, valor_base)
        self.cilindrada = cilindrada

    def calcular_impuesto(self):
        if self.cilindrada == 125:
            print(f"Impuesto agregado: {self.valor_base * 0.50 + self.valor_base}")
        elif self.cilindrada == 250:
            print(f"Impuesto agregado: {self.valor_base * 0.75 + self.valor_base}")
        elif self.cilindrada >= 500:
            print(f"Impuesto agregado: {self.valor_base * 1 + self.valor_base}")
        else:
            print("Error no se agrego la cilindrada.")

moto1 = Motocicleta("Tornado", "2025", 10000, 250)
moto1.mostrar_info()
moto1.calcular_impuesto()