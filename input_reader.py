from pathlib import Path, PurePath


def read(file, name='data'):
    input_file = open(PurePath.joinpath(Path(file).parent, name+'.csv'), 'r')
    return input_file.readlines()
