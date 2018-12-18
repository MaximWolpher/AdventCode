from input_reader import read
data = read(__file__)
test_data = read(__file__, name='test')


def parse_dep(input_data):
    parsed = dict()
    for line in input_data:
        split_line = line.rstrip().split(' ')
        if parsed.get(split_line[1]) is None:
            parsed[split_line[1]] = list()
        parsed[split_line[1]].append(split_line[-3])
        parsed[split_line[1]] = sorted(parsed[split_line[1]])
    return parsed


def dependencies(input_data):
    parsed = dict()
    for line in input_data:
        split_line = line.rstrip().split(' ')
        if parsed.get(split_line[-3]) is None:
            parsed[split_line[-3]] = list()
        parsed[split_line[-3]].append(split_line[1])
    return parsed


def find_all(dependencies):
    big_set = set()
    for key, value in dependencies.items():
        big_set.add(key)
        for dep in value:
            big_set.add(dep)
    return sorted(list(big_set))


def replace_dep(dependencies, all_list):
    repl_list = all_list[:]
    for key, value in dependencies.items():
        idx = repl_list.index(key)
        repl_list[idx] = value
    return repl_list


def find_missing(input_data, all_list):
    small_set = set()
    for x in input_data:
        if isinstance(x, list):
            for y in x:
                small_set.add(y)
        elif isinstance(x, str):
            small_set.add(x)
    return sorted(list(set(all_list) - small_set))


def remove_deps(deps, letter):
    for key, value in deps.items():
        if letter in value:
            value.remove(letter)


def task_one(input_data):
    parsed = parse_dep(input_data)
    deps = dependencies(input_data)
    all_list = find_all(parsed)
    repl = replace_dep(parsed, all_list)
    next_layer = find_missing(repl, all_list)
    path = list()
    while len(path) < len(all_list):
        if not deps.get(next_layer[0]) or not deps[next_layer[0]]:
            path = path + [next_layer.pop(0)]
            remove_deps(deps, path[-1])
        else:
            next_layer = next_layer[1:]+next_layer[0:1]
            continue
        idx = all_list.index(path[-1])
        inner = repl[idx]
        if isinstance(inner, list):
            next_layer = sorted(list(set(inner + next_layer)))
        elif isinstance(inner, str):
            next_layer = sorted(list(set([inner] + next_layer)))
    return ''.join(path)


def deligate(deps, path, next_layer, workers):
    alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    min_time = min(next_layer)
    min_worker = 0
    for idx, worker in enumerate(workers):
        if next_layer:
            task = next_layer.pop(0)
            work_time = alphabet.index(task)+1
            if work_time == min_time:
                min_worker = idx
            workers[idx] += work_time
            path = path + [task]
            remove_deps(deps, path[-1])
        else:
            workers[idx] = max(workers[min_worker], workers[idx])


def task_two(input_data, n):
    workers = [0] * n
    parsed = parse_dep(input_data)
    deps = dependencies(input_data)
    all_list = find_all(parsed)
    repl = replace_dep(parsed, all_list)
    next_layer = find_missing(repl, all_list)
    path = list()
    while len(path) < len(all_list):
        if not deps.get(next_layer[0]) or not deps[next_layer[0]]:
            deligate(deps, path, next_layer, workers)
        else:
            next_layer = next_layer[1:]+next_layer[0:1]
            continue
        idx = all_list.index(path[-1])
        inner = repl[idx]
        if isinstance(inner, list):
            next_layer = sorted(list(set(inner + next_layer)))
        elif isinstance(inner, str):
            next_layer = sorted(list(set([inner] + next_layer)))
    return ''.join(path)


#print('Task one: ', task_one(test_data))
print('Task two: ', task_two(test_data, 2))
