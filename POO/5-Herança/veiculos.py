class Veiculo:
    def __init__(self, num, preco):
        self.num = num
        self.preco = preco

    @property
    def num(self):
        return self.__num

    @num.setter
    def num(self, num):
        assert type(num) == int, "O atributo num deve ser um número inteiro"
        self.__num = num

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, preco):
        assert type(preco) == float or type(preco) == int, "O atributo preco deve ser um número"
        assert preco > 0, "O atributo preco deve ser maior que zero"
        self.__preco = preco

    def validar_preco(self):
        return self.preco > 0

    def __str__(self):
        return f"Número: {self.num}\nPreço: {self.preco}"

class Terrestre(Veiculo):
    def __init__(self, num, preco, tipo_solo):
        super().__init__(num, preco)
        self.tipo_solo = tipo_solo

    def __str__(self):
        return f"{super().__str__()}\nTipo de solo: {self.tipo_solo}"

class Aquatico(Veiculo):
    pass

class Aereo(Veiculo):
    pass

class ComRodas(Terrestre):
    def __init__(self, num, preco, tipo_solo, num_rodas):
        super().__init__(num, preco, tipo_solo)
        self.num_rodas = num_rodas

    def __str__(self):
        return f"{super().__str__()}\nNúmero de rodas: {self.num_rodas}"

class Automovel(ComRodas):
    def __init__(self, num, preco, tipo_solo, num_rodas, motor):
        super().__init__(num, preco, tipo_solo, num_rodas)
        self.motor = motor

    def __str__(self):
        return f"{super().__str__()}\nMotor: {self.motor}"

if __name__ == '__main__':
    # veiculo_areo = Aereo(1, 100000)
    # print(veiculo_areo)
    # veiculo_aquatico = Aquatico(2, 50000)
    # print(veiculo_aquatico)
    # veiculo_terrestre = Terrestre(3, 20000, "Asfalto")
    # print(veiculo_terrestre)

    automovel = Automovel(4, 10000, "Asfalto", 4, "1.0")
    print(automovel)