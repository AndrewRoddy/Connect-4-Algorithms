# All code written by Andrew Roddy
import pygame
import random
from check_board import *


class Connect4:
    def __init__(self):
        # Instalizes a blank board
        self.board = [
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
        ]  # Instalizes an empty board
        self.player = "".join(
            random.choices(["X", "O"])
        )  # Selectes a random starting player
        self.game_running = True  # Checks if the game is running
        self.winner = ""  # The winner of the game
        self.running = True  # Checks if pygame is running
        self.mode = ""  # The current game mode
        # On Laptop screen.size = 649 fullscreen
        # On Desktop screen.size = 1369 fullscreen
        self.size = 500  # The smallest screen dimension
        self.center = 0  # The positive difference of y and x

        self.generate_text()  # Generates the text
        self.generate_image()  # Generates the images
    
    def reset(self):
        # Instalizes a blank board
        self.board = [
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
        ]  # Instalizes an empty board
        self.player = "".join(
            random.choices(["X", "O"])
        )  # Selectes a random starting player
        self.game_running = True  # Checks if the game is running
        self.winner = ""  # The winner of the game
        self.running = True  # Checks if pygame is running

        # On Laptop screen.size = 649 fullscreen
        # On Desktop screen.size = 1369 fullscreen
        self.size = 500  # The smallest screen dimension
        self.center = 0  # The positive difference of y and x

        self.generate_text()  # Generates the text
        self.generate_image()  # Generates the images
    
    
    def resize(self, screen):
        try:  # Creates a past screen size variable
            past_x, past_y = self.screen_x, self.screen_y
        except AttributeError:
            past_x, past_y = 0, 0

        (
            self.screen_x,
            self.screen_y,
        ) = screen.get_size()  # Creates current screen size variables

        if (
            past_x != self.screen_x or past_y != self.screen_y
        ):  # Checks if the screen size has changed
            if self.screen_x > self.screen_y:
                self.size = self.screen_y
            else:
                self.size = self.screen_x

            self.center = (self.size - self.screen_x) * (-0.385)

            self.generate_text()  # Regenerates images and text using current size metrics
            self.generate_image()
            self.text_coords = (self.screen_x / 2.15, self.size / 50)

        return screen

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
                break

        if check_win(self.board, self.player):  # Checks if the player has won
            self.winner = self.player
            self.game_running = False

        if check_full(self.board):  # Checks if the game ends in a tie
            self.game_running = False
            self.winner = "Z"

        if self.player == "X":  # Switches the player
            self.player = "O"
        else:
            self.player = "X"

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

    def draw_board(self, screen):
        icons = [self.image["orange_chip"], self.image["blue_chip"]]
        players = ["X", "O"]

        self.image["blue_chip"] = pygame.transform.scale(
            self.image["blue_chip"], (self.size * 0.1, self.size * 0.1)
        )
        self.image["orange_chip"] = pygame.transform.scale(
            self.image["orange_chip"], (self.size * 0.1, self.size * 0.1)
        )

        for i in range(len(self.board[0])):  # 0-6
            number_x = (
                self.center
                + (self.size / 25)
                + (i + self.size / 1500)  # Adds to adjust for text  # Same as chips
                * (self.size / 7.5)
            )
            screen.blit(  # Top Numbers
                self.text[str(i + 1)],
                (number_x, self.size * 0.15),
            )

            screen.blit(  # Bottom Numbers
                self.text[str(i + 1)],
                (number_x, (self.size - self.size * 0.06)),
            )

            x_coordinate = self.center + (i + self.size / 1500) * (self.size / 7.5)
            for j in range(len(self.board)):  # 0-5
                for k in range(len(icons)):
                    if self.board[j][i] == players[k]:
                        y_coordinate = self.size / 5 + (j * self.size / 8)

                        screen.blit(
                            icons[k],
                            (
                                x_coordinate,
                                y_coordinate,
                            ),
                        )
        return screen

    def colum_select(self):
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
        if self.mode == "pvp" or self.player == "X":
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and self.game_running:
                    for i in range(len(keys)):
                        if event.key == keys[i] and self.check_turn((i + 1)):
                            self.player_turn((i + 1))
                            return True

                if event.type == pygame.QUIT:
                    self.running = False

        if self.mode == "random" and self.player == "O":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            while True:
                pick = random.randint(1, 7)
                if self.check_turn(pick):
                    self.player_turn(pick)
                    break

    def generate_text(self):
        # Instalizes all Text
        pygame.font.init()

        font = pygame.font.Font(None, round(self.size / 7))
        text_dict = {
            "x_text": font.render("O", True, "orange"),
            "o_text": font.render("O", True, "blue"),
            "x_wins": font.render("ORANGE WINS", True, "orange"),
            "o_wins": font.render("BLUE WINS", True, "blue"),
            "game_tie": font.render("TIE", True, "black"),
        }
        font = pygame.font.Font(None, round(self.size * 0.06))

        for i in range(1, 8):  # Generates the numbers
            text_dict[str(i)] = font.render(
                str(i),
                True,
                "black",
            )

        # Generates the menu text
        text_dict["menu"] = font.render("Select Your Mode", True, "black")
        self.text = text_dict

    def generate_image(self):
        image_dict = {
            "blue_chip": pygame.image.load("images\\blue_chip.png"),
            "orange_chip": pygame.image.load("images\\orange_chip.png"),
            "space_button": pygame.image.load("images\\space_button.png"),
            "P_key": pygame.image.load("images\\P_key.png"),
            "R_key": pygame.image.load("images\\R_key.png"),
            "E_key": pygame.image.load("images\\E_key.png"),
            "M_key": pygame.image.load("images\\M_key.png"),
            "H_key": pygame.image.load("images\\H_key.png"),
            "A_key": pygame.image.load("images\\A_key.png"),
            "logo": pygame.image.load("images\\logo.png"),
        }
        # Using blit to copy content from one surface to other
        self.image = image_dict
        return image_dict

    def main_menu(self, screen):
        screen = self.resize(screen)

        modes = ["P_key", "R_key", "E_key", "M_key", "H_key", "A_key"]
        """
        P_key = pvp
        R_key = random
        E_key = easy
        M_key = medium
        H_key = hard
        A_key = AI
        """
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                for i in range(len(modes)):
                    if event.key == pygame.K_p:
                        self.mode = "pvp"
                        return screen, False
                    if event.key == pygame.K_r:
                        self.mode = "random"
                        return screen, False
                    if event.key == pygame.K_e:
                        self.mode = "easy"
                        return screen, False
                    if event.key == pygame.K_m:
                        self.mode = "medium"
                        return screen, False
                    if event.key == pygame.K_h:
                        self.mode = "hard"
                        return screen, False
                    if event.key == pygame.K_a:
                        self.mode = "AI"
                        return screen, False
            
            if event.type == pygame.QUIT:
                self.running = False
        screen.fill("white")

        for i in range(len(modes)):
            self.image[modes[i]] = pygame.transform.scale(
                self.image[modes[i]], (self.size * 0.15, self.size * 0.15)
            )
            rect = self.image[modes[i]].get_rect(
                center=(
                    i * self.screen_x / 6.5 + self.screen_x / 9,
                    self.screen_y * 0.6,
                )
            )
            screen.blit(self.image[modes[i]], rect)

        self.image["logo"] = pygame.transform.scale(
            self.image["logo"], (self.size * 0.9, self.size * 0.5)
        )
        rect = self.image["logo"].get_rect(
            center=(self.screen_x / 2, self.screen_y / 4)
        )
        screen.blit(self.image["logo"], rect)

        rect = self.text["menu"].get_rect(
            center=(self.screen_x / 2, self.screen_y * 0.8)
        )
        screen.blit(self.text["menu"], rect)

        return screen, True

    def game_over(self, screen):
        screen = self.resize(screen)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return screen, True

            if event.type == pygame.QUIT:
                self.running = False
        if self.winner == "X":
            screen.blit(self.text["x_wins"], self.text_coords)
        if self.winner == "O":
            screen.blit(self.text["o_wins"], self.text_coords)
        if self.winner == "Z":
            screen.blit(self.text["game_tie"], self.text_coords)
        return screen, False

