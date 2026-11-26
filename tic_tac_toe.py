def createBoard():
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]
    return board

def outputBoard(board):
    print("Current Board:")
    print()
    print("  0 1 2")
    print("0 " + "|".join(board[0]))
    print("  -----")
    print("1 " + "|".join(board[1]))
    print("  -----")
    print("2 " + "|".join(board[2]))
    print()

def updateBoard(board, input_list, player):
    board[int(input_list[0])][int(input_list[1])] = player

def checkWin(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check Top-left to Bottom-right diagonal
    if all(board[i][i] == player for i in range(3)):
        return True
    # Check Top-right to Bottom-left diagonal
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True

def checkDraw(board):
    for row in board:
        if " " in row:
            return False
    return True

# Function for... (choosing a player?)
def setPlayer(player):
    if player == "X":
        return "O"
    elif player == "O":
        return "X"
    else:
        return "X" # X is starting player

# ... write as many functions as you need
def isValidMove(board, input_list):
    if len(input_list) != 2:
        print("Invalid input. Input row and column (0-2) separated by a space.")
        return False
    try:
        row = int(input_list[0])
        col = int(input_list[1])
    except ValueError:
        print("Invalid input. Input row and column (0-2) separated by a space.")
        return False
    if row < 0 or row > 2 or col < 0 or col > 2:
        print("Invalid move. Try again.")
        return False
    if board[row][col] != " ":
        print("Cell already taken. Try again.")
        return False
    return True

# Tic-tac-toe game
if __name__ == "__main__":
    # Start a new round of Tic-tac-toe
    print("Welcome to a new round of Tic-Tac-Toe!")
    number_of_games = 1
    exit_game = False

    while number_of_games < 2 or input("Do you want to play a new round? (y/n): ").lower() == "y":

        print(f"Starting game {number_of_games} ...")

        board = createBoard()
        player = setPlayer("")
        game_over = False

        while not game_over:
            outputBoard(board)
            print(f"Player {player}'s turn. Input row and column (0-2) separated by a space:")
            input_list = input().split()
            if input_list[0] == "exit":
                print("Exiting the game.")
                exit_game = True
                break

            if isValidMove(board, input_list):
                updateBoard(board, input_list, player)
            else:
                continue

            if checkWin(board, player):
                outputBoard(board)
                print(f"Player {player} wins!")
                game_over = True
            elif checkDraw(board):
                outputBoard(board)
                print("It's a draw!")
                game_over = True
            else:
                player = setPlayer(player)

        number_of_games += 1
        if exit_game:
            break
