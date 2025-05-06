from src.knapsack_ga import algoritmo_genetico

def test_algoritmo_genetico():
    melhor_solucao, valor = algoritmo_genetico()
    assert isinstance(melhor_solucao, list)
    assert isinstance(valor, int)
