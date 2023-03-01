import sys
import math
from src import Heuristic
from src import Pit
from src import Play
from src import Piece
# game loop
while True:
    inputs = input().split()
    pit_width = int(inputs[0])
    pit_height = int(inputs[1])
    pit_depth = int(inputs[2])
    pit_shape = inputs[3]
    pit = Pit(pit_width,pit_height, pit_depth, pit_shape)
    block_count = int(input())
    plays = []
    heuristic = Heuristic()
    for i in range(block_count): #each rotation for the block
        inputs = input().split()
        block_index = int(inputs[0])
        width = int(inputs[1])
        height = int(inputs[2])
        depth = int(inputs[3])
        shape = inputs[4]
        piece = Piece(block_index, width, height,depth,shape)
        play =heuristic.best_position(piece,pit)
        plays.append(play)
    plays.sort(reverse=True, key=lambda x:x.score) #ordena pela jogada com o menor score
    piece = plays[0].getPiece()
    #put the block in the pit
    print(piece.getBlockIndex()+ " "+ ' '.join(play.getPosition()))

    
