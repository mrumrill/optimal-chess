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


    #def is_game_over(self):
        # Implement logic to check if the game is over
        #optimal = Optimal()

       # if optimal.best_move() is None:
       #     return True
       # else:
       #     return False

    def get_current_player(self):
        return self.current_player

    def get_board(self):
        return self.board

    #def make_move(self, move):
        # Implement logic to make a move on the board
        #optimal = Optimal()
        #optimal.engine.make_moves_from_current_position([move])

    def get_game_result(self):
        # Implement logic to determine the game result (checkmate, stalemate, etc.)
        pass

