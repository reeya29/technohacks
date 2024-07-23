import random

def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows, columns and diagonals
    for i in range(3):
        if all([spot == player for spot in board[i]]):
            return True
        if all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def check_tie(board):
    for row in board:
        if " " in row:
            return False
    return True

def player_move(board, player):
    while True:
        move = input(f"Player {player}, enter your move (1-9): ")
        if move.isdigit() and int(move) in range(1, 10):
            move = int(move) - 1
            row, col = divmod(move, 3)
            if board[row][col] == " ":
                board[row][col] = player
                break
            else:
                print("This spot is already taken.")
        else:
            print("Invalid input. Please enter a number between 1 and 9.")

def computer_move(board, player):
    while True:
        move = random.randint(0, 8)
        row, col = divmod(move, 3)
        if board[row][col] == " ":
            board[row][col] = player
            break

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    game_mode = input("Enter 1 for two players or 2 to play against the computer: ")
    while game_mode not in ["1", "2"]:
        game_mode = input("Invalid input. Enter 1 for two players or 2 to play against the computer: ")

    while True:
        print_board(board)
        if game_mode == "2" and current_player == "O":
            computer_move(board, current_player)
        else:
            player_move(board, current_player)

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        if check_tie(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = "O" if current_player == "X" else "X"

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        play_game()
    else:
        print("Thanks for playing!")

# Run the game
play_game()
