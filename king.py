'''
King subclass
'''
from piece import Piece

class King(Piece):
    note = 'K'
    canCastle = True
    
    def disableCastle(self):
        self.canCastle = False
