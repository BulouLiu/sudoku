import pytest
from sudoku_io import read_sudoku, print_sudoku

def test_read_sudoku():
    with open("temp.txt", "w") as f:
        f.write("530070000\n600195000\n098000060\n800060003\n400803001\n700020006\n060000280\n000419005\n000080079")

    board = read_sudoku("temp.txt")

    assert board == [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    import os
    os.remove("temp.txt")

def test_print_sudoku(capsys):
    board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    print_sudoku(board)

    captured = capsys.readouterr()
    output = captured.out

    expected_output = "530|070|000\n600|195|000\n098|000|060\n---+---+---\n800|060|003\n400|803|001\n700|020|006\n---+---+---\n060|000|280\n000|419|005\n000|080|079\n"
    assert output == expected_output
