import pygame
from pathlib import Path
from labirinto import checar_colisao

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

    def movimentacao(self, furia):
        ...
        
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
        offset = (int(italo.posicao.x - self.posicao.x), int(italo.posicao.y - self.posicao.y))
        return self.get_mask().overlap(italo.get_mask(), offset) is not None
# --------------------------------------------------------------------------------------------------------------------------------
