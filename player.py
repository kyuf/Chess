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
        for f in 'ABCDEFGH':
            pieces['P'].append(f+self.ranks[1])
        #add initial rook, knight, bishop, queen, king positions
        r = self.ranks[0]
        pieces['R'] = ['A'+r, 'H'+r]
        pieces['N'] = ['B'+r, 'G'+r]
        pieces['B'] = ['C'+r, 'F'+r]
        pieces['Q'] = ['D'+r]
        pieces['K'] = ['E'+r]
        #store into self
        self.pieces = pieces
    
    #moves follow PGN notation
    def move(self, notation, spaces):
        #determine piece being moved
        #pawn if first letter is lowercase
        if notation[0].lower() == notation[0]:
            pieceType = 'P'
        #rook, knight, bishop, queen, king if first letter is R, N, B, Q, K
        elif notation[0] in 'RNBQK':
            pieceType = notation[0]
        #castle if O-O or O-O-O
        elif notation == 'O-O' or notation == 'O-O-O':
            spaces, self.pieces = castle.castle(notation, spaces, self)
            #no capture is made so return None for second and third
            return spaces, None, None
        #no piece found
        else:
            raise RuntimeError('Incorrect piece notation')
            
        #check if move is legal
        legal = False
        #try move with all player pieces
        for pieceSpace in self.pieces[pieceType]:
            canMove = spaces[pieceSpace].move(spaces, notation)
            if canMove:
                legal = True
                oldSpace, newSpace, capture = canMove
                #set piece at new space
                spaces[newSpace] = spaces[pieceSpace]
                #clear old space
                spaces[oldSpace] = '  '
            #exit loop if legal move is found
            if legal:
                break
        #return updated spaces and capture
        return (spaces, capture, newSpace) if legal else False
    
    def __repr__(self):
        return 'White' if self.color == 'w' else 'Black'
