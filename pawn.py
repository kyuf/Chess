'''
Pawn subclass
'''
from copy import deepcopy

from piece import Piece

class Pawn(Piece):
    #modify __init__ to determine forawrd variable based off Piece color
    def __init__(self, color, space, note):
        Piece.__init__(self, color, space, note)
        self.vulnerable = False
    
    def canEnPassant(self, spaces, newSpace, vulSpace, player):
        tmpSpaces = deepcopy(spaces)
        tmpSpaces[newSpace] = spaces[self.space]
        tmpSpaces[self.space] = '  '
        tmpSpaces[vulSpace] = '  '
        return not player.newInCheck(tmpSpaces)

    def move(self, spaces, notation, newSpace):
        #check if pawn is in valid column
        if self.space[0] != notation[0]:
            return None

        #remove any existing vulnerability
        if self.vulnerable:
            self.vulnerable = False

        #use spaces and notation to determine if move is legal
        fO, rO, fN, rN = self.partitionSpaces(newSpace)
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

    def newMove(self, spaces, player):       
        fO, rO = self.space[0], self.space[1]

        # move forward one space
        newSpace = fO + chr(ord(rO)+self.forward)
        if spaces[newSpace] == '  ':
            if self.canMove(spaces, newSpace, player):
                #promoting
                if newSpace[-1] == player.ranks[2]:
                    for pro in 'NBRQ':
                        self.addToMoveset('{}={}'.format(newSpace, pro))
                #normal
                else:
                    self.addToMoveset(newSpace)
            #move forward two spaces
            if rO == player.ranks[1]:
                newSpace = fO + chr(ord(rO)+(self.forward*2))
                if spaces[newSpace] == '  ':
                    if self.canMove(spaces, newSpace, player):
                        self.addToMoveset(newSpace)

        # capture normal
        for f in [chr(ord(fO)-1), chr(ord(fO)+1)]:
            if f in 'abcdefgh':
                newSpace = f + chr(ord(rO)+self.forward)
                if (spaces[newSpace] != '  '
                        and spaces[newSpace].color != player.color):
                    if self.canMove(spaces, newSpace, player):
                        #promoting
                        if newSpace[-1] == player.ranks[2]:
                            for pro in 'NBRQ':
                                self.addToMoveset(
                                        '{}x{}={}'.format(fO, newSpace, pro))
                        #normal
                        else:
                            self.addToMoveset('{}x{}'.format(fO, newSpace))

        # capture en passant
        if rO == player.ranks[3]:
            for f in [chr(ord(fO)-1), chr(ord(fO)+1)]:
                if f in 'abcdefgh':
                    newSpace = f + chr(ord(rO)+self.forward)
                    vulSpace = f + rO
                    if (spaces[newSpace] == '  '
                            and spaces[vulSpace] != '  '
                            and spaces[vulSpace].vulnerable):
                        if self.canEnPassant(spaces, newSpace,
                                vulSpace, player):
                            self.addToMoveset('{}x{}'.format(fO, newSpace))

            # check if space is empty
            # move pawn
            # check if king in check
            # add to moveset if valid

    #state of vulnerability
    def isVul(self):
        '''
        Return Pawn's state of vulnerability to en passant
        '''
        return self.vulnerable

    #return space where vulnerable pawn would be captured and pawn space
    def getVulSpace(self):
        if self.vulnerable:
            return self.space[0] + chr(ord(self.space[1]) + self.forward)
        else:
            return None