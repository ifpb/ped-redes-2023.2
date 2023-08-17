class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.__nome = nome
        self.__idade = idade
        self.__cpf = cpf

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        assert type(nome) == str, "Nome deve ser uma string"
        self.__nome = nome

    @property
    def idade(self):
        return self.__idade
    
    @idade.setter
    def idade(self, idade):
        if type(idade) != int:
            print("Idade deve ser um inteiro")
            return
        if idade < 0 or idade > 100:
            print("Idade deve ser um número entre 0 e 100")
            return
        self.__idade = idade

    def __str__(self):
        return f"{self.__nome} - {self.__idade} - {self.__cpf}"

try:
    pessoa = Pessoa("João", 35, "123.456.789-00")
    pessoa.nome = 32233
    print(pessoa)
except AssertionError as e:
    print(e)