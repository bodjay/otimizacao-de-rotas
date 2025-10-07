import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../..')))

from otimizador import genetic_algorithm as ga

def calculate_route_by_restrictions(locations, restrictions, population_size=100, generations=500, mutation_rate=0.01):
    """
    Calculate the optimal route based on given locations and restrictions using a genetic algorithm.

    :param locations: List of locations to visit.
    :param restrictions: Dictionary of restrictions to consider (e.g., time windows, vehicle capacity).
    :param population_size: Number of individuals in the population.
    :param generations: Number of generations to evolve.
    :param mutation_rate: Probability of mutation for each individual.
    :return: The best route found.
    """

    return ga.genetic_algorithm(genetic_algorithm=locations, 
                           population_size=population_size, 
                           generations=generations, 
                           mutation_probability=mutation_rate, 
                           tournament_size=5, 
                           vehicle_capacity=restrictions.get('vehicle_capacity', 100), 
                           max_distance=restrictions.get('max_distance', 1000))

