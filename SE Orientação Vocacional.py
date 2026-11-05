"""
Sistema de Orientação Vocacional - protótipo em Python
Modelo: rules-based (pontuação por regras)
Autor: ChatGPT
Como usar: execute e responda o questionário (opções A/B/C etc).
Saída: lista de carreiras recomendadas ordenadas por pontuação.
"""

from collections import defaultdict, OrderedDict

# --- Perguntas (chave -> pergunta + opções) ---
QUESTIONS = OrderedDict([
    ("q1",  ("Você prefere trabalhar com números/algoritmos ou com pessoas?", 
             {"A":"Números/algoritmos", "B":"Pessoas", "C":"Ambos"})),
    ("q2",  ("Gosta de desenhar, criar visualmente (layouts, ilustrações)?",
             {"A":"Sim (criação visual)", "B":"Pouco", "C":"Não"})),
    ("q3",  ("Prefere rotina estável ou tarefas diferentes todo dia?",
             {"A":"Rotina estável", "B":"Tarefas diferentes", "C":"Algo entre"})),
    ("q4",  ("Curte resolver problemas lógicos e abstratos (puzzles, código)?",
             {"A":"Muito", "B":"Mais ou menos", "C":"Não"})),
    ("q5",  ("Tem interesse forte em saúde, biologia ou cuidar de pessoas?",
             {"A":"Sim", "B":"Um pouco", "C":"Não"})),
    ("q6",  ("Gosta de argumentar, debater e entender leis/justiça?",
             {"A":"Sim", "B":"Pouco", "C":"Não"})),
    ("q7",  ("Prefere ambiente acadêmico/pesquisa ou prático/industria?",
             {"A":"Pesquisa/academia", "B":"Prático/indústria", "C":"Ambos"})),
    ("q8",  ("Aprecia estatística, análise de dados e tirar conclusões?",
             {"A":"Sim", "B":"Mais ou menos", "C":"Não"})),
    ("q9",  ("Você gosta de escrever (artigos, notícias, roteiros)?",
             {"A":"Sim", "B":"Às vezes", "C":"Não"})),
    ("q10", ("Prefere trabalhar ao ar livre ou no escritório/laboratório?",
             {"A":"Ao ar livre", "B":"Escritório/lab", "C":"Indiferente"})),
    ("q11", ("Gosta de tecnologia/gadgets e se manter atualizado sobre eles?",
             {"A":"Sim", "B":"Pouco", "C":"Não"})),
    ("q12", ("Gosta de ensinar ou orientar outras pessoas?",
             {"A":"Sim", "B":"Um pouco", "C":"Não"})),
    ("q13", ("Você é criativo com sabores/receitas/produtos manuais?",
             {"A":"Sim", "B":"Mais ou menos", "C":"Não"})),
    ("q14", ("Gosta de planejar, organizar e gerir equipes/projetos?",
             {"A":"Sim", "B":"Pouco", "C":"Não"})),
    ("q15", ("Tem interesse em economia, finanças e mercados?",
             {"A":"Sim", "B":"Pouco", "C":"Não"})),
    ("q16", ("Gosta de anatomia e procedimentos técnicos precisos?",
             {"A":"Sim", "B":"Pouco", "C":"Não"})),
    ("q17", ("Tem interesse em segurança digital e proteção de dados?",
             {"A":"Sim", "B":"Um pouco", "C":"Não"})),
    ("q18", ("Gosta de estética e moda, acompanhar tendências?",
             {"A":"Sim", "B":"Pouco", "C":"Não"})),
    ("q19", ("Prefere atividades físicas e esportes como trabalho?",
             {"A":"Sim", "B":"Às vezes", "C":"Não"})),
    ("q20", ("Gosta de trabalhar com máquinas, estruturas, cálculo aplicado?",
             {"A":"Sim", "B":"Pouco", "C":"Não"})),
])

# --- Carreiras possíveis (lista/keys) ---
CAREERS = [
    "Engenharia (Geral)",
    "Engenharia Civil",
    "Engenharia Elétrica",
    "Engenharia de Software / Ciência da Computação",
    "Sistemas de Informação",
    "Segurança da Informação",
    "Análise de Dados / Estatística",
    "Matemática / Física (Pesquisa/Acadêmico)",
    "Medicina",
    "Enfermagem",
    "Farmácia",
    "Biologia / Ciências Biológicas",
    "Psicologia",
    "Direito",
    "Administração / Gestão",
    "Economia / Finanças",
    "Design Gráfico / Multimídia",
    "UX/UI Design",
    "Arquitetura",
    "Comunicação / Jornalismo",
    "Marketing / Publicidade",
    "Pedagogia / Educação",
    "Educação Física / Esportes",
    "Gastronomia",
    "Turismo / Hotelaria",
    "Agronomia / Ciências Agrárias",
    "Moda",
    "Teatro / Artes Cênicas",
    "Música",
    "Química / Engenharia Química",
    "Pesquisa em Química/Bioquímica",
    "Farmacologia / Biomedicina"
]

