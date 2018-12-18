from input_reader import read
import re

data = read(__file__)
test_data = read(__file__, name='test')

alphabet_list = list('abcdefghijklmnopqrstuvwxyz')


def task_one(input_data, alphabet):
    unchanged = input_data
    while True:
        for letter in alphabet:
            reg_str = letter+letter.upper()
            reg_str_opp = letter.upper()+letter
            input_data = re.sub(reg_str, '', input_data)
            input_data = re.sub(reg_str_opp, '', input_data)
        if input_data == unchanged:
            break
        else:
            unchanged = input_data
    return len(input_data)


def task_two(input_data, alphabet):
    best_so_far = 2**1000
    for letter in alphabet:
        reg = re.compile(f'[{letter}]', re.I)
        short_data = reg.sub('', input_data)
        cur_len = task_one(short_data, alphabet)
        if cur_len < best_so_far:
            best_so_far = cur_len
    return best_so_far


res_one = task_one(data[0], alphabet_list)
print('Task One: ', res_one)
res_two = task_two(data[0], alphabet_list)
print('Task Two: ', res_two)
