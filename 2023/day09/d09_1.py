import os


def next_value(seq):
    return 0


def answer(all_history):
    result = 0
    for line in all_history.split('\n'):
        seq = [int(x) for x in line.split(' ')]
        result += next_value(seq)
    return result


all_history = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""
result = answer(all_history)
# assert result == 68


input_file_path = os.path.dirname(os.path.realpath(__file__)) + "//input.txt"
with open(input_file_path) as fd:
    result = answer(all_history)
    print(result)
