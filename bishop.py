'''
Bishop subclass
'''
from piece import Piece

class Bishop(Piece):
    note = 'B'
    
    def move(self, spaces, notation):
        #use spaces and notation to determine if move is legal
        #return oldSpace, newSpace, capture
        #capture is either type of piece captured or None 
        pass
