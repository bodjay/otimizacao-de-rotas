import pygame
from pygame.locals import *
import random
from genetic_algorithm import genetic_algorithm, default_problems
from draw_functions import draw_paths, draw_plot, draw_cities
import sys
import numpy as np

# Configurações do Pygame
WIDTH, HEIGHT = 800, 400
NODE_RADIUS = 10
FPS = 30
PLOT_X_OFFSET = 450

# Configurações do Algoritmo Genético
N_CITIES = 15
POPULATION_SIZE = 100
GENERATIONS = 50
MUTATION_PROBABILITY = 0.5
TOURNAMENT_SIZE = 3
VEHICLE_CAPACITY = 10
MAX_DISTANCE = 500

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Inicializar cidades
cities_locations = [(random.randint(NODE_RADIUS + PLOT_X_OFFSET, WIDTH - NODE_RADIUS), random.randint(NODE_RADIUS, HEIGHT - NODE_RADIUS))
                    for _ in range(N_CITIES)]

# Inicializar Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Otimização de Rotas")
clock = pygame.time.Clock()

# Executar Algoritmo Genético
best_route = genetic_algorithm(
    cities_locations,
    population_size=POPULATION_SIZE,
    generations=GENERATIONS,
    mutation_probability=MUTATION_PROBABILITY,
    tournament_size=TOURNAMENT_SIZE,
    vehicle_capacity=VEHICLE_CAPACITY,
    max_distance=MAX_DISTANCE
)

NODE_RADIUS = 10

# Loop principal do Pygame
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            running = False

    screen.fill(WHITE)

    # Desenhar cidades e rotas
    draw_cities(screen, cities_locations, RED, NODE_RADIUS)
    # Corrigir largura da linha para um valor fixo
    draw_paths(screen, best_route, BLUE, width=2)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()