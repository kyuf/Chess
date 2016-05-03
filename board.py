'''
Used to generate chess board based on given piece positions
'''
import os

#import classes for pieces
from pawn import Pawn
from knight import Knight
from bishop import Bishop
from rook import Rook
from queen import Queen
from king import King


def initiate():
    '''
    Creates initial board conditions and returns as spaces dictionary
    '''
    spaces = {}
    #fill in empty spaces
    for f in 'abcdefgh':
        for r in '3456':
            spaces[f+r] = '  '
        #fill in pawns
        for r, c in {'2': 'w', '7': 'b'}.items():
            spaces[f+r] = Pawn(c, f+r, 'P')
    
    #wet, make dry
    for r, c in {'1': 'w', '8': 'b'}.items():
        #fill in rooks
        for f in 'ah':
            spaces[f+r] = Rook(c, f+r, 'R')
        #fill in knights
        for f in 'bg':
            spaces[f+r] = Knight(c, f+r, 'N')
        #fill in bishops
        for f in 'cf':
            spaces[f+r] = Bishop(c, f+r, 'B')
        #fill in queens
        spaces['d'+r] = Queen(c, 'd'+r, 'Q')
        #fill in kings
        spaces['e'+r] = King(c, 'e'+r, 'K')
    
    return spaces


def generate(spaces):
    '''
    Draws the current board arrangement based on spaces input

    See ref.txt for design of the board
    '''
    os.system('clear')
    fil = '\n' + (' '*6).join(list('ABCDEFGH')).rjust(60)
    print(fil)
    print(('_'*55).rjust(62))
    for r in '87654321':
        print('      |' * 9)
        print('   {}  '.format(r), end='')
        for f in 'ABCDEFGH':
            print('|  {}  '.format(spaces[f.lower()+r]), end='')
        print('|  {}'.format(r))
        print('      |' + '______|' * 8)
    print(fil + '\n')
