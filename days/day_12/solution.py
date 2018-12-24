import re
from input_reader import read

data = read(__file__)
test_data = read(__file__, name='test')


def parse(input_data):
    init = input_data[0].rstrip().split(' ')[2]
    reg_list = list()
    for line in range(2, len(input_data)):
        split_line = input_data[line].rstrip().split(' => ')
        reg_list.append([re.compile(re.escape(split_line[0])), split_line[1]])
    return init, reg_list


def task_one(init: str, reg_list: list, gens: int) -> list:
    init = list('.' * 2 * gens + '.' * 2 + init + '.' * 2 + '.' * 2 * gens)
    start_loc = 2 * gens + 2
    all_scores = list()
    for geneation in range(gens):
        temp_list = ['.'] * len(init)
        for idx in range(2, len(init) - 2):
            window = ''.join(init[idx-2:idx+3])
            for reg in reg_list:
                wat = reg[0].match(window)
                if wat:
                    temp_list[idx] = reg[1]
                    break
        init = temp_list[:]
        score = 0
        for idx, value in enumerate(init):
            if value == '#':
                score += (idx - start_loc)
        all_scores.append(score)
    return all_scores


def task_two(input_data: list, gens: int) -> int:
    diff = input_data[-1] - input_data[-2]
    return input_data[-1] + diff * (gens - len(input_data))


parsed_test = parse(test_data)
parsed_data = parse(data)
scores = task_one(*parsed_data, gens=200)
print('Task one: ', scores[20-1])
print('Task two: ', task_two(scores, gens=50000000000))
