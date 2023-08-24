class Televisao:

    ## Método Construtor ou Método de Inicialização
    def __init__(self):
        self.ligado = False
        self.canal = 1
        self.volume = 0
        self.brilho = 0
        self.contraste = 0
        self.closed_caption = False
        self.sleep = False

    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False

    def aumentar_volume(self, valor):
        self.volume += valor
        
tv1 = Televisao()
tv1.ligar()
tv1.aumentar_volume(10)
tv1.aumentar_volume(10)
print("TV 1 ligada ?", tv1.ligado)
print("Volume da TV 1:", tv1.volume)
tv1.canal = 7

tv2 = Televisao()
tv2.canal = 10

print("Canal da TV 1: ", tv1.canal)
print("Canal da TV 2: ", tv2.canal)
