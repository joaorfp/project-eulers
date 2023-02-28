def card_value(card):
    values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    return values[card[0]]

import collections

def rank_hand(hand):
    values = [card_value(card) for card in hand]
    suits = [card[1] for card in hand]

    value_counts = collections.Counter(values)
    suit_counts = collections.Counter(suits)

    if len(suit_counts) == 1:
        flush = True
    else:
        flush = False

    sorted_values = sorted(values)
    straight = (sorted_values[-1] - sorted_values[0] == 4) and (len(set(sorted_values)) == 5)

    if straight and flush:
        rank = 9
    elif value_counts.most_common(1)[0][1] == 4:
        rank = 8
    elif (value_counts.most_common(1)[0][1] == 3) and (value_counts.most_common(2)[1][1] == 2):
        rank = 7
    elif flush:
        rank = 6
    elif straight:
        rank = 5
    elif (value_counts.most_common(1)[0][1] == 3):
        rank = 4
    elif (value_counts.most_common(1)[0][1] == 2) and (value_counts.most_common(2)[1][1] == 2):
        rank = 3
    elif (value_counts.most_common(1)[0][1] == 2):
        rank = 2
    else:
        rank = 1
    return rank

def compare_hands(hand1, hand2):
    rank1 = rank_hand(hand1)
    rank2 = rank_hand(hand2)
    print(hand1, hand2)

    if rank1 > rank2:
        print('aaaaaaa')
        return True
    elif rank2 > rank1:
        return False
    else:
        for card1, card2 in zip(sorted(hand1, reverse=True), sorted(hand2, reverse=True)):
            if card_value(card1) > card_value(card2):
                return True
            elif card_value(card2) > card_value(card1):
                return False
        return 'Tie'

    
if __name__ == '__main__':
    with open('poker.txt') as f:
        hands = f.read().strip().split('\n')
        count = 0
        for hand in hands:
            cards = hand.split()
            hand1 = cards[:5]
            hand2 = cards[5:]
            if compare_hands(hand1, hand2) == True:
                count += 1

        print(count)
