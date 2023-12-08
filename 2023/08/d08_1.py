import os


def find_way(network):
    steps, string_nodes = network.split("\n\n")
    nodes = dict()
    for record in string_nodes.splitlines():
        node = record[:3]
        left_node = record[7:10]
        right_node = record[12:15]
        nodes[node] = (left_node, right_node)

    steps_cnt = 0
    current_node = "AAA"
    while current_node != "ZZZ":
        step_i = steps_cnt % len(steps)
        current_node = (
            nodes[current_node][0] if steps[step_i] == "L" else nodes[current_node][1]
        )
        steps_cnt += 1
    return steps_cnt


test_network = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)"""
steps_cnt = find_way(test_network)
assert steps_cnt == 2

test_network = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""
steps_cnt = find_way(test_network)
assert steps_cnt == 6


input_file_path = os.path.dirname(os.path.realpath(__file__)) + "//input.txt"
with open(input_file_path) as fd:
    steps_cnt = find_way(fd.read())
    print(steps_cnt)
