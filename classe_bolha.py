import constantes
import math
from classe_italo import ItaloSena

# Esse documento contém a classe das bolhas

# Haverá 121 bolhas no mapa

# Para ganhar o jogo, o jogador deve coletar todas as bolhas, além dos peixes e dos baiacus

# --------------------------------------------- COLETÁVEL: BOLINHAS -------------------------------------------------
class Coletavel_bolha(ItaloSena):
    # Inicializações 
    def __init__(self, x, y, peixes, mapa):
        self.posicoes = []
        self.mapa = mapa
        self.gerar_posicoes(x, y, peixes)
        self.qtd_bolhas = 0

    # Posicionar as bolhas nos corredores
    def gerar_posicoes(self, x_inicial, y_inicial, peixes):
        def posicao_valida(x, y):
            if 0 <= y // 47 < len(self.mapa) and 0 <= x // 47 < len(self.mapa[0]):
                mapa_y = y // 47
                mapa_x = x // 47
                return self.mapa[mapa_y][mapa_x] == '.'
            return False
        
        for x in range(x_inicial, 1068, 47):
            for y in range(y_inicial, 620, 47):
                if posicao_valida(x, y) and (x, y) not in peixes.posicoes:
                    self.posicoes.append((x, y))
    
    # Mostrar as bolhas na tela
    def renderizar(self, screen):
        for pos in self.posicoes:
            screen.blit(constantes.BOLHA, pos)
    
    # Verificar a colisão com a bolha para coletá-la
    def verificar_colisao(self, position):
        to_remove = []
        for pos in self.posicoes:
            distancia = math.sqrt((pos[0] - position.x) ** 2 + (pos[1] - position.y) ** 2)
            if distancia < constantes.RAIO_BOLINHA + 19:
                to_remove.append(pos)
        
        for pos in to_remove:
            self.posicoes.remove(pos)
            self.qtd_bolhas += 1

    # Verificar se pegou todas as bolhas
    def verificar_pegou_bolhas(self):
        if self.qtd_bolhas == 121:
            return True
        return False
# --------------------------------------------------------------------------------------------------------------------
