import pygame
import constantes

class Botao:
    def __init__(self, imagem, texto, centrox, centroy):
        self.imagem = imagem
        self.texto = texto
        self.centrox = centrox
        self.centroy = centroy

    def desenhar(self):
        constantes.SCREEN.blit(self)

    def clique(self):
        if 'clicou':
            return True

    def passar_por_cima(self):
        if 'passou':
            return True
