import os


def count_benefits(cards):
    benefits = []
    for card in cards.splitlines():
        _, nums = card.split(": ")
        my_nums, win_nums = nums.split(" | ")
        win_card_number = len(set(my_nums.strip().replace("  ", " ").split(" ")) & set(win_nums.strip().replace("  ", " ").split(" "))) - 1
        card_bonus = 1 * 2 ** (win_card_number) if win_card_number >= 0 else 0
        benefits.append(card_bonus)
    return benefits


test_cards = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""
benefits = count_benefits(test_cards)
print(benefits)
assert sum(benefits) == 13


input_file_path = os.path.dirname(os.path.realpath(__file__)) + "//input.txt"
with open(input_file_path) as fd:
    benefits = count_benefits(fd.read())
    print(sum(benefits))
