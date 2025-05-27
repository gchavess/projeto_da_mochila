from typing import List, Tuple
from individual import generate_individual, calculate_fitness, mutate
from selection import tournament_selection, crossover

def genetic_algorithm(
    items: List[Tuple[int, int]],
    capacity: int,
    population_size: int,
    generations: int,
    mutation_rate: float
) -> Tuple[List[int], int]:
    n_items = len(items)
    population = [generate_individual(n_items) for _ in range(population_size)]

    best_individual = max(population, key=lambda ind: calculate_fitness(ind, items, capacity))
    best_fitness = calculate_fitness(best_individual, items, capacity)

    for _ in range(generations):
        new_population: List[List[int]] = []

        while len(new_population) < population_size:
            parent1 = tournament_selection(population, items, capacity)
            parent2 = tournament_selection(population, items, capacity)
            child1, child2 = crossover(parent1, parent2)
            mutate(child1, mutation_rate)
            mutate(child2, mutation_rate)
            new_population.extend([child1, child2])

        population = new_population[:population_size]

        current_best = max(population, key=lambda ind: calculate_fitness(ind, items, capacity))
        current_fitness = calculate_fitness(current_best, items, capacity)

        if current_fitness > best_fitness:
            best_individual = current_best
            best_fitness = current_fitness

    return best_individual, best_fitness
