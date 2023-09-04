class Pais:
    def __init__(self, nome, capital, dimensao, fronteira=[]):
        self.nome = nome
        self.capital = capital
        self.dimensao = dimensao
        self.__fronteira = fronteira

    def add_pais_fronteira(self, pais):
        self.__fronteira.append(pais)

    @property
    def fronteira(self):
        return self.__fronteira

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, n):
        self.__nome = n

    @property
    def capital(self):
        return self.__capital

    @capital.setter
    def capital(self, c):
        self.__capital = c

    @property
    def dimensao(self):
        return f"{self.__dimensao} km2"

    @dimensao.setter
    def dimensao(self, d):
        self.__dimensao = d

    def __str__(self):
        return f"País: {self.nome}, capital: {self.capital}, dimensão: {self.dimensao}"

if __name__ == '__main__':
    paises_fronteira = ['Uruguai', 'Argentina', 'Paraguai', 'Peru', 'Bolívia', 'Colombia', 'Guiana Francesa', 'Guiana', 'Venezuela']
    p = Pais("Brasil", "Brasília", 20032, paises_fronteira)
    p.add_pais_fronteira('Suriname')
    print(p)
    print("Países que fazem fronteira: ")
    [print(f) for f in p.fronteira]
    print(" - ".join(p.fronteira))