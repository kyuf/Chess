'''
Pawn subclass
'''
from piece import Piece

class Pawn(Piece):
    #modify __init__ to determine forawrd variable based off Piece color
    def __init__(self, color, space, note):
        Piece.__init__(self, color, space, note)
        self.vulnerable = False
    
    def move(self, spaces, notation, newSpace):
        #check if pawn is in valid column
        if self.space[0] != notation[0]:
            return None

        #remove any existing vulnerability
        if self.vulnerable:
            self.vulnerable = False

        #use spaces and notation to determine if move is legal
        rO, fO, rN, fN = self.partitionSpaces(newSpace)
        dy = ord(rN) - ord(rO)

        #no capture is being made
        if not 'x' in notation:
            #single space move
            if dy == self.forward:
                return self.space
            #double space move
            elif dy == self.forward * 2:
                #check that pawn has not moved
                if rO != '2' and rO != '7':
                    return None
                #check if middle space is empty
                mid = spaces[fO+chr(ord(rO)+self.forward)]
                if mid == '  ':
                    self.vulnerable = True
                    return self.space 
                else:
                    return None
        #capture is being made
        else:
            #capture must be single diagonal
            if abs(ord(fO)-ord(fN)) == 1 and dy == self.forward:
                return self.space
            else:
                return None

    #state of vulnerability
    def isVul(self):
        return self.vulnerable

    #return space where vulnerable pawn would be captured and pawn space
    def getVulSpace(self):
        if self.vulnerable:
            return self.space[0] + chr(ord(self.space[1]) + self.forward)
        else:
            return None