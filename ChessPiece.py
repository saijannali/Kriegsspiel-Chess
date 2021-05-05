#!/usr/bin/python
# -*- coding: utf-8 -*-
import itertools

class PieceFactory():
    def __init__(self):
        self.pieces = {
            "p": Pawn,
            "r": Rook,
            "n": Knight,
            "b": Bishop,
            "k": King,
            "q": Queen,
        }

    def create_piece(self, piece, colour, use_symbol):
        """
        Colour must be explicitly stated with either a 0 or 1, for white or black respectively.
        Piece must be specified with a LOWERCASE letter.
        Use_symbol is bool and decides if a piece is represented by a letter or a symbol.
        """
        return self.pieces[piece](colour=colour, use_symbol=use_symbol)

    def letter_to_symbol(self, letter, colour=0):
        """Get the chess symbol for a piece from it's representing letter"""
        for piece_letter in self.pieces:
            if letter == piece_letter:
                return self.pieces[piece_letter]().symbols[colour]
        return False

class ChessPiece():
    def __init__(self, use_symbol=True, colour=0):
        #pylint: disable=E1101,E0203
        self.owner_id = colour
        self.illegal_moves = [(0,0)]
        self.move_counter = 0
        self.use_symbol = use_symbol
        if use_symbol:
            self.symbol = self.symbols[colour]
        else:
            self.symbol = self.letters[colour]

        #If moves are colour dependant, moves should be a dict
        if isinstance(self._moves, dict): 
            self._moves = self._moves[colour]
        
        if not hasattr(self, "can_jump"):
            self.can_jump = False

        if not hasattr(self, "attack_moves"):
            self.attack_moves = self.moves
        else:
            self.attack_moves = self.attack_moves[colour]
    
    def __str__(self):
        return self.symbol
    
    def __repr__(self):
        return self.symbol

    def is_legal_transform(self, _from, _to, attacking=False):
        """
        Check if a move transform is legal for that piece type.
        Only checks if the move is in the piece's movespace.
        'attacking' refers to if the piece is attempting an attacking move. 
        """
        x_transform = _from[0] - _to[0]
        y_transfrom = _from[1] - _to[1]
        if attacking:
            return (x_transform, y_transfrom) in self.attack_moves
        else:
            return (x_transform, y_transfrom) in self.moves

    def get_moves(self):
        return self._moves

    moves = property(get_moves)
    
            
class Pawn(ChessPiece):
    def __init__(self, *args, **kwargs):
        self.name = "Pawn"
        self.symbols = {0: "♙", 1: chr(9823)}
        self.letters = {0: "P", 1: "p"}
        self._moves = {0: [(0,-1)], 1: [(0,1)]}
        self.attack_moves = {0: [(1,-1), (-1, -1)], 1: [(1, 1), (-1, 1)] }
        super().__init__(*args, **kwargs)

    def get_moves(self):
        #Overwrite moves getter for pawn. Moves change depending on the situation
        if self.move_counter == 0:
            #Can move 2 if it is the pawn's first move
            return self._moves + {0: [(0,-2)], 1: [(0,2)]}[self.owner_id]
        else:
            return self._moves

    def promote(self):
        return Queen(self.use_symbol, self.owner_id)
    
    moves = property(get_moves)
    
class King(ChessPiece):
    def __init__(self, *args, **kwargs):
        self.name = "King"
        self.symbols = {0: "♔", 1: "♚"}
        self.letters = {0: "K", 1: "k"}
        self._moves = [combination for combination in itertools.product([0,-1,1], repeat=2)]
        super().__init__(*args, **kwargs)

class Queen(ChessPiece):
    def __init__(self, *args, **kwargs):
        self.name = "Queen"
        self.symbols = {0: "♕", 1: "♛"}
        self.letters = {0: "Q", 1: "q"}
        up_moves = [(0,i) for i in range(0,8)]
        down_moves = [(0,i) for i in range(-8,0)]
        right_moves = [(i,0) for i in range(0,8)]
        left_moves = [(i,0) for i in range(-8, 0)]
        up_right = [(a,a) for a in range(0,8)]
        down_right = [(a,-a) for a in range(0,8)]
        up_left = [(-a,a) for a in range(0,8)]
        down_left = [(-a,-a) for a in range(0,8)]
        self._moves = list(itertools.chain(up_right, down_right, up_left, down_left, down_moves, up_moves, right_moves, left_moves))

        super().__init__(*args, **kwargs)
        
class Rook(ChessPiece):
    def __init__(self, *args, **kwargs):
        self.name = "Rook"
        self.symbols = {0: "♖", 1: "♜"}
        self.letters = {0: "R", 1: "r"}
        up_moves = [(0,i) for i in range(0,8)]
        down_moves = [(0,i) for i in range(-8,0)]
        right_moves = [(i,0) for i in range(0,8)]
        left_moves = [(i,0) for i in range(-8, 0)]
        self._moves = list(itertools.chain(down_moves, up_moves, right_moves, left_moves))
        super().__init__(*args, **kwargs)

class Knight(ChessPiece):
    def __init__(self, *args, **kwargs):
        self.name = "Knight"
        self.symbols = {0: "♘", 1: "♞"}
        self.letters = {0: "N", 1: "n"}
        self._moves = [(2, 1), (2, -1), (-2,1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
        self.can_jump = True
        super().__init__(*args, **kwargs)

class Bishop(ChessPiece):
    def __init__(self, *args, **kwargs):
        self.name = "Bishop"
        self.symbols = {0: "♗", 1: "♝"}
        self.letters = {0: "B", 1: "b"}
        up_right = [(a,a) for a in range(0,8)]
        down_right = [(a,-a) for a in range(0,8)]
        up_left = [(-a,a) for a in range(0,8)]
        down_left = [(-a,-a) for a in range(0,8)]
        self._moves = list(itertools.chain(up_right, down_right, up_left, down_left))
        super().__init__(*args, **kwargs)
