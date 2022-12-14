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


def find_most_calories_bug(elfs_calories):
    most_calories = 0
    for bug in elfs_calories:
        if most_calories < sum(bug):
            most_calories = sum(bug)
    return most_calories


with open('input.txt', 'r') as file:
    foods = file.read()
elfs_calories = read_list_of_food(foods)
print(f'most calories: {find_most_calories_bug(elfs_calories)}')
