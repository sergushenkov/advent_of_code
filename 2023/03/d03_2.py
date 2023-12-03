import os


def find_numbers(row):
    start_end_numbers = []
    i = 0
    while i < len(row):
        if not row[i].isdigit():
            i += 1
            continue
        start_number = i
        while i < len(row) and row[i].isdigit():
            i += 1
        start_end_numbers.append((start_number, i))
    return start_end_numbers


def check_gears(schema, j, first_ch, last_ch):
    start_row = max(j - 1, 0)
    end_row = j + 1
    start_ch = max(first_ch - 1, 0)
    end_ch = last_ch + 1
    for delta_row, check_row in enumerate(schema[start_row : end_row + 1]):
        for delta_ch, ch in enumerate(check_row[start_ch:end_ch]):
            if ch == "*":
                return (start_row + delta_row, start_ch + delta_ch)


def count_gear_ratio(text_schema):
    schema = text_schema.split("\n")
    gears = dict()
    for j, row in enumerate(schema):
        for first_ch, last_ch in find_numbers(row):
            xy = check_gears(schema, j, first_ch, last_ch)
            if xy in gears:
                gears[xy].append(int(row[first_ch:last_ch]))
            else:
                gears[xy] = [int(row[first_ch:last_ch])]
    return sum(
        map(lambda x: x[0] * x[1], filter(lambda x: len(x) == 2, gears.values()))
    )


test_schema = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""
assert count_gear_ratio(test_schema) == 467835


input_file_path = os.path.dirname(os.path.realpath(__file__)) + "//input.txt"
with open(input_file_path) as fd:
    print(count_gear_ratio(fd.read()))
