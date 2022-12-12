input_string = '''Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
'''.strip()

with open('input.txt') as file:
    input_string = file.read().strip()

grid = []  # node = [status(-1,0,1), high, cost]
for line in input_string.split('\n'):
    row = []
    for node in line:
        if node == 'S' or node == 'a':
            row.append(['0', ord('a'), 0])
        elif node == 'E':
            row.append(['E', ord('z'), len(input_string)])
        else:
            row.append(['-1', ord(node), len(input_string)])
    grid.append(row)

not_finish = True
while not_finish:
    not_finish = False
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j][0] != '0':
                continue
            _, high, cost = grid[i][j]
            for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                x = i + dx
                y = j + dy
                if len(grid) > x >= 0 and len(grid[0]) > y >= 0:
                    if high + 1 >= grid[x][y][1] and cost + 1 < grid[x][y][2]:
                        grid[x][y][2] = cost + 1
                        not_finish = True
                        if grid[x][y][0] == 'E':
                            result = grid[x][y][2]
                        else:
                            grid[x][y][0] = '0'
            grid[i][j][0] = '1'
print(result)
