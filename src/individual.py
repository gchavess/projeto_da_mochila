import random
from typing import List, Tuple


def generate_individual(n_items: int) -> List[int]:
    return [random.randint(0, 1) for _ in range(n_items)]


def calculate_fitness(individual: List[int], items: List[Tuple[int, int]], capacity: int) -> int:
    total_weight = sum(weight * bit for (weight, _), bit in zip(items, individual))
    if total_weight > capacity:
        return 0
    return sum(value * bit for (_, value), bit in zip(items, individual))


def mutate(individual: List[int], mutation_rate: float) -> None:
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            individual[i] ^= 1


def calculate_total_weight(individual: List[int], items: List[Tuple[int, int]]) -> int:
    return sum(weight * bit for (weight, _), bit in zip(items, individual))
