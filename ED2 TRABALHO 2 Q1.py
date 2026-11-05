# Trabalho 2 - Estrutura de Dados 2 (Questão 1)
grafo = { 
    0: [1, 3, 4, 8],
    1: [0, 2, 5, 12],
    2: [1, 3, 6, 14],
    3: [0, 2, 7, 10],
    4: [0, 5, 7, 9],
    5: [1, 4, 6, 13],
    6: [2, 5, 7, 15],
    7: [3, 4, 6, 11],
    8: [0, 9, 10],
    9: [4, 8, 11],
    10: [3, 8, 11],
    11: [7, 9, 10],
    12: [1, 13, 14],
    13: [5, 12, 15],
    14: [2, 12, 15],
    15: [6, 13, 14]
}
def colorir_grafo(grafo):
    cores = {} 
    for vertice in grafo:
        vizinhos = grafo[vertice]
        cores_usadas = {cores[v] for v in vizinhos if v in cores}
        cor = 1
        while cor in cores_usadas:
            cor += 1
        cores[vertice] = cor
    return cores
cores_resultado = colorir_grafo(grafo)

for vertice in sorted(cores_resultado):
    print(f"Vértice {vertice} → Cor {cores_resultado[vertice]}")

print(f"\nNúmero mínimo de cores usadas: {max(cores_resultado.values())}")


