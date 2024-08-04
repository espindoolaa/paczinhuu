import pygame
import constantes

# Esse documento contém a classe dos peixes

# Haverá dois peixes no mapa

# Ao coletar um peixe, o jogador fica temporariamente com uma velocidade maior

# Para ganhar o jogo, o jogador deve coletar todos os peixes, além das bolinhas e dos baiacus

# ----------------------------------------------------------------- COLETÁVEL: PEIXE -------------------------------------------------------------
class Coletavel_peixe:
    def __init__(self, posicoes):
        self.posicoes = posicoes
        self.x = posicoes[0]
        self.y = posicoes[1]
    
    # Mostrar os peixes na tela
    def renderizar(self, tela):
        for pos in self.posicoes:
            tela.blit(constantes.PEIXE, pos)

    # Verificar a colisão com o peixe para coletá-lo
    def coleta_peixe(self, italosena):
        for pos in self.posicoes:
            peixe_rect = pygame.Rect(pos[0] - constantes.RAIO_PEIXE, pos[1] - constantes.RAIO_PEIXE, constantes.RAIO_PEIXE*2, constantes.RAIO_PEIXE*2)
            if peixe_rect.colliderect(italosena):
                self.posicoes.remove(pos)
                return True
        return False
    
    # Verificar se pegou todos os peixes
    def verificar_pegou_peixes(self, qtd):
        if qtd == 2:
            return True
        return False
# -------------------------------------------------------------------------------------------------------------------------------------------------
