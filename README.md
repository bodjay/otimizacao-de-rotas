# 1. Sistema de Otimização de Rotas via Algoritmos Genéticos

### Arquitetura
1. O projeto conta com o algoritmo genetico disponibilizado pela FIAP mas manipulado para atender os casos de uso;
2. FastMCP Como ferramenta para disponibilização de ferramentas que se conectam com agentes.

## 1.1. Incluir restrições realistas
Para considerar as restrições na otimizção, é preciso consideralas no momento da avaliação dos resultados. Neste caso, foi criado um novo método de fitness que abrange as novas restrições.

#### tools/otimizador/genetic.py:252:1
```py
# Representação genética para rotas e função fitness com restrições realistas
#   - Prioridades diferentes para entregas (medicamentos críticos vs. insumos regulares);
#   - Capacidade limitada de carga dos veículos;
#   - Autonomia limitada dos veículos (distância máxima que pode ser percorrida);

def calculate_fitness_with_constraints(path: List[Tuple[float, float]], priorities: List[int], vehicle_capacity: int, max_distance: float) -> float: 
```

## 1.2. Visualizar as rotas otimizadas em um mapa para fácil interpretação.

Para o mapa iterativo e facilitar a visualizar a otimização das rotas, execute o comando na raiz do projeto. Os caminhos são marcados com INICIO e FIM para facilitar a interpretação da rota.

>NOTA <i>As saídas estarão presentes no diretório `outputs/`.</i>
```bash
!python demo.py
```

- [Mapa iterativo com 5 rotas](/outputs/best_route_5.html)
- [Mapa iterativo com 10 rotas](/outputs/best_route_5.html)
- [Mapa iterativo com 12 rotas](/outputs/best_route_5.html)

## 2. (Em desenvolvimento) Integração com LLMs para Geração de Instruções e Relatórios

Para a integração com LLM, um conjunto de tools foi implementado. Este por sua vez possui duas ferramentas:
1. `city_coords` - Localiza as informações de latitude e longitude de uma determinada cidade.
2. `tsp_solver` - Executa o método responsável por calcular a melhor rota. (O mesmo utilizado anteriormente)

Embora não utilizado, este projeto conta com um servidor MCP pronto para ser consumido por uma LLM.

Utilize o arquivo `tools/client.py` como exemplo para visualização das ferramentas em ação.  
```sh
!python tools/client.py 
```


> NOTA É preciso inicializar o servidor de mcp através do comando `python tools/server.py`

# TODO

## 2.1 Gerar instruções detalhadas para motoristas e equipes de entrega

- Criar relatórios diários/semanais sobre eficiência de rotas,
economia de tempo e recursos;
- Sugerir melhorias no processo com base nos padrões identificados.
Página 6 de 8
- Implementar prompts eficientes para extrair informações úteis da
LLM;
- Permitir que o sistema responda as perguntas em linguagem natural
sobre as rotas e entregas

# refs
- https://github.com/FIAP/genetic_algorithm_tsp
- https://github.com/kelvins/municipios-brasileiros/tree/main/json
