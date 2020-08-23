# Nine Men's Morris Game
 Nine Men's Morris Game
 The program consists of eight python files.
 There are two phases in the game: Opening and End/Mid Game.
 MiniMaxOpening: Implements the MiniMax algorithm to find the next move in the Opening Phase of game for white.
 MiniMaxGame: Implements the MiniMax algorithm to find the next move in the Mig/End Phase of game for white.
 MiniMaxOpeningBlack:Implements the MiniMax algorithm to find the next move in the Opening Phase of game for black.
 MiniMaxGameBlack:Implements the MiniMax algorithm to find the next move in the Mig/End Phase of game for black.
 MiniMaxOpeningImproved:Implements the MiniMax algorithm with Improvement to find the next move in the Opening Phase of game for white.
 MiniMaxGameImproved:Implements the MiniMax algorithm with Improvement to find the next move in the Mig/End Phase of game for white.
 ABOpening:Implements the AB algorithm to find the next move in the Opening Phase of game for white.
 ABGame:Implements the AB algorithm to find the next move in the Mig/End Phase of game for white.

The program takes three agruments: board1.txt board2.txt 2

board1.txt: input board position
board2.txt: output file location
2: depth upto which the algorithm should run

Examples:

First program: MiniMaxOpening
The first program plays a move in the opening phase of the game. 
For example, the input can be:
(you type:)
board1.txt board2.txt 2
(the program replies:)
Board Position: xxxxxxxxxWxxWxxxBxxxxxx
Positions evaluated by static estimation: 9.
MINIMAX estimate: 9987.
Here it is assumed that the file board1.txt content is:
xxxxxxxxxWxxxxxxBxxxxxx
The file board2.txt is created by the program, and its content is:
xxxxxxxxxWxxWxxxBxxxxxx

Second program: MiniMaxGame
The second program plays in the midgame/endgame phase. 
For example, the input can be:
(you type:)
board3.txt board4.txt 3
(the program replies:)
Board Position: xxxxxxxxWWWxWWxBBBBxxxx.
Positions evaluated by static estimation: 125.
MINIMAX estimate: 9987.
Here it is assumed that the file board3.txt exists and its content is:
xxxxxxxxxxWWxWWxBBBxxxx
The file board4.txt is created by the program, and its content is:
xxxxxxxxWWWxWWxBBBBxxxx