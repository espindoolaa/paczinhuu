# CLASSE BOLINHA GRANDE

import pygame
import random
import constantes
import classe_italo

# BOLINHA GRANDE
class Bolinha_grande:
    def __init__(self, posicoes):
        self.posicoes = posicoes
        self.x = posicoes[0]
        self.y = posicoes[1]
        
    def renderizar(self, screen):
        for pos in self.posicoes:
            pygame.draw.circle(screen, (255, 0, 0), pos, constantes.RAIO_BOLINHA_GRANDE)

    # def coleta_bolinha_grande(self, ItaloSena):
    #     retangulo_da_bolinha_grande = pygame.Rect(self.x - self.constantes.RAIO_BOLINHA_GRANDE, self.y - self.constantes.RAIO_BOLINHA_GRANDE, self.constantes.RAIO_BOLINHA_GRANDE*2, self.constantes.RAIO_BOLINHA_GRANDE*2)
    #     return retangulo_da_bolinha_grande.colliderect(ItaloSena)

    def coleta_bolinha_grande(self, italosena):
        for pos in self.posicoes:
            retangulo_da_bolinha_grande = pygame.Rect(pos[0] - constantes.RAIO_BOLINHA_GRANDE, pos[1] - constantes.RAIO_BOLINHA_GRANDE, constantes.RAIO_BOLINHA_GRANDE*2, constantes.RAIO_BOLINHA_GRANDE*2)
            if retangulo_da_bolinha_grande.colliderect(italosena):
                self.posicoes.remove(pos)
                return True
        return False
