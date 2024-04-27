import os


def find_details(text_schema):
    schema = text_schema.split('\n')
    parts = []
    for j, row in enumerate(schema):
        i = 0
        while i < len(row):
            if not row[i].isdigit():
                i += 1
                continue
            first_ch = i
            while i < len(row) and row[i].isdigit():
                i += 1
            last_ch = i
            is_part = False

            start_row = max(j-1, 0)
            end_row = j + 1
            start_ch = max(first_ch - 1, 0)
            end_ch = last_ch + 1
            for check_row in schema[start_row:end_row + 1]:
                for ch in check_row[start_ch:end_ch]:
                    if not ch.isdigit() and ch != ".":
                        is_part = True
                        break
                if is_part:
                    break
            if is_part:
                parts.append(int(row[first_ch:last_ch]))
    return parts


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
parts = find_details(test_schema)
print(parts)
assert sum(parts) == 4361
assert 114 not in parts
assert 58 not in parts

input_file_path = os.path.dirname(os.path.realpath(__file__)) + "//input.txt"
with open(input_file_path) as fd:
    parts = find_details(fd.read())
    print(sum(parts))
