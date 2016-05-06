'''
King subclass
'''
from piece import CastlePiece

class King(CastlePiece):   
    def inCheck(self, spaces, kingSpace):
        '''
        Return True if King in check else False
        '''
        #helper functions
        def isAdjacent(space):
            '''
            Check if space is adjacent to piece
            '''
            return (abs(ord(self.space[0])-ord(space[0])) <= 1
                    and abs(ord(self.space[1])-ord(space[1])) <= 1)

        def checkCheck(space, attackers):
            '''
            Check if piece is attacking King
            '''
            #if attacking piece is king it must be adjacent
            if space.note == 'K' and not isAdjacent(space.space):
                return False
            elif space.color != self.color and space.note in attackers:
                return True
            return False

        def getRange(sig, start, end):
            return [chr(i) for i in range(ord(start)+sig, ord(end)+sig, sig)]

        #get space coordinate values
        fO, rO = kingSpace[0], kingSpace[1]

        #set range variables
        up = getRange(1, rO, '8')
        down = getRange(-1, rO, '1')
        right = getRange(1, fO, 'h')
        left = getRange(-1, fO, 'a')

        #check for vertical and horizontal attackers
        for filesAndRanks in [
                zip([fO]*len(up), up),
                zip([fO]*len(down), down),
                zip(right, [rO]*len(right)),
                zip(left, [rO]*len(left))
                ]:
            for f, r in filesAndRanks:
                space = spaces[f+r]
                if space != '  ':
                    if checkCheck(space, 'RQK'):
                        return True
                    break

        #check for knight attackers
        for k in [0, 1]:
            for r in [ord(rO)+(2-k), ord(rO)-(2-k)]:
                if r >= ord('1') and r <= ord('8'):
                    for f in [ord(fO)+(1+k), ord(fO)-(1+k)]:
                        if f >= ord('a') and f <= ord('h'):
                            space = spaces[chr(f)+chr(r)]
                            if space != '  ':
                                if checkCheck(space, 'N'):
                                    return True

        #check for diagonal attackers
        #include check for pawn attackers here
        for filesAndRanks in [
                zip(right, up),
                zip(left, up),
                zip(right, down),
                zip(left, down)
                ]:
            for f, r in filesAndRanks:
                space = spaces[f+r]
                if space != '  ':
                    #spaces where pawns need to be considered
                    if ord(r) - ord(rO) == self.forward:
                        attackers = 'PBQK'
                    #no pawns
                    else:
                        attackers = 'BQK'
                    if checkCheck(space, attackers):
                        return True
                    break

        return False

    def move(self, spaces, player):
        fO, rO = self.space[0], self.space[1]
        deltas = [
            (-1, 1), (0, 1), (1, 1), (1, 0),
            (1, -1), (0, -1), (-1, -1), (-1, 0)
        ]
        for df, dr in deltas:
            f = chr(ord(fO)+df)
            r = chr(ord(rO)+dr)
            if f in 'abcdefgh' and r in '12345678':
                newSpace = f + r
                if spaces[newSpace] == '  ':
                    if self.canMove(spaces, newSpace, player):
                        self.addToMoveset('K{}'.format(newSpace))
                #capture
                elif spaces[newSpace].color != player.color:
                    if self.canMove(spaces, newSpace, player):
                        self.addToMoveset('Kx{}'.format(newSpace))