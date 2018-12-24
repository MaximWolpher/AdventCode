from input_reader import read

data = read(__file__)
test_data = read(__file__, name='test')


def parse(input_data):
    return int(input_data[0])


def next_states(state: int) -> list:
    return [int(d) for d in str(state)]


def task_one(input_data) -> str:
    states = [3, 7]
    idx = 0
    idy = 1
    while len(states) <= input_data + 10:
        next_sum = states[idx] + states[idy]
        states += next_states(next_sum)
        idx = (idx + 1 + states[idx]) % len(states)
        idy = (idy + 1 + states[idy]) % len(states)
    return ''.join([str(d) for d in states[input_data: input_data + 10]])


parsed_data = parse(data)
print('Task one: ', task_one(parsed_data))
