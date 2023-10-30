from servidores_dns import servidores_dns
from busca_sequencial import *
from busca_binaria import *
import timeit

for servidor in servidores_dns:
    print(servidor)

print("Buscando por IP:")
print(busca_sequencial(servidores_dns, '200.162.136.138'))
print(busca_sequencial_recursiva(servidores_dns, '201.73.200.3'))
print(busca_binaria(servidores_dns, '201.28.69.242'))
print(busca_binaria_recursiva(servidores_dns, '200.223.129.162'))

print("### Comparação de desempenho: ###")
print("Busca sequencial (Iterativa)", timeit.timeit("busca_sequencial(servidores_dns, '200.162.136.138')",
                    setup="from servidores_dns import servidores_dns; from __main__ import busca_sequencial",
                    number=1000))

print("Busca sequencial (Recursiva)", timeit.timeit("busca_sequencial_recursiva(servidores_dns, '200.162.136.138')",
                    setup="from servidores_dns import servidores_dns; from __main__ import busca_sequencial_recursiva",
                    number=1000))

print("Busca binária (Iterativa)", timeit.timeit("busca_binaria(servidores_dns, '200.162.136.138')",
                    setup="from servidores_dns import servidores_dns; from __main__ import busca_binaria",
                    number=1000))

print("Busca binária (Recursiva)", timeit.timeit("busca_binaria_recursiva(servidores_dns, '200.162.136.138')",
                    setup="from servidores_dns import servidores_dns; from __main__ import busca_binaria_recursiva",
                    number=1000))