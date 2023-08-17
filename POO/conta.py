class ContaBancaria:
    def __init__(self, numero, titular, saldo):
        self.numero = numero
        self.titular = titular
        self.__saldo = saldo

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        if self.__saldo >= valor:
            self.__saldo -= valor
            print("Saque realizado com sucesso")
            return True
        print("Saldo insuficiente!")
        return False
    
    def get_saldo(self):
        return "R$ "+str(self.__saldo)

conta = ContaBancaria(123, "João", 1000)
conta.depositar(500)
conta.sacar(5000)
print("Saldo atual:", conta.get_saldo())
