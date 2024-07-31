import pygame
import random
import constantes
import labirinto

# CLASSE ÍTALO
class ItaloSena:
    def __init__(self, posicao_inicial):
        self.posicao = pygame.Vector2(posicao_inicial)
    
        self.x_velocidade = 0
        self.y_velocidade = 0

        self.em_furia = False

        self.hit_box = pygame.Rect(self.posicao.x, self.posicao.y, 38, 38)
        self.jogador_mask = pygame.mask.Mask((self.hit_box.width, self.hit_box.height))

    
    def movimentacao(self):
        if pygame.key.get_pressed()[pygame.K_UP]:
            if self.em_furia:
                self.y_velocidade = -constantes.VEL_FURIA
            else:
                self.y_velocidade = -constantes.VEL_NORMAL
            self.x_velocidade = 0
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            if self.em_furia:
                self.y_velocidade = constantes.VEL_FURIA
            else:
                self.y_velocidade = constantes.VEL_NORMAL
            self.x_velocidade = 0
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            if self.em_furia:
                self.x_velocidade = -constantes.VEL_FURIA
            else:
                self.x_velocidade = -constantes.VEL_NORMAL
            self.y_velocidade = 0
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            if self.em_furia:
                self.x_velocidade = constantes.VEL_FURIA
            else:
                self.x_velocidade = constantes.VEL_NORMAL
            self.y_velocidade = 0

        # Movimentação Incremental
        steps = max(abs(self.x_velocidade), abs(self.y_velocidade))
        for _ in range(steps):
            if self.x_velocidade != 0:
                self.posicao.x += self.x_velocidade / steps
                self.hit_box.topleft = (self.posicao.x, self.posicao.y)
                if labirinto.checar_colisao(self):
                    self.posicao.x -= self.x_velocidade / steps
                    self.hit_box.topleft = (self.posicao.x, self.posicao.y)
                    break

            if self.y_velocidade != 0:
                self.posicao.y += self.y_velocidade / steps
                self.hit_box.topleft = (self.posicao.x, self.posicao.y)
                if labirinto.checar_colisao(self):
                    self.posicao.y -= self.y_velocidade / steps
                    self.hit_box.topleft = (self.posicao.x, self.posicao.y)
                    break
    
    def renderizar(self):
        # Desenha o personagem na tela como um quadrado amarelo
        pygame.draw.rect(constantes.SCREEN, "yellow", (int(self.posicao.x), int(self.posicao.y), 38, 38))
    
    def colisao(self, lista):
        for parede in lista:
            if self.hit_box.colliderect(parede):
                if self.y_velocidade < 0 and self.x_velocidade == 0: 
                    self.y_italo += 14 
                elif self.y_velocidade > 0 and self.x_velocidade == 0: 
                    self.y_italo -= 1 
                elif self.x_velocidade < 0 and self.y_velocidade == 0: 
                    self.x_italo += 14 
                else:                                                 
                    self.x_italo -= 1

                self.x_velocidade = 0
                self.y_velocidade = 0
        
    def get_mask(self):
        surface = pygame.Surface((self.hit_box.width, self.hit_box.height), pygame.SRCALPHA)
        surface.fill((255, 255, 255))
        return pygame.mask.from_surface(surface)
