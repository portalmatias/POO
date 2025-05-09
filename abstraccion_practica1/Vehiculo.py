from abc import ABC, abstractmethod

class Vehiculo(ABC):
    def __init__(self, marca):
        self.marca = marca

    @abstractmethod
    def arrancar(self):
        pass

