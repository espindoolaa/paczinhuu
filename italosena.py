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

        self.furia_timer = 0  # Temporizador do estado de fúria
        self.furia_duracao = 10000  # Duração tempo de fúria

        self.hit_box = pygame.Rect(self.posicao.x, self.posicao.y, 38, 38)
        self.jogador_mask = pygame.mask.Mask((self.hit_box.width, self.hit_box.height))

    def iniciar_furia(self):
        self.em_furia = True
        self.furia_timer = pygame.time.get_ticks()  # Registra o tempo do estado de fúria
    
    def atualizar_furia(self):
        if self.em_furia and (pygame.time.get_ticks() - self.furia_timer > self.furia_duracao):
            self.em_furia = False

    def movimentacao(self):
        if self.em_furia:
            vel = constantes.VEL_FURIA
        else:
            vel = constantes.VEL_NORMAL

        if pygame.key.get_pressed()[pygame.K_UP]:
            self.y_velocidade = -vel
            self.x_velocidade = 0
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            self.y_velocidade = vel
            self.x_velocidade = 0
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.x_velocidade = -vel
            self.y_velocidade = 0
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.x_velocidade = vel
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
        
    def get_mask(self):
        surface = pygame.Surface((self.hit_box.width, self.hit_box.height), pygame.SRCALPHA)
        surface.fill((255, 255, 255))
        return pygame.mask.from_surface(surface)

    def retornar_posicao(self):
        return self.posicao
