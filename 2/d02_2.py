game = """A Y
B X
C Z"""

BALANCE = {('A', 'X'): 3, ('A', 'Y'): 1, ('A', 'Z'): 2, ('B', 'X'): 1,
           ('B', 'Y'): 2, ('B', 'Z'): 3, ('C', 'X'): 2, ('C', 'Y'): 3, ('C', 'Z'): 1}
FIFURA = {'X': 0, 'Y': 3, 'Z': 6}

with open('input.txt', 'r') as f:
    game = f.read()
score = 0
for raund in game.split('\n'):
    if raund.strip() == '':
        break
    a, x = raund.strip().split(' ')
    score += FIFURA[x] + BALANCE[(a, x)]
print(score)
