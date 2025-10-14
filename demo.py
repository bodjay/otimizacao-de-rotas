import folium
import random
from typing import List, Dict
from tools.otimizador.genetic import genetic_algorithm, default_problems

class RouteVisualizer:
    def __init__(self):
        self.colors = ['red', 'blue', 'green', 'purple', 'orange', 'darkred', 
                      'lightred', 'beige', 'darkblue', 'darkgreen', 'cadetblue', 
                      'darkpurple', 'white', 'pink', 'lightblue', 'lightgreen', 
                      'gray', 'black', 'lightgray']
    
    def create_interactive_map(self, 
                             cities: List[Dict], 
                             best_route: List[Dict],
                             fitness: float,
                             generation: int = None,
                             save_path: str = "route_map.html") -> folium.Map:
        """
        Cria um mapa interativo com a rota otimizada.
        
        Args:
            cities: Lista de cidades com latitude e longitude
            best_route: Melhor rota encontrada pelo algoritmo genético
            fitness: Valor de fitness da rota
            generation: Número da geração (opcional)
            save_path: Caminho para salvar o mapa
            
        Returns:
            Mapa folium interativo
        """
        # Calcular centro do mapa
        lats = [city['latitude'] for city in cities]
        lons = [city['longitude'] for city in cities]
        center_lat = sum(lats) / len(lats)
        center_lon = sum(lons) / len(lons)
        
        # Criar mapa
        m = folium.Map(location=[center_lat, center_lon], zoom_start=12)
        
        # Adicionar título
        title = f"Rota Otimizada - Fitness: {fitness:.2f}"
        if generation is not None:
            title += f" - Geração: {generation}"
        
        title_html = f'''
            <h3 align="center" style="font-size:20px"><b>{title}</b></h3>
        '''
        m.get_root().html.add_child(folium.Element(title_html))
        
        # Adicionar marcadores para todas as cidades
        for i, city in enumerate(cities):
            folium.Marker(
                [city['latitude'], city['longitude']],
                popup=f"Cidade {i+1}<br>Lat: {city['latitude']}<br>Lon: {city['longitude']}",
                tooltip=f"Cidade {i+1}",
                icon=folium.Icon(color='blue', icon='info-sign')
            ).add_to(m)
        
        # Adicionar linha da rota otimizada
        route_coords = [[city['latitude'], city['longitude']] for city in best_route]
        # Fechar o ciclo adicionando o primeiro ponto no final
        route_coords.append(route_coords[0])
        
        folium.PolyLine(
            route_coords,
            color='red',
            weight=3,
            opacity=0.8,
            popup=f"Rota Otimizada - Distância: {fitness:.2f}",
            tooltip="Clique para ver detalhes"
        ).add_to(m)
        
        # Adicionar marcadores especiais para início e fim
        folium.Marker(
            route_coords[0],
            popup="Ponto de Partida",
            tooltip="Início",
            icon=folium.Icon(color='green', icon='play')
        ).add_to(m)
        
        folium.Marker(
            route_coords[-2],  # Última cidade antes de fechar o ciclo
            popup="Ponto de Chegada",
            tooltip="Fim",
            icon=folium.Icon(color='darkred', icon='stop')
        ).add_to(m)
        
        # Salvar mapa
        m.save(save_path)
        return m    
    
def run_demo(problem_size: int = 4):
    """
    Executa uma demonstração completa do algoritmo genético com visualização.
    
    Args:
        problem_size: Tamanho do problema (5, 10, 12, ou 15)
    """
    print(f"🚀 Executando demonstração para {problem_size} cidades...")
    
    # Preparar dados
    cities_data = []
    priorities = []
    vehicle_capacity = random.randint(1, problem_size)
    max_distance = random.randint(10, 1000)

    for i, (lat, lon) in enumerate(default_problems[problem_size]):
        cities_data.append({
            'id': i + 1,
            'name': f'Cidade {i + 1}',
            'latitude': lat,
            'longitude': lon
        })

        priorities.append(random.randint(0 , 1))

        
    
    # Executar algoritmo genético
    print("🧬 Executando algoritmo genético...")    
    best_route = genetic_algorithm(
        cities_data,
        population_size=50,
        generations=100,
        priorities=priorities,
        mutation_probability=0.3,
        tournament_size=5,
        vehicle_capacity=vehicle_capacity,
        max_distance=max_distance
    )
    
    # Calcular fitness da melhor rota
    from tools.otimizador.genetic import calculate_fitness_with_constraints
    best_route_coords = [(city['latitude'], city['longitude']) for city in best_route]
    fitness = calculate_fitness_with_constraints(best_route_coords, priorities, vehicle_capacity, max_distance)
    
    print(f"✅ Melhor rota encontrada com fitness: {fitness:.2f}")
    
    # Visualizar resultados
    visualizer = RouteVisualizer()
    
    # Mapa principal
    print("🗺️ Criando mapa interativo...")
    visualizer.create_interactive_map(
        cities_data, best_route, fitness, save_path=f"outputs/best_route_{problem_size}.html"
    )    
    
    print("📊 Resultados salvos:")
    print(f"   - Mapa da melhor rota: outputs/best_route_{problem_size}.html")
    
    return best_route, fitness

def run_multiple_problems():
    """Executa e compara resultados para diferentes tamanhos de problema."""
    results = {}
    
    for problem_size in [5, 10, 12]:
        print(f"\n{'='*50}")
        print(f"ANALISANDO PROBLEMA COM {problem_size} CIDADES")
        print(f"{'='*50}")
        
        best_route, fitness = run_demo(problem_size)
        results[problem_size] = {
            'fitness': fitness,
            'route': best_route
        }

if __name__ == "__main__":
    # Executar demonstração para 5 cidades
    # run_demo(5)
    
    # Executa e compara resultados para diferentes tamanhos de problema.
    run_multiple_problems()    