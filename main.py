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

    players[turn].test(spaces)

    #prompt player for move input
    notation = input('{} to play: '.format(players[turn]))

    try:
        #update spaces and capture if legal otherwise raises error
        spaces, players[1-turn] = players[turn].move(
                notation, spaces, players[1-turn])
    #setup error catching
    #declare re-input for move
    except RuntimeError as e:
        board.generate(spaces)
        print(e)
    #if entered move is legal
    else:
        #set to next player's turn
        turn = 1 - turn
        
        #update board
        board.generate(spaces)