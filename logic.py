from gui import board , board_cols,board_rows
import math
def mark_square(row , col , player):
    """
    put a player in a square

    Args:
        row (int): int which determine we are on which row
        col (int): int which determine we are on which col
        player (int): player = 1 : manual gamer , player = 2 : ai 
    """
    board[row][col] = player

def availabe_squares(row , col):
    return board[row][col] == 0

def if_board_isfull (check_board = board):
    """
    Check if board is full by checking if all indexs equal to 0 

    Args:
        check_board (_type_, optional): equal to board to not make any changes in the board we are playing on . Defaults to board.

    Returns:
        return true if its full false if its not 
    """
    for row in range(board_rows):
        for col in range(board_cols):
            if check_board[row][col] == 0 :
                return False
    return True

def check_win(player , check_board = board):
    """
    check if there is a winner by checking x o rules 

    Args:
        player (int): if we pass the value of 1 and 2 
        check_board (matrix): equal to board to not make any changes in the board we are playing on . Defaults to board.

    Returns:
        True if we have a win situation
    """
    for col in range(board_cols):
        if check_board[0][col] == player and check_board[1][col]==player and check_board[2][col]==player:
            return True
    for row in range(board_rows):
        if  check_board[row][0] == player and check_board[row][1]==player and check_board[row][2]==player:
            return True
    if check_board[0][0] == player and check_board[1][1] == player and check_board[2][2] == player:
        return True
    elif check_board[0][2] == player and check_board[1][1] == player and check_board[2][0] == player :
        return True
    return False


def minmax(minmax_board , depth , is_maximizing , alpha , beta):
    """
    if this is False so we are in ai mode which try to get best case and best score 
    , we check all the squaress if one is 0 so we insert a value of player (2) and we make score = recuse the function untill we get the last value 
    dont forget to pass the maximizing as false to make next turn it the player turn the check the max value , then we check the max value of score and best score and put the best score with such low value
    ,
    now the other case when its player turn we try to minimize what player will do and we get the minimum from best score and current score 
    we do it reccursivly till the base case which checks who win  (check win is function has rules of x o ) => will return who win
    Args:
        minmax_board (matrix): board we are playing on 
        depth (list): depth of the tree
        is_maximizing (bool): determine if we in a player state or ai state

    Returns:
      int : best score between current and the one returning from recursion
    """
    if check_win(2,minmax_board):
        return float('inf')
    elif check_win(1 , minmax_board):
        return float('-inf')
    elif if_board_isfull(minmax_board):
        return 0
    if is_maximizing : 
        best_score = float('-inf')
        for row in range(board_rows):
            for col in range(board_cols):
                if minmax_board[row][col] == 0:
                    minmax_board[row][col] = 2
                    score = minmax(minmax_board , depth +1 , False , alpha , beta) # false because player will do the worst thing to the ai 
                    minmax_board[row][col] = 0 
                    best_score = max(score , best_score)
                    alpha = max(alpha , score)
                    if beta <= alpha :
                        break
        return best_score
    else :
        best_score = float('inf')
        for row in range(board_rows):
            for col in range(board_cols):
                if minmax_board[row][col] == 0:
                    minmax_board[row][col] = 1
                    score = minmax(minmax_board , depth +1 , True ,alpha , beta ) # false because player will do the worst thing to the ai 
                    minmax_board[row][col] = 0 
                    best_score = min(score , best_score)
                    beta = min(beta , score)
                    if beta <= alpha :
                        break
        return best_score
    

def bestmove():
     """

     
     Keyword arguments:
        
        Return: return_description
     """
     
     best_score = -1000
     move = (-1,-1)
     for row in range(board_rows):
         for col in range(board_cols):
             if board[row][col] == 0:
                 board[row][col] = 2
                 score = minmax(board , 0, False , float('-inf'), float('inf') )
                 board[row][col] = 0 
                 if score > best_score:
                     best_score = score 
                     move = (row , col )
     if move != (-1,-1):
         mark_square(move[0] , move[1] , 2)
         return True
     return False