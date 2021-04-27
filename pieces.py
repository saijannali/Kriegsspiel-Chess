import Board

class Pieces:
    # https://github.com/Dirk94/ChessAI/blob/master/pieces.py
    def __init__(self, row, column, side, curr_piece, piece_value):
        self.row = row
        self.column = column
        self.side = side
        self.curr_piece = curr_piece
        self.piece_value = piece_value


    def horizontalMoves(self, board):
        moves = []
        for i in range(1, 4 - self.row):
            if ("is in range"):
                pass

class King(Pieces):
    curr_piece = "K"
    piece_value = 20000
    super(King, self).__init__(row, column, side, King.curr_piece, King.piece_value)    
    # get horizontal and diagonal moves
    # apply horizontal to queen and rook
    # apply diagonal to queen; don't create diagonal function, instead just implement it in queen?
    # pawn can move forward two spaces if first turn, one space all others
    # king can move all around one space

    def moves(self):
        pass

    def isValid(self):
        pass

    def currSpace(self):
        pass

    def lastSpace(self):
        pass