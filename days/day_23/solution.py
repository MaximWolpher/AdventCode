from input_reader import read
import numpy as np

data = read(__file__)
test_data = read(__file__, name='test')


def parse(input_data: list) -> list:
    out_data = list()
    for line in input_data:
        clean_line = line.rstrip().replace(' r=', '')
        clean_line = clean_line.replace('pos=<', '')
        clean_line = clean_line.replace('>', '')
        out_data.append(clean_line.split(','))
    return np.array(out_data, dtype=int)


def manhattan(a, b):
    return np.sum(np.abs(a-b))


def task_one(input_data: np.array):

    pos = input_data[:, :3]
    rad = input_data[:, 3:]
    strongest = np.argmax(rad)
    ref_pos = pos[strongest]
    ref_rad = rad[strongest]
    counter = 0
    for idx, point in enumerate(input_data):
        dist = manhattan(pos[idx], ref_pos)
        if dist <= ref_rad:
            counter += 1
    return counter


parsed_test = parse(test_data)
parsed_data = parse(data)

print(task_one(parsed_data))
