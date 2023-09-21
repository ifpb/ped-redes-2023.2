lista = [3, 2, 1, 9, 7, 5, 4, 6, 8]
index = int(input("Digite um índice: "))
try:
    print(lista[index])
except ArithmeticError:
    print(f"O índice {index} não existe.")
finally:
    print("Fim do programa")

# print("Fim do programa")