# chess_game.py
from optimal import Optimal

class ChessGame:
    def __init__(self):
        # Initialize the chess game with starting board state and player turn
        self.board = self.user_input_board()

    
    def user_input_board(self):
        # Prompt user to input the chess board and current player's turn
        board = input("Enter the chess board configuration: ")
        
        return board

    def get_current_player(self):
        return self.current_player

    def get_board(self):
        return self.board

