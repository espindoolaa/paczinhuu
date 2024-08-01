# CLASSE BOLINHA PEQUENA

import pygame
import constantes
import math
from classe_italo import ItaloSena

class Bolinha_pequena(ItaloSena):        
    def __init__(self, x, y, bolinhas_grandes, mapa):
        self.posicoes = []
        self.mapa = mapa
        self.gerar_posicoes(x, y, bolinhas_grandes)
        self.qtd_bolinhas = 0

    def gerar_posicoes(self, x_inicial, y_inicial, bolinhas_grandes):
        def posicao_valida(x, y):
            if 0 <= y // 47 < len(self.mapa) and 0 <= x // 47 < len(self.mapa[0]):
                mapa_y = y // 47
                mapa_x = x // 47
                return self.mapa[mapa_y][mapa_x] == '.'
            return False
        
        for x in range(x_inicial, 1068, 47):
            for y in range(y_inicial, 620, 47):
                if posicao_valida(x, y) and (x, y) not in bolinhas_grandes.posicoes:
                    self.posicoes.append((x, y))
    
    def renderizar(self, screen):
        for pos in self.posicoes:
            pygame.draw.circle(screen, (255, 255, 0), pos, constantes.RAIO_BOLINHA_PEQUENA)
    
    def verificar_colisao(self, position):
        to_remove = []
        for pos in self.posicoes:
            distancia = math.sqrt((pos[0] - position.x) ** 2 + (pos[1] - position.y) ** 2)
            if distancia < constantes.RAIO_BOLINHA_PEQUENA + 19:  # Considerando que 19 é o raio do personagem
                to_remove.append(pos)
        
        for pos in to_remove:
            self.posicoes.remove(pos)
            self.qtd_bolinhas += 1
        