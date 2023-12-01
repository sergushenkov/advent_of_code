bags = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

alfabet = 'abcdefghijklmnopqrstuvwxyz'
alfabet += alfabet.upper()
things = dict(zip(alfabet, range(1, 53)))

with open('input.txt', 'r') as fd:
    bags = fd.read()
result = 0
group = []
for bag in bags.split('\n'):
    group.append(set(i for i in bag))
    if len(group) < 3:
        continue
    common = group[0] & group[1] & group[2]
    if common:
        for i in common:
            result += things[i]
    group = []
print(result)
