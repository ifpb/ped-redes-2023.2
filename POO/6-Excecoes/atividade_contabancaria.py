from abc import ABC

class SaldoInsuficiente(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)

class ContaBancaria(ABC):
    def __init__(self, numero, saldo):
        self.numero = numero
        self.saldo = saldo

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, n):
        try:
            p1 = int(n[:5])
            p2 = n[5]
            assert p2 == '-', 'Separador deve ser hífen'
            p3 = n[6]
            assert p3 == 'X' or type(int(p3)) == int, 'Sétimo dígito deve ser X ou número'
            self.__numero = n
        except ValueError:
            raise AssertionError('Cinco primeiros dígitos da conta devem ser apenas números')

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, s):
        assert type(s) == int or type(s) == float, 'Saldo deve ser numérico'
        self.__saldo = s

    def sacar(self, valor):
        assert type(valor) == int or type(valor) == float, 'Valor do saque deve ser numérico'
        assert valor > 0, 'Valor do saque deve ser maior que zero'
        if self.saldo - valor < 0:
            raise SaldoInsuficiente(f'Saldo insuficiente para saque (saldo: {self.saldo}, saque: {valor})')
        self.saldo -= valor

    def depositar(self, valor):
        assert type(valor) == int or type(valor) == float, 'Valor do depósito deve ser numérico'
        assert valor > 0, 'Valor do depósito deve ser maior que zero'
        self.saldo += valor

    def __str__(self):
        return f'Conta: {self.numero}, Saldo: {self.saldo}'

class ContaPoupanca(ContaBancaria):
    def __init__(self, numero, saldo, taxa_juros):
        self.taxa_juros = taxa_juros
        super().__init__(numero, saldo)

    @property
    def taxa_juros(self):
        return self.__taxa_juros

    @taxa_juros.setter
    def taxa_juros(self, t):
        assert type(t) == int or type(t) == float, 'Taxa de juros deve ser numérica'
        assert 0 <= t <= 1, 'Taxa de juros deve ser entre 0 e 1'
        self.__taxa_juros = t

    def ganho_anual(self):
        return self.saldo * self.taxa_juros * 12

    def __str__(self):
        return f'{super().__str__()}, Taxa de juros: {self.taxa_juros}'

class LimiteChequeEspecialExcedente(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)


class ContaCorrente(ContaBancaria):
    MAX_CHEQUE_ESPECIAL = 1000

    def __init__(self, numero, saldo, limite_cheque_especial):
        super().__init__(numero, saldo)
        self.limite_cheque_especial = limite_cheque_especial

    def sacar(self, valor):
        assert type(valor) == int or type(valor) == float, 'Valor do saque deve ser numérico'
        assert valor > 0, 'Valor do saque deve ser maior que zero'
        if self.saldo - valor < self.limite_cheque_especial * -1:
            raise SaldoInsuficiente(f'Saldo insuficiente para saque (saldo: {self.saldo}, com cheque especial: {self.limite_cheque_especial}, saque: {valor})')
        self.saldo -= valor

    @property
    def limite_cheque_especial(self):
        return self.__limite_cheque_especial

    @limite_cheque_especial.setter
    def limite_cheque_especial(self, l):
        assert type(l) == int or type(l) == float, 'Limite do cheque especial deve ser numérico'
        if l > ContaCorrente.MAX_CHEQUE_ESPECIAL:
            raise LimiteChequeEspecialExcedente(f'Limite do cheque especial não pode ser maior que 1000 (valor fornecido: {l})')
        self.__limite_cheque_especial = l

    def __str__(self):
        return f'{super().__str__()}, Limite do cheque especial: {self.limite_cheque_especial}'

if __name__ == '__main__':
    try:
        poupanca = ContaPoupanca('12345-X', 1000, 0.1)
        corrente = ContaCorrente('12345-X', 1000, 1000)
        contas = [poupanca, corrente]
        for conta in contas:
            conta.sacar(100)
        print(poupanca)
        print(corrente)
        poupanca.sacar(1000)
        corrente.sacar(2000)
        print(poupanca)
        print(corrente)
    except AssertionError as e:
        print(e)
    except SaldoInsuficiente as e:
        print(e)
    except LimiteChequeEspecialExcedente as e:
        print(e)
    except Exception as e:
        print("Erro inesperado: ", e)