'''
Rook subclass
'''
from piece import Piece

class Rook(Piece):
    note = 'R'
    canCastle = True
    
    def disableCastle(self):
        self.canCastle = False
    
    def move(self, spaces, notation):
        #use spaces and notation to determine if move is legal
        #return oldSpace, newSpace, capture
        #capture is either type of piece captured or None 
        pass
