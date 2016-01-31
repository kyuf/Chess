'''
Player class contains information of player's pieces and allows moves to be
made.
'''
import castle
import king

class Player:
    #pieces contains dictionary with sets of current positions for each type
    #of piece
    def __init__(self, color):
        self.color = color
        #color used to determine starting ranks and forward pawn direction
        if self.color == 'w':
            self.ranks = '124'
            self.forward = 1
        else:
            self.ranks = '875'
            self.forward = -1
        #add initial pawn positions
        pieces = {}
        pieces['P'] = set()
        for f in 'abcdefgh':
            pieces['P'].add(f+self.ranks[1])
        #add initial rook, knight, bishop, queen, king positions
        r = self.ranks[0]
        pieces['R'] = {'a'+r, 'h'+r}
        pieces['N'] = {'b'+r, 'g'+r}
        pieces['B'] = {'c'+r, 'f'+r}
        pieces['Q'] = {'d'+r}
        pieces['K'] = {'e'+r}
        #store into self
        self.pieces = pieces
    
    #moves follow PGN notation
    def move(self, notation, spaces, opponent):
        #vulnerable pawns can be captured en passant
        #clear any previously vulnerable pawns
        self.vulnerableSpace = None
        
        #castle if O-O or O-O-O
        if notation == 'O-O' or notation == 'O-O-O':
            spaces, self.pieces = castle.castle(notation, spaces, self)
            return spaces, opponent
        
        #determine new space
        if notation[-2] != '=':
            newSpace = notation[-2:]
        else:
            #pawn promotion will put '=X' at end of notation where X is new
            #piece type
            newSpace = notation[-4:-2]
        #check that new space is within the board
        if newSpace[0] not in 'abcdefgh' or newSpace[1] not in '12345678':
            raise RuntimeError('Cannot move outside of board')
        #check for capture
        capturedPiece = spaces[newSpace] if 'x' in notation else None
        
        #cannot capture king or piece of same color
        if capturedPiece:
            #captured space cannot be empty unless en passant
            if capturedPiece == '  ':
                if (opponent.vulnerableSpace == 
                        newSpace[0] + str(int(newSpace[1])-self.forward)):
                    capturedPiece = spaces[opponent.vulnerableSpace]
                else:
                    raise RuntimeError('No piece to capture')
            elif type(capturedPiece) == king.King:
                raise RuntimeError('Cannot capture King')
            elif capturedPiece.color == self.color:
                raise RuntimeError('Cannot capture own piece')
            
        #if not capturing new space cannot be occupied
        else:
            if spaces[newSpace] != '  ':
                raise RuntimeError('Cannot move into occupied space')
        
        #determine piece being moved
        #pawn if first letter is lowercase
        if notation[0] in 'abcdefgh':
            pieceType = 'P'
            #pawns move differently for white and black
            oldSpace = notation[0] + str(int(newSpace[1])-self.forward)
            #check if player has pawn on oldSpace
            if oldSpace in self.pieces['P']:
                #check if capturing files are adjacent
                if (capturedPiece
                        and abs(ord(newSpace[0])-ord(oldSpace[0])) != 1):
                    raise RuntimeError('Capturing pawn files must be adjacent')
            #check if pawn is moving double
            #must be on starting rank and have clear path
            elif not capturedPiece:
                if (notation[0] + self.ranks[1] in self.pieces['P']
                        and spaces[oldSpace] == '  '
                        and notation[-1] == self.ranks[2]):
                    oldSpace = notation[0] + self.ranks[1]
                    #pawn is vulnerable
                    self.vulnerableSpace = newSpace
                else:
                    raise RuntimeError('Pawn move illegal')
        
        #rook, knight, bishop, queen, king if first letter is R, N, B, Q, K
        elif notation[0] in 'RNBQK':
            pieceType = notation[0]
            #try move with all player pieces
            for pieceSpace in self.pieces[pieceType]:
                oldSpace = spaces[pieceSpace].move(spaces, notation, newSpace)
                if oldSpace:
                    break
            if not oldSpace:
                #move is illegal
                raise RuntimeError('Move found to be illegal')
        
        #no piece found
        else:
            raise RuntimeError('Incorrect piece notation')
        
        #remove captured piece from opponent's pieces
        if capturedPiece:
            spaces[capturedPiece.space] = '  '
            opponent.pieces[capturedPiece.note].remove(capturedPiece.space)
        #set piece at new space
        spaces[newSpace] = spaces[oldSpace]
        spaces[newSpace].updatePieceSpace(newSpace)
        #clear old space
        spaces[oldSpace] = '  '
        #update player piece sets
        self.pieces[pieceType].remove(oldSpace)
        self.pieces[pieceType].add(newSpace)
        #return updated spaces and captured piece type
        print(self.vulnerableSpace)
        return spaces, opponent
        
    
    def __repr__(self):
        return 'White' if self.color == 'w' else 'Black'
