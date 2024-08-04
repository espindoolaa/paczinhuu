import pygame
from pathlib import Path

# Esse documento contém constantes utilizadas no nosso projeto

VEL_NORMAL = 3
VEL_FURIA = 4
RAIO_PEIXE = 12
RAIO_BAIACU = RAIO_PEIXE
RAIO_BOLINHA = 7
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

# --------------=-------- IMAGENS ------------------------------
PRAIA = pygame.image.load(Path('imgs', 'praia.png'))
BOTAO = pygame.image.load(Path('imgs', 'botao.png'))
BOTAO_HOOVER = pygame.image.load(Path('imgs', 'botao_hoover.png'))
peixe = pygame.image.load(Path('imgs', 'peixe.png'))
PEIXE = pygame.transform.scale_by(peixe, 1/8)
baiacu = pygame.image.load(Path('imgs', 'baiacu.png'))
BAIACU = pygame.transform.scale_by(baiacu, 1/14)
# --------------------------------------------------------------
