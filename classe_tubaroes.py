import pygame
from pathlib import Path
from labirinto import checar_colisao
import random

# Esse documento contém a classe dos tubarões

# Haverá dois tubarões no jogo, que derrotam o player caso este colida com algum deles

# Caso o player esteja em estado de fúria (após coletar um baiacu), o player mata o tubarão ao colidir com ele

# ---------------------------------------------------- CLASSE TUBARÕES --------------------------------------------------------
class Tubaroes():
    def __init__(self, posicao_inicial, velocidade=2):
        self.posicao = pygame.Vector2(posicao_inicial)
        self.velocidade = velocidade
        self.tubarao_tigre = pygame.image.load(Path('imgs', "tubarao_tigre1.png"))
        self.tubarao_x, self.tubarao_y = self.tubarao_tigre.get_size()
        self.tubarao_tigre = pygame.transform.scale(self.tubarao_tigre, ((1/14.978) * self.tubarao_x, (1/8.404) * self.tubarao_y))
        self.hit_box = pygame.Rect(self.posicao.x, self.posicao.y, self.tubarao_tigre.get_width(), self.tubarao_tigre.get_height())
        self.tubarao_mask = pygame.mask.Mask((self.hit_box.width, self.hit_box.height))
        self.nagaiola = True
        self.saindogaiola = False
        self.posicaosaida = (520, 285)
        self.direcao_atual = random.choice(['up', 'down', 'left', 'right'])

    def movimentacao(self, furia):
        direction_vectors = {
            'up': pygame.Vector2(0, -1),
            'down': pygame.Vector2(0, 1),
            'left': pygame.Vector2(-1, 0),
            'right': pygame.Vector2(1, 0)
        }

        if self.nagaiola and not self.saindogaiola:
            if self.posicao.distance_to(self.posicaosaida) < self.velocidade:
                self.posicao = self.posicaosaida
                self.saindogaiola = True
            else:
                direction = (self.posicaosaida - self.posicao).normalize()
                self.posicao += direction * self.velocidade
                self.hit_box.topleft = (self.posicao.x, self.posicao.y)

        elif self.nagaiola and self.saindogaiola:
            if not checar_colisao(self):
                self.posicao += direction_vectors['up'] * self.velocidade
                self.hit_box.topleft = (self.posicao.x, self.posicao.y)
            else:
                self.nagaiola = False
                self.saindogaiola = False         
        
        else:
            new_position = self.posicao + direction_vectors[self.direcao_atual] * self.velocidade
            self.hit_box.topleft = (new_position.x, new_position.y)

            if checar_colisao(self):
                possible_directions = ['up', 'down', 'left', 'right']
                possible_directions.remove(self.direcao_atual)
                random.shuffle(possible_directions)
                for new_direction in possible_directions:
                    new_position = self.posicao + direction_vectors[new_direction] * self.velocidade
                    self.hit_box.topleft = (new_position.x, new_position.y)
                    if not checar_colisao(self):
                        self.direcao_atual = new_direction
                        self.posicao = new_position
                        break
            else:
                self.posicao = new_position

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

    def checar_colisao_complayer(self, italo):
        offset = (int(italo.posicao.x - self.posicao[0]), int(italo.posicao.y - self.posicao[1]))
        return self.get_mask().overlap(italo.get_mask(), offset) is not None
# --------------------------------------------------------------------------------------------------------------------------------
