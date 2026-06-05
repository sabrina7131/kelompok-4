nama-proyek/
 main.py
templates/
    product.html

def print_board(board):
    """Prints the Tic Tac Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def get_player_move(board, player):
    """Gets a valid move from the player."""
    while True:
        try:
            row = int(input(f"Player {player}, enter row (0, 1, or 2): "))
            col = int(input(f"Player {player}, enter column (0, 1, or 2): "))
            if 0 <= row <= 2 and 0 <= col <= 2:
                if board[row][col] == " ":
                    return row, col
                else:
                    print("That spot is already taken. Try again.")
            else:
                print("Invalid input. Row and column must be 0, 1, or 2.")
        except ValueError:
            print("Invalid input. Please enter numbers.")

def check_win(board, player):
    """Checks if the current player has won."""
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def check_tie(board):
    """Checks if the game is a tie."""
    for row in board:
        if " " in row:
            return False
    return True

def play_tic_tac_toe():
    """Plays a game of Tic Tac Toe."""
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        row, col = get_player_move(board, current_player)
        board[row][col] = current_player
        print_board(board)

        if check_win(board, current_player):
            print(f"Congratulations! Player {current_player} wins!")
            break
        elif check_tie(board):
            print("It's a tie!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    play_tic_tac_toe()
