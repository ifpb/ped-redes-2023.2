class RegistroPonto:
    def __init__(self, horario, funcionario, justificativa=None):
        self.horario = horario
        self.funcionario = funcionario
        self.justificativa = justificativa

class RelogioPonto:
    def __init__(self):
        self.registros = []

    def adicionar_registro(self, registro):
        self.registros.append(registro)

    def imprimir_registros(self):
        for registro in self.registros:
            print("Horário:", registro.horario, "Funcionário:", registro.funcionario)

relogio_ponto = RelogioPonto()
registro1 = RegistroPonto("08:00", "João")
registro2 = RegistroPonto("08:05", "Maria")
registro3 = RegistroPonto("08:10", "José")
registro4 = RegistroPonto("08:15", "Ana")
registro5 = RegistroPonto("10:15", "Aderbal", "Perdi o ônibus")
relogio_ponto.adicionar_registro(registro1)
relogio_ponto.adicionar_registro(registro2)
relogio_ponto.adicionar_registro(registro3)
relogio_ponto.adicionar_registro(registro4)
relogio_ponto.imprimir_registros()