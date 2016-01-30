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
    notation = input('%s to play: ' % players[turn])
    
    #check if move is legal

    #returns updated spaces and capture if legal otherwise returns None
    tmp = players[turn].move(notation, spaces)
    if tmp:
        spaces, capturedPiece = tmp
        #remove captured piece from opponent's pieces
        if capturedPiece:
            players[1-turn].pieces[capturedPiece.note].remove(notation[-2:])
    else:
        raise RuntimeError('Illegal move')
    #set to next player's turn
    turn = 1 - turn
    
    #update board
    board.generate(spaces)
    
    #setup error catching
    '''
    #declare re-input for move
    except Exception as e:
        board.generate(spaces)
        print(e)
    '''
    
