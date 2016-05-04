'''
Bishop subclass
'''
from piece import Piece

class Bishop(Piece):
    def move(self, spaces, notation, newSpace):
        #use spaces and notation to determine if move is legal
        fO, rO, fN, rN = self.partitionSpaces(newSpace)
        dx = ord(fN) - ord(fO)
        dy = ord(rN) - ord(rO)
        if abs(dx) != abs(dy):
            return None
        #check spaces in between are empty
        a = abs(dx)
        for i in range(1, a):
            if spaces[chr(ord(fO)+dx//a*i)+chr(ord(rO)+dy//a*i)] != '  ':
                return None
        #return space to use as oldSpace
        return self.space

    

    def newMove(self, spaces, player):
        def getRange(sig, start, end):
            return [chr(i) for i in range(ord(start)+sig, ord(end)+sig, sig)]
        
        fO, rO = self.space[0], self.space[1]

        #set range variables
        up = getRange(1, rO, '8')
        down = getRange(-1, rO, '1')
        right = getRange(1, fO, 'h')
        left = getRange(-1, fO, 'a')

        for filesAndRanks in [
                zip(right, up),
                zip(left, up),
                zip(right, down),
                zip(left, down)
                ]:
            for f, r in filesAndRanks:
                newSpace = f + r
                if spaces[newSpace] == '  ':
                    if self.canMove(spaces, newSpace, player):
                        self.addToMoveset('B{}'.format(newSpace))
                        if player.sameColorBishops(self.space):
                            for val in [fO, rO, self.space]:
                                self.addToMoveset(
                                        'B{}{}'.format(val, newSpace))
                #pathing is blocked by a piece
                else:
                    #cpature
                    if spaces[newSpace].color != player.color:
                        if self.canMove(spaces, newSpace, player):
                            self.addToMoveset('Bx{}'.format(newSpace))
                            if player.sameColorBishops(self.space):
                                for val in [fO, rO, self.space]:
                                    self.addToMoveset(
                                            'B{}x{}'.format(val, newSpace))
                    #terminate current path
                    break
                