# All code written by Andrew Roddy


def ascii_art() -> str:
    """Generates Ascii Art for the program

    Returns:
        str: ASCII Art
    """
    return "\n   ____                            _     _  _\n  / ___|___  _ __  _ __   ___  ___| |_  | || |\n | |   / _ \| '_ \| '_ \ / _ \/ __| __| | || |_\n | |__| (_) | | | | | | |  __/ (__| |_  |__   _|\n  \____\___/|_| |_|_| |_|\___|\___|\__|    |_|\nUse -1 to forfeit."


def empty_board() -> list:
    """Generates an empty Connect 4 board.

    Returns:
        list: A 2d list of the empty Connect 4 board.
    """
    return [
        ["_", "_", "_", "_", "_", "_", "_"],
        ["_", "_", "_", "_", "_", "_", "_"],
        ["_", "_", "_", "_", "_", "_", "_"],
        ["_", "_", "_", "_", "_", "_", "_"],
        ["_", "_", "_", "_", "_", "_", "_"],
        ["_", "_", "_", "_", "_", "_", "_"],
    ]


def display_board(board: list) -> None:
    """Prints the board with column numbers to the terminal.

    Args:
        board (list): Prints the board to the terminal.
    """
    print("1 2 3 4 5 6 7")
    for i in range(len(board)):  # Runs once for every row in the board
        print(*board[i], sep=" ")

    print("1 2 3 4 5 6 7")


def player_turn(board: list, column: int, player: str) -> list:
    """Allows the player to place an icon on the board.

    Args:
        board (list): The current Connect 4 board.
        column (int): The column that the user selected.
        player (str): The current player's icon.

    Returns:
        list: The updated Connect 4 board.
    """
    column -= 1  # Changes from a visual column to a list column

    for i in range(len(board) - 1, -1, -1):
        if board[i][column] == "_":  # Checks if the column is empty
            board[i][column] = player
            return board


def check_turn(board: list, column: int) -> bool:
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


def check_win_horizontal(board: list, player: str) -> bool:
    """Checks if the current user has won the game horizontally.

    Args:
        board (list): The current Connect 4 board.
        player (str): The current player's icon.

    Returns:
        bool: True if the player has won, False if the player has not won.
    """
    for x in range(len(board[0]) - 3):
        for y in range(len(board)):
            if (
                board[y][x] == player
                and board[y][x + 1] == player
                and board[y][x + 2] == player
                and board[y][x + 3] == player
            ):
                return True
    return False


def check_win_vertical(board: list, player: str) -> bool:
    """Checks if the current user has won the game vertically.

    Args:
        board (list): The current Connect 4 board.
        player (str): The current player's icon.

    Returns:
        bool: True if the player has won, False if the player has not won.
    """
    for y in range(len(board[0]) - 4):
        for x in range(len(board)):
            if (
                board[y][x] == player
                and board[y + 1][x] == player
                and board[y + 2][x] == player
                and board[y + 3][x] == player
            ):
                return True
    return False


def check_win_diagnol(board: list, player: str) -> bool:
    """Checks if the current user has won the game diagnoly.

    Args:
        board (list): The current Connect 4 board.
        player (str): The current player's icon.

    Returns:
        bool: True if the player has won, False if the player has not won.
    """
    for y in range(len(board[0]) - 4):
        for x in range(len(board) - 2):
            if (
                board[y + 3][x] == player
                and board[y + 2][x + 1] == player
                and board[y + 1][x + 2] == player
                and board[y][x + 3] == player
            ):
                return True
    return False


def check_win_reverse_diagnol(board: list, player: str) -> bool:
    """Checks if the current user has won the game in a reverse diagnol.

    Args:
        board (list): The current Connect 4 board.
        player (str): The current player's icon.

    Returns:
        bool: True if the player has won, False if the player has not won.
    """
    for y in range(len(board[0]) - 4):
        for x in range(len(board) - 2):
            if (
                board[y][x] == player
                and board[y + 1][x + 1] == player
                and board[y + 2][x + 2] == player
                and board[y + 3][x + 3] == player
            ):
                return True
    return False


def check_win(board: list, player: str) -> bool:
    """Runs the 4 win checking functions and returns True if any of them return True.

    Args:
        board (list): The current Connect 4 board.
        player (str): The current player's icon.

    Returns:
        bool: True if the player has won.
    """
    return (
        check_win_horizontal(board, player)
        or check_win_vertical(board, player)
        or check_win_reverse_diagnol(board, player)
        or check_win_diagnol(board, player)
    )


def check_full(board: list) -> bool:
    """Checks if the players have filled the board and tied.

    Args:
        board (list): The current Connect 4 board.

    Returns:
        bool: True if the board is full, False if the board is not full.
    """
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "_":
                return False
    return True


def main():
    print(ascii_art())  # Prints the art
    board = empty_board()  # Instalizes an empty board
    player = "X"  # Sets the first player to X

    while True:
        print("\n")
        display_board(board)  # Prints the current board
        try:
            column = int(input(f"What column {player}? "))
            if column == -1:  # If the user enters -1, they forfeit
                break

        except ValueError:
            print("Enter a number")
            continue

        if check_turn(board, column) == False:
            print("Column is full or out of range")
            continue

        column = int(column)

        board = player_turn(board, column, player)

        if check_win(board, player):  # Checks if the player has won
            display_board(board)
            print(f"{player} Wins!\n")
            break

        if check_full(board):  # Checks if the game ends in a tie
            display_board(board)
            print("Tie!")
            break

        if player == "X":  # Switches the player
            player = "O"
        else:
            player = "X"

    print("Thanks for playing!")
    rematch = input("Play Again? ")

    if rematch.lower() == "y" or rematch.lower() == "yes" or rematch.lower() == "1":
        main()


if __name__ == "__main__":
    main()


