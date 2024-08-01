import pygame
import random

class Tubaroes():
    def __init__(self, posicao_inicial, velocidade=2):
        self.posicao = pygame.Vector2(posicao_inicial)
        self.velocidade = velocidade
        self.tubarao_tigre = pygame.image.load("tubarao_tigre1.png")
        self.tubarao_x, self.tubarao_y = self.tubarao_tigre.get_size()
        self.tubarao_tigre = pygame.transform.scale(self.tubarao_tigre, ((1/14.978) * self.tubarao_x, (1/8.404) * self.tubarao_y))
        self.hit_box = pygame.Rect(self.posicao.x, self.posicao.y, self.tubarao_tigre.get_width(), self.tubarao_tigre.get_height())
        self.tubarao_mask = pygame.mask.Mask((self.hit_box.width, self.hit_box.height))

    def movimentacao(self, furia, screen):
        # Movendo o tubarão aleatoriamente com a intenção de atacar ou fugir
        direction = random.choice(['up', 'down', 'left', 'right'])
        if furia:
            if direction == 'up':
                self.posicao.y -= self.velocidade
            elif direction == 'down':
                self.posicao.y += self.velocidade
            elif direction == 'left':
                self.posicao.x -= self.velocidade
            elif direction == 'right':
                self.posicao.x += self.velocidade

        else:
            if direction == 'up':
                self.posicao.y -= self.velocidade
            elif direction == 'down':
                self.posicao.y += self.velocidade
            elif direction == 'left':
                self.posicao.x -= self.velocidade
            elif direction == 'right':
                self.posicao.x += self.velocidade


        # Limites de tela que depois serão substituídos pelos limites das boias.
        if self.posicao.x < 0:
            self.posicao.x = 0
        elif self.posicao.x + self.tubarao_x > screen[0]:
            self.posicao.x = screen[0] - self.tubarao_x

        if self.posicao.y < 0:
            self.posicao.y = 0
        elif self.posicao.y + self.tubarao_y > screen[1]:
            self.posicao.y = screen[1] - self.tubarao_y

        self.hit_box.topleft = (self.posicao.x, self.posicao.y)

    def acelerar_desacelerar(self, furia, velocidade):
        if furia:
            self.velocidade = 2
        else:
            if velocidade < 4:
                self.velocidade = velocidade + 0.2
            else:
                self.velocidade = 4

    def renderizar(self, tela):
        tela.blit(self.tubarao_tigre, self.posicao)

    def get_mask(self):
        return pygame.mask.from_surface(self.tubarao_tigre)

    def checar_colisao(self, italo):
        offset = (int(italo.posicao.x - self.posicao.x), int(italo.posicao.y - self.posicao.y))
        return self.get_mask().overlap(italo.get_mask(), offset) is not None
