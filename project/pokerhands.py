import collections

# receives a card in the parameter and return an integer as value
def card_value(card):
    values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    return values[card[0]]


# This function takes a hand (a list of 5 cards) as input and returns its rank (an integer from 1 to 9, with 9 representing a straight flush and 1 representing a high card).
def rank_hand(hand):
    # numerical value for each card
    values = [card_value(card) for card in hand]

    # suit for each card
    suits = [card[1] for card in hand]

    # the number of occurrences of each card value and suit in the hand
    value_counts = collections.Counter(values)
    suit_counts = collections.Counter(suits)

    # checks for flush case, by checking if all suits are the same in that hand
    if len(suit_counts) == 1:
        flush = True
    else:
        flush = False

    sorted_values = sorted(values)

    # checks whether the difference between the highest ad lowest card values is  4(hand would be straight) and whether there are 5 distinct card values in the hand
    straight = (sorted_values[-1] - sorted_values[0] == 4) and (len(set(sorted_values)) == 5)

    # Sets a rank for the hand
    if straight and flush:
        rank = 9
    
    # if the hand contains 4 cards with the same value, its rank 8
    elif value_counts.most_common(1)[0][1] == 4:
        rank = 8

    # if the hand contains 3 cards with the same value and 2 cards with another value, its rank 7
    elif (value_counts.most_common(1)[0][1] == 3) and (value_counts.most_common(2)[1][1] == 2):
        rank = 7

    # if the hand is a flush(all cards have the same suit), its rank 6
    elif flush:
        rank = 6

    # if the hand is a straight(all cards have consecutive values), its rank 5
    elif straight:
        rank = 5

    # if the hand contains 3 cards of the same value, its rank 4
    elif (value_counts.most_common(1)[0][1] == 3):
        rank = 4

    # if the hand has 2 pairs of cards with the same value, its rank 3
    elif (value_counts.most_common(1)[0][1] == 2) and (value_counts.most_common(2)[1][1] == 2):
        rank = 3

    # if the hand has 1 pair of cards with the same value, its rank 2
    elif (value_counts.most_common(1)[0][1] == 2):
        rank = 2

    # if the card has a high value, its rank 1
    else:
        rank = 1
    print(value_counts.most_common(1)[0][1])
    return rank

# This function takes two hands as input and returns True or False. It determines each hand's value and compare them.
def compare_hands(hand1, hand2):
    rank1 = rank_hand(hand1)
    rank2 = rank_hand(hand2)
    # compare the hands
    if rank1 > rank2:
        return True
    elif rank2 > rank1:
        return False
    else:
        # The code below sorts each hand and compare card by card to determine the value, it returns tie if they have the same value
        for card1, card2 in zip(sorted(hand1, reverse=True), sorted(hand2, reverse=True)):
            if card_value(card1) > card_value(card2):
                return True
            elif card_value(card2) > card_value(card1):
                return False
        return 'Tie'


if __name__ == '__main__':
    with open('poker.txt') as f:
        # read the file
        hands = f.read().strip().split('\n')
        count = 0
        for hand in hands:
            # splits the hands and limit 5 hands for each round
            cards = hand.split()
            hand1 = cards[:5]
            hand2 = cards[5:]
            # compare hands
            if compare_hands(hand1, hand2) == True:
                count += 1

        print(count)
