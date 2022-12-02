game = """A Y
B X
C Z"""

BALANCE = {('A','X'):3, ('A','Y'):6, ('A','Z'):0, ('B','X'):0, ('B','Y'):3, ('B','Z'):6, ('C','X'):6, ('C','Y'):0, ('C','Z'):3}
FIFURA = {'X':1, 'Y':2, 'Z':3}

with open('input.txt', 'r') as f:
    game = f.read()
score = 0
for raund in game.split('\n'):
    if raund.strip() == '':
        break
    a, x = raund.strip().split(' ')
    score += FIFURA[x] + BALANCE[(a, x)]
print(score)