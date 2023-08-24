class VideoGame:
    ultimo_num_serie = 0
    def __init__(self, data_fabricacao='21/08/2023', marca='', modelo=''):
        self.data_fabricacao = data_fabricacao
        self.marca = marca
        self.modelo = modelo
        self.capacidade_hd = 256
        self.jogos_instalados = []
        self.ano_garantia = 1
        VideoGame.ultimo_num_serie += 1
        self.num_serie = VideoGame.ultimo_num_serie

    def __str__(self):
        return f'VideoGame: {self.num_serie}, {self.data_fabricacao}, {self.marca}, {self.modelo}, {self.capacidade_hd}, {self.jogos_instalados}, {self.ano_garantia}'

vg1 = VideoGame()
vg1.marca = 'Microsoft'
vg1.modelo = 'Xbox One'
print(vg1)
vg2 = VideoGame('10/10/2020')
vg2.marca = 'Nintendo'
vg2.modelo = 'Switch'
print(vg2)
vg3 = VideoGame('21/08/2023', 'Sony', 'Playstation 5')
print(vg3)
print(VideoGame.__name__)
print(VideoGame.__module__)
vg3_dicionario = vg3.__dict__
print(vg3_dicionario['marca'])