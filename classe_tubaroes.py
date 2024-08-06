import pygame
from pathlib import Path
import random

# Esse documento contém a classe do tubarão

# Haverá um tubarão no jogo, que derrota o player caso este colida com ele

# Caso o player esteja em estado de fúria (após coletar um baiacu), o player manda o tubarão para a gaiola após colidir com ele

# ---------------------------------------------------- CLASSE TUBARÕES --------------------------------------------------------
class Tubaroes():
    # Inicializações
    def __init__(self, posicao_inicial, velocidade=2):
        self.posicao = pygame.Vector2(posicao_inicial)
        self.velocidade = velocidade
        self.tubarao_tigre = pygame.image.load(Path('imgs', "tubarao_tigre1.png"))
        self.tubarao_x, self.tubarao_y = self.tubarao_tigre.get_size()
        self.tubarao_tigre = pygame.transform.scale(self.tubarao_tigre, ((1/14.978) * self.tubarao_x, (1/8.404) * self.tubarao_y))
        self.hit_box = pygame.Rect(self.posicao.x, self.posicao.y, float(self.tubarao_tigre.get_width()), float(self.tubarao_tigre.get_height()))
        self.tubarao_mask = pygame.mask.Mask((self.hit_box.width, self.hit_box.height))
        self.nagaiola = True
        self.saindogaiola = False
        self.posicaosaida = (520, 285)
        self.direcao_atual = random.choice(['U', 'D', 'L', 'R'])
        self.cond = False


    # Movimentar o tubarão
    def movimentacao(self):
        sentidos = {
            'U': pygame.Vector2(0, -1),
            'D': pygame.Vector2(0, 1),
            'L': pygame.Vector2(-1, 0),
            'R': pygame.Vector2(1, 0)
        }

        if self.posicao.x == 520 and 285 >= self.posicao.y > 101:
            self.posicao += sentidos['U'] * self.velocidade
            self.hit_box.topleft = (self.posicao.x, self.posicao.y)
        else:
            if 374 < self.posicao.x < 576 and self.posicao.y == 101:
                self.posicao += sentidos['R'] * self.velocidade
                self.hit_box.topleft = (self.posicao.x, self.posicao.y)
            else:
                if self.posicao.x == 576 and 118 >= self.posicao.y > 55:
                    self.posicao += sentidos['U'] * self.velocidade
                    self.hit_box.topleft = (self.posicao.x, self.posicao.y)
                else:
                    if 560 < self.posicao.x < 846 and self.posicao.y == 55:
                        self.posicao += sentidos['R'] * self.velocidade
                        self.hit_box.topleft = (self.posicao.x, self.posicao.y)
                    else:
                        if self.posicao.x == 846 and self.posicao.y < 385:
                            self.posicao += sentidos['D'] * self.velocidade
                            self.hit_box.topleft = (self.posicao.x, self.posicao.y)
                        else:
                            if self.posicao.x > 740 and self.posicao.y == 385:
                                self.posicao += sentidos['L'] * self.velocidade
                                self.hit_box.topleft = (self.posicao.x, self.posicao.y)
                            else:
                                if self.posicao.x == 740 and self.posicao.y > 155:
                                    self.posicao += sentidos['U'] * self.velocidade
                                    self.hit_box.topleft = (self.posicao.x, self.posicao.y)
                                else:
                                    if self.posicao.x > 654 and self.posicao.y == 155:
                                        self.posicao += sentidos['L'] * self.velocidade
                                        self.hit_box.topleft = (self.posicao.x, self.posicao.y)
                                    else:
                                        if self.posicao.x == 654 and self.posicao.y < 375:
                                            self.posicao += sentidos['D'] * self.velocidade
                                            self.hit_box.topleft = (self.posicao.x, self.posicao.y)
                                        else: 
                                            if self.posicao.x > 374 and self.posicao.y == 375:
                                                self.posicao += sentidos['L'] * self.velocidade
                                                self.hit_box.topleft = (self.posicao.x, self.posicao.y)
                                            else:
                                                if self.posicao.x == 374 and self.posicao.y > 55 and self.cond == False: 
                                                    self.posicao += sentidos['U'] * self.velocidade
                                                    self.hit_box.topleft = (self.posicao.x, self.posicao.y)
                                                else:
                                                    self.cond = True
                                                    if self.posicao.x > 190 and self.posicao.y == 55:
                                                        self.posicao += sentidos['L'] * self.velocidade
                                                        self.hit_box.topleft = (self.posicao.x, self.posicao.y)
                                                    else:
                                                        if self.posicao.x == 190 and self.posicao.y < 385:
                                                            self.posicao += sentidos['D'] * self.velocidade
                                                            self.hit_box.topleft = (self.posicao.x, self.posicao.y)
                                                        else:
                                                            if self.posicao.x < 296 and self.posicao.y == 385:
                                                                self.posicao += sentidos['R'] * self.velocidade
                                                                self.hit_box.topleft = (self.posicao.x, self.posicao.y)
                                                            else:
                                                                if self.posicao.x == 296 and self.posicao.y > 155:
                                                                    self.posicao += sentidos['U'] * self.velocidade
                                                                    self.hit_box.topleft = (self.posicao.x, self.posicao.y)
                                                                else:
                                                                    if self.posicao.x < 370 and self.posicao.y == 155:
                                                                        self.posicao += sentidos['R'] * self.velocidade
                                                                        self.hit_box.topleft = (self.posicao.x, self.posicao.y)
                                                                    else:
                                                                        if self.posicao.x == 370 and self.posicao.y < 185:
                                                                            self.posicao += sentidos['D'] * self.velocidade
                                                                            self.hit_box.topleft = (self.posicao.x, self.posicao.y)      
                                                                        else:
                                                                            if self.posicao.x < 520 and self.posicao.y == 185 and self.cond == True:
                                                                                self.posicao += sentidos['R'] * self.velocidade
                                                                                self.hit_box.topleft = (self.posicao.x, self.posicao.y)
                                                                            else:
                                                                                self.cond = False
                                                                    
                                                        



    # Verificar aceleração
    def acelerar_desacelerar(self, furia, velocidade):
        if furia:
            self.velocidade = 2
        else:
            if velocidade < 4:
                self.velocidade = velocidade + 0.2
            else:
                self.velocidade = 4

    # Mostrar tubarão na tela
    def renderizar(self, tela):
        tela.blit(self.tubarao_tigre, self.posicao)

    # Pegar a máscara do tubarão
    def get_mask(self):
        return pygame.mask.from_surface(self.tubarao_tigre)

    # Checar se o player colidiu com o tubarão
    def checar_colisao_complayer(self, italo):
        offset = (int(italo.posicao.x - self.posicao[0]), int(italo.posicao.y - self.posicao[1]))
        return self.get_mask().overlap(italo.get_mask(), offset) is not None
    
    def resetar_posicao(self):
        self.posicao = pygame.Vector2(self.posicaosaida)
        self.hit_box.topleft = self.posicao
        self.nagaiola = True
        self.saindogaiola = False
        self.direcao_atual = random.choice(['U', 'D', 'L', 'R'])
        self.movimentacao()

# --------------------------------------------------------------------------------------------------------------------------------
