from typing import List, Tuple
import math

def calcular_distancia(ponto1: Tuple[float, float], ponto2: Tuple[float, float]) -> float:
    """
    Calcula a distância Euclidiana entre dois pontos.
    """
    return math.sqrt((ponto1[0] - ponto2[0]) ** 2 + (ponto1[1] - ponto2[1]) ** 2)

def calcular_aptidao(caminho: List[Tuple[float, float]]) -> float:
    """
    Calcula a aptidão de um caminho com base na distância total.
    """
    distancia = 0
    n = len(caminho)
    for i in range(n):
        distancia += calcular_distancia(caminho[i], caminho[(i + 1) % n])
    return distancia

def aplicar_restricoes(caminho: List[Tuple[float, float]], prioridades: List[int], capacidade: int, autonomia: float) -> float:
    """
    Aplica restrições ao cálculo de aptidão considerando prioridades, capacidade de carga e autonomia dos veículos.

    Parâmetros:
    - caminho (List[Tuple[float, float]]): Caminho a ser avaliado.
    - prioridades (List[int]): Lista de prioridades para cada ponto do caminho.
    - capacidade (int): Capacidade máxima de carga do veículo.
    - autonomia (float): Distância máxima que o veículo pode percorrer.

    Retorna:
    float: Penalidade aplicada ao caminho com base nas restrições.
    """
    penalidade = 0
    carga_atual = 0
    distancia_total = 0

    for i in range(len(caminho)):
        if i > 0:
            distancia = calcular_distancia(caminho[i - 1], caminho[i])
            distancia_total += distancia

        # Penalidade por exceder a autonomia
        if distancia_total > autonomia:
            penalidade += (distancia_total - autonomia) * 10

        # Penalidade por exceder a capacidade
        carga_atual += prioridades[i]
        if carga_atual > capacidade:
            penalidade += (carga_atual - capacidade) * 5

    return penalidade

# Atualizar a função de aptidão para incluir as restrições
def calcular_aptidao_com_restricoes(caminho: List[Tuple[float, float]], prioridades: List[int], capacidade: int, autonomia: float) -> float:
    """
    Calcula a aptidão de um caminho considerando as restrições.

    Parâmetros:
    - caminho (List[Tuple[float, float]]): Caminho a ser avaliado.
    - prioridades (List[int]): Lista de prioridades para cada ponto do caminho.
    - capacidade (int): Capacidade máxima de carga do veículo.
    - autonomia (float): Distância máxima que o veículo pode percorrer.

    Retorna:
    float: Aptidão do caminho com penalidades aplicadas.
    """
    distancia = calcular_aptidao(caminho)
    penalidade = aplicar_restricoes(caminho, prioridades, capacidade, autonomia)
    return distancia + penalidade