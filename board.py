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
    spaces = {}
    #fill in empty spaces
    for f in 'abcdefgh':
        for r in '3456':
            spaces[f+r] = '  '
        #fill in pawns
        for r, c in {'2': 'w', '7': 'b'}.items():
            spaces[f+r] = Pawn(c, f+r)
    
    #wet, make dry
    for r, c in {'1': 'w', '8': 'b'}.items():
        #fill in rooks
        for f in 'ah':
            spaces[f+r] = Rook(c, f+r)
        #fill in knights
        for f in 'bg':
            spaces[f+r] = Knight(c, f+r)
        #fill in bishops
        for f in 'cf':
            spaces[f+r] = Bishop(c, f+r)
        #fill in queens
        spaces['d'+r] = Queen(c, 'd'+r)
        #fill in kings
        spaces['e'+r] = King(c, 'e'+r)
    
    return spaces

#Takes in dict containing board spaces and generates board
#design of board can be viewed in ref.txt
def generate(spaces):
    os.system('clear')
    fil = '\n    ' + '      %s' * 8 % ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H')
    print(fil)
    print('       ' + '_' * 55)
    for r in '87654321':
        print('      |' * 9)
        print('   %s  ' % r, end='')
        for f in 'ABCDEFGH':
            print('|  %s  ' % spaces[f.lower()+r], end='')
        print('|  %s' % r)
        print('      |' + '______|' * 8)
    print(fil + '\n')
