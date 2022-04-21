#
# David Smedberg, Meriem Falih, Brandon Rauenhorst, Gabriel Silva de Oliveira, Annabelle Steed, and Cameron Swan
# 4/21-26/2022
# Tic Tac Toe Project
#

print("Welcome to Tic Tac Toe!")
row1 = ["-", "-", "-"]
row2 = ["-", "-", "-"]
row3 = ["-", "-", "-"]

def main():
    printBoard()
    victoryCheck = []
    playerTurn = 1
    while True:
        print("Player 1 Turn")
        playerTurn = 1
        print(0, 1, 2)
        print(3, 4, 5)
        print(6, 7, 8)
        p1 = int(input("Enter value of board space you wish to place a marker on: "))
        placeTic(playerTurn, p1)

        victoryCheck = gameCheck()
        if victoryCheck[0]:
            print("Player 1 wins!")
            break
        elif victoryCheck[1]:
            print("Player 2 wins!")
            break
        elif victoryCheck[2]:
            print("Draw!")
            break
        printBoard()
        print("Player 2 Turn")
        playerTurn = 2
        print(0, 1, 2)
        print(3, 4, 5)
        print(6, 7, 8)
        p2 = int(input("Enter value of board space you wish to place a marker on: "))
        placeTic(playerTurn, p2)

        victoryCheck = gameCheck()
        if victoryCheck[0]:
            print("Player 1 wins!")
            break
        elif victoryCheck[1]:
            print("Player 2 wins!")
            break
        elif victoryCheck[2]:
            print("Draw!")
            break
        printBoard()

    print("\nGame over")
    printBoard()

def placeTic(playerTurn, player):
    spaceTaken = False
    if playerTurn == 2:
        while True:
            if player >= 6 and player <= 8:
                if row3[player-6] != "-":
                    print("Space taken!")
                    spaceTaken = True
                    player = int(input("Enter value of board space you wish to place a marker on: "))
                else:
                    row3[player-6] = "O"
                    spaceTaken = False
            if player >= 3 and player <= 5:
                if row2[player-3] != "-":
                    print("Space taken!")
                    spaceTaken = True
                    player = int(input("Enter value of board space you wish to place a marker on: "))
                else:
                    row2[player-3] = "O"
                    spaceTaken = False
            if player <= 2:
                if row1[player] != "-":
                    print("Space taken!")
                    spaceTaken = True
                    player = int(input("Enter value of board space you wish to place a marker on: "))
                else:
                    row1[player] = "O"
                    spaceTaken = False
                    break
            if player >= 6 and player <= 8:
                if row3[player-6] == "O" and not spaceTaken:
                    break
            elif player >= 3 and player <= 5:
                if row2[player-3] == "O" and not spaceTaken:
                    break
            elif player <= 2:
                if row1[player] == "O" and not spaceTaken:
                    break
            else:
                while player not in range(0, 9):
                    print("Space not found")
                    player = int(input("Enter value of board space you wish to place a marker on: "))
    else:
        while True:
            if player >= 6 and player <= 8:
                if row3[player-6] != "-":
                    print("Space taken!")
                    spaceTaken = True
                    player = int(input("Enter value of board space you wish to place a marker on: "))
                else:
                    row3[player-6] = "X"
                    spaceTaken = False
            if player >= 3 and player <= 5:
                if row2[player-3] != "-":
                    print("Space taken!")
                    spaceTaken = True
                    player = int(input("Enter value of board space you wish to place a marker on: "))
                else:
                    row2[player-3] = "X"
                    spaceTaken = False
            if player <= 2:
                if row1[player] != "-":
                    print("Space taken!")
                    spaceTaken = True
                    player = int(input("Enter value of board space you wish to place a marker on: "))
                else:
                    row1[player] = "X"
                    spaceTaken = False
                    break
            if player >= 6 and player <= 8:
                if row3[player-6] == "X" and not spaceTaken:
                    break
            elif player >= 3 and player <= 5:
                if row2[player-3] == "X" and not spaceTaken:
                    break
            elif player <= 2:
                if row1[player] == "X" and not spaceTaken:
                    break
            else:
                while player not in range(0, 9):
                    print("Space not found")
                    player = int(input("Enter value of board space you wish to place a marker on: "))

def printBoard():
    print("\nPrinting board...")
    print(row1)
    print(row2)
    print(row3)

def gameCheck():
    if row1[0] == row1[1] and row1[0] == row1[2]:
        if row1[0] == "X":
            return True, False, False
        elif row1[0] == "O":
            return False, True, False
    if row2[0] == row2[1] and row2[0] == row2[2]:
        if row2[0] == "X":
            return True, False, False
        elif row2[0] == "O":
            return False, True, False
    if row3[0] == row3[1] and row3[0] == row3[2]:
        if row3[0] == "X":
            return True, False, False
        elif row3[0] == "O":
            return False, True, False
    if row1[0] == row2[0] and row1[0] == row3[0]:
        if row1[0] == "X":
            return True, False, False
        elif row1[0] == "O":
            return False, True, False
    if row1[1] == row2[1] and row1[1] == row3[1]:
        if row1[1] == "X":
            return True, False, False
        elif row1[1] == "O":
            return False, True, False
    if row1[2] == row2[2] and row1[2] == row3[2]:
        if row1[2] == "X":
            return True, False, False
        elif row1[2] == "O":
            return False, True, False
    if row1[0] == row2[1] and row1[0] == row3[2]:
        if row1[0] == "X":
            return True, False, False
        elif row1[0] == "O":
            return False, True, False
    if row1[2] == row2[1] and row1[2] == row3[0]:
        if row1[2] == "X":
            return True, False, False
        elif row1[2] == "O":
            return False, True, False
    if ('-' not in row1) and ('-' not in row2) and ('-' not in row3):
        return False, False, True
    return False, False, False


main()
