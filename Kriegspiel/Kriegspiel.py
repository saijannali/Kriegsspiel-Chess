#!/usr/bin/python
# -*- coding: utf-8 -*-
#pylint: disable=W0614,E0102,E0213
from ChessPiece import Pawn, Rook, Knight, Bishop, King, Queen, PieceFactory, ChessPiece
from Board import Board
from Player import *
from Referee import * 
import argparse

DEFAULT_LAYOUT = ["rqkr".upper(), "pppp".upper(), "pppp", "rqkr"] #**********

class Kriegspiel():
    def __init__(self,  player_1, player_2, referee, board_layout=None, use_symbols=True,):
        """
        player_1/2, Player objects
        referee, Referee object
        board_layout, iterable, a board layout to load.
        use_symbols, bool, if pieces should use chess symbols (♔) or letters (K).
        """
        
        self.players = {0: player_1,
                        1: player_2}
        self.use_symbols = use_symbols
        self.last_move = 1 #Who's move it was last
        self.referee = referee
        self.moves_made = 0

        if isinstance(board_layout, Board):
            self.board = board_layout
        else:
            self.board = Board()
            if not board_layout:
                #If no board layout specified, load default starting chess board
                self.load_game(DEFAULT_LAYOUT)
            else:
                self.load_game(board_layout)

    def print_board(self, show_key=True):
        self.board.print_board(show_key=show_key)

    def load_game(self, board_layout):
        """
        Load a game from a matrix in the format:
        ["rnbqkbnr", "pppppppp", "00000000", ... ]
        
        CAPITAL letters are WHITE pieces, lowercase are black.
        """
        piece_layout = []
        for row in board_layout:
            temp_row = []
            for piece in row:
                if str(piece) == "0":
                    temp_piece = 0
                elif piece.istitle():
                    temp_piece = PieceFactory().create_piece(piece=piece.lower(), colour=0, use_symbol=self.use_symbols)
                else:
                    temp_piece = PieceFactory().create_piece(piece=piece, colour=1, use_symbol=self.use_symbols)
                temp_row.append(temp_piece)
            piece_layout.append(temp_row)
        self.board.load_board(piece_layout)
            
    def move_piece(self, _from, _to, player_id):
        """
        Move a piece from one cell to another.
        !! Assumes move is legal!
        """

        moving_piece = self.board.get_piece(_from)
        self.board.move_piece(_from, _to)
        moving_piece.move_counter += 1
        return True

    def do_move(self):
        self.last_move = Kriegspiel.opponent_id(self.last_move)
        current_player_id = self.last_move
        #Player object:
        current_player = self.get_player(self.last_move)

        print("\nIt's {name}'s (ID: {id}) turn to make a move. [Move no {move_no}]".format(name=current_player.name, id=current_player_id, move_no=self.moves_made))

        is_valid_move = False
        while not is_valid_move:
            _from, _to = current_player.do_move(self.get_board_for_player(current_player_id))
            is_valid_move = self.referee.is_move_legal(_from=_from, _to=_to, player_id=self.last_move, board= self.board)
            move_output = self.referee.verify_move(_from=_from, _to=_to, board=self.board, player_id=self.last_move, player_name=self.players[self.last_move].name)

            #If illegal, tell only the player that was making the move:
            if isinstance(move_output[0], IllegalMove):
                current_player.notify(move_output[0], self.moves_made)

        #Loop through the ref outputs and notify the corresponding players
        for output in move_output:
            self.get_player(player_id=output.for_player).notify(output, self.moves_made)

        #When move is valid, perform the move:
        self.move_piece(_from, _to, player_id=self.last_move)

        #If the piece is a pawn and it is reaching the other side of the board, give a promotion:
        if isinstance(self.board.get_piece(_to), Pawn) and _to[1] in [0, 3]:                                #***********
            promoted_piece = self.board.get_piece(_to).promote()
            self.board.add_piece(_to[1], _to[0], promoted_piece)

        self.moves_made += 1

        #Check if the game is over:
        for player_id in [0,1]:
            if self.referee.is_game_over(player_id, self.board):
                print(self.referee.is_game_over(player_id, self.board))
                self.end_game(winner_id=Kriegspiel.opponent_id(player_id))

    def get_player(self, player_id):
        """
        Get a player oject from a given ID.
        """
        return self.players[player_id]

    def get_board_for_player(self, player_id):
        """
        Return the board from a player's perspective.
        Only includes their pieces.
        """
        board_copy = Board()
        for r_no, row in enumerate(self.board.board):
            for c_no, cell in enumerate(row):
                if isinstance(cell, ChessPiece):
                    if cell.owner_id == player_id:
                        board_copy.add_piece(r_no, c_no, cell)

        return board_copy

    def get_pieces_for_player(self, player_id):
        """
        <Generator>
        Get all of the pieces of a given player
        """
        for r_no, row in enumerate(self.board.board):
            for c_no, cell in enumerate(row):
                if isinstance(cell, ChessPiece):
                    if cell.owner_id == player_id:
                        yield cell

    def end_game(self, winner_id):
        """
        End the current game.
        """
        print("Game Over - Player {} won the game".format(winner_id))
        quit()


    def opponent_id(player_id):
        """
        <Static>
        Get the opposing ID of a player.
        """
        return (player_id+1)%2

    def to_letter_coordinates(cell):
        """
        <Static>
        Get the letter coordinates, eg "a5", for a given numerical coordinate (0,6)
        """
        #pylint: disable=E1136
        col_conversion = {b: a for a,b in zip(list("abcd"),[0,1,2,3])}                  #*********
        row_conversion = {b: a for a,b in zip(list("4321"),[0,1,2,3])}                  #*********

        col = col_conversion[cell[0]]
        row = row_conversion[cell[1]]
        return "{}{}".format(col, row)



