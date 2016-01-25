'''
Player class contains information of player's pieces and allows moves to be
made.
'''
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
    
    def move(self, notation, space):
        pass
    
    def __repr__(self):
        return 'White' if self.color == 'w' else 'Black'
