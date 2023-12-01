input_string = '''1
2
-3
3
-2
0
4
'''

with open('input.txt', 'r') as file:
    input_string = file.read()

line = [int(x) for x in input_string.strip().split('\n')]
numbers = line.copy()
length = len(line)

def shift_num(numbers, num):
    old_i = line.index(num)
    shift = num
    line.remove(num)
    while shift != 0:
        if shift > 0:
            shift -= 1
            old_i += 1
        else:
            shift += 1
            old_i -= 1
        if old_i <= 0:
            old_i += len(line)
        if old_i > len(line):
            old_i -= len(line)
    line.insert(old_i, num)

print(line)
for num in numbers:
    if num == 0:
        continue
    shift_num(numbers, num)
    # print(line)
zero = line.index(0)

first = line[(zero + 1000) % (length)]
second = line[(zero + 2000) % (length)]
thirth = line[(zero + 3000) % (length)]
print(first + second + thirth)