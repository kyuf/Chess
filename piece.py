from copy import deepcopy

class Piece:
    '''
    Superclass for chess pieces
    '''
    def __init__(self, color, space, note):
        #color is either 'w' or 'b'
        self.color = color
        self.note = note
        self.space = space
        #pawn and king need forward attribute for move calculations
        if self.note in 'PK':
            self.forward = 1 if self.color == 'w' else -1
    
    def __repr__(self):
        #self.note defined in subclasses
        return self.color + self.note
    
    def updatePieceSpace(self, newSpace):
        '''
        Updates piece space to given newSpace after moving
        '''
        self.space = newSpace
    
    def addToMoveset(self, *args):
        '''
        Adds moves (in notation) to the piece's moveset attribute
        '''
        for move in args:
            self.moveset[move] = self.space

    def getMoveset(self, spaces, player):
        '''
        Find available moves for piece
        '''
        self.moveset = {}
        self.move(spaces, player)
        return self.moveset

    def canMove(self, spaces, newSpace, player):
        tmpSpaces = deepcopy(spaces)
        tmpSpaces[newSpace] = spaces[self.space]
        tmpSpaces[self.space] = '  '
        if tmpSpaces[newSpace].note == 'K':
            return not player.inCheck(tmpSpaces, newSpace)
        return not player.inCheck(tmpSpaces)


class CastlePiece(Piece):
    '''
    Class for pieces that can castle (king and rook)
    '''
    def __init__(self, color, space, note):
        Piece.__init__(self, color, space, note)
        self.canCastle = True

    def disableCastle(self):
        '''
        Sets piece canCastle attribute to False
        '''
        self.canCastle = False