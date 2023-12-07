import os


def count_win(camel_cards):
    all_hands = []
    cards_weight = {
        "A": 12,
        "K": 11,
        "Q": 10,
        "J": 9,
        "T": 8,
        "9": 7,
        "8": 6,
        "7": 5,
        "6": 4,
        "5": 3,
        "4": 2,
        "3": 1,
        "2": 0,
    }
    for line in camel_cards.splitlines():
        hand, bid = line.split(" ")
        bid = int(bid)
        cards = dict()

        hands_weight = 0
        for card in hand:
            cards[card] = cards.get(card, 0) + 1
            hands_weight = hands_weight * 13 + cards_weight[card]

        if 5 in cards.values():
            hand_type = 7
        elif 4 in cards.values():
            hand_type = 6
        elif 3 in cards.values() and 2 in cards.values():
            hand_type = 5
        elif 3 in cards.values():
            hand_type = 4
        elif 2 in cards.values() and len(cards.values()) == 3:
            hand_type = 3
        elif 2 in cards.values() and len(cards.values()) == 4:
            hand_type = 2
        else:
            hand_type = 1

        all_hands.append((hand, bid, hand_type, hands_weight))

    all_hands.sort(key=lambda x: (x[2], x[3]))
    range = 1
    total_winnings = 0
    for _, bid, hand_type, hands_weight in all_hands:
        total_winnings += range * bid
        range += 1
    return total_winnings


test_camel_cards = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""
total_winnings = count_win(test_camel_cards)
assert total_winnings == 6440


input_file_path = os.path.dirname(os.path.realpath(__file__)) + "//input.txt"
with open(input_file_path) as fd:
    total_winnings = count_win(fd.read())
    print(total_winnings)
