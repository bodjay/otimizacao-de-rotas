import random
import math
import copy 
from typing import List, Tuple

default_problems = {
5: [(733, 251), (706, 87), (546, 97), (562, 49), (576, 253)],
10:[(470, 169), (602, 202), (754, 239), (476, 233), (468, 301), (522, 29), (597, 171), (487, 325), (746, 232), (558, 136)],
12:[(728, 67), (560, 160), (602, 312), (712, 148), (535, 340), (720, 354), (568, 300), (629, 260), (539, 46), (634, 343), (491, 135), (768, 161)],
15:[(512, 317), (741, 72), (552, 50), (772, 346), (637, 12), (589, 131), (732, 165), (605, 15), (730, 38), (576, 216), (589, 381), (711, 387), (563, 228), (494, 22), (787, 288)]
}

def generate_random_population(cities_location: List[Tuple[float, float]], population_size: int) -> List[List[Tuple[float, float]]]:
    """
    Generate a random population of routes for a given set of cities.

    Parameters:
    - cities_location (List[Tuple[float, float]]): A list of tuples representing the locations of cities,
      where each tuple contains the latitude and longitude.
    - population_size (int): The size of the population, i.e., the number of routes to generate.

    Returns:
    List[List[Tuple[float, float]]]: A list of routes, where each route is represented as a list of city locations.
    """
    return [random.sample(cities_location, len(cities_location)) for _ in range(population_size)]


def calculate_distance(point1: Tuple[float, float], point2: Tuple[float, float]) -> float:
    """
    Calculate the Euclidean distance between two points.

    Parameters:
    - point1 (Tuple[float, float]): The coordinates of the first point.
    - point2 (Tuple[float, float]): The coordinates of the second point.

    Returns:
    float: The Euclidean distance between the two points.
    """
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


def calculate_fitness(path: List[Tuple[float, float]]) -> float:
    """
    Calculate the fitness of a given path based on the total Euclidean distance.

    Parameters:
    - path (List[Tuple[float, float]]): A list of tuples representing the path,
      where each tuple contains the coordinates of a point.

    Returns:
    float: The total Euclidean distance of the path.
    """
    distance = 0
    n = len(path)
    for i in range(n):
        distance += calculate_distance(path[i], path[(i + 1) % n])

    return distance


def order_crossover(parent1: List[Tuple[float, float]], parent2: List[Tuple[float, float]]) -> List[Tuple[float, float]]:
    """
    Perform order crossover (OX) between two parent sequences to create a child sequence.

    Parameters:
    - parent1 (List[Tuple[float, float]]): The first parent sequence.
    - parent2 (List[Tuple[float, float]]): The second parent sequence.

    Returns:
    List[Tuple[float, float]]: The child sequence resulting from the order crossover.
    """
    length = len(parent1)

    # Choose two random indices for the crossover
    start_index = random.randint(0, length - 1)
    end_index = random.randint(start_index + 1, length)

    # Initialize the child with a copy of the substring from parent1
    child = parent1[start_index:end_index]

    # Fill in the remaining positions with genes from parent2
    remaining_positions = [i for i in range(length) if i < start_index or i >= end_index]
    remaining_genes = [gene for gene in parent2 if gene not in child]

    for position, gene in zip(remaining_positions, remaining_genes):
        child.insert(position, gene)

    return child

### demonstration: crossover test code
# Example usage:
# parent1 = [(1, 1), (2, 2), (3, 3), (4,4), (5,5), (6, 6)]
# parent2 = [(6, 6), (5, 5), (4, 4), (3, 3),  (2, 2), (1, 1)]

# # parent1 = [1, 2, 3, 4, 5, 6]
# # parent2 = [6, 5, 4, 3, 2, 1]


# child = order_crossover(parent1, parent2)
# print("Parent 1:", [0, 1, 2, 3, 4, 5, 6, 7, 8])
# print("Parent 1:", parent1)
# print("Parent 2:", parent2)
# print("Child   :", child)


# # Example usage:
# population = generate_random_population(5, 10)

# print(calculate_fitness(population[0]))


# population = [(random.randint(0, 100), random.randint(0, 100))
#           for _ in range(3)]



