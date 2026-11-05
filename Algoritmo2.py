import math

def f(x):
    return x * math.exp(x) - 2

def g(x):
    return 2 / math.exp(x)

x0 = 1
precisao = 0.04
k = 0

while True:
    x1 = g(x0)
    erro = abs(x1 - x0)

    print("Iteração:", k + 1)
    print("x0:", x0)
    print("x1:", x1)
    print("Erro:", erro)
    print()

    if erro < precisao:
        break

    x0 = x1
    k += 1

print("Raiz aproximada:", x1)
print("Total de iterações:", k + 1)