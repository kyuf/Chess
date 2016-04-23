'''
Main file
'''
import board
import player  

#create initial state of board
spaces = board.initiate()
board.generate(spaces)

#initialize players and turn counter
white = player.Player('w')
black = player.Player('b')

#turn = 0 for white and turn = 1 for black
turn = 0
players = {0: white, 1: black}

#loop for player move inputs
while True:
    try:
        #prompt player for move input
        notation = input('%s to play: ' % players[turn])

        #update spaces and capture if legal otherwise raises error
        spaces, players[1-turn] = players[turn].move(notation, spaces, players[1-turn])

        #set to next player's turn
        turn = 1 - turn
        
        #update board
        board.generate(spaces)
    
    #setup error catching
    #declare re-input for move
    except RuntimeError as e:
        board.generate(spaces)
        print(e)