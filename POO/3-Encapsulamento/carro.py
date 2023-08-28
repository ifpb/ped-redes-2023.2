class Carro:
    def __init__(self, cor, velocidade, marca, modelo, kms=0):
        self.__inicializar_propriedades(cor, velocidade, marca, modelo, kms)

    def __inicializar_propriedades(self, cor, velocidade, marca, modelo, kms):
        self.cor = cor
        self.velocidade = velocidade
        self.marca = marca
        self.modelo = modelo
        self.kms = kms

    def calcular_velocidade_legal(self):
        if self.velocidade > 80:
            print("Acima do permitido!")
        else:
            print("Velocidade OK!")

    @property
    def kms(self):
        return self.__kms
    
    @kms.setter
    def kms(self, k):
        if type(k) != int and type(k) != float:
            self.__kms = 0
            print("Kms deve ser um número")
        elif k < 0:
            self.__kms = 0
            print("Kms deve ser maior ou igual a 0")
        else:
            self.__kms = k

    @property
    def cor(self):
        return self.__cor
    
    @cor.setter
    def cor(self, c):
        if c not in ['branco', 'vermelho', 'azul', 'prata', 'amarelo', 'cinza', 'preto']:
            print("Cor passada inválida!")
        else:
            self.__cor = c

    @property
    def marca(self):
        return self.__marca
    
    @marca.setter
    def marca(self, m):
        if type(m) != str:
            print("Marca deve ser uma string")
            self.__marca = ""
        else:
            self.__marca = m

    @property
    def modelo(self):
        return self.__modelo
    
    @modelo.setter
    def modelo(self, m):
        if type(m) != str:
            print("Marca deve ser uma string")
            self.__modelo = ""
        else:
            self.__modelo = m

    @property
    def velocidade(self):
        return self.__velocidade
    
    @velocidade.setter
    def velocidade(self, v):
        if type(v) != int and type(v) != float:
            print("Velocidade deve ser um número")
            self.__velocidade = 0
        elif v < 0:
            print("Velocidade deve ser maior ou igual a 0")
            self.__velocidade = 0
        else:
            self.__velocidade = v

    def __str__(self):
        return self.cor + "," + str(self.velocidade) + "," + self.marca + "," + self.modelo + "," + str(self.kms)

carro = Carro("branco", 50, "Ford", "Focus", -50)
carro.kms = "MUITO BOM"
carro.cor = "LEGAL"
print(carro)
print(carro.calcular_velocidade_legal())

    

