import os


class Map:
    def __init__(self, almanac_part):
        almanac_part = almanac_part.splitlines()
        self._name = almanac_part[0][:-1]
        self._map = []
        for record in almanac_part[1:]:
            dst_start, src_start, range_length = map(int, record.split(" "))
            self._map.append([dst_start, src_start, range_length])

    def mapping(self, source):
        dst = []
        while source:
            (src_start, src_range_length) = source.pop()
            is_not_in_map = True
            for dst_start, map_start, map_range_length in self._map:
                if (
                    src_start >= (map_start + map_range_length)
                    or (src_start + src_range_length - 1) < map_start
                ):
                    continue  # этот маппинг не применим к этому входному диапазону

                if map_start <= src_start < (
                    map_start + map_range_length
                ) and map_start <= (src_start + src_range_length) <= (
                    map_start + map_range_length
                ):
                    dst.append((dst_start + (src_start - map_start), src_range_length))
                    is_not_in_map = False
                    break  # входной диапазон целиком внутри маппинга

                if map_start > src_start and map_start <= (
                    src_start + src_range_length
                ) <= (map_start + map_range_length):
                    dst.append((dst_start, src_start + src_range_length - map_start))
                    source.append((src_start, map_start - src_start))
                    is_not_in_map = False
                    break  # входной диапазон начинается ДО маппинга

                if map_start <= src_start < (map_start + map_range_length) and (
                    src_start + src_range_length
                ) > (map_start + map_range_length):
                    dst.append(
                        (
                            dst_start + (src_start - map_start),
                            (map_start + map_range_length - src_start),
                        )
                    )
                    source.append(
                        (
                            (map_start + map_range_length),
                            (
                                src_start
                                + src_range_length
                                - (map_start + map_range_length)
                            ),
                        )
                    )
                    is_not_in_map = False
                    break  # входной диапазон заканчивается после маппинга

                if map_start > src_start and (src_start + src_range_length) > (
                    map_start + map_range_length
                ):
                    dst.append((dst_start, map_range_length))
                    source.append((src_start, map_start - src_start))
                    source.append(
                        (
                            (map_start + map_range_length),
                            (
                                src_start
                                + src_range_length
                                - (map_start + map_range_length)
                            ),
                        )
                    )
                    is_not_in_map = False
                    break  # маппинг перекрывает середину входного диапазона

            if is_not_in_map:  # для входного диапазона не нашёлся подходящий маппинг
                dst.append((src_start, src_range_length))
        return dst


def create_maps(almanac):
    almanac_parts = almanac.split("\n\n")

    seeds_v = list(map(int, almanac_parts[0][7:].split(" ")))
    seeds = []
    for i in range(len(seeds_v) // 2):
        seeds.append((seeds_v[2 * i], seeds_v[2 * i + 1]))

    src = seeds
    for almanac_part in almanac_parts[1:]:
        current_map = Map(almanac_part)
        src = current_map.mapping(src)
    return src


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
humidity_to_location = create_maps(test_almanac)
humidity_to_location.sort(key=lambda x: x[0])
assert humidity_to_location[0][0] == 46

input_file_path = os.path.dirname(os.path.realpath(__file__)) + "//input.txt"
with open(input_file_path) as fd:
    almanac = fd.read()
    humidity_to_location = create_maps(almanac)
    humidity_to_location.sort(key=lambda x: x[0])
    print(humidity_to_location[0][0])
