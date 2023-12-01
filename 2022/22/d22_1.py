input_string = '''        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5
'''

with open('input.txt', 'r') as file:
    input_string = file.read()

delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
grid, way = input_string.split('\n\n')
grid = [list(line) for line in grid.split('\n')]
max_col = max((len(row) for row in grid))
for i in range(len(grid)):
    current_col = len(grid[i])
    while current_col < max_col:
        grid[i].append(' ')
        current_col += 1

row = 0
col = grid[row].index('.')
facing = 0

way = way.strip()
cursor = 0
while cursor < len(way):
    if way[cursor] == 'R':
        facing += 1
        facing %= 4
        cursor += 1
    elif way[cursor] == 'L':
        facing = 3 if facing == 0 else facing - 1
        cursor += 1
    else:
        length = ''
        while cursor < len(way) and way[cursor].isdigit():
            length += way[cursor]
            cursor += 1
        length = int(length)
        while length > 0:
            next_row = row + delta[facing][0]
            next_col = col + delta[facing][1]
            if not(0 <= next_row < len(grid)) or not(0 <= next_col < max_col) or grid[next_row][next_col] == ' ':
                find_row = row
                find_col = col
                while (0 <= find_row < len(grid)) and (0 <= find_col < max_col) and grid[find_row][find_col] != ' ':
                    find_row -= delta[facing][0]
                    find_col -= delta[facing][1]
                next_row = find_row + delta[facing][0]
                next_col = find_col + delta[facing][1]
            if grid[next_row][next_col] == '#':
                break
            elif grid[next_row][next_col] == '.':
                row = next_row
                col = next_col
                length -= 1

print(1000 * (row+1) + 4 * (col+1) + facing)
