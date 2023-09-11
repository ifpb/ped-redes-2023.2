class Produto:
    def __init__(self, codigo, valor, descricao):
        self.codigo = codigo
        self.valor = valor
        self.descricao = descricao

class ItemPedido:
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade

    def __str__(self):
        return f"Produto: {self.produto.descricao}, Quantidade: {self.quantidade}, Preço unitário: {self.produto.valor}, Sub-total: {self.produto.valor * self.quantidade}"

class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente
        self.itens = []

    def adicionar_item(self, item):
        self.itens.append(item)

    def calcular_total(self):
        # total = 0
        # for item in self.itens:
        #     total += item.produto.valor * item.quantidade
        # return total
        return sum([item.produto.valor * item.quantidade for item in self.itens])

    def __str__(self):
        itens = "\n".join([str(i) for i in self.itens])
        return f"Cliente: {self.cliente} \nItens: \n{itens} \nValor total: {self.calcular_total()}"

if __name__ == '__main__':
    camiseta = Produto(1, 50, "Camiseta")
    calca = Produto(2, 60, "Calça")
    meia = Produto(3, 10, "Meia")
    pedido = Pedido("Diego")
    pedido.adicionar_item(ItemPedido(camiseta, 8))
    pedido.adicionar_item(ItemPedido(calca, 2))
    pedido.adicionar_item(ItemPedido(meia, 4))
    print(pedido)
