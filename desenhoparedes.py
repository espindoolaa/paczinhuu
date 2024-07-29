import pygame

pygame.init()

class Paredes():
    def __init__(self, x, y):
        self.boia = pygame.image.load("boiaquadrada.png")
        self.boia_size = self.boia.get_size()
        self.boia = pygame.transform.scale(self.boia, (1/9 * self.boia_size[0], 1/9 * self.boia_size[1]))
        self.boia_x = x
        self.boia_y = y
        self.coord = (x, y) 

    def printar_paredes(self, tela):
        tela.blit(self.boia, self.coord)   
        
def desenhar_paredes(nums, linha, tela, pular = (), dir = True):
    for k in nums:
        # Checando se k é um número a ser pulado
        if pular != ():
            num_pulado = False
            for t in pular:
                if k == t:
                    num_pulado = True

            if num_pulado == False:
                if dir == True:
                    parede = Paredes(k, linha)
                else:
                    parede = Paredes(linha, k)
                parede.printar_paredes(tela) 
        # Se não houver número a ser pulado   
        else:
            if dir == True:
                parede = Paredes(k, linha)
            else:
                parede = Paredes(linha, k)
            parede.printar_paredes(tela)  
        

def paredes_na_tela(tamanho_tela, tela):

    # ------- BORDAS --------
    desenhar_paredes(range(2, tamanho_tela[0] - 47, 47), 0, tela) # Parede do topo
    desenhar_paredes(range(2, tamanho_tela[0] - 47, 47), 564, tela) # Parede de baixo
    desenhar_paredes(range(47, tamanho_tela[1] - 47, 47), 2, tela, pular = (188, 282, 376), dir = False ) # Lateral esquerda
    desenhar_paredes(range(47, tamanho_tela[1] - 47, 47), 1036, tela, pular = (188, 282, 376), dir = False) # Lateral direita

    # ------- GAIOLA ----------
    desenhar_paredes(range(425, 614, 47), 235, tela, pular = (519,)) # Parede do topo da gaiola
    desenhar_paredes(range(425, 614, 47), 329, tela) # Parede de baixo da gaiola
    desenhar_paredes((425, 613), 282, tela) # Parede das laterais da gaiola

    # ------- RESTO DAS PAREDES ---------
    desenhar_paredes((96, 519, 942), 47, tela) # Linha 2
    desenhar_paredes((237, 284, 331, 425, 613, 707, 754, 801), 94, tela) # Linha 3
    desenhar_paredes((49, 96, 143, 237, 425, 472, 566, 613, 801, 895, 942, 989), 141, tela) # Linha 4
    desenhar_paredes((143, 237, 331, 707, 801, 895), 188, tela) # Linha 5
    desenhar_paredes((49, 96, 143, 237, 331, 707, 801, 895, 942, 989), 235, tela) # Linha 6
    desenhar_paredes((331, 707), 282, tela) # Linha 7
    desenhar_paredes((49, 96, 143, 237, 331, 707, 801, 895, 942, 989), 329, tela) # Linha 8
    desenhar_paredes((143, 331, 707, 895), 376, tela) # Linha 9
    desenhar_paredes((49, 96, 143, 237, 284, 331, 425, 472, 519, 556, 613, 707, 754, 801, 895, 942, 989), 423, tela) # Linha 10
    desenhar_paredes((237, 425, 519, 613, 801), 470, tela) # Linha 11
    desenhar_paredes((96, 237, 331, 519, 707, 801, 942), 517, tela) # Linha 12
