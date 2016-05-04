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
    
    def partitionSpaces(self, newSpace):
        '''
        Partitions spaces into rank and file for calculations
        '''
        #old file, old rank, new file, new rank
        return self.space[0], self.space[1], newSpace[0], newSpace[1]
    
    def addToMoveset(self, *args):
        '''
        Adds moves (in notation) to the piece's moveset attribute
        '''
        for move in args:
            self.moveset.add(move)

    def getMoveset(self, spaces, player):
        '''
        Find available moves for piece
        '''
        self.moveset = set()
        self.newMove(spaces, player)
        return self.moveset

    def canMove(self, spaces, newSpace, player):
        tmpSpaces = deepcopy(spaces)
        tmpSpaces[newSpace] = spaces[self.space]
        tmpSpaces[self.space] = '  '
        if tmpSpaces[newSpace].note == 'K':
            return not player.newInCheck(tmpSpaces, newSpace)
        return not player.newInCheck(tmpSpaces)


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