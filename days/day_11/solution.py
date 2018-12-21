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
    draw_data = input_data.copy()
    min_x = np.min(draw_data[:, 0])
    mm_x = np.abs(min_x - np.max(draw_data[:, 0]))
    min_y = np.min(draw_data[:, 1])
    mm_y = np.abs(min_y - np.max(draw_data[:, 1]))
    if min_x < 0:
        draw_data[:, 0] += np.abs(min_x)
    else:
        draw_data[:, 0] -= np.abs(min_x)
    if min_y < 0:
        draw_data[:, 1] += np.abs(min_y)
    else:
        draw_data[:, 1] -= np.abs(min_y)
    board = np.zeros((mm_x+1, mm_y+1), dtype=int)
    for px, py in draw_data:
        board[px, py] = 1
    return board.T


def task_one(input_data):
    pos = input_data[:, :2]
    vel = input_data[:, 2:]
    variance = 2**1000
    last_pos = 0
    for seconds in range(50000):
        var_y = np.var(pos[:, 1])
        if var_y > variance:
            print('seconds: ', seconds)
            return draw(last_pos)
        else:
            variance = var_y
            last_pos = pos.copy()
            pos += vel
    return "nothing found"


parsed_test = parse(test_data)
parsed_data = parse(data)

with open('result.txt', 'a') as f:
    for line in task_one(parsed_data):
        f.writelines(str(line))
