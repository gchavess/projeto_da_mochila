import random
from typing import List, Tuple
from individual import calculate_fitness
from config import TOURNAMENT_SIZE


def tournament_selection(population: List[List[int]], items: List[Tuple[int, int]], capacity: int) -> List[int]:
    tournament = random.sample(population, TOURNAMENT_SIZE)
    return max(tournament, key=lambda ind: calculate_fitness(ind, items, capacity))


def crossover(parent1: List[int], parent2: List[int]) -> Tuple[List[int], List[int]]:
    point = random.randint(1, len(parent1) - 1)
    return (
        parent1[:point] + parent2[point:],
        parent2[:point] + parent1[point:]
    )
