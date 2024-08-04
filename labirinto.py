import pygame
from pathlib import Path

# Esse documento contém o labirinto utilizado no nosso jogo e a função para checar a colisão com ele

labirinto_imagem = pygame.image.load(Path('imgs', 'paredes.png'))
labirinto_rect = labirinto_imagem.get_rect()
labirinto_mask = pygame.mask.from_surface(labirinto_imagem)

# ----------------------------------- CHECAR COLISÃO -------------------------------------
def checar_colisao(jogador):
    jogador_mask = jogador.get_mask()
    offset = (jogador.hit_box.x - labirinto_rect.x, jogador.hit_box.y - labirinto_rect.y)
    if labirinto_mask.overlap(jogador_mask, offset):
        return True
    return False
# ----------------------------------------------------------------------------------------
