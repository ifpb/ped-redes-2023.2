from estrutura_linear import EstruturaLinear

class Host:
    def __init__(self, hostname, ip):
        self.hostname = hostname
        self.ip = ip

    def __str__(self):
        return f"{self.hostname} - {self.ip}"


class ListaEncadeada(EstruturaLinear):
    def __init__(self):
        super().__init__()

    def adicionar(self, hostname, ip):
        host = Host(hostname, ip)
        self.inserir_no_final(host)

    def remover(self, hostname):
        atual = self.cabeca
        
        if atual.carga.hostname == hostname:
            self.remover_do_inicio()

        atual = atual.prox

        while atual is not self.cabeca:
            if atual.carga.hostname == hostname:
                # remover elemento
                if atual.ant is not None:
                    atual.ant.prox = atual.prox
                if atual.prox is not None:
                    atual.prox.ant = atual.ant
            atual = atual.prox
    
    def resolver(self, hostname):
        atual = self.cabeca

        if atual.carga.hostname == hostname:
            return atual.carga.ip

        atual = atual.prox

        while atual is not self.cabeca:
            if atual.carga.hostname == hostname:
                return atual.carga.ip
            atual = atual.prox
        
        return "hostname não encontrado"

    def listar(self):
        self.imprimir()

    def inserir_todos(self, elementos):
        for elemento in elementos:
            self.adicionar(elemento.carga.hostname, elemento.carga.ip)

    def ordenar(self, lista):
        if len(lista) <= 1: return lista
        pivo = lista[0].carga.hostname
        iguais = self.extrair_iguais(pivo, lista)
        menores = self.extrair_menores(pivo, lista)
        maiores = self.extrair_maiores(pivo, lista)

        resultado = ListaEncadeada()
        resultado.inserir_todos(self.ordenar(menores))
        resultado.inserir_todos(iguais)
        resultado.inserir_todos(self.ordenar(maiores))
        return resultado

    def extrair_iguais(self, valor, lista):
        iguais = ListaEncadeada()
        for i in range(len(lista)):
            if lista[i].carga.hostname == valor:
                iguais.adicionar(lista[i].carga.hostname, lista[i].carga.ip)
        return iguais

    def extrair_menores(self, valor, lista):
        menores = ListaEncadeada()
        for i in range(len(lista)):
            if lista[i].carga.hostname < valor:
                menores.adicionar(lista[i].carga.hostname, lista[i].carga.ip)
        return menores

    def extrair_maiores(self, valor, lista):
        maiores = ListaEncadeada()
        for i in range(len(lista)):
            if lista[i].carga.hostname > valor:
                maiores.adicionar(lista[i].carga.hostname, lista[i].carga.ip)
        return maiores

if __name__ == '__main__':

    lista = ListaEncadeada()
    lista.adicionar("localhost", "127.0.0.1")
    lista.adicionar("google.com", "216.58.222.78")
    lista.adicionar("amazon.com", "176.32.103.205")
    lista.adicionar("facebook.com", "31.13.74.35")
    lista.adicionar("ifpb.edu.br", "200.130.72.31")
    lista.listar()

    lista.remover("localhost")
    print("Após remoção: ")
    lista.listar()

    print("Resolvendo elementos")
    print(lista.resolver("amazon.com"))
    print(lista.resolver("notfound.com"))

    print("Antes da ordenação:")
    lista.listar()

    print("Depois da ordenação:")
    lista = lista.ordenar(lista)
    lista.listar()
