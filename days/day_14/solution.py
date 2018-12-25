from input_reader import read

data = read(__file__)
test_data = read(__file__, name='test')


def parse(input_data: list):
    return int(input_data[0])


def next_states(state: int) -> list:
    return [int(d) for d in str(state)]


def task_one(input_data: int) -> str:
    states = [3, 7]
    idx = 0
    idy = 1
    while len(states) <= input_data + 10:
        next_sum = states[idx] + states[idy]
        states += next_states(next_sum)
        idx = (idx + 1 + states[idx]) % len(states)
        idy = (idy + 1 + states[idy]) % len(states)
    return ''.join([str(d) for d in states[input_data: input_data + 10]])


def task_two(input_data: str) -> int:
    states = [3, 7]
    idx = 0
    idy = 1
    while True:
        next_sum = states[idx] + states[idy]
        next_state_list = next_states(next_sum)
        states += next_state_list
        idx = (idx + 1 + states[idx]) % len(states)
        idy = (idy + 1 + states[idy]) % len(states)
        for x in range(len(next_state_list)+1):
            if x == 0:
                if ''.join([str(d) for d in states[-len(input_data): 0]]) == input_data:
                    return len(states) - len(input_data)
            else:
                if ''.join([str(d) for d in states[-(len(input_data) + x): -x]]) == input_data:
                    return len(states) - len(input_data) - x


parsed_data = parse(data)
print('Task one: ', task_one(parsed_data))
print('Task two: ', task_two(str(702831)))
