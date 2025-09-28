# Otimização de Rotas para Distribuição de Medicamentos e Insumos

O sistema hospitalar enfrenta desafios logísticos na distribuição. eficiente de medicamentos e insumos entre suas diversas unidades e para atendimento domiciliar.

O desafio é desenvolver um sistema de otimização de rotas
utilizando algoritmos genéticos para resolver esse problema de "caixeiro
viajante médico", além de utilizar LLMs para gerar relatórios e instruções claras
para as equipes de entrega.

Este modelo considera as seguintes restrições:
- Prioridades diferentes para entregas (medicamentos críticos vs.
insumos regulares);
- Capacidade limitada de carga dos veículos;
- Autonomia limitada dos veículos (distância máxima que pode ser
percorrida);
- Múltiplos veículos disponíveis (ampliando para o problema de
roteamento de veículos - VRP);

## Sumário
- [INSTALAÇÃO](#INSTALAÇÃO)
- [População inicial](#)
- [Avaliação de aptidão](#)
- [Seleção](#)
- [Cruzamento & mutação](#)
- [Condição de término](#)

## INSTALAÇÃO
```sh
pip install -r requirements.txt
```

## População inicial

Para inicializar os individuos candidatos à solução do problema.
Inicializar população de forma: **Aleatória***, heurística ou a partir de soluções conhecidas.

> _A aleatoriedade pode trazer mais variedade, podendo até mesmo melhorar o resultado da solução._

```python
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
```

## Avaliação de aptidão
- 

## Seleção
- Fazer manutenção de diversidade
- Elitimos
    preserva os melhores indivíduos e os leva para a próxima geração porém, descarta a chance de explorar soluções diversificadas.

- Roleta / Proporcional
    - Bem simples de implementar. Reproduz o que possuir maior valor de fitness comparado com toda a população porém, pode levar a convergencia prematura

- Torneio
    - Seleciona um numero N de indv. de forma aleatória, reproduz o que possuir maior valor de fitness porém, ao ajustar o tamanho do torneio a pressão seletiva e diversidade são afetados.

- Rankeado
    - Ordenados por aptidão. Menos eficacia computacional pois a função de ordenação costumam ser caras.

## Cruzamento & Mutação

## Condição de término