def read_file():
    import os

    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(f"{dir_path}/input.txt") as fd:
        return fd.read()


def prepare_data(raw_data):
    data = []
    for token in raw_data.split("mul(")[1:]:
        closing_i = token.find(")")
        if closing_i < 3:
            continue
        truncated_token = token[:closing_i]
        comma_i = truncated_token.find(",")
        if comma_i < 1:
            continue
        x = truncated_token[:comma_i]
        y = truncated_token[comma_i + 1 :]
        if x.isdigit() and y.isdigit():
            data.append((int(x), int(y)))
    return data


def prepare_data_2(raw_data):
    data = []
    dont_i = raw_data.find("don't()")
    while dont_i > 0:
        first_part = raw_data[:dont_i]
        second_part = raw_data[dont_i + 7:]
        data.extend(prepare_data(first_part))
        do_i = second_part.find("do()")
        if do_i < 0:
            raw_data = ""
            break
        raw_data = second_part[do_i + 4:]
        dont_i = raw_data.find("don't()")
    data.extend(prepare_data(raw_data))
    return data


def calc_sum(data):
    result = 0
    for x, y in data:
        result += x * y
    return result


test_raw_data = (
    "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
)
test_data = [(2, 4), (5, 5), (11, 8), (8, 5)]
test_data_2 = [(2, 4), (8, 5)]
assert prepare_data(test_raw_data) == test_data
assert calc_sum(test_data) == 161
assert prepare_data_2(test_raw_data) == test_data_2

raw_data = read_file()
data = prepare_data(raw_data)
print(f"First answer: {calc_sum(data)}")

data_2 = prepare_data_2(raw_data)
print(f"Second answer: {calc_sum(data_2)}")
