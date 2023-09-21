from enum import Enum


class GrauInstrucao(Enum):
    GRADUADO = "Graduado"
    ESPECIALISTA = "Especialista"
    MESTRE = "Mestre"
    DOUTOR = "Doutor"

    def get_by_value(value):
        for grau in GrauInstrucao:
            if grau.value == value:
                return grau
        return None

if __name__ == '__main__':
    grau = input("Digite o grau de instrução")
    resultado = GrauInstrucao.get_by_value(grau)

    print(resultado)
