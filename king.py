'''
King subclass
'''
from piece import Piece

class King(Piece):  
    def disableCastle(self):
        self.canCastle = False
    
    def move(self, spaces, notation, newSpace):
        #use spaces and notation to determine if move is legal
        rO, fO, rN, fN = self.partitionSpaces(newSpace)
        dx = ord(fN) - ord(fO)
        dy = ord(rN) - ord(rO)
        #king can only move one space
        if abs(dx) != 1 and abs(dy) != 1:
            return None
        #check if diagonal
        if abs(dx) == abs(dy):
            #check spaces in between are empty
            a = abs(dx)
            for i in range(1, a):
                if spaces[chr(ord(fO)+dx//a*i)+chr(ord(rO)+dy//a*i)] != '  ':
                    return None
        #if not diagonal check horizontal/vertical
        #moving vertically
        elif fO == fN:
            #check if spaces in between are empty
            for i in range(1, abs(dy)):
                if spaces[fO+chr(ord(rO)+dy//abs(dy)*i)] != '  ':
                    return None
        #moving horizontally
        elif rO == rN:
            #check if spaces in between are empty
            for i in range(1, abs(dx)):
                if spaces[chr(ord(fO)+dx//abs(dx)*i)+rO] != '  ':
                    return None
        else:
            return None
        #return space to use as oldSpace
        return self.space

    def inCheck(self, spaces, kingSpace):
        pass
