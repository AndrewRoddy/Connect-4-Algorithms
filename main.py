# All code written by Andrew Roddy
import pygame
import random


class Connect4():
        
    def empty_board(self) -> list:
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


    def check_full(self, board: list) -> bool:
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


    def check_win_horizontal(self, board: list, player: str) -> bool:
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


    def check_win_vertical(self, board: list, player: str) -> bool:
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


    def check_win_diagnol(self, board: list, player: str) -> bool:
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


    def player_turn(self, board: list, column: int, player: str) -> list:
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


    def check_turn(self, board: list, column: int) -> bool:
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


    def check_win_reverse_diagnol(self, board: list, player: str) -> bool:
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


    def check_win(self, board: list, player: str) -> bool:
        """Runs the 4 win checking functions and returns True if any of them return True.

        Args:
            board (list): The current Connect 4 board.
            player (str): The current player's icon.

        Returns:
            bool: True if the player has won.
        """
        return (
            self.check_win_horizontal(board, player)
            or self.check_win_vertical(board, player)
            or self.check_win_reverse_diagnol(board, player)
            or self.check_win_diagnol(board, player)
        )


    def draw_board(self, board: list, screen, image) -> None:
        for i in range(len(board[0])):
            for j in range(len(board)):
                if board[j][i] == "X":
                    screen.blit(
                        image["red_chip"], (((i + 0.5) * 70) - 25, ((j + 1.5) * 70) - 25)
                    )
                if board[j][i] == "O":
                    screen.blit(
                        image["blue_chip"], (((i + 0.5) * 70) - 25, ((j + 1.5) * 70) - 25)
                    )
                if board[j][i] == "_":
                    pygame.draw.circle(screen, "gray", ((i + 0.5) * 70, (j + 1.5) * 70), 20)

        return screen


    def colum_select(self, board, player, winner, game_running, running, mode="pvp"):
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
                        if event.key == keys[i] and self.check_turn(board, (i + 1)):
                            self.player_turn(board, (i + 1), player)

                            if self.check_win(board, player):  # Checks if the player has won
                                winner = player
                                game_running = False

                            if self.check_full(board):  # Checks if the game ends in a tie
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
                if self.check_turn(board, pick):
                    self.player_turn(board, pick, player)
                    if self.check_win(board, player):  # Checks if the player has won
                        winner = player
                        game_running = False

                    if self.check_full(board):  # Checks if the game ends in a tie
                        game_running = False
                        winner = "Z"
                    player = "X"
                    break

        return board, player, winner, game_running, running


    def generate_text(self):
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
        text["menu"] = font.render("Press Space To Begin", True, "black")
        return text


    def draw_text(self, screen, text, key):
        if key == "x_wins":
            screen.blit(text["x_wins"], (200, 15))
        if key == "o_wins":
            screen.blit(text["o_wins"], (200, 15))
        if key == "game_tie":
            screen.blit(text["game_tie"], ((200, 15)))
        if key == "x_text":
            screen.blit(text["x_text"], (240, 20))
        if key == "o_text":
            screen.blit(text["o_text"], (240, 20))
        if key == "numbers":
            screen.blit(text["numbers"], (30, 60))
            screen.blit(text["numbers"], (30, 480))
        if key == "menu":
            screen.blit(text["menu"], (240, 20))

        return screen


    def generate_image(self):
        image = {
            "blue_chip": pygame.image.load("images\\blue_chip.png"),
            "red_chip": pygame.image.load("images\\red_chip.png"),
            "space_button": pygame.image.load("images\\space_button.png"),
            "logo": pygame.image.load("images\\connect_four_logo.png"),
        }
        # create a surface object, image is drawn on it.
        image["blue_chip"] = pygame.transform.scale(image["blue_chip"], (50, 50))
        image["red_chip"] = pygame.transform.scale(image["red_chip"], (50, 50))
        image["logo"] = pygame.transform.scale(image["logo"], (450, 400))
        # Using blit to copy content from one surface to other
        return image


    def restart_game(self):
        board = self.empty_board()  # Instalizes an empty board
        player = "".join(random.choices(["X", "O"]))  # Sets the first player to random
        game_running = True
        winner = ""
        return board, player, game_running, winner


    def main_menu(self, screen, text, image):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return False, screen
        screen.fill("white")
        screen.blit(image["space_button"], (100, 250))
        screen.blit(image["logo"], (10, -100))
        screen.blit(text["menu"], (10, 450))
        return True, screen


    def game_over(self, screen, text, winner):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return True, screen

        if winner == "X":
            self.draw_text(screen, text, "x_wins")
        if winner == "O":
            self.draw_text(screen, text, "o_wins")
        if winner == "Z":
            self.draw_text(screen, text, "game_tie")
        return (
            False,
            screen,
        )


def main():
    # pygame setup #
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    clock = pygame.time.Clock()
    running = True
    pygame.display.set_caption("Connect 4            -Andrew Roddy")
    ################

    game = Connect4()
    text = game.generate_text()
    image = game.generate_image()

    board, player, game_running, winner = game.restart_game()
    mode = "pvp"
    # While the game is running

    menu = True
    while running:
        if menu == True:
            menu, screen = game.main_menu(screen, text, image)

        elif game_running == False:
            game_running, screen = game.game_over(screen, text, winner)
            if game_running == True:
                board, player, game_running, winner = game.restart_game()
        else:
            # Draw from back to front
            screen.fill("aliceblue")

            board, player, winner, game_running, running = game.colum_select(
                board, player, winner, game_running, running, mode
            )

            # Draws the pieces on the board
            screen = game.draw_board(board, screen, image)
            screen = game.draw_text(screen, text, "numbers")
            if player == "X" and game_running:
                screen = game.draw_text(screen, text, "x_text")
            if player == "O" and game_running:
                screen = game.draw_text(screen, text, "o_text")

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

# Seperate functions into different files

# Add Bot Opponents
# Random
# Easy
# AI
# Add Difficulty
# Make it so the user can choose their icon
# Add Online Play
"""
