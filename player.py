'''
Player class contains information of player's pieces and allows moves to be
made.
'''
import castle
from bishop import Bishop
from knight import Knight
from rook import Rook
from queen import Queen

class Player:
    def __init__(self, color):
        self.color = color
        self.moveset = None
        # self.castleset = {'O-O', 'O-O-O'}
        #color used to determine starting ranks
        if self.color == 'w':
            self.ranks = '1285'
        else:
            self.ranks = '8714'
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
        self.vulSpace = None
    
    def getMoveset(self, spaces):
        '''
        Create new set of available moves for player from board conditions
        '''
        self.moveset = {}
        self.banned = set()
        for typ in 'PNBRQK':
            for testPiece in self.pieces[typ]:
                for move, oldSpace in spaces[testPiece].getMoveset(
                            spaces, self).items():
                    if move in self.moveset or move in self.banned:
                        self.moveset.pop(move, None)
                        self.banned.add(move)
                    else:
                        self.moveset[move] = oldSpace

        # self.moveset |= self.castleset

    def sameColorBishops(self, space):
        for bishopSpace in self.pieces['B']:
            if bishopSpace != space:
                #black spaces are even and white spaces are odd
                rem = sum(map(ord, space)) % 2
                if (sum(map(ord, bishopSpace)) % 2) == rem:
                    return True
        return False

    def inCheck(self, spaces, kingSpace=None):
        '''
        Return True if King in check else False
        '''
        if kingSpace:
            return spaces[kingSpace].inCheck(spaces, kingSpace)
        for kingSpace in self.pieces['K']:
            #will raise error if king in check
            return spaces[kingSpace].inCheck(spaces, kingSpace)

    def move(self, notation, spaces, opponent):
        #vulnerable pawns can be captured en passant
        #clear any previously vulnerable pawns
        self.vulSpace = None

        #castle if O-O or O-O-O
        if notation == 'O-O' or notation == 'O-O-O':
            castling = True
            spaces, newSpaces, oldSpaces, pieceType = castle.castle(
                    notation, spaces, self)
        #no castle move
        elif notation in self.moveset:
            castling = False
            #determine new space
            if notation[-2] != '=':
                newSpace = notation[-2:]
                promoting = False
            else:
                #pawn promotion has '=X' at end of notation where X is new
                #piece type
                newSpace = notation[-4:-2]
                promoting = True

            #check for capture
            if 'x' in notation:
                if spaces[newSpace] != '  ':
                    capturedPiece = spaces[newSpace]
                #if captured space is empty en passant
                else:
                    capturedPiece = spaces[opponent.vulSpace]
            else:
                capturedPiece = None
            
            #determine piece being moved
            #pawn if first letter is lowercase
            if notation[0] in 'abcdefgh':
                pieceType = 'P'
            #rook, knight, bishop, queen, king
            elif notation[0] in 'RNBQK':
                pieceType = notation[0]      
            #no piece found
            else:
                raise RuntimeError('Incorrect piece notation')
            
            #find correct piece to move
            oldSpace = self.moveset[notation]

            #special considerations for moving pawns
            if pieceType == 'P':
                #check if pawn was made vulnerable
                if abs(ord(newSpace[1])-ord(oldSpace[1])) == 2:
                    self.vulSpace = newSpace
                    spaces[oldSpace].makeVul()
                #check if pawn is being promoted
                elif promoting:
                    newPiece = notation[-1]
                    if newPiece in 'RNBQ':
                        self.pieces['P'].remove(oldSpace)
                        self.pieces[newPiece].add(oldSpace)
                        if newPiece == 'R':
                            spaces[oldSpace] = Rook(
                                    self.color, oldSpace, 'R')
                            #disable new rook's ability to castle
                            spaces[oldSpace].disableCastle()
                        elif newPiece == 'N':
                            spaces[oldSpace] = Knight(
                                    self.color, oldSpace, 'N')
                        elif newPiece == 'B':
                            spaces[oldSpace] = Bishop(
                                    self.color, oldSpace, 'B')
                        else:
                            spaces[oldSpace] = Queen(
                                    self.color, oldSpace, 'Q')
                        pieceType = newPiece
                    else:
                        raise RuntimeError('Invalid promotion')

            #remove captured piece from opponent's pieces
            if capturedPiece:
                spaces[capturedPiece.space] = '  '
                opponent.pieces[capturedPiece.note].remove(
                        capturedPiece.space) 

            #reformat newSpace and oldSpace
            newSpaces, oldSpaces = [newSpace], [oldSpace]

        else:
            raise RuntimeError('Invalid notation')

        #update spaces and pieces
        for n, o, p in zip(newSpaces, oldSpaces, pieceType):
            #set piece at new space
            spaces[n] = spaces[o]
            spaces[n].updatePieceSpace(n)
            #clear old space
            spaces[o] = '  '
            #update player piece sets
            self.pieces[p].remove(o)
            self.pieces[p].add(n)   

        #disable castling for piece if rook or king
        if not castling and pieceType in 'KR':
            spaces[newSpace].disableCastle()

        #update spaces and opponent
        return spaces, opponent
    
    def __repr__(self):
        return 'White' if self.color == 'w' else 'Black'
