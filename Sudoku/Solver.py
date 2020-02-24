import numpy as np
import random

def printBoard(board):
    ''' print a 9 x 9 matrix in sudoku format,
        where zeros are empty spaces.
        0 0 0 | 0 0 0 | 0 0 0 
        0 0 0 | 0 0 0 | 0 0 0 
        0 0 0 | 0 0 0 | 0 0 0 
        ---------------------
        0 0 0 | 0 0 0 | 0 0 0 
        0 0 0 | 0 0 0 | 0 0 0 
        0 0 0 | 0 0 0 | 0 0 0 
        ---------------------
        0 0 0 | 0 0 0 | 0 0 0 
        0 0 0 | 0 0 0 | 0 0 0 
        0 0 0 | 0 0 0 | 0 0 0 
    '''
    for i,row in enumerate(board):
        for j,n in enumerate(row):
            print(n,end=' ')
            if j in [2,5]:
                print('|',end=' ')
        print()
        if i in [2,5]:
            print('-'*21)

def getRow(mat,i):
    ''' return the ith row '''
    return mat[i]

def getCol(mat,j):
    ''' return the jth col '''
    result = []
    for row in mat:
        result.append(row[j])

    return result

def getSquare(mat,i,j):
    ''' return a 1D array representing
        the 3 x 3 bloc the element with index (i,j) is in
    '''
    return [mat[i//3 * 3 + n][j//3 * 3 + m] for n in range(3) for m in range(3)]

def getNb(mat,i,j):
    l = list(dict.fromkeys(getRow(mat,i) + getCol(mat,j) + getSquare(mat,i,j)))
    l.remove(0)
    return l

def possibleVal(mat,i,j):
    l = [i for i in range(1,10)]
    for x in getNb(mat,i,j):
        l.remove(x)
    return l

def solveSudoku(board):
    # look for completness
    done = False

    while not done:
        done = True
        # row index
        for i in range(9):
            
            # col index
            for j in range(9):
                
                # empty if is 0
                if board[i][j] == 0:
                    done = False

                    # if only 1 value fit then it is correct
                    ans = possibleVal(board,i,j)
                    if len(ans) == 1:
                        board[i][j] = ans[0]
                            

# init a 9 x 9 matrix with zeros
board = [[0]*9 for i in range(9)]
board = [[random.randint(1,9) for i in range(9)] for i in range(9)]
board = [[5,3,0,0,7,0,0,0,0],
         [6,0,0,1,9,5,0,0,0],
         [0,9,8,0,0,0,0,6,0],
         [8,0,0,0,6,0,0,0,3],
         [4,0,0,8,0,3,0,0,1],
         [7,0,0,0,2,0,0,0,6],
         [0,6,0,0,0,0,2,8,0],
         [0,0,0,4,1,9,0,0,5],
         [0,0,0,0,8,0,0,7,9]]
         
##printBoard(board)
##print()
##solveSudoku(board)
##printBoard(board)
##