# TODO: implement a mutation_intensity and invert pieces of code instead of just swamping two. 
def mutate(solution:  List[Tuple[float, float]], mutation_probability: float) ->  List[Tuple[float, float]]:
    """
    Mutate a solution by inverting a segment of the sequence with a given mutation probability.

    Parameters:
    - solution (List[int]): The solution sequence to be mutated.
    - mutation_probability (float): The probability of mutation for each individual in the solution.

    Returns:
    List[int]: The mutated solution sequence.
    """
    mutated_solution = copy.deepcopy(solution)

    # Check if mutation should occur    
    if random.random() < mutation_probability:
        
        # Ensure there are at least two cities to perform a swap
        if len(solution) < 2:
            return solution
    
        # Select a random index (excluding the last index) for swapping
        index = random.randint(0, len(solution) - 2)
        
        # Swap the cities at the selected index and the next index
        mutated_solution[index], mutated_solution[index + 1] = solution[index + 1], solution[index]   
        
    return mutated_solution

### Demonstration: mutation test code    
# # Example usage:
# original_solution = [(1, 1), (2, 2), (3, 3), (4, 4)]
# mutation_probability = 1

# mutated_solution = mutate(original_solution, mutation_probability)
# print("Original Solution:", original_solution)
# print("Mutated Solution:", mutated_solution)


def sort_population(population: List[List[Tuple[float, float]]], fitness: List[float]) -> Tuple[List[List[Tuple[float, float]]], List[float]]:
    """
    Sort a population based on fitness values.

    Parameters:
    - population (List[List[Tuple[float, float]]]): The population of solutions, where each solution is represented as a list.
    - fitness (List[float]): The corresponding fitness values for each solution in the population.

    Returns:
    Tuple[List[List[Tuple[float, float]]], List[float]]: A tuple containing the sorted population and corresponding sorted fitness values.
    """
    # Combine lists into pairs
    combined_lists = list(zip(population, fitness))

    # Sort based on the values of the fitness list
    sorted_combined_lists = sorted(combined_lists, key=lambda x: x[1])

    # Separate the sorted pairs back into individual lists
    sorted_population, sorted_fitness = zip(*sorted_combined_lists)

    return sorted_population, sorted_fitness


# Representação genética para rotas e função fitness com restrições realistas

def calculate_fitness_with_constraints(path: List[Tuple[float, float]], priorities: List[int], vehicle_capacity: int, max_distance: float) -> float:
    """
    Calcula a aptidão de uma rota considerando restrições realistas.

    Parâmetros:
    - path (List[Tuple[float, float]]): Lista de coordenadas representando a rota.
    - priorities (List[int]): Lista de prioridades para cada entrega (1 = alta prioridade, 0 = baixa prioridade).
    - vehicle_capacity (int): Capacidade máxima de carga do veículo.
    - max_distance (float): Distância máxima que o veículo pode percorrer.

    Retorna:
    - float: Valor da aptidão (quanto menor, melhor).
    """
    total_distance = 0
    total_priority_penalty = 0

    # Verificar capacidade do veículo
    if len(path) > vehicle_capacity:
        return float('inf')  # Penalidade alta para rotas que excedem a capacidade

    # Calcular distância total e penalidades de prioridade
    for i in range(len(path)):
        total_distance += calculate_distance(path[i], path[(i + 1) % len(path)])
        if priorities[i] == 0:  # Penalidade para entregas de baixa prioridade
            total_priority_penalty += 10

    # Verificar autonomia do veículo
    if total_distance > max_distance:
        return float('inf')  # Penalidade alta para rotas que excedem a autonomia

    # Aptidão é baseada na distância total e penalidades
    return total_distance + total_priority_penalty

# Exemplo de uso:
# path = [(0, 0), (1, 1), (2, 2)]
# priorities = [1, 0, 1]
# fitness = calculate_fitness_with_constraints(path, priorities, vehicle_capacity=5, max_distance=100)
# print(f"Aptidão da rota: {fitness}")


# Operadores Genéticos: Seleção, Crossover e Mutação

def selection_tournament(population: List[List[Tuple[float, float]]], fitnesses: List[float], tournament_size: int) -> List[Tuple[float, float]]:
    """
    Seleciona um indivíduo da população usando o método de torneio.

    Parâmetros:
    - population (List[List[Tuple[float, float]]]): População atual.
    - fitnesses (List[float]): Lista de valores de aptidão para cada indivíduo.
    - tournament_size (int): Número de indivíduos no torneio.

    Retorna:
    - List[Tuple[float, float]]: O indivíduo vencedor do torneio.
    """
    tournament = random.sample(list(zip(population, fitnesses)), tournament_size)
    winner = min(tournament, key=lambda x: x[1])  # Menor fitness vence
    return winner[0]

