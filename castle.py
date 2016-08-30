'''
Handles castling king side and queen side
'''
def castle(notation, spaces, player):
    r = player.ranks[0]
    kingSpace = 'e' + r
    #select king or queen side rook space
    #O-O is king side
    if notation == 'O-O':
        castleTemplate = 'hgf'
    #O-O-O is queen side
    else:
        castleTemplate = 'abcd'

    rookSpace = castleTemplate[0] + r
    checkIfEmpty = castleTemplate[1:]
    newKingSpace = castleTemplate[-2] + r
    newRookSpace = castleTemplate[-1] + r
        
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

        return (spaces,
                [newKingSpace,newRookSpace],
                [kingSpace, rookSpace],
                'KR')
    else:
        raise RuntimeError('Cannot castle')
