import math
from abc import ABC, abstractmethod


class FormaGeometrica(ABC):
    def __init__(self, nome):
        self.nome = nome

    @abstractmethod
    def calcula_area(self):
        pass

class Retangulo(FormaGeometrica):
    def __init__(self, nome, base, altura):
        super().__init__(nome)
        self.base = base
        self.altura = altura

    def calcula_area(self):
        return self.base * self.altura


class Triangulo(FormaGeometrica):
    def __init__(self, nome, base, altura):
        super().__init__(nome)
        self.base = base
        self.altura = altura

    def calcula_area(self):
        return (self.base * self.altura) / 2

class Circulo(FormaGeometrica):
    def __init__(self, nome, raio):
        super().__init__(nome)
        self.raio = raio

    def calcula_area(self):
        return math.pi * (self.raio ** 2)

class Trapezio(FormaGeometrica):
    def __init__(self, nome, base_maior, base_menor, altura):
        super().__init__(nome)
        self.base_maior = base_maior
        self.base_menor = base_menor
        self.altura = altura

    def calcula_area(self):
        return ((self.base_maior + self.base_menor) * self.altura) / 2

class Losango(FormaGeometrica):
    def __init__(self, nome, diagonal_maior, diagonal_menor):
        super().__init__(nome)
        self.diagonal_maior = diagonal_maior
        self.diagonal_menor = diagonal_menor

    def calcula_area(self):
        return (self.diagonal_maior * self.diagonal_menor) / 2

class Quadrado(Retangulo):
    def __init__(self, nome, lado):
        super().__init__(nome, lado, lado)


if __name__ == '__main__':
    formas = [
        Retangulo('Retângulo', 10, 5),
        Triangulo('Triângulo', 10, 5),
        Circulo('Círculo', 5),
        Trapezio('Trapézio', 10, 5, 5),
        Losango('Losango', 10, 5),
        Quadrado('Quadrado', 5)
    ]

    for forma in formas:
        print(f'{forma.nome}, área = {forma.calcula_area()}')