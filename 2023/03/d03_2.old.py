import os


def find_details(text_schema):
    schema = text_schema.split('\n')
    gears = dict()
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
            is_gear = False

            start_row = max(j-1, 0)
            end_row = j + 1
            start_ch = max(first_ch - 1, 0)
            end_ch = last_ch + 1
            for delta_row, check_row in enumerate(schema[start_row:end_row + 1]):
                for delta_ch, ch in enumerate(check_row[start_ch:end_ch]):
                    if ch == "*":
                        is_gear = True
                        xy = (start_row+delta_row, start_ch+delta_ch)
                        if xy in gears:                        
                            gears[xy].append(int(row[first_ch:last_ch]))
                        else:
                            gears[xy] = [int(row[first_ch:last_ch])]
                        break
                if is_gear:
                    break
    result = 0
    for nums in gears.values():
        if len(nums) == 2:
            result += nums[0] * nums[1]
    return gears, result


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
gears, result = find_details(test_schema)
print(gears)
assert result == 467835


input_file_path = os.path.dirname(os.path.realpath(__file__)) + "//input.txt"
with open(input_file_path) as fd:
    gears, result = find_details(fd.read())
    print(result)
