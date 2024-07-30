import pygame

# Classe ItaloSena para o personagem controlável
class ItaloSena:
    def __init__(self, posicao_inicial, tamanho=47, velocidade_normal=200, velocidade_furia=300):
        self.posicao = pygame.Vector2(posicao_inicial)  # Posição inicial do personagem
        self.tamanho = tamanho  # Tamanho do quadrado que representa o personagem
        self.velocidade_normal = velocidade_normal  # Velocidade normal de movimento
        self.velocidade_furia = velocidade_furia  # Velocidade de movimento em fúria
        self.velocidade = self.velocidade_normal  # Velocidade atual
        self.em_furia = False  # Estado inicial de fúria
    
    def mover(self, direcao, dt):
        # Movimenta Ítalo com base na direção e no tempo
        if direcao == 'cima':
            self.posicao.y -= self.velocidade * dt
        elif direcao == 'baixo':
            self.posicao.y += self.velocidade * dt
        elif direcao == 'esquerda':
            self.posicao.x -= self.velocidade * dt
        elif direcao == 'direita':
            self.posicao.x += self.velocidade * dt
    
    def renderizar(self, tela):
        # Desenha o personagem na tela como um quadrado amarelo
        pygame.draw.rect(tela, "yellow", (int(self.posicao.x), int(self.posicao.y), self.tamanho, self.tamanho))
    
    def ativar_furia(self):
        # Ativa o estado de fúria e altera a velocidade
        self.em_furia = True
        self.velocidade = self.velocidade_furia
    
    def desativar_furia(self):
        # Desativa o estado de fúria e retorna à velocidade normal
        self.em_furia = False
        self.velocidade = self.velocidade_normal
    
    def verificar_coleta(self, item):
        # item será um objeto de uma classe de coletáveis
        # item.posicao e item.tamanho devem ser atributos dos objetos coletáveis
        distancia = self.posicao.distance_to(item.posicao)
        if distancia < self.tamanho + item.tamanho:
            if item.tipo == 'bolinha_maior':  # Tipo de item a ser definido na classe de coletáveis
                self.ativar_furia()
            # Lógica adicional para outros tipos de itens
            return True
        return False

# Configuração inicial do pygame
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

# Instancia o personagem Ítalo Sena no centro da tela
italo = ItaloSena(posicao_inicial=(screen.get_width() / 2, screen.get_height() / 2))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 128))  # Fundo azul escuro

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        italo.mover('cima', dt)
    if keys[pygame.K_DOWN]:
        italo.mover('baixo', dt)
    if keys[pygame.K_LEFT]:
        italo.mover('esquerda', dt)
    if keys[pygame.K_RIGHT]:
        italo.mover('direita', dt)

    # Aqui a verificação de coleta seria chamada quando os itens estiverem implementados
    # Exemplo (comentado, pois item não está definido):
    # for item in lista_de_itens:
    #     if italo.verificar_coleta(item):
    #         # marcar item como coletado

    # Renderiza o personagem Ítalo na tela
    italo.renderizar(screen)

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
