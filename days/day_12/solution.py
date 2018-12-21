import numpy as np
from input_reader import read

data = read(__file__)
test_data = read(__file__, name='test')


def tenth(x: int) -> int:
    if x < 0:
        return 0
    else:
        return x // 100 - 10 * (x // 1000)


def power(x: int,y: int, serial: int) -> int:
    return tenth((((x + 10) * y) + serial) * (x + 10)) - 5


def find_3x3(row, col, board):
    return np.sum(board[col: col+3, row: row+3])


def task_one(input_data, grid_x, grid_y):
    board = np.zeros((grid_x, grid_y))
    for row in range(grid_x):
        for col in range(grid_y):
            board[col, row] = power(col, row, input_data)
    max_score = 0
    good_coords = [0, 0]
    for row in range(grid_x-1):
        for col in range(grid_y-1):
            score = find_3x3(col, row, board)
            if score > max_score:
                max_score = score
                good_coords = [row, col]
    return good_coords, max_score


print(task_one(2187,300,300))
