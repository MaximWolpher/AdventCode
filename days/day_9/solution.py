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
    players = [0]*input_data[0]
    player_count = 0
    for marble in range(2, L + 1):
        player_count = (player_count + 1) % input_data[0]
        if marble % 23 == 0:
            players[player_count] += marble
            drop_marble_index = (current_idx-7) % len(circle)
            players[player_count] += circle[drop_marble_index]
            del circle[drop_marble_index]
            current_idx = drop_marble_index % len(circle)
        else:
            plus_one = (current_idx + 1) % marble
            plus_two = (current_idx + 2) % marble
            if plus_two == 0:
                plus_two = marble
            circle = circle[:plus_one+1] + [marble] + circle[plus_two:]
            current_idx = circle.index(marble)
    return max(players)


parsed_test = parse(test_data, True)
parsed_data = parse(data)

print(task_one(parsed_data))