# --- Regras de inferência (>=30) ---
# Cada regra: condições sobre respostas (question_key, valor_aceito) e
# consequencias: dicionario career->points
# valor_aceito pode ser str ou list
RULES = [
    # 1
    ( [("q1","A")], {"Engenharia de Software / Ciência da Computação":3, "Análise de Dados / Estatística":2, "Matemática / Física (Pesquisa/Acadêmico)":2} ),
    # 2
    ( [("q1","B")], {"Psicologia":3, "Pedagogia / Educação":2, "Comunicação / Jornalismo":2, "Medicina":1} ),
    # 3
    ( [("q4","A")], {"Engenharia (Geral)":2, "Engenharia de Software / Ciência da Computação":3, "Matemática / Física (Pesquisa/Acadêmico)":3} ),
    # 4
    ( [("q2","A")], {"Design Gráfico / Multimídia":3, "Arquitetura":2, "Moda":2, "UX/UI Design":2} ),
    # 5
    ( [("q3","A")], {"Administração / Gestão":2, "Contabilidade":0, "Engenharia Civil":2} ),
    # 6
    ( [("q5","A")], {"Medicina":4, "Enfermagem":3, "Farmácia":2, "Biologia / Ciências Biológicas":2} ),
    # 7
    ( [("q6","A")], {"Direito":4, "Comunicação / Jornalismo":1} ),
    # 8
    ( [("q7","A")], {"Matemática / Física (Pesquisa/Acadêmico)":3, "Pesquisa em Química/Bioquímica":3} ),
    # 9
    ( [("q8","A")], {"Análise de Dados / Estatística":4, "Economia / Finanças":2, "Engenharia (Geral)":1} ),
    # 10
    ( [("q9","A")], {"Comunicação / Jornalismo":3, "Marketing / Publicidade":2, "Direito":1} ),
    # 11
    ( [("q10","A")], {"Agronomia / Ciências Agrárias":3, "Turismo / Hotelaria":2, "Educação Física / Esportes":2} ),
    # 12
    ( [("q11","A")], {"Engenharia de Software / Ciência da Computação":3, "Sistemas de Informação":2, "Segurança da Informação":2} ),
    # 13
    ( [("q12","A")], {"Pedagogia / Educação":4, "Psicologia":2, "Treinamento Corporativo":1} ),
    # 14
    ( [("q13","A")], {"Gastronomia":4, "Design Gráfico / Multimídia":1, "Artes Cênicas":0} ),
    # 15
    ( [("q14","A")], {"Administração / Gestão":4, "Engenharia (Geral)":1, "Marketing / Publicidade":1} ),
    # 16
    ( [("q15","A")], {"Economia / Finanças":4, "Administração / Gestão":2, "Análise de Dados / Estatística":2} ),
    # 17
    ( [("q16","A")], {"Medicina":3, "Enfermagem":3, "Biomedicina / Farmacologia":2, "Dentistry":0} ),
    # 18
    ( [("q17","A")], {"Segurança da Informação":4, "Sistemas de Informação":2, "Engenharia de Software / Ciência da Computação":2} ),
    # 19
    ( [("q18","A")], {"Moda":4, "Design Gráfico / Multimídia":2, "Marketing / Publicidade":1} ),
    # 20
    ( [("q19","A")], {"Educação Física / Esportes":4, "Fisioterapia":1} ),
    # 21
    ( [("q20","A")], {"Engenharia Civil":3, "Engenharia Elétrica":3, "Engenharia (Geral)":2} ),
    # 22 - combinação: números fortes + gosto por stats => Data Science
    ( [("q1","A"), ("q8","A")], {"Análise de Dados / Estatística":4, "Engenharia de Software / Ciência da Computação":2} ),
    # 23 - criatividade + tecnologia => UX/UI ou Design + Tech
    ( [("q2","A"), ("q11","A")], {"UX/UI Design":3, "Design Gráfico / Multimídia":2, "Engenharia de Software / Ciência da Computação":1} ),
    # 24 - interesse em saúde + gosto por procedimentos técnicos => Medicina/Enfermagem
    ( [("q5","A"), ("q16","A")], {"Medicina":4, "Enfermagem":3} ),
    # 25 - gosto por escrever + interesse social => Jornalismo/Comunicação
    ( [("q9","A"), ("q1","B")], {"Comunicação / Jornalismo":4, "Marketing / Publicidade":1} ),
    # 26 - gostar de gerir + interesse por finanças => Administração/Economia
    ( [("q14","A"), ("q15","A")], {"Administração / Gestão":3, "Economia / Finanças":3} ),
    # 27 - outdoor + interesse por agricultura => Agronomia
    ( [("q10","A"), ("q11","C")], {"Agronomia / Ciências Agrárias":4} ),
    # 28 - gosto por estética + criatividade => Moda/Design
    ( [("q2","A"), ("q18","A")], {"Moda":3, "Design Gráfico / Multimídia":2} ),
    # 29 - prefere tarefas variadas + criatividade => Artes cênicas/música/gastronomia
    ( [("q3","B"), ("q13","A")], {"Gastronomia":3, "Teatro / Artes Cênicas":2, "Música":2} ),
    # 30 - interessa em tecnologia + segurança => Segurança da Informação
    ( [("q11","A"), ("q17","A")], {"Segurança da Informação":4} ),
    # 31 - gosto por ensinar + interesse em área especifica => Pedagogia especializada
    ( [("q12","A"), ("q1","A")], {"Pedagogia / Educação":2, "Matemática / Física (Pesquisa/Acadêmico)":2} ),
    # 32 - gosto por estrutura/estética + construção => Arquitetura
    ( [("q2","A"), ("q20","A")], {"Arquitetura":4} ),
    # 33 - estatística + finanças => Financial Analyst / Economista
    ( [("q8","A"), ("q15","A")], {"Economia / Finanças":4, "Análise de Dados / Estatística":2} ),
    # 34 - interesse em química + pesquisa => Química/Engenharia Química
    ( [("q7","A"), ("q20","A")], {"Química / Engenharia Química":3, "Pesquisa em Química/Bioquímica":3} ),
    # 35 - gosta de trabalhar com pessoas e saúde mental => Psicologia
    ( [("q1","B"), ("q5","B")], {"Psicologia":4} ),
    # 36 - gosta de viajar/atender pessoas => Turismo/Hotelaria
    ( [("q10","A"), ("q3","B")], {"Turismo / Hotelaria":4} ),
    # 37 - comunicação + marketing => Marketing
    ( [("q9","A"), ("q14","A")], {"Marketing / Publicidade":4} ),
    # 38 - gosto por lógica e construção => Engenharia Elétrica/Engenharia
    ( [("q4","A"), ("q20","A")], {"Engenharia Elétrica":3, "Engenharia (Geral)":2} ),
    # 39 - interesse por ciências da vida + pesquisa => Biologia/Pesquisa
    ( [("q5","A"), ("q7","A")], {"Biologia / Ciências Biológicas":3, "Pesquisa em Química/Bioquímica":2} ),
    # 40 - gosto por estética visual + usabilidade => UX/UI forte
    ( [("q2","A"), ("q8","B")], {"UX/UI Design":3, "Design Gráfico / Multimídia":2} ),
]

