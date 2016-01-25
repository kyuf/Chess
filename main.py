'''
Main file
'''
import board
import player  

#create initial state of board
space = board.initiate()
board.generate(space)

#initialize players and turn counter
white = player.Player('w')
black = player.Player('b')

#turn = 0 for white and turn = 1 for black
turn = 0
players = {0: white, 1: black}

#loop for player move inputs
while True:
    notation = input('%s to play: ' % players[turn])
    
    #check if move is legal
    try:
        players[turn].move(notation, space)
        #set to next player's turn
        turn = 1 - turn
        
        #update board
        board.generate(space)
    
    #declare re-input for move
    except:
        board.generate(space)
        print('Illegal move')
    
