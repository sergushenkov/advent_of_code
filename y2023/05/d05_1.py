import os


def create_maps(almanac):
    almanac_parts = almanac.split("\n\n")

    seeds = list(map(int, almanac_parts[0][7:].split(" ")))

    seed2soil = dict()
    soil2fertilizer = dict()
    fertilizer2water = dict()
    water2light = dict()
    light2temperature = dict()
    temperature2humidity = dict()
    humidity2location = dict()
    maps = [
        seed2soil,
        soil2fertilizer,
        fertilizer2water,
        water2light,
        light2temperature,
        temperature2humidity,
        humidity2location,
    ]

    src = seeds
    for i, almanac_part in enumerate(almanac_parts[1:]):
        for record in almanac_part.splitlines()[1:]:
            dst_start, src_start, range_length = map(int, record.split(" "))
            for x in src:
                if src_start <= x < src_start + range_length:
                    maps[i][x] = dst_start + (x - src_start)

        for x in src:
            if x not in maps[i]:
                maps[i][x] = x
        src = maps[i].values()

    return maps


test_almanac = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""
maps = create_maps(test_almanac)
humidity_to_location = maps[6]
assert min(humidity_to_location.values()) == 35


input_file_path = os.path.dirname(os.path.realpath(__file__)) + "//input.txt"
with open(input_file_path) as fd:
    maps = create_maps(fd.read())
    print(min(maps[6].values()))
