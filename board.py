'''
Used to generate chess board based on given piece positions
'''
#import classes for pieces
from pawn import *
from knight import *
from bishop import *
from rook import *
from queen import *
from king import *
import os

#Creates initial board conditions
#board is described using files (vertical) and ranks (horizontal)
def initiate():
    space = {}
    #fill in empty spaces
    for f in 'ABCDEFGH':
        for r in '3456':
            space[f+r] = '  '
        #fill in pawns
        for r, c in {'2': 'w', '7': 'b'}.items():
            space[f+r] = Pawn(c, f+r)
    
    #wet
    for r, c in {'1': 'w', '8': 'b'}.items():
        #fill in rooks
        for f in 'AH':
            space[f+r] = Rook(c, f+r)
        #fill in knights
        for f in 'BG':
            space[f+r] = Knight(c, f+r)
        #fill in bishops
        for f in 'CF':
            space[f+r] = Bishop(c, f+r)
        #fill in queens
        space['D'+r] = Queen(c, f+r)
        #fill in kings
        space['E'+r] = King(c, f+r)
    
    return space

#Takes in dict containing board spaces and generates board
#design of board can be viewed in ref.txt
def generate(space):
    os.system('clear')
    fil = '\n    ' + '      %s' * 8 % ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H')
    print(fil)
    print('       ' + '_' * 55)
    for r in '87654321':
        print('      |' * 9)
        print('   %s  ' % r, end='')
        for f in 'ABCDEFGH':
            print('|  %s  ' % space[f+r], end='')
        print('|  %s' % r)
        print('      |' + '______|' * 8)
    print(fil)