def mutate(route: List[Tuple[float, float]], mutation_probability: float) -> List[Tuple[float, float]]:
    """
    Aplica mutação em uma rota com uma dada probabilidade.

    Parâmetros:
    - route (List[Tuple[float, float]]): Rota a ser mutada.
    - mutation_probability (float): Probabilidade de mutação.

    Retorna:
    - List[Tuple[float, float]]: Rota mutada.
    """
    if random.random() < mutation_probability:
        idx1, idx2 = random.sample(range(len(route)), 2)
        route[idx1], route[idx2] = route[idx2], route[idx1]  # Troca dois pontos
    return route


# Integração dos operadores genéticos ao fluxo principal do algoritmo genético

def genetic_algorithm(cities_location: List[Tuple[float, float]], population_size: int, generations: int, mutation_probability: float, tournament_size: int, vehicle_capacity: int, max_distance: float) -> List[Tuple[float, float]]:
    """
    Executa o algoritmo genético para otimização de rotas.

    Parâmetros:
    - cities_location (List[Tuple[float, float]]): Lista de coordenadas das cidades.
    - population_size (int): Tamanho da população.
    - generations (int): Número de gerações.
    - mutation_probability (float): Probabilidade de mutação.
    - tournament_size (int): Tamanho do torneio para seleção.
    - vehicle_capacity (int): Capacidade máxima do veículo.
    - max_distance (float): Distância máxima que o veículo pode percorrer.

    Retorna:
    - List[Tuple[float, float]]: A melhor rota encontrada.
    """
    # Gerar população inicial
    population = generate_random_population(cities_location, population_size)

    for generation in range(generations):
        # Calcular fitness para cada indivíduo
        fitnesses = [
            calculate_fitness_with_constraints(individual, [1] * len(individual), vehicle_capacity, max_distance)
            for individual in population
        ]

        # Nova população
        new_population = []

        while len(new_population) < population_size:
            # Seleção
            parent1 = selection_tournament(population, fitnesses, tournament_size)
            parent2 = selection_tournament(population, fitnesses, tournament_size)

            # Crossover
            child = order_crossover(parent1, parent2)

            # Mutação
            child = mutate(child, mutation_probability)

            new_population.append(child)

        population = new_population

    # Retornar o melhor indivíduo da última geração
    best_index = fitnesses.index(min(fitnesses))
    return population[best_index]

# Exemplo de uso:
# cities = [(0, 0), (1, 1), (2, 2), (3, 3)]
# best_route = genetic_algorithm(cities, population_size=10, generations=50, mutation_probability=0.1, tournament_size=3, vehicle_capacity=5, max_distance=100)
# print(f"Melhor rota: {best_route}")


if __name__ == '__main__':
    N_CITIES = 10
    
    POPULATION_SIZE = 100
    N_GENERATIONS = 100
    MUTATION_PROBABILITY = 0.3
    cities_locations = [(random.randint(0, 100), random.randint(0, 100))
              for _ in range(N_CITIES)]
    
    # CREATE INITIAL POPULATION
    population = generate_random_population(cities_locations, POPULATION_SIZE)

    # Lists to store best fitness and generation for plotting
    best_fitness_values = []
    best_solutions = []
    
    for generation in range(N_GENERATIONS):
  
        
        population_fitness = [calculate_fitness(individual) for individual in population]    
        
        population, population_fitness = sort_population(population,  population_fitness)
        
        best_fitness = calculate_fitness(population[0])
        best_solution = population[0]
           
        best_fitness_values.append(best_fitness)
        best_solutions.append(best_solution)    

        print(f"Generation {generation}: Best fitness = {best_fitness}")

        new_population = [population[0]]  # Keep the best individual: ELITISM
        
        while len(new_population) < POPULATION_SIZE:
            
            # SELECTION
            parent1 = selection_tournament(population, population_fitness, tournament_size=10)
            parent2 = selection_tournament(population, population_fitness, tournament_size=10)
            
            # CROSSOVER
            child1 = order_crossover(parent1, parent2)
            
            ## MUTATION
            child1 = mutate(child1, MUTATION_PROBABILITY)
            
            new_population.append(child1)
            
    
        print('generation: ', generation)
        population = new_population



