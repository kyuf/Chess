'''
Superclass for chess pieces
'''
class Piece:
    def __init__(self, color, space, note):
        #color is either 'w' or 'b'
        self.color = color
        self.space = space
        self.note = note
    
    def __repr__(self):
        #self.note defined in subclasses
        return self.color + self.note
    
    #update piece space after moving
    def updatePieceSpace(self, newSpace):
        self.space = newSpace
    
    #return partition spaces into rank and file for calculations
    def partitionSpaces(self, newSpace):
        #old rank, old file, new rank, new file
        return self.space[1], self.space[0], newSpace[1], newSpace[0]
