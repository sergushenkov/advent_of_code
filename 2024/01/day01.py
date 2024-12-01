def read_file():
    import os

    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(f"{dir_path}/input.txt") as fd:
        return fd.read()


def prepare_date(raw_data):
    first, second = [], []
    for row in raw_data.split("\n"):
        x, y = row.split()
        first.append(int(x))
        second.append(int(y))
    first.sort()
    second.sort()
    return first, second


def prepare_date_2(raw_data):
    first, second = dict(), dict()
    for row in raw_data.split("\n"):
        x, y = row.split()
        first[x] = first.get(x, 0) + 1
        second[y] = second.get(y, 0) + 1
    return first, second


def calc_total_distance(first, second):
    total = 0
    for x, y in zip(first, second):
        total += abs(x - y)
    return total


def calc_similarity_score(first, second):
    total_score = 0
    for x in first:
        total_score += int(x) * second.get(x, 0) * first[x]
    return total_score


test_data = """3   4
4   3
2   5
1   3
3   9
3   3"""
assert len(read_file().split("\n")) == 1000
assert prepare_date(test_data) == ([1, 2, 3, 3, 3, 4], [3, 3, 3, 4, 5, 9])
assert calc_total_distance([1, 2, 3, 3, 3, 4], [3, 3, 3, 4, 5, 9]) == 11
assert prepare_date_2(test_data) == (
    {"3": 3, "4": 1, "2": 1, "1": 1},
    {"4": 1, "3": 3, "5": 1, "9": 1},
)
assert (
    calc_similarity_score(
        {"3": 3, "4": 1, "2": 1, "1": 1}, {"4": 1, "3": 3, "5": 1, "9": 1}
    )
    == 31
)


raw_data = read_file()
first, second = prepare_date(raw_data)
print(f"First answer: {calc_total_distance(first, second)}")

first, second = prepare_date_2(raw_data)
print(f"Second answer: {calc_similarity_score(first, second)}")
