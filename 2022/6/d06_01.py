input = '''mjqjpqmgbljsphdztnvjfqwrcgsmlb'''

with open('input.txt', 'r') as file:
    input = file.read()

first = 4
last = 0
while first <= len(input):
    if len(set(input[last:first])) == 4:
        print(first)
        break
    first += 1
    last += 1
