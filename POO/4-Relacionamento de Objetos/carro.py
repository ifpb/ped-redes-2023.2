class Pessoa:
    def __init__(self, nome, end, data_nascimento, veiculo):
        self.nome = nome
        self.endereco = end
        self.data_nascimento = data_nascimento
        self.veiculo = veiculo

    @property
    def veiculo(self):
        return self.__veiculo

    @veiculo.setter
    def veiculo(self, v):
        assert isinstance(v, Carro), "O veículo deve ser um objeto da classe Carro"
        self.__veiculo = v

class Carro:
    def __init__(self, modelo, placa, ano, valor):
        self.modelo = modelo
        self.placa = placa
        self.ano = ano
        self.valor = valor


if __name__ == '__main__':
    try:
        c = Carro("Fusca", "ABC-1234", 1975, 5000)

        p = Pessoa("Lucas", "Rua 1", "01/01/2000", c)
        print("Veículo de ", p.nome)
        print("Modelo: ", p.veiculo.modelo)
        print("Placa: ", p.veiculo.placa)
        print("Ano: ", p.veiculo.ano)
        print("Valor: ", p.veiculo.valor)

        p.veiculo = Carro("Gol", "DEF-5678", 2010, 20000)
        print("Modelo: ", p.veiculo.modelo)
        print("Placa: ", p.veiculo.placa)
        print("Ano: ", p.veiculo.ano)
        print("Valor: ", p.veiculo.valor)
    except AssertionError as e:
        print(e)