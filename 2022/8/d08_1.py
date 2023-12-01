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


def check_row(row):
    l = 0
    r = len(row) - 1
    left = row[l]
    right = row[r]
    high = {l, r}
    while (left < 9 or right < 9) and (l < r):
        if left > right:
            while row[r] <= right:
                r -= 1
            right = row[r]
            high.add(r)
        else:
            while left >= row[l] and (l < r):
                l += 1
            left = row[l]
            high.add(l)
    return high


def transposition(block):
    new_block = []
    for j in range(len(block[0])):
        row = []
        for i in range(len(block)):
            row.append(block[i][j])
        new_block.append(row)
    return new_block


with open('input.txt', 'r') as file:
    input = file.read()

map = create_map(input)
visible_map = []

for row in map:
    visible = check_row(row)
    visible_row = []
    for i in range(len(row)):
        if i in visible:
            visible_row.append(1)
        else:
            visible_row.append(0)
    visible_map.append(visible_row)


map = transposition(map)
visible_map = transposition(visible_map)

for i in range(len(map)):
    visible = check_row(map[i])
    for j in range(len(map[i])):
        if j in visible:
            visible_map[i][j] = 1

print(sum(sum(x) for x in visible_map))
