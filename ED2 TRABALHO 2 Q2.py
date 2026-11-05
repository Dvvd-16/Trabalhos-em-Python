import csv
import sys

# Trabalho 2 - Estrutura de Dados 2 (Questão 2)

def ler_matriz_csv(caminho_arquivo):
    matriz = []
    with open(caminho_arquivo, 'r') as arquivo_csv:
        leitor = csv.reader(arquivo_csv)
        for linha in leitor:
            matriz.append([int(valor) for valor in linha])
    return matriz

def prim(matriz):
    n = len(matriz)
    selecionado = [False] * n
    no_pai = [-1] * n
    chave = [sys.maxsize] * n
    chave[0] = 0

    for _ in range(n):
        # Escolhe o vértice com menor chave ainda não selecionado
        min_valor = sys.maxsize
        u = -1
        for v in range(n):
            if not selecionado[v] and chave[v] < min_valor:
                min_valor = chave[v]
                u = v

        selecionado[u] = True

        for v in range(n):
            peso = matriz[u][v]
            if peso > 0 and not selecionado[v] and peso < chave[v]:
                chave[v] = peso
                no_pai[v] = u

    return no_pai, chave

def exibir_mst(pai, pesos):
    print("Arestas da Árvore Geradora Mínima:")
    custo_total = 0
    for i in range(1, len(pai)):
        print(f"{pai[i]} - {i} (peso {pesos[i]})")
        custo_total += pesos[i]
    print(f"\nCusto total: {custo_total}")

# Diretório do arquivo CSV (Alterar para o diretório correto):
caminho = r'C:\Users\luize\Desktop\Trabalho 2 ED2 - GRAFOS\grafo.csv.txt'

matriz = ler_matriz_csv(caminho)
pai, pesos = prim(matriz)
exibir_mst(pai, pesos)
