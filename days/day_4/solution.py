from input_reader import read
import datetime

data = read(__file__)
test_data = read(__file__, name='test')


def parse_data(input_data):
    output_list = list()
    for idx, line in enumerate(input_data):
        parsed_line = line.rstrip().replace('#', '').split(' ')
        time_date = ' '.join(parsed_line[0:2])[1:-1]
        time_stamp = datetime.datetime.fromisoformat(time_date)
        output_list.append([time_stamp.timestamp(), time_stamp.minute, parsed_line[3]])
    return output_list


def sort_list(input_data):
    sorted_list = sorted(input_data, key=lambda x: x[0])  # TODO wrong direction
    return [x[1:] for x in sorted_list]


def task_one(input_data):
    sleep = [None, None]
    sorted_data = sort_list(parse_data(input_data))
    big_dict = dict()
    dict_key = ''
    for entry in sorted_data:
        minute = entry[0]
        value = entry[1]
        if value.isdigit() and dict_key == '':
            dict_key = value
        if sleep[0] is not None and sleep[1] is not None:
            if big_dict.get(dict_key) is None:
                big_dict[dict_key] = [0]*60
            for minute_idx in range(sleep[0], sleep[1]):
                big_dict[dict_key][minute_idx] += 1
            sleep = [None, None]
            if value.isdigit():
                dict_key = value
        if value == 'asleep':
            sleep[0] = minute
        if value == 'up':
            sleep[1] = minute
    if sleep[0] is not None and sleep[1] is not None:
        if big_dict.get(dict_key) is None:
            big_dict[dict_key] = [0] * 60
        for minute_idx in range(sleep[0], sleep[1]):
            big_dict[dict_key][minute_idx] += 1
    max_guard = max(big_dict.items(), key=lambda x: sum(x[1]))[0]
    max_minute = big_dict[max_guard].index(max(big_dict[max_guard]))
    return max_guard, max_minute, int(max_guard) * int(max_minute), big_dict


def task_two(input_data):
    max_dict = dict()
    for key, value in input_data.items():
        max_dict[key] = [max(value), value.index(max(value))]
    max_guard = max(max_dict.items(), key=lambda x: x[1][0])
    return int(max_guard[0]) * max_guard[1][1]


res = task_one(data)
print(res[:3])
print(task_two(res[3]))

