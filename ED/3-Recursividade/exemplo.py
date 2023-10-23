def imprimir_numero(num):
    if num < 5:
        imprimir_numero(num + 1)
        print(num)

def somar(num1, num2):
    if num1 == num2:
        return num1+num2
    else:
        return somar(num1 + 1, num2)

def fibonacci(n):
    print("fibonacci de ", n)
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_it(n):
    if n <= 1:
        return n
    else:
        a = 0
        b = 1
        for i in range(2, n+1):
            c = a + b
            a = b
            b = c
        return c

def imprimir_frutas(frutas):
    if len(frutas) > 0:
        print(frutas[0])
        imprimir_frutas(frutas[1:])

def imprimir_frutas_contador(frutas, contador=0):
    if contador < len(frutas):
        print(frutas[contador])
        imprimir_frutas_contador(frutas, contador + 1)

def contem_par(numeros):
    if len(numeros) == 0:
        return False
    if numeros[0] % 2 == 0:
        return True
    return contem_par(numeros[1:])

if __name__ == '__main__':
    # frutas = ['banana', 'maçã', 'uva', 'pera', 'mamão', 'abacaxi']
    # imprimir_frutas_contador(frutas)
    print(contem_par([1, 3, 1, 5, 3, 2]))
