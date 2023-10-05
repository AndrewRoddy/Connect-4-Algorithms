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
        self.running = True
        self.size = 500

    def resize(self, screen):
        self.screen_x, self.screen_y = screen.get_size()
        if self.screen_x > self.screen_y:
            self.size = self.screen_y
        else:
            self.size = self.screen_x
        

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
                break

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
        icons = [image["red_chip"], image["blue_chip"]]
        players = ["X", "O"]
        
        image["red_chip"] = pygame.transform.scale(image["red_chip"], (self.size * 0.9, self.size * 0.8))
        rect = image["red_chip"].get_rect(center=(self.screen_x/2, self.screen_y/4))
        screen.blit(image["red_chip"], rect)

        image["red_chip"] = pygame.transform.scale(image["red_chip"], (self.size/10, self.size/10))
    
        for i in range(len(self.board[0])):
            for j in range(len(self.board)):
                for k in range(len(icons)):
                    if self.board[j][i] == players[k]:
                        """
                        i is 0 - 6 horizontal
                        j is 0 - 5 and vertical
                        for j
                        ((0 + 500/1000) * (500/7)) - 500 / 20 = 10.7
                        ((5 + 500/1000) * (500/7)) - 500 / 20 = 367.
                        
                        for i
                        ((6 + 500/1000) * (500/7)) - 500 / 20 = 493.2
                        """
                        screen.blit(
                            icons[k],
                            ((

                                (((i + self.size / 1500) * (self.size / 6))),
                                (((j + self.size / 1500) * (self.size / 7)))
                                ),),
                        )
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
            "blue_chip": pygame.image.load("images\\blue.png"),
            "red_chip": pygame.image.load("images\\red.png"),
            "space_button": pygame.image.load("images\\space.png"),
            "logo": pygame.image.load("images\\logo.png"),
        }
         # Using blit to copy content from one surface to other
        return image

    def main_menu(self, screen, text, image):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return False, screen
            if event.type == pygame.QUIT:
                self.running = False
        screen.fill("white")
        
        image["space_button"] = pygame.transform.scale(image["space_button"], (self.size * 0.5, self.size * 0.25))
        rect = image["space_button"].get_rect(center=(self.screen_x/2, self.screen_y * 0.6))
        screen.blit(image["space_button"], rect)
        
        image["logo"] = pygame.transform.scale(image["logo"], (self.size * 0.9, self.size * 0.5))
        rect = image["logo"].get_rect(center=(self.screen_x/2, self.screen_y/4))
        screen.blit(image["logo"], rect)
        
        rect = text["menu"].get_rect(center=(self.screen_x/2, self.screen_y * 0.8))
        screen.blit(text["menu"], rect)
        
        return True, screen

    def game_over(self, screen, text):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return True, screen
            if event.type == pygame.QUIT:
                self.running = False
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
    screen = pygame.display.set_mode((500, 500),pygame.RESIZABLE)
    clock = pygame.time.Clock()
    pygame.display.set_caption("Connect 4            -Andrew Roddy")
    
    ################

    g = Connect4()
    text = g.generate_text()
    image = g.generate_image()

    mode = "pvp"
    # While the game is running

    menu = True
    while g.running:
        g.resize(screen)
        if menu == True:
            menu, screen = g.main_menu(screen, text, image)

        elif g.game_running == False:
            g.game_running, screen = g.game_over(screen, text)
            if g.game_running == True:
                g = Connect4()
        else:
            # Draw from back to front
            screen.fill("aliceblue")

            g.colum_select(mode)

            # Draws the pieces on the board
            screen = g.draw_board(screen, image)
            screen = g.draw_text(screen, text, "numbers")
            if g.player == "X" and g.game_running:
                screen = g.draw_text(screen, text, "x_text")
            if g.player == "O" and g.game_running:
                screen = g.draw_text(screen, text, "o_text")

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
