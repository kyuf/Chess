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

        if self.note != 'P':
            self.basicMoveTemplate = [self.note+'{}', self.note+'{}{}']
            self.captureMoveTemplate = [self.note+'x{}', self.note+'{}x{}']
    
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

    def updateMoveset(self, spaces, pathSet, player):
        '''
        Helper function for moving non-pawn pieces
        '''
        for filesAndRanks in pathSet:
            for f, r in filesAndRanks:
                newSpace = f + r

                # notation template for a non-capturing move
                if spaces[newSpace] == '  ':
                    regMove, explicitMove = self.basicMoveTemplate

                # notation template for a capturing move
                elif spaces[newSpace].color != player.color:
                    regMove, explicitMove = self.captureMoveTemplate

                # moving to newSpace is not valid
                else:
                    # continue to next space
                    if self.note in 'NK':
                        continue

                    # explore new path
                    else:
                        break

                # add moves to moveset
                if self.canMove(spaces, newSpace, player):
                    self.addToMoveset(regMove.format(newSpace))

                    # determine if explicit notation needs to be added
                    if self.note in 'BN':
                        needExplicit = player.sameColorSpace(
                                self.space, self.note)
                    else:
                        needExplicit = len(player.pieces[self.note]) > 1

                    if needExplicit:
                        for val in [self.space[0], self.space[1], self.space]:
                            self.addToMoveset(
                                    explicitMove.format(val, newSpace))



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