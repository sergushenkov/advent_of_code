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
    if input_data == []:
        min_x = min(sensor_x - taxicab_length, beacon_x)
        max_x = max(sensor_x + taxicab_length, beacon_x)
        min_y = min(sensor_y - taxicab_length, beacon_y)
        max_y = max(sensor_y + taxicab_length, beacon_y)
    else:
        min_x = min(sensor_x - taxicab_length, beacon_x, min_x)
        max_x = max(sensor_x + taxicab_length, beacon_x, max_x)
        min_y = min(sensor_y - taxicab_length, beacon_y, min_y)
        max_y = max(sensor_y + taxicab_length, beacon_y, max_x)
    input_data.append((sensor_x, sensor_y, beacon_x, beacon_y, taxicab_length))

coal_y = 2000000
min_x -= 2
max_x += 2
grid = ['.' for y in range(max_x - min_x)]
for (sensor_x, sensor_y, beacon_x, beacon_y, taxicab_length) in input_data:
    if sensor_y == coal_y:
        grid[sensor_x - min_x] = 'S'
    if beacon_y == coal_y:
        grid[beacon_x - min_x] = 'B'
    for x in range(sensor_x - taxicab_length, sensor_x + taxicab_length):
        if grid[x - min_x] in {'S', 'B', '#'}:
            continue
        if abs(x - sensor_x) + abs(coal_y - sensor_y) <= taxicab_length:
            grid[x - min_x] = '#'

result = 0
for x in range(len(grid)):
    if grid[x] == '#':
        result += 1
print(result)
