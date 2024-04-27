import os


def read_data(file_name):
    dir_name = os.path.dirname(os.path.abspath(__file__))
    with open(dir_name + "\\" + file_name, "r") as f:
        raw_data = f.read()
        bags = [bag.strip() for bag in raw_data.split("\n")]
        return bags


def create_things():
    alfabet = "abcdefghijklmnopqrstuvwxyz"
    alfabet += alfabet.upper()
    things = dict(zip(alfabet, range(1, 53)))
    return things


def find_common(bag):
    part1 = set(i for i in bag[: len(bag) // 2])
    part2 = set(i for i in bag[len(bag) // 2 :])
    common = part1 & part2
    return common


def count_score(bags):
    things = create_things()
    result = 0
    for bag in bags:
        common = find_common(bag)
        for thing in common:
            result += things[thing]
    return result


if __name__ == "__main__":
    file_name = "input.txt"
    bags = read_data(file_name)
    result = count_score(bags)
    print(result)
