import random
from typing import List, Tuple

# --- Parâmetros iniciais ---
ITEMS = [(2, 3), (3, 4), (4, 5), (5, 6)]  # (peso, valor)
CAPACITY = 5
POPULATION_SIZE = 20
GENERATIONS = 100
MUTATION_RATE = 0.1
TOURNAMENT_SIZE = 3

def generate_individual(n_items: int) -> List[int]:
    """Gera um indivíduo aleatório com n_items bits (0 ou 1)."""
    return [random.randint(0, 1) for _ in range(n_items)]

def calculate_fitness(individual: List[int], items: List[Tuple[int, int]], capacity: int) -> int:
    """Calcula a aptidão de um indivíduo, retornando 0 se exceder a capacidade."""
    total_weight = sum(weight * selected for (weight, _), selected in zip(items, individual))
    if total_weight > capacity:
        return 0
    return sum(value * selected for (_, value), selected in zip(items, individual))

def tournament_selection(population: List[List[int]], items: List[Tuple[int, int]], capacity: int) -> List[int]:
    """Seleciona o melhor indivíduo de um torneio aleatório."""
    tournament = random.sample(population, TOURNAMENT_SIZE)
    return max(tournament, key=lambda ind: calculate_fitness(ind, items, capacity))

def crossover(parent1: List[int], parent2: List[int]) -> Tuple[List[int], List[int]]:
    """Realiza crossover de um ponto entre dois pais."""
    point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

def mutate(individual: List[int], mutation_rate: float) -> None:
    """Muta o indivíduo com base na taxa de mutação."""
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            individual[i] = 1 - individual[i]

def genetic_algorithm(items: List[Tuple[int, int]], capacity: int, population_size: int,
                     generations: int, mutation_rate: float) -> Tuple[List[int], int]:
    """Executa o algoritmo genético para o problema da mochila."""
    n_items = len(items)
    population = [generate_individual(n_items) for _ in range(population_size)]
    best_individual = max(population, key=lambda ind: calculate_fitness(ind, items, capacity))
    best_fitness = calculate_fitness(best_individual, items, capacity)

    for _ in range(generations):
        new_population = []
        while len(new_population) < population_size:
            parent1 = tournament_selection(population, items, capacity)
            parent2 = tournament_selection(population, items, capacity)
            child1, child2 = crossover(parent1, parent2)
            mutate(child1, mutation_rate)
            mutate(child2, mutation_rate)
            new_population.extend([child1, child2])
        population = new_population[:population_size]  # Trunca se exceder
        current_best = max(population, key=lambda ind: calculate_fitness(ind, items, capacity))
        current_fitness = calculate_fitness(current_best, items, capacity)
        if current_fitness > best_fitness:
            best_individual = current_best
            best_fitness = current_fitness

    return best_individual, best_fitness

def main():
    """Função principal para executar o algoritmo genético."""
    best_solution, max_value = genetic_algorithm(ITEMS, CAPACITY, POPULATION_SIZE, GENERATIONS, MUTATION_RATE)
    print(f"Melhor solução: {best_solution}")
    print(f"Valor total: {max_value}")
    print(f"Peso total: {sum(weight * selected for (weight, _), selected in zip(ITEMS, best_solution))}")

if __name__ == "__main__":
    main()
