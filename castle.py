'''
Handles castling king side and queen side
'''
def castle(notation, spaces, player):
    r = player.ranks[0]
    kingSpace = 'e' + r
    #select king or queen side rook space
    #O-O is king side
    if notation == 'O-O':
        rookSpace = 'h' + r
        checkIfEmpty = 'fg'
        newKingSpace = 'g' + r
        newRookSpace = 'f' + r
    #O-O-O is queen side
    else:
        rookSpace = 'a' + r
        checkIfEmpty = 'dcb'
        newKingSpace = 'c' + r
        newRookSpace = 'd' + r
        
    #check if king and rook are in correct spaces
    if (kingSpace in player.pieces['K']
            and rookSpace in player.pieces['R']
            #check king and rook have not been moved
            and spaces[kingSpace].canCastle
            and spaces[rookSpace].canCastle):
        #check spaces in between are empty
        for f in checkIfEmpty:
            if spaces[f+r] != '  ':
                #blocking pieces prevent castling
                raise RuntimeError('Castling blocked')
        #check the king is not in check and will not be in check
        #king also cannot castle through check
        for f in 'e' + checkIfEmpty[:2]:
            if spaces[kingSpace].inCheck(spaces, f+r):
                if f == 'e':
                    raise RuntimeError('Cannot castle out of check')
                else:
                    raise RuntimeError('Cannot castle into or through check')
        #castling allowed
        #disable future castle and re-arrange pieces
        spaces[kingSpace].disableCastle()
        spaces[rookSpace].disableCastle()
        spaces[newKingSpace] = spaces[kingSpace]
        spaces[newRookSpace] = spaces[rookSpace]
        spaces[kingSpace] = '  '
        spaces[rookSpace] = '  '
        #update piece spaces
        spaces[newKingSpace].updatePieceSpace(newKingSpace)
        spaces[newRookSpace].updatePieceSpace(newRookSpace)
        #update player piece locations
        player.pieces['K'] = {newKingSpace}
        player.pieces['R'].remove(rookSpace)
        player.pieces['R'].add(newRookSpace)
        return spaces
    else:
        raise RuntimeError('Cannot castle')
