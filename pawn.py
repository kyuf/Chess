'''
Pawn subclass
'''
from piece import Piece

class Pawn(Piece):
    note = 'P'
    hasNotMoved = True
    
    def move(self, spaces, notation, newSpace):
        #use spaces and notation to determine if move is legal
        #return oldSpace if able to move else None
        
        #pawns move differently for white and black
        forward = 1 if self.color == 'w' else -1
        
        #pawns move differently if capturing
        if 'x' in notation:
            pass
        else:
            #pawn must be in same column and newSpace must be empty
            #be careful with case sensitivity
            if self.space[0] != newSpace[0] or spaces[newSpace] != '  ':
                return None
            #pawn can move 1 space if it has moved before
            diff = int(newSpace[1]) - int(self.space[1])
            if diff == forward:
                self.hasNotMoved = False
                return self.space
            #pawn can move 2 space if it hasn't moved before
            elif diff == forward * 2 and self.hasNotMoved:
                #check if middle space is occupied
                if spaces[self.space[0]+str(int(newSpace[1])-forward)] != '  ':
                    return None
                self.hasNotMoved = False
                return self.space
    
    def promote(self, pick):
        #method to promote pawn to new piece
        pass
