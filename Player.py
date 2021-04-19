# what the player needs to do:
# take the start state of the board. 
# make special start states for player 1 and player 2. 
# insert number of enemy pieces. 

# function for pawn tries.

# function for random pieces. 
# what denotes random?
# places x number of known pieces in y number of spaces not occupied by player. 
# starting with 4 by 4 with 8 pieces each, this is 
# will starting lineup be known?
# returns list of all possible states. 

# for random player, takes random value out of returned list and makes that move until game end. 
# does not use minimax, because no heuristic involved. 



import random
from board import Board

# this is the intial RandomPlayer class. 
# Elements such as heuristics, minimax, sampling and more are loosely written but not yet implemented. 
class RandomPlayer():
    def __init__(self):
        self.random = random.Random(max_depth)

    def findMove(self, given, enemyNo):
        states = getRandomStates(given, enemyNo)
        return self.random.choice(states)
    
    def getRandomStates(board, enemyNo):
        # takes board featuring player pieces. 
        # For all empty spaces on the board, places any combination of viable pieces for enemy.
        # since only number is known, no restriction on pieces beyond the max of a type a player can have (i.e., won't add 8 pawns)
        # returns list of all random states. 
        # 