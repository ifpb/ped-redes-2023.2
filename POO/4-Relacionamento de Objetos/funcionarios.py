class Endereco:
    def __init__(self, rua, cidade, estado, pais):
        self.rua = rua
        self.cidade = cidade
        self.estado = estado
        self.pais = pais

class Funcionario:
    def __init__(self, id, nome, cargo, salario, endereco):
        self.id = id
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
        self.endereco = endereco

    def aumentar_salario(self, porcentagem):
        self.salario += self.salario * porcentagem / 100

    @property
    def salario(self):
        return self.__salario

    def exibir_salario(self):
        return "R$ " + str(self.__salario)

    @salario.setter
    def salario(self, s):
        assert type(s) == float or type(s) == int, "O atributo salario deve ser um número"
        assert s > 0, "O atributo salario deve ser maior que zero"
        self.__salario = s

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco):
        assert isinstance(endereco, Endereco), "O atributo endereco deve ser um objeto da classe Endereco"
        self.__endereco = endereco

    def __str__(self):
        return f"ID: {self.id}\nNome: {self.nome}\nCargo: {self.cargo}\nSalário: {self.exibir_salario()}\nEndereço: {self.endereco.rua}, {self.endereco.cidade}, {self.endereco.estado}, {self.endereco.pais}"


if __name__ == '__main__':
    e = Endereco("Rua 1", "São Paulo", "SP", "Brasil")
    nome = input("Digite o nome do funcionario")
    cargo = input("Digite o cargo do funcionario")
    salario = float(input("Digite o salário do funcionário"))
    f1 = Funcionario(1, nome, cargo, salario, e)
    print(f1)
    f1.aumentar_salario(10)
    print(f1)