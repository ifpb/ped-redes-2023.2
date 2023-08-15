class Celular:
    def __init__(self, marca, modelo, cor, tamanho_tela, sistema_operacional, preco, resolucao_camera, memoria_interna):
        self.resolucao_camera = resolucao_camera
        self.memoria_interna = memoria_interna
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.tamanho_tela = tamanho_tela
        self.sistema_operacional = sistema_operacional
        self.preco = preco

    def reajustar_preco(self, percentual):
        self.preco = self.preco + (self.preco * percentual / 100)

celular1 = Celular("Samsung", "Galaxy S10", "Branco", "6.1 polegadas", "Android", 3500.00, "16 Mega-pixels", "64GB")

celular2 = Celular("Apple", "iPhone 11", "Preto", "6.1 polegadas", "iOS", 5000.00, "12 Mega-pixels", "128GB")

print("Celular 1:", celular1.marca, celular1.modelo, celular1.cor, celular1.tamanho_tela, celular1.sistema_operacional, celular1.preco)
print("Celular 2:", celular2.marca, celular2.modelo, celular2.cor, celular2.tamanho_tela, celular2.sistema_operacional, celular2.preco)

celular2.reajustar_preco(10)
print("Celular 1:", celular1.marca, celular1.modelo, celular1.cor, celular1.tamanho_tela, celular1.sistema_operacional, celular1.preco)
print("Celular 2:", celular2.marca, celular2.modelo, celular2.cor, celular2.tamanho_tela, celular2.sistema_operacional, celular2.preco)