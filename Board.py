# import Player
# import pieces

# adjusted range to 4 to represent 4x4 board, and changes pieces used to fill in board.
class Board:
    def __init__(self):
        # uses None to establish empty spaces
        self.board = [["  " for x in range(3)] for y in range(4)]
        
        # separate boards for white and black. Above is umpire's board, which contains full information.
        # These exist to show to each player, so that the players at no point get access to the other player's board.
     
        # might not need umpire's board, instead use separate white and blackboards and have program check both. work on this later?
        self.whiteBoard = [["  " for x in range(3)] for y in range(4)]
        self.blackBoard = [["  " for x in range(3)] for y in range(4)]

        # checks last moves made
        self.recentMove = ""
        self.counter = 0
        
        # initializes number of pieces for each side. This can be more accurately done in fillboard, but this is temp solution.
        self.whiteNo = 6
        self.blackNo = 6

        # determines if the game is over. Used as endgame. 
        self.gameOver = False
        
        # 0 is white, 1 is black. This variable is changed after each move. 
        self.side = 0

        #list of all possible moves
        self.possibleMoves =[]

    # checks if the given location is empty
    # returns true if empty, false if not
    def isEmpty(self, x, y):
        return self.board[y][x] == None

    # may be useful for isCheck function
    def getAllValidMoves(self, side):
        return null
        #TODO

    def fillBoard(self):
        # note: for potential larger boards 4x5 and 4x6, the pieces are the same but there is now a gap. 
        # this would mean adjusting the indices for where the pieces are placed on black's side. 
        sides = ["White", "Black"]
        pos = 1

        # fills pawns ****check format
        for x in range(3):
            self.board[pos][x] = "PW" 
            self.whiteBoard[pos][x] = "PW"
        
        pos = 2
        for x in range(3):
            self.board[pos][x] = "PB"
            self.blackBoard[pos][x] = "PB"

        # used shorthand for referring to pieces so that strings are smaller. P is pawn, R is rook, Q is queen, K is king.
        # W at end represents white piece, B means black piece
        pos = 0
        self.board[pos][0] = "RW"
        self.board[pos][1] = "QW"
        self.board[pos][2] = "KW"
        # self.board[pos][3] = "RW"
        self.whiteBoard[pos][0] = "RW"
        self.whiteBoard[pos][1] = "QW"
        self.whiteBoard[pos][2] = "KW"
        # self.whiteBoard[pos][3] = "RW"
        
        pos = 3
        self.board[pos][0] = "RB"
        self.board[pos][1] = "QB"
        self.board[pos][2] = "KB"
        # self.board[pos][3] = "RB"
        self.blackBoard[pos][0] = "RB"
        self.blackBoard[pos][1] = "QB"
        self.blackBoard[pos][2] = "KB"
        # self.blackBoard[pos][3] = "RB"
        # the distinction is made so that when capturing a piece, the player will not attempt to capture its own pieces.

    # makeMove returns a number based on the change in pieces. 
    # needs way to indicate that move is illegal. 

    # return function is important, in that players attempting to make a move only know if the move was valid or not.
    def makeMove(self, piece, x, y):
        if piece.isValid(x, y):
            # gets the current space of the given piece
            space = piece.currSpace()
            # if the space isn't empty, but the move is valid, then captures the other piece.
            if not self.board[y][x].isEmpty():
                # if the piece it lands on is on its own team, the move is invalid.
                if self.board[y][x].whichSide() == piece.whichSide():
                    return False
                # otherwise, captures the piece and moves on. 
                removePiece(x, y, piece.whichSide)
            # places the piece on the space it wants to move to on the umpire board
            self.board[y][x] = piece
            # replaces its current spot with nothing. 
            self.board[space[0]][space[1]] = None
            
            # does the same on for the moving side's board, and returns true to indicate valid move.
            if self.side == 0:
                self.whiteBoard[y][x] = piece
                self.whiteBoard[space[0]][space[1]] = None
                return True
            else:
                self.blackBoard[y][x] = piece
                self.blackBoard[space[0]][space[1]] = None
                return True
        return False

    # takes stored current and previous position
    # or will previous position have to be based on a trace? most likely
    # in that case, looks at trace and undoes last move?
    # trace could consist of each umpire board for each move. undoMove could look at last move from
    # given side and reverse it using current position of piece in both states. Maybe?


    # ignore for time being. only relevant with minimax
    def undoMove(self, piece):
        pass

    # takes coordinates of piece to be removed, and decreases piece counter depending on side that moved. 
    def removePiece(self, x, y, side):
        self.board[y][x] = None
        # side represents the side moving
        if side == 0:
            self.blackBoard[space[0]][space[1]] = None
            self.blackNo -= 1
        else:
            self.whiteBoard[space[0]][space[1]] = None
            self.whiteNo -= 1

    # prints the boards for the umpire and each player side by side.
    def printBoard(self):
        print("White's Board        Black's Board       Umpire's Board")
        for i in range(4):
            line = ""
            line2 = ""
            line3 = ""
            for j in range(3):
                line = line + "|" + str(self.whiteBoard[i][j])
                line2 = line2 + "|" + str(self.blackBoard[i][j])
                line3 = line3 + "|" + str(self.board[i][j])
            print(line + "|         " + line2 + "|          " + line3 + "|          ")

    # occurs when a player has no valid moves left
    def isStaleMate(self, side):
        # algorithm:
        # checks side moving
        # takes remaining pieces of other side
        # checks if all moves are valid. 
        # if false for every one of them, returns true, else false.
        if side == 0:
            pass
        else:   
            pass 
        return None

    def isCheck(self, side):
        # algorithm:
        # takes position of other king
        # for all pieces of moving side, tries to move them to king's spot.
        # if any piece can validly move onto king, isCheck returns true.
        # if all isValid calls for pieces return false, returns false.
        if self.side == 0:
            pass
        else:
            pass
        return None

    def isCheckMate(self, side):
        # algo:
        # this will likely only be called after there is a check
        # tries moving enemy king to all adjacent squares.
        # If none are valid (king's isValid already considers if it enters check)...
        # ...then returns true and game ends with side entered's victory.
        # if a move is valid, returns false. 
        return None

    # something important about the above three functions is that they require a way to access a piece based on side.
    # while it would be possible to scan the relevant one-sided board and return the piece,
    # what is a more efficient way of calling a piece by its associated side? 
    # i.e., we're looking for check, so let's get the enemy king. 
    # or, let's try to move all of this side's pieces. 

    # currently the idea for implementation is having side be an attribute of each piece.
    # from there, scan umpire board for piece of class x, then return it if it has attribute y.
    # inefficient, but currently it is difficult to access a list in O(1) using means other than coordinates. 


    def checkRules(self):
        #check side
        #if white
        if (self.side == 0):
            pass
            #check vertical
            # if()
        # if black
        else:
            pass

# this and above printBoard function are attempts to create a board. 
sample = Board()
sample.fillBoard()
sample.printBoard()