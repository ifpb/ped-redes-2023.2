from time import sleep


class Semaforo:
    def __init__(self):
        self.cor = "vermelho"
        self.temporizador = 10
        self.mudar_cor()

    def mudar_cor(self):
        while self.temporizador > 0:
            print("Cor:", self.cor, "Temporizador:", self.temporizador)
            self.temporizador -= 1
            sleep(1)
        if self.cor == "vermelho":
            self.cor = "verde"
            self.temporizador = 20
        elif self.cor == "verde":
            self.cor = "amarelo"
            self.temporizador = 3
        elif self.cor == "amarelo":
            self.cor = "vermelho"
            self.temporizador = 10
        self.mudar_cor()

semaforo = Semaforo()
