'''
    Richard Elgar
    SDEV220
    Tic-Tac-Toe Game
    Due: 28 Sep 21

In a game of tic-tac-toe, two players take turns marking an available cell in a grid with their respective tokens (either X or O). 
-- When one player has placed three tokens in a horizontal, vertical, or diagonal row on the grid, the game is over and that player has won. 
-- A draw (no winner) occurs when all the cells in the grid have been filled with tokens and neither player has achieved a win. 

Create a program for playing tic-tac-toe. The program prompts two players to alternately enter an X token and an O token. 
Whenever a token is entered, the program redisplays the board on the console and determines the status of the game (win, draw, or continue). 
'''

#   prints the board
def printBoard(board):
    print("\n\n")
#   nested for each loops; rows -> cols
    for row in range(3):
        for col in range(3):
#   0 == no player; 1 == player 1 -> print 'X'; 2 == player2 -> print 'O'
            if(board[row][col] == 1):
                print("| X",end=" |")
            elif(board[row][col] == 2):
                print("| O",end=" |")
            else:
                print("| ",end="    ")
        if(row == 0 or row == 1):               #
            print("\n-----------------")        #   formatting for board
    print("\n\n")                               #


#   checks the board to see if the player has won
def checkWinner(board,playerNum):
#   check each row for horizontal win
    for row in board:
        if(row[0] == playerNum and row[1] == playerNum and row[2] == playerNum):
            return True

#   check each column for vertical win
    for col in range(3):
        if(board[0][col] == playerNum and board[1][col] == playerNum and board[2][col] == playerNum):
            return True

#   check for diagonal wins
    if((board[0][0] == playerNum and board[1][1] == playerNum and board[2][2] == playerNum) or
        (board[0][2] == playerNum and board[1][1] == playerNum and board[2][0] == playerNum)):
        return True

    return False


#   checks for a draw -- if no more spaces on the board are available, and neither player has won -- the game is a draw
def checkDraw(board):
    for row in board:
        for col in row:
            if col == 0:
                return False
    return True


#   checks to make sure input is valid (0, 1 or 2) and then checks to make sure the space entered hasn't already been taken
def validMove(board,playerTurn,inpRow,inpCol):
    if(0 <= inpRow <= 2) and (0 <= inpCol <= 2):
        if(board[inpRow][inpCol] == 0):
            return True
        else:
            print("INVALID MOVE -- Space has already been taken. Try again.")
            return False
    else:
        print("INVALID MOVE -- input must be 0, 1, or 2.")
        return False


#   Start of game -- init board. set all spaces on board to 0
#   Player 1/X sets board vals to 1; Player 2/O sets board vals to 2
board = [   [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
        
printBoard(board)
playerTurn = 1              #  player 1 goes first

#   while loop repeats turns until a player has won or there is a draw
while(  (not checkDraw(board)) and (not checkWinner(board,1)) and (not checkWinner(board,2))    ):

#   input from player for row, then col
    print("\nPLAYER ",playerTurn," ...")
    inputRow = int(input(" -- Enter a row(0, 1, or 2): "))
    inputCol = int(input(" -- Enter a column(0, 1, or 2): "))

#   inner while loop validates input -- player must input 0, 1 or 2 for row/col vals, and that spot on the board must not have been taken already
    while not validMove(board,playerTurn,inputRow,inputCol):
        print("Invalid values entered. Try again...")
        print("PLAYER ",playerTurn," ...")
        inputRow = int(input(" -- Enter a row(0, 1, or 2): "))
        inputCol = int(input(" -- Enter a column(0, 1, or 2): "))

#   set space on board to players value using playerTurn var then print board
    board[inputRow][inputCol] = playerTurn
    printBoard(board)

#   check board for winner
    if checkWinner(board,playerTurn):
        print("PLAYER ",playerTurn," HAS WON.")
        break

    if checkDraw(board):
        print("DRAW -- NO WINNER")
        break

#   change player turn
    if playerTurn == 1:
        playerTurn = 2
    elif playerTurn == 2:
        playerTurn = 1
