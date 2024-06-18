# TicTacToe.py

playerTurn = 'X'
gameFinished = False
board = [['']*3 for _ in range(3)]
validMove = False

def updateBoard(board, row, column, playerTurn):
    print('inserting into row ' + row + ' and column ' + column)
    board[int(row)][int(column)] = playerTurn


def validateMove(board, row, column):
    # code goes here start with this method
    # return false when a move is not valid
    #  check to see if the spot is not occupied by another player if not it will override
    # make sure they put a valid number example if my input row 9 and column 9, the board is 3 by 3
    return True

#fill out the next three funciton return True if a player has 3 in a row horizontal,diagonal, or vertical 
def winnerHorizontal(board):
    # code goes here
    return False
def winnerVertical(board):
    # code goes here
    return False
def winnerDiagonal(board):
    # code goes here
    return False

def winner(board):
    if winnerHorizontal(board):
        return True
    if winnerVertical(board):
        return True
    if winnerDiagonal(board):
        return True
    return False

def main():
    global playerTurn, gameFinished, validMove
    while not gameFinished:
        inputRowMove = '-1'
        inputColumnMove = '-1'
        while not validMove:
            print(board)
            print('\n')
            print('Player ' + playerTurn + ' \n')
            inputRowMove = input('Please enter row move 0, 1, or 2\n')    
            print('Player ' + playerTurn + ' \n')
            inputColumnMove = input('Please enter column move 0, 1, or 2\n')
            validMove = validateMove(board, inputRowMove, inputColumnMove)
        updateBoard(board, inputRowMove, inputColumnMove, playerTurn)
        validMove = False
        if winner(board):
            gameFinished = True
            print('Player ' + playerTurn + ' wins')
            exit()
        else:
            playerTurn = 'O' if playerTurn == 'X' else 'X'

if __name__ == "__main__":
    main()
