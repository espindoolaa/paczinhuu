import pygame
from pathlib import Path
from labirinto import checar_colisao
import random
import constantes

# Esse documento contém a classe dos tubarões

# Haverá dois tubarões no jogo, que derrotam o player caso este colida com algum deles

# Caso o player esteja em estado de fúria (após coletar um baiacu), o player mata o tubarão ao colidir com ele

coords = [
    (212, 71), (400, 71), (682, 71), (870, 71),
    (165, 118), (212, 118), (870, 118), (917, 118),
    (400, 165), (682, 165),
    (400, 212), (541, 212), (682, 212),
    (212, 306), (306, 306), (776, 306), (870, 306),
    (212, 400), (400, 400), (682, 400), (870, 400),
    (165, 494), (212, 494), (400, 494), (682, 494), (870, 494), (917, 494) 
]
dircoords = [
    'DLR', 'DLR', 'DLR', 'DLR',
    'ULR', 'UDL', 'UDR', 'ULR',
    'UDL', 'UDR',
    'UDR', 'ULR', 'UDL',
    'UDLR', 'UDL', 'UDR', 'UDLR',
    'UDR', 'UDR', 'UDL', 'UDL'
    'DLR', 'UDL', 'UDL', 'UDR', 'UDR', 'DLR'
]

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

    # Checar se o tubarão está num nódulo do labirinto
    def checar_nodulo(self):
        for p in range(len(coords)):
            if self.direcao_atual == 'L' or self.direcao_atual == 'R':
                centrox = self.hit_box.centerx
                coords_linha = []
                for y in (self.hit_box.midbottom[1], self.hit_box.midtop[1]):
                    coord = (centrox, y)
                    coords_linha.append(coord)

                if coords[p] in coords_linha:
                    return (1, x)
                return 0
            
            elif self.direcao_atual == 'U' or self.direcao_atual == 'D':
                centroy = self.hit_box.centery
                coords_linha = []
                for x in (self.hit_box.midleft[0], self.hit_box.midright[0]):
                    coord = (x, centroy)
                    coords_linha.append(coord)
                
            
                if coords[p] in coords_linha:
                    return (1, x)
                return 0

    # Movimentar o tubarão
    def movimentacao(self):
        direction_vectors = {
            'U': pygame.Vector2(0, -1),
            'D': pygame.Vector2(0, 1),
            'L': pygame.Vector2(-1, 0),
            'R': pygame.Vector2(1, 0)
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
                self.posicao += direction_vectors['U'] * self.velocidade
                self.hit_box.topleft = (self.posicao.x, self.posicao.y)
            else:
                self.nagaiola = False
                self.saindogaiola = False         
        
        else:
            new_position = self.posicao + direction_vectors[self.direcao_atual] * self.velocidade
            self.hit_box.topleft = (new_position.x, new_position.y)

            if checar_colisao(self):
                possible_directions = ['U', 'D', 'L', 'R']
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
                check = self.checar_nodulo()
                if check != 0:
                    x = check[1]
                    possible_directions = dircoords[x]
                    list_possible_directions = []
                    for k in possible_directions:
                        list_possible_directions.append(k)
                    random.shuffle(list_possible_directions)
                    for new_direction in list_possible_directions:
                        new_position = self.posicao + direction_vectors[new_direction] * self.velocidade
                        self.hit_box.topleft = (new_position.x, new_position.y)
                        if not checar_colisao(self):
                            self.direcao_atual = new_direction
                            self.posicao = new_position
                            break
                        
                else:
                    self.posicao = new_position
    
            if self.posicao.x < 0:
                self.posicao.x = constantes.SIZE[0]
            elif self.posicao.x > constantes.SIZE[0]:
                self.posicao.x = 0

            self.hit_box.topleft = (self.posicao.x, self.posicao.y)
        
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
# --------------------------------------------------------------------------------------------------------------------------------
