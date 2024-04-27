import os


def find_variants(races):
    str_time, str_distance = races.splitlines()
    time = int(str_time[11:].replace(" ", ""))
    distance = int(str_distance[11:].replace(" ", ""))

    variants = 0
    for t in range(time):
        if (time - t) * t > distance:
            variants += 1
    return variants


test_races = """Time:      7  15   30
Distance:  9  40  200"""
variants = find_variants(test_races)
assert variants == 71503


input_file_path = os.path.dirname(os.path.realpath(__file__)) + "//input.txt"
with open(input_file_path) as fd:
    variants = find_variants(fd.read())
    print(variants)
