'''
Pawn subclass
'''
from piece import Piece
from knight import *
from bishop import *
from rook import *
from queen import *

class Pawn(Piece):
    #modify __init__ to determine forawrd variable based off Piece color
    def __init__(self, color, space, note):
        Piece.__init__(self, color, space, note)
        self.hasNotMoved = True
        self.forward = 1 if self.color == 'w' else -1
    
    '''
    def move(self, spaces, notation, newSpace, capturedPiece, player):
        oldSpace = notation[0] + str(int(newSpace[1])-player.forward)
        #check if player has pawn on oldSpace
        if oldSpace in player.pieces['P']:
            #check if capturing files are adjacent
            if (capturedPiece
                    and abs(ord(newSpace[0])-ord(oldSpace[0])) != 1):
                raise RuntimeError('Capturing pawn files must be adjacent')
        #check if pawn is moving double
        #must be on starting rank and have clear path
        elif not capturedPiece:
            if (notation[0] + player.ranks[1] in player.pieces['P']
                    and spaces[oldSpace] == '  '
                    and notation[-1] == player.ranks[2]):
                oldSpace = notation[0] + player.ranks[1]
                #pawn is vulnerable
                player.vulnerableSpace = newSpace
            else:
                raise RuntimeError('Pawn move illegal')
    '''

    def promote(self, notation, newSpace):
        #method to promote pawn to new piece
        #promote to knight
        if notation[-1] == 'N':
            return Knight(self.color, newSpace)
        #promote to knight
        elif notation[-1] == 'B':
            return Bishop(self.color, newSpace)
        #promote to knight
        elif notation[-1] == 'R':
            return Rook(self.color, newSpace)
        #promote to knight
        elif notation[-1] == 'Q':
            return Queen(self.color, newSpace)
        else:
            return None
