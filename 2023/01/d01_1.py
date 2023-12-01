import os


def find_calibration_value(document):
    calibration_value = 0
    for line in document.splitlines():
        calibration_value += int(find_digit(line) + find_digit(line[::-1]))
    return calibration_value


def find_digit(line):
    for ch in line:
        if ch.isdigit():
            return ch


test_document = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""
assert find_calibration_value(test_document) == 142


current_dir = os.path.dirname(os.path.realpath(__file__)) + "\\"
with open(current_dir + "input.txt", "r") as fd:
    print(find_calibration_value(fd.read()))
