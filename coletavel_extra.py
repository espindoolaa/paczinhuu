# CLASSE COLETÁVEL EXTRA

import pygame
import random
import constantes

class Coletavel_extra():
    def __init__(self, posicoes):
        self.posicoes = posicoes
        self.x = posicoes[0]
        self.y = posicoes[1]
        
    def renderizar(self, screen):
        for pos in self.posicoes:
            pygame.draw.circle(screen, (255, 0, 0), pos, constantes.RAIO_BOLINHA_GRANDE)
    def coleta_bolinha_grande(self, ItaloSena):
        retangulo_da_bolinha_grande = pygame.Rect(self.x - self.constantes.RAIO_BOLINHA_GRANDE, self.y - self.constantes.RAIO_BOLINHA_GRANDE, self.constantes.RAIO_BOLINHA_GRANDE*2, self.constantes.RAIO_BOLINHA_GRANDE*2)
        return retangulo_da_bolinha_grande.colliderect(ItaloSena) 

    
