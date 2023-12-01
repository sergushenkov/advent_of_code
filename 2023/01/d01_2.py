import os

digits = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

inverse_digits = {
    "eno": 1,
    "owt": 2,
    "eerht": 3,
    "ruof": 4,
    "evif": 5,
    "xis": 6,
    "neves": 7,
    "thgie": 8,
    "enin": 9,
}


def find_calibration_value(document):
    calibration_value = 0
    for line in document.splitlines():
        calibration_value += find_digit(line) * 10 + find_digit(line[::-1], inverse_digits)
    return calibration_value


def find_digit(line, digits=digits):
    for i, ch in enumerate(line):
        if ch.isdigit():
            return int(ch)
        if line[i:i+3] in digits: 
            return digits[line[i:i+3]]
        if line[i:i+4] in digits: 
            return digits[line[i:i+4]]
        if line[i:i+5] in digits: 
            return digits[line[i:i+5]]

test_document = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""
assert find_calibration_value(test_document) == 281


current_dir = os.path.dirname(os.path.realpath(__file__)) + "\\"
with open(current_dir + "input.txt", "r") as fd:
    print(find_calibration_value(fd.read()))
