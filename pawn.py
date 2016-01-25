'''
Pawn subclass
'''
from piece import Piece

class Pawn(Piece):
    note = 'P'
    hasMoved = False
    
    def move(self, spaces, notation):
        #use spaces and notation to determine if move is legal
        pass
