# All code written by Andrew Roddy

def AsciiArt():
    return "\n   ____                            _     _  _\n  / ___|___  _ __  _ __   ___  ___| |_  | || |\n | |   / _ \| '_ \| '_ \ / _ \/ __| __| | || |_\n | |__| (_) | | | | | | |  __/ (__| |_  |__   _|\n  \____\___/|_| |_|_| |_|\___|\___|\__|    |_|\n\n\n"



def Empty_Board():
    return [
        ["_", "_", "_", "_", "_", "_", "_"],
        ["_", "_", "_", "_", "_", "_", "_"],
        ["_", "_", "_", "_", "_", "_", "_"],
        ["_", "_", "_", "_", "_", "_", "_"],
        ["_", "_", "_", "_", "_", "_", "_"],
        ["_", "_", "_", "_", "_", "_", "_"],
    ]


def DisplayBoard(board):
    print("1 2 3 4 5 6 7")
    for i in range(len(board)):
        print(*board[i], sep=" ")
        
    print("1 2 3 4 5 6 7")


def playerTurn(board, column):
    for i in range(len(board[column])):
        if board[i][column] == "_":
            board[i][column] = "X"
    
    return board
     


def checkWinVert():
    global GameRunning, Winner
    check, check2, check3, check4, finder = -1, 6, 13, 20, False
    while finder == False:
        check += 1
        check2 += 1
        check3 += 1
        check4 += 1
        if (
            board[check] == player
            and board[check2] == player
            and board[check3] == player
            and board[check4] == player
        ):
            finder, GameRunning, Winner = True, False, player
        if check4 == 41:
            finder = True


def checkWinHorizontal():
    global GameRunning, Winner
    check, check2, check3, check4, finder = -1, 0, 1, 2, False
    while finder == False:
        check += 1
        check2 += 1
        check3 += 1
        check4 += 1
        if (
            board[check] == player
            and board[check2] == player
            and board[check3] == player
            and board[check4] == player
        ):
            finder, GameRunning, Winner = True, False, player
        if check4 == 6 or check4 == 13 or check4 == 20 or check4 == 27 or check4 == 34:
            check += 3
            check2 += 3
            check3 += 3
            check4 += 3
        if check4 == 41:
            finder = True


def checkWinDiagnol():
    global GameRunning, Winner
    check, check2, check3, check4, finder = 20, 14, 8, 2, False
    while finder == False:
        check += 1
        check2 += 1
        check3 += 1
        check4 += 1
        if (
            board[check] == player
            and board[check2] == player
            and board[check3] == player
            and board[check4] == player
        ):
            finder, GameRunning, Winner = True, False, player
        if check4 == 6 or check4 == 13:
            check += 3
            check2 += 3
            check3 += 3
            check4 += 3
        if check4 == 20:
            finder = True


def checkWinBackDiag():
    global GameRunning, Winner
    check, check2, check3, check4, finder = -1, 7, 15, 23, False
    while finder == False:
        check += 1
        check2 += 1
        check3 += 1
        check4 += 1
        if (
            board[check] == player
            and board[check2] == player
            and board[check3] == player
            and board[check4] == player
        ):
            finder, GameRunning, Winner = True, False, player
        if check4 == 27 or check4 == 34:
            check += 3
            check2 += 3
            check3 += 3
            check4 += 3
        if check4 == 41:
            finder = True


def checkWin():
    global player
    checkWinVert()
    checkWinHorizontal()
    checkWinDiagnol()
    checkWinBackDiag()


def RunGame():
    global player, turnNumber, GameRunning
    DisplayBoard()
    while GameRunning == True:
        player, turnNumber = "M", "000"
        turnNumber = input("M's Turn:  ")
        while (
            turnNumber != "1"
            and turnNumber != "2"
            and turnNumber != "3"
            and turnNumber != "4"
            and turnNumber != "5"
            and turnNumber != "6"
            and turnNumber != "7"
        ):
            turnNumber = input("M's Turn:  ")
        playerTurn()
        DisplayBoard()
        checkWin()
        if GameRunning == True:
            player, turnNumber = "O", "000"
            turnNumber = input("O's Turn:  ")
            while (
                turnNumber != "1"
                and turnNumber != "2"
                and turnNumber != "3"
                and turnNumber != "4"
                and turnNumber != "5"
                and turnNumber != "6"
                and turnNumber != "7"
            ):
                turnNumber = input("O's Turn:  ")
            playerTurn()
            DisplayBoard()
            checkWin()
    print(f"{Winner} Wins!!!")

 
def main():
    board = Empty_Board()
    while True:
        DisplayBoard(board)
        column = int(input("Where do u wanna go?"))
        board = playerTurn(board, column)
    """
        global GameRunning

        GameRunning, Winner, playAgain = True, "Nobody", "yes"

        print(AsciiArt())
        while (
        playAgain.lower() == "yes"
        or playAgain.lower() == "y"
        or playAgain.lower() == "si"
        or playAgain.lower() == "play"
        or playAgain == "1"
        ):
            GameRunning = True
            Variables()
            RunGame()
            playAgain = input("Would you like to play again?\n")
            print("Thanks for playing!!")
    """
    
if __name__ == "__main__":
    main()