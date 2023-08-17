class Poligono:
    def __init__(self, lados):
        self.lados = lados

    def perimetro(self):
        return sum(self.lados)

    def __str__(self):
        return f'Polígono de {len(self.lados)} lados'
    
class Quadrilatero(Poligono):
    def __init__(self, lados):
        assert len(lados) == 4, "Quadrilátero deve ter 4 lados"
        super().__init__(lados)

    def __str__(self):
        return f'Quadrilátero de lados {self.lados}'
    
class Hexagono(Poligono):
    def __init__(self, lados):
        assert len(lados) == 6, "Hexágono deve ter 6 lados"
        super().__init__(lados)

    def __str__(self):
        return f'Hexágono de lados {self.lados}'
    
class Triangulo(Poligono):
    def __init__(self, lados):
        assert len(lados) == 3, "Triângulo deve ter 3 lados"
        super().__init__(lados)

    def __str__(self):
        return f'Triângulo de lados {self.lados}'

class Retangulo(Quadrilatero):
    def __init__(self, lado1, lado2):
        super().__init__([lado1, lado2, lado1, lado2])

    def __str__(self):
        return f'Retângulo de lados {self.lados[0]} e {self.lados[1]}'
    
class Quadrado(Quadrilatero):
    def __init__(self, lado):
        super().__init__([lado, lado, lado, lado])

    def __str__(self):
        return f'Quadrado de lado {self.lados[0]}'
    
triangulo = Triangulo([3, 4, 5])
quadrado = Quadrado(5)
retangulo = Retangulo(3, 4)
print("Perimetro do retangulo = "+str(retangulo.perimetro()))
print("Perimetro do quadrado = "+str(quadrado.perimetro()))
print("Perimetro do triangulo = "+str(triangulo.perimetro()))

print(triangulo, quadrado, retangulo, sep='\n')