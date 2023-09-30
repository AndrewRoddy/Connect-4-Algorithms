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