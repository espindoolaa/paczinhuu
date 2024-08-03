import pygame
from pathlib import Path

VEL_NORMAL = 3
VEL_FURIA = 4
RAIO_BOLINHA_GRANDE = 12
RAIO_BOLINHA_PEQUENA = 7
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
BOTAO_HOOVER = pygame.image.load(Path('imgs', 'botao_hoover.png'))
peixe = pygame.image.load(Path('imgs', 'peixe.png'))
PEIXE = pygame.transform.scale_by(peixe, 1/8)