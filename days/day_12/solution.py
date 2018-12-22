import re
from input_reader import read

data = read(__file__)
test_data = read(__file__, name='test')


def parse(input_data):
    init = input_data[0].rstrip().split(' ')[2]
    reg_list = list()
    for line in range(2, len(input_data)):
        split_line = input_data[line].rstrip().split(' => ')
        reg_list.append([re.compile(split_line[0]), split_line[1]])
    return init, reg_list


def task_one(init: str, reg_list: list, gens:int) -> int:
    init = '.' * 2 * gens + '.' * 2 + init
    for idx in range(2, len(init)-2):
        window = init[idx-2:idx+2]
        did_match = False
        for reg in reg_list:
            if reg[0].search(window):
                init = reg[0].sub(lambda m: m.group()[:2] + reg[1] + m.group()[3:], init)
                did_match = True
                break
        if not did_match:
            init = init[:]

    return init


parsed_test = parse(test_data)
parsed_data = parse(data)
print(task_one(*parsed_test, gens=20))