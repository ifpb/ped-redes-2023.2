from datetime import datetime

class Videogame:

    __ULTIMO_NUM_SERIE = 0

    def __init__(self, data_fabricacao=None, marca="", modelo=""):
        if data_fabricacao == None:
            self.data_fabricacao = datetime.today()
        else:
            self.data_fabricacao = datetime.strptime(data_fabricacao, '%d/%m/%Y')
        self.marca = marca
        self.modelo = modelo
        self.capacidade_hd = 50
        self.jogos_instalados = []
        self.anos_garantia = 1
        self.numero_serie = self.__obter_num_serie()
        self.__incrementar_num_serie()

    def get_idade(self):
        return (datetime.today() - self.data_fabricacao).days

    @staticmethod
    def validar_max_anos_garantia(anos):
        if anos > 10:
            print("Máximo de anos de garantia excedido")
        else:
            print("Garantia ok")

    @classmethod
    def __obter_num_serie(cls):
        return cls.__ULTIMO_NUM_SERIE + 1
    
    @classmethod
    def __incrementar_num_serie(cls):
        cls.__ULTIMO_NUM_SERIE += 1

    def instalar_jogo(self, jogo):
        self.jogos_instalados.append(jogo)

    def __str__(self):
        return f"""
        Marca: {self.marca}, modelo: {self.modelo}, 
        Fabricação: {self.data_fabricacao.strftime('%d/%m/%Y')}, 
        Capacidade: {self.capacidade_hd}, 
        Número de série: {self.numero_serie}, 
        Jogos Instalados: {self.jogos_instalados},
        Anos de garantia: {self.anos_garantia}
        """