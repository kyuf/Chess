'''
Bishop subclass
'''
from piece import Piece

class Bishop(Piece):
    def move(self, spaces, player):
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
                