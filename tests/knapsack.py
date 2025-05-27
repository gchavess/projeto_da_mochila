import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from algorithm import genetic_algorithm
from config import ITEMS, CAPACITY, POPULATION_SIZE, GENERATIONS, MUTATION_RATE


def test_algoritmo_genetico():
    melhor_solucao, valor = genetic_algorithm(
        items=ITEMS,
        capacity=CAPACITY,
        population_size=POPULATION_SIZE,
        generations=GENERATIONS,
        mutation_rate=MUTATION_RATE
    )

    assert isinstance(melhor_solucao, list)
    assert all(isinstance(bit, int) and bit in (0, 1) for bit in melhor_solucao)
    assert isinstance(valor, int)
    assert valor >= 0
