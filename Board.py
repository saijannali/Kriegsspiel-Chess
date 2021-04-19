#Board class - general gist, might need to add/remove depending on what we need.


class Board:
    def __init__(self):
        self.board = [[[None for x in range(8)] for y in range(8)] #8x8 grid, each row in a list, 8 lists
        self.recentMove = "";
        self.counter = 0; 

        #returns true if empyt, false if not
        def isEmpty(self,x,y) -> bool:
            return self.board[y][x] == None

        def getAllValidMoves(self, side);
            #TODO

        def fillBoard(self);
            sides = ["White", "Black"]

            pos = 1

            # fills pawns ****check format
            for i in range(2):
                for x in range(8):
                    self.board[pos][x] = "pawn" 
                pos = 6

            pos = 0
            for index in range(2):
                self.board[pos][0] = "rook"
                self.board[pos][1] = "knight"
                self.board[pos][2] = "bishop"
                self.board[pos][3] = "queen"
                self.board[pos][4] = "king"
                self.board[pos][5] = "rook"
                self.board[pos][6] = "bishop"
                self.board[pos][7] = "knight"
                self.board[pos][8] = "rook"
                pos = 7

        def makeMove(self)
        #todo

        def removePiece(self, x,y);
            self.board[y][x] = None

        def printBoard(self):
                


        