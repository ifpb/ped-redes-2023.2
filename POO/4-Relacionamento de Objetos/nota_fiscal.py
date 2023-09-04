class Cliente:
    def __init__(self, login, nome, senha):
        self.login = login
        self.nome = nome
        self.senha = senha

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, s):
        assert len(s) >= 6, "A senha deve ter ao menos 6 caracteres"
        self.__senha = s

    def validar_senha(self):
        return len(self.senha) > 6

class Produto:
    def __init__(self, descricao, preco_unitario, quantidade):
        self.descricao = descricao
        self.preco_unitario = preco_unitario
        self.quantidade = quantidade

    def __str__(self):
        return f"{self.descricao} - {self.preco_unitario} - {self.quantidade}"

class NotaFiscal:
    def __init__(self, numero, empresa, endereco, cliente, produtos):
        self.numero = numero
        self.cliente = cliente
        self.produtos = produtos
        self.empresa = empresa
        self.endereco = endereco

    @property
    def produtos(self):
        return self.__produtos

    def add_produto(self, produto):
        assert isinstance(produto, Produto), "O produto deve ser um objeto da classe Produto"
        self.produtos.append(produto)

    @produtos.setter
    def produtos(self, produtos):
        assert isinstance(produtos, list), "Os produtos devem ser uma lista"
        for p in produtos:
            assert isinstance(p, Produto), "Os produtos devem ser objetos da classe Produto"
        self.__produtos = produtos

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente):
        assert isinstance(cliente, Cliente), "O cliente deve ser um objeto da classe Cliente"
        self.__cliente = cliente

    def validar_senha_cliente(self):
        return self.cliente.validar_senha()

    def __str__(self):
        return f"Empresa: {self.empresa}, Endereço: {self.endereco}, Cliente: {self.cliente.nome}, Produtos: {[str(p) for p in self.produtos]}"

if __name__ == '__main__':
    cliente = Cliente("lucas", "Lucas", "123456")
    produtos = [Produto("Arroz", 10, 2), Produto("Feijão", 5, 3)]
    empresa = "Empresa X"
    endereco = "Rua 1"
    nota_fiscal = NotaFiscal(1, empresa, endereco, cliente, produtos)
    nota_fiscal.cliente = cliente
    nota_fiscal.produtos = [Produto("Arroz", 10, 2), Produto("Feijão", 5, 3)]
    nota_fiscal.add_produto(Produto("Macarrão", 3, 1))
    print(nota_fiscal)