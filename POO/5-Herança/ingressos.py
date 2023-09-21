class Ingresso:
    def __init__(self, valor):
        self.valor = valor

    def imprimir_ingresso(self):
        tipo_ingresso = 'Ingresso normal' if type(self).__name__ == 'Ingresso' else 'Ingresso VIP'
        print(f"Valor do ingresso ({tipo_ingresso}) = R$", self.valor)


class IngressoVIP(Ingresso):
    def __init__(self, valor, adicional):
        super().__init__(valor + adicional)


if __name__ == '__main__':
    ingresso = Ingresso(50)
    ingresso.imprimir_ingresso()
    ingresso_vip = IngressoVIP(50, 10)
    ingresso_vip.imprimir_ingresso()
