import sys

def read_sudoku(filename):
    with open(filename, 'r') as f:
        lines = f.read().splitlines()
    board = []
    for line in lines:
        if "---+---+---" not in line:
            row = [int(num) for num in line if num.isdigit()]
            board.append(row)
    return board

def print_sudoku(board):
    for i in range(9):
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end="")
            print(str(board[i][j]), end="")
        print()
