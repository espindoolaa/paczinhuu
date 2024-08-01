# CLASSE COLETÁVEL EXTRA
import pygame
import random
import constantes
import classe_bolinha_pequena


class Coletavel_extra():
    '''
    Parâmetros:
    bolinhas_pequenas_posicoes: lista de tuplas com as posições (x, y) onde há bolinhas pequenas
    '''

    def __init__(self):
        self.posicao_atual = (80, 80)  # Posição atual do coletável extra
        self.image = pygame.image.load('camarao.png')  # Carrega a imagem do tubarão
        self.tempo_spawn = 0  # Momento em que o tubarão aparece na tela
        self.tempo_vida = 15000  # Tempo de vida do camarão em milisegundos (15 segundos)
        self.vivo = False
        self.coletado = False

        
    def spawn(self):
        if not self.vivo and not self.coletado:
            self.posicao_atual = (80, 80)
            self.spawn_time = pygame.time.get_ticks()  # Registra o tempo de spawn
            self.vivo = True
    
    def renderizar(self, screen):
        if self.vivo:
            screen.blit(self.image, self.posicao_atual)  # Desenha a imagem do camarão na tela
    
    def verificar_coleta(self, posicao_italo):
        if self.vivo:
            camarao_rect = self.image.get_rect(topleft=self.posicao_atual)  # Retângulo da colisão do camarão
            italo_rect = pygame.Rect(posicao_italo.x, posicao_italo.y, 38, 38)  # Retângulo de colisão de Ítalo
            # Verificar a colisão entre o retângulo do camarão e o retângulo do ítalo
            if camarao_rect.colliderect(italo_rect):
                self.vivo = False  # "Inativa" o camarão
                self.coletado = True
                
                return True  # Foi coletado

        return False
    
    def atualizar(self):
        if self.vivo and (pygame.time.get_ticks() - self.tempo_spawn > self.tempo_vida):
            self.vivo = False  # Se o tempo expirar, inativa
            self.coletado = True


    
