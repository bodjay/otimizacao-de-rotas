import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from genetic_algorithm import calculate_distance, calculate_fitness_with_constraints, generate_random_population
import unittest

class TestGeneticAlgorithm(unittest.TestCase):

    def test_calculate_distance(self):
        point1 = (0, 0)
        point2 = (3, 4)
        self.assertEqual(calculate_distance(point1, point2), 5.0)

    def test_calculate_fitness_with_constraints(self):
        path = [(0, 0), (3, 4), (6, 8)]
        priorities = [1, 0, 1]
        fitness = calculate_fitness_with_constraints(path, priorities, vehicle_capacity=5, max_distance=20)
        self.assertLess(fitness, float('inf'))

    def test_generate_random_population(self):
        cities = [(0, 0), (1, 1), (2, 2)]
        population = generate_random_population(cities, 5)
        self.assertEqual(len(population), 5)
        for individual in population:
            self.assertEqual(len(individual), len(cities))

    def test_calculate_fitness_with_constraints_infeasible(self):
        path = [(0, 0), (100, 100), (200, 200)]
        priorities = [0, 1, 1]
        fitness = calculate_fitness_with_constraints(path, priorities, vehicle_capacity=1, max_distance=50)
        self.assertEqual(fitness, float('inf'))

if __name__ == "__main__":
    unittest.main()