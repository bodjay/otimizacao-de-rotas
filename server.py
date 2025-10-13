import json
from fastmcp import FastMCP
from tools.tsp import find_best_route

mcp = FastMCP("Otimizador de Rotas - TSP Solver")

@mcp.tool
def city_coords(city: list) -> list:
    with open("tools/municipios.json", "r", encoding='utf-8-sig') as f:
        data = json.load(f)

    results = []
    for c in city:
        print(f"Buscando pela cidade: {c}")
        result = next((item for item in data if item["nome"] == c), None)
        if result:
            results.append(result)

    return results

@mcp.tool
def tsp_solver(cities: list, ) -> list:
    return find_best_route(cities)

if __name__ == "__main__":
    mcp.run(transport="http", host="127.0.0.1", port=8000)