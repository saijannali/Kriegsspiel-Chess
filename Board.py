#Board class - general gist, might need to add/remove depending on what we need.


# adjusted range to 4 to represent 4x4 board, and changes pieces used to fill in board.
class Board:
    def __init__(self):
        # uses None to establish empty spaces
        self.board = [[None for x in range(4)] for y in range(4)]
        
        # separate boards for white and black. Above is umpire's board, which contains full information.
        # These exist to show to each player, so that the players at no point get access to the other player's board.
     
        # might not need umpire's board, instead use separate white and blackboards and have program check both. work on this later?
        self.whiteBoard = [[None for x in range(4)] for y in range(4)]
        self.blackBoard = [[None for x in range(4)] for y in range(4)]

        # checks last moves made
        self.recentMove = ""
        self.counter = 0
        
        # initializes number of pieces for each side. This can be more accurately done in fillboard, but this is temp solution.
        self.whiteNo = 8
        self.blackNo = 8

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
    def makeMove(self, move: str) -> bool:



    def getAllValidMoves(self, side):
        return null
        #TODO

    def fillBoard(self):
        # note: for potential larger boards 4x5 and 4x6, the pieces are the same but there is now a gap. 
        # this would mean adjusting the indices for where the pieces are placed on black's side. 
        sides = ["White", "Black"]
        pos = 1

        # fills pawns ****check format
        for x in range(4):
            self.board[pos][x] = "PW" 
            self.whiteBoard[pos][x] = "PW"
        
        pos = 2
        for x in range(4):
            self.board[pos][x] = "PB"
            self.blackBoard[pos][x] = "PB"

        # used shorthand for referring to pieces so that strings are smaller. P is pawn, R is rook, Q is queen, K is king.
        # W at end represents white piece, B means black piece
        pos = 0
        self.board[pos][0] = "RW"
        self.board[pos][1] = "QW"
        self.board[pos][2] = "KW"
        self.board[pos][3] = "RW"
        self.whiteBoard[pos][0] = "RW"
        self.whiteBoard[pos][1] = "QW"
        self.whiteBoard[pos][2] = "KW"
        self.whiteBoard[pos][3] = "RW"
        
        pos = 3
        self.board[pos][0] = "RB"
        self.board[pos][1] = "QB"
        self.board[pos][2] = "KB"
        self.board[pos][3] = "RB"
        self.blackBoard[pos][0] = "RB"
        self.blackBoard[pos][1] = "QB"
        self.blackBoard[pos][2] = "KB"
        self.blackBoard[pos][3] = "RB"
        # the distinction is made so that when capturing a piece, the player will not attempt to capture its own pieces.

    def makeMove(self):
        return null
        # todo

    # takes coordinates of piece to be removed, and decreases piece counter depending on side that moved. 
    def removePiece(self, x, y):
        self.board[y][x] = None
        if side == 0:
            self.blackNo -= 1
        else:
            self.whiteNo -= 1

    def printBoard(self):
        return None

    def isStaleMate(self):
        return None
    def isCheck(self):
        if self.side == 0:
            
        else:

        return None
    def isCheckMate(self):
        return None
    def checkRules(self):
        #check side
        #if white
        if (self.side == 0):
            #check vertical
            if()
        # if black
        else:

for i in range(4): print(i)
sample = Board()
sample.fillBoard()
print(sample)
for i in range(4):
    for j in range(4):
        print(sample.board[i][j])
    print("row finished \n")