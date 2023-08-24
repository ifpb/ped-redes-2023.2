class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

class Aluno(Pessoa):
    def __init__(self, nome, idade, cpf, matricula, curso):
        super.__init__(nome, idade, cpf)
        self.matricula = matricula
        self.curso = curso

    def __str__(self):
        return f"{self.matricula} - {self.nome}"

class Professor(Pessoa):
    def __init__(self, nome, idade, cpf, codigo, disciplinas):
        super.__init__(nome, idade, cpf)
        self.codigo = codigo
        self.disciplinas = disciplinas

    def __str__(self):
        return f"{self.codigo} - {self.nome}"

class Disciplina:
    def __init__(self, codigo, nome):
        self.codigo = codigo
        self.nome = nome

    def __str__(self):
        return f"{self.codigo} - {self.nome}"
        
class Curso:
    def __init__(self, codigo, nome, disciplinas):
        self.codigo = codigo
        self.nome = nome
        self.disciplinas = disciplinas

    def __str__(self):
        return f"{self.codigo} - {self.nome}"

class Turma:
    def __init__(self, codigo, curso, disciplina, professor, alunos):
        self.codigo = codigo
        self.curso = curso
        self.disciplina = disciplina
        self.professor = professor
        self.alunos = alunos

    def __str__(self):
        return f"{self.codigo} - {self.disciplina.nome} - {self.professor.nome}"

disciplina1 = Disciplina("DSC101", "Introdução à Programação")
disciplina2 = Disciplina("MAT202", "Matemática Discreta")
disciplina3 = Disciplina("ENG303", "Engenharia de Software")
print(disciplina1)

curso1 = Curso("CSC101", "Ciência da Computação", [disciplina1, disciplina2])

professor1 = Professor("João Silva", 35, "123.456.789-00", "PROF101", [disciplina1, disciplina3])

aluno1 = Aluno("Maria Souza", 20, "987.654.321-00", "2021001", curso1)
aluno2 = Aluno("Pedro Oliveira", 22, "456.789.123-00", "2021002", curso1)

turma1 = Turma("TURMA101", curso1, disciplina1, professor1, [aluno1, aluno2])

print(turma1)

# print(turma1.disciplina.nome)
# print(turma1.professor.nome)
# print(turma1.curso.nome)
# for aluno in turma1.alunos:
#     print(aluno.nome)