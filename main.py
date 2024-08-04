import pygame
import sys
import classe_italo
import constantes
import classe_tubaroes
import classe_bolinha
import classe_peixe
import labirinto
import classe_baiacu
import botoes
from pathlib import Path
pygame.init()

# Esse documento contém a função do loop principal do jogo

# ---------------------- CURSOR -------------------------------
imagem_cursor = pygame.image.load(Path('imgs', 'cursor_click.png'))
imagem_cursor = pygame.transform.scale_by(imagem_cursor, 1/2)
cursor_superficie = pygame.Surface(imagem_cursor.get_size(), pygame.SRCALPHA)
cursor_superficie.blit(imagem_cursor, (0, 0))
cursor_click = pygame.cursors.Cursor((0, 0), cursor_superficie)
cursor_padrao = pygame.SYSTEM_CURSOR_ARROW
# --------------------------------------------------------------


# ------------------------------------- VITÓRIA -----------------------------------------
def tela_vitoria():
    # Inicialização
    screen_vit = pygame.display.set_mode((1075, 614))
    imagemfundo_vitoria = pygame.image.load(Path('imgs', 'vitoria.png'))

    # Botões da tela de vitória
    botoes_vitoria = []
    botao_reiniciar = botoes.Botoes(constantes.BOTAO, 'REINICIAR', (393, 400))
    botao_sair = botoes.Botoes(constantes.BOTAO, 'SAIR', (693, 400))
    botoes_vitoria.append(botao_reiniciar)
    botoes_vitoria.append(botao_sair)
    
    # Loop da tela de vitória
    while True:
        screen_vit.blit(imagemfundo_vitoria, (0, 0))
        pygame.display.set_caption('Paczinhuu - VITÓRIA!')
        for botao in botoes_vitoria:
            botoes.Botoes.verificar_hoover(botao, cursor_click, cursor_padrao)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                for botao in botoes_vitoria:
                    clicou = botoes.Botoes.verificar_clique(botao, constantes.SCREEN)
                    if clicou == True:
                        if botao == botao_reiniciar:
                            rodar_jogo()
                        if botao == botao_sair:
                            pygame.quit()
                            sys.exit()

        pygame.display.update()
# ---------------------------------------------------------------------------------------

# ------------------------------ GAME OVER -----------------------------------
def tela_gameover():
    screen = pygame.display.set_mode((1075, 614))
    imagemfundo_gameover = pygame.image.load(Path('imgs', 'gameover.png'))

    # Botões da tela de game over
    botoes_gameover = []
    botao_reiniciar = botoes.Botoes(constantes.BOTAO, 'REINICIAR', (393, 400))
    botao_sair = botoes.Botoes(constantes.BOTAO, 'SAIR', (693, 400))
    botoes_gameover.append(botao_reiniciar)
    botoes_gameover.append(botao_sair)
    
    # Loop da tela de game over
    while True:
        screen.blit(imagemfundo_gameover, (0, 0))
        pygame.display.set_caption('Paczinhuu - GAME OVER!')
        for botao in botoes_gameover:
            botoes.Botoes.verificar_hoover(botao, cursor_click, cursor_padrao)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                for botao in botoes_gameover:
                    clicou = botoes.Botoes.verificar_clique(botao, constantes.SCREEN)
                    if clicou == True:
                        if botao == botao_reiniciar:
                            rodar_jogo()
                        if botao == botao_sair:
                            pygame.quit()
                            sys.exit()

        pygame.display.update()
# ----------------------------------------------------------------------------

