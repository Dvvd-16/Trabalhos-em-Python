import math

def f(x):
    return x * math.exp(x) - 2

def derivada_f(x):
    return math.exp(x) + x * math.exp(x)

x0 = 0.5
tolerancia = 0.04
maxIter = 100

iteracao = 0
erro = tolerancia + 1

while erro > tolerancia and iteracao < maxIter:

    fx = f(x0)
    dfx = derivada_f(x0)

    if dfx == 0:
        print("Derivada zero. O método falhou.")
        break

    x1 = x0 - (fx / dfx)

    erro = abs(x1 - x0)

    print("Iteração:", iteracao + 1)
    print("x0:", x0)
    print("f(x0):", fx)
    print("f'(x0):", dfx)
    print("x1:", x1)
    print("Erro:", erro)
    print()

    x0 = x1
    iteracao += 1

if erro <= tolerancia:
    print("Raiz encontrada:", x1)
    print("Total de iterações:", iteracao)
else:
    print("Número máximo de iterações atingido.")