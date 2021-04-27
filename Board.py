import Player
# import pieces

# adjusted range to 4 to represent 4x4 board, and changes pieces used to fill in board.
class Board:
    def __init__(self):
        # uses None to establish empty spaces
        self.board = [[None for x in range(3)] for y in range(4)]
        
        # separate boards for white and black. Above is umpire's board, which contains full information.
        # These exist to show to each player, so that the players at no point get access to the other player's board.
     
        # might not need umpire's board, instead use separate white and blackboards and have program check both. work on this later?
        self.whiteBoard = [[None for x in range(3)] for y in range(4)]
        self.blackBoard = [[None for x in range(3)] for y in range(4)]

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

    # returns true if empty, false if not
    # def isEmpty(self,x,y) -> bool:
    def isEmpty(self, x, y):
        return self.board[y][x] == None

    #move input in ['x','y'], return is valid
    # def makeMove(self, move: str) -> bool:
    #     return null

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

    # makeMove returns a number based on the change in pieces. -1 will be read by the player as being an illegal move.
    def makeMove(self, piece, x, y):
        if piece.isValid():
            space = piece.currSpace()
            if not self.board[y][x].isEmpty():
                # alternatively, call whichSide() function for that piece, so self.board[][].whichSide()
                if self.board[y][x] is black:
                    return removePiece(x,y,1)
                else:
                    return removePiece(x,y,0)
            self.board[y][x] = piece
            self.board[space[0]][space[1]] = None
            if self.side == 0:
                self.whiteBoard[y][x] = piece
                self.whiteBoard[space[0]][space[1]] = None
            else:
                self.blackBoard[y][x] = piece
                self.blackBoard[space[0]][space[1]] = None
        return -1
        # todo

    # takes stored current and previous position
    # or will previous position have to be based on a trace? most likely
    # in that case, looks at trace and undoes last move?
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

    # needs work. Does not function, while below code snippet does.
    # except, that below snippet prints the board twice for unknown reasons.
    def printBoard(self):
        for i in range(4):
            for j in range(3):
                print("|" + self.board[i][j], end= "|")
            print("_ _ _ _\n")

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
sample = Board
sample.fillBoard
for i in range(4):
    line = ""
    for j in range(3):
        line = line + "|" + str(i*j) + "|"
    print(line)
    print("_ _ _ _")
sample.printBoard