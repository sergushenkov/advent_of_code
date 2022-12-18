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

# visited = set()
# current_point = 'start'
# current_flow = 0
# all_flow = 0
# timer = 30
# time = 0
# while len(visited) < len(grid) and timer - time > 0:
#     visited.add(current_point)
#     all_flow += time * current_flow
#     current_flow += grid[current_point][0]
#     timer -= time
#     print(timer, current_point, current_flow, all_flow)
#     max_rent = 0
#     next_point = ''
#     flow, points = grid[current_point]
#     for point, way in points.items():
#         if point in visited:
#             continue
#         current_rent = grid[point][0] * (timer - way)
#         if current_rent > max_rent:
#             max_rent = current_rent
#             next_point = point
#             next_way = way
#     current_point = next_point
#     time = next_way + 1

# all_flow += timer * current_flow
# print(all_flow)

def visit_point(point, cost, timer, current_flow, sum_flow, visited, level):
    visited.add(point)
    sum_flow += cost * current_flow
    timer -= cost
    current_flow += grid[point][0]
    all_flows = []
    last_point = True
    level += 1
    for next_point, next_cost in grid[point][1].items():
        # print(grid[point][1], next_point, next_cost)
        if level > 4:
            break
        if next_point not in visited:
            last_point = False
            next_cost += 1
            all_flows.append(visit_point(next_point, next_cost, timer, current_flow, sum_flow, visited.copy(), level))
    if last_point or level > 4:
        sum_flow += timer * current_flow
        return (sum_flow, [point])
    a,b = sorted(all_flows, reverse=True, key=lambda x: x[0])[0]
    b.append(point)
    return (a,b)

visited = set()
current_point = 'start'
current_flow = 0
sum_flow = 0
timer = 30
next_cost = 0
while len(visited) < len(grid) and timer - next_cost > 0:
    visited.add(current_point)
    _, next_point = visit_point(current_point, next_cost, timer, current_flow, sum_flow, visited, 0)
    sum_flow += next_cost * current_flow
    current_flow += grid[current_point][0]
    timer -= next_cost
    print(timer, current_point, current_flow, sum_flow)
    # print(grid[current_point])
    key = next_point[-2] if len(next_point) > 1 else next_point[0]
    # print(grid[current_point][1], key)
    if current_point == key:
        break
    next_cost = grid[current_point][1][key] + 1
    current_point = key

sum_flow += timer * current_flow
print(sum_flow)