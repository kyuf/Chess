'''
Pawn subclass
'''
from piece import Piece

class Pawn(Piece):
    note = 'P'
    hasNotMoved = True
    
    def promote(self, pick):
        #method to promote pawn to new piece
        pass
