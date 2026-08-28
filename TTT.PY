game_board = [
    ["_", "_", "_"],
    ["_", "_", "_"],
    ["_", "_", "_"],
]

def checkifSlotisOccupied(row, column):
    if game_board[row][column] == "_":
        return False
    else: 
        return True

def printTheBoard():
    print(f"The Game Board \n------------\n{game_board[0][0]}{game_board[0][1]}{game_board[0][2]}\n{game_board[1][0]}{game_board[1][1]}{game_board[1][2]}\n{game_board[2][0]}{game_board[2][1]}{game_board[2][2]}")

def checkForVictory(playerChar):
    #Check for Vert wins
    if game_board[0][0] == playerChar and game_board[1][0] == playerChar and game_board[2][0] == playerChar: 
        return True
    if game_board[0][1] == playerChar and game_board[1][1] == playerChar and game_board[2][1] == playerChar:
        return True
    if game_board[0][2] == playerChar and game_board[1][2] == playerChar and game_board[2][2] == playerChar:
        return True

    #Check for Horiz wins
    if game_board [0][0] == playerChar and game_board [0][1] == playerChar and game_board [0][2] == playerChar:
        return True
    if game_board [1][0] == playerChar and game_board [1][1] == playerChar and game_board [1][2] == playerChar:
        return True
    if game_board [2][0] == playerChar and game_board [2][1] == playerChar and game_board [2][2] == playerChar:
        return True
    
    #Check for Diag wins
    if game_board[0][2] == playerChar and game_board[1][1] == playerChar and game_board[2][0] == playerChar:
        return True
    if game_board[0][0] == playerChar and game_board[1][1] == playerChar and game_board[2][2] == playerChar:
        return True
        
    #If the player has not won yet...
    return False

def main():
    gameIsUnderway = True
    while gameIsUnderway:
        
        # if checkForVictory("X"):
        #     print("You win")
        #     gameIsUnderway = False

        # X's Turn
        print("X! - It is your turn!")
        row = int(input("Please select a row! "))
        column = int(input("Please select a column! "))
        if checkifSlotisOccupied(row, column) == True:
            print("Big dawg, that slot is full")
            #Reset the turn
        else:
            game_board[row][column] = "X"
            printTheBoard()
            if checkForVictory("X"):
                print("X!- You have won the game!")
                gameIsUnderway = False
                break

        # O's Turn
        print("O! - It is your turn!")
        row = int(input("Please select a row! "))
        column = int(input("Please select a column! "))
        if checkifSlotisOccupied(row, column) == True:
            print("Big dawg, that slot is full")
            #Reset the turn
        else:
            game_board[row][column] = "O"
            printTheBoard()
            if checkForVictory("O"):
                print("O!- You have won the game!")
                gameIsUnderway = False
                break
    return None

if __name__ == '__main__':
    main()