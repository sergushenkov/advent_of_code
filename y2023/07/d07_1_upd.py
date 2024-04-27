import os


class Hand:
    def __init__(self, str_hand):
        self.hands_weight = Hand.calculate_hands_weight(str_hand)
        self.combination = Hand.calculate_combination(str_hand)

    @staticmethod
    def calculate_hands_weight(str_hand):
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
        hands_weight = 0
        for card in str_hand:
            hands_weight = hands_weight * 13 + cards_weight[card]
        return hands_weight

    @staticmethod
    def calculate_combination(str_hand):
        cards = dict()
        for card in str_hand:
            cards[card] = cards.get(card, 0) + 1
        if 5 in cards.values():
            return 7
        if 4 in cards.values():
            return 6
        if 3 in cards.values() and 2 in cards.values():
            return 5
        if 3 in cards.values():
            return 4
        if 2 in cards.values() and len(cards.values()) == 3:
            return 3
        if 2 in cards.values() and len(cards.values()) == 4:
            return 2
        return 1


def count_win(camel_cards):
    all_hands = []

    for line in camel_cards.splitlines():
        str_hand, bid = line.split(" ")
        hand = Hand(str_hand)
        bid = int(bid)
        all_hands.append((hand.combination, hand.hands_weight, bid))

    all_hands.sort(key=lambda x: (x[0], x[1]))
    range = 1
    total_winnings = 0
    for _, _, bid in all_hands:
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
    camel_cards = fd.read()

total_winnings = count_win(camel_cards)
print(total_winnings)
