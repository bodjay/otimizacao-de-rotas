import random
import math
import copy 
from typing import List, Tuple

default_problems = {
    5: [
        (-23.5505, -46.6333),  # São Paulo, SP
        (-22.9068, -43.1729),  # Rio de Janeiro, RJ
        (-19.9167, -43.9345),  # Belo Horizonte, MG
        (-30.0331, -51.2300),  # Porto Alegre, RS
        (-15.7797, -47.9297)   # Brasília, DF
    ],
    10: [
        (-23.5505, -46.6333),  # São Paulo, SP
        (-22.9068, -43.1729),  # Rio de Janeiro, RJ
        (-19.9167, -43.9345),  # Belo Horizonte, MG
        (-30.0331, -51.2300),  # Porto Alegre, RS
        (-15.7797, -47.9297),  # Brasília, DF
        (-3.7172, -38.5434),   # Fortaleza, CE
        (-12.9714, -38.5014),  # Salvador, BA
        (-8.0476, -34.8770),   # Recife, PE
        (-25.4284, -49.2733),  # Curitiba, PR
        (-16.6809, -49.2533)   # Goiânia, GO
    ],
    12: [
        (-23.5505, -46.6333),  # São Paulo, SP
        (-22.9068, -43.1729),  # Rio de Janeiro, RJ
        (-19.9167, -43.9345),  # Belo Horizonte, MG
        (-30.0331, -51.2300),  # Porto Alegre, RS
        (-15.7797, -47.9297),  # Brasília, DF
        (-3.7172, -38.5434),   # Fortaleza, CE
        (-12.9714, -38.5014),  # Salvador, BA
        (-8.0476, -34.8770),   # Recife, PE
        (-25.4284, -49.2733),  # Curitiba, PR
        (-16.6809, -49.2533),  # Goiânia, GO
        (-1.4554, -48.4902),   # Belém, PA
        (-20.4697, -54.6201)   # Campo Grande, MS
    ],
    15: [
        (-23.5505, -46.6333),  # São Paulo, SP
        (-22.9068, -43.1729),  # Rio de Janeiro, RJ
        (-19.9167, -43.9345),  # Belo Horizonte, MG
        (-30.0331, -51.2300),  # Porto Alegre, RS
        (-15.7797, -47.9297),  # Brasília, DF
        (-3.7172, -38.5434),   # Fortaleza, CE
        (-12.9714, -38.5014),  # Salvador, BA
        (-8.0476, -34.8770),   # Recife, PE
        (-25.4284, -49.2733),  # Curitiba, PR
        (-16.6809, -49.2533),  # Goiânia, GO
        (-1.4554, -48.4902),   # Belém, PA
        (-20.4697, -54.6201),  # Campo Grande, MS
        (-5.7950, -35.2094),   # Natal, RN
        (-22.8842, -43.1040),  # Niterói, RJ
        (-23.9608, -46.3332)   # Santos, SP
    ],
    20: [
        (-23.5505, -46.6333),  # São Paulo, SP
        (-22.9068, -43.1729),  # Rio de Janeiro, RJ
        (-19.9167, -43.9345),  # Belo Horizonte, MG
        (-30.0331, -51.2300),  # Porto Alegre, RS
        (-15.7797, -47.9297),  # Brasília, DF
        (-3.7172, -38.5434),   # Fortaleza, CE
        (-12.9714, -38.5014),  # Salvador, BA
        (-8.0476, -34.8770),   # Recife, PE
        (-25.4284, -49.2733),  # Curitiba, PR
        (-16.6809, -49.2533),  # Goiânia, GO
        (-1.4554, -48.4902),   # Belém, PA
        (-20.4697, -54.6201),  # Campo Grande, MS
        (-5.7950, -35.2094),   # Natal, RN
        (-22.8842, -43.1040),  # Niterói, RJ
        (-23.9608, -46.3332),  # Santos, SP
        (-21.7673, -43.3493),  # Juiz de Fora, MG
        (-22.2528, -54.8167),  # Dourados, MS
        (-23.3045, -51.1693),  # Londrina, PR
        (-22.3145, -49.0587),  # Bauru, SP
        (-29.1686, -51.1794)   # Caxias do Sul, RS
    ]
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
#   - Prioridades diferentes para entregas (medicamentos críticos vs. insumos regulares);
#   - Capacidade limitada de carga dos veículos;
#   - Autonomia limitada dos veículos (distância máxima que pode ser percorrida);
#   - Múltiplos veículos disponíveis (ampliando para o problema de roteamento de veículos - VRP);
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

def genetic_algorithm(
        cities_location: List[dict],
        priorities: List[int],
        population_size: int = 10,
        generations: int = 200,
        mutation_probability: float = 0.5,
        tournament_size: int = 5,
        vehicle_capacity: int = 10,
        max_distance: float = 1000) -> List[dict]:
    """
    Executa o algoritmo genético para otimização de rotas.

    Parâmetros:
    - cities_location (List[dict]): Lista de objetos representando as cidades.
    - population_size (int): Tamanho da população.
    - generations (int): Número de gerações.
    - mutation_probability (float): Probabilidade de mutação.
    - tournament_size (int): Tamanho do torneio para seleção.
    - vehicle_capacity (int): Capacidade máxima do veículo.
    - max_distance (float): Distância máxima que o veículo pode percorrer.

    Retorna:
    - List[dict]: A melhor rota encontrada como uma lista de objetos cidade.
    """
    # Extrair coordenadas das cidades
    cities_coordinates = [(city['latitude'], city['longitude']) for city in cities_location]

    # Gerar população inicial
    population = generate_random_population(cities_coordinates, population_size)

    for generation in range(generations):
        # Calcular fitness para cada indivíduo
        fitnesses = [
            calculate_fitness_with_constraints(individual, priorities, vehicle_capacity, max_distance)
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
    best_route_coordinates = population[best_index]

    # Mapear coordenadas de volta para objetos cidade
    best_route = []
    for coord in best_route_coordinates:
        city = next((city for city in cities_location if city['latitude'] == coord[0] and city['longitude'] == coord[1]), None)
        if city:
            best_route.append(city)

    return best_route

# Exemplo de uso:
# cities = [(0, 0), (1, 1), (2, 2), (3, 3)]
# best_route = genetic_algorithm(cities, population_size=10, generations=50, mutation_probability=0.1, tournament_size=3, vehicle_capacity=5, max_distance=100)
# print(f"Melhor rota: {best_route}")