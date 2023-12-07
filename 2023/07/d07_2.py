import os


def count_win(camel_cards):
    all_hands = []
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
    for line in camel_cards.splitlines():
        hand, bid = line.split(" ")
        bid = int(bid)
        cards = dict()

        hands_weight = 0
        for card in hand:
            cards[card] = cards.get(card, 0) + 1
            hands_weight = hands_weight * 13 + cards_weight[card]

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

        if first_other_card + J_number == 5:
            hand_type = 7
        elif first_other_card + J_number == 4:
            hand_type = 6
        elif first_other_card + J_number == 3 and second_other_card == 2:
            hand_type = 5
        elif first_other_card + J_number == 3:
            hand_type = 4
        elif first_other_card + J_number == 2 and second_other_card == 2:
            hand_type = 3
        elif first_other_card + J_number == 2:
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
assert total_winnings == 5905


input_file_path = os.path.dirname(os.path.realpath(__file__)) + "//input.txt"
with open(input_file_path) as fd:
    total_winnings = count_win(fd.read())
    print(total_winnings)
