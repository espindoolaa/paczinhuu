import pygame
from pathlib import Path

VEL_NORMAL = 3
VEL_FURIA = 4
RAIO_BOLINHA_GRANDE = 10
RAIO_BOLINHA_PEQUENA = 5
SIZE = (1086, 620)
SCREEN = pygame.display.set_mode(SIZE)

MAPA = [
    "#######################", 
    "#@#........#........#@#",  
    "#....###.#...#.###....#", 
    "####.#...##.##...#.####", 
    "---#.#.#.......#.#.#---", 
    "####.#.#.##x##.#.#.####",
    ".......#.#ggg#.#.......",
    "####.#.#.#####.#.#.####",
    "---#...#.......#...#---",
    "####.###.#####.###.####",
    "#....#...#.#.#...#....#",
    "#@#..#.#...#...#.#..#@#",
    "#######################",
]

# Imagens
PRAIA = pygame.image.load(Path('imgs', 'praia.png'))
BOTAO = pygame.image.load(Path('imgs', 'botao.png'))
