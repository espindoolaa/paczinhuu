import pygame
import random
import constantes
import labirinto
from pathlib import Path

# CLASSE ÍTALO
class ItaloSena:
    def __init__(self, posicao_inicial):
        self.posicao = pygame.Vector2(posicao_inicial)
    
        self.x_velocidade = 0
        self.y_velocidade = 0

        self.em_furia = False

        self.furia_timer = 0  # Temporizador do estado de fúria
        self.furia_duracao = 10000  # Duração tempo de fúria

        self.hit_box = pygame.Rect(self.posicao.x, self.posicao.y, 30, 30)
        self.jogador_mask = pygame.mask.Mask((self.hit_box.width, self.hit_box.height))

        # Carregar as imagens do personagem
        # Imagens normais
        self.imagens = { 
            'up': [pygame.image.load(Path('imgs', 'up1.png')), pygame.image.load(Path('imgs', 'up2.png'))],
            'down': [pygame.image.load(Path('imgs', 'down1.png')), pygame.image.load(Path('imgs', 'down2.png'))],
            'left': [pygame.image.load(Path('imgs', 'left1.png')), pygame.image.load(Path('imgs', 'left2.png'))],
            'right': [pygame.image.load(Path('imgs', 'right1.png')), pygame.image.load(Path('imgs', 'right2.png'))],
        }
        # Imagens em fúria
        self.imagens_furia = {
            'up': [pygame.image.load(Path('imgs', 'up_fury1.png')), pygame.image.load(Path('imgs', 'up_fury2.png'))],
            'down': [pygame.image.load(Path('imgs', 'down_fury1.png')), pygame.image.load(Path('imgs', 'down_fury2.png'))],
            'left': [pygame.image.load(Path('imgs', 'left_fury1.png')), pygame.image.load(Path('imgs', 'left_fury2.png'))],
            'right': [pygame.image.load(Path('imgs', 'right_fury1.png')), pygame.image.load(Path('imgs', 'right_fury2.png'))],

        }

        self.direcao_atual = 'right'
        self.frame_atual = 0
        self.timer_animacao = pygame.time.get_ticks()

    # Iniciar a fúria
    def iniciar_furia(self):
        self.em_furia = True
        self.furia_timer = pygame.time.get_ticks()  # Registra o tempo do estado de fúria
    
    # Atualizar a fúria e voltar ao normal
    def atualizar_furia(self):
        if self.em_furia and (pygame.time.get_ticks() - self.furia_timer > self.furia_duracao):
            self.em_furia = False

    # Movimentação do personagem (teclas)
    def movimentacao(self):
        if self.em_furia:
            vel = constantes.VEL_FURIA
        else:
            vel = constantes.VEL_NORMAL

        if pygame.key.get_pressed()[pygame.K_UP]:
            self.y_velocidade = -vel
            self.x_velocidade = 0
            self.direcao_atual = 'up'
        elif pygame.key.get_pressed()[pygame.K_DOWN]:
            self.y_velocidade = vel
            self.x_velocidade = 0
            self.direcao_atual = 'down'
        elif pygame.key.get_pressed()[pygame.K_LEFT]:
            self.x_velocidade = -vel
            self.y_velocidade = 0
            self.direcao_atual = 'left'
        elif pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.x_velocidade = vel
            self.y_velocidade = 0
            self.direcao_atual = 'right'
        
        else:
            self.x_velocidade = 0
            self.y_velocidade = 0

        # Movimentação Incremental
        steps = max(abs(self.x_velocidade), abs(self.y_velocidade))
        for _ in range(steps):
            if self.x_velocidade != 0:
                self.posicao.x += self.x_velocidade / steps
                
                if self.posicao.x < 0:
                    self.posicao.x = constantes.SIZE[0]
                elif self.posicao.x > constantes.SIZE[0]:
                    self.posicao.x = 0

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
    
    def atualizar_animacao(self):
        intervalo_animacao = 100 if self.em_furia else 350
        if pygame.time.get_ticks() - self.timer_animacao > intervalo_animacao:  
            self.frame_atual = (self.frame_atual + 1) % len(self.imagens_furia[self.direcao_atual] if self.em_furia else self.imagens[self.direcao_atual])
            self.timer_animacao = pygame.time.get_ticks()
    
    def renderizar(self):
        self.atualizar_animacao()
        imagens_atual = self.imagens_furia if self.em_furia else self.imagens
        imagem_atual = imagens_atual[self.direcao_atual][self.frame_atual]
        constantes.SCREEN.blit(imagem_atual, (int(self.posicao.x), int(self.posicao.y)))

    def get_mask(self):
        surface = pygame.Surface((self.hit_box.width, self.hit_box.height), pygame.SRCALPHA)
        surface.fill((255, 255, 255))
        return pygame.mask.from_surface(surface)

    def retornar_posicao(self):
        return self.posicao
