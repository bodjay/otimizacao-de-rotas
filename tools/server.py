import json
from fastmcp import FastMCP
from otimizador.genetic  import genetic_algorithm

mcp = FastMCP("Otimizador de Rotas - TSP Solver")

@mcp.tool
def city_coords(city: list) -> list:
    with open("tools/otimizador/municipios.json", "r", encoding='utf-8-sig') as f:
        data = json.load(f)

    results = []
    for c in city:
        print(f"Buscando pela cidade: {c}")
        result = next((item for item in data if item["nome"] == c), None)
        if result:
            results.append(result)

    return results

@mcp.tool
def tsp_solver(cities: list, priorities: list, vehicle_capacity: int, max_distance: int) -> list:
    return genetic_algorithm(cities, priorities, vehicle_capacity, max_distance)

if __name__ == "__main__":
    mcp.run(transport="http", host="127.0.0.1", port=8000)