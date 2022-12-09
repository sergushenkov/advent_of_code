input_string = '''R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
'''

input_string = '''R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
'''


def tail2head(head, tail):
    head_x, head_y = head
    tail_x, tail_y = tail
    if (abs(tail_x - head_x) + abs(tail_y - head_y)) > 2:
        if abs(tail_x - head_x) == 1:
            tail_x = head_x
        elif abs(tail_y - head_y) == 1:
            tail_y = head_y
    if abs(tail_x - head_x) > 1:
        tail_x = (tail_x + head_x) // 2
    if abs(tail_y - head_y) > 1:
        tail_y = (tail_y + head_y) // 2
    return (tail_x, tail_y)


with open('input.txt', 'r') as file:
    input_string = file.read()

direction = {'U': (0, 1), 'R': (1, 0), 'D': (0, -1), 'L': (-1, 0)}
knots = 10
rope = [(1, 1) for x in range(knots)]
points = {rope[-1]}
prevent_tail = rope[-1]

for line in input_string.split('\n'):
    if line.strip() == '':
        break
    when, size = line.strip().split()
    for _ in range(int(size)):
        dx, dy = direction[when]
        rope[0] = (rope[0][0] + dx, rope[0][1] + dy)
        for i in range(1, knots):
            rope[i] = tail2head(rope[i-1], rope[i])
        points.add(rope[-1])

print(len(points))  # 2391
print(rope)
