import pygame
import random

class Tubaroes():
    def __init__(self, posicao_inicial, velocidade=130):
        self.posicao = pygame.Vector2(posicao_inicial) 
        self.velocidade = velocidade 
        self.tubarao_tigre = pygame.image.load("tubarao_tigre1.png")
        self.largura_tubarao, self.altura_tubarao = self.tubarao_tigre.get_size()
        self.tubarao_tigre = pygame.transform.scale(self.tubarao_tigre, ((1/14.978) * self.largura_tubarao, (1/8.404) * self.altura_tubarao))


    # IA reativa (para o desenvolvimento da movimentação reativa, precisarei da poisção do Italo_Sena)
    def movimentacao(self, furia): 
        # Movendo o tubarão aleatoriamente com a intenção de atacar 
        if furia:
            direction = random.choice(['up', 'down', 'left', 'right'])

            if direction == 'up':
                self.posicao.y -= self.velocidade
            elif direction == 'down':
                self.posicao.y += self.velocidade
            elif direction == 'left':
                self.posicao.x -= self.velocidade
            elif direction == 'right':
                self.posicao.x += self.velocidade

        # Movendo o tubarão aleatoriamente com a intenção de fugir (*por ora está igual ao de cima*).
        else:
            direction = random.choice(['up', 'down', 'left', 'right'])

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
        elif self.posicao.x + self.largura > screen.get_width():
            self.posicao.x = screen.get_width() - self.largura

        if self.posicao.y < 0:
            self.posicao.y = 0
        elif self.posicao.y + self.altura > screen.get_height():
            self.posicao.y = screen.get_height() - self.altura

    def acelerar_desacelerar(self, furia, velocidade):
        if furia == True: 
            self.velocidade = 120
        else:
            if velocidade < 154:
                self.velocidade = velocidade + 0.8
            else:
                self.velocidade = 154

    '''
    def colisao(self, furia):
        if furia == True and colisao_com_italo == True (ou seja, posição italo == positao tutuba, logo):
            self.posicao_inicial = (screen.get_width() / 2, screen.get_height() / 2)
            self.velocidade = 180
    '''

    def render(self, tela):
        tela.blit(self.tubarao_tigre, self.posicao)

            



# Configuração inicial do pygame
pygame.init()
screen = pygame.display.set_mode((1086, 620))
clock = pygame.time.Clock()
running = True
dt = 0
posicao_inicial = (screen.get_width() / 2, screen.get_height() / 2)

tubarao1 = Tubaroes(posicao_inicial, 3)


# looping infinito para rodar os tubarões
while running:
    # Captura eventos, como clicar no botão de fechar a janela
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running = False

    # Preenche a tela com uma cor para limpar o quadro anterior
    screen.fill("dark blue")

    # Realiza o movimento aleatório do tubarão
    tubarao1.movimentacao(furia=False)

    # Desenha o tubarão na interface
    tubarao1.render(screen)
    pygame.display.flip()

    # Controla o FPS e calcula o tempo delta.
    dt = clock.tick(60) / 1000

pygame.quit()