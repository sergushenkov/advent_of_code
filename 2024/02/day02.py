def read_file():
    import os

    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(f"{dir_path}/input.txt") as fd:
        return fd.read()


def prepare_data(raw_data):
    all_reports = []
    for row in raw_data.split("\n"):
        report = [int(x) for x in row.split(" ")]
        if report[0] > report[-1]:
            report = report[::-1]
        all_reports.append(report)
        assert len(report) > 4
    return all_reports


def check_report(report, tolerate=0):
    prev = None
    for x in report:
        if prev is None:
            prev = x
            continue
        delta = x - prev
        if delta in [1, 2, 3]:
            prev = x
            continue
        tolerate -= 1
        if tolerate < 0:
            return False
    return True


def calc_answer(all_reports, tolerate=0):
    answer = sum(check_report(report, tolerate) for report in all_reports)
    return answer


test_data = """1 2 7 8 9"""
assert prepare_data(test_data) == [[1, 2, 7, 8, 9]]
assert check_report([1, 3, 6, 7, 9])
assert not check_report([1, 5, 6, 7, 9])
assert not check_report([1, 3, 3, 7, 9])
assert not check_report([1, 3, 6, 5, 9])
assert check_report([1, 3, 6, 7, 9], 1)
assert not check_report([1, 3, 3, 7, 9], 1)
assert check_report([1, 3, 6, 5, 8], 1)
assert not check_report([1, 7, 6, 5, 8], 1)
assert check_report([1, 5, 4, 5, 8], 1)
assert not check_report([1, 4, 3, 4, 7], 1)
test_data = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""
all_reports = prepare_data(test_data)
assert calc_answer(all_reports) == 2
assert calc_answer(all_reports, 1) == 4

raw_data = read_file()
all_reports = prepare_data(raw_data)
print(f"First answer: {calc_answer(all_reports)}")
print(f"Second answer: {calc_answer(all_reports, 1)}")  # 418
