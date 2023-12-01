input = '''30373
25512
65332
33549
35390
'''


def create_map(input):
    map = []
    for line in input.split('\n'):
        if line.strip() == '':
            break
        map.append(list(int(x) for x in line))
    return map


with open('input.txt', 'r') as file:
    input = file.read()
map = create_map(input)
max_visio = 0

for i in range(1, len(map)-1):
    for j in range(1, len(map[0])-1):
        up = down = left = right = 0
        for x in range(i-1, -1, -1):
            up += 1
            if map[i][j] <= map[x][j]:
                break
        for x in range(i+1, len(map), 1):
            down += 1
            if map[i][j] <= map[x][j]:
                break
        for x in range(j-1, -1, -1):
            left += 1
            if map[i][j] <= map[i][x]:
                break
        for x in range(j+1, len(map[0]), 1):
            right += 1
            if map[i][j] <= map[i][x]:
                break
        if up * down * left * right > max_visio:
            max_visio = up * down * left * right

print(max_visio)
