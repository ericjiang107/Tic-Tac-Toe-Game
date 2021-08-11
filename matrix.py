# Write a function that prints board 
def showBoard(board):
    for i in range(len(board)):
        for j in range(len(board[i])): 
            if j < len(board[i]) - 1:
                print(board[i][j], end = " |")
            else: 
                print(board[i][j])

        if i < len(board) - 1:
            print('--+--+--')


#check for valid position 
def checkValid(board, i , j): 
    if board[i][j] != '0': 
        return False 
    return True

#function to input X into board 
def insertX(board, i, j):  
    board[i][j] = 'X'
    return board

#function to input O into board
def insertO(board, i, j): 
    board[i][j] = 'O'
    return board

# check if win by row
def checkRowWin(board, i, check): 
    for j in range(len(board[i])):
        if board[i][j] != check: 
            return False 
    return True

#check if win by col
def checkColWin(board, j, check): 
    for i in range(len(board)): 
        if board[i][j] != check: 
            return False 
    return True

#check if win by diagonal 
def checkCrossWin(board, check): 
    if board[0][0] == check and board[1][1] == check and board[2][2] == check: 
        return True
    elif board[2][0] == check and board[1][1] == check and board[0][2] == check: 
        return True
    else: 
        return False
         

#check win condition 
def checkWin(board, player1_turn, i , j):
    check = ''
    if player1_turn: 
        check = 'X'
    else: 
        check = 'O'

    print("check: ", check)
    print("check Row: ", checkRowWin(board, i, check))
    print("check col: ", checkColWin(board, j, check))
    print("check cross: ", checkCrossWin(board, check))
    return checkRowWin(board, i, check) or checkColWin(board, j, check) or checkCrossWin(board, check)

# Make a 3 by 3 matrix 
board = [['0','0','0'],['0','0','0'],['0','0','0']]
showBoard(board)


player1_turn = True # X 
player2_turn = False # O 
row = -1 
col = -1
win = False

while not win: 
    if player1_turn: 
        valid = False 
        print("\nPlayer 1 Turn")
        #player one input
        while not valid:
            row = int(input("Enter row (0,1,2) "))
            col = int(input("Enter column (0,1,2) "))
            valid = checkValid(board, row, col)
            if not valid: 
                print("Invalid input")

        insertX(board, row, col)

    else: 
        valid = False 
        print("\nPlayer 2 Turn")
        #player 2 input
        while not valid:
            row = int(input("Enter row (0,1,2) "))
            col = int(input("Enter column (0,1,2) "))
            valid = checkValid(board, row, col)
            if not valid: 
                print("Invalid input")
    
        insertO(board, row, col)

    win = checkWin(board, player1_turn, row, col)
    player1_turn = not player1_turn
    player2_turn = not player2_turn
    print("win: ", win)
    showBoard(board)

if player1_turn: 
    print("Player 2 Won!")
else: 
    print("Player 1 Won!")
    

