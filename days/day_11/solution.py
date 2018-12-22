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


def find_square(row, col, board, square):
    return np.sum(board[col: col+square, row: row+square])


def task(input_data, grid_x, grid_y, squares):
    board = np.zeros((grid_x, grid_y))
    for row in range(grid_x):
        for col in range(grid_y):
            board[col, row] = power(col, row, input_data)
    max_score = 0
    good_coords = [0, 0]
    best_square = 0
    for square in squares:
        for row in range(grid_x-square+1):
            for col in range(grid_y-square+1):
                score = find_square(col, row, board, square=square)
                if score > max_score:
                    max_score = score
                    good_coords = [row, col]
                    best_square = square
    return good_coords, best_square


print('Task One: ', task(2187, 300, 300, squares=[3]))
print('Task Two: ', task(2187, 300, 300, squares=range(1, 301)))

