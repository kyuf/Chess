'''
Knight subclass
'''
from piece import Piece

class Knight(Piece):
    def move(self, spaces, notation, newSpace):
        #use spaces and notation to determine if move is legal
        fO, rO, fN, rN = self.partitionSpaces(newSpace)
        if (fO == fN or rO == rN
                or abs(ord(fO)-ord(fN)) + abs(ord(rO)-ord(rN)) != 3):
            return None
        else:
            #return space to use as oldSpace
            return self.space

    def newMove(self, spaces, player):
        fO, rO = self.space[0], self.space[1]
        deltas = [
            (-1, 2),
            (1, 2),
            (2, 1),
            (2, -1),
            (1, -2),
            (-1, -2),
            (-2, -1),
            (-2, 1)
        ]
        for df, dr in deltas:
            f = chr(ord(fO)+df)
            r = chr(ord(rO)+dr)
            if f in 'abcdefgh' and r in '12345678':
                newSpace = f + r
                if spaces[newSpace] == '  ':
                    if self.canMove(spaces, newSpace, player):
                        self.addToMoveset(
                            'N{}'.format(newSpace),
                            'N{}{}'.format(fO, newSpace),
                            'N{}{}'.format(rO, newSpace),
                            'N{}{}'.format(self.space, newSpace)
                        )
                #capture
                elif spaces[newSpace].color != player.color:
                    if self.canMove(spaces, newSpace, player):
                        self.addToMoveset(
                            'Nx{}'.format(newSpace),
                            'N{}x{}'.format(fO, newSpace),
                            'N{}x{}'.format(rO, newSpace),
                            'N{}x{}'.format(self.space, newSpace)
                        )
