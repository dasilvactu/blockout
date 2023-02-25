import sys
import math
from heristic import Heuristic
from pit import Pit
from play import Play
from piece import Piece
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
        #use the Heuristic to choose a position
        position,score = heuristic.best_position(piece,pit)
        play = Play(piece,position,score)
        plays.append(piece)
    plays.sort(key=lambda x:x.score)
    play = plays[0]
    piece = play.getPiece()
    #put the block in the pit
    print(piece.getBlockIndex()+ " "+ ' '.join(play.getPosition()))

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    
