import play
import numpy as np
class Heuristic(): #greedy
    def __init__(self):
        pass
    def best_position(self,piece,pit): #heuristica gulosa que retorna a posição que o elemento deve ser posto, baseado no avanço máximo em altura.
        pitMatrix = pit.getMatrixPerLevel()
        # cria a matriz do elemento para que ela represente as posições marcadas na representação em 3d
        piece.setMatrix(pit)
        #para as variacoes de largura e profundidade, falta definir uma estratégia melhor para saber as variações exatas em cada dimensão, respeitando os limites do pit
        movesX = 1
        movesz = 1
        plays = []
        for z in range(movesZ):
            for x in range(movesX):
                # 2 - cria a jogada com as coordenadas de largura e profundidade
                play = Play(piece,[x,z],pit.getHeight())
                y = pit.getHeight()
                contactMatrix = np.array(pitMatrix) + np.array(piece.getMatrix())
                while 2 not in contactMatrix: 
                    y = y -1
                    piece.movePiece(-1)
                    contactMatrix = np.array(pitMatrix) + np.array(piece.getMatrix())
                play.setscore(y)
                plays.append(play)
        plays.sort(reverse=True, key=lambda x:x.score) #ordena pela jogada com o menor score
        #retorna a jogada que tiver o menor score
        return plays[0]
        