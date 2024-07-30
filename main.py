import pygame
from sys import exit
from pygame.locals import *
import constantes

class Italo: # classe Italo que vai conter caracteristicas e métodos do player

    def __init__(self):
        self.raio = constantes.RAIO # tamanho do circulo
        self.x_italo = constantes.CORDENADA_italo_x # cordenada inicial x
        self.y_italo = constantes.CORDENADA_italo_Y # cordenada inicial y
        self.x_velocidade = 0 # velocidade inical x (não mexer) / também é usado para deslocar o italo indefinadamente na posição horizontal
        self.y_velocidade = 0 # velocidade inical y (não mexer) / também é usado para deslocar o italo indefinadamente na posição horizontal
        self.hit_box = pygame.Rect(self.x_italo - self.raio // 2, self.y_italo - self.raio // 2, self.raio, self.raio) # rit box do italo, define um retangulo que nao aparece na tela que vai verificar se existe colisão

    def movimentacao(self, event): # metodo responsavel receber os comandos do teclado e definir a direção (esquerda,direita,cima,baixo)

        if event.type == KEYDOWN:
            if event.key == K_w:
                self.y_velocidade = -constantes.VELOCIDADE_ITALO
                self.x_velocidade = 0
            if event.key == K_s:
                self.y_velocidade = constantes.VELOCIDADE_ITALO
                self.x_velocidade = 0
            if event.key == K_a:
                self.y_velocidade = 0
                self.x_velocidade = -constantes.VELOCIDADE_ITALO
            if event.key == K_d:
                self.y_velocidade = 0
                self.x_velocidade = constantes.VELOCIDADE_ITALO     

    def desenhar_italo(self): # desenha o italo andando e as paredes
        
        self.x_italo += self.x_velocidade # adiciona a posição de italo horizontal a velocidade para ele "andar"
        self.y_italo += self.y_velocidade # adiciona a posição de italo vertical a velocidade para ele "andar" 

        # parte responsável por jogar o player do outro lado da tela quando ele atravessa as bordas
        if self.x_italo < 0:
            self.x_italo = constantes.LARGURA
        elif self.x_italo > constantes.LARGURA:
            self.x_italo = 0

        if self.y_italo < 0:
            self.y_italo = constantes.ALTURA
        elif self.y_italo > constantes.ALTURA:
            self.y_italo = 0

        self.hit_box.topleft = (self.x_italo, self.y_italo) # atualiza a hit_box // é preciso para a hit_box "andar junto do player" e poder verificar a colisão

        pygame.draw.circle(tela, constantes.AMARELO, (italo_sena.x_italo, italo_sena.y_italo), constantes.RAIO) # desenha o italo
        for parede in constantes.lista_paredes: # desenha todas as paredes dentro da lista de constantes
            pygame.draw.rect(tela, constantes.VERDE_CLARO, parede)
    
    def colisão(self):
        for parede in constantes.lista_paredes: # para cada parede na lista de paredes em constantes vai verificar se bateu
            if italo_sena.hit_box.colliderect(parede):
                
                if self.y_velocidade < 0 and self.x_velocidade == 0: # colisão por baixo
                    self.y_italo += 14 # quantos blocos afasta ao bater
                elif self.y_velocidade > 0 and self.x_velocidade == 0: # colisão por cima
                    self.y_italo -= 1 # quantos blocos afasta ao bater
                elif self.x_velocidade < 0 and self.y_velocidade == 0: # colisão pela direita
                    self.x_italo += 14 # quantos blocos afasta ao bater
                else:                                                  # colisão pela esquerda
                    self.x_italo -= 1 # quantos blocos afasta ao bater

                self.x_velocidade = 0
                self.y_velocidade = 0

tela = pygame.display.set_mode((constantes.LARGURA, constantes.ALTURA))
italo_sena = Italo()

pygame.init()
jogo_rodando = True
while jogo_rodando:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        italo_sena.movimentacao(event)

    tela.fill(constantes.PRETO)
    italo_sena.colisão()
    italo_sena.desenhar_italo()
    pygame.display.update()