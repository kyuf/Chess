'''
Knight subclass
'''
from piece import Piece

class Knight(Piece):
    note = 'N'
    
    def move(self, spaces, notation, newSpace):
        #use spaces and notation to determine if move is legal
        #return oldSpace
        rO, fO, rN, fN = self.partitionSpaces(newSpace)
        if (fO == fN or rO == rN
                or abs(ord(fO)-ord(fN)) + abs(ord(rO)-ord(rN)) != 3):
            return None
        else:
            return self.space
        
