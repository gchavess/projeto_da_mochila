import random
""
# --- Parâmetros iniciais ---
pesos = [2, 3, 4, 5]
valores = [3, 4, 5, 6]
capacidade = 5
n_itens = len(pesos)

populacao_tamanho = 20
geracoes = 100
taxa_mutacao = 0.1

def gerar_individuo():
    return [random.randint(0, 1) for _ in range(n_itens)]

def calcular_aptidao(individuo):
    peso_total = sum(p * i for p, i in zip(pesos, individuo))
    valor_total = sum(v * i for v, i in zip(valores, individuo))
    if peso_total > capacidade:
        return 0
    return valor_total

def selecao(populacao):
    torneio = random.sample(populacao, 3)
    return max(torneio, key=calcular_aptidao)

def crossover(pai1, pai2):
    ponto = random.randint(1, n_itens - 1)
    filho1 = pai1[:ponto] + pai2[ponto:]
    filho2 = pai2[:ponto] + pai1[ponto:]
    return filho1, filho2

def mutar(individuo):
    for i in range(n_itens):
        if random.random() < taxa_mutacao:
            individuo[i] = 1 - individuo[i]

def algoritmo_genetico():
    populacao = [gerar_individuo() for _ in range(populacao_tamanho)]
    melhor = max(populacao, key=calcular_aptidao)

    for _ in range(geracoes):
        nova_populacao = []
        while len(nova_populacao) < populacao_tamanho:
            pai1 = selecao(populacao)
            pai2 = selecao(populacao)
            filho1, filho2 = crossover(pai1, pai2)
            mutar(filho1)
            mutar(filho2)
            nova_populacao += [filho1, filho2]
        populacao = nova_populacao
        melhor_da_geracao = max(populacao, key=calcular_aptidao)
        if calcular_aptidao(melhor_da_geracao) > calcular_aptidao(melhor):
            melhor = melhor_da_geracao

    return melhor, calcular_aptidao(melhor)

if __name__ == "__main__":
    melhor_solucao, valor_max = algoritmo_genetico()
    print("Melhor solução:", melhor_solucao)
    print("Valor total:", valor_max)
