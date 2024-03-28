# main.py

from optimal import Optimal
from chess_game import ChessGame

def main():
    optimal = Optimal()
    chess_game = ChessGame()
    move_list = []
    optimal.engine.set_fen_position(chess_game.board)
    print(optimal.engine.get_board_visual())
    
    while not optimal.is_game_over():
            move_to_make = optimal.best_move()
            optimal.make_move(move_to_make)
            move_list.append(move_to_make)
            

    print(move_list)
    print("Game Over")

if __name__ == "__main__":
    main()
