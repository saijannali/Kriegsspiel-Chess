class Board():
    def __init__(self, size=4, *args, **kwargs):        #*****
        self.board = [[0 for x in range(size)] for y in range(size)]
        # sideboard is for the use of the ai player. 
        # by establishing the location of every piece the player has, the entire board won't need to be scanned...
        # ...in order for an ai player to establish what the available pieces are.
        self.sideboard = {}     #*****

        # for use in the heuristic and random board creation
        self.p1piececount = 8
        self.p2piececount = 8

    def add_piece(self, loc_x, loc_y, piece):
        """
        Add any object to the board at an x, y position.
        Any object in that cell gets replaced with no check./
        """
        self.board[loc_x][loc_y] = piece
        # ideally allows for pieces to be added to/updated in the dictionary as each move passes
        # not throughly tested enough for correctness 
        self.sideboard[piece] = [loc_x, loc_y]      #*****

    def get_piece(self, loc):
        #Return the contents of a cell, given it's location
        return self.board[loc[1]][loc[0]]

    def get_owner_of_piece(self, loc):
        #Return the owner id of the piece in a given cell location
        return self.board[loc[1]][loc[0]].owner_id

    def cell_is_free(self, loc):
        #Is a cell free (not occupied)?
        return self.board[loc[1]][loc[0]] == 0
    
    def move_piece(self, _from, to, replace_from_with=0):
        """
        Move a piece from one cell to another.
        "From" cell can be replaced with anything. Replaced by 0 by default.
        "To" cell gets replaced by the "from" contents.
        No checks are made as to whether the move is legal.
        """
        print("MOVE FUNCTION")
        print(to, _from)
        self.board[to[1]][to[0]] = self.board[_from[1]][_from[0]]
        self.board[_from[1]][_from[0]] = replace_from_with

    def get_random_states(self, player):
        # pseudocode to attempt to replicate the idea

        # 
        pass


    def print_board(self, show_key=False):
        """
        Output the board to the console.
        show_key is bool and decides if a key (a-h, 1-8) is shown on the x and y axis.
        """
        for row_label, row in zip(list("4321"), self.board):        #********
            print(row_label, end=" | ")
            for cell in row:
                if cell == 0:
                    cell = "_"
                print("{} ".format(cell), end="")
            print("")
        print("    a b c d")                                                #********

    def load_board(self, board): 
        """
        Load a board from a matrix in the format:
        ["rnbqkbnr", "pppppppp", "00000000", ... ]
        """
        if isinstance(board, Board):
            board = board.board

        for row_no, row in enumerate(board):
            for cell_no, cell in enumerate(row):
                self.add_piece(row_no, cell_no, cell)

    def save_board(self):
        """
        Get the current gameboard as a list in the format:
        ["rnbqkbnr", "pppppppp", "00000000", ... ]
        TODO: Test if this actually works
        """
        piece_layout = []
        for row in self.board:
            temp_row = []
            for piece in row:
                if hasattr(piece, "letter"):
                    temp_row.append(piece.letter)
                    print(piece.letter)
                else:
                    temp_row.append(piece)
            piece_layout.append(temp_row)
        return piece_layout

