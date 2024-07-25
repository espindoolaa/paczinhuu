import pygame

# Classe do Ítalo Sena
class ItaloSena:
    def __init__(self, posicao_inicial, tamanho=20, velocidade=200):
        # Posição inicial do personagem
        self.posicao = pygame.Vector2(posicao_inicial)
        # Tamanho do círculo que representa o personagem
        self.tamanho = tamanho
        # Velocidade do movimento em pixels por segundo
        self.velocidade = velocidade
    
    def mover(self, direcao, dt):

        # Muda a posição do personagem com base na direção e no tempo
        if direcao == 'cima':
            self.posicao.y -= self.velocidade * dt
        elif direcao == 'baixo':
            self.posicao.y += self.velocidade * dt
        elif direcao == 'esquerda':
            self.posicao.x -= self.velocidade * dt
        elif direcao == 'direita':
            self.posicao.x += self.velocidade * dt
    
    def renderizar(self, tela):
        # Desenha o personagem na tela como um círculo amarelo ("pac-man")
        pygame.draw.circle(tela, "yellow", (int(self.posicao.x), int(self.posicao.y)), self.tamanho)

# Configuração inicial do pygame
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

# Instancia o personagem Ítalo Sena no centro da tela
italo = ItaloSena(posicao_inicial=(screen.get_width() / 2, screen.get_height() / 2))

while running:
    # Captura eventos, como clicar no botão de fechar a janela
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Preenche a tela com uma cor para limpar o quadro anterior
    screen.fill("dark blue")

    # Processa a entrada do usuário para mover o Ítalo
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        italo.mover('cima', dt)
    if keys[pygame.K_DOWN]:
        italo.mover('baixo', dt)
    if keys[pygame.K_LEFT]:
        italo.mover('esquerda', dt)
    if keys[pygame.K_RIGHT]:
        italo.mover('direita', dt)

    # Renderiza o personagem Ítalo na tela
    italo.renderizar(screen)

    # Atualiza o display com o que foi desenhado
    pygame.display.flip()

    # Controla o FPS e calcula o tempo delta
    dt = clock.tick(60) / 1000

pygame.quit()