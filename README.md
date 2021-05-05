# B351-Final

### Structure of the Github Repository
This repository contains files used in the final project. Previous files that were worked on but no longer used were deleted, but can be seen in the commit history.
This was done to make the repository easy to read.

### Running the project
In order to run the project, access the Kriegspiel folder and open Kriegspiel.py.

Within this file are settings for the game. In the code block starting on line 239, the players can be set. By default, Player 1 is a human and Player 2 is the Random Player. The subsequent code blocks influence the referee type and gamemode and are set to standard rules.

In an IDE or command line, run Kriegspiel.py and the game will begin.

### Playing the game
With the presets, Player 1 is the human and will be prompted to move. Player input should follow this format: "start_space end_space", where the player input omits the quotes. An example would be "b3 a2" to move white's pawn to capture. If an incorrect input or illegal move is made, the referee will notify the player and ask for a new input.

The referee output on each turn will show the player any of their previous moves and outcomes of those moves, in addition to a board containing only their pieces. This gives the player ample information to understand which pieces are available to move and how each piece is expected to move. 

As in regular chess, the game is played until a checkmate or stalemate is reached, after which the outcome is declared.

### How Files Work
Kriegspiel is used to run the game and set the rules. It also determines starting position, which can be changed on line 10. 
Board is used to create the board for each player, and is used by the referee to determine legality. 
Referee checks player moves and returns an output based on the rules of the game. It also prevents illegal moves from being made. It contains multiple types of referees, but "fair" is the standard used. 
Referee output is used to determine what the referee tells the player. 
CheatAnalyser is used to facilitate referee outputs. 
ChessPiece defines each piece, their movement patterns and importance.
Player contains all player options to be used. This includes RandomPlayer, HumanPlayer, and the basis of a Minimax player. 

Our 4x4 board follows the Silverman 4x4 layout, with 2 rooks, a king, a queen, and 4 pawns for each player. This can be modified to include any combination of pieces, as long as it contains a king. For stability, there should be 8 pieces on each side, restricted to their respective two rows.

