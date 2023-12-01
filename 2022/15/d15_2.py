input_string = '''Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3
'''.strip()

with open('input.txt', 'r') as file:
    input_string = file.read().strip()

input_data = []
for line in input_string.split('\n'):
    sensor, beacon = line.split(': closest beacon is at x=')
    sensor_x, sensor_y = sensor.split(', y=')
    sensor_x = int(sensor_x[12:])
    sensor_y = int(sensor_y)
    beacon_x, beacon_y = map(int, beacon.split(', y='))
    taxicab_length = abs(beacon_x - sensor_x) + abs(beacon_y - sensor_y)
    input_data.append((sensor_x, sensor_y, beacon_x, beacon_y, taxicab_length))

# max_x = 20 + 1
# max_y = 20 + 1
max_x = 4_000_000 + 1
max_y = 4_000_000 + 1
grid = [set() for x in range(max_x)]
for (sensor_x, sensor_y, beacon_x, beacon_y, taxicab_length) in input_data:
    for x in range(max(0, sensor_x - taxicab_length), min(max_x, sensor_x + taxicab_length)):
        delta_y = taxicab_length - abs(x - sensor_x)
        from_y = max(0, sensor_y - delta_y)
        to_y = min(max_y, sensor_y + delta_y)
        grid[x].add((from_y, to_y))

for x in range(max_x):
    y = 0
    flag = True
    while y < max_y and flag:
        flag = False
        for (from_y, to_y) in grid[x]:
            if from_y <= y < to_y or (y > 0 and y + 1 == from_y and y < to_y):
                y = to_y
                flag = True
                break
        if y == max_y:
            flag = True
    if not flag:
        print(x, y+1, x * 4_000_000 + y+1)
        exit()
