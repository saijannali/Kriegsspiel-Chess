#pylint: disable=W0614 
from ChessPiece import *
from RefereeOutput import *


"""
Container for referee output objects, with additional arguments.
"""
class SavedOutput():
    def __init__(self, output=None, moves_made=None):
        self.output = output
        self.moves_made = moves_made

class CheatAnalyser():
    def __init__(self):
        self.piece_values = {
            Pawn: 1,
            King: 10000,
            Queen: 9,
            Rook: 5,
            Knight: 3,
            Bishop: 3,
        }
        #A log of all referee outputs, in chronological order
        self.ref_outputs = []

    def get_score_for_board(self, board, player_id):
        """
        Basic utility function.
        Get the score of a given board state.
        Simply sums the scores of all pieces on the board.
        """
        score = 0
        for row in board:
            for piece in row:
                if isinstance(piece, ChessPiece):
                    if piece.owner_id == player_id:
                        score += self.piece_values[type(piece)]
                    else:
                        score -= self.piece_values[type(piece)]

        return score

    def add_ref_output(self, output, moves_made, echo=False):
        """
        Update the latest referee output object in the log with the number of moves made and the output
        given by the referee.
        """ 
        try:
            if not self.ref_outputs[-1].output:
                self.ref_outputs[-1].output = output
                self.ref_outputs[-1].moves_made = moves_made
            else:
                self.create_next_ref_output()
                self.add_ref_output(output, moves_made, echo=echo)
        except IndexError:
            #Triggers if the ref_outputs list is empty.
            #Fix by creating a ref output object before adding to it.
            self.create_next_ref_output()
            self.add_ref_output(output, moves_made, echo=echo)

        if echo:
            print("({}) Saved outputs:".format(self))
            print("  m#\tFrom\tTo\tOutput")
        for o in self.ref_outputs:
            if echo: print("  {}\t{}\t{}\t{}".format(o.moves_made, o.output.from_cell, o.output.to_cell, o.output))

    def create_next_ref_output(self, output=None, moves_made=None):
        """
        Create next SavedOutput object and add it to the log.
        """
        self.ref_outputs.append(SavedOutput(output, moves_made))
