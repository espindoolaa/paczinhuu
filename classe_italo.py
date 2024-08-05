import pygame
import constantes
import labirinto
from pathlib import Path

# Esse documento contém a classe do Ítalo Sena (jogador)

# --------------------------------------------------------------- CLASSE ÍTALO -----------------------------------------------------------------
class ItaloSena:
    # Inicializações
    def __init__(self, posicao_inicial):
        self.posicao = pygame.Vector2(posicao_inicial)
        self.x_velocidade = 0
        self.y_velocidade = 0
        self.em_furia = False
        self.furia_timer = 0
        self.furia_duracao = 10000
        self.velmaior = False
        self.velmaior_timer = 0
        self.velmaior_duracao = 10000
        self.hit_box = pygame.Rect(self.posicao.x, self.posicao.y, 30, 30)
        self.jogador_mask = pygame.mask.Mask((self.hit_box.width, self.hit_box.height))

        # Carregar as imagens do personagem
        self.imagens = { # Imagens normais
            'up': [pygame.image.load(Path('imgs', 'up1.png')), pygame.image.load(Path('imgs', 'up2.png'))],
            'down': [pygame.image.load(Path('imgs', 'down1.png')), pygame.image.load(Path('imgs', 'down2.png'))],
            'left': [pygame.image.load(Path('imgs', 'left1.png')), pygame.image.load(Path('imgs', 'left2.png'))],
            'right': [pygame.image.load(Path('imgs', 'right1.png')), pygame.image.load(Path('imgs', 'right2.png'))],
        }
        self.imagens_furia = { # Imagens em fúria
            'up': [pygame.image.load(Path('imgs', 'up_fury1.png')), pygame.image.load(Path('imgs', 'up_fury2.png'))],
            'down': [pygame.image.load(Path('imgs', 'down_fury1.png')), pygame.image.load(Path('imgs', 'down_fury2.png'))],
            'left': [pygame.image.load(Path('imgs', 'left_fury1.png')), pygame.image.load(Path('imgs', 'left_fury2.png'))],
            'right': [pygame.image.load(Path('imgs', 'right_fury1.png')), pygame.image.load(Path('imgs', 'right_fury2.png'))],

        }
        self.direcao_atual = 'right'
        self.frame_atual = 0
        self.timer_animacao = pygame.time.get_ticks()

    # Iniciar a fúria (quando coleta baiacu)
    def iniciar_furia(self):
        self.em_furia = True
        self.furia_timer = pygame.time.get_ticks()
    
    # Atualizar a fúria e voltar ao normal
    def atualizar_furia(self):
        if self.em_furia and (pygame.time.get_ticks() - self.furia_timer > self.furia_duracao):
            self.em_furia = False

    # Iniciar o aumento de velocidade (quando coleta peixe)
    def iniciar_velmaior(self):
        self.velmaior = True
        self.velmaior_timer = pygame.time.get_ticks()

    # Atualizar a velocidade e voltar ao normal
    def atualizar_velmaior(self):
        if self.velmaior and (pygame.time.get_ticks() - self.velmaior_timer > self.velmaior_duracao):
            self.velmaior = False

    # Movimentação do personagem
    def movimentacao(self):
        if self.em_furia or self.velmaior:
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
    
    # Atualizar animação do personagem
    def atualizar_animacao(self):
        intervalo_animacao = 100 if self.em_furia else 350
        if pygame.time.get_ticks() - self.timer_animacao > intervalo_animacao:  
            self.frame_atual = (self.frame_atual + 1) % len(self.imagens_furia[self.direcao_atual] if self.em_furia else self.imagens[self.direcao_atual])
            self.timer_animacao = pygame.time.get_ticks()
    
    # Mostrar o personagem na tela
    def renderizar(self):
        self.atualizar_animacao()
        imagens_atual = self.imagens_furia if self.em_furia else self.imagens
        imagem_atual = imagens_atual[self.direcao_atual][self.frame_atual]
        constantes.SCREEN.blit(imagem_atual, (int(self.posicao.x), int(self.posicao.y)))

    # Pegar a máscara do personagem para usar no mecanismo de colisão com as paredes
    def get_mask(self):
        surface = pygame.Surface((self.hit_box.width, self.hit_box.height), pygame.SRCALPHA)
        surface.fill((255, 255, 255))
        return pygame.mask.from_surface(surface)

    # Retornar a posição atual do personagem
    def retornar_posicao(self):
        return self.posicao
# -------------------------------------------------------------------------------------------------------------------------
