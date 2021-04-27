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


# big inspiration for this code was the player.py from assignment A4. 
import random
# from Board import Board
# import pieces

# this is the intial RandomPlayer class. 
# Elements such as heuristics, minimax, sampling and more are loosely written but not yet implemented. 
class RandomPlayer():
    def __init__(self):
        self.random = random.Random()

    def findMove(self, given, enemyNo):
        # states = given.getRandomStates(enemyNo)
        # pick = self.random.choice(states)
        # define what pieces is here
        return None

# minimax will be stored here. Monte carlo sampling will likely be implemented as modification to this minimax. 