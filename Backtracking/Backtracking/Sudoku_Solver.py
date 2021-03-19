'''
Sudoku Solver

Given a 9*9 sudoku board, in which some entries are filled and others are 0 (0 indicates that the cell is empty), you need to find out whether the Sudoku puzzle can be solved or not i.e. return true or false.

Input Format :
9 Lines where ith line contains ith row elements separated by space

Output Format :
true or false

Sample Input :
9 0 0 0 2 0 7 5 0 
6 0 0 0 5 0 0 4 0 
0 2 0 4 0 0 0 1 0 
2 0 8 0 0 0 0 0 0 
0 7 0 5 0 9 0 6 0 
0 0 0 0 0 0 4 0 1 
0 1 0 0 0 5 0 8 0 
0 9 0 0 7 0 0 0 4 
0 8 2 0 4 0 0 0 6

Sample Output :
true
'''

def isSafe(board, row, col, num):
    return not usedInRow(board, row, num) and not usedInCol(board, col, num) and not usedInBox(board, row-row%3, col-col%3, num)

def usedInBox(board, boxStartRow, boxStartCol, num):
    for row in range(3):
        for col in range(3):
            if board[row+boxStartRow][col+boxStartCol] == num:
                return True
        return False

def usedInCol(board, col, num):
    for row in range(9):
        if board[row][col] == num:
            return True
    return False

def usedInRow(board, row, num):
    for col in range(9):
        if board[row][col] == num:
            return True
    return False

def findUnassignedLocation(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j, True
    return i, j, False
    
def solveSudoku(board):
    #Implement Your Code Here
    row, col, unassigned = findUnassignedLocation(board)
    if not unassigned:
        return True
    
    for i in range(1, 10):
        if isSafe(board, row, col, i):
            board[row][col] = i
            if solveSudoku(board):
                return True
            else:
                board[row][col] = 0
    
    return False

board = [[ int(ele) for ele in input().split() ]for i in range(9)]
ans = solveSudoku(board)
if ans is True:
    print('true')
else:
    print('false')