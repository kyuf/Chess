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
        return not player.inCheck(tmpSpaces)

    def move(self, spaces, player):       
        #remove any existing vulnerability
        if self.vulnerable:
            self.vulnerable = False

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
                            and spaces[vulSpace].note == 'P'
                            and spaces[vulSpace].color != player.color
                            and spaces[vulSpace].isVul()):
                        if self.canEnPassant(spaces, newSpace,
                                vulSpace, player):
                            self.addToMoveset('{}x{}'.format(fO, newSpace))

    #state of vulnerability
    def isVul(self):
        '''
        Return Pawn's state of vulnerability to en passant
        '''
        return self.vulnerable

    def makeVul(self):
        '''
        Make pawn vulnerable
        '''
        self.vulnerable = True