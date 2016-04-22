'''
King subclass
'''
from piece import Piece

class King(Piece):  
    def disableCastle(self):
        self.canCastle = False
    
    def move(self, spaces, notation, newSpace):
        #use spaces and notation to determine if move is legal
        fO, rO, fN, rN = self.partitionSpaces(newSpace)
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
        fO, rO = kingSpace[0], kingSpace[1]

        #set range variables
        up = range(ord(rO)+1, ord('8'))
        down = range(ord(rO)-1, ord('1'), -1)
        right = range(ord(fO)+1, ord('h'))
        left = range(ord(fO)-1, ord('a'), -1)

        #check for vertical attackers
        for d in [up, down]:
            for r in d:
                pass

        #check for horizontal attackers
        for d in [right, left]:
            for f in d:
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
        for d in [
                zip(up, right),
                zip(up, left),
                zip(down, right),
                zip(down, left)
                ]:
            for r, f in d:
                pass

        return False