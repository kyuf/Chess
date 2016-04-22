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
        #helper functions
        def checkCheck(space, attackers):
            if space.color != self.color and space.note in attackers:
                return True
            return False

        def getRange(sig, start, end):
            return [chr(i) for i in range(ord(start)+sig, ord(end)+sig, sig)]

        #get space coordinate values
        fO, rO = kingSpace[0], kingSpace[1]

        #set range variables
        up = getRange(1, rO, '8')
        down = getRange(-1, rO, '1')
        right = getRange(1, fO, 'h')
        left = getRange(-1, fO, 'a')

        #check for vertical and horizontal attackers
        for filesAndRanks in [
                zip([fO]*len(up), up),
                zip([fO]*len(down), down),
                zip(right, [rO]*len(right)),
                zip(left, [rO]*len(left))
                ]:
            for f, r in filesAndRanks:
                space = spaces[f+r]
                if space != '  ':
                    if checkCheck(space, 'RQK'):
                        return True
                    break

        #check for knight attackers
        for k in [0, 1]:
            for r in [ord(rO)+(2-k), ord(rO)-(2-k)]:
                if r >= ord('1') and r <= ord('8'):
                    for f in [ord(fO)+(1+k), ord(fO)-(1+k)]:
                        if f >= ord('a') and f <= ord('h'):
                            space = spaces[chr(f)+chr(r)]
                            if space != '  ':
                                if checkCheck(space, 'N'):
                                    return True

        #check for diagonal attackers
        #include check for pawn attackers here
        for filesAndRanks in [
                zip(right, up),
                zip(left, up),
                zip(right, down),
                zip(left, down)
                ]:
            for f, r in filesAndRanks:
                print(f+r)
                space = spaces[f+r]
                if space != '  ':
                    #spaces where pawns need to be considered
                    if ord(r) - ord(rO) == self.forward:
                        attackers = 'PBQK'
                    #no pawns
                    else:
                        attackers = 'BQK'
                    if checkCheck(space, attackers):
                        return True
                    break

        return False