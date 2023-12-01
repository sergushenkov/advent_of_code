input_string = '''[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]
'''.strip()

with open('input.txt', 'r') as file:
    input_string = file.read().strip()


def list_compare(a, b):
    if len(a) == 0 and len(b) == 0:
        return
    elif len(a) == 0 and len(b) > 0:
        return True
    elif len(b) == 0 and len(a) > 0:
        return False
    elif isinstance(a[0], int) and isinstance(b[0], int):
        if a[0] < b[0]:
            return True
        elif a[0] > b[0]:
            return False
    elif isinstance(a[0], int) and isinstance(b[0], list):
        a[0] = [a[0]]
        rezult = list_compare(a[0], b[0])
        if rezult is not None:
            return rezult
    elif isinstance(a[0], list) and isinstance(b[0], int):
        b[0] = [b[0]]
        rezult = list_compare(a[0], b[0])
        if rezult is not None:
            return rezult
    elif isinstance(a[0], list) and isinstance(b[0], list):
        rezult = list_compare(a[0], b[0])
        if rezult is not None:
            return rezult
    return list_compare(a[1:], b[1:])


packs = ['[[2]]', '[[6]]']
for pair in input_string.split('\n\n'):
    left, right = pair.split('\n')
    # left = eval(left)
    # right = eval(right)
    for new_pack in (left, right):
        for i in range(len(packs)):
            if list_compare(eval(new_pack), eval(packs[i])):
                a = packs[:i]
                a.append(new_pack)
                a.extend(packs[i:])
                packs = a
                break

print((packs.index('[[2]]') + 1) * (packs.index('[[6]]') + 1))
