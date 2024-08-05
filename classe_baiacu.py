import pygame
import constantes

# Esse documento contém a classe dos baiacus

# Haverá dois baiacus no mapa

# Ao coletar um baiacu, o jogador fica temporariamente em estado de fúria: sua animação muda, sua velocidade é aumentada e ele adquire a capacidade de matar os tubarões

# Para ganhar o jogo, o jogador deve coletar todos os baiacus, além das bolinhas e dos peixes

# ----------------------------------------------------------------- COLETÁVEL: BAIACU -------------------------------------------------------------
class Coletavel_baiacu:
    # Inicializações
    def __init__(self, posicoes):
        self.posicoes = posicoes
        self.x = posicoes[0]
        self.y = posicoes[1]
    
    # Mostrar os baiacus na tela
    def renderizar(self, tela):
        for pos in self.posicoes:
            tela.blit(constantes.BAIACU, pos)

    # Verificar a colisão com o baiacu para coletá-lo
    def coleta_baiacu(self, italosena):
        for pos in self.posicoes:
            baiacu_rect = pygame.Rect(pos[0] - constantes.RAIO_BAIACU, pos[1] - constantes.RAIO_BAIACU, constantes.RAIO_BAIACU*2, constantes.RAIO_BAIACU*2)
            if baiacu_rect.colliderect(italosena):
                self.posicoes.remove(pos)
                return True
        return False
    
    # Verificar se pegou todos os baiacus
    def verificar_pegou_baiacus(self, qtd):
        if qtd == 2:
            return True
        return False
# -------------------------------------------------------------------------------------------------------------------------------------------------
