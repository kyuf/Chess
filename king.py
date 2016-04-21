'''
King subclass
'''
from itertools import chain
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
        #get space coordinate values
        rO, fO = kingSpace[1], kingSpace[0]

        #set range variables
        up = range(ord(rO), ord('8'))
        down = range(ord(rO), ord('1'), -1)
        right = range(ord(fO), ord('h'))
        left = range(ord(fO), ord('a'), -1)

        #check for vertical attackers
        for r in chain(up, down):
            pass

        #check for horizontal attackers
        for f in chain(right, left):
            pass
        #check for knight attackers
        for k in [0, 1]:
            for f in [ord(fO)+(2-k), ord(fO)-(2-k)]:
                if f >= ord('1') and f <= ord('8'):
                    for r in [ord(rO)+(1+k), ord(rO)-(1+k)]:
                        if r >= ord('a') and r <= ord('h'):
                            pass
        #check for diagonal attackers
        #include check for pawn attackers here
        for r, f in chain(
                zip(up, right),
                zip(up, left),
                zip(down, right),
                zip(down, left)
                ):
            pass

        return False