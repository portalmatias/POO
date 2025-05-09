from abc import ABC, abstractmethod


class Vehiculo(ABC):
    def __init__(self, marca, año, valor_base):
        self.marca = marca
        self.año = año
        self.valor_base = valor_base

    @abstractmethod
    def calcular_impuesto(self):
        pass

    def mostrar_info(self):
        print(f"Marca: {self.marca} - Año: {self.año} - Valor base: {self.valor_base}")