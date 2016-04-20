'''
Rook subclass
'''
from piece import Piece

class Rook(Piece):
    def disableCastle(self):
        self.canCastle = False
    
    def move(self, spaces, notation, newSpace):
        #use spaces and notation to determine if move is legal
        rO, fO, rN, fN = self.partitionSpaces(newSpace)
        #moving vertically
        if fO == fN:
            dy = ord(rN) - ord(rO)
            #check if spaces in between are empty
            for i in range(1, abs(dy)):
                if spaces[fO+chr(ord(rO)+dy//abs(dy)*i)] != '  ':
                    return None
        #moving horizontally
        elif rO == rN:
            dx = ord(fN) - ord(fO)
            #check if spaces in between are empty
            for i in range(1, abs(dx)):
                if spaces[chr(ord(fO)+dx//abs(dx)*i)+rO] != '  ':
                    return None
        else:
            return None
        #return space to use as oldSpace
        return self.space