# --- Motor de inferência simples ---
def match_rule(rule_conditions, answers):
    """Verifica se todas as condições da regra são satisfeitas pelas respostas."""
    for (qk, expected) in rule_conditions:
        if qk not in answers:
            return False
        val = answers[qk]
        if isinstance(expected, list):
            if val not in expected:
                return False
        else:
            if val != expected:
                return False
    return True

def infer(answers):
    """Aplica regras e soma pontos nas carreiras. Retorna ranking."""
    scores = defaultdict(int)
    matched_rules = []
    for conditions, consequents in RULES:
        if match_rule(conditions, answers):
            matched_rules.append((conditions, consequents))
            for career, pts in consequents.items():
                scores[career] += pts
    return scores, matched_rules

# --- Utilitários para pergunta/resposta interativa ---
def ask_user():
    print("=== Sistema de Orientação Vocacional (protótipo) ===\nResponda com a letra da opção (A/B/C).")
    answers = {}
    for key, (text, opts) in QUESTIONS.items():
        print(f"\n{ text }")
        for k,opt in opts.items():
            print(f"  {k}) {opt}")
        while True:
            resp = input("Resposta: ").strip().upper()
            if resp in opts:
                answers[key] = resp
                break
            else:
                print("Opção inválida. Digite A, B ou C.")
    return answers

def pretty_print_results(scores):
    if not scores:
        print("\nNenhuma regra foi satisfeita. Tente respostas diferentes ou revise o questionário.")
        return
    print("\n=== Recomendação (top 10) ===")
    ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    for i,(career,pts) in enumerate(ranked[:10], start=1):
        print(f"{i}. {career} — pontuação: {pts}")
    print("\nObservação: este é um protótipo baseado em regras simples. Use como orientação inicial.")

# --- Função principal para execução ---
def main():
    answers = ask_user()
    scores, matched = infer(answers)
    pretty_print_results(scores)
    # debug opcional: mostrar regras correspondidas
    print("\n(Regras satisfeitas: {})".format(len(matched)))
    # for idx,(conds,cons) in enumerate(matched, start=1):
    #     print(f"Regra {idx}: se {conds} => {cons}")

if __name__ == "__main__":
    main()
