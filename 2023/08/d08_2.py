import os


def prime_factors(number):
    factors = {}
    factor = 2
    while factor <= number:
        if number % factor == 0:
            number //= factor
            factors[factor] = factors.get(factor, 0) + 1
        else:
            factor += 1
    return factors


def min_mult(numbers):
    total_factors = dict()
    for number in numbers:
        factors = prime_factors(number)
        for key, value in factors.items():
            if value > total_factors.get(key, 0):
                total_factors[key] = value
    mult = 1
    for key, value in total_factors.items():
        for _ in range(value):
            mult *= key
    return mult


def find_way(network):
    steps, string_nodes = network.split("\n\n")
    nodes = dict()
    start_nodes = set()
    end_nodes = set()
    for record in string_nodes.splitlines():
        node = record[:3]
        left_node = record[7:10]
        right_node = record[12:15]
        nodes[node] = (left_node, right_node)
        if node[2] == "A":
            start_nodes.add(node)
        if node[2] == "Z":
            end_nodes.add(node)

    steps_way = []
    for node in start_nodes:
        steps_cnt = 0
        ends = dict()
        while 1 == 1:
            step_i = steps_cnt % len(steps)
            node = nodes[node][0] if steps[step_i] == "L" else nodes[node][1]
            steps_cnt += 1
            if node in end_nodes:
                if node in ends:
                    steps_way.append(steps_cnt - ends[node])
                    break
                else:
                    ends[node] = steps_cnt

    return steps_way


test_network = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""
steps_cnt = find_way(test_network)
assert min_mult(steps_cnt) == 6


input_file_path = os.path.dirname(os.path.realpath(__file__)) + "//input.txt"
with open(input_file_path) as fd:
    steps_cnt = find_way(fd.read())
    print(min_mult(steps_cnt))
