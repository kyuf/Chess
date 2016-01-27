'''
Handles castling king side and queen side
'''
def castle(notation, spaces, player):
    r = player.ranks[0]
    kingSpace = 'E' + r
    #select king or queen side rook space
    #O-O is king side
    if notation == 'O-O':
        rookSpace = 'H' + r
        checkIfEmpty = 'FG'
        newKingSpace = 'G' + r
        newRookSpace = 'F' + r
    #O-O-O is queen side
    else:
        rookSpace = 'A' + r
        checkIfEmpty = 'BCD'
        newKingSpace = 'C' + r
        newRookSpace = 'D' + r
        
    #check if king and rook are in correct spaces
    if (player.pieces['K'] == kingSpace
            and rookSpace in player.pieces['R']
            #check king and rook have not been moved
            and spaces[kingSpace].canCastle
            and spaces[rookSpace].canCastle):
        #check spaces in between are empty
        for space in checkIfEmpty:
            if spaces[space+r] != '  ':
                #blocking pieces prevent castling
                raise RuntimeError('Castling blocked')
        #castling allowed
        #disable future castle and re-arrange pieces
        spaces[kingSpace].disableCastle()
        spaces[rookSpace].disableCastle()
        spaces[newKingSpace] = spaces[kingSpace]
        spaces[newRookSpace] = spaces[rookSpace]
        spaces[kingSpace] = '  '
        spaces[rookSpace] = '  '
        #update player piece locations
        player.pieces['K'] = [newKingSpace]
        player.pieces['R'].remove(rookSpace)
        player.pieces['R'].append(newRookSpace)
        return spaces, player.pieces