def main():
    # pygame setup #
    pygame.init()
    screen = pygame.display.set_mode((500, 500), pygame.RESIZABLE)
    clock = pygame.time.Clock()
    pygame.display.set_caption("Column Clash by: Andrew Roddy")
    ##################

    g = Connect4()

    # While the game is running

    menu = True
    while g.running:
        screen = g.resize(screen)
        if menu == True:
            screen.fill("aliceblue")
            screen, menu = g.main_menu(screen)
            if menu == False:
                g.reset()
                screen = g.draw_board(screen)

        elif g.game_running == False:
            screen.fill("aliceblue")
            screen = g.draw_board(screen)
            screen, g.game_running = g.game_over(screen)

            if g.game_running == True:
                menu = True
        else:
            # Draw from back to front

            g.colum_select()
            # Draws the pieces on the board
            screen.fill("aliceblue")
            screen = g.draw_board(screen)
            if g.player == "X" and g.game_running:
                screen.blit(g.text["x_text"], g.text_coords)
            if g.player == "O" and g.game_running:
                screen.blit(g.text["o_text"], g.text_coords)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.QUIT:
                    g.running = False
            # Runs pygame
        pygame.display.flip()  # displays to screen
        clock.tick(60)  # limits FPS to 60

    pygame.quit()


if __name__ == "__main__":
    main()
"""
# TODO

# Add algorithms for different difficulties

# Make it so the board resets only after making a move

# Fix the other meny

# Make the game mode selection keys more obvious
"""
