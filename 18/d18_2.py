input_string = '''2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5
'''

with open('input.txt', 'r') as file:
    input_string = file.read()

n = 25
all_blocks = set()
grid = [[[-1 for z in range(0, n)] for y in range(0, n)]
        for x in range(0, n)]
for line in input_string.strip().split('\n'):
    x, y, z = (int(i)+1 for i in line.split(','))
    grid[x][y][z] = 1
    all_blocks.add((x, y, z))

area = 0
dim = ((0, 0, -1), (0, -1, 0), (-1, 0, 0), (0, 0, 1), (0, 1, 0), (1, 0, 0))

grid[0][0][0] = 0
change_flag = True
while change_flag:
    change_flag = False
    for x in range(n):
        for y in range(n):
            for z in range(n):
                if grid[x][y][z] == 0:
                    continue
                if grid[x][y][z] == -1:
                    for dx, dy, dz in dim:
                        if x+dx < 0 or x+dx >= n or y+dy < 0 or y+dy >= n or z+dz < 0 or z+dz >= n:
                            continue
                        if grid[x+dx][y+dy][z+dz] == 0:
                            grid[x][y][z] = 0
                            change_flag = True
                            break

for x, y, z in all_blocks:
    for dx, dy, dz in dim:
        if x+dx < 0 or x+dx >= n or y+dy < 0 or y+dy >= n or z+dz < 0 or z+dz >= n:
            continue
        if grid[x+dx][y+dy][z+dz] == 0:
            area += 1

print(area)
