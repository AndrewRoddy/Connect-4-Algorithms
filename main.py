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
        self.player = "".join(random.choices(["X", "O"])) # Selectes a random starting player
        self.game_running = True # Checks if the game is running
        self.winner = "" # The winner of the game
        self.mode = "pvp" # Current Gamemode
        self.running = True # Checks if pygame is running
        self.size = 500 # The smallest screen dimension
        self.generate_text() # Generates the text
        self.generate_image() # Generates the images

    def resize(self, screen):
        try: # Creates a past screen size variable
            past_x, past_y = self.screen_x, self.screen_y
        except AttributeError:
            past_x, past_y = 0, 0
            
        self.screen_x, self.screen_y = screen.get_size() # Creates current screen size variables

        if past_x != self.screen_x or past_y != self.screen_y: # Checks if the screen size has changed
            if self.screen_x > self.screen_y:
                self.size = self.screen_y
            else:
                self.size = self.screen_x
            self.generate_text() # Regenerates images and text using current size metrics
            self.generate_image()


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

    def draw_board(self, screen) -> None:
        icons = [self.image["orange_chip"], self.image["blue_chip"]]
        players = ["X", "O"]

        self.image["blue_chip"] = pygame.transform.scale(
            self.image["blue_chip"], (self.size * 0.1, self.size * 0.1)
        )
        self.image["orange_chip"] = pygame.transform.scale(
            self.image["orange_chip"], (self.size * 0.1, self.size * 0.1)
        )
        for i in range(len(self.board[0])):
            for j in range(len(self.board)):
                for k in range(len(icons)):
                    if self.board[j][i] == players[k]:
                        screen.blit(
                            icons[k],
                            (
                                ((i + self.size / 1500) * (self.size / 7.5)),
                                (
                                    (j + self.size / 1500) * (self.size / 7)
                                    + self.size * 0.1
                                ),
                            ),
                        )
        screen = self.draw_text(screen, "numbers")
        return screen

    def colum_select(self, mode="pvp"):
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
                            return True

                if event.type == pygame.QUIT:
                    self.running = False
        if mode == "random" and self.player == "O":
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

        font = pygame.font.Font(None, 74)
        text_dict = {
            "x_text": font.render("O", True, "orange"),
            "o_text": font.render("O", True, "blue"),
            "x_wins": font.render("ORANGE WINS", True, "orange"),
            "o_wins": font.render("BLUE WINS", True, "blue"),
            "game_tie": font.render("TIE", True, "black"),
        }

        font = pygame.font.Font(None, 32)
        text_dict["numbers"] = font.render(
            "  1         2         3         4         5          6         7",
            True,
            "black",
        )
        text_dict["menu"] = font.render("Press Space To Begin", True, "black")
        self.text = text_dict

    def draw_text(self, screen, key):
        if key == "x_wins":
            screen.blit(self.text["x_wins"], (200, 15))
        if key == "o_wins":
            screen.blit(self.text["o_wins"], (200, 15))
        if key == "game_tie":
            screen.blit(self.text["game_tie"], ((200, 15)))
        if key == "x_text":
            screen.blit(self.text["x_text"], (240, 20))
        if key == "o_text":
            screen.blit(self.text["o_text"], (240, 20))
        if key == "numbers":
            screen.blit(self.text["numbers"], (30, 50))
            screen.blit(self.text["numbers"], (30, 480))
        if key == "menu":
            screen.blit(self.text["menu"], (240, 20))

        return screen

    def generate_image(self):
        image_dict = {
            "blue_chip": pygame.image.load("images\\blue_chip.png"),
            "orange_chip": pygame.image.load("images\\orange_chip.png"),
            "space_button": pygame.image.load("images\\space_button.png"),
            "logo": pygame.image.load("images\\logo.png"),
        }
        # Using blit to copy content from one surface to other
        self.image = image_dict
        return image_dict

    def main_menu(self, screen):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return False, screen
            if event.type == pygame.QUIT:
                self.running = False
        screen.fill("white")

        self.image["space_button"] = pygame.transform.scale(
            self.image["space_button"], (self.size * 0.5, self.size * 0.25)
        )
        rect = self.image["space_button"].get_rect(
            center=(self.screen_x / 2, self.screen_y * 0.6)
        )
        screen.blit(self.image["space_button"], rect)

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

        return True, screen

    def game_over(self, screen):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return True, screen
            if event.type == pygame.QUIT:
                self.running = False
        if self.winner == "X":
            self.draw_text(screen, "x_wins")
        if self.winner == "O":
            self.draw_text(screen, "o_wins")
        if self.winner == "Z":
            self.draw_text(screen, "game_tie")
        return (
            False,
            screen,
        )


def main():
    # pygame setup #
    pygame.init()
    screen = pygame.display.set_mode((500, 500), pygame.RESIZABLE)
    clock = pygame.time.Clock()
    pygame.display.set_caption("Column Clash by: Andrew Roddy")

    ################

    g = Connect4()

    mode = "pvp"
    # While the game is running

    menu = True
    while g.running:
        g.resize(screen)
        if menu == True:
            screen.fill("aliceblue")
            menu, screen = g.main_menu(screen)
            if menu == False:
                g = Connect4()
                screen = g.draw_board(screen)

        elif g.game_running == False:
            screen.fill("aliceblue")
            screen = g.draw_board(screen)
            g.game_running, screen = g.game_over(screen)

            if g.game_running == True:
                g = Connect4()
                screen = g.draw_board(screen)
        else:
            # Draw from back to front

            g.colum_select(mode)
            # Draws the pieces on the board
            screen.fill("aliceblue")
            screen = g.draw_board(screen)
            if g.player == "X" and g.game_running:
                screen = g.draw_text(screen, "x_text")
            if g.player == "O" and g.game_running:
                screen = g.draw_text(screen, "o_text")

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

# Seperate functions into different files

# Add Bot Opponents
# Random
# Easy
# AI
# Add Difficulty
# Make it so the user can choose their icon
# Add Online Play
"""