def pvp(c):
    """Play chess in PVP mode."""
    import os
    #Ensure that correct console clearing command is in use, depending on the OS
    if os.name == "nt":
        clear_cmd = "cls"
    else:
        clear_cmd = "clear"

    while True:
        c.do_move()
        input("@{} Press enter once you've ready to end your turn.".format(c.players[c.last_move].name))
        os.system(clear_cmd)
        input("@{}, press enter when you're ready to take your turn\n>".format(c.players[Kriegspiel.opponent_id(c.last_move)].name))

def debug(c):
    """Play chess with debug mode enabled. Prints out entire board after each move."""
    while True:
        print("Full board:")
        c.print_board(show_key=True)
        c.do_move()

def testing(c):
    """
    Used for testing.
    Add code here and run the game in gamemode "testing" to run this code.
    """
    pass

                    
if __name__ == "__main__":
    #Check if terminal supports chess characters. Use lettering for characters if not.
    use_symbols = True
    try:
        print(King().symbol,)
    except UnicodeEncodeError:
        use_symbols = False

    referees = {
        "fair": Referee(),
        "0": CheatingReferee(cheating_player_id=0),
        "1": CheatingReferee(cheating_player_id=1),
        "laxx": LaxxReferee(),
    }

    player_types = {
        "human": HumanPlayer,
        "random": RandomPlayer,
    }

    game_modes = {
        "pvp": pvp,
        "debug": debug,
        "testing": testing,
    }

    #Parse any passed args:
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--layout_file", help="The filepath of the layout you wish to load.")
    parser.add_argument("-r", "--referee", help="The type of referee.", choices=sorted([x for x in referees]))
    parser.add_argument("-g", "--gamemode", help="The game mode to use.", choices=sorted([x for x in game_modes]))
    parser.add_argument("-p1", "--player1", help="The type of player one.", choices=sorted([x for x in player_types]))
    parser.add_argument("-p2", "--player2", help="The type of player two.", choices=sorted([x for x in player_types]))
    args = parser.parse_args()


    #Set the players
    if args.player1:
        p1 = player_types[args.player1](name="White")
    else:
        p1 = HumanPlayer(name="White") 
    if args.player2:
        p2 = player_types[args.player2](name="Black")
    else:
        p2 = HumanPlayer(name="Black") 

    #Set the layout
    if args.layout_file:
        with open(args.layout_file) as layout_file:
            layout = layout_file.read().splitlines()
    else:
        layout = DEFAULT_LAYOUT

    #Set the type of referee
    if args.referee:
        referee = referees[args.referee]
    else:
        #If referee is not specified, use a fair referee
        referee = referees["fair"]
        
    #Set the game mode
    if args.gamemode:
        gamemode = args.gamemode
    else:
        gamemode = "pvp"

    #Initialise Chess game
    c = Kriegspiel(player_1=p1, player_2=p2, referee=referee, use_symbols=use_symbols, board_layout=layout)

    #Run the game in the chosen gamemode
    game_modes[gamemode](c)
