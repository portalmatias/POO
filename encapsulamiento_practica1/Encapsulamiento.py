class Vehiculo:
    def __init__(self, marca, modelo, kilometro):
        self.marca = marca
        self.modelo = modelo
        self.__kilometro = kilometro

    def mostrar_info(self):
        print( f"""
        Marca: {self.marca}
        Modelo: {self.modelo}
        Kilometros: {self.__kilometro}
        """)

    def _calcular_consumo(self):
        consumo = self.__kilometro * 0.5
        return consumo

    @property
    def kilometro(self):
        return self.__kilometro

    @kilometro.setter
    def kilometro(self, nuevo_kilometro):
        self.__kilometro = nuevo_kilometro
        print(f"Los kilometros ahora son: {nuevo_kilometro}. Consumo ahora: {self._calcular_consumo()}")

vehiculo1 = Vehiculo("vw", "golf", 15000)

vehiculo1.mostrar_info()


vehiculo1.kilometro = 20000
