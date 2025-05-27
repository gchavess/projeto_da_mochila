from config import ITEMS, CAPACITY, POPULATION_SIZE, GENERATIONS, MUTATION_RATE
from algorithm import genetic_algorithm
from individual import calculate_total_weight


def main() -> None:
    best_solution, max_value = genetic_algorithm(
        items=ITEMS,
        capacity=CAPACITY,
        population_size=POPULATION_SIZE,
        generations=GENERATIONS,
        mutation_rate=MUTATION_RATE
    )

    total_weight = calculate_total_weight(best_solution, ITEMS)

    print("=== Resultado ===")
    print(f"Melhor solução: {best_solution}")
    print(f"Valor total: {max_value}")
    print(f"Peso total: {total_weight}")


if __name__ == "__main__":
    main()
