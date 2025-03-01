import time

def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(row[col] == player for row in board):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def get_player_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            row, col = divmod(move, 3)
            if board[row][col] == " ":
                return row, col
            else:
                print("Cell is already occupied. Choose another.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number between 1 and 9.")

def tic_tac_toe():
    print("""
    =======================================================
    Tic-Tac-Toe Game
    Created by Neha Khan
    =======================================================
    """)

    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    for _ in range(9):  # Maximum of 9 moves
        current_player = players[turn % 2]
        print(f"Player {current_player}'s turn")
        row, col = get_player_move(board)
        board[row][col] = current_player
        print_board(board)

        if check_winner(board, current_player):
            print(f"Player {current_player} wins!")
            return

        turn += 1

    print("It's a tie!")

if __name__ == "__main__":
    tic_tac_toe()
