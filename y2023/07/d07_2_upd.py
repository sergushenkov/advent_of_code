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
            "T": 9,
            "9": 8,
            "8": 7,
            "7": 6,
            "6": 5,
            "5": 4,
            "4": 3,
            "3": 2,
            "2": 1,
            "J": 0,
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
        J_number, first_other_card, second_other_card = Hand.active_cards(cards)
        if first_other_card + J_number == 5:
            return 7
        if first_other_card + J_number == 4:
            return 6
        if first_other_card + J_number == 3 and second_other_card == 2:
            return 5
        if first_other_card + J_number == 3:
            return 4
        if first_other_card + J_number == 2 and second_other_card == 2:
            return 3
        if first_other_card + J_number == 2:
            return 2
        return 1

    @staticmethod
    def active_cards(cards):
        J_number = cards.get("J", 0)
        other_card = [x for x in cards.values()]
        if J_number > 0:
            other_card.remove(J_number)

        first_other_card = 0
        if other_card:
            first_other_card = max(other_card)
            other_card.remove(first_other_card)

        second_other_card = 0
        if other_card:
            second_other_card = max(other_card)
            other_card.remove(second_other_card)
        return J_number, first_other_card, second_other_card


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
assert total_winnings == 5905


input_file_path = os.path.dirname(os.path.realpath(__file__)) + "//input.txt"
with open(input_file_path) as fd:
    camel_cards = fd.read()

total_winnings = count_win(camel_cards)
print(total_winnings)
