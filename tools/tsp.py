from tools.genetic_algorithm import genetic_algorithm

def find_best_route(cities: list) -> list:
    best_route = genetic_algorithm(cities, vehicle_capacity=100, max_distance=1000)
    
    return best_route
