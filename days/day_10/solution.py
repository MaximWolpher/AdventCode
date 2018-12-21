import numpy as np
from input_reader import read

data = read(__file__)
test_data = read(__file__, name='test')


def parse(input_data):
    out_list = list()
    for line in input_data:
        clean_line = line.rstrip().replace(',', '')
        clean_line = clean_line.replace('>', '')
        clean_line = clean_line.replace('<', ' ')
        sub_line = [word for word in clean_line.split(' ') if word]
        out_list.append([int(num) for idx, num in enumerate(sub_line) if idx in [1, 2, 4, 5]])
    return np.asarray(out_list, dtype=int)


def draw(input_data):
    draw_data = input_data[:]
    min_x = np.min(draw_data[:, 0])
    mm_x = np.abs(min_x - np.max(draw_data[:, 0]))
    min_y = np.min(draw_data[:, 1])
    mm_y = np.abs(min_y - np.max(draw_data[:, 1]))
    print(draw_data)
    print(min_x, min_y, mm_x, mm_y)
    draw_data[:, 0] += np.abs(min_x)
    draw_data[:, 1] += np.abs(min_y)
    print(draw_data)
    board = np.zeros((mm_x+1, mm_y+1))
    print(board.shape)
    for px, py in draw_data:
        board[px, py] = 1
    print(board)


def task_one(input_data):
    pos = input_data[:, :2]
    vel = input_data[:, 2:]
    variance = 2**1000
    for seconds in range(4):
        new_variance = np.var(pos)
        print(new_variance)
        draw(pos)
        pos += vel
    return "nothing found"


parsed_test = parse(test_data)
parsed_data = parse(data)

print(task_one(parsed_test))
