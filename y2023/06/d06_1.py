import os


def find_variants(races):
    str_time, str_distance = races.splitlines()
    time = []
    for x in str_time[11:].split(" "):
        if x.isdigit():
            time.append(int(x))
    distance = []
    for x in str_distance[11:].split(" "):
        if x.isdigit():
            distance.append(int(x))
    races = list(zip(time, distance))

    variants = []
    for time, distance in races:
        variants_count = 0
        for t in range(time):
            if (time - t) * t > distance:
                variants_count += 1
        variants.append(variants_count)
    return variants


test_races = """Time:      7  15   30
Distance:  9  40  200"""
variants = find_variants(test_races)
result = 1
for num in variants:
    result = result * num
assert result == 288


input_file_path = os.path.dirname(os.path.realpath(__file__)) + "//input.txt"
with open(input_file_path) as fd:
    variants = find_variants(fd.read())
    result = 1
    for num in variants:
        result *= num
    print(result)
