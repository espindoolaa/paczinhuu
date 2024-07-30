import pygame
# dimençoes da tela
LARGURA = 1086
ALTURA = 620

# cores
PRETO = (0,0,0)
AMARELO = (255,255,0)
AZUL = (0,0,255)
VERDE_CLARO = (0,130,130)

# valores para o pacman (ítalo)
RAIO = 12 # aumente/diminui o tamanho da circulo
VELOCIDADE_ITALO = 0.2 # aumente/diminui a velocidade que anda no mapa
CORDENADA_italo_x,CORDENADA_italo_Y = LARGURA//2, ALTURA//2

# paredes do mapa // para adicionar uma parede ao jogo basta colocar dentro da lista uma tupla com EIXO X, EIXO Y, LARGURA E ALTURA
lista_paredes = [
    pygame.Rect(800,100,80,100),
    pygame.Rect(200,200,80,100)
]