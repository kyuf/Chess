'''
Player class contains information of player's pieces and allows moves to be
made.
'''
import castle

class Player:
    #pieces contains dictionary with lists of current positions for each type
    #of piece
    def __init__(self, color):
        self.color = color
        if self.color == 'w':
            self.ranks = '12'
        else:
            self.ranks = '87'
        #add initial pawn positions
        pieces = {}
        pieces['P'] = []
        for f in 'abcdefgh':
            pieces['P'].append(f+self.ranks[1])
        #add initial rook, knight, bishop, queen, king positions
        r = self.ranks[0]
        pieces['R'] = ['a'+r, 'h'+r]
        pieces['N'] = ['b'+r, 'g'+r]
        pieces['B'] = ['c'+r, 'f'+r]
        pieces['Q'] = ['d'+r]
        pieces['K'] = ['e'+r]
        #store into self
        self.pieces = pieces
    
    #moves follow PGN notation
    def move(self, notation, spaces):
        #determine piece being moved
        #pawn if first letter is lowercase
        if notation[0] in 'abcdefgh':
            pieceType = 'P'
        #rook, knight, bishop, queen, king if first letter is R, N, B, Q, K
        elif notation[0] in 'RNBQK':
            pieceType = notation[0]
        #castle if O-O or O-O-O
        elif notation == 'O-O' or notation == 'O-O-O':
            spaces, self.pieces = castle.castle(notation, spaces, self)
            #castling does not capture so second and third are None
            return spaces, None
        #no piece found
        else:
            raise RuntimeError('Incorrect piece notation')
            
        #check if move is legal
        #check for capture
        newSpace = notation[-2:]
        capturedPiece = spaces[newSpace] if 'x' in notation else None
        #cannot capture king or piece of same color
        if capturedPiece:
            if capturedPiece.note == 'K' or capturedPiece.color == player.color:
                return False
            #captured space cannot be empty
            elif capturedPiece == '  ':
                raise RuntimeError('Cannot capture empty space')

        #try move with all player pieces
        for pieceSpace in self.pieces[pieceType]:
            oldSpace = spaces[pieceSpace].move(spaces, notation, newSpace)
            if oldSpace:
                #set piece at new space
                spaces[newSpace] = spaces[pieceSpace]
                #clear old space
                spaces[oldSpace] = '  '
                #return updated spaces and captured piece type
                return spaces, capturedPiece
        #move is illegal
        return False
    
    def __repr__(self):
        return 'White' if self.color == 'w' else 'Black'
