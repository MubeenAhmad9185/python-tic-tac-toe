# Tic-Tac-Toe Game

A simple command-line implementation of the classic Tic-Tac-Toe game written in Python. Two players can take turns to play the game and compete to win or tie.

## Features

- Supports two players (`X` and `O`).
- Detects winners and ties.
- Prevents invalid moves (e.g., already occupied cells or out-of-bounds inputs).
- Fully interactive, with user inputs for each move.

## How to Play

1. Run the Python script.
2. Players take turns entering their desired row and column (0, 1, or 2) to place their mark (`X` or `O`).
3. The game ends when a player wins or all spots are filled (tie).

### Example Gameplay
 | | 
-----
 | | 
-----
 | | 

Player X enter row (0, 1, 2): 0  
Player X enter column (0, 1, 2): 0  
X| | 
-----
 | | 
-----
 | | 

Player O enter row (0, 1, 2): 1  
Player O enter column (0, 1, 2): 1  
X| | 
-----
 |O| 
-----
 | | 

Player X enter row (0, 1, 2): 0  
Player X enter column (0, 1, 2): 1  
X|X| 
-----
 |O| 
-----
 | | 
