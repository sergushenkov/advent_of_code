import os


def create_maps(almanac):
    almanac_parts = almanac.split("\n\n")

    seeds_v = list(map(int, almanac_parts[0][7:].split(" ")))
    seeds = []
    for i in range(len(seeds_v) // 2):
        seeds.append((0, seeds_v[2 * i], seeds_v[2 * i + 1]))

    seed2soil = []
    soil2fertilizer = []
    fertilizer2water = []
    water2light = []
    light2temperature = []
    temperature2humidity = []
    humidity2location = []
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
        current_map = []
        for record in almanac_part.splitlines()[1:]:
            dst_start, src_start, range_length = map(int, record.split(" "))
            current_map.append([src_start, range_length, dst_start])
        while src:
            (_, src_start, src_range_length) = src.pop()
            is_not_in_map = True
            for map_start, map_range_length, dst_start in current_map:
                if (
                    src_start >= (map_start + map_range_length)
                    or (src_start + src_range_length - 1) < map_start
                ):
                    continue
                if map_start <= src_start < (
                    map_start + map_range_length
                ) and map_start <= (src_start + src_range_length) <= (
                    map_start + map_range_length
                ):
                    maps[i].append(
                        (
                            src_start,
                            dst_start + (src_start - map_start),
                            src_range_length,
                        )
                    )
                    is_not_in_map = False
                    break
                if map_start > src_start and map_start <= (
                    src_start + src_range_length
                ) <= (map_start + map_range_length):
                    maps[i].append(
                        (map_start, dst_start, src_start + src_range_length - map_start)
                    )
                    src.append((0, src_start, map_start - src_start))
                    is_not_in_map = False
                    break
                if map_start <= src_start < (map_start + map_range_length) and (
                    src_start + src_range_length
                ) > (map_start + map_range_length):
                    maps[i].append(
                        (
                            src_start,
                            dst_start + (src_start - map_start),
                            (map_start + map_range_length - src_start),
                        )
                    )
                    src.append(
                        (
                            0,
                            (map_start + map_range_length),
                            (
                                src_start
                                + src_range_length
                                - (map_start + map_range_length)
                            ),
                        )
                    )
                    is_not_in_map = False
                    break
                if map_start > src_start and (src_start + src_range_length) > (
                    map_start + map_range_length
                ):
                    maps[i].append((map_start, dst_start, map_range_length))
                    src.append((0, src_start, map_start - src_start))
                    src.append(
                        (
                            0,
                            (map_start + map_range_length),
                            (
                                src_start
                                + src_range_length
                                - (map_start + map_range_length)
                            ),
                        )
                    )
                    is_not_in_map = False
                    break
            if is_not_in_map:
                maps[i].append((src_start, src_start, src_range_length))
        src = maps[i].copy()
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
humidity_to_location.sort(key=lambda x: x[1])
assert humidity_to_location[0][1] == 46

input_file_path = os.path.dirname(os.path.realpath(__file__)) + "//input.txt"
with open(input_file_path) as fd:
    maps = create_maps(fd.read())
    humidity_to_location = maps[6]
    humidity_to_location.sort(key=lambda x: x[1])
    print(humidity_to_location[0][1])
