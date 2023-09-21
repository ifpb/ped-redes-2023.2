from abc import ABC, abstractmethod


class Veiculo(ABC):
    def __init__(self, marca, modelo, ano, valor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    @property
    @abstractmethod
    def limite_km(self):
        pass

    @abstractmethod
    def calcular_imposto(self):
        pass

    def __str__(self):
        return f"""
        Marca: {self.marca},
        Modelo: {self.modelo},
        Ano: {self.ano},
        Valor: {self.valor},
        Limite de quilometragem: {self.limite_km},
        Imposto: {self.calcular_imposto()}
        """

class Automovel(Veiculo):
    def calcular_imposto(self):
        return self.valor * 0.10

    @property
    def limite_km(self):
        return 100000

class Motocicleta(Veiculo):
    @property
    def limite_km(self):
        return 50000
    def calcular_imposto(self):
        return self.valor * 0.05


if __name__ == '__main__':
    automovel = Automovel("Ford", "Ka", 2010, 10000)
    print(automovel)
    motocicleta = Motocicleta("Honda", "Biz", 2015, 5000)
    print(motocicleta)