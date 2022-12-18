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

# input_string = '''1,1,1
# 2,1,1
# '''

# with open('input.txt', 'r') as file:
#     input_string = file.read()

max_n = 5
min_n = 5
n = 25
all_blocks = set()
grid = [[[0 for z in range(-1, n)] for y in range(-1, n)]
        for x in range(-1, n)]
for line in input_string.strip().split('\n'):
    x, y, z = (int(i) for i in line.split(','))
    max_n = max(x, y, z, max_n)
    min_n = min(x, y, z, min_n)
    grid[x][y][z] = 1
    all_blocks.add((x, y, z))
# print(min_n, max_n)

area = 0
dim = ((0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0))
for x, y, z in all_blocks:
    for dx, dy, dz in dim:
        if x+dx < -1 or x+dx >= n or y+dy < -1 or y+dy >= n or z+dz < -1 or z+dz >= n:
            continue
        if grid[x+dx][y+dy][z+dz] == 0:
            area += 1

print(area)
