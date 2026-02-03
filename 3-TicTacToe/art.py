def print_game_logo():
    print("-------------------------")
    print("  T I C   T A C   T O E  ")
    print("-------------------------")
    print("\n")
    print("Players: 'X' and 'O'")
    print("To make a move, enter a number between 1-9.")
    print("-------------------------\n")


def draw_board(board):
    print("\n")
    print("     |     |")
    print(f"  {board[0][0]}  |  {board[0][1]}  |  {board[0][2]}")
    print("_____|_____|_____")
    print("     |     |")
    print(f"  {board[1][0]}  |  {board[1][1]}  |  {board[1][2]}")
    print("_____|_____|_____")
    print("     |     |")
    print(f"  {board[2][0]}  |  {board[2][1]}  |  {board[2][2]}")
    print("     |     |\n")

def draw_reference_board():
    print("Reference Board:")
    print("     |     |")
    print("  1  |  2  |  3")
    print("_____|_____|_____")
    print("     |     |")
    print("  4  |  5  |  6")
    print("_____|_____|_____")
    print("     |     |")
    print("  7  |  8  |  9")
    print("     |     |\n")
