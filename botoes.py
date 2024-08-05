import pygame
import constantes as ct

# Este documento contém a classe dos botões, utilizados nas diferentes telas do jogo

pygame.init()

# ----------------------------------------------------------- BOTÕES ---------------------------------------------------------
class Botoes:
    # Inicializações
    def __init__ (self, imagem, texto, coord_centro):
        self.coord_centro = pygame.Vector2(coord_centro)
        self.imagem = imagem
        self.rect = self.imagem.get_rect(center=(self.coord_centro))
        self.fonte_botoes = pygame.font.Font('fontegamer.ttf', 35)

        self.texto = texto
        self.texto_normal = self.fonte_botoes.render(self.texto, True, (0,0,0))
        self.texto_normal_rect = self.texto_normal.get_rect(center=(self.coord_centro))

        self.texto_hoover = self.fonte_botoes.render(self.texto, True, (255, 255, 255))
        self.texto_hoover_rect = self.texto_hoover.get_rect(center=(self.coord_centro))

        self.clicado = False
        self.cursor_click = False

    # Mostrar botão na tela
    def desenhar_botao(self, tela, imagem, imagemrect, texto, textorect):
        tela.blit(imagem, imagemrect)
        tela.blit(texto, textorect)

    # Verificar se o botão foi clicado
    def verificar_clique(self, tela):
        posicao_mouse = pygame.mouse.get_pos()

        if self.rect.collidepoint(posicao_mouse):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicado == False:
                self.clicado = True
        
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicado = False
        return self.clicado
    
    # Verificar se o usuário passou o cursor pelo botão
    def verificar_hoover(self, click, padrao):
     
        posicao_mouse = pygame.mouse.get_pos()
        if self.rect.collidepoint(posicao_mouse):
            
            self.imagem = ct.BOTAO_HOOVER
            if self.texto_normal_rect.collidepoint(posicao_mouse):
                Botoes.desenhar_botao(self, ct.SCREEN, self.imagem, self.rect, self.texto_hoover, self.texto_hoover_rect)
            else:
                Botoes.desenhar_botao(self, ct.SCREEN, self.imagem, self.rect, self.texto_normal, self.texto_normal_rect)
            
            if not self.cursor_click:
                pygame.mouse.set_cursor(click)
                self.cursor_click = True

        else:
            self.imagem = ct.BOTAO
            Botoes.desenhar_botao(self, ct.SCREEN, self.imagem, self.rect, self.texto_normal, self.texto_normal_rect)
            if self.cursor_click:
                pygame.mouse.set_cursor(padrao)
                self.cursor_click = False
                pygame.mouse.set_cursor(padrao)
                self.cursor_click = False
# -----------------------------------------------------------------------------------------------------------------------------