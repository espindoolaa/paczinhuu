import pygame
import sys
import constantes as ct
import botoes as bt

pygame.init()

def tela_menuinicial():
    screen = pygame.display.set_mode(ct.SIZE)

    imagemfundo_inicial = pygame.image.load('menuinicial.png')
    imagem_botao = pygame.image.load('botao.png')

    botoes_menu = []

    botao_jogar = bt.Botoes(imagem_botao, 'JOGAR', (543, 280))
    botao_sair = bt.Botoes(imagem_botao, 'SAIR', (543, 320))

    botoes_menu.append(botao_jogar)
    botoes_menu.append(botao_sair)

    while True:
        screen.blit(imagemfundo_inicial, (0, 0))
        pygame.display.set_caption('Paczinhuu - Menu Inicial')
                
        clicou = bt.Botoes.verificar_clique()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if evento.type == pygame.MOUSEBUTTONDOWN:
                for botao in botoes_menu:
                    clicou = bt.Botoes.verificar_clique()
                    if clicou == True:
                        if botao == botao_jogar:
                            tela_historia()
                        if botao == botao_sair:
                            pygame.quit()
                            sys.exit()


def tela_historia():
    

#def tela_instrucoes():

#def tela_gameover():

#def tela_vitoria():
