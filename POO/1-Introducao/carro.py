class Carro:
    def __init__(self, cor, velocidade):
        self.cor = cor
        self.velocidade = velocidade
    

c1 = Carro("branco", "Baixa")
print("C1 = ", c1.cor, c1.velocidade)
c2 = Carro("vermelho", "Alta")
print("C2 = ", c2.cor, c2.velocidade)

# c3 = c2
c3 = Carro(c2.cor, c2.velocidade)
c3.cor = "azul"

print("C2 = ", c2.cor, c2.velocidade)
print("C3 = ", c3.cor, c3.velocidade)