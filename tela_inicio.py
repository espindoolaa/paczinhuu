import pygame
import sys
import constantes as ct
import botoes as bt
from main import rodar_jogo
from pathlib import Path

pygame.init()

def tela_menuinicial():
    screen = pygame.display.set_mode((1075, 614))

    imagemfundo_inicial = pygame.image.load(Path('imgs', 'menuinicial.png'))
    imagem_botao = pygame.image.load(Path('imgs', 'botao.png'))

    # Botões da tela de início
    botoes_menu = []

    botao_jogar = bt.Botoes(imagem_botao, 'JOGAR', (543, 300))
    botao_sair = bt.Botoes(imagem_botao, 'SAIR', (543, 370))

    botoes_menu.append(botao_jogar)
    botoes_menu.append(botao_sair)

    # Rodar tela de início
    while True:
        screen.blit(imagemfundo_inicial, (0, 0))
        pygame.display.set_caption('Paczinhuu - Menu Inicial')
        for botao in botoes_menu:
            bt.Botoes.desenhar_botao(botao, screen)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if evento.type == pygame.MOUSEBUTTONDOWN:
                for botao in botoes_menu:
                    clicou = bt.Botoes.verificar_clique(botao)
                    if clicou == True:  
                        if botao == botao_jogar:
                            tela_historia()
                        if botao == botao_sair:
                            pygame.quit()
                            sys.exit()

        pygame.display.update()

def tela_historia():
    screen = pygame.display.set_mode((1075, 614))
    imagemfundo_historia = pygame.image.load(Path('imgs', 'historia.png'))
    
    while True:
        screen.blit(imagemfundo_historia, (0, 0))
        pygame.display.set_caption('Paczinhuu - Instruções')

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    tela_instrucoes()

        pygame.display.update()

def tela_instrucoes():
    screen = pygame.display.set_mode((1075, 614))
    imagemfundo_instrucoes = pygame.image.load(Path('imgs', 'instrucoes.png'))
    
    while True:
        screen.blit(imagemfundo_instrucoes, (0, 0))
        pygame.display.set_caption('Paczinhuu - Instruções')

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    rodar_jogo()

        pygame.display.update()

#def tela_pausa():

def tela_gameover():
    screen = pygame.display.set_mode((1075, 614))
    imagemfundo_gameover = pygame.image.load(Path('imgs''gameover.png'))
    
    while True:
        screen.blit(imagemfundo_gameover, (0, 0))
        pygame.display.set_caption('Paczinhuu - GAME OVER!')

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

def tela_vitoria():
    screen = pygame.display.set_mode((1075, 614))
    imagemfundo_vitoria = pygame.image.load(Path('imgs''vitoria.png'))
    
    while True:
        screen.blit(imagemfundo_vitoria, (0, 0))
        pygame.display.set_caption('Paczinhuu - VITÓRIA!')

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

# Aqui o jogo é rodado
tela_menuinicial()
