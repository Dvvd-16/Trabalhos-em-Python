# Trabalho 2 - Estrutura de Dados 2 (Questão 3)

# Grafo que representa o labirinto (lista de adjacência)
grafo = {
    "AA": ["01", "04"],
    "01": ["AA", "06"],
    "02": ["03", "07"],
    "03": ["02"],
    "04": ["AA", "05", "09"],
    "05": ["04", "19"],
    "06": ["01", "07"],
    "07": ["02", "06", "08"],
    "08": ["07", "15"],
    "09": ["04", "10", "29"],
    "10": ["09", "16"],
    "11": ["12"],
    "12": ["11", "13", "17"],
    "13": ["12"],
    "14": ["15"],
    "15": ["08", "14", "21"],
    "16": ["10", "17"],
    "17": ["12", "16"],
    "18": ["19", "24"],
    "19": ["05", "18", "20"],
    "20": ["19", "27"],
    "21": ["15"],
    "22": ["23"],
    "23": ["22", "32"],
    "24": ["18", "25"],
    "25": ["24", "34"],
    "26": ["27", "40"],  
    "27": ["20", "26", "28"],
    "28": ["27", "46"],
    "29": ["09", "30"],
    "30": ["29", "51"],
    "31": ["32", "47"],
    "32": ["23", "31"],
    "33": ["34", "38"],
    "34": ["25", "33"],
    "35": ["45"],
    "36": ["57"],
    "37": ["38", "41"],
    "38": ["33", "37"],
    "39": ["40", "43"],
    "40": ["39", "26"],  
    "41": ["37", "42"],
    "42": ["41"],
    "43": ["39", "44"],
    "44": ["43", "49"],
    "45": ["35", "46"],
    "46": ["28", "45"],
    "47": ["31", "48", "52"],
    "48": ["47", "54"],
    "49": ["44", "50"],
    "50": ["49", "BB"],
    "51": ["30", "52"],
    "52": ["47", "51", "59"],
    "53": ["54", "60"],
    "54": ["48", "53"],
    "55": ["56", "61"],
    "56": ["55"],
    "57": ["36", "58"],
    "58": ["57"],
    "59": ["52"],
    "60": ["53", "61"],
    "61": ["55", "60"],
    "62": ["63"],
    "63": ["62", "BB"],
    "BB": ["50", "63"]
}

# Função DFS (busca em profundidade) com recursão
def dfs(grafo, atual, fim, caminho=None, visitados=None):
    if caminho is None:
        caminho = []
    if visitados is None:
        visitados = set()
        
    caminho.append(atual)
    visitados.add(atual)
    
    if atual == fim:
        return caminho
    
    for vizinho in grafo.get(atual, []):
        if vizinho not in visitados:
            resultado = dfs(grafo, vizinho, fim, caminho.copy(), visitados.copy())
            if resultado:
                return resultado
                
    return None

# Executa a busca
caminho = dfs(grafo, "AA", "BB")

# Mostra o caminho encontrado (caso exista)
if caminho:
    print("\nCaminho percorrido pelo DFS até o fim do labirinto:")
    print(" -> ".join(caminho))
    print("\n")
    
    # Formato do labirinto (ajustado para terminal)
    labirinto = """
    ████████████████████████████████████████████████
       AA                            01 █ 02   03 ██
    ██    ██████████████████████████    █    ███████
    ██ 04                       05 █ 06   07   08 ██
    ██    █████████████████████    ███████████    ██
    ██ 09   10 █ 11   12   13 █    █ 14        15 ██
    ██    █    ██████    ██████    ███████████    ██
    ██    █ 16        17 █ 18   19        20 █ 21 ██
    ██    ████████████████    ███████████    ███████
    ██    █ 22        23 █ 24   25 █ 26   27   28 ██
    ██    ███████████    ██████    █    ██████    ██
    ██ 29   30 █ 31   32 █ 33   34 █    █ 35 █    ██
    ███████    █    ██████    ██████    █    █    ██
    ██ 36 █    █    █ 37   38 █ 39   40 █    █    ██
    ██    █    █    █    ██████    ██████    █    ██
    ██    █    █    █ 41   42 █ 43   44 █ 45   46 ██
    ██    █    █    ████████████████    ████████████
    ██    █    █ 47             48 █ 49        50 ██
    ██    █    █    ███████████    ███████████    ██
    ██    █ 51   52 █ 53        54 █ 55   56 █ BB
    ██    █    █    █    ███████████    ██████    ██
    ██ 57   58 █ 59 █ 60             61 █ 62   63 ██
    ████████████████████████████████████████████████
    """

    # Substitui os nós do caminho percorrido por *
    for no in caminho:
        labirinto = labirinto.replace(no, "**")

    # Mostra o labirinto com o caminho percorrido
    print("Labirinto ilustrado com caminho percorrido:")
    print(labirinto)
else:
    print("Nenhum caminho encontrado até o fim do labirinto.")
