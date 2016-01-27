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
        #pawn if first letter is lowercase
        if notation[0].lower() == notation[0]:
            pass
        #rook if first letter is R
        elif notation[0] == 'R':
            pass
        #knight if first letter is N
        elif notation[0] == 'N':
            pass
        #bishop if first letter is B
        elif notation[0] == 'B':
            pass
        #queen if first letter is Q
        elif notation[0] == 'Q':
            pass
        #king if first letter is K
        elif notation[0] == 'K':
            pass
        #kcastle if O-O or O-O-O
        elif notation == 'O-O' or notation == 'O-O-O':
            spaces, self.pieces = castle.castle(notation, spaces, self)
        
    
    def __repr__(self):
        return 'White' if self.color == 'w' else 'Black'
