'''
Queen subclass
'''
from piece import Piece

class Queen(Piece):
    def move(self, spaces, notation, newSpace):
        #use spaces and notation to determine if move is legal
        fO, rO, fN, rN = self.partitionSpaces(newSpace)
        dx = ord(fN) - ord(fO)
        dy = ord(rN) - ord(rO)
        #check if diagonal
        if abs(dx) == abs(dy):
            #check spaces in between are empty
            a = abs(dx)
            for i in range(1, a):
                if spaces[chr(ord(fO)+dx//a*i)+chr(ord(rO)+dy//a*i)] != '  ':
                    return None
        #if not diagonal check horizontal/vertical
        #moving vertically
        elif fO == fN:
            #check if spaces in between are empty
            for i in range(1, abs(dy)):
                if spaces[fO+chr(ord(rO)+dy//abs(dy)*i)] != '  ':
                    return None
        #moving horizontally
        elif rO == rN:
            #check if spaces in between are empty
            for i in range(1, abs(dx)):
                if spaces[chr(ord(fO)+dx//abs(dx)*i)+rO] != '  ':
                    return None
        else:
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

        #horizontal and vertical paths
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

        #diagonal paths
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
                        self.addToMoveset('Q{}'.format(newSpace))
                        if len(player.pieces['Q']) > 1:
                            for val in [fO, rO, self.space]:
                                self.addToMoveset(
                                        'Q{}{}'.format(val, newSpace))
                #pathing is blocked by a piece
                else:
                    #cpature
                    if spaces[newSpace].color != player.color:
                        if self.canMove(spaces, newSpace, player):
                            self.addToMoveset('Qx{}'.format(newSpace))
                            if len(player.pieces['Q']) > 1:
                                for val in [fO, rO, self.space]:
                                    self.addToMoveset(
                                            'Q{}x{}'.format(val, newSpace))
                    #terminate current path
                    break