'''
Queen subclass
'''
from piece import Piece

class Queen(Piece):
    def move(self, spaces, player):
        def getRange(sig, start, end):
            return [chr(i) for i in range(ord(start)+sig, ord(end)+sig, sig)]
        
        fO, rO = self.space[0], self.space[1]

        #set range variables
        up = getRange(1, rO, '8')
        down = getRange(-1, rO, '1')
        right = getRange(1, fO, 'h')
        left = getRange(-1, fO, 'a')

        #horizontal, vertical and diagonal paths
        for filesAndRanks in [
                zip([fO]*len(up), up),
                zip([fO]*len(down), down),
                zip(right, [rO]*len(right)),
                zip(left, [rO]*len(left)),
                zip(right, up),
                zip(left, up),
                zip(right, down),
                zip(left, down)
                ]:
            for f, r in filesAndRanks:
                newSpace = f + r
                if spaces[newSpace] == '  ':
                    if self.canMove(spaces, newSpace, player):
                        self.addToMoveset('Q{}'.format(newSpace))
                        if len(player.pieces['Q']) > 1:
                            for val in [fO, rO, self.space]:
                                self.addToMoveset(
                                        'Q{}{}'.format(val, newSpace))
                #pathing blocked by a piece
                else:
                    #capture
                    if spaces[newSpace].color != player.color:
                        if self.canMove(spaces, newSpace, player):
                            self.addToMoveset('Qx{}'.format(newSpace))
                            if len(player.pieces['Q']) > 1:
                                for val in [fO, rO, self.space]:
                                    self.addToMoveset(
                                            'Q{}x{}'.format(val, newSpace))
                    #terminate current path
                    break
