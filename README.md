# Chess Game with Stockfish

This project is a Python program that simulates a chess game where both players make optimal moves using the Stockfish chess engine.

## Files
- `main.py`: Contains the main program logic to run the chess game.
- `stockfish.py`: Defines the `Stockfish` class responsible for interacting with the Stockfish engine.
- `chess_game.py`: Defines the `ChessGame` class representing the chess game state and logic.
- `README.md`: This file providing an overview of the project.

## Usage
To run the chess game simulation, execute `main.py`. The program will continue to make optimal moves for each player until the game is over.

## Implementation Details
- `main.py`: Initializes the Stockfish engine and the chess game. It then alternates between players, using Stockfish to determine the best move for each turn.
- `stockfish.py`: Contains the `Stockfish` class with methods to interact with the Stockfish engine and retrieve the best move based on the current board state.
- `chess_game.py`: Defines the `ChessGame` class with methods to manage the chess game state, including initializing the board, checking game over conditions, getting the current player, making moves, and determining the game result.

## Dependencies
- Python 3.x
- Stockfish chess engine

## Future Improvements
- Implement a graphical user interface for the chess game.
- Allow user input for moves alongside Stockfish's optimal moves.

