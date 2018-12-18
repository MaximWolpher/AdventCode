from input_reader import read

data = read(__file__)


def task_one(input_data):
    return sum([int(x) for x in input_data])


def task_two(input_data):
    current_freq = 0
    seen_set = set()
    while True:
        for row in input_data:
            current_freq += int(row)
            if current_freq not in seen_set:
                seen_set.add(current_freq)
            else:
                return current_freq


print('Task one: ', task_one(data))
print('Task two: ', task_two(data))
