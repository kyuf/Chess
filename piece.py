'''
Superclass for chess pieces
'''
class Piece:
    def __init__(self, color, space):
        #color is either 'w' or 'b'
        self.color = color
        self.space = space
    
    def __repr__(self):
        #self.note defined in subclasses
        return self.color + self.note
    
    #update piece space after moving
    def updatePieceSpace(self, newSpace):
        self.space = newSpace
