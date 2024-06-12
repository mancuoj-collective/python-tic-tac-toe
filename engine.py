import random


def new_board():
    return [None] * 9


def print_board(board):
    print("    1 2 3")
    print("   -------")
    for row in range(3):
        print(f"{row + 1} | ", end="")
        for col in range(3):
            print(board[row * 3 + col] or " ", end=" ")
        print("|")
    print("   -------")


def get_move(board):
    while True:
        try:
            move = int(input("Enter move (1-9): ")) - 1
            if move < 0 or move >= 9:
                raise ValueError
            if board[move] is not None:
                print("This square is already taken, try again.")
                continue
            return move
        except ValueError:
            print("Invalid input, try again.")


def make_move(board, move, player):
    board[move] = player


def check_winner(board):
    lines = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ]

    for line in lines:
        a, b, c = line
        if board[a] and board[a] == board[b] == board[c]:
            return board[a]
    return None


def check_draw(board):
    return None not in board


def get_random_ai_move(board):
    available_moves = [i for i in range(9) if board[i] is None]
    return random.choice(available_moves)


def get_ai_move(board):
    best_score = float("-inf")
    best_move = None
    for i in range(len(board)):
        if board[i] is None:
            board[i] = "O"
            score = minimax(board, False)
            board[i] = None
            if score > best_score:
                best_score = score
                best_move = i
    return best_move


def minimax(board, is_maximizing):
    winner = check_winner(board)
    if winner == "X":
        return -10
    elif winner == "O":
        return 10
    elif check_draw(board):
        return 0

    if is_maximizing:
        best_score = float("-inf")
        for i in range(len(board)):
            if board[i] is None:
                board[i] = "O"
                score = minimax(board, False)
                board[i] = None
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for i in range(len(board)):
            if board[i] is None:
                board[i] = "X"
                score = minimax(board, True)
                board[i] = None
                best_score = min(score, best_score)
        return best_score


def play_game():
    board = new_board()
    player = "X"
    print_board(board)
    while True:
        if player == "X":
            move = get_move(board)
        else:
            move = get_ai_move(board)
        make_move(board, move, player)
        print_board(board)
        winner = check_winner(board)
        if winner:
            print(f"{winner} wins!")
            break
        if check_draw(board):
            print("Draw!")
            break
        player = "O" if player == "X" else "X"


if __name__ == "__main__":
    play_game()
