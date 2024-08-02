import pygame
import sys
import classe_italo
import constantes
import classe_tubaroes
import classe_bolinha_pequena
import classe_bolinha_grande
import labirinto
import coletavel_extra
from pathlib import Path
pygame.init()

def tela_vitoria():
    screen = pygame.display.set_mode((1075, 614))
    imagemfundo_vitoria = pygame.image.load(Path('imgs', 'vitoria.png'))
    
    while True:
        screen.blit(imagemfundo_vitoria, (0, 0))
        pygame.display.set_caption('Paczinhuu - VITÓRIA!')

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

# def tela_pause():
    

def rodar_jogo():

    # Variáveis de contagem
    contagem_bolinhas_grandes = 0
    contagem_camarao = 0

    placa_image = pygame.image.load(Path('imgs', 'placa.png'))  # Carrega a imagem da placa

    # Fonte
    font = pygame.font.Font('fontegamer.ttf', 25)  # Fonte padrão do Pygame com tamanho 36

    # Definição das posições das placas
    placa_rect1 = placa_image.get_rect(topleft=(10, 10))
    placa_rect2 = placa_image.get_rect(topleft=(placa_rect1.right + 10, 10))
    placa_rect3 = placa_image.get_rect(topleft=(placa_rect2.right + 10, 10))

    # Inicialização do programa
    posicao_inicial_italo = (517, 380)
    posicao_inicial_tubarao1 = (517, 350)

    size = (1086, 620)
    pygame.display.set_mode(size)
    pygame.display.set_caption('Paczinhuu')
    clock = pygame.time.Clock()

    running = True

    italo = classe_italo.ItaloSena(posicao_inicial_italo)

    # Posiciona as bolinhas grandes nos cantos
    bolinhas_grandes = classe_bolinha_grande.Bolinha_grande([(60, 75), (995, 70), (60, 540), (995, 540)])

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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = True
        
        
        # Fundo da praia e as boias (labirinto)
        constantes.SCREEN.blit(constantes.PRAIA, (0, 0))
        constantes.SCREEN.blit(labirinto.labirinto_imagem, (0,0))

        # Movimentação de Ítalo
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
        
        # ---------- BOLINHAS -----------------------------------------------
        bolinhas_pequenas.renderizar(constantes.SCREEN)
        bolinhas_grandes.renderizar(constantes.SCREEN)

        bolinhas_pequenas.verificar_colisao(new_position)

        italo_rect = pygame.Rect(italo.posicao[0], italo.posicao[1], 30, 30)
        if bolinhas_grandes.coleta_bolinha_grande(italo_rect):
            contagem_bolinhas_grandes += 1
            italo.iniciar_furia()

        # --------------------------------------------------------------------

        # ----------------- CAMARÃO -------------------
        camarao.atualizar()

        if camarao.vivo:
            camarao.spawn()
            camarao.renderizar(constantes.SCREEN)
        

        # Verificar se Ítalo coletou o camarão
        if camarao.verificar_coleta(italo.posicao):
            print("Camarão coletado!")
            contagem_camarao += 1
            camarao.coletado = True
        
        # ----------------------------------------------

        # --------------------------------------------- PLACAS -------------------------------------------------
        # Renderizar as placas
        constantes.SCREEN.blit(placa_image, placa_rect1)
        constantes.SCREEN.blit(placa_image, placa_rect2)
        constantes.SCREEN.blit(placa_image, placa_rect3)

        # Renderizar as contagens dentro das placas
        texto_bolinhas_grandes = font.render(f'Bolinhas Grandes: {contagem_bolinhas_grandes}', True, (0, 0, 0))
        texto_bolinhas_pequenas = font.render(f'Bolinhas Pequenas: {bolinhas_pequenas.qtd_bolinhas}', True, (0, 0, 0))
        texto_camarao = font.render(f'Camarões: {contagem_camarao}', True, (0, 0, 0))

        # Posicionar os textos dentro das placas
        text_rect1 = texto_bolinhas_grandes.get_rect(center=(placa_rect1.centerx, placa_rect1.centery))
        text_rect2 = texto_bolinhas_pequenas.get_rect(center=(placa_rect2.centerx, placa_rect2.centery))
        text_rect3 = texto_camarao.get_rect(center=(placa_rect3.centerx, placa_rect3.centery))

        constantes.SCREEN.blit(texto_bolinhas_grandes, text_rect1)
        constantes.SCREEN.blit(texto_bolinhas_pequenas, text_rect2)
        constantes.SCREEN.blit(texto_camarao, text_rect3)

        # ---------------------------------------------------------------------------------------------------------

        if classe_bolinha_pequena.Bolinha_pequena.verificar_pegoutodaspequenas(bolinhas_pequenas) and classe_bolinha_grande.Bolinha_grande.verificar_pegoutodasgrandes(bolinhas_grandes, contagem_bolinhas_grandes):
            tela_vitoria()
        pygame.display.flip()
        
        clock.tick(60)

    pygame.quit()
    sys.exit()
