input_string = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
"""

with open('input.txt', 'r') as file:
    input_string = file.read()

# monkey = [0:[things], 1:'anxiety_up', 2:check, 3:if_true, 4:if_false, 5:count_pass]
monkeys = []
for monkey_text in input_string.strip().split('\n\n'):
    _, line1, line2, line3, line4, line5 = monkey_text.split('\n')
    things = list(int(i) for i in line1.strip()[16:].split(', '))
    anxiety_up = line2.strip()[17:]
    check = int(line3.strip()[19:])
    if_true = int(line4.strip()[-1:])
    if_false = int(line5.strip()[-1:])
    monkeys.append([things, anxiety_up, check, if_true, if_false, 0])

for _ in range(20):
    for monkey in monkeys:
        things, anxiety_up, check, if_true, if_false, cnt = monkey
        monkey[5] += len(things)
        for old in things:
            new = eval(anxiety_up) // 3
            if new % check == 0:
                monkeys[if_true][0].append(new)
            else:
                monkeys[if_false][0].append(new)
        while len(things) > 0:
            things.pop()
monkeys = sorted(monkeys, key=lambda x: x[5], reverse=True)
print(monkeys[0][5] * monkeys[1][5])
