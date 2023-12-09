import sys
import cProfile
from sudoku_io import read_sudoku, print_sudoku
from sudoku_solver import is_valid, solve_sudoku

if len(sys.argv) < 2:
    print("Please provide the input file name.")
    sys.exit(1)
filename = sys.argv[1]
board = read_sudoku(filename)
profiler = cProfile.Profile()
profiler.enable()
if solve_sudoku(board):
    print_sudoku(board)
else:
    print("No solution exists.")
profiler.disable()
profiler.print_stats()