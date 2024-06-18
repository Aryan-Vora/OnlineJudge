import sys
from itertools import combinations

lines = sys.stdin.read().split('\n')
names = ["highest-card", "one-pair", "two-pairs", "three-of-a-kind", "straight", "flush",
         "full-house", "four-of-a-kind", "straight-flush", "royal-flush"]


def score(hand):
    ranks = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
             '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

    hand_ranks = [ranks[card[0]] for card in hand]
    hand_suits = [card[1] for card in hand]
    hand_ranks.sort(reverse=True)
    flush = len(set(hand_suits)) == 1
    straight = len(set(hand_ranks)) == 5 and (max(
        hand_ranks) - min(hand_ranks) == 4 or set(hand_ranks) == set([14, 2, 3, 4, 5]))
    counts = [hand_ranks.count(rank) for rank in set(hand_ranks)]
    four_of_a_kind = 4 in counts
    three_of_a_kind = 3 in counts
    pairs = counts.count(2)
    if straight and flush:
        return 8  # Straight flush
    elif four_of_a_kind:
        return 7  # Four of a kind
    elif three_of_a_kind and pairs == 1:
        return 6  # Full house
    elif flush:
        return 5  # Flush
    elif straight:
        return 4  # Straight
    elif three_of_a_kind:
        return 3  # Three of a kind
    elif pairs == 2:
        return 2  # Two pair
    elif pairs == 1:
        return 1  # One pair
    else:
        return 0  # High card


for line in lines:
    if line == "":
        break
    cards = line.split(" ")
    hand = cards[:5]
    deck = cards[5:]
    highest_score = 0
    # start by taking the hand and checking score
    # then remove 1 card from hand and add the top card from deck
    # then remove 2 cards and add the top 2 from deck note this has to have every combination of 2 cards removed so 5 choose 2
    # do same for 3 4 and 5
    for num_draw in range(6):
        for discard in combinations(hand, num_draw):
            new_hand = [
                card for card in hand if card not in discard] + deck[:num_draw]
            score_ = score(new_hand)
            if score_ > highest_score:
                highest_score = score_

    print("Hand: " + " ".join(hand) + " Deck: " +
          " ".join(deck) + " Best hand: " + names[highest_score])
