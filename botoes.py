import pygame

pygame.init()

class Botoes:
    def __init__ (self, imagem, texto, coord_centro):
        self.coord_centro = pygame.Vector2(coord_centro)
        self.imagem = imagem
        self.rect = self.imagem.get_rect(center=(self.coord_centro))
        fonte_botoes = pygame.font.Font('fontegamer.ttf', 35)

        self.texto = texto
        self.texto_fonte = fonte_botoes.render(self.texto, True, (0,0,0))
        self.texto_rect = self.texto_fonte.get_rect(center=(self.coord_centro))

        self.texto = texto
        self.texto_fonte = fonte_botoes.render(self.texto, True, (0,0,0))
        self.texto_rect = self.texto_fonte.get_rect(center=(self.coord_centro))

        self.clicado = False

    def desenhar_botao(self, tela):
        tela.blit(self.imagem, self.rect)
        tela.blit(self.texto_fonte, self.texto_rect)

    def verificar_clique(self):
        posicao_mouse = pygame.mouse.get_pos()

        if self.rect.collidepoint(posicao_mouse):
                if pygame.mouse.get_pressed()[0] == 1 and self.clicado == False:
                    self.clicado = True
        
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicado = False
        return self.clicado