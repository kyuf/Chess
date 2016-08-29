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

        pathSet = [
                zip([fO]*len(up), up),
                zip([fO]*len(down), down),
                zip(right, [rO]*len(right)),
                zip(left, [rO]*len(left))
                ]

        self.updateMoveset(spaces, pathSet, player)
