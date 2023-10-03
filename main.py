# All code written by Andrew Roddy
import pygame
import random


class Connect4:
    def __init__(self):
        self.board = [
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
        ]  # Instalizes an empty board
        self.player = "".join(random.choices(["X", "O"]))
        self.game_running = True
        self.winner = ""
        self.mode = "pvp"

    def check_full(self) -> bool:
        """Checks if the self.players have filled the board and tied.

        Args:
            board (list): The current Connect 4 board.

        Returns:
            bool: True if the board is full, False if the board is not full.
        """
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == "_":
                    return False
        return True

    # Win Checks
    def check_win_horizontal(self) -> bool:
        """Checks if the current user has won the game horizontally.

        Args:
            board (list): The current Connect 4 board.
            player (str): The current player's icon.

        Returns:
            bool: True if the player has won, False if the player has not won.
        """
        for x in range(len(self.board[0]) - 3):
            for y in range(len(self.board)):
                if (
                    self.board[y][x] == self.player
                    and self.board[y][x + 1] == self.player
                    and self.board[y][x + 2] == self.player
                    and self.board[y][x + 3] == self.player
                ):
                    return True
        return False

    def check_win_vertical(self) -> bool:
        """Checks if the current user has won the game vertically.

        Args:
            board (list): The current Connect 4 board.
            player (str): The current player's icon.

        Returns:
            bool: True if the player has won, False if the player has not won.
        """
        for y in range(len(self.board[0]) - 4):
            for x in range(len(self.board)):
                if (
                    self.board[y][x] == self.player
                    and self.board[y + 1][x] == self.player
                    and self.board[y + 2][x] == self.player
                    and self.board[y + 3][x] == self.player
                ):
                    return True
        return False

    def check_win_diagnol(self) -> bool:
        """Checks if the current user has won the game diagnoly.

        Args:
            board (list): The current Connect 4 board.
            player (str): The current player's icon.

        Returns:
            bool: True if the player has won, False if the player has not won.
        """
        for y in range(len(self.board[0]) - 4):
            for x in range(len(self.board) - 2):
                if (
                    self.board[y + 3][x] == self.player
                    and self.board[y + 2][x + 1] == self.player
                    and self.board[y + 1][x + 2] == self.player
                    and self.board[y][x + 3] == self.player
                ):
                    return True
        return False

    def check_win_reverse_diagnol(self) -> bool:
        """Checks if the current user has won the game in a reverse diagnol.

        Args:
            board (list): The current Connect 4 board.
            player (str): The current player's icon.

        Returns:
            bool: True if the player has won, False if the player has not won.
        """
        for y in range(len(self.board[0]) - 4):
            for x in range(len(self.board) - 2):
                if (
                    self.board[y][x] == self.player
                    and self.board[y + 1][x + 1] == self.player
                    and self.board[y + 2][x + 2] == self.player
                    and self.board[y + 3][x + 3] == self.player
                ):
                    return True
        return False

    def check_win(self) -> bool:
        """Runs the 4 win checking functions and returns True if any of them return True.

        Args:
            board (list): The current Connect 4 board.
            player (str): The current player's icon.

        Returns:
            bool: True if the player has won.
        """
        return (
            self.check_win_horizontal()
            or self.check_win_vertical()
            or self.check_win_reverse_diagnol()
            or self.check_win_diagnol()
        )

    def player_turn(self, column: int) -> list:
        """Allows the player to place an icon on the board.

        Args:
            board (list): The current Connect 4 board.
            column (int): The column that the user selected.
            player (str): The current player's icon.

        Returns:
            list: The updated Connect 4 board.
        """
        column -= 1  # Changes from a visual column to a list column

        for i in range(len(self.board) - 1, -1, -1):
            if self.board[i][column] == "_":  # Checks if the column is empty
                self.board[i][column] = self.player
                return self.board

    def check_turn(self, column: int) -> bool:
        """Checks if the player's turn is valid.

        Args:
            board (list): The current Connect 4 board.
            column (int): The column that the user selected.

        Returns:
            bool: True if the turn is valid, False if the turn is invalid.
        """
        if column > 7 or column < 0:
            return False

        if self.board[0][column - 1] != "_":  # Checks if the column is full
            return False

        return True

    def draw_board(self, screen, image) -> None:
        for i in range(len(self.board[0])):
            for j in range(len(self.board)):
                if self.board[j][i] == "X":
                    screen.blit(
                        image["red_chip"],
                        (((i + 0.5) * 70) - 25, ((j + 1.5) * 70) - 25),
                    )
                if self.board[j][i] == "O":
                    screen.blit(
                        image["blue_chip"],
                        (((i + 0.5) * 70) - 25, ((j + 1.5) * 70) - 25),
                    )
                if self.board[j][i] == "_":
                    pygame.draw.circle(
                        screen, "gray", ((i + 0.5) * 70, (j + 1.5) * 70), 20
                    )

        return screen

    def colum_select(self, running, mode="pvp"):
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
        if mode == "pvp" or self.player == "X":
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and self.game_running:
                    for i in range(len(keys)):
                        if event.key == keys[i] and self.check_turn((i + 1)):
                            self.player_turn((i + 1))

                            if self.check_win():  # Checks if the player has won
                                self.winner = self.player
                                self.game_running = False

                            if self.check_full():  # Checks if the game ends in a tie
                                self.game_running = False
                                self.winner = "Z"

                            if self.player == "X":  # Switches the player
                                self.player = "O"
                            else:
                                self.player = "X"
                if event.type == pygame.QUIT:
                    running = False
        if mode == "random" and self.player == "O":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            while True:
                pick = random.randint(1, 7)
                if self.check_turn(pick):
                    self.player_turn(pick)
                    if self.check_win():  # Checks if the player has won
                        self.winner = self.player
                        self.game_running = False

                    if self.check_full():  # Checks if the game ends in a tie
                        self.game_running = False
                        self.winner = "Z"
                    self.player = "X"
                    break

        return running

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

    def game_over(self, screen, text):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return True, screen

        if self.winner == "X":
            self.draw_text(screen, text, "x_wins")
        if self.winner == "O":
            self.draw_text(screen, text, "o_wins")
        if self.winner == "Z":
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

    mode = "pvp"
    # While the game is running

    menu = True
    while running:
        if menu == True:
            menu, screen = game.main_menu(screen, text, image)

        elif game.game_running == False:
            game.game_running, screen = game.game_over(screen, text)
            if game.game_running == True:
                game = Connect4()
        else:
            # Draw from back to front
            screen.fill("aliceblue")

            running = game.colum_select(running, mode)

            # Draws the pieces on the board
            screen = game.draw_board(screen, image)
            screen = game.draw_text(screen, text, "numbers")
            if game.player == "X" and game.game_running:
                screen = game.draw_text(screen, text, "x_text")
            if game.player == "O" and game.game_running:
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
