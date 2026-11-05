import math

def funcao(x):
    resultado = x * math.exp(x) - 2
    return resultado

raiz = 0
b = 1
a = 0
cont = 0
taxadeerro = b - a

print("Iteração atual: x", cont)
print("Intervalo atual:", a, "até", b)
print("Intersecção:", raiz)
taxadeerro = b - a
print("Taxa de erro atual:", taxadeerro)
print()
cont += 1

while taxadeerro > 0.04:
    raiz = (a + b) / 2

    print("Iteração atual: x", cont)
    print("Intervalo atual:", a, "até", b)
    print("Intersecção:", raiz)

    if funcao(raiz) * funcao(b) < 0:
        a = raiz
    else:
        b = raiz

    taxadeerro = b - a

    print("Taxa de erro atual:", taxadeerro)
    print()

    cont += 1


print("Raiz aproximada:", raiz)
print("Intervalo final:", a, "até", b)
print("Taxa de erro final:", taxadeerro)