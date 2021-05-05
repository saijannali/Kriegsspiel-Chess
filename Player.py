import itertools
from ChessPiece import ChessPiece
import random
from CheatAnalyser import CheatAnalyser
from Referee import Referee

class Player():
    def __init__(self, name=None):
        self.name = name


    # Heuristic is determined by whether the player wins, or makes notable gains.
    
    # Win condition: game over in favor of the player

    # Favorable outcomes: 
    #   - Given piece captures a piece
    #       - This is a greedy approach, but enemy piece count is the most reliable metric to measure progress. 
    #       - As opposed to standard chess, the player does not know enemy pieces, so value of capture cannot influence decision.
    #       - This needs to be done without putting oneself in check, which the program will prevent anyways.  
    #   - Gets out of check, which is a given for the game's rules.
    #       - Essentially, the given move should be legal and get as much as possible.

    def heuristic(self, board):
        # on losing game over:
        if Referee.is_game_over(self.name, board):
            return 0
        #checking which player is the opponent
        name = ""
        if self.name == "White":
            name = "Black"
        if self.name == "Black":
            name = "White"
        # on winning game over:
        if Referee.is_game_over(name, board):
            return 200

        # non-game over state:

        # based on player, returns number of enemy pieces left. 
        # The fewer pieces left, the better the score
        if self.name == "White":
            return 10 - board.p2piececount
        if self.name == "Black":
            return 10 - board.p1piececount

    def do_move(self, board):
        """
        Choose a move and return it in the form (from, to) where
        from and to are coordinates on the board.
        """
        raise NotImplementedError("do_move method not implemented for Player: {}".format(self))

    def notify(self, ref_output=None, moves_made=None):
        """
        Player recieves output from the referee in the form of a RefereeOutput object.
        """
        pass

class HumanPlayer(Player):
    def __init__(self, *args, **kwargs):
        self.analyser = CheatAnalyser()
        super().__init__(*args, **kwargs)

    def do_move(self, board):
        print(board.sideboard)
        print("History of referee outputs:")
        print("  m#\tFrom\tTo\tOutput")
        for o in self.analyser.ref_outputs:
            print("  {}\t{}\t{}\t{}".format(o.moves_made, o.output.from_cell, o.output.to_cell, o.output))
        board.print_board(show_key=True)
        col_conversion = {a: b for a,b in zip(list("abcd"),[0,1,2,3])}                                  #************
        row_conversion = {a: b for a,b in zip(list("4321"),[0,1,2,3])}                                  #************
        in_string = input(">")
        #Handle user input and potential errors if the format is incorrect:
        try:
            _from, _to = in_string.split(" ")
        except ValueError:
            print("Invalid input!")
            print("\tMust be in format: [from_location] [to_location] (e.g 'a2 a3')")
            return self.do_move(board)

        try:
            #Convert user input to numerical coordinates. a7 -> (0,1); a6 -> (0,2)...
            from_cell = (col_conversion[_from[0]], row_conversion[_from[1]])
            to_cell = (col_conversion[_to[0]], row_conversion[_to[1]])
        except KeyError:
            print("Invalid move coordinates.")
            print("\tMust be in range a1-h7")
            return self.do_move(board)
            
        return (from_cell, to_cell)

    """
    Override notify function.
    Pass the referee output to the cheat analyser
    """
    def notify(self, ref_output, moves_made):
        super().notify(ref_output, moves_made)
        self.analyser.add_ref_output(ref_output, moves_made)

# random player that replaces the old code's class. 
class RandomPlayer(Player):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # what defines a random move?
    #   - takes a random piece
    #   - considers what that piece is, gets all moves based on piece
    #   - picks any random move. if invalid, removes it from list and picks another. 
    #   - if this move is deemed illegal by the referee, do_move is called again

    def do_move(self, board):
        """
        sideboard is the dictionary of the pieces on the board and their current locations.
        remove the comment on the below line to see. 
        This and below lines are useful for testing, but are cheating if playing. 
        """
        # print(board.sideboard)

        """
        shows the player's board each attempted move.
        remove comment for clarity on the random player's position, but note that it will print multiple times each AI turn.
        """
        # board.print_board(show_key=True)


        # a list of each piece available, which will be taken from the dictionary.
        keyslist = []

        # loops through dictionary of player's pieces rather than all 16 spaces of the board.
        # this is intended to take less time, especially when there are multiple failed attempts.
        for i in board.sideboard:
            keyslist.append(i)

        # from the available pieces, takes a random one.
        chosenpiece = keyslist[random.randint(0, len(keyslist)-1)]

        # gets the location of the chosen piece, and uses its coordinates to get a start location.
        current = board.sideboard[chosenpiece]
        start = (current[0], current[1])

        # gets a list of all moves for the piece and chooses one at random.
        moves = chosenpiece.get_moves()
        moveindex = random.randint(0, len(moves)-1)
        end = moves[moveindex]

        # checks if the move is inbounds, rerolls until it is.
        # this effectively locks in the piece to be used, unless that piece cannot be used at all.
        while (start[0]-end[0] > 3 or start[0]-end[0] < 0 or start[1]-end[1] > 3 or start[1]-end[1] < 0):
            moves.remove(end)
            moveindex = random.randint(0, len(moves)-1)
            end = moves[moveindex]

        # once a valid move is found, the endpoint is set.
        end = (start[0]-end[0], start[1]-end[1])
        
        """
        The below comments can be used in testing to see what the ai ultimately picked as its move.
        """
        # print("Start:" + str(start))
        # print("End:" + str(end))

        # returns the start and end locations the player wants to do. 
        return (start, end)



class mmPlayer(Player):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.player = Player
    
    # due to restrictions on what do_move function calls want, do_move calls a helper function that performs minimax
    def do_move(self, board):
        start = self.mini(board, 2)[2]
        end = self.mini(board, 2)[1]
        return (start, end)

    # complications with code prevent this from working
    def mini(self, board, depth):
        if depth == 0 or Referee.is_game_over(Referee, self.player, board):
            return self.heuristic(board)

        # player 1's move
        if self.player == "White":
            bestMove = 0
            bestValue = -math.inf
            start = 0
            for piece in board.sideboard:
                movelist = piece.get_moves
                # currently judges the scores of random moves and has no depth
                move = board.makeMove(movelist[random.randint(0, len(movelist)-1)])
                score = self.mini(move, depth-1)
                if score >= bestValue:
                    bestValue = score
                    start = board.sideboard[piece]
                    end = move
            return (bestValue, end, piece)

        # player 2's move; with the current presets, the AI is always player 2.
        else:
            bestMove = 0
            bestValue = math.inf
            start = 0
            for piece in board.sideboard:
                movelist = piece.get_moves
                move = board.makeMove(movelist[random.randint(0, len(movelist)-1)])
                score = self.mini(move, depth-1)
                if score <= bestValue:
                    bestValue = score
                    start = board.sideboard[piece]
                    end = move
            return (bestValue, end, piece)