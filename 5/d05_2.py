input = '''    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
'''

with open('input.txt', 'r') as file:
    input = file.read()

row_count = 0
rows = input.split('\n')

for line in rows:
    row_count += 1
    if not (line.strip()[0].isdigit()):
        continue
    stack_count = len(line.strip().split('   '))
    break

stacks = []
for i in range(stack_count):
    stacks.append([])

for line in rows[row_count-2::-1]:
    stack = 0
    while stack < stack_count:
        if line[4*stack] == '[':
            crate = line[4*stack + 1]
            stacks[stack].append(crate)
        stack += 1

for line in rows[row_count + 1:]:
    if line == '':
        break
    _, move, _, from_stack, _, to_stack = line.split(' ')
    crate = []
    for i in range(int(move)):
        crate.append(stacks[int(from_stack) - 1].pop())
    for i in range(int(move)):
        stacks[int(to_stack) - 1].append(crate.pop())

for stack in stacks:
    print(stack.pop(), end='')
