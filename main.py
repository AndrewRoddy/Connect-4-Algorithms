# All code written by Andrew Roddy
import pygame
import random


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


def draw_board(board: list, screen) -> None:
    for i in range(len(board[0])):
        for j in range(len(board)):
            if board[j][i] == "X":
                pygame.draw.circle(screen, "red", ((i + 0.5) * 70, (j + 1.5) * 70), 20)
            if board[j][i] == "O":
                pygame.draw.circle(screen, "blue", ((i + 0.5) * 70, (j + 1.5) * 70), 20)
            if board[j][i] == "_":
                pygame.draw.circle(screen, "gray", ((i + 0.5) * 70, (j + 1.5) * 70), 20)

    return screen


def colum_select(board, player, winner, game_running, running, mode="pvp"):
    # If a key is pressed then runs everything else
    keys = [
        pygame.K_1,
        pygame.K_2,
        pygame.K_3,
        pygame.K_4,
        pygame.K_5,
        pygame.K_6,
        pygame.K_7,
    ]
    if mode == "pvp" or player == "X":
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and game_running:
                for i in range(len(keys)):
                    if event.key == keys[i] and check_turn(board, (i + 1)):
                        player_turn(board, (i + 1), player)

                        if check_win(board, player):  # Checks if the player has won
                            winner = player
                            game_running = False

                        if check_full(board):  # Checks if the game ends in a tie
                            game_running = False
                            winner = "Z"

                        if player == "X":  # Switches the player
                            player = "O"
                        else:
                            player = "X"
            if event.type == pygame.QUIT:
                running = False
    if mode == "random" and player == "O":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        while True:
            pick = random.randint(1, 7)
            if check_turn(board, pick):
                player_turn(board, pick, player)
                if check_win(board, player):  # Checks if the player has won
                    winner = player
                    game_running = False

                if check_full(board):  # Checks if the game ends in a tie
                    game_running = False
                    winner = "Z"
                player = "X"
                break

    return board, player, winner, game_running, running


def generate_text():
    # Instalizes all Text
    pygame.font.init()

    font = pygame.font.Font(None, 74)
    text = {
        "x_text": font.render("X", True, "red"),
        "o_text": font.render("O", True, "blue"),
        "x_wins": font.render("X WINS", True, "red"),
        "o_wins": font.render("O WINS", True, "blue"),
        "game_tie": font.render("TIE", True, "black"),
    }

    font = pygame.font.Font(None, 32)
    text["numbers"] = font.render(
        "1          2          3         4           5          6          7",
        True,
        "black",
    )
    return text


def draw_text(screen, text, winner, player):
    if winner != "":
        if winner == "X":
            screen.blit(text["x_wins"], (200, 250))

        if winner == "O":
            screen.blit(text["o_wins"], (200, 250))

        if winner == "Z":
            screen.blit(text["game_tie"], (240, 240))
    else:
        if player == "X":
            screen.blit(text["x_text"], (240, 20))
        if player == "O":
            screen.blit(text["o_text"], (240, 20))

    # Manages Text
    screen.blit(text["numbers"], (30, 60))
    screen.blit(text["numbers"], (30, 480))

    return screen


def restart_game():
    board = empty_board()  # Instalizes an empty board
    player = "".join(random.choices(["X", "O"]))  # Sets the first player to random
    game_running = True
    winner = ""
    return board, player, game_running, winner


def main_menu(screen):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                return False, screen

    screen.fill("white")
    return True, screen


def game_over(screen, text, winner, player):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                return True, screen
    screen.fill("white")
    draw_text(screen, text, winner, player)
    return False, screen,


def main():
    # pygame setup #
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    clock = pygame.time.Clock()
    running = True
    pygame.display.set_caption("Connect 4            -Andrew Roddy")
    ################
    
    text = generate_text()

    board, player, game_running, winner = restart_game()
    mode = "random"
    # While the game is running

    menu = True
    while running:
        if menu == True:
            menu, screen = main_menu(screen)

        elif game_running == False:
            game_running, screen = game_over(screen, text, winner, player)
            if game_running == True:
                board, player, game_running, winner = restart_game()
        else:
            # Draw from back to front
            screen.fill("aliceblue")

            # Draws the pieces on the board
            screen = draw_board(board, screen)

            board, player, winner, game_running, running = colum_select(
                board, player, winner, game_running, running, mode
            )

            screen = draw_text(screen, text, winner, player)
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.QUIT:
                    running = False
            # Runs pygame
        pygame.display.flip()  # displays to screen
        clock.tick(60)  # limits FPS to 60

    pygame.quit()


if __name__ == "__main__":
    main()
"""
# TODO

# Add pygame
# Add start screen
# Start by just showing a visual of the board

# Seperate functions into different files

# Add Bot Opponents
# Random
# Easy
# AI
# Add Difficulty
# Make it so the user can choose their icon
# Add Online Play
"""
