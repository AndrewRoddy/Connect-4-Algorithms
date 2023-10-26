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
        self.mode = "pvp"  # Current Gamemode
        self.running = True  # Checks if pygame is running
        
        self.screen = pygame.display.set_mode((500, 500), pygame.RESIZABLE)
        # On Laptop screen.size = 649 fullscreen
        # On Desktop screen.size = 1369 fullscreen
        self.size = 500  # The smallest screen dimension
        self.center = 0  # The positive difference of y and x
        self.generate_text()  # Generates the text
        self.generate_image()  # Generates the images

    def resize(self):
        try:  # Creates a past screen size variable
            past_x, past_y = self.screen_x, self.screen_y
        except AttributeError:
            past_x, past_y = 0, 0

        (
            self.screen_x,
            self.screen_y,
        ) = self.screen.get_size()  # Creates current screen size variables
        
        if (
            past_x != self.screen_x or past_y != self.screen_y
        ):  # Checks if the screen size has changed
            if self.screen_x > self.screen_y:
                self.size = self.screen_y
            else:
                self.size = self.screen_x
            
            self.center = (
                (self.size - self.screen_x) * (-0.385)
                )
            
            self.generate_text()  # Regenerates images and text using current size metrics
            self.generate_image()
            self.text_coords = (self.screen_x / 2.15, self.size / 50)
            screen = self.refresh_screen(screen)
            
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

    def draw_board(self):
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
                self.center +
                (self.size / 25) + # Adds to adjust for text
                (i + self.size / 1500) # Same as chips
                * (self.size / 7.5) 
                )
            self.screen.blit(  # Top Numbers
                self.text[str(i + 1)],
                (number_x, self.size * 0.15),
            )

            self.screen.blit(  # Bottom Numbers
                self.text[str(i + 1)],
                (number_x, (self.size - self.size * 0.06)),
            )

            x_coordinate = self.center + (i + self.size / 1500) * (self.size / 7.5)
            for j in range(len(self.board)):  # 0-5
                for k in range(len(icons)):
                    if self.board[j][i] == players[k]:
                        y_coordinate = self.size / 5 + (j * self.size / 8)

                        self.screen.blit(
                            icons[k],
                            (
                                x_coordinate,
                                y_coordinate,
                            ),
                        )


    def colum_select(self, screen, mode="pvp"):
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
                            screen = self.refresh_screen(screen)
                            return screen

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
                    self.refresh_screen()
                    break
        
        
        return screen

    def refresh_screen(self, screen):
        screen.fill("aliceblue")
        screen = self.draw_board(screen)
        if self.player == "X" and self.game_running:
            screen.blit(self.text["x_text"], self.text_coords)
        if self.player == "O" and self.game_running:
            screen.blit(self.text["o_text"], self.text_coords)
            
        return screen

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
        
        for i in range(1,8): # Generates the numbers
            text_dict[str(i)] = font.render(
            str(i),
            True,
            "black",
        )

        # Generates the menu text
        text_dict["menu"] = font.render("Press Space To Begin", True, "black")
        self.text = text_dict

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

    def main_menu(self):
        self.resize()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return False
            if event.type == pygame.QUIT:
                self.running = False
        self.screen.fill("white")

        self.image["space_button"] = pygame.transform.scale(
            self.image["space_button"], (self.size * 0.5, self.size * 0.25)
        )
        rect = self.image["space_button"].get_rect(
            center=(self.screen_x / 2, self.screen_y * 0.6)
        )
        self.screen.blit(self.image["space_button"], rect)

        self.image["logo"] = pygame.transform.scale(
            self.image["logo"], (self.size * 0.9, self.size * 0.5)
        )
        rect = self.image["logo"].get_rect(
            center=(self.screen_x / 2, self.screen_y / 4)
        )
        self.screen.blit(self.image["logo"], rect)

        rect = self.text["menu"].get_rect(
            center=(self.screen_x / 2, self.screen_y * 0.8)
        )
        self.screen.blit(self.text["menu"], rect)

        return True

    def game_over(self):
        self.resize()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return True
                
            if event.type == pygame.QUIT:
                self.running = False
        if self.winner == "X":
            self.screen.blit(self.text["x_wins"], self.text_coords)
        if self.winner == "O":
            self.screen.blit(self.text["o_wins"], self.text_coords)
        if self.winner == "Z":
            self.screen.blit(self.text["game_tie"], self.text_coords)
        return False


def main():
    # pygame setup #
    pygame.init()
    screen = pygame.display.set_mode((500, 500), pygame.RESIZABLE)
    clock = pygame.time.Clock()
    pygame.display.set_caption("Column Clash by: Andrew Roddy")

    ################

    g = Connect4()
    #g.screen = screen
    mode = "pvp"
    # While the game is running

    menu = True
    while g.running:
        screen = g.resize(screen)
        if menu == True:
            g.screen.fill("aliceblue")
            menu = g.main_menu()
            if menu == False:
                g = Connect4()
                g.draw_board()

        elif g.game_running == False:
            g.screen.fill("aliceblue")
            g.draw_board()
            g.game_running = g.game_over()

            if g.game_running == True:
                g = Connect4()
                g.draw_board()
        else:
            # Draw from back to front

            screen = g.colum_select(screen, mode)
            
            # Draws the pieces on the board
            


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
