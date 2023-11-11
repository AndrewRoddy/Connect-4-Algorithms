import random


def check_turn(board, column: int) -> bool:
    """Checks if the player's turn is valid.

    Args:
        board (list): The current Connect 4 board.
        column (int): The column that the user selected.

    Returns:
        bool: True if the turn is valid, False if the turn is invalid.
    """
    if column > 7 or column < 0:
        return False

    if board[0][column - 1] != "_":  # Checks if the column is full
        return False

    return True


def check_possible_rows(board, player):
    focus = []  # focus = [[y,x],[y,x],[y,x]]
    for x in range(len(board[0]) - 2):
        for y in range(len(board)):
            if (
                board[y][x] == player
                and board[y][x + 1] == player
                and board[y][x + 2] == player
            ):
                focus.append([y, x])
    return focus


def random_algorithm(board):
    while True:
        pick = random.randint(1, 7)
        if check_turn(board, pick):
            return pick


def easy_algorithm(board, player):
    enemy = "O" if player == "X" else "X"
    focus = check_possible_rows(board, enemy)

    for i in range(len(focus)):
        ic(i)
        for j in [-1, 3]:
            user_number = focus[i][1] + j
            if 0 >= user_number <= 6:
                if board[focus[i][0]][focus[i][1] + j] == "_" and check_turn(board, (int(user_number) + 1)):
                    return (int(user_number) + 1)
    return random_algorithm(board)


def medium_algorithm(board, player):
    pass


def hard_algorithm(board, player):
    pass


def ai_algorithm(board, player):
    pass

def display_board(board: list) -> None:
    """Prints the board with column numbers to the terminal.

    Args:
        board (list): Prints the board to the terminal.
    """
    print("1 2 3 4 5 6 7")
    for i in range(len(board)):  # Runs once for every row in the board
        print(*board[i], sep=" ")

    print("1 2 3 4 5 6 7")