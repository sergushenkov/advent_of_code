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
for bag in bags.split('\n'):
    part1 = set(i for i in bag[:len(bag)//2])
    part2 = set(i for i in bag[len(bag)//2:])
    common = part1 & part2
    if common:
        for i in common:
            result += things[i]
print(result)