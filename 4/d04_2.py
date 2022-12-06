sections = '''2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8'''

with open('input.txt', 'r') as f:
    sections = f.read()

score = 0
for pair in sections.split('\n'):
    if pair.strip() == '':
        break
    (a, b), (c, d) = (x.split('-') for x in pair.split(','))
    first = {x for x in range(int(a), int(b) + 1)}
    second = {x for x in range(int(c), int(d) + 1)}
    if len(first & second) > 0:
        score += 1
    # print(first, second, score)
print(score)
