import time
import art
import logic

def play_game():
    art.print_game_logo()
    art.draw_reference_board()
    board = logic.initialize_board()
    
    current_player = "X" 
    game_should_continue = True

    while game_should_continue:
    
        if current_player == "X":
            try:
                position = int(input(f"Your turn ({current_player}), make your move (1-9): "))
                if position < 1 or position > 9:
                    print("Please enter a number between 1 and 9.")
                    continue
            except ValueError:
                print("Invalid input! Please enter a valid number.")
                continue
        else:
            print("Computer (O) is thinking...")
            time.sleep(1) 
            position = logic.get_best_move(board)

        success = logic.update_board(board, position, current_player)
        art.draw_board(board)
        
        if not success:
            if current_player == "X": 
                print("This cell is already full! Choose another spot.")
            continue

        winner = logic.check_winner(board)
        if winner:
            if winner == "X":
                print("Game Over! YOU WIN! 🏆")
            else:
                print("Game Over! COMPUTER WINS! 🤖")
            game_should_continue = False
        elif logic.is_board_full(board):
            print("The game is a draw! 🤝")
            game_should_continue = False
        else:
            current_player = "O" if current_player == "X" else "X"

    restart = input("\nDo you want to play again? (Y/N): ").upper()
    if restart == "Y":
        play_game()

if __name__ == "__main__":
    play_game()