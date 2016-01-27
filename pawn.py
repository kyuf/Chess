'''
Pawn subclass
'''
from piece import Piece

class Pawn(Piece):
    note = 'P'
    hasMoved = False
    
    def move(self, spaces, notation):
        #use spaces and notation to determine if move is legal
        #return oldSpace, newSpace, capture
        #capture is either type of piece captured or None 
        pass
    
    def promote(self, pick):
        #method to promote pawn to new piece
