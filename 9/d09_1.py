input_string = '''R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
'''

with open('input.txt', 'r') as file:
    input_string = file.read()

direction = {'U': (0, 1), 'R': (1, 0), 'D': (0, -1), 'L': (-1, 0)}
head_x = head_y = tail_x = tail_y = 1
points = {(tail_x, tail_y)}

for line in input_string.split('\n'):
    if line.strip() == '':
        break
    when, size = line.strip().split()
    for _ in range(int(size)):
        dx, dy = direction[when]
        head_x += dx
        head_y += dy
        if (abs(tail_x - head_x) + abs(tail_y - head_y)) > 2:
            if abs(tail_x - head_x) == 1:
                tail_x = head_x
            else:
                tail_y = head_y
        if abs(tail_x - head_x) > 1:
            tail_x = (tail_x + head_x) // 2
        if abs(tail_y - head_y) > 1:
            tail_y = (tail_y + head_y) // 2
        points.add((tail_x, tail_y))
print(len(points))
