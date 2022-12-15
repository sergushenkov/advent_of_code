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

max_x = 4_000_000 + 1
max_y = 4_000_000 + 1
grid = [['.' for y in range(max_y)] for x in range(max_x)]
for (sensor_x, sensor_y, beacon_x, beacon_y, taxicab_length) in input_data:
    if 0 < sensor_x < max_x and 0 < sensor_y < max_y:
        grid[sensor_x][sensor_y] = 'S'
    if 0 < beacon_x < max_x and 0 < beacon_y < max_y:
        grid[beacon_x][beacon_y] = 'B'
    for x in range(max(0, sensor_x - taxicab_length), min(max_x, sensor_x + taxicab_length)):
        for y in range(max(0, sensor_y - taxicab_length), min(max_y, sensor_y + taxicab_length)):
            if grid[x][y] in {'S', 'B', '#'}:
                continue
            if abs(x - sensor_x) + abs(y - sensor_y) <= taxicab_length:
                grid[x][y] = '#'

for x in range(max_x):
    for y in range(max_y):
        if grid[x][y] == '.':
            print(x * 4_000_000 + y)
