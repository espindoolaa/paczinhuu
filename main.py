import pygame
import random
import classe_italo
import constantes
import classe_tubaroes
import classe_bolinha_pequena
import classe_bolinha_grande
import labirinto
import coletavel_extra

pygame.init()

# Variáveis de contagem
contagem_bolinhas_grandes = 0
contagem_bolinhas_pequenas = 0
contagem_camarao = 0

font = pygame.font.Font('fontegamer.ttf', 36)
placa_image = pygame.image.load('placa.png')
placa_rect = placa_image.get_rect(topleft=(10, 10))  # Posição da placa na tela

# Inicialização do programa
posicao_inicial_italo = (517, 380)
posicao_inicial_tubarao1 = (517, 350)


size = (1086, 620)
pygame.display.set_caption('Paczinhuu')
clock = pygame.time.Clock()

running = True

italo = classe_italo.ItaloSena(posicao_inicial_italo)

# Posiciona as bolinhas grandes nos cantos
bolinhas_grandes = classe_bolinha_grande.Bolinha_grande([(71, 75), (1009, 75), (73, 540), (1006, 540)])

# Objeto das bolinhas pequenas
bolinhas_pequenas = classe_bolinha_pequena.Bolinha_pequena(71, 71, bolinhas_grandes, constantes.MAPA)

# Objeto do camarão
camarao = coletavel_extra.Coletavel_extra()

# Objeto dos tubarões (dois ao total)
tubarao1 = classe_tubaroes.Tubaroes(posicao_inicial_tubarao1)

# Loop do jogo
while running:

    # Loop eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Fundo da praia e as boias (labirinto)
    constantes.SCREEN.blit(constantes.PRAIA, (0, 0))
    constantes.SCREEN.blit(labirinto.labirinto_imagem, labirinto.labirinto_rect.topleft)

    # Renderizar o fundo da placa
    constantes.SCREEN.blit(placa_image, placa_rect)


    # Movimentação de Ítalo
    prev_pos = italo.posicao.xy
    italo.movimentacao()
    italo.atualizar_furia()
    new_position = italo.retornar_posicao()
    italo.renderizar()

    # --------- TUBARÃO ------------
    tubarao1.movimentacao(False, constantes.SIZE)
    if tubarao1.checar_colisao(italo):
        print("Colisão detectada!")
    
    tubarao1.renderizar(constantes.SCREEN)

    # ------------------------------
    # Bolinhas
    bolinhas_pequenas.renderizar(constantes.SCREEN)
    bolinhas_grandes.renderizar(constantes.SCREEN)

    bolinhas_pequenas.verificar_colisao(new_position)

    # Checa e remove bolinhas grandes coletadas
    italo_rect = pygame.Rect(italo.posicao[0], italo.posicao[1], 30, 30)
    if bolinhas_grandes.coleta_bolinha_grande(italo_rect):
        contagem_bolinhas_grandes += 1
        italo.iniciar_furia()

    # ----- CAMARÃO ------
    camarao.atualizar()

    if not camarao.vivo and not camarao.coletado:
        camarao.spawn()

    # Verificar se Ítalo coletou o camarão
    if camarao.verificar_coleta(italo.posicao):
        print("Camarão coletado!")
        contagem_camarao += 1

    # Renderizar o camarão se estiver ativo
    if camarao.vivo:
        camarao.renderizar(constantes.SCREEN)

    # ----------------------------------------

    # Renderizar o fundo da placa e as contagens na placa
    # constantes.SCREEN.blit(placa_image, placa_rect)
    texto_bolinhas_grandes = font.render(f'Bolinhas Grandes: {contagem_bolinhas_grandes}', True, (0, 0, 0))
    texto_bolinhas_pequenas = font.render(f'Bolinhas Pequenas: {bolinhas_pequenas.qtd_bolinhas}', True, (0, 0, 0))
    texto_camarao = font.render(f'Camarões: {contagem_camarao}', True, (0, 0, 0))
    constantes.SCREEN.blit(texto_bolinhas_grandes, (placa_rect.x + 10, placa_rect.y + 10))
    constantes.SCREEN.blit(texto_bolinhas_pequenas, (placa_rect.x + 10, placa_rect.y + 40))
    constantes.SCREEN.blit(texto_camarao, (placa_rect.x + 10, placa_rect.y + 70))

    pygame.display.flip()
    
    clock.tick(60)

pygame.quit()
