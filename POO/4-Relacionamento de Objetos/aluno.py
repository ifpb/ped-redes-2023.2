class Turma:
    def __init__(self, entrada, curso, total_semestres, alunos=[]):
        self.entrada = entrada
        self.curso = curso
        self.total_semestres = total_semestres
        self.alunos = alunos

class Curso:
    def __init__(self, nome, matriculas=[]):
        self.nome = nome
        self.matriculas = matriculas

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def matriculas(self):
        return self.__matriculas

    @matriculas.setter
    def matriculas(self, matriculas):
        self.__matriculas = matriculas

    def add_matricula(self, matricula):
        self.matriculas.append(matricula)

    def remover_matricula(self, matricula):
        self.matriculas.remove(matricula)


class Matricula:
    def __init__(self, numero, data, curso=None):
        self.numero = numero
        self.data = data
        self.curso = curso

    def __str__(self):
        return f"{self.numero} - {self.data}"

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, n):
        self.__numero = n

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, d):
        self.__data = d

    @property
    def curso(self):
        return self.__curso

    @curso.setter
    def curso(self, curso):
        self.__curso = curso


class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, n):
        self.__nome = n

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula

if __name__ == '__main__':
    m = Matricula("202223123", "2020-01-01")
    a = Aluno("Jacksoan", m)
    print(a.nome)
    print(a.matricula.numero)
    print(a.matricula.data)
    print(a.matricula)

    c = Curso("Redes de Computadores")
    mat = Matricula("2023231", "2020-02-02", c)
    mat2 = Matricula("2022231", "2021-02-02", c)
    c.add_matricula(mat)
    c.add_matricula(mat2)
    a2 = Aluno("Agnes", mat)

    print("Matrículas do curso de Redes de Computadores :")
    for m in c.matriculas:
        print(m.curso.nome, m.numero, m.data)

    turma = Turma("2020.1", c, 6)
    turma.alunos.append(a)
    turma.alunos.append(a2)

    print("Turma: ")
    print(turma.entrada, turma.curso.nome, turma.total_semestres)
    print("Alunos da turma:")
    for a in turma.alunos:
        print(a.nome, a.matricula.numero, a.matricula.data)

