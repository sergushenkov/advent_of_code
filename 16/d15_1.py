input_string = '''Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II
'''

with open('input.txt', 'r') as file:
    input_string = file.read()

grid = dict()
zero_points = []
for line in input_string.strip().split('\n'):
    point = line[6:8]
    head, tail = line.replace('tunnel leads to valve', 'tunnels lead to valves').split('; tunnels lead to valves ')
    flow_rate = int(head[23:])
    if flow_rate <= 0:
        zero_points.append(point)
    ways = {way: 1 for way in tail.split(', ')}
    grid[point] = [flow_rate, ways]

print(grid, '\n')
while zero_points:
    zp = zero_points.pop()
    if zp == 'AA':
        print('add start')
        grid['start'] = grid[zp].copy()
        print(grid, '\n')
    _, ways = grid[zp]
    for change_point, add_distance in ways.items():
        _, change_ways = grid[change_point]
        # add_distance = change_ways[zp]
        del change_ways[zp]
        for new_point, distance in ways.items():
            if new_point == change_point:
                continue
            change_ways[new_point] = distance + add_distance
    del grid[zp]
print(grid)

while min(len(grid[point][1]) for point in grid) < len(grid) - 2:
    all_points = [point for point in grid]
    while all_points:
        zp = all_points.pop()
        _, ways = grid[zp]
        ways_in_work = ways.copy()
        for point, add_distance in ways_in_work.items():
            _, add_ways = grid[point]
            # add_distance = change_ways[zp]
            for new_point, distance in add_ways.items():
                if new_point == zp or ways.get(new_point, 1000000) < distance + add_distance:
                    continue
                ways[new_point] = distance + add_distance
    print(f'добавил пути: {grid}')

def visit_point(point, cost, timer, current_flow, sum_flow, visited):
    visited.add(point)
    print(f'level {len(visited)}')
    sum_flow += cost * current_flow
    timer -= cost
    current_flow += grid[point][0]
    all_flows = []
    last_point = True
    for next_point, next_cost in grid[point][1].items():
        # print(grid[point][1], next_point, next_cost)
        if next_point not in visited:
            last_point = False
            next_cost += 1
            all_flows.append(visit_point(next_point, next_cost, timer, current_flow, sum_flow, visited.copy()))
    if last_point:
        sum_flow += timer * current_flow
        return sum_flow
    return max(all_flows)

print(visit_point('start', 0, 30, 0, 0, set()))