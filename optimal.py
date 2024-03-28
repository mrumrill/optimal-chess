# stockfish.py
from stockfish import Stockfish

class Optimal:
    def __init__(self):
        # Initialize Stockfish engine here
        
        self.engine = Stockfish(path=r"C:\Users\mattr\Downloads\stockfish-windows-x86-64\stockfish\stockfish-windows-x86-64")

    def best_move(self):
        # Implement logic to get the best move from Stockfish engine based on the current board state
        best_move = self.engine.get_best_move()
        return best_move
    
    def is_game_over(self):
        # Implement logic to check if the game is over

        if self.best_move() is None:
            return True
        else:
            return False
        
    def make_move(self, move):
        # Implement logic to make a move on the board
        self.engine.make_moves_from_current_position([move])