# ------------------------------------------- LOOP DO JOGO --------------------------------------------
def rodar_jogo():
    # Inicialização
    screen = pygame.display.set_mode(constantes.SIZE)
    pygame.display.set_caption('Paczinhuu')
    font = pygame.font.Font('fontegamer.ttf', 25)
    posicao_inicial_italo = (517, 380)
    posicao_inicial_tubarao1 = (480, 280)
    clock = pygame.time.Clock()
    running = True
    italo = classe_italo.ItaloSena(posicao_inicial_italo)
    lista_directions = ['up', 'down', 'left', 'right']

    # Variáveis de contagem
    contagem_peixes = 0
    contagem_baiacus = 0

    # Definição das posições das placas
    placa_image = pygame.image.load(Path('imgs', 'placa.png'))
    placa_rect1 = placa_image.get_rect(topleft=(10, 10))
    placa_rect2 = placa_image.get_rect(topleft=(placa_rect1.right + 10, 10))
    placa_rect3 = placa_image.get_rect(topleft=(placa_rect2.right + 10, 10))

    # Posicionar os coletáveis
    peixes = classe_peixe.Coletavel_peixe([(60, 75), (995, 540)])
    bolinhas = classe_bolinha.Bolinha(71, 71, peixes, constantes.MAPA)
    baiacus = classe_baiacu.Coletavel_baiacu([(987, 60), (53, 530)])

    # Objeto dos tubarões (dois ao total)
    tubarao1 = classe_tubaroes.Tubaroes(posicao_inicial_tubarao1)
    
    # Loop principal do jogo
    while running:
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(constantes.PRAIA, (0, 0))
        screen.blit(labirinto.labirinto_imagem, (0,0))

        italo.movimentacao()
        italo.atualizar_furia()
        italo.atualizar_velmaior()
        new_position = italo.retornar_posicao()
        italo.renderizar()

        tubarao1.movimentacao(italo.em_furia)
        if tubarao1.checar_colisao_complayer(italo):
            tela_gameover()
        tubarao1.renderizar(screen)
        
        bolinhas.renderizar(screen)
        peixes.renderizar(screen)
        baiacus.renderizar(screen)

        bolinhas.verificar_colisao(new_position)

        italo_rect = pygame.Rect(italo.posicao[0], italo.posicao[1], 30, 30)
        
        if peixes.coleta_peixe(italo_rect):
            contagem_peixes += 1
            italo.iniciar_velmaior()
        
        if baiacus.coleta_baiacu(italo_rect):
            contagem_baiacus += 1
            italo.iniciar_furia()
        
        # Renderizar as placas
        constantes.SCREEN.blit(placa_image, placa_rect1)
        constantes.SCREEN.blit(placa_image, placa_rect2)
        constantes.SCREEN.blit(placa_image, placa_rect3)

        # Renderizar as contagens dentro das placas
        texto_peixes = font.render(f'PEIXES: {contagem_peixes}', True, (0, 0, 0))
        texto_bolinhas = font.render(f'BOLINHAS: {bolinhas.qtd_bolinhas}', True, (0, 0, 0))
        texto_baiacus = font.render(f'BAIACUS: {contagem_baiacus}', True, (0, 0, 0))

        # Posicionar os textos dentro das placas
        text_rect1 = texto_peixes.get_rect(center=(placa_rect1.centerx, placa_rect1.centery))
        text_rect2 = texto_bolinhas.get_rect(center=(placa_rect2.centerx, placa_rect2.centery))
        text_rect3 = texto_baiacus.get_rect(center=(placa_rect3.centerx, placa_rect3.centery))

        constantes.SCREEN.blit(texto_peixes, text_rect1)
        constantes.SCREEN.blit(texto_bolinhas, text_rect2)
        constantes.SCREEN.blit(texto_baiacus, text_rect3)

        if classe_bolinha.Bolinha.verificar_pegou_bolinhas(bolinhas) and classe_peixe.Coletavel_peixe.verificar_pegou_peixes(peixes, contagem_peixes) and classe_baiacu.Coletavel_baiacu.verificar_pegou_baiacus(baiacus, contagem_baiacus):
            tela_vitoria()

        pygame.display.flip()    
        clock.tick(60)

    pygame.quit()
    sys.exit()
# --------------------------------------------------------------------------------------------------------------------------

