import pygame

# Pensei em fazer as paredes com várias boias em pixel art alinhadas (tipo a foto que mandei no discord, mas dps a gt pensa nisso melhor)

# Esse código, no caso, só mostra a boia na tela conforme a coordenada dada. Ainda não tem o mecanismo das colisões
class Paredes():
    def __init__(self, x, y, tela):
        self.boia = pygame.image.load("boiaquadrada.png")
        self.boia_size = self.boia.get_size()
        self.boia = pygame.transform.scale(self.boia, (1/10 * self.boia_size[0], 1/10 * self.boia_size[1]))
        self.boia_x = x
        self.boia_y = y
        self.coord = (x, y)        
        
    def desenhar_parede(self, tela):
        tela.blit(self.boia, self.coord)
