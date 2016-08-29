'''
Knight subclass
'''
from piece import Piece

class Knight(Piece):
    def move(self, spaces, player):
        fO, rO = self.space[0], self.space[1]
        deltas = [
            (-1, 2), (1, 2), (2, 1), (2, -1),
            (1, -2), (-1, -2), (-2, -1), (-2, 1)
        ]
        fSet = []
        rSet = []
        for df, dr in deltas:
            f = chr(ord(fO)+df)
            r = chr(ord(rO)+dr)
            if f in 'abcdefgh' and r in '12345678':
                fSet.append(f)
                rSet.append(r)
        pathSet = ([zip(fSet, rSet)])

        self.updateMoveset(spaces, pathSet, player)
