'''
Player class contains information of player's pieces and allows moves to be
made.
'''
from copy import deepcopy
import castle
import king
from knight import *
from bishop import *
from rook import *
from queen import *

class Player:
    #pieces contains dictionary with sets of current positions for each type
    #of piece
    def __init__(self, color):
        self.color = color
        #color used to determine starting ranks
        if self.color == 'w':
            self.ranks = '128'
        else:
            self.ranks = '871'
        #add initial pawn positions
        self.pieces = {}
        self.pieces['P'] = set()
        for f in 'abcdefgh':
            self.pieces['P'].add(f+self.ranks[1])
        #add initial rook, knight, bishop, queen, king positions
        r = self.ranks[0]
        self.pieces['R'] = {'a'+r, 'h'+r}
        self.pieces['N'] = {'b'+r, 'g'+r}
        self.pieces['B'] = {'c'+r, 'f'+r}
        self.pieces['Q'] = {'d'+r}
        self.pieces['K'] = {'e'+r}
        #no pawns vulnerable at start of game
        self.vulSpaces = None
    
    #moves follow PGN notation
    def move(self, notation, spaces, opponent):
        #vulnerable pawns can be captured en passant
        #clear any previously vulnerable pawns
        self.vulSpaces = None
        
        #store temporary vaiables in case of check
        tmpSpaces = deepcopy(spaces)
        tmpOpponent = deepcopy(opponent)

        #castle if O-O or O-O-O
        if notation == 'O-O' or notation == 'O-O-O':
            tmpSpaces, self.pieces = castle.castle(notation, tmpSpaces, self)
            return tmpSpaces, opponent
        
        #determine new space
        if notation[-2] != '=':
            newSpace = notation[-2:]
            promoting = False
        else:
            #pawn promotion will put '=X' at end of notation where X is new
            #piece type
            newSpace = notation[-4:-2]
            if newSpace[1] == self.ranks[2]:
                promoting = True
            else:
                raise RuntimeError('Can only promote on last rank')
        #check that new space is within the board
        if newSpace[0] not in 'abcdefgh' or newSpace[1] not in '12345678':
            raise RuntimeError('Cannot move outside of board')
        #check for capture
        capturedPiece = tmpSpaces[newSpace] if 'x' in notation else None
        
        #check if capture is legal
        if capturedPiece:
            #captured space cannot be empty unless en passant
            if capturedPiece == '  ':
                if opponent.vulSpaces and opponent.vulSpaces[0] == newSpace:
                    capturedPiece = tmpSpaces[opponent.vulSpaces[1]]
                else:
                    raise RuntimeError('No piece to capture')
            #cannot capture king
            elif type(capturedPiece) == king.King:
                raise RuntimeError('Cannot capture King')
            #cannot capture piece of same color
            elif capturedPiece.color == self.color:
                raise RuntimeError('Cannot capture own piece')
            
        #if not capturing new space cannot be occupied
        else:
            if tmpSpaces[newSpace] != '  ':
                raise RuntimeError('Cannot move into occupied space')
        
        #determine piece being moved
        #pawn if first letter is lowercase
        if notation[0] in 'abcdefgh':
            pieceType = 'P'      
        #rook, knight, bishop, queen, king if first letter is R, N, B, Q, K
        elif notation[0] in 'RNBQK':
            pieceType = notation[0]      
        #no piece found
        else:
            raise RuntimeError('Incorrect piece notation')
        
        #find correct piece to move
        for pieceSpace in self.pieces[pieceType]:
            oldSpace = tmpSpaces[pieceSpace].move(
                    tmpSpaces, notation, newSpace
                    )
            if oldSpace:
                break
        if not oldSpace:
            #move is illegal
            raise RuntimeError('Move found to be illegal')

        #special considerations for moving pawns
        if pieceType == 'P':
            #check if pawn was made vulnerable
            if tmpSpaces[oldSpace].isVul():
                self.vulSpaces = tmpSpaces[oldSpace].getVulSpace(), newSpace
            #check if pawn is being promoted
            elif promoting:
                newPiece = notation[-1]
                if newPiece in 'RNBQ':
                    self.pieces['P'].remove(oldSpace)
                    self.pieces[newPiece].add(oldSpace)
                    if newPiece == 'R':
                        tmpSpaces[oldSpace] = Rook(self.color, oldSpace, 'R')
                    elif newPiece == 'N':
                        tmpSpaces[oldSpace] = Knight(self.color, oldSpace, 'N')
                    elif newPiece == 'B':
                        tmpSpaces[oldSpace] = Bishop(self.color, oldSpace, 'B')
                    else:
                        tmpSpaces[oldSpace] = Queen(self.color, oldSpace, 'Q')
                    pieceType = newPiece
                else:
                    raise RuntimeError('Invalid promotion')

        #remove captured piece from opponent's pieces
        if capturedPiece:
            tmpSpaces[capturedPiece.space] = '  '
            tmpOpponent.pieces[capturedPiece.note].remove(capturedPiece.space)
        #set piece at new space
        tmpSpaces[newSpace] = tmpSpaces[oldSpace]
        tmpSpaces[newSpace].updatePieceSpace(newSpace)
        #clear old space
        tmpSpaces[oldSpace] = '  '
        #update player piece sets
        self.pieces[pieceType].remove(oldSpace)
        self.pieces[pieceType].add(newSpace)   

        #check if player's king is in check
        for kingSpace in self.pieces['K']:
            #will raise error if king in check
            if tmpSpaces[kingSpace].inCheck(tmpSpaces, kingSpace):
                #reverse pieces update
                self.pieces[pieceType].remove(newSpace)
                self.pieces[pieceType].add(oldSpace) 
                raise RuntimeError('King in check')

        #return updated spaces and captured piece type
        return tmpSpaces, tmpOpponent
        
    
    def __repr__(self):
        return 'White' if self.color == 'w' else 'Black'
