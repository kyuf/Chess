'''
Bishop subclass
'''
from piece import Piece

class Bishop(Piece):
    def move(self, spaces, notation, newSpace):
        #use spaces and notation to determine if move is legal
        rO, fO, rN, fN = self.partitionSpaces(newSpace)
        dx = ord(fN) - ord(fO)
        dy = ord(rN) - ord(rO)
        if abs(dx) != abs(dy):
            return None
        #check spaces in between are empty
        a = abs(dx)
        for i in range(1, a):
            if spaces[chr(ord(fO)+dx//a*i)+chr(ord(rO)+dy//a*i)] != '  ':
                return None
        #return space to use as oldSpace
        return self.space
