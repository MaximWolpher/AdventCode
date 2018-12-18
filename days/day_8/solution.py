from input_reader import read
data = read(__file__)
test_data = read(__file__, name='test')


def parse(input_data, test=False):
    parsed = list()
    for line in input_data:
        split_line = line.rstrip().split(' ')
        if not test:
            return list(map(int, [split_line[0], split_line[-2]]))
        else:
            parsed.append(list(map(int, [split_line[0], split_line[-6], split_line[-1]])))
    return parsed


def task_one(input_data):
    circle = [0, 1]
    current_idx = 1
    L = input_data[1]
    print(L)
    for marble in range(2, L+1):
        plus_one = (current_idx + 1) % (marble + 1)
        plus_two = (current_idx + 2) % (marble + 1)
        print(plus_one, plus_two)
        circle = circle[:plus_one] + [marble] + circle[plus_two:]
        current_idx = marble
        print(circle)
        break


parsed_test = parse(test_data, True)
parsed_data = parse(data)

print(task_one(parsed_test[0][:2]))
print(test_data[2])
