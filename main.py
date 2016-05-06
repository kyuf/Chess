'''
Main file
'''
import board
import player  

def game():
    #create initial state of board
    spaces = board.initiate()
    board.generate(spaces)

    #initialize players and turn counter
    white = player.Player('w')
    black = player.Player('b')

    #turn = 0 for white and turn = 1 for black
    turn = 0
    players = {0: white, 1: black}

    #loop to alternate player turns
    while True:
        #get available moves
        players[turn].getMoveset(spaces)
        # print(players[turn].moveset)
        if isGameOver(players[turn], players[1-turn], spaces):
            input('Press enter to exit..')
            break

        needInput = True

        #loop until valid input
        while needInput:
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
                needInput = False
                #set to next player's turn
                turn = 1 - turn
                #update board
                board.generate(spaces)

def isGameOver(player, opponent, spaces):
    if not player.moveset:
        for kingSpace in player.pieces['K']:
            if spaces[kingSpace].inCheck(spaces, kingSpace):
                print('Checkmate! {} wins!'.format(opponent))
            else:
                print('Stalemate!')
        return True
    return False

if __name__ == '__main__':
    game()