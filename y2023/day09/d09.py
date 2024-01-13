import os


def next_value(seq):
    new_seq = []
    for i in range(1, len(seq)):
        new_seq.append(seq[i] - seq[i-1])
    if new_seq == (len(seq) - 1) * [0]:
        return seq[-1]
    return seq[-1] + next_value(new_seq)


def prev_value(seq):
    new_seq = []
    for i in range(1, len(seq)):
        new_seq.append(seq[i] - seq[i-1])
    if new_seq == (len(seq) - 1) * [0]:
        return seq[0]
    return seq[0] - prev_value(new_seq)


def answer(all_history):
    result_1 = 0
    result_2 = 0
    for line in all_history.split('\n'):
        seq = [int(x) for x in line.split(' ')]
        result_1 += next_value(seq)
        result_2 += prev_value(seq)
    return result_1, result_2


all_history = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""
result_1, result_2 = answer(all_history)
assert result_1 == 114
assert result_2 == 2

input_file_path = os.path.dirname(os.path.realpath(__file__)) + "//input.txt"
with open(input_file_path) as fd:
    all_history = fd.read()
    result_1, result_2 = answer(all_history)
    print(result_1, result_2)
