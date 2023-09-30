# All code written by Andrew Roddy
import pygame
from winner import *

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
    # pygame setup #
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    clock = pygame.time.Clock()
    running = True
    pygame.display.set_caption('Connect 4            -Andrew Roddy')
    #              #
    
    board = empty_board()  # Instalizes an empty board
    player = "X"  # Sets the first player to X
    
    
    # Generate Text
    pygame.font.init()
    font = pygame.font.Font(None, 32)
    numbers = font.render('1          2          3         4           5          6          7', True, "white")

    font = pygame.font.Font(None, 74)
    x_text = font.render('X', True, "red")
    o_text = font.render('O', True, "blue")
    x_wins = font.render('X WINS', True, "red")
    o_wins = font.render('O WINS', True, "blue")
    game_tie = font.render('TIE', True, "black")
    
    game_running = True
    winner = ""
    # While the game is running
    while running:
        # Draw from back to front
        screen.fill("aliceblue")
        
        # Draws the circles on the board
        for i in range(len(board[0])):
            for j in range(len(board)):
                if board[j][i] == "X":
                    pygame.draw.circle(screen, "red", ((i + 0.5)*70, (j + 1.5)*70), 20)
                if board[j][i] == "O":
                    pygame.draw.circle(screen, "blue", ((i + 0.5)*70, (j + 1.5)*70), 20)
                if board[j][i] == "_":
                    pygame.draw.circle(screen, "white", ((i + 0.5)*70, (j + 1.5)*70), 20)

        
        # If a key is pressed then runs everything else
        keys = [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7]
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and game_running:
                for i in range(len(keys)):
                    if event.key == keys[i] and check_turn(board, (i + 1)):
                        player_turn(board, (i + 1), player)
                        if check_win(board, player): # Checks if the player has won
                            winner = player
                            game_running = False
                            
                        if player == "X":  # Switches the player
                            player = "O"
                        else:
                            player = "X"
                            
            # Runs quitting the game
            if event.type == pygame.QUIT:
                running = False
        
        if winner != "":
            if winner == "X":
                screen.blit(x_wins, (200,250))
            if winner == "O":
                screen.blit(o_wins, (200,250))
        else:
            if player == "X": screen.blit(x_text, (240,20))
            if player == "O": screen.blit(o_text, (240,20))
            
        # Manages Text
        screen.blit(numbers, (30,60))
        screen.blit(numbers, (30,480))
        
        
        if check_full(board):  # Checks if the game ends in a tie
            game_running = False
            screen.blit(game_tie, (240,240))

        # Runs pygame
        pygame.display.flip() # displays to screen
        clock.tick(60)  # limits FPS to 60
        
    """
    print("Thanks for playing!")
    rematch = input("Play Again? ")

    if rematch.lower() == "y" or rematch.lower() == "yes" or rematch.lower() == "1":
        main()
    """
    pygame.quit()



if __name__ == "__main__":
    main()

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