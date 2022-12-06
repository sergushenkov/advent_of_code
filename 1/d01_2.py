foods = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""


def read_list_of_food(foods):
    elfs_calories = []
    elf_bug = []
    for line in foods.strip().split('\n'):
        if line.strip().isdigit():
            elf_bug.append(int(line))
        else:
            elfs_calories.append(elf_bug)
            elf_bug = []
    if elf_bug != []:
        elfs_calories.append(elf_bug)
    return elfs_calories


def calc_sum_calories(elfs_calories):
    all_calories = []
    for bug in elfs_calories:
        all_calories.append(sum(bug))
    return all_calories


with open('input.txt', 'r') as file:
    foods = file.read()
elfs_calories = read_list_of_food(foods)
all_calories = calc_sum_calories(elfs_calories)
all_calories.sort(reverse=True)
print(f'three most calories: {sum(all_calories[:3])}')
