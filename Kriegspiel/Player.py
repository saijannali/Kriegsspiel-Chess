import itertools
from ChessPiece import ChessPiece
import random
from CheatAnalyser import CheatAnalyser

class Player():
    def __init__(self, name=None):
        self.name = name

    # what are win conditions?
    # game over in favor of player
    # what about favorable positions? 
    # give piece captures certain scores
    # depth? make it on init, since function is difficult to take different bounds in. 
    # except the player cannot know which piece they captured. 
    # count by number of captures?

    # ******
    def heuristic(self, board):
    # on losing game over
        if board.is_game_over:
            pass
    # on winning game over

    # non-game over states

    # 

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
        self.player = Player


    # what defines a random move?
    # takes a random piece
    # considers what that piece is, gets all spaces based on movement
    # picks any random space. if invalid, removes it from list and picks another. 
    # does that mean list is global variable?
    # should makeMove insert list, so that recursion can have it removed?
    # second option better

    # alternatively, pick different piece and move combo. 
    # a move is a starting position and end position. 
    # output is from cell, end cell
    # should try to avoid hell no moves at all costs.
    # so randomly pick piece, get list of moves from that, pick randomly from list of moves. 
    



    # Note: this function was written after the old RandomPlayer was discarded.
    # name is preserved due to function using do_move for all players
    def do_move(self, board):
        # dictionary of the pieces on the board and a list of their types.
        print(board.sideboard)
        # pieces = {}
        # piecetype = []
        # board.print_board(show_key=True)
        # have get all pieces for side function to call here instead of loop?

        # (the below comment is for later)
        # this function, tied with self.white or self.black in Board, allows the ai to access its pieces faster than
        # the previous implementation, which scanned the entire board for each attempted move. 
        # for i in range(0,4):
        #     for j in range(0,4):
        #         if not board.cell_is_free((j, i)):
        #             pieces[board.get_piece((j, i))] = (j, i) 
        #             piecetype.append(board.get_piece((j,i)))
        keyslist = []
        # this aims to reduce complexity. 
        # instead of looping through all 16 spaces every ai move,
        # it only loops through the number of pieces the player has each attempt.
        # this hopefully takes less time, especially when there are multiple failed moves.
        for i in board.sideboard:
            keyslist.append(i)
        chosenpiece = keyslist[random.randint(0, len(keyslist)-1)]
        current = board.sideboard[chosenpiece]
        start = (current[0], current[1])
        # this only gets the type of piece
        # gets the type of piece based on what is available
        # piece = piecetype[random.randint(0, len(pieces)-1)]
        # gets the current position of the randomly selected piece.
        # start = pieces.get(piece)

        # gets a list of all moves from the piece. 
        # adjust so that only valid moves are available. 
        moves = chosenpiece.get_moves()
        moveindex = random.randint(0, len(moves)-1)
        end = moves[moveindex]
        end = (start[0]-end[0]%4, start[1]-end[1]%4)
        print("start:" + str(start))
        print("end:" + str(end))
        # currently works after some attempts, but ref now returns both sides moves to p1
        # why is it doing that?
        return (start, end)

# start of minimax player. not yet implemented.
class mmPlayer(Player):
    def __init__(self, *args, **kwargs):
        self.analyser = CheatAnalyser()
        super().__init__(*args, **kwargs)
        self.player = Player
    
    # will complete later
    # as minimax, it will be structured about the same as a4's player
    def do_move(self, board):
        # check how else player name can be derived
        if player.name == p1:
            bestMove = 0
            bestValue = -math.inf
            start = 0
            for piece in board.sideboard:
                movelist = piece.get_moves
                # currently judges the scores of random moves
                # and has no depth
                move = board.makeMove(movelist[random.randint(0, len(movelist)-1)])
                score = self.heuristic(board)
                if score >= bestValue:
                    bestValue = score
                    start = board.sideboard[piece]
                    end = move
            return (start, end)

        else:
            bestMove = 0
            bestValue = -math.inf
            start = 0
            for piece in board.sideboard:
                movelist = piece.get_moves
                move = board.makeMove(movelist[random.randint(0, len(movelist)-1)])
                score = self.heuristic(board)
                if score >= bestValue:
                    bestValue = score
                    start = board.sideboard[piece]
                    end = move
            return (start, end)