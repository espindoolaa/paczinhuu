import pygame
import random
import classe_italo
import constantes
import classe_bolinha_pequena
import classe_bolinha_grande
import labirinto

pygame.init()


# Inicialização do programa
posicao_inicial_italo = (517, 375)
size = (1086, 620)
pygame.display.set_caption('Paczinhuu')
clock = pygame.time.Clock()

running = True

italo = classe_italo.ItaloSena(posicao_inicial_italo)

# Posiciona as bolinhas grandes nos cantos
bolinhas_grandes = classe_bolinha_grande.Bolinha_grande([(71, 75), (1009, 75), (73, 540), (1006, 540)])

# Objeto das bolinhas pequenas
bolinhas_pequenas = classe_bolinha_pequena.Bolinha_pequena(71, 71, bolinhas_grandes, constantes.MAPA, italo)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    constantes.SCREEN.blit(constantes.PRAIA, (0, 0))
    constantes.SCREEN.blit(labirinto.labirinto_imagem, labirinto.labirinto_rect.topleft)

    prev_pos = italo.posicao.xy

    italo.movimentacao()
        
    italo.renderizar()


    bolinhas_pequenas.renderizar(constantes.SCREEN)
    bolinhas_grandes.renderizar(constantes.SCREEN)

    # Checa e remove bolinhas grandes coletadas
    italo_rect = pygame.Rect(italo.posicao[0], italo.posicao[1], 38, 38)
    bolinhas_grandes.coleta_bolinha_grande(italo_rect)
    
    pygame.display.flip()
    
    clock.tick(60)

pygame.quit()
