'''
Main file
'''
import board
import player
import os

#create initial state of board
os.system('clear')
space = board.initiate()
board.generate(space)

#initialize players
white = player.Player('w')
black = player.Player('b')
