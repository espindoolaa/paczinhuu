import pygame
import random
VEL_NORMAL = 3
VEL_FURIA = 4
RAIO_BOLINHA_GRANDE = 10
RAIO_BOLINHA_PEQUENA = 5

mapa = [
    "#######################", 
    "#.#........#........#.#",  
    "#....###.#...#.###....#", 
    "####.#...##.##...#.####", 
    "---#.#.#.......#.#.#---", 
    "####.#.#.##x##.#.#.####",
    ".........#ggg#.#.......",
    "####.#.#.#####.#.#.####",
    "---#...#.......#...#---",
    "####.###.#####.###.####",
    "#....#...#.#.#.#.#....#",
    "#.#..#.#...#.....#..#.#",
    "#######################",
]

pygame.init()

# CLASSE ÍTALO
class ItaloSena:
    def __init__(self, posicao_inicial):
        self.posicao = pygame.Vector2(posicao_inicial)
    
        self.x_velocidade = 0
        self.y_velocidade = 0

        self.em_furia = False

        self.hit_box = pygame.Rect(self.posicao.x - 12 // 2, self.posicao.y - 12 // 2, 12, 12)
   
        self.labirinto = pygame.image.load('paredes.png')
        self.labirinto_rect = self.labirinto.get_rect()
        self.labirinto_mask = pygame.mask.from_surface(self.labirinto)
    
    def checar_colisao(self):
        #self.jogador_mask = pygame.mask.from_
        self.offset = (self.hit_box.x - self.labirinto_rect.x, self.hit_box.y - self.labirinto_rect.y)
        if self.labirinto_mask.overlap(self.jogador_mask, self.offset):
            return True
        return False
    
    def movimentacao(self):
        if pygame.key.get_pressed()[pygame.K_UP]:
            if self.em_furia:
                self.y_velocidade = -VEL_FURIA
            else:
                self.y_velocidade = -VEL_NORMAL
            self.x_velocidade = 0
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            if self.em_furia:
                self.y_velocidade = VEL_FURIA
            else:
                self.y_velocidade = VEL_NORMAL
            self.x_velocidade = 0
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            if self.em_furia:
                self.x_velocidade = -VEL_FURIA
            else:
                self.x_velocidade = -VEL_NORMAL
            self.y_velocidade = 0
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            if self.em_furia:
                self.x_velocidade = VEL_FURIA
            else:
                self.x_velocidade = VEL_NORMAL
            self.y_velocidade = 0

        self.posicao.x += self.x_velocidade
        self.posicao.y += self.y_velocidade

    def renderizar(self):
        # Desenha o personagem na tela como um quadrado amarelo
        pygame.draw.rect(screen, "yellow", (int(self.posicao.x), int(self.posicao.y), 45, 45))
    
    def colisao(self, lista):
        for parede in lista:
            if self.hit_box.colliderect(parede):
                if self.y_velocidade < 0 and self.x_velocidade == 0: 
                    self.y_italo += 14 
                elif self.y_velocidade > 0 and self.x_velocidade == 0: 
                    self.y_italo -= 1 
                elif self.x_velocidade < 0 and self.y_velocidade == 0: 
                    self.x_italo += 14 
                else:                                                 
                    self.x_italo -= 1

                self.x_velocidade = 0
                self.y_velocidade = 0
        
    def get_mask(self):
        return pygame.mask.from_surface((self.hit_box.width, self.hit_box.height), pygame.SRCALPHA)

    

# BOLINHA PEQUENA
class Bolinha_pequena:        
    def __init__(self, x, y, bolinhas_grandes, mapa):
        self.posicoes = []
        self.mapa = mapa
        self.gerar_posicoes(x, y, bolinhas_grandes)
    
    def gerar_posicoes(self, x_inicial, y_inicial, bolinhas_grandes):
        # Verifica se a posição é válida no mapa
        def posicao_valida(x, y):
            if 0 <= y // 47 < len(self.mapa) and 0 <= x // 47 < len(self.mapa[0]):
                mapa_y = y // 47
                mapa_x = x // 47
                return self.mapa[mapa_y][mapa_x] == '.'
            return False
        
        for x in range(x_inicial, 1068, 47):
            for y in range(y_inicial, 620, 47):
                if posicao_valida(x, y) and (x, y) not in bolinhas_grandes.posicoes:
                    self.posicoes.append((x, y))
    
    def renderizar(self, screen):
        for pos in self.posicoes:
            pygame.draw.circle(screen, (255, 255, 0), pos, RAIO_BOLINHA_PEQUENA)
    
    
# BOLINHA GRANDE
class Bolinha_grande:
    def __init__(self, posicoes):
        self.posicoes = posicoes
        
    def renderizar(self, screen):
        for pos in self.posicoes:
            pygame.draw.circle(screen, (255, 0, 0), pos, RAIO_BOLINHA_GRANDE)

# COLETÁVEL EXTRA

# Imagens
praia = pygame.image.load('praia.jpg')

# Inicialização do programa
posicao_inicial_italo = (500, 500)
size = (1086, 620)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Paczinhuu')
clock = pygame.time.Clock()



running = True

italo = ItaloSena(posicao_inicial_italo)

# Posiciona as bolinhas grandes nos cantos
bolinhas_grandes = Bolinha_grande([(71, 71), (1068, 71), (71, 620), (1068, 620)])

# Objeto das bolinhas pequenas
bolinhas_pequenas = Bolinha_pequena(71, 71, bolinhas_grandes, mapa)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.blit(praia, (0, 0))

    if not italo.checar_colisao():
        italo.movimentacao()
    italo.renderizar()

    bolinhas_pequenas.renderizar(screen)
    bolinhas_grandes.renderizar(screen)
    
    pygame.display.flip()
    
    clock.tick(60)
    
