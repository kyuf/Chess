'''
Rook subclass
'''
from piece import CastlePiece

class Rook(CastlePiece):
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
                zip([fO]*len(up), up),
                zip([fO]*len(down), down),
                zip(right, [rO]*len(right)),
                zip(left, [rO]*len(left))
                ]:
            for f, r in filesAndRanks:
                newSpace = f + r
                if spaces[newSpace] == '  ':
                    if self.canMove(spaces, newSpace, player):
                        self.addToMoveset('R{}'.format(newSpace))
                        if len(player.pieces['R']) > 1:
                            for val in [fO, rO, self.space]:
                                self.addToMoveset(
                                        'R{}{}'.format(val, newSpace))
                #pathing blocked by a piece
                else:
                    #capture
                    if spaces[newSpace].color != player.color:
                        if self.canMove(spaces, newSpace, player):
                            self.addToMoveset('Rx{}'.format(newSpace))
                            if len(player.pieces['R']) > 1:
                                for val in [fO, rO, self.space]:
                                    self.addToMoveset(
                                            'R{}x{}'.format(val, newSpace))
                    #terminate current path
                    break