'''
Rook subclass
'''
from piece import Piece

class Rook(Piece):
    note = 'R'
    canCastle = True
    
    def disableCastle(self):
        self.canCastle = False
