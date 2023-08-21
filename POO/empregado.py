class Empregado:

    num_empregados_criados = 0

    def __init__(self, nome, salario=1100.00):
        self.nome = nome
        self.salario_base = salario
        Empregado.num_empregados_criados += 1

    def desconto_vale_transporte(self):
        return self.salario_base * 0.06
    
    def calcular_irpf(self):
        ## TODO - implementar método
        pass

class Funcionario:
    pass



print("Número de empregados criados = ", Empregado.num_empregados_criados)

empregado1 = Empregado("João")
print(empregado1.nome)
print(empregado1.salario_base)
print(empregado1.calcular_irpf())
print("Desconto vale-transporte: ", empregado1.desconto_vale_transporte())
print("Número de empregados criados = ", Empregado.num_empregados_criados)

empregado2 = Empregado("Maria", 2000.00)
print(empregado2.nome)
print(empregado2.salario_base)
print("Desconto vale-transporte: ", empregado2.desconto_vale_transporte())
print("Número de empregados criados = ", Empregado.num_empregados_criados)
