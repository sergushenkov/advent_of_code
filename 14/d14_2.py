input_string = '''498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9
'''.strip()

with open('input.txt', 'r') as file:
    input_string = file.read().strip()

grid = [['.' for y in range(500)] for x in range(1000)]
max_depth = 0
min_width = max_width = 500
for line in input_string.split('\n'):
    points = line.split(' -> ')
    base_x, base_y = map(int, points[0].split(','))
    grid[base_x][base_y] = '#'
    for point in points:
        x, y = map(int, point.split(','))
        if x < min_width:
            min_width = x
        if x > max_width:
            max_width = x
        if y > max_depth:
            max_depth = y
        while base_x != x or base_y != y:
            if base_x == x:
                while base_y != y:
                    if base_y < y:
                        base_y += 1
                    else:
                        base_y -= 1
                    grid[base_x][base_y] = '#'
            elif base_y == y:
                while base_x != x:
                    if base_x < x:
                        base_x += 1
                    else:
                        base_x -= 1
                    grid[base_x][base_y] = '#'
            else:
                print(f'ALARM: ', base_x, base_y, x, y)

for x in range(1000):
    grid[x][max_depth + 2] = '#'

sand_count = 0
fall_flag = True
while fall_flag:
    next_x = 500
    next_y = 0
    moving_flag = True
    while moving_flag:
        if grid[next_x][next_y + 1] not in {'#', 'o'}:
            next_y += 1
        elif grid[next_x - 1][next_y + 1] not in {'#', 'o'}:
            next_y += 1
            next_x -= 1
        elif grid[next_x + 1][next_y + 1] not in {'#', 'o'}:
            next_y += 1
            next_x += 1
        else:
            moving_flag = False
            grid[next_x][next_y] = 'o'
            sand_count += 1
    if next_y == 0:
        fall_flag = False

print(sand_count)

# # рисунок
# for y in range(max_depth + 2):
#     print()
#     for x in range(min_width - 2, max_width + 4):
#         print(grid[x][y], end='')
