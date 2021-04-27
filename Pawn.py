class Pawn:
    def __init__(self,side,board,x,y):
        self.attemptExists = False

    #Input: move = [x,y] []
    #       curr_pawn = [x,y]
    #returns bool
    def isValidMove(self, curr_pawn, move):
        #check all possible moves
        #check if within board:
        if curr_pawn == self.board[move[0]][move[1]]:
            pass
        # checks if the pawn is on the left side of the board. 
        if curr_pawn[1] == 0:
            xDist = move[1]-curr_pawn[1]
            yDist = move[0]-curr_pawn[0]
        if curr_pawn[1] == 3:
            pass
        # white left pawn  = curr_pawn[0] = 1, curr_pawn[1] = 0 
        
        if (self.board[3][1]):
            pass
        return None

    def sendMoveCoord(self,side,board,x,y):
        return None


    